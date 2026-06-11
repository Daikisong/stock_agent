# E2R Stock-Web v12 Residual Calibration Research

file_name: `e2r_stock_web_v12_residual_round_R4_loop_136_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md`  
schema_family: `v12_sector_archetype_residual`  
created_at: `2026-06-07T00:00:00+09:00`  
selected_round: `R4`  
selected_loop: `136`  
large_sector_id: `L4_MATERIALS_SPREAD_RESOURCE`  
canonical_archetype_id: `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`  
fine_archetype_id: `REFINING_AND_PETCHEM_FEEDSTOCK_PRODUCT_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_HIGH_MAE_FALSE_STAGE2`  
selection_basis: `docs/core/V12_Research_No_Repeat_Index.md`  
selected_priority_bucket: `Priority 0 / under-covered residual`  
price_source: `Songdaiki/stock-web`  
price_basis: `tradable_raw`  
price_adjustment_status: `raw_unadjusted_marcap`  
stock_web_manifest_max_date: `2026-02-20`  

---

## 1. Execution contract

MAIN EXECUTION PROMPT: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`  
NO-REPEAT INDEX: `docs/core/V12_Research_No_Repeat_Index.md`  

This run follows the v12 coverage-index-first contract:

1. Read the No-Repeat Index as the duplication ledger only.
2. Select an under-covered canonical archetype.
3. Derive round and sector from the selected canonical archetype.
4. Use `Songdaiki/stock-web` OHLC paths only for price validation.
5. Emit calibration-usable trigger rows with entry_date, entry_price, and 30/90/180D MFE/MAE fields.
6. Avoid previously covered high-frequency C17 symbols where possible.

---

## 2. Selection rationale

`C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` remains under-covered relative to the 30-row and 50-row targets. The visible No-Repeat Index snapshot shows:

| canonical_archetype_id | rows | symbols | positives/counter | 4B/4C | S2 hit/bad |
|---|---:|---:|---:|---:|---:|
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 12 | 9 | 1/2 | 1/1 | 0.50/0.38 |

The visible top covered symbols are `011780`, `011170`, `004000`, `006650`, `014680`, `014830`. This run uses new visible C17 symbols:

- `010950` S-Oil
- `051910` LG화학
- `298000` 효성화학

Loop selection follows the v12 rule:

`selected_loop = max(existing loop for selected_round and selected_canonical_archetype_id) + 1`

The registry shows an existing `R4 / C17` item at loop `135`, so this run uses loop `136`.

---

## 3. Archetype hypothesis

C17 should not fire on a raw commodity rebound alone.

The key bridge is:

`feedstock/product spread -> realized company margin -> operating revision/cash-flow confirmation -> durable price path`

For petrochemical and refining names, the false-positive trap is especially easy:

- naphtha/LPG/refining/crack-spread headlines can move prices before earnings prove pass-through;
- lower feedstock cost can help only if utilization, product demand, and downstream selling prices do not collapse at the same time;
- integrated large caps can dilute spread benefit through batteries, holding-company mix, debt, or one-off losses;
- weak-margin oversupply regimes often create short MFE followed by long MAE.

Therefore C17 needs a company-specific margin bridge, not just "chemical/refining/resource" vocabulary.

---

## 4. Calibration cases

### Case A — S-Oil (`010950`) — positive, but later refining-margin watch

case_id: `C17_010950_REFINING_MARGIN_REBOUND_Q1_2024`  
row_class: `positive_with_local_4b_watch`  
trigger_family: `refining_margin_rebound_and_seasonal_demand_expectation`  
evidence_family: `reported_refining_margin_rebound | seasonal_margin_outlook | stock_web_forward_path`  
as_of_date: `2024-02-13`  
entry_date: `2024-02-13`  
entry_price: `71,500`  

Rationale:

S-Oil gave a cleaner C17 test than broad petrochemical names because the trigger was closer to a refining-margin channel. The early-2024 path showed a usable spread-linked rerating: the stock moved from the February entry zone to an April high near 84,500. However, the later 2024 industry backdrop weakened, so the row is not a free Green. It is better used as a positive C17 bridge with a later local-4B watch when margins roll over.

Approximate forward price path from stock-web:

| window | high | low | MFE_pct | MAE_pct |
|---|---:|---:|---:|---:|
| 30D | 79,700 | 70,500 | 11.47 | -1.40 |
| 90D | 84,500 | 66,400 | 18.18 | -7.13 |
| 180D | 84,500 | 57,100 | 18.18 | -20.14 |

Interpretation:

- Positive C17 signal exists when refining margin rebound is backed by reported earnings/management margin discussion.
- But the later MAE says the rule should not promote to durable Green unless margin strength survives the next reporting window.
- Recommended handling: `Stage2-Actionable -> Stage3-Yellow only if spread and revision persist; local 4B watch after margin fade`.

---

### Case B — LG화학 (`051910`) — counterexample: low-margin petrochemical oversupply + battery mix dilution

case_id: `C17_051910_LOW_MARGIN_PETCHEM_OVERSUPPLY_2024`  
row_class: `counterexample`  
trigger_family: `petrochemical_feedstock_substitution_low_margin_oversupply`  
evidence_family: `petchem_low_margin | LPG_substitution | large_cap_mix_dilution | stock_web_forward_path`  
as_of_date: `2024-05-20`  
entry_date: `2024-05-20`  
entry_price: `391,500`  

Rationale:

LG화학 was explicitly part of the South Korean petrochemical complex exposed to low margins and naphtha/LPG substitution. But this is exactly the trap C17 needs to block: feedstock substitution and industry-volume support do not necessarily equal a listed-company margin rerating. In LG화학's case, battery exposure and petchem oversupply diluted any simple spread thesis.

Approximate forward price path from stock-web:

| window | high | low | MFE_pct | MAE_pct |
|---|---:|---:|---:|---:|
| 30D | 399,500 | 350,000 | 2.04 | -10.60 |
| 90D | 399,500 | 263,500 | 2.04 | -32.69 |
| 180D | 399,500 | 208,000 | 2.04 | -46.87 |

Interpretation:

- This is a clear `Stage2 false-positive` if triggered only by petrochemical feedstock headlines.
- The correct C17 rule must demand visible product spread, operating revision, and segment-level margin bridge.
- Large-cap mixed businesses need extra penalty when the commodity spread thesis is not the dominant earnings driver.

---

### Case C — 효성화학 (`298000`) — counterexample: PP/chemical label spike without durable balance-sheet/margin repair

case_id: `C17_298000_PP_CHEMICAL_LABEL_SPIKE_HIGH_MAE_2024`  
row_class: `counterexample_high_MAE`  
trigger_family: `chemical_margin_turnaround_label_spike`  
evidence_family: `chemical_product_vocabulary | margin_repair_unconfirmed | stock_web_forward_path`  
as_of_date: `2024-05-20`  
entry_date: `2024-05-20`  
entry_price: `71,000`  

Rationale:

효성화학 is a useful C17 stress case because the stock generated a large short-lived vertical move around the same broad petrochemical/feedstock discussion window. But the follow-through failed hard. This shows why C17 should not treat product vocabulary or one-day spread optimism as a durable rerating signal. Without segment-level margin repair, utilization improvement, or balance-sheet relief, the later path turns into high-MAE decay.

Approximate forward price path from stock-web:

| window | high | low | MFE_pct | MAE_pct |
|---|---:|---:|---:|---:|
| 30D | 72,000 | 59,500 | 1.41 | -16.20 |
| 90D | 77,400 | 55,100 | 9.01 | -22.39 |
| 180D | 77,400 | 28,150 | 9.01 | -60.35 |

Interpretation:

- Price-only chemical spread optimism created MFE but not a durable rerating.
- This is a strong high-MAE guardrail row.
- Recommended handling: block Stage2 unless spread expansion is visible in company-level earnings, cash conversion, and debt/liquidity repair.

---

## 5. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R4","selected_loop":"136","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_AND_PETCHEM_FEEDSTOCK_PRODUCT_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_HIGH_MAE_FALSE_STAGE2","symbol":"010950","company_name":"S-Oil","case_id":"C17_010950_REFINING_MARGIN_REBOUND_Q1_2024","case_polarity":"positive_with_local_4b_watch","trigger_type":"refining_margin_rebound_and_seasonal_demand_expectation","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":71500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":11.47,"MAE_30D_pct":-1.40,"MFE_90D_pct":18.18,"MAE_90D_pct":-7.13,"MFE_180D_pct":18.18,"MAE_180D_pct":-20.14,"profile_verdict":"current_profile_partial_miss","residual_error_type":"positive_but_later_margin_fade_watch","evidence_bridge":"reported refining margin rebound plus seasonal demand expectation; later 2024 margin fade requires local 4B watch","calibration_usable":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R4","selected_loop":"136","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_AND_PETCHEM_FEEDSTOCK_PRODUCT_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_HIGH_MAE_FALSE_STAGE2","symbol":"051910","company_name":"LG화학","case_id":"C17_051910_LOW_MARGIN_PETCHEM_OVERSUPPLY_2024","case_polarity":"counterexample","trigger_type":"petrochemical_feedstock_substitution_low_margin_oversupply","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":391500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.04,"MAE_30D_pct":-10.60,"MFE_90D_pct":2.04,"MAE_90D_pct":-32.69,"MFE_180D_pct":2.04,"MAE_180D_pct":-46.87,"profile_verdict":"current_profile_false_positive_risk","residual_error_type":"petchem_feedstock_headline_without_company_margin_bridge","evidence_bridge":"industry LPG substitution and low-margin oversupply did not translate into listed-company margin/revision bridge","calibration_usable":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R4","selected_loop":"136","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_AND_PETCHEM_FEEDSTOCK_PRODUCT_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_HIGH_MAE_FALSE_STAGE2","symbol":"298000","company_name":"효성화학","case_id":"C17_298000_PP_CHEMICAL_LABEL_SPIKE_HIGH_MAE_2024","case_polarity":"counterexample_high_MAE","trigger_type":"chemical_margin_turnaround_label_spike","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":71000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.41,"MAE_30D_pct":-16.20,"MFE_90D_pct":9.01,"MAE_90D_pct":-22.39,"MFE_180D_pct":9.01,"MAE_180D_pct":-60.35,"profile_verdict":"current_profile_false_positive_risk","residual_error_type":"chemical_label_price_spike_without_margin_repair","evidence_bridge":"chemical product vocabulary and short-lived MFE did not survive without visible margin/cash/balance-sheet repair","calibration_usable":true}
```

---

## 6. Stage transition summary

| case_id | initial_stage_candidate | observed_result | recommended_stage_treatment |
|---|---|---|---|
| C17_010950_REFINING_MARGIN_REBOUND_Q1_2024 | Stage2-Actionable / Yellow | Positive MFE, later MAE watch | Permit Stage2; Yellow only after second confirmation; 4B watch if refining margin rolls over |
| C17_051910_LOW_MARGIN_PETCHEM_OVERSUPPLY_2024 | Stage2 false-positive risk | Low MFE, high MAE | Block Stage2 unless segment-level spread and revision bridge are present |
| C17_298000_PP_CHEMICAL_LABEL_SPIKE_HIGH_MAE_2024 | Stage2 false-positive risk | Small MFE, severe MAE | Block Stage2; classify as price-only/label spike unless cash/balance-sheet repair appears |

---

## 7. Residual contribution

```jsonl
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","selected_round":"R4","selected_loop":"136","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","loop_contribution_label":"canonical_archetype_rule_candidate","new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count_visible_index_basis":3,"same_archetype_new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"high_MAE_guardrail_count":2,"sector_specific_rule_candidate":false,"canonical_archetype_rule_candidate":true,"do_not_propose_new_weight_delta":false}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","selected_round":"R4","selected_loop":"136","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","existing_axis_strengthened":"C17_company_specific_feedstock_product_spread_margin_bridge_requirement; C17_petchem_feedstock_headline_stage2_block; C17_integrated_largecap_mix_dilution_penalty; C17_high_MAE_local_4B_watch_after_commodity_beta_spike","new_axis_proposed":null,"existing_axis_weakened":null}
```

---

## 8. Shadow scoring suggestion

No immediate global score delta is proposed.

Suggested C17-specific guardrail:

- Require at least one of:
  - realized product spread expansion in earnings/commentary,
  - segment-level operating-margin revision,
  - utilization plus selling-price pass-through,
  - cash-flow improvement tied to the spread.
- Penalize:
  - broad petrochemical low-margin/oversupply context without company-level evidence,
  - integrated large-cap names where the commodity spread is not the dominant earnings driver,
  - one-day chemical/refining label spikes with MAE above 20%.
- Treat `MFE > 8% and MAE < -20%` without margin confirmation as `local_4B_watch`, not Stage3-Green.

```jsonl
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","selected_round":"R4","selected_loop":"136","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","shadow_weight_action":"hold_for_more_evidence","reason":"3 usable rows strengthen C17 guardrail, but row count remains below 30 and should not yet trigger a runtime weight delta","candidate_rule":"company_specific_spread_margin_bridge_required_before_stage2_or_green"}
```

---

## 9. Coverage impact

Before local run:
- C17 visible No-Repeat Index rows: `12`
- C17 visible unique symbols: `9`

Local contribution:
- New visible C17 symbols: `3`
- Calibration-usable trigger rows: `3`
- Positive/counterexample mix: `1 / 2`
- High-MAE guardrail rows: `2`

After local handoff candidate:
- Effective C17 rows if ingested: `15`
- Remaining to 30-row floor: `15`
- Remaining to 50-row target: `35`

---

## 10. Final status

round_schedule_status: `coverage_index_selected`  
round_sector_consistency: `pass`  
large_sector_id: `L4_MATERIALS_SPREAD_RESOURCE`  
canonical_archetype_id: `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`  
fine_archetype_id: `REFINING_AND_PETCHEM_FEEDSTOCK_PRODUCT_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_HIGH_MAE_FALSE_STAGE2`  
new_independent_case_count: `3`  
reused_case_count: `0`  
same_archetype_new_symbol_count_visible_index_basis: `3`  
same_archetype_new_trigger_family_count: `3`  
calibration_usable_case_count: `3`  
calibration_usable_trigger_count: `3`  
positive_case_count: `1`  
counterexample_count: `2`  
current_profile_error_count: `2`  
diversity_score_summary: `new_visible_C17_symbol=3, new_trigger_family=3, positive/counterexample=1/2, refining-margin positive-with-watch=1, petchem-low-margin false-positive=1, chemical-label high-MAE=1`  
do_not_propose_new_weight_delta: `false`  
auto_selected_coverage_gap: `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD: rows=12, need_to_30=18, need_to_50=38`  
sector_specific_rule_candidate: `false`  
canonical_archetype_rule_candidate: `true`  
loop_contribution_label: `canonical_archetype_rule_candidate`  
new_axis_proposed: `null`  
existing_axis_strengthened: `C17_company_specific_feedstock_product_spread_margin_bridge_requirement; C17_petchem_feedstock_headline_stage2_block; C17_integrated_largecap_mix_dilution_penalty; C17_high_MAE_local_4B_watch_after_commodity_beta_spike`  
existing_axis_weakened: `null`  
next_recommended_archetypes: `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`
