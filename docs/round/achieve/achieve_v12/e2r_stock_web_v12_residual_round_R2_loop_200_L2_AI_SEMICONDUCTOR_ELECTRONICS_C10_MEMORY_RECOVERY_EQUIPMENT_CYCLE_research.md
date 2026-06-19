# E2R Stock-Web Historical Calibration v12 / C10 Supplier-Order Conversion & 4B Reopen Repair

## 0. Research Metadata

```text
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 200
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: quality reinforcement after all canonical archetypes >80 rows; C10 has 210 rows but only 0 hard-4C representative rows and high URL/proxy cleanup need
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_REPAIR
output_filename: e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
current_run_note: generated_from_current_execution_after_C13_loop_199; C10 selected per Priority 1 balance reinforcement and prior run non-overlap
```

One-line contribution: this loop separates **generic memory-cycle beta** from **supplier-level order/revenue conversion**, and adds a C10 repair rule for cases where a prior 4B or bearish headline must reopen to Stage2-Actionable after company-specific conversion evidence appears. The gear being calibrated is not “memory is recovering”; it is “whose equipment order book actually got pulled into that recovery.”

## 1. Control Prompt / No-Repeat Interpretation

The main prompt requires `coverage_index_first`, actual Songdaiki/stock-web 1D OHLCV, complete 30/90/180D MFE/MAE, canonical trigger labels, no live scan, no `stock_agent` code patch, and shadow-only residual output. The No-Repeat Index is used only as a duplicate-prevention ledger. Current cumulative coverage shows all C01~C32 archetypes over 80 rows, so this run is quality repair rather than row filling. C10 specifically has `210 rows / 68 symbols / positives-counter 27-32 / 4B-4C 27-0`; therefore the target is **C10 order-conversion / 4B reopen / hard-4C boundary quality**, not another generic memory recovery proof.

## 2. Stock-Web OHLC Input / Price Source Validation

```text
price_source: Songdaiki/stock-web
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
tradable_columns: d,o,h,l,c,v,a,mc,s,m
MFE_formula: (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_formula: (min low from entry_date through N tradable rows / entry_price - 1) * 100
validation_status: usable_for_historical_calibration
```

Corporate-action contamination was checked by scanning the 180-tradable-row calibration window for major share-count changes and raw price discontinuities. No selected trigger row had a contaminated 180D window.

## 3. Historical Eligibility Gate — Actual Entry Rows

|symbol|entry_date|open|high|low|close|volume|shares|price_shard_path|
|---|---|---|---|---|---|---|---|---|
|031980|2024-06-03|56400|56500|52900|55700|223818|21562395|atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv|
|083450|2024-11-29|14740|14820|13960|14000|316872|18618260|atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv|
|281820|2024-06-03|38100|40150|37700|38900|236488|20861556|atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv|
|240810|2024-12-05|22000|22500|21750|21800|203934|49083901|atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv|
|084370|2024-10-31|35000|37700|35000|37400|222269|22916042|atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv|
|036930|2024-10-31|29450|31800|29450|31000|2964215|47268321|atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv|
|319660|2024-08-14|30600|31600|29900|30450|498509|28966714|atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv|
|095610|2024-11-14|14870|15090|14300|14370|121578|19768226|atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv|

## 4. Case Selection Summary

|case_id|symbol|company|trigger|trigger_date|entry_date|180D MFE/MAE|case_role|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|C10_031980_20240531_STAGE2A|031980|PSK Holdings|Stage2-Actionable|2024-05-31|2024-06-03|53.14/-50.27|direct_supplier_order_bridge_high_mae_control|current_profile_should_preserve_stage2a_but_block_green|
|C10_083450_20241129_STAGE2A|083450|GST|Stage2-Actionable|2024-11-29|2024-11-29|66.79/-0.29|low_mae_supplier_conversion_positive_control|current_profile_too_conservative_if_treated_as_generic_memory_beta|
|C10_281820_20240603_STAGE2A|281820|KCTech|Stage2-Actionable|2024-06-03|2024-06-03|51.67/-35.35|front_end_equipment_positive_high_mae_control|current_profile_should_cap_yellow_green_due_high_mae|
|C10_240810_20241205_4B|240810|Wonik IPS|4B|2024-12-05|2024-12-05|98.85/-4.59|bad_headline_not_hard4c_positive_reopen|current_profile_hard4c_too_aggressive_if_no_offset_check|
|C10_084370_20241031_4B|084370|Eugene Tech|4B|2024-10-31|2024-10-31|32.22/-18.98|moderate_recovery_requires_order_conversion|current_profile_should_hold_at_4b_or_stage2_not_green|
|C10_036930_20241031_STAGE2|036930|Jusung Engineering|Stage2|2024-10-31|2024-10-31|40.0/-16.61|ald_optional_but_not_actionable_without_conversion|current_profile_stage2a_too_loose_if_no_customer_order|
|C10_319660_20240814_4B|319660|PSK|4B|2024-08-14|2024-08-14|5.09/-48.93|late_beta_extension_counterexample|current_profile_should_route_to_local_4b_not_actionable|
|C10_095610_20241114_STAGE2A|095610|TES|Stage2-Actionable|2024-11-14|2024-11-14|95.89/-8.91|trough_reopen_positive_control|current_profile_too_late_if_prior_4b_not_cleared|

## 5. Trigger-Level Backtest Result

|trigger_id|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|
|C10_STAGE2A_031980_20240531_HBM_REFLOW_MICRON_SUPPLIER_BRIDGE|55700|53.14|-5.03|53.14|-35.19|53.14|-50.27|2024-06-19|85300|-67.53|
|C10_STAGE2A_083450_20241129_ULTRA_LOW_CHILLER_MEMORY_THERMAL_BRIDGE|14000|34.64|-0.29|66.79|-0.29|66.79|-0.29|2025-02-24|23350|-34.18|
|C10_STAGE2A_281820_20240603_CMP_WET_CLEANING_SUPPLIER_BRIDGE|38900|51.67|-3.08|51.67|-24.29|51.67|-35.35|2024-07-11|59000|-57.37|
|C10_4B_240810_20241205_CAPEX_REVISION_DOWN_BUT_PROCESS_UPGRADE_OFFSET|21800|13.3|-2.98|30.73|-4.59|98.85|-4.59|2025-08-13|43350|-12.23|
|C10_4B_084370_20241031_MEMORY_RECOVERY_WITHOUT_ORDER_DETAIL|37400|6.55|-15.64|32.22|-18.98|32.22|-18.98|2025-02-19|49450|-37.61|
|C10_STAGE2_036930_20241031_ALD_CAPEX_OPTIONALITY_NOT_ACTIONABLE|31000|9.84|-16.61|29.03|-16.61|40.0|-16.61|2025-03-21|43400|-33.41|
|C10_4B_319660_20240814_BETA_EXTENSION_WITH_WEAK_FORWARD_PATH|30450|5.09|-32.68|5.09|-48.93|5.09|-48.93|2024-08-16|32000|-51.41|
|C10_STAGE2A_095610_20241114_MEMORY_RECOVERY_TROUGH_ORDER_CONVERSION|14370|13.43|-8.91|70.84|-8.91|95.89|-8.91|2025-07-16|28150|-17.41|

## 6. Evidence Source Map

|case_id|source_type|source_url|evidence_note|
|---|---|---|---|
|C10_031980_20240531_STAGE2A|direct_or_company_specific|https://www.thelec.net/news/articleView.html?idxno=4859|The Elec reported PSK Holdings supplied reflow equipment to Micron for HBM and described its HBM reflow/descum customer footprint across major DRAM makers.|
|C10_083450_20241129_STAGE2A|direct_or_company_specific|https://www.gst-in.com/en/m31.php|GST official product materials identify thermal control systems and ultra-low-temperature chiller capability; the entry row tests when this becomes supplier-specific C10 evidence rather than a broad memory beta.|
|C10_281820_20240603_STAGE2A|direct_or_company_specific|https://www.kctech.com/eng/page/product1.php|KCTech official product page identifies CMP and wet cleaning systems for semiconductor processes; the case tests whether front-end memory equipment exposure needs company-specific bridge and MAE brake.|
|C10_240810_20241205_4B|direct_or_company_specific|https://www.asiae.co.kr/en/article/2024120507561579363|Asia Business Daily reported a target-price cut / 2025 earnings forecast miss risk, with HBM3E demand weakness and process-upgrade discussion; price path then recovered strongly, making it a hard-4C overreaction repair row.|
|C10_084370_20241031_4B|direct_or_company_specific|https://www.eugenetech.co.kr/eng/main/main.php|Eugene Tech is a semiconductor equipment maker; this row uses the post-SK-hynix-Q3 memory recovery regime to test whether broad capex cycle evidence is enough without order conversion.|
|C10_036930_20241031_STAGE2|direct_or_company_specific|https://m.thebell.co.kr/m/newsview.asp?newskey=202402261105163080101554&svccode=|Jusung exposure is tied to ALD / memory capex optionality; prior customer capex commentary was selective, so this row keeps Stage2 capped unless supplier order/backlog conversion appears.|
|C10_319660_20240814_4B|direct_or_company_specific|https://www.pskinc.com/en/ir/financial-status/|PSK financial/product materials show semiconductor equipment exposure, but this entry lacked a fresh supplier-order bridge and produced severe forward drawdown.|
|C10_095610_20241114_STAGE2A|direct_or_company_specific|https://dealsite.co.kr/articles/123029|Dealsite described TES as a front-end equipment maker tied to Samsung/SK Hynix customer capex and explained why recovery was improving but not complete; this row tests the trough-to-reopen condition.|

## 7. Case Notes / Residual Diagnosis

### 7.1 Direct supplier order bridge is not the same as generic memory beta

`031980 / PSK Holdings` is the cleanest bridge row in this loop. The evidence is customer-specific: reflow equipment supplied to Micron for HBM, plus existing Samsung/SK Hynix HBM equipment footprint. The forward path had very high 180D upside but also a -50.27% MAE, so the proper calibration result is not “block Stage2”; it is **allow Stage2-Actionable but block Green until drawdown/visibility improves**.

`083450 / GST` and `281820 / KCTech` are equipment/component bridge controls. Their actual stock-web paths show that supplier-specific equipment exposure can work, but the MAE profile differs sharply: GST produced a low-MAE recovery path, while KCTech produced a high-MAE path. This supports a two-step gate: Stage2-Actionable can clear with a company-specific bridge, but Stage3-Yellow/Green needs either low-MAE confirmation or stronger revenue/order conversion.

### 7.2 Bad headline does not automatically mean hard 4C

`240810 / Wonik IPS` is the key reopen row. The December 2024 evidence was negative on headline — 2025 earnings forecast miss risk and capex revision-down language — but the forward path showed `MFE_180D +98.85%` with only `MAE_180D -4.59%`. That is not a hard 4C. It is a local 4B/watch row that must be allowed to reopen if process-upgrade or supplier-conversion evidence appears.

### 7.3 Generic customer capex beta still needs supplier conversion

`084370 / Eugene Tech`, `036930 / Jusung Engineering`, and `319660 / PSK` test the opposite side. They are all plausible memory equipment names, but the selected entry rows do not have the same direct order bridge as PSK Holdings or the later TES reopen row. `319660` in particular produced `MFE_180D +5.09% / MAE_180D -48.93%`, which is the shape of a late beta chase, not a validated Stage2-Actionable.

### 7.4 Trough reopen condition

`095610 / TES` is the positive reopen control. Broad front-end recovery in May 2024 was not enough to claim complete recovery; however, the November 2024 trough entry produced `MFE_180D +95.89% / MAE_180D -8.91%`. The rule implication is that C10 needs a **4B clearing condition**: after a prior broad-cycle watch, Stage2-Actionable can reopen if the stock-web path and non-price customer/revenue bridge improve together.

## 8. Current Calibrated Profile Stress Test

```text
profile_proxy: e2r_2_2_rolling_calibrated
baseline_guardrails_preserved:
  stage2_required_bridge: true
  local_4b_watch_guard: true
  earlier_thesis_break_watch: true
  hard_4c_confirmation: true
  stage3_green_not_loosened: true

current_profile_errors_observed:
  - generic_memory_beta_too_loose_for_stage2_actionable
  - hard4c_too_aggressive_when_offset_or_reopen_bridge_exists
  - high_mae_true_supplier_bridge_needs_green_blocker_not_stage2_blocker
  - supplier_order_conversion_missed_positive_after_prior_4b
```

Interpretation: C10 does not need a global score threshold change. It needs a canonical-level routing refinement: generic memory recovery can start Stage2/watch, direct supplier order conversion can clear Stage2-Actionable, late beta without supplier bridge should remain local 4B, and hard 4C should require non-price supplier thesis break rather than a bad headline alone.

## 9. Residual Contribution Summary

```text
new_independent_case_count: 8
new_independent_trigger_count: 8
unique_symbol_count: 8
reused_exact_duplicate_key_count: 0
calibration_usable_case_count: 8
calibration_usable_trigger_count: 8

positive_or_reopen_case_count: 5
counterexample_or_4b_case_count: 3
current_profile_error_count: 6

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

production_scoring_changed: false
shadow_weight_only: true
```

### Proposed canonical rule candidate

```text
canonical_rule_candidate:
C10_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_GATE

rule_shape:
1. Customer-level memory recovery / capex restart headline alone => Stage2 or local 4B watch, not Stage2-Actionable.
2. Supplier-level order, shipment, revenue conversion, customer qualification, or explicit equipment allocation => Stage2-Actionable can clear.
3. High MAE after true supplier bridge => block Stage3-Green, do not retroactively block Stage2-Actionable.
4. Negative capex or earnings headline with process-upgrade / customer-transition / later conversion offset => local 4B/watch, not hard 4C.
5. Hard 4C requires non-price supplier thesis break: order cancellation, confirmed capex pushout affecting supplier revenue, margin break, customer loss, or inventory/backlog failure.
```


## 10. Research Proxy Component Breakdown and Profile Comparison

The following component table is a research proxy, not a production score. It is included so the later batch/coding agent can see why the proposed C10 rule changes routing rather than loosening global thresholds.

| case_id | trigger_type | contract_score | backlog_visibility_score | margin_bridge_score | revision_score | relative_strength_score | customer_quality_score | policy_or_regulatory_score | valuation_repricing_score | execution_risk_score | legal_or_contract_risk_score | dilution_cb_risk_score | accounting_trust_risk_score | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | component_delta_explanation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| C10_031980_20240531_STAGE2A | Stage2-Actionable | 78 | 72 | 55 | 65 | 70 | 92 | 0 | 45 | 55 | 15 | 0 | 80 | 78 | Stage2-Actionable | 78 | Stage2-Actionable | direct Micron/HBM supplier bridge preserved; Green blocked by high MAE |
| C10_083450_20241129_STAGE2A | Stage2-Actionable | 62 | 60 | 50 | 58 | 72 | 80 | 0 | 45 | 35 | 10 | 0 | 75 | 72 | Stage2 | 79 | Stage2-Actionable | low-MAE supplier thermal-control bridge upgrades from generic beta |
| C10_281820_20240603_STAGE2A | Stage2-Actionable | 60 | 58 | 52 | 55 | 78 | 78 | 0 | 50 | 60 | 10 | 0 | 75 | 76 | Stage2-Actionable | 76 | Stage2-Actionable | supplier bridge valid, but high-MAE prevents Yellow/Green |
| C10_240810_20241205_4B | 4B | 45 | 45 | 35 | 30 | 55 | 65 | 0 | 35 | 70 | 10 | 0 | 72 | 61 | 4C | 66 | 4B | negative capex headline offset by later conversion; hard 4C too aggressive |
| C10_084370_20241031_4B | 4B | 45 | 48 | 35 | 42 | 58 | 62 | 0 | 40 | 62 | 10 | 0 | 70 | 75 | Stage2-Actionable | 64 | 4B | memory recovery without order conversion capped at watch/local 4B |
| C10_036930_20241031_STAGE2 | Stage2 | 42 | 46 | 34 | 40 | 56 | 58 | 0 | 40 | 58 | 10 | 0 | 72 | 74 | Stage2-Actionable | 68 | Stage2 | ALD optionality lacks enough supplier-order conversion for actionable upgrade |
| C10_319660_20240814_4B | 4B | 35 | 38 | 30 | 35 | 52 | 55 | 0 | 35 | 78 | 10 | 0 | 68 | 73 | Stage2-Actionable | 55 | 4B | late beta extension with weak forward path; route to watch not actionable |
| C10_095610_20241114_STAGE2A | Stage2-Actionable | 60 | 62 | 50 | 60 | 74 | 82 | 0 | 45 | 38 | 10 | 0 | 78 | 61 | 4B | 79 | Stage2-Actionable | 4B clears when customer/revenue conversion improves after trough |

### 10.1 Profile-level comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | changed_thresholds | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | current calibrated rule with generic C10 bridge | none | none | 8 | all representative rows | 42.44 | -19.72 | 55.46 | -22.99 | 0.38 | 2 | 0 | not_applicable | mixed | mixed | partially correct but generic memory beta still too loose |
| P0b_e2r_2_0_baseline_reference | baseline_reference | older baseline tends to over-promote cycle beta | none | legacy | 8 | all representative rows | 42.44 | -19.72 | 55.46 | -22.99 | 0.50 | 1 | 0 | not_applicable | weak | weak | weaker than calibrated profile; not recommended |
| P1_L2_sector_specific_candidate | sector_specific | require supplier-level bridge across L2 equipment cycle names | stage2_required_bridge + local_4b_watch_guard | no global threshold change | 8 | supplier bridge rows preferred | 50.43 | -14.12 | 62.71 | -19.03 | 0.25 | 1 | 0 | not_applicable | medium | medium | improves false-positive control without blocking true suppliers |
| P2_C10_canonical_candidate | canonical_archetype_specific | C10 supplier-order conversion and 4B reopen gate | C10_supplier_order_conversion + 4B_clear_path | no Stage3 Green loosening | 8 | direct supplier/reopen rows | 56.09 | -11.09 | 73.47 | -12.23 | 0.13 | 0 | 0 | not_applicable | medium | medium | best score-return alignment for this batch |
| P3_counterexample_guard_profile | counterexample_guard | keep generic beta, late extension, and bad headlines capped | hard_4c_confirmation + high_MAE_green_blocker | hard 4C requires non-price thesis break | 8 | counterexample rows stress-tested | 24.58 | -29.06 | 34.86 | -31.51 | 0.13 | 2 | 0 | not_applicable | high for 319660 | low for reopen cases | good guardrail but too conservative for reopen positives |

## 11. Machine-Readable JSONL Rows

```jsonl
{"row_type":"case","case_id":"C10_031980_20240531_STAGE2A","symbol":"031980","company":"PSK Holdings","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_REPAIR","case_role":"direct_supplier_order_bridge_high_mae_control","evidence_family":"supplier_specific_hbm_reflow_customer_order","source_url":"https://www.thelec.net/news/articleView.html?idxno=4859","calibration_usable":true,"narrative_only":false}
{"row_type":"trigger","case_id":"C10_031980_20240531_STAGE2A","trigger_id":"C10_STAGE2A_031980_20240531_HBM_REFLOW_MICRON_SUPPLIER_BRIDGE","symbol":"031980","company":"PSK Holdings","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-31","entry_date":"2024-06-03","entry_price":55700.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","MFE_30D_pct":53.14,"MAE_30D_pct":-5.03,"MFE_90D_pct":53.14,"MAE_90D_pct":-35.19,"MFE_180D_pct":53.14,"MAE_180D_pct":-50.27,"peak_180D_date":"2024-06-19","peak_180D_price":85300.0,"trough_180D_date":"2024-12-09","trough_180D_price":27700.0,"drawdown_after_peak_pct":-67.53,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"insufficient_forward_window":false,"calibration_usable":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|031980|Stage2-Actionable|2024-06-03","source_url":"https://www.thelec.net/news/articleView.html?idxno=4859","case_role":"direct_supplier_order_bridge_high_mae_control","current_profile_verdict":"current_profile_should_preserve_stage2a_but_block_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_031980_20240531_STAGE2A","trigger_id":"C10_STAGE2A_031980_20240531_HBM_REFLOW_MICRON_SUPPLIER_BRIDGE","symbol":"031980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","stage_label_before":"Stage2-Actionable","stage_label_after":"Stage2-Actionable","weighted_score_before":78,"weighted_score_after":78,"raw_component_scores_before":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"raw_component_scores_after":{"eps_fcf_explosion":22,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"error_type":"high_mae_true_supplier_bridge_not_false_positive","score_return_alignment_label":"current_profile_should_preserve_stage2a_but_block_green","MFE_90D_pct":53.14,"MAE_90D_pct":-35.19,"MFE_180D_pct":53.14,"MAE_180D_pct":-50.27}
{"row_type":"case","case_id":"C10_083450_20241129_STAGE2A","symbol":"083450","company":"GST","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_REPAIR","case_role":"low_mae_supplier_conversion_positive_control","evidence_family":"thermal_chiller_memory_equipment_bridge","source_url":"https://www.gst-in.com/en/m31.php","calibration_usable":true,"narrative_only":false}
{"row_type":"trigger","case_id":"C10_083450_20241129_STAGE2A","trigger_id":"C10_STAGE2A_083450_20241129_ULTRA_LOW_CHILLER_MEMORY_THERMAL_BRIDGE","symbol":"083450","company":"GST","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-29","entry_date":"2024-11-29","entry_price":14000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083450/2024.csv","MFE_30D_pct":34.64,"MAE_30D_pct":-0.29,"MFE_90D_pct":66.79,"MAE_90D_pct":-0.29,"MFE_180D_pct":66.79,"MAE_180D_pct":-0.29,"peak_180D_date":"2025-02-24","peak_180D_price":23350.0,"trough_180D_date":"2024-11-29","trough_180D_price":13960.0,"drawdown_after_peak_pct":-34.18,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"insufficient_forward_window":false,"calibration_usable":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|083450|Stage2-Actionable|2024-11-29","source_url":"https://www.gst-in.com/en/m31.php","case_role":"low_mae_supplier_conversion_positive_control","current_profile_verdict":"current_profile_too_conservative_if_treated_as_generic_memory_beta"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_083450_20241129_STAGE2A","trigger_id":"C10_STAGE2A_083450_20241129_ULTRA_LOW_CHILLER_MEMORY_THERMAL_BRIDGE","symbol":"083450","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","stage_label_before":"Stage2","stage_label_after":"Stage2-Actionable","weighted_score_before":72,"weighted_score_after":79,"raw_component_scores_before":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"raw_component_scores_after":{"eps_fcf_explosion":22,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"error_type":"supplier_specific_conversion_missed_positive","score_return_alignment_label":"current_profile_too_conservative_if_treated_as_generic_memory_beta","MFE_90D_pct":66.79,"MAE_90D_pct":-0.29,"MFE_180D_pct":66.79,"MAE_180D_pct":-0.29}
{"row_type":"case","case_id":"C10_281820_20240603_STAGE2A","symbol":"281820","company":"KCTech","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_REPAIR","case_role":"front_end_equipment_positive_high_mae_control","evidence_family":"cmp_wet_cleaning_front_end_equipment_bridge","source_url":"https://www.kctech.com/eng/page/product1.php","calibration_usable":true,"narrative_only":false}
{"row_type":"trigger","case_id":"C10_281820_20240603_STAGE2A","trigger_id":"C10_STAGE2A_281820_20240603_CMP_WET_CLEANING_SUPPLIER_BRIDGE","symbol":"281820","company":"KCTech","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-03","entry_date":"2024-06-03","entry_price":38900.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv","MFE_30D_pct":51.67,"MAE_30D_pct":-3.08,"MFE_90D_pct":51.67,"MAE_90D_pct":-24.29,"MFE_180D_pct":51.67,"MAE_180D_pct":-35.35,"peak_180D_date":"2024-07-11","peak_180D_price":59000.0,"trough_180D_date":"2024-12-20","trough_180D_price":25150.0,"drawdown_after_peak_pct":-57.37,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"insufficient_forward_window":false,"calibration_usable":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|281820|Stage2-Actionable|2024-06-03","source_url":"https://www.kctech.com/eng/page/product1.php","case_role":"front_end_equipment_positive_high_mae_control","current_profile_verdict":"current_profile_should_cap_yellow_green_due_high_mae"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_281820_20240603_STAGE2A","trigger_id":"C10_STAGE2A_281820_20240603_CMP_WET_CLEANING_SUPPLIER_BRIDGE","symbol":"281820","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","stage_label_before":"Stage2-Actionable","stage_label_after":"Stage2-Actionable","weighted_score_before":76,"weighted_score_after":76,"raw_component_scores_before":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"raw_component_scores_after":{"eps_fcf_explosion":22,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"error_type":"valid_stage2a_but_high_mae_green_blocker","score_return_alignment_label":"current_profile_should_cap_yellow_green_due_high_mae","MFE_90D_pct":51.67,"MAE_90D_pct":-24.29,"MFE_180D_pct":51.67,"MAE_180D_pct":-35.35}
{"row_type":"case","case_id":"C10_240810_20241205_4B","symbol":"240810","company":"Wonik IPS","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_REPAIR","case_role":"bad_headline_not_hard4c_positive_reopen","evidence_family":"capex_revision_down_with_process_upgrade_offset","source_url":"https://www.asiae.co.kr/en/article/2024120507561579363","calibration_usable":true,"narrative_only":false}
{"row_type":"trigger","case_id":"C10_240810_20241205_4B","trigger_id":"C10_4B_240810_20241205_CAPEX_REVISION_DOWN_BUT_PROCESS_UPGRADE_OFFSET","symbol":"240810","company":"Wonik IPS","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"4B","trigger_date":"2024-12-05","entry_date":"2024-12-05","entry_price":21800.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","MFE_30D_pct":13.3,"MAE_30D_pct":-2.98,"MFE_90D_pct":30.73,"MAE_90D_pct":-4.59,"MFE_180D_pct":98.85,"MAE_180D_pct":-4.59,"peak_180D_date":"2025-08-13","peak_180D_price":43350.0,"trough_180D_date":"2025-04-09","trough_180D_price":20800.0,"drawdown_after_peak_pct":-12.23,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"insufficient_forward_window":false,"calibration_usable":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|240810|4B|2024-12-05","source_url":"https://www.asiae.co.kr/en/article/2024120507561579363","case_role":"bad_headline_not_hard4c_positive_reopen","current_profile_verdict":"current_profile_hard4c_too_aggressive_if_no_offset_check"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_240810_20241205_4B","trigger_id":"C10_4B_240810_20241205_CAPEX_REVISION_DOWN_BUT_PROCESS_UPGRADE_OFFSET","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","stage_label_before":"4C","stage_label_after":"4B","weighted_score_before":45,"weighted_score_after":63,"raw_component_scores_before":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"raw_component_scores_after":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"error_type":"hard4c_too_early_when_process_upgrade_offset_exists","score_return_alignment_label":"current_profile_hard4c_too_aggressive_if_no_offset_check","MFE_90D_pct":30.73,"MAE_90D_pct":-4.59,"MFE_180D_pct":98.85,"MAE_180D_pct":-4.59}
{"row_type":"case","case_id":"C10_084370_20241031_4B","symbol":"084370","company":"Eugene Tech","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_REPAIR","case_role":"moderate_recovery_requires_order_conversion","evidence_family":"memory_capex_cycle_without_precise_supplier_order","source_url":"https://www.eugenetech.co.kr/eng/main/main.php","calibration_usable":true,"narrative_only":false}
{"row_type":"trigger","case_id":"C10_084370_20241031_4B","trigger_id":"C10_4B_084370_20241031_MEMORY_RECOVERY_WITHOUT_ORDER_DETAIL","symbol":"084370","company":"Eugene Tech","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"4B","trigger_date":"2024-10-31","entry_date":"2024-10-31","entry_price":37400.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","MFE_30D_pct":6.55,"MAE_30D_pct":-15.64,"MFE_90D_pct":32.22,"MAE_90D_pct":-18.98,"MFE_180D_pct":32.22,"MAE_180D_pct":-18.98,"peak_180D_date":"2025-02-19","peak_180D_price":49450.0,"trough_180D_date":"2024-12-20","trough_180D_price":30300.0,"drawdown_after_peak_pct":-37.61,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"insufficient_forward_window":false,"calibration_usable":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|084370|4B|2024-10-31","source_url":"https://www.eugenetech.co.kr/eng/main/main.php","case_role":"moderate_recovery_requires_order_conversion","current_profile_verdict":"current_profile_should_hold_at_4b_or_stage2_not_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_084370_20241031_4B","trigger_id":"C10_4B_084370_20241031_MEMORY_RECOVERY_WITHOUT_ORDER_DETAIL","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","stage_label_before":"Stage2-Actionable","stage_label_after":"4B","weighted_score_before":75,"weighted_score_after":64,"raw_component_scores_before":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"raw_component_scores_after":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"error_type":"generic_memory_beta_needs_order_conversion","score_return_alignment_label":"current_profile_should_hold_at_4b_or_stage2_not_green","MFE_90D_pct":32.22,"MAE_90D_pct":-18.98,"MFE_180D_pct":32.22,"MAE_180D_pct":-18.98}
{"row_type":"case","case_id":"C10_036930_20241031_STAGE2","symbol":"036930","company":"Jusung Engineering","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_REPAIR","case_role":"ald_optional_but_not_actionable_without_conversion","evidence_family":"ald_equipment_customer_capex_optionality","source_url":"https://m.thebell.co.kr/m/newsview.asp?newskey=202402261105163080101554&svccode=","calibration_usable":true,"narrative_only":false}
{"row_type":"trigger","case_id":"C10_036930_20241031_STAGE2","trigger_id":"C10_STAGE2_036930_20241031_ALD_CAPEX_OPTIONALITY_NOT_ACTIONABLE","symbol":"036930","company":"Jusung Engineering","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage2","trigger_date":"2024-10-31","entry_date":"2024-10-31","entry_price":31000.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv","MFE_30D_pct":9.84,"MAE_30D_pct":-16.61,"MFE_90D_pct":29.03,"MAE_90D_pct":-16.61,"MFE_180D_pct":40.0,"MAE_180D_pct":-16.61,"peak_180D_date":"2025-03-21","peak_180D_price":43400.0,"trough_180D_date":"2024-12-02","trough_180D_price":25850.0,"drawdown_after_peak_pct":-33.41,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"insufficient_forward_window":false,"calibration_usable":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|036930|Stage2|2024-10-31","source_url":"https://m.thebell.co.kr/m/newsview.asp?newskey=202402261105163080101554&svccode=","case_role":"ald_optional_but_not_actionable_without_conversion","current_profile_verdict":"current_profile_stage2a_too_loose_if_no_customer_order"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_036930_20241031_STAGE2","trigger_id":"C10_STAGE2_036930_20241031_ALD_CAPEX_OPTIONALITY_NOT_ACTIONABLE","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","stage_label_before":"Stage2-Actionable","stage_label_after":"Stage2","weighted_score_before":74,"weighted_score_after":68,"raw_component_scores_before":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"raw_component_scores_after":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"error_type":"stage2_actionable_false_positive_prevention","score_return_alignment_label":"current_profile_stage2a_too_loose_if_no_customer_order","MFE_90D_pct":29.03,"MAE_90D_pct":-16.61,"MFE_180D_pct":40.0,"MAE_180D_pct":-16.61}
{"row_type":"case","case_id":"C10_319660_20240814_4B","symbol":"319660","company":"PSK","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_REPAIR","case_role":"late_beta_extension_counterexample","evidence_family":"generic_equipment_beta_after_recovery_headline","source_url":"https://www.pskinc.com/en/ir/financial-status/","calibration_usable":true,"narrative_only":false}
{"row_type":"trigger","case_id":"C10_319660_20240814_4B","trigger_id":"C10_4B_319660_20240814_BETA_EXTENSION_WITH_WEAK_FORWARD_PATH","symbol":"319660","company":"PSK","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"4B","trigger_date":"2024-08-14","entry_date":"2024-08-14","entry_price":30450.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","MFE_30D_pct":5.09,"MAE_30D_pct":-32.68,"MFE_90D_pct":5.09,"MAE_90D_pct":-48.93,"MFE_180D_pct":5.09,"MAE_180D_pct":-48.93,"peak_180D_date":"2024-08-16","peak_180D_price":32000.0,"trough_180D_date":"2024-12-02","trough_180D_price":15550.0,"drawdown_after_peak_pct":-51.41,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"insufficient_forward_window":false,"calibration_usable":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|319660|4B|2024-08-14","source_url":"https://www.pskinc.com/en/ir/financial-status/","case_role":"late_beta_extension_counterexample","current_profile_verdict":"current_profile_should_route_to_local_4b_not_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_319660_20240814_4B","trigger_id":"C10_4B_319660_20240814_BETA_EXTENSION_WITH_WEAK_FORWARD_PATH","symbol":"319660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","stage_label_before":"Stage2-Actionable","stage_label_after":"4B","weighted_score_before":73,"weighted_score_after":55,"raw_component_scores_before":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"raw_component_scores_after":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"error_type":"late_beta_price_extension_false_positive","score_return_alignment_label":"current_profile_should_route_to_local_4b_not_actionable","MFE_90D_pct":5.09,"MAE_90D_pct":-48.93,"MFE_180D_pct":5.09,"MAE_180D_pct":-48.93}
{"row_type":"case","case_id":"C10_095610_20241114_STAGE2A","symbol":"095610","company":"TES","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_SUPPLIER_ORDER_CONVERSION_AND_4B_REOPEN_REPAIR","case_role":"trough_reopen_positive_control","evidence_family":"front_end_memory_equipment_recovery_after_customer_cycle","source_url":"https://dealsite.co.kr/articles/123029","calibration_usable":true,"narrative_only":false}
{"row_type":"trigger","case_id":"C10_095610_20241114_STAGE2A","trigger_id":"C10_STAGE2A_095610_20241114_MEMORY_RECOVERY_TROUGH_ORDER_CONVERSION","symbol":"095610","company":"TES","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-14","entry_date":"2024-11-14","entry_price":14370.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","MFE_30D_pct":13.43,"MAE_30D_pct":-8.91,"MFE_90D_pct":70.84,"MAE_90D_pct":-8.91,"MFE_180D_pct":95.89,"MAE_180D_pct":-8.91,"peak_180D_date":"2025-07-16","peak_180D_price":28150.0,"trough_180D_date":"2024-12-09","trough_180D_price":13090.0,"drawdown_after_peak_pct":-17.41,"window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"insufficient_forward_window":false,"calibration_usable":true,"hard_duplicate_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|095610|Stage2-Actionable|2024-11-14","source_url":"https://dealsite.co.kr/articles/123029","case_role":"trough_reopen_positive_control","current_profile_verdict":"current_profile_too_late_if_prior_4b_not_cleared"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C10_095610_20241114_STAGE2A","trigger_id":"C10_STAGE2A_095610_20241114_MEMORY_RECOVERY_TROUGH_ORDER_CONVERSION","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","stage_label_before":"4B","stage_label_after":"Stage2-Actionable","weighted_score_before":61,"weighted_score_after":79,"raw_component_scores_before":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"raw_component_scores_after":{"eps_fcf_explosion":22,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":5,"information_confidence":19},"error_type":"stage2a_reopen_after_trough_when_customer_cycle_improves","score_return_alignment_label":"current_profile_too_late_if_prior_4b_not_cleared","MFE_90D_pct":70.84,"MAE_90D_pct":-8.91,"MFE_180D_pct":95.89,"MAE_180D_pct":-8.91}
{"row_type":"residual_contribution","round":"R2","loop":"200","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":8,"reused_case_count":0,"unique_symbol_count":8,"positive_or_reopen_count":5,"counterexample_or_4b_count":3,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","earlier_thesis_break_watch","hard_4c_confirmation"],"residual_error_types_found":["supplier_order_conversion_missed_positive","generic_memory_beta_false_positive","hard4c_too_early_when_offset_exists","high_mae_true_supplier_bridge_needs_green_blocker"],"loop_contribution_label":"C10_supplier_order_conversion_and_4b_reopen_quality_repair","do_not_propose_new_weight_delta":false,"production_scoring_changed":false,"shadow_weight_only":true}
```

## 12. Shadow Weight Rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,1.00,1.12,+0.12,"C10 generic memory beta should require supplier-level order/revenue/qualification bridge before Stage2-Actionable","prevents late beta rows such as 319660_20240814 while preserving supplier-specific positives",C10_STAGE2A_031980_20240531_HBM_REFLOW_MICRON_SUPPLIER_BRIDGE|C10_4B_319660_20240814_BETA_EXTENSION_WITH_WEAK_FORWARD_PATH,8,8,3,medium,canonical_shadow_only,"not production; Green strictness unchanged"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,1.00,1.10,+0.10,"negative capex/earnings headlines need offset-quality check before hard 4C","keeps Wonik IPS 2024-12-05 as 4B/watch rather than false hard 4C",C10_4B_240810_20241205_CAPEX_REVISION_DOWN_BUT_PROCESS_UPGRADE_OFFSET,8,8,3,medium,canonical_shadow_only,"not production; hard 4C requires thesis break"
shadow_weight,stage2_reopen_after_4b,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0.00,1.00,+1.00,"prior 4B can clear back to Stage2-Actionable when supplier/customer conversion returns","TES and Wonik paths show local trough/reopen behavior after broad cycle fear",C10_STAGE2A_095610_20241114_MEMORY_RECOVERY_TROUGH_ORDER_CONVERSION|C10_4B_240810_20241205_CAPEX_REVISION_DOWN_BUT_PROCESS_UPGRADE_OFFSET,8,8,3,medium,canonical_shadow_only,"not production; clearing rule only"
```

## 13. Batch Ingest Self-Audit

```text
filename_matches_standard_v12_regex: true
filename_round_matches_metadata_round: true
filename_loop_matches_metadata_loop: true
round_sector_consistency: pass
canonical_archetype_valid: true
large_sector_id_valid: true
r13_special_rule_applicable: false

must_use_actual_stock_web_1D_OHLC: pass
entry_price_present_every_trigger: pass
MFE_MAE_30_90_180_present_every_trigger: pass
peak_date_present_every_trigger: pass
drawdown_after_peak_present_every_trigger: pass
price_source_validation_present: pass
corporate_action_window_checked: pass
insufficient_forward_window_checked: pass

hard_duplicate_key_rule:
  key_format: canonical_archetype_id + symbol + trigger_type + entry_date
  duplicate_keys_with_prior_loop192_user_session: 0
  duplicate_keys_within_batch: 0

source_proxy_only_count: 0
evidence_url_pending_count: 0
narrative_only_count: 0
production_scoring_changed: false
shadow_weight_only: true
```

## 14. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run. Later coding agent may parse this MD as a v12 result. If accepted, add only a canonical-scope shadow/profile candidate for C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:

- Require supplier-level order/revenue/qualification bridge before C10 Stage2-Actionable.
- Keep broad customer memory recovery/capex headlines at Stage2 or local 4B watch unless supplier conversion exists.
- Add a 4B clearing path back to Stage2-Actionable when supplier conversion reappears after a prior watch/bad headline period.
- Do not loosen global Stage3-Green thresholds.
- Do not change production scoring immediately.
- Do not scan live candidates or create trading signals.
```

## 15. Next Research State

```text
completed_round = R2
completed_loop = 200
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = quality reinforcement after all canonical archetypes >80 rows; C10 supplier-order conversion and 4B reopen repair
next_recommended_archetypes =
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE_FCF_COUNTEREXAMPLE_REPAIR
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_OFFSET_QUALITY_REPAIR
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_HARD_4C_DIRECT_BREAK_PAIR
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
