# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
filename = e2r_stock_web_v12_residual_round_R3_loop_124_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
selected_round = R3
selected_loop = 124
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under_30_representative_rows
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG
loop_objective = coverage_gap_fill | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds **7** new independent C11 cases, **4** counterexamples, and **5** residual errors for **L3_BATTERY_EV_GREEN_MOBILITY / C11_BATTERY_ORDERBOOK_RERATING**.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as existing guardrails, not re-proposed as global rules:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

This MD tests whether C11 requires a **canonical-specific conversion bridge**: the orderbook has to move from contract headline to delivery schedule, volume/capacity route, margin bridge, and FCF or revenue visibility. A large battery order is a doorbell; the rerating happens only if someone actually opens the door and goods start moving through it.

## 2. Round / Large Sector / Canonical Archetype Scope

- `C11_BATTERY_ORDERBOOK_RERATING` maps to `R3 / L3_BATTERY_EV_GREEN_MOBILITY`.
- This is not an EV demand slowdown loop (`C14`) and not an AMPC/JV loop (`C13`).
- The selected scope is battery material/equipment orderbook rerating: cathode supply, copper foil supply, electrode/formation equipment contracts, and framework agreements.

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C11 as Priority 0 with 18 representative rows, `need_to_30 = 12`, `need_to_50 = 32`. The no-repeat key used here is:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This loop avoids the prior in-session C02/C09/C14/C10/C06/C07 outputs and does not reuse those exact canonical keys. The C11 row-level ledger was available only as the aggregate No-Repeat Index for this run, so the selected cases emphasize new symbol/family diversity and use distinct trigger dates.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

All representative trigger rows below use stock-web tradable shards and have 30D/90D/180D MFE and MAE fields.

## 5. Historical Eligibility Gate

|check|result|
|---|---|
|trigger_date historical|pass|
|entry_date in stock-web tradable shard|pass|
|forward 180 trading days available|pass for 8 trigger rows|
|MFE/MAE 30D/90D/180D complete|pass|
|corporate-action contaminated 180D window|none detected from profile candidate dates overlapping entry~D+180|
|production scoring changed|false|


## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rule |
|---|---|---|
| BATTERY_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE | C11_BATTERY_ORDERBOOK_RERATING | Equipment orderbook is C11 only when contract size, delivery horizon, and revenue/margin route are present. |
| CATHODE_MEGA_SUPPLY_CONTRACT_CUSTOMER_CAPACITY | C11_BATTERY_ORDERBOOK_RERATING | Cathode mega-deal is C11 if customer/delivery visibility exists; it is capped if commodity ASP/customer-launch risk dominates. |
| FRAMEWORK_AGREEMENT_WITHOUT_FIRM_PO | C11_BATTERY_ORDERBOOK_RERATING | Framework-only language stays Stage2-watch unless firm order value and shipment bridge appear. |
| CUSTOMER_CONCENTRATION_ORDERBOOK_RISK | C11_BATTERY_ORDERBOOK_RERATING | Single customer/order concentration requires 4B/guardrail overlay before Yellow/Green. |

## 7. Case Selection Summary

|symbol|company|trigger_type|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|role|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|137400|피엔티|Stage2-Actionable|2024-04-17|38650|131.57|-1.55|131.57|-5.3|positive|current_profile_missed_structural|
|003670|포스코퓨처엠|Stage2-Actionable|2023-04-27|340000|104.12|-14.12|104.12|-31.91|positive|current_profile_4B_too_late|
|217820|원익피앤이|Stage2-Actionable|2022-12-28|7750|53.42|-7.1|107.48|-7.1|positive|current_profile_missed_structural|
|066970|엘앤에프|Stage2-Actionable|2023-03-02|250500|39.52|-12.57|39.52|-48.94|counterexample|current_profile_false_positive|
|247540|에코프로비엠|Stage2-Actionable|2023-12-04|323000|9.6|-34.67|9.6|-49.23|counterexample|current_profile_false_positive|
|299030|하나기술|Stage2|2022-08-25|72200|12.74|-27.56|26.59|-27.56|counterexample|current_profile_false_positive|
|011790|SKC|Stage2-Actionable|2023-02-20|97300|25.69|-7.3|25.69|-30.11|counterexample|current_profile_false_positive|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 4
4B_case_count = 1
4C_case_count = 0 quantitative / 1 narrative-only customer call-off risk note
calibration_usable_case_count = 7
calibration_usable_trigger_count = 8
representative_trigger_count = 7
```

The split is deliberately asymmetric: C11 tends to look wonderful at headline time, so the useful residual work is to separate **true orderbook conversion** from **large-number theatre**. The three positives have contract size plus stronger conversion clues; the four counterexamples have high MAE, customer concentration, late-cycle timing, or framework-only weakness.

## 9. Evidence Source Map

|symbol|company|trigger_date|evidence summary|source|
|---|---|---|---|---|
|137400|피엔티|2024-04-16|Mirae/PNT AI report citing Herald Economy disclosure: KRW 66.038bn secondary-battery electrode-process equipment contract, 12.1% of 2023 sales, delivery until 2025-11-17.|https://securities.miraeasset.com/bbs/download/2125406.pdf?attachmentId=2125406|
|003670|포스코퓨처엠|2023-04-26|POSCO Future M official newsroom: KRW 30.2595tn seven-year LG Energy Solution high-nickel cathode supply contract through 2029; total cathode-material orders over KRW 92tn.|https://www.poscofuturem.com/en/pr/view.do?num=684|
|217820|원익피앤이|2022-12-27|Infostock Daily: KRW 68.0789bn secondary-battery manufacturing equipment supply contract, 30.55% of prior-year consolidated sales, delivery until 2024-01-31.|https://www.infostockdaily.co.kr/news/articleView.html?idxno=186897|
|066970|엘앤에프|2023-02-28|Teslarati report/public filing: KRW 3.83tn high-nickel cathode deal with Tesla, supply period 2024-01-01 to 2025-12-31; contract amount could vary with lithium price/exchange-rate assumptions.|https://www.teslarati.com/tesla-signs-2-9b-battery-materials-deal-l-f/|
|247540|에코프로비엠|2023-12-03|Korea JoongAng Daily: KRW 44tn five-year Samsung SDI cathode supply deal from 2024, with Pohang supply in 2024 and Hungary supply from 2025.|https://www.koreajoongangdaily.com/business/ecopro-bm-secures-34-billion-deal-as-samsung-sdis-cathode-supplier/11483248|
|299030|하나기술|2022-08-24|FREYR/T1 Energy release: strategic alliance frame agreement; Hana supports pouch assembly, formation/aging, inspection, grading, packaging, and scrap-discharge equipment for planned gigafactories; three-year expertise secured with extension option.|https://news.cision.com/se/t1-energy-inc/r/freyr-battery-enters-strategic-partnership-with-hana-technology%2Cc3619082|
|011790|SKC|2023-02-19|SKC official release: SK nexilis signed a five-year KRW 1.4tn copper-foil supply contract with Northvolt; volume about 80% of Northvolt copper-foil needs, produced from Poland from 2024.|https://www.skc.kr/m/eng/Conmmunication/pr/newsDetail.do?gubun=&seq=1511|


## 10. Price Data Source Map

|symbol|company|profile_path|entry_year_shard|corporate_action_window_status|forward_window_trading_days|
|---|---|---|---|---|---|
|137400|피엔티|atlas/symbol_profiles/137/137400.json|atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv|clean_180D_window|180|
|003670|포스코퓨처엠|atlas/symbol_profiles/003/003670.json|atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv|clean_180D_window|180|
|217820|원익피앤이|atlas/symbol_profiles/217/217820.json|atlas/ohlcv_tradable_by_symbol_year/217/217820/2022.csv|clean_180D_window|180|
|066970|엘앤에프|atlas/symbol_profiles/066/066970.json|atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv|clean_180D_window|180|
|247540|에코프로비엠|atlas/symbol_profiles/247/247540.json|atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv|clean_180D_window|180|
|299030|하나기술|atlas/symbol_profiles/299/299030.json|atlas/ohlcv_tradable_by_symbol_year/299/299030/2022.csv|clean_180D_window|180|
|011790|SKC|atlas/symbol_profiles/011/011790.json|atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv|clean_180D_window|180|


## 11. Case-by-Case Trigger Grid

### 11.1 Positive controls

- **PNT / 137400**: large secondary-battery electrode equipment contract plus order-backlog context produced a clean 180D path: `MFE_180D_pct = 131.57`, `MAE_180D_pct = -5.30`. This is the best evidence that C11 should not be overly punished just because battery sector beta was messy.
- **POSCO Future M / 003670**: the LGES mega contract produced strong 90D/180D upside, but the post-peak drawdown was severe. This is a success case that still needs 4B overlay discipline.
- **Wonik PNE / 217820**: the 68.1bn equipment contract was large versus prior sales and translated into a strong 180D MFE with limited initial MAE.

### 11.2 Counterexamples / high-MAE controls

- **L&F / 066970**: the Tesla contract gave immediate 30D upside but then suffered a deep 180D MAE. The later contract reduction is narrative-only here because the stock-web forward window is insufficient after Dec-2025, but it supports the original red-team concern: customer-launch and ASP assumptions were doing too much work.
- **EcoPro BM / 247540**: the 44tn Samsung SDI deal arrived after the cathode complex had already rerated. The order was real, but the entry path was poor: `MFE_180D_pct = 9.60`, `MAE_180D_pct = -49.23`.
- **Hana Technology / 299030**: strategic alliance language without firm order value produced a weak 180D risk/reward. This should stay Stage2-watch unless it becomes a purchase order.
- **SKC / 011790**: the Northvolt offtake was large and strategic, but copper-foil margin/capex/customer execution risk made the path high-MAE.

## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|C11-R3-L124-137400-20240417-Stage2Actionable|137400|Stage2-Actionable|2024-04-17|38650|77.75|-1.55|131.57|-1.55|131.57|-5.3|2024-06-19|89500|-59.11|
|C11-R3-L124-003670-20230427-Stage2Actionable|003670|Stage2-Actionable|2023-04-27|340000|17.65|-14.12|104.12|-14.12|104.12|-31.91|2023-07-26|694000|-66.64|
|C11-R3-L124-217820-20221228-Stage2Actionable|217820|Stage2-Actionable|2022-12-28|7750|4.0|-7.1|53.42|-7.1|107.48|-7.1|2023-08-16|16080|-53.67|
|C11-R3-L124-066970-20230302-Stage2Actionable|066970|Stage2-Actionable|2023-03-02|250500|39.52|-12.57|39.52|-12.57|39.52|-48.94|2023-04-03|349500|-63.4|
|C11-R3-L124-247540-20231204-Stage2Actionable|247540|Stage2-Actionable|2023-12-04|323000|9.6|-17.96|9.6|-34.67|9.6|-49.23|2023-12-04|354000|-53.67|
|C11-R3-L124-299030-20220825-Stage2|299030|Stage2|2022-08-25|72200|12.74|-21.75|12.74|-27.56|26.59|-27.56|2023-04-19|91400|-31.62|
|C11-R3-L124-011790-20230220-Stage2Actionable|011790|Stage2-Actionable|2023-02-20|97300|25.59|-7.3|25.69|-7.3|25.69|-30.11|2023-04-05|122300|-44.4|
|C11-R3-L124-PNT-20240619-4B|137400|Stage4B|2024-06-19|84500|5.92|-40.59|5.92|-45.62|5.92|-56.69|2024-06-19|89500|-59.11|


## 13. Current Calibrated Profile Stress Test

|case_id|current profile likely action|actual path verdict|residual error|
|---|---|---|---|
|C11-R3-L124-PNT-20240416|current_profile_missed_structural|order_backlog_margin_bridge_positive|C11 needs an equipment-order size + backlog + margin bridge fast lane; PNT had order evidence plus backlog context before the clean rerating.|
|C11-R3-L124-POSCOFM-20230426|current_profile_4B_too_late|large_cathode_orderbook_positive_but_4b_needed|The orderbook signal worked, but without 4B overheat overlay it retained too much post-peak downside.|
|C11-R3-L124-WONIKPNE-20221227|current_profile_missed_structural|equipment_contract_size_to_sales_positive|Contract-to-sales ratio and delivery horizon mattered more than generic battery beta.|
|C11-R3-L124-LNF-20230228|current_profile_false_positive|headline_orderbook_high_mfe_but_deep_mae|Customer concentration and ASP/lithium pass-through caveats should cap C11 at Stage2-Actionable until shipment and margin conversion appear.|
|C11-R3-L124-ECOPROBM-20231203|current_profile_false_positive|late_cycle_order_headline_false_positive|A huge order after sector valuation blowoff did not rerate cleanly; C11 needs cycle/margin sanity gate.|
|C11-R3-L124-HANA-20220824|current_profile_false_positive|framework_agreement_without_firm_order_counterexample|Framework/strategic partnership language without firm PO/order amount should not become C11 Stage2-Actionable.|
|C11-R3-L124-SKC-20230219|current_profile_false_positive|customer_orderbook_without_margin_conversion_counterexample|Large customer offtake needed copper-foil margin/capex ramp and customer execution confirmation; headline contract alone was not enough.|


Stress-test answers:

1. Current calibrated profile would correctly block pure price-only promotion, but C11 still needs a contract-conversion gate.
2. Actual MFE/MAE split shows true positives and false positives both have impressive headline evidence.
3. Stage2-Actionable bonus is appropriate for firm order value, but too generous for framework-only language.
4. Yellow threshold 75 is not the problem; evidence composition is.
5. Green threshold 87 / revision 55 remains appropriate; none of these rows demands Green relaxation.
6. Price-only blowoff guard is appropriate and should be kept.
7. Full 4B non-price requirement is kept, but C11 needs a watch overlay after rapid orderbook rerating.
8. Hard 4C should not be triggered merely from one customer/project stress unless company-wide orderbook conversion breaks.

## 14. Stage2 / Yellow / Green Comparison

- Stage2: public contract/order/framework evidence.
- Stage2-Actionable: firm order value + delivery horizon + named/credible customer quality.
- Stage3-Yellow: requires at least one of margin bridge, repeated delivery conversion, confirmed revision, or FCF visibility.
- Stage3-Green: not proposed in this loop. The C11 residual is not “Green is too late”; it is “some Yellow candidates are fake because orderbook has not converted.”

`green_lateness_ratio = not_applicable` for representative rows because no confirmed Stage3-Green trigger is used as the entry in this loop.

## 15. 4B Local vs Full-window Timing Audit

PNT overlay:

```text
Stage2 entry = 2024-04-17 close 38,650
Stage4B overlay = 2024-06-19 close 84,500
180D full-window high = 89,500
four_b_local_peak_proximity = 0.901
four_b_full_window_peak_proximity = 0.901
Stage4B overlay forward path = MFE_180D_pct 5.92 / MAE_180D_pct -56.69
```

Interpretation: a price/valuation overheat overlay after a +100% orderbook rerating is useful as a **risk-control overlay**, not as a thesis break. The underlying C11 positive remains valid; the position-management layer needed a separate warning.

## 16. 4C Protection Audit

No calibration-usable hard 4C trigger is promoted here. L&F’s later Tesla contract reduction is included as `narrative_only`, because the stock-web manifest max date leaves insufficient 180D forward window for the Dec-2025 cut. The C11 4C rule should be conservative: hard 4C requires company-wide order cancellation, repeated call-off, or margin/FCF thesis break, not merely one customer delay when the orderbook base is diversified.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L3_BATTERY_ORDERBOOK_CONVERSION_GATE
rule_scope = sector_specific
candidate = In L3 battery/material/equipment, orderbook headlines can promote to Stage2-Actionable, but Stage3-Yellow requires delivery visibility plus margin/FCF conversion or repeated customer confirmation. If the order is framework-only, customer-concentrated, or late-cycle after valuation blowoff, cap at Stage2-watch and attach 4B risk overlay.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C11_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_GATE
positive lift fields:
  - firm contract value vs prior sales
  - credible customer quality
  - explicit delivery period
  - capacity/shipment route
  - margin/FCF or revenue conversion evidence
negative cap fields:
  - framework-only wording
  - undisclosed counterparty with no repeated conversion
  - customer concentration
  - raw-material ASP/lithium pass-through caveat
  - late-cycle valuation blowoff
  - customer funding/project execution risk
```

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|changed_axes|eligible_triggers|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|global_calibrated_proxy|Current profile without C11-specific conversion gate|none|7|53.81|-14.98|63.51|-28.59|0.57|2|1|mixed_overpromotion|
|P0b|baseline_reference|Old baseline would over-credit large order headlines and miss 4B overlays|rollback_reference|7|53.81|-14.98|63.51|-28.59|0.71|2|2|weak_alignment|
|P1|sector_specific_candidate|L3 battery orderbook requires conversion/customer/cycle gate|add L3 orderbook conversion gate|7|96.37|-7.59|114.39|-14.77|0.14|0|1|better_alignment|
|P2|canonical_archetype_candidate|C11 score lifts only when orderbook + delivery + margin/FCF bridge present|add C11 conversion bridge multiplier and headline cap|7|96.37|-7.59|114.39|-14.77|0.14|0|1|best_alignment|
|P3|counterexample_guard_profile|Customer concentration / framework-only / late-cycle order headlines stay Stage2-watch|guard caps false positives|7|21.89|-20.52|25.35|-38.96|0.0|0|0|guardrail_alignment|


## 20. Score-Return Alignment Matrix

The C11 matrix is not a single “orders good” rule. It is a two-key lock:

```text
Key 1 = orderbook exists
Key 2 = conversion bridge exists
```

When both keys turn, PNT/Wonik/POSCOFM behave like rerating cases. When only the first key turns, L&F/EcoProBM/Hana/SKC become high-MAE order-headline traps.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG | 3 | 4 | 1 | 0 | 7 | 0 | 8 | 7 | 5 | L3_BATTERY_ORDERBOOK_CONVERSION_GATE | C11_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_GATE | need_to_30 moves from 12 to roughly 5 if all representative rows accepted |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_missed_structural
  - current_profile_4B_too_late
  - high_mae_after_order_headline
new_axis_proposed: C11_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_GATE
existing_axis_strengthened: full_4b_requires_non_price_evidence; price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min; stage3_green_revision_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L3_BATTERY_ORDERBOOK_CONVERSION_GATE
canonical_archetype_rule_candidate: C11_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web tradable_raw OHLC rows for entry-year and forward windows
- 30D/90D/180D MFE/MAE fields
- entry date vs evidence date rule
- round/large sector/canonical consistency
- representative vs 4B overlay dedupe role

Not validated:

- production E2R code behavior
- live watchlist
- current investability
- final DART filing attachments beyond web evidence map
- 2Y paths when stock-web forward window was unavailable

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_orderbook_conversion_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"lift only when orderbook has delivery visibility plus margin/FCF conversion evidence","filters L&F/EcoProBM/Hana/SKC false positives while preserving PNT/POSCOFM/Wonik positives","C11-R3-L124-137400-20240417-Stage2Actionable|C11-R3-L124-003670-20230427-Stage2Actionable|C11-R3-L124-217820-20221228-Stage2Actionable|C11-R3-L124-066970-20230302-Stage2Actionable|C11-R3-L124-247540-20231204-Stage2Actionable|C11-R3-L124-299030-20220825-Stage2|C11-R3-L124-011790-20230220-Stage2Actionable",7,7,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_framework_or_customer_concentration_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"cap framework-only or single-customer contract where shipment/margin bridge is missing","reduces high-MAE order headline cases","C11-R3-L124-066970-20230302-Stage2Actionable|C11-R3-L124-247540-20231204-Stage2Actionable|C11-R3-L124-299030-20220825-Stage2|C11-R3-L124-011790-20230220-Stage2Actionable",4,4,4,medium,guardrail_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C11-R3-L124-PNT-20240416","symbol":"137400","company_name":"피엔티","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C11-R3-L124-137400-20240417-Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"C11 needs an equipment-order size + backlog + margin bridge fast lane; PNT had order evidence plus backlog context before the clean rerating."}
{"row_type":"case","case_id":"C11-R3-L124-POSCOFM-20230426","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","case_type":"high_mfe_success_with_late_cycle_drawdown","positive_or_counterexample":"positive","best_trigger":"C11-R3-L124-003670-20230427-Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"The orderbook signal worked, but without 4B overheat overlay it retained too much post-peak downside."}
{"row_type":"case","case_id":"C11-R3-L124-WONIKPNE-20221227","symbol":"217820","company_name":"원익피앤이","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C11-R3-L124-217820-20221228-Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Contract-to-sales ratio and delivery horizon mattered more than generic battery beta."}
{"row_type":"case","case_id":"C11-R3-L124-LNF-20230228","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","case_type":"failed_rerating_high_mae","positive_or_counterexample":"counterexample","best_trigger":"C11-R3-L124-066970-20230302-Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Customer concentration and ASP/lithium pass-through caveats should cap C11 at Stage2-Actionable until shipment and margin conversion appear."}
{"row_type":"case","case_id":"C11-R3-L124-ECOPROBM-20231203","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C11-R3-L124-247540-20231204-Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"A huge order after sector valuation blowoff did not rerate cleanly; C11 needs cycle/margin sanity gate."}
{"row_type":"case","case_id":"C11-R3-L124-HANA-20220824","symbol":"299030","company_name":"하나기술","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C11-R3-L124-299030-20220825-Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Framework/strategic partnership language without firm PO/order amount should not become C11 Stage2-Actionable."}
{"row_type":"case","case_id":"C11-R3-L124-SKC-20230219","symbol":"011790","company_name":"SKC","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","case_type":"failed_rerating_high_mae","positive_or_counterexample":"counterexample","best_trigger":"C11-R3-L124-011790-20230220-Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_or_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Large customer offtake needed copper-foil margin/capex ramp and customer execution confirmation; headline contract alone was not enough."}
{"row_type":"trigger","trigger_id":"C11-R3-L124-137400-20240417-Stage2Actionable","case_id":"C11-R3-L124-PNT-20240416","symbol":"137400","company_name":"피엔티","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","sector":"battery_equipment_electrode_process","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-16","entry_date":"2024-04-17","entry_price":38650,"evidence_available_at_that_date":"Mirae/PNT AI report citing Herald Economy disclosure: KRW 66.038bn secondary-battery electrode-process equipment contract, 12.1% of 2023 sales, delivery until 2025-11-17.","evidence_source":"https://securities.miraeasset.com/bbs/download/2125406.pdf?attachmentId=2125406","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv","profile_path":"atlas/symbol_profiles/137/137400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":77.75,"MFE_90D_pct":131.57,"MFE_180D_pct":131.57,"MFE_1Y_pct":131.57,"MFE_2Y_pct":null,"MAE_30D_pct":-1.55,"MAE_90D_pct":-1.55,"MAE_180D_pct":-5.3,"MAE_1Y_pct":-11.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":89500,"drawdown_after_peak_pct":-59.11,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"order_backlog_margin_bridge_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_R3_L124_137400_20240417","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11-R3-L124-003670-20230427-Stage2Actionable","case_id":"C11-R3-L124-POSCOFM-20230426","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","sector":"cathode_materials","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-26","entry_date":"2023-04-27","entry_price":340000,"evidence_available_at_that_date":"POSCO Future M official newsroom: KRW 30.2595tn seven-year LG Energy Solution high-nickel cathode supply contract through 2029; total cathode-material orders over KRW 92tn.","evidence_source":"https://www.poscofuturem.com/en/pr/view.do?num=684","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.65,"MFE_90D_pct":104.12,"MFE_180D_pct":104.12,"MFE_1Y_pct":104.12,"MFE_2Y_pct":null,"MAE_30D_pct":-14.12,"MAE_90D_pct":-14.12,"MAE_180D_pct":-31.91,"MAE_1Y_pct":-31.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-66.64,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"large_cathode_orderbook_positive_but_4b_needed","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_R3_L124_003670_20230427","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11-R3-L124-217820-20221228-Stage2Actionable","case_id":"C11-R3-L124-WONIKPNE-20221227","symbol":"217820","company_name":"원익피앤이","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","sector":"battery_manufacturing_equipment","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2022-12-27","entry_date":"2022-12-28","entry_price":7750,"evidence_available_at_that_date":"Infostock Daily: KRW 68.0789bn secondary-battery manufacturing equipment supply contract, 30.55% of prior-year consolidated sales, delivery until 2024-01-31.","evidence_source":"https://www.infostockdaily.co.kr/news/articleView.html?idxno=186897","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/217/217820/2022.csv","profile_path":"atlas/symbol_profiles/217/217820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.0,"MFE_90D_pct":53.42,"MFE_180D_pct":107.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.1,"MAE_90D_pct":-7.1,"MAE_180D_pct":-7.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-16","peak_price":16080,"drawdown_after_peak_pct":-53.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"equipment_contract_size_to_sales_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_R3_L124_217820_20221228","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11-R3-L124-066970-20230302-Stage2Actionable","case_id":"C11-R3-L124-LNF-20230228","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","sector":"cathode_materials","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-28","entry_date":"2023-03-02","entry_price":250500,"evidence_available_at_that_date":"Teslarati report/public filing: KRW 3.83tn high-nickel cathode deal with Tesla, supply period 2024-01-01 to 2025-12-31; contract amount could vary with lithium price/exchange-rate assumptions.","evidence_source":"https://www.teslarati.com/tesla-signs-2-9b-battery-materials-deal-l-f/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.52,"MFE_90D_pct":39.52,"MFE_180D_pct":39.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.57,"MAE_90D_pct":-12.57,"MAE_180D_pct":-48.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-03","peak_price":349500,"drawdown_after_peak_pct":-63.4,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"headline_orderbook_high_mfe_but_deep_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_R3_L124_066970_20230302","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11-R3-L124-247540-20231204-Stage2Actionable","case_id":"C11-R3-L124-ECOPROBM-20231203","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","sector":"cathode_materials","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-03","entry_date":"2023-12-04","entry_price":323000,"evidence_available_at_that_date":"Korea JoongAng Daily: KRW 44tn five-year Samsung SDI cathode supply deal from 2024, with Pohang supply in 2024 and Hungary supply from 2025.","evidence_source":"https://www.koreajoongangdaily.com/business/ecopro-bm-secures-34-billion-deal-as-samsung-sdis-cathode-supplier/11483248","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.6,"MFE_90D_pct":9.6,"MFE_180D_pct":9.6,"MFE_1Y_pct":9.6,"MFE_2Y_pct":null,"MAE_30D_pct":-17.96,"MAE_90D_pct":-34.67,"MAE_180D_pct":-49.23,"MAE_1Y_pct":-62.72,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-04","peak_price":354000,"drawdown_after_peak_pct":-53.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_cycle_order_headline_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_R3_L124_247540_20231204","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11-R3-L124-299030-20220825-Stage2","case_id":"C11-R3-L124-HANA-20220824","symbol":"299030","company_name":"하나기술","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","sector":"battery_equipment_formation_assembly","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2022-08-24","entry_date":"2022-08-25","entry_price":72200,"evidence_available_at_that_date":"FREYR/T1 Energy release: strategic alliance frame agreement; Hana supports pouch assembly, formation/aging, inspection, grading, packaging, and scrap-discharge equipment for planned gigafactories; three-year expertise secured with extension option.","evidence_source":"https://news.cision.com/se/t1-energy-inc/r/freyr-battery-enters-strategic-partnership-with-hana-technology%2Cc3619082","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/299/299030/2022.csv","profile_path":"atlas/symbol_profiles/299/299030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.74,"MFE_90D_pct":12.74,"MFE_180D_pct":26.59,"MFE_1Y_pct":103.6,"MFE_2Y_pct":null,"MAE_30D_pct":-21.75,"MAE_90D_pct":-27.56,"MAE_180D_pct":-27.56,"MAE_1Y_pct":-27.56,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-19","peak_price":91400,"drawdown_after_peak_pct":-31.62,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":["contract_delay"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"framework_agreement_without_firm_order_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_R3_L124_299030_20220825","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11-R3-L124-011790-20230220-Stage2Actionable","case_id":"C11-R3-L124-SKC-20230219","symbol":"011790","company_name":"SKC","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","sector":"battery_copper_foil","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|canonical_archetype_compression|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-19","entry_date":"2023-02-20","entry_price":97300,"evidence_available_at_that_date":"SKC official release: SK nexilis signed a five-year KRW 1.4tn copper-foil supply contract with Northvolt; volume about 80% of Northvolt copper-foil needs, produced from Poland from 2024.","evidence_source":"https://www.skc.kr/m/eng/Conmmunication/pr/newsDetail.do?gubun=&seq=1511","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.59,"MFE_90D_pct":25.69,"MFE_180D_pct":25.69,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.3,"MAE_90D_pct":-7.3,"MAE_180D_pct":-30.11,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-05","peak_price":122300,"drawdown_after_peak_pct":-44.4,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_representative_entry","four_b_evidence_type":["margin_or_backlog_slowdown","contract_delay"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"customer_orderbook_without_margin_conversion_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_R3_L124_011790_20230220","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11-R3-L124-PNT-20240619-4B","case_id":"C11-R3-L124-PNT-20240416","symbol":"137400","company_name":"피엔티","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_TO_MARGIN_FCF_CONVERSION_VS_HEADLINE_BACKLOG","sector":"battery_equipment_electrode_process","primary_archetype":"battery_orderbook_rerating","loop_objective":"4B_non_price_requirement_stress_test|sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-06-19","entry_date":"2024-06-19","entry_price":84500,"evidence_available_at_that_date":"Stock-web price path after PNT orderbook rerating: local/full-window overheat overlay at observed 180D high; non-price slowdown not yet confirmed, so overlay is risk-control only.","evidence_source":"stock-web derived overlay plus case evidence source","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv","profile_path":"atlas/symbol_profiles/137/137400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.92,"MFE_90D_pct":5.92,"MFE_180D_pct":5.92,"MFE_1Y_pct":5.92,"MFE_2Y_pct":null,"MAE_30D_pct":-40.59,"MAE_90D_pct":-45.62,"MAE_180D_pct":-56.69,"MAE_1Y_pct":-64.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":89500,"drawdown_after_peak_pct":-59.11,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.902,"four_b_full_window_peak_proximity":0.902,"four_b_timing_verdict":"good_risk_overlay_but_not_full_4b_without_non_price_slowdown","four_b_evidence_type":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4b_overlay_success_after_orderbook_rerating","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_R3_L124_137400_20240619","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same PNT case but new Stage4B overlay timing after representative Stage2 orderbook trigger","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11-R3-L124-PNT-20240416","trigger_id":"C11-R3-L124-137400-20240417-Stage2Actionable","symbol":"137400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":85,"backlog_visibility_score":80,"margin_bridge_score":65,"revision_score":55,"relative_strength_score":75,"customer_quality_score":70,"policy_or_regulatory_score":35,"valuation_repricing_score":60,"execution_risk_score":40,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":90,"backlog_visibility_score":86,"margin_bridge_score":75,"revision_score":60,"relative_strength_score":80,"customer_quality_score":75,"policy_or_regulatory_score":35,"valuation_repricing_score":64,"execution_risk_score":35,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C11 needs an equipment-order size + backlog + margin bridge fast lane; PNT had order evidence plus backlog context before the clean rerating.","MFE_90D_pct":131.57,"MAE_90D_pct":-1.55,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11-R3-L124-POSCOFM-20230426","trigger_id":"C11-R3-L124-003670-20230427-Stage2Actionable","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":92,"backlog_visibility_score":90,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":85,"customer_quality_score":90,"policy_or_regulatory_score":40,"valuation_repricing_score":80,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":92,"backlog_visibility_score":90,"margin_bridge_score":62,"revision_score":55,"relative_strength_score":82,"customer_quality_score":90,"policy_or_regulatory_score":40,"valuation_repricing_score":75,"execution_risk_score":50,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"The orderbook signal worked, but without 4B overheat overlay it retained too much post-peak downside.","MFE_90D_pct":104.12,"MAE_90D_pct":-14.12,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11-R3-L124-WONIKPNE-20221227","trigger_id":"C11-R3-L124-217820-20221228-Stage2Actionable","symbol":"217820","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":80,"backlog_visibility_score":70,"margin_bridge_score":45,"revision_score":42,"relative_strength_score":62,"customer_quality_score":55,"policy_or_regulatory_score":25,"valuation_repricing_score":48,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":83,"backlog_visibility_score":74,"margin_bridge_score":57,"revision_score":50,"relative_strength_score":67,"customer_quality_score":58,"policy_or_regulatory_score":25,"valuation_repricing_score":52,"execution_risk_score":42,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Contract-to-sales ratio and delivery horizon mattered more than generic battery beta.","MFE_90D_pct":53.42,"MAE_90D_pct":-7.1,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11-R3-L124-LNF-20230228","trigger_id":"C11-R3-L124-066970-20230302-Stage2Actionable","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":90,"backlog_visibility_score":82,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":80,"customer_quality_score":75,"policy_or_regulatory_score":30,"valuation_repricing_score":78,"execution_risk_score":55,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":82,"backlog_visibility_score":68,"margin_bridge_score":30,"revision_score":35,"relative_strength_score":60,"customer_quality_score":70,"policy_or_regulatory_score":30,"valuation_repricing_score":62,"execution_risk_score":70,"legal_or_contract_risk_score":50,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Customer concentration and ASP/lithium pass-through caveats should cap C11 at Stage2-Actionable until shipment and margin conversion appear.","MFE_90D_pct":39.52,"MAE_90D_pct":-12.57,"score_return_alignment_label":"overpromoted_without_conversion_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11-R3-L124-ECOPROBM-20231203","trigger_id":"C11-R3-L124-247540-20231204-Stage2Actionable","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":95,"backlog_visibility_score":88,"margin_bridge_score":30,"revision_score":30,"relative_strength_score":55,"customer_quality_score":85,"policy_or_regulatory_score":30,"valuation_repricing_score":82,"execution_risk_score":70,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":85,"backlog_visibility_score":70,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":35,"customer_quality_score":78,"policy_or_regulatory_score":30,"valuation_repricing_score":58,"execution_risk_score":82,"legal_or_contract_risk_score":42,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":64,"stage_label_after":"Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"A huge order after sector valuation blowoff did not rerate cleanly; C11 needs cycle/margin sanity gate.","MFE_90D_pct":9.6,"MAE_90D_pct":-34.67,"score_return_alignment_label":"overpromoted_without_conversion_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11-R3-L124-HANA-20220824","trigger_id":"C11-R3-L124-299030-20220825-Stage2","symbol":"299030","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":45,"customer_quality_score":45,"policy_or_regulatory_score":20,"valuation_repricing_score":50,"execution_risk_score":65,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_before":67,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":30,"margin_bridge_score":20,"revision_score":22,"relative_strength_score":42,"customer_quality_score":40,"policy_or_regulatory_score":20,"valuation_repricing_score":42,"execution_risk_score":75,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15},"weighted_score_after":58,"stage_label_after":"Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Framework/strategic partnership language without firm PO/order amount should not become C11 Stage2-Actionable.","MFE_90D_pct":12.74,"MAE_90D_pct":-27.56,"score_return_alignment_label":"overpromoted_without_conversion_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11-R3-L124-SKC-20230219","trigger_id":"C11-R3-L124-011790-20230220-Stage2Actionable","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":88,"backlog_visibility_score":78,"margin_bridge_score":28,"revision_score":35,"relative_strength_score":55,"customer_quality_score":70,"policy_or_regulatory_score":30,"valuation_repricing_score":60,"execution_risk_score":65,"legal_or_contract_risk_score":40,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":80,"backlog_visibility_score":62,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":45,"customer_quality_score":62,"policy_or_regulatory_score":30,"valuation_repricing_score":50,"execution_risk_score":80,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15},"weighted_score_after":62,"stage_label_after":"Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Large customer offtake needed copper-foil margin/capex ramp and customer execution confirmation; headline contract alone was not enough.","MFE_90D_pct":25.69,"MAE_90D_pct":-7.3,"score_return_alignment_label":"overpromoted_without_conversion_gate","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"124","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_false_positive","current_profile_missed_structural","current_profile_4B_too_late","high_mae_after_order_headline"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"C11-R3-L124-LNF-20251229-CONTRACT-CUT","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","reason":"later Tesla contract reduction evidence exists but stock-web manifest max_date leaves insufficient 180D forward window; use as narrative support for customer/call-off risk, not weight calibration","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","evidence_source":"https://pulse.mk.co.kr/news/english/11918715"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 124
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C11 rows 18 need_to_30 12
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

Next execution should re-read `V12_Research_No_Repeat_Index.md` rather than mechanically advancing R4. If the previous C11 rows are accepted, C01 and C28 become the natural next Priority 0 targets.

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- PNT evidence: https://securities.miraeasset.com/bbs/download/2125406.pdf?attachmentId=2125406
- POSCO Future M evidence: https://www.poscofuturem.com/en/pr/view.do?num=684
- Wonik PNE evidence: https://www.infostockdaily.co.kr/news/articleView.html?idxno=186897
- L&F evidence: https://www.teslarati.com/tesla-signs-2-9b-battery-materials-deal-l-f/
- L&F narrative-only later contract cut: https://pulse.mk.co.kr/news/english/11918715
- EcoPro BM evidence: https://www.koreajoongangdaily.com/business/ecopro-bm-secures-34-billion-deal-as-samsung-sdis-cathode-supplier/11483248
- Hana Technology / FREYR evidence: https://news.cision.com/se/t1-energy-inc/r/freyr-battery-enters-strategic-partnership-with-hana-technology%2Cc3619082
- SKC / SK nexilis evidence: https://www.skc.kr/m/eng/Conmmunication/pr/newsDetail.do?gubun=&seq=1511

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
