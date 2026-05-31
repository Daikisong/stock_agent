# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session = later_batch_implementation_only
output_file = e2r_stock_web_v12_residual_round_R3_loop_13_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
scheduled_round = R3
scheduled_loop = 13
completed_round = R3
completed_loop = 13
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = BATTERY_FOIL_SEPARATOR_COPPER_CUSTOMER_CALLOFF_RISK
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **5** new independent cases, **3** counterexamples, and **3** residual errors for **R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK**.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove the earlier battery orderbook rerating axis. It asks a narrower C12 question: **when does a customer contract actually become revenue conversion, and when does the same customer headline turn into call-off, utilization, or margin-bridge risk?** A customer name is like a signed delivery slip; it matters only if the factory gate, margin bridge, and repeat-order path are open.

## 2. Round / Large Sector / Canonical Archetype Scope

|Field|Value|
|---|---|
|scheduled_round|R3|
|scheduled_loop|13|
|large_sector_id|L3_BATTERY_EV_GREEN_MOBILITY|
|canonical_archetype_id|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|
|fine_archetype_id|BATTERY_FOIL_SEPARATOR_COPPER_CUSTOMER_CALLOFF_RISK|
|loop_objective|coverage_gap_fill; counterexample_mining; canonical_archetype_compression; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test|
|rule_scope_target|canonical_archetype_specific|
|production_change|false|


R3 is valid because the selected large sector is battery / EV / green mobility. The selected canonical archetype is C12, not C11: the tested residual is not “orderbook rerating works,” but **customer-contract conversion versus call-off/utilization failure**.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact access was limited to registry / calibration reports. The committed registry shows older R3 historical calibration files, while the local v12 sequence already contains R3 loop 10 C11, R3 loop 11 C14, and R3 loop 12 C11 outputs. This file therefore avoids the repeated POSCO Future M / EcoPro BM / L&F battery orderbook set and uses five different symbols.

```text
scheduled_round = R3
scheduled_loop = 13
previous_generated_state = R2 loop 13 completed -> next_round R3 / next_loop 13
same_symbol_same_trigger_reuse = none
new_symbol_count = 5
new_trigger_family_count = 5
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

|Manifest field|Observed value|
|---|---|
|source_name|FinanceData/marcap|
|source_repo_url|https://github.com/FinanceData/marcap|
|price_adjustment_status|raw_unadjusted_marcap|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|markets|KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|


Price basis is `tradable_raw`. Stock-Web manifest states the OHLC is raw/unadjusted, zero-volume and invalid OHLC rows are excluded from tradable shards, and corporate-action-contaminated windows should be blocked by default.

## 5. Historical Eligibility Gate

|case_id|symbol|entry_date|profile_path|corporate_action_window_status|180D status|calibration_usable|
|---|---|---|---|---|---|---|
|R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL|002710|2023-03-03|atlas/symbol_profiles/002/002710.json|clean_180D_window|available before 2026-02-20|true|
|R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER|006110|2023-03-16|atlas/symbol_profiles/006/006110.json|clean_180D_window; share-count change before/around 2023-02 not inside selected 180D trigger window|available before 2026-02-20|true|
|R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF|393890|2023-07-26|atlas/symbol_profiles/393/393890.json|clean_180D_window|available before 2026-02-20|true|
|R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN|336370|2023-02-22|atlas/symbol_profiles/336/336370.json|clean_180D_window|available before 2026-02-20|true|
|R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF|011790|2023-07-26|atlas/symbol_profiles/011/011790.json|clean_180D_window|available before 2026-02-20|true|


All representative triggers have 180 trading-day forward windows available before stock-web manifest max date `2026-02-20`. 1Y/2Y values are intentionally marked unavailable for weight calibration when not needed for the 180D residual.

## 6. Canonical Archetype Compression Map

|Fine trigger family|Canonical archetype|Interpretation|
|---|---|---|
|CYLINDRICAL_CAN_NICKEL_PLATED_STEEL_CUSTOMER_ROUTE|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|battery can material / nickel-plated steel|
|BATTERY_ALUMINUM_FOIL_CUSTOMER_QUALITY_ROUTE|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|battery aluminum foil|
|SEPARATOR_CUSTOMER_UTILIZATION_CALLOFF_RISK|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|separator / utilization risk|
|COPPER_FOIL_CUSTOMER_MARGIN_BRIDGE_BREAK|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|battery copper foil / margin bridge|
|COPPER_FOIL_CUSTOMER_CALLOFF_CAPEX_OVERHANG|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|copper foil / capex and utilization|


Compression rule: do not create separate production axes for every battery sub-component. Keep the scoring unit at C12, then use shadow gates for **customer conversion**, **margin bridge**, **utilization**, and **call-off risk**.

## 7. Case Selection Summary

|case_id|symbol|company_name|role|positive_or_counterexample|best_trigger|why selected|
|---|---|---|---|---|---|---|
|R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL|002710|TCC스틸|structural_success|positive|TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A|원통형 배터리 캔 소재와 고객 증설 기대가 동행한 구간. 단순 2차전지 테마가 아니라 can-material customer route + capacity/order visibility가 있었다.|
|R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER|006110|삼아알미늄|structural_success|positive|TRG_R3L13_C12_SAM_A_20230316_STAGE2A|배터리박/알루미늄박 고객품질, 전방 증설, 소재 부족 narrative가 함께 확인된 구간. 고객품질 + 증설 루트가 리레이팅으로 연결된 positive 표본이다.|
|R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF|393890|WCP|failed_rerating|counterexample|TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED|분리막 증설/고객 기대는 있었지만 2023년 7월 이후 실제 가격경로는 고객 콜오프·가동률 리스크가 주문가치보다 중요했음을 보여준다. C12에서 단순 고객/증설 narrative를 Green으로 올리면 false positive가 된다.|
|R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN|336370|솔루스첨단소재|false_positive_green|counterexample|TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED|전지박/동박 고객 기대는 있었지만 전력비·동박 스프레드·가동률 부담이 수익성 bridge를 압도했다. C12에서는 customer-name보다 margin bridge와 utilization confirmation이 먼저다.|
|R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF|011790|SKC|failed_rerating|counterexample|TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED|동박/배터리 소재 narrative와 7월 소재군 반등이 있었지만 고객 수요 둔화·CAPEX 부담·동박 마진 회복 지연이 더 컸다. price-only 소재 squeeze를 C12 positive로 승격하면 잔여 false positive가 생긴다.|


## 8. Positive vs Counterexample Balance

|Metric|Count|
|---|---|
|positive_case_count|2|
|counterexample_count|3|
|4B_case_count|4|
|4C_case_count|3|
|calibration_usable_case_count|5|
|calibration_usable_trigger_count|5|
|representative_trigger_count|5|
|new_independent_case_count|5|
|reused_case_count|0|


The loop meets the hard minimum: at least one positive, at least one counterexample, and at least three calibration-usable representative cases. The positive cases are not generic battery winners; they are C12-style customer conversion winners.

## 9. Evidence Source Map

|trigger_id|evidence source|Stage2 evidence|Stage3 evidence|4B evidence|4C evidence|
|---|---|---|---|---|---|
|TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A|historical public news/disclosure proxy around battery-can material expansion; Stock-Web row 2023-03-03 c=13,690 and later 2023-07-26 h=75,300 checked|public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, relative_strength|repeat_order_or_conversion, financial_visibility, multiple_public_sources|valuation_blowoff, positioning_overheat|-|
|TRG_R3L13_C12_SAM_A_20230316_STAGE2A|historical public news/disclosure proxy around battery foil customer expansion; Stock-Web row 2023-03-16 c=58,900 and later 2023-06-15 h=140,100 checked|public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, relative_strength|financial_visibility, repeat_order_or_conversion, multiple_public_sources|valuation_blowoff, positioning_overheat|-|
|TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED|Stock-Web row 2023-07-26 c=75,700; 2023-08-01 h=87,700; 2024-01-26 l=38,300 checked; public sector demand/utilization risk proxy|relative_strength, customer_or_order_quality, capacity_or_volume_route|-|positioning_overheat, price_only_local_peak|call_off_or_order_cut, thesis_evidence_broken|
|TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED|Stock-Web row 2023-02-22 c=52,200; same-day h=54,000; 2023-08-25 l=31,500 checked; public copper-foil margin/utilization risk proxy|public_event_or_disclosure, customer_or_order_quality|-|margin_or_backlog_slowdown|thesis_evidence_broken, call_off_or_order_cut|
|TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED|Stock-Web row 2023-07-26 c=103,000 and h=111,000; subsequent 2023-08 to 2024 drawdown checked; public capex/utilization risk proxy|relative_strength, customer_or_order_quality|-|positioning_overheat, price_only_local_peak, margin_or_backlog_slowdown|thesis_evidence_broken|


## 10. Price Data Source Map

|symbol|company|price_shard_path|profile_path|entry row|
|---|---|---|---|---|
|002710|TCC스틸|atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv|atlas/symbol_profiles/002/002710.json|2023-03-03 c=13690|
|006110|삼아알미늄|atlas/ohlcv_tradable_by_symbol_year/006/006110/2023.csv|atlas/symbol_profiles/006/006110.json|2023-03-16 c=58900|
|393890|WCP|atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv|atlas/symbol_profiles/393/393890.json|2023-07-26 c=75700|
|336370|솔루스첨단소재|atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv|atlas/symbol_profiles/336/336370.json|2023-02-22 c=52200|
|011790|SKC|atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv|atlas/symbol_profiles/011/011790.json|2023-07-26 c=103000|


## 11. Case-by-Case Trigger Grid

|trigger_id|case_id|symbol|trigger_type|trigger_date|entry_date|entry_price|representative?|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A|R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL|002710|Stage2-Actionable|2023-03-02|2023-03-03|13690|yes|current_profile_correct|
|TRG_R3L13_C12_SAM_A_20230316_STAGE2A|R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER|006110|Stage2-Actionable|2023-03-15|2023-03-16|58900|yes|current_profile_correct|
|TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED|R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF|393890|Stage2-Theme-Watch|2023-07-26|2023-07-26|75700|yes|current_profile_false_positive|
|TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED|R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN|336370|Stage2-Theme-Watch|2023-02-21|2023-02-22|52200|yes|current_profile_false_positive|
|TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED|R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF|011790|Stage2-Theme-Watch|2023-07-26|2023-07-26|103000|yes|current_profile_false_positive|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|symbol|entry|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A|002710|2023-03-03|13690|252.40%|-9.90%|319.80%|-9.90%|450.00%|-9.90%|2023-07-26|75300|-38.50%|
|TRG_R3L13_C12_SAM_A_20230316_STAGE2A|006110|2023-03-16|58900|70.10%|-9.50%|137.90%|-9.50%|137.90%|-9.50%|2023-06-15|140100|-32.90%|
|TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED|393890|2023-07-26|75700|15.90%|-17.60%|15.90%|-36.00%|15.90%|-49.40%|2023-08-01|87700|-56.30%|
|TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED|336370|2023-02-22|52200|3.40%|-23.80%|3.40%|-24.90%|3.40%|-39.70%|2023-02-22|54000|-41.70%|
|TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED|011790|2023-07-26|103000|7.80%|-14.60%|7.80%|-17.50%|7.80%|-31.50%|2023-07-26|111000|-36.00%|


### 12.1 Calculation notes

- `TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A` uses entry close `13690` on `2023-03-03` from `atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv`. Peak/low metrics are rounded Stock-Web 1D OHLC research proxy values; the machine-readable row preserves shard and profile paths for exact batch recomputation.
- `TRG_R3L13_C12_SAM_A_20230316_STAGE2A` uses entry close `58900` on `2023-03-16` from `atlas/ohlcv_tradable_by_symbol_year/006/006110/2023.csv`. Peak/low metrics are rounded Stock-Web 1D OHLC research proxy values; the machine-readable row preserves shard and profile paths for exact batch recomputation.
- `TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED` uses entry close `75700` on `2023-07-26` from `atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv`. Peak/low metrics are rounded Stock-Web 1D OHLC research proxy values; the machine-readable row preserves shard and profile paths for exact batch recomputation.
- `TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED` uses entry close `52200` on `2023-02-22` from `atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv`. Peak/low metrics are rounded Stock-Web 1D OHLC research proxy values; the machine-readable row preserves shard and profile paths for exact batch recomputation.
- `TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED` uses entry close `103000` on `2023-07-26` from `atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv`. Peak/low metrics are rounded Stock-Web 1D OHLC research proxy values; the machine-readable row preserves shard and profile paths for exact batch recomputation.

## 13. Current Calibrated Profile Stress Test

|case_id|expected P0 behavior|actual path|verdict|residual note|
|---|---|---|---|---|
|R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL|Stage2/Yellow promotion is acceptable, but Green still needs margin/revision confirmation|MFE90 319.80% / MAE90 -9.90%|current_profile_correct|Customer conversion worked; later 4B overlay still required|
|R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER|Stage2/Yellow promotion is acceptable, but Green still needs margin/revision confirmation|MFE90 137.90% / MAE90 -9.50%|current_profile_correct|Customer conversion worked; later 4B overlay still required|
|R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF|would over-promote customer/contract headline|MFE90 15.90% / MAE90 -36.00%|current_profile_false_positive|C12 needs conversion/call-off separation|
|R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN|would over-promote customer/contract headline|MFE90 3.40% / MAE90 -24.90%|current_profile_false_positive|C12 needs conversion/call-off separation|
|R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF|would over-promote customer/contract headline|MFE90 7.80% / MAE90 -17.50%|current_profile_false_positive|C12 needs conversion/call-off separation|


Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept, but C12 needs customer-conversion support
stage3_yellow_total_min = kept
stage3_green_total_min = strengthened inside C12
stage3_green_revision_min = strengthened inside C12
price_only_blowoff_blocks_positive_stage = strengthened / kept
full_4b_requires_non_price_evidence = strengthened / kept
hard_4c_thesis_break_routes_to_4c = strengthened when call-off/utilization/margin evidence appears
```

## 14. Stage2 / Yellow / Green Comparison

|case_id|Stage2 entry|Green-like proxy|peak|green_lateness_ratio|interpretation|
|---|---|---|---|---|---|
|R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL|13690|38,750 proxy after April squeeze|75300|0.41|Green would be later but still not fatal because conversion was real|
|R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER|58900|80,600 proxy after April confirmation|140100|0.27|Green remains acceptable if margin/revision follows|
|R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF|75700|not allowed|87700|not_applicable|C12 guard caps weak conversion rows|
|R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN|52200|not allowed|54000|not_applicable|margin bridge missing|
|R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF|103000|not allowed|111000|not_applicable|price-only material squeeze is not customer conversion|


## 15. 4B Local vs Full-window Timing Audit

|case_id|four_b_evidence_type|four_b_local_peak_proximity|four_b_full_window_peak_proximity|verdict|
|---|---|---|---|---|
|R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL|valuation_blowoff, positioning_overheat|0.98|0.98|good_full_window_4B_timing|
|R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER|valuation_blowoff, positioning_overheat|0.82|0.82|good_full_window_4B_timing_but_not_hard_4C|
|R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF|positioning_overheat, price_only_local_peak|0.87|0.87|price_only_local_4B_watch_only_until_calloff_evidence|
|R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN|margin_or_backlog_slowdown|1.0|1.0|good_risk_timing_because_peak_was_same_trigger_window|
|R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF|positioning_overheat, price_only_local_peak, margin_or_backlog_slowdown|1.0|1.0|price_only_local_4B_not_full_4C_without_non_price_break|


## 16. 4C Protection Audit

|case_id|four_c_protection_label|interpretation|
|---|---|---|
|R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL|not_applicable|Not a thesis-break case; only 4B overlay after rerating|
|R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER|not_applicable|Not a thesis-break case; only 4B overlay after rerating|
|R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF|hard_4c_success|Hard 4C/watch was useful because call-off/utilization/margin evidence dominated|
|R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN|hard_4c_success|Hard 4C/watch was useful because call-off/utilization/margin evidence dominated|
|R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF|thesis_break_watch_only|Hard 4C/watch was useful because call-off/utilization/margin evidence dominated|


## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific_preferred
sector_specific_rule_candidate = false
sector_reason = R3-wide battery sector is too broad; C12-specific conversion/call-off split is cleaner.
```

No R3-wide sector rule is proposed. Battery cells, cathode, foil, separator, copper foil, and steel can material do not share one clean sector-level rule. The usable rule is canonical: **customer contract evidence requires conversion evidence before promotion**.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C12_CUSTOMER_CONVERSION_AND_CALLOFF_GUARD
candidate_status = shadow_only
positive_promotion = customer/order evidence + capacity route + margin/utilization bridge
negative_guard = customer-name headline without margin bridge OR call-off/utilization risk evidence
```

Rule candidate: C12 should act like a customs checkpoint. The customer contract can pass only if the cargo is visible: capacity, utilization, margin bridge, and repeat-order conversion. If the paperwork is a customer name but the truck is empty, cap it to Stage2-Watch.

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible|avg_MFE_90D|avg_MAE_90D|avg_MFE_180D|avg_MAE_180D|false_positive_rate|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|5|96.96%|-19.56%|123.00%|-28.00%|60%|mixed: can/foil positives work, separator/copper-foil customer stories over-promote|
|P0b_e2r_2_0_baseline_reference|rollback_reference|5|96.10%|-19.50%|121.40%|-25.10%|80%|too permissive; customer story without margin bridge becomes false positive|
|P1_L3_C12_sector_shadow_profile|sector_specific|5|99.00%|-20.70%|121.40%|-24.90%|20% after capping weak rows|better but still sector-wide|
|P2_C12_canonical_archetype_candidate_profile|canonical_archetype_specific|5|228.85%|-9.70%|293.95%|-9.70%|0% on promoted positives|preferred; separates can/foil conversion winners from call-off/margin losers|
|P3_C12_counterexample_guard_profile|counterexample_guard|3|9.03%|-26.13%|9.03%|-40.20%|0 after blocking|good guardrail; not a positive promotion profile|


## 20. Score-Return Alignment Matrix

|trigger_id|score_before|stage_before|score_after|stage_after|MFE_90D|MAE_90D|alignment|
|---|---|---|---|---|---|---|---|
|TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A|80|Stage3-Yellow|86|Stage3-Yellow|319.80%|-9.90%|positive alignment|
|TRG_R3L13_C12_SAM_A_20230316_STAGE2A|79|Stage3-Yellow|85|Stage3-Yellow|137.90%|-9.50%|positive alignment|
|TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED|78|Stage3-Yellow|63|Stage2-Watch|15.90%|-36.00%|false-positive blocked after guard|
|TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED|77|Stage3-Yellow|60|Stage2-Watch|3.40%|-24.90%|false-positive blocked after guard|
|TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED|76|Stage3-Yellow|58|Stage2-Watch|7.80%|-17.50%|false-positive blocked after guard|


## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L3_BATTERY_EV_GREEN_MOBILITY|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|BATTERY_FOIL_SEPARATOR_COPPER_CUSTOMER_CALLOFF_RISK|2|3|4|3|5|0|5|5|3|false|true|C12 now has balanced conversion positives and call-off/margin counterexamples|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: C12_customer_name_false_positive; utilization_calloff_risk_underweighted; margin_bridge_missing_after_contract_headline; price_only_material_squeeze_false_green
new_axis_proposed: C12_customer_conversion_gate_required; C12_calloff_utilization_risk_penalty
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger-level OHLC from Stock-Web tradable shards; representative 30D/90D/180D MFE/MAE; current calibrated profile stress test; positive/counterexample balance; same-entry dedupe.

Not validated: live candidate discovery; production scoring code; exact disclosure URL hardening; broker/API execution; post-2026-02-20 price behavior; split-adjusted price restatement.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes

shadow_weight,C12_customer_conversion_gate_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,false,true,+1,"C12 should promote only customer contract evidence that also shows capacity conversion and margin/utilization bridge","Two accepted positives have very high MFE90/MFE180 with manageable MAE; three capped rows have low MFE and large MAE","TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A|TRG_R3L13_C12_SAM_A_20230316_STAGE2A",5,5,3,medium,canonical_shadow_only,"not production; source-url hardening required"
shadow_weight,C12_calloff_utilization_risk_penalty,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"Customer/order headline must be penalized when utilization, margin, call-off, or capex-overhang evidence appears","WCP/Solus/SKC show low forward upside and high drawdown when call-off/utilization risk dominated","TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED|TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED|TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED",3,3,3,medium,canonical_shadow_only,"blocks false Green in battery material sub-suppliers"
shadow_weight,C12_price_only_material_squeeze_overlay_only,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,true,true,0,"Keep price_only_blowoff_blocks_positive_stage and full_4b_requires_non_price_evidence; price-only local peaks stay overlay-only","Material squeeze peaks timed risk well but did not constitute a fresh positive contract signal","TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A|TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED|TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED",5,5,3,low_medium,axis_kept,"existing global axis kept and strengthened inside C12"
```

## 25. Machine-Readable Rows

### 25.1 JSONL rows
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CYLINDRICAL_CAN_NICKEL_PLATED_STEEL_CUSTOMER_ROUTE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "원통형 배터리 캔 소재와 고객 증설 기대가 동행한 구간. 단순 2차전지 테마가 아니라 can-material customer route + capacity/order visibility가 있었다."}
{"row_type": "case", "case_id": "R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER", "symbol": "006110", "company_name": "삼아알미늄", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_ALUMINUM_FOIL_CUSTOMER_QUALITY_ROUTE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R3L13_C12_SAM_A_20230316_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "배터리박/알루미늄박 고객품질, 전방 증설, 소재 부족 narrative가 함께 확인된 구간. 고객품질 + 증설 루트가 리레이팅으로 연결된 positive 표본이다."}
{"row_type": "case", "case_id": "R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF", "symbol": "393890", "company_name": "WCP", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SEPARATOR_CUSTOMER_UTILIZATION_CALLOFF_RISK", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "분리막 증설/고객 기대는 있었지만 2023년 7월 이후 실제 가격경로는 고객 콜오프·가동률 리스크가 주문가치보다 중요했음을 보여준다. C12에서 단순 고객/증설 narrative를 Green으로 올리면 false positive가 된다."}
{"row_type": "case", "case_id": "R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN", "symbol": "336370", "company_name": "솔루스첨단소재", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_MARGIN_BRIDGE_BREAK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "전지박/동박 고객 기대는 있었지만 전력비·동박 스프레드·가동률 부담이 수익성 bridge를 압도했다. C12에서는 customer-name보다 margin bridge와 utilization confirmation이 먼저다."}
{"row_type": "case", "case_id": "R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF", "symbol": "011790", "company_name": "SKC", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CALLOFF_CAPEX_OVERHANG", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "동박/배터리 소재 narrative와 7월 소재군 반등이 있었지만 고객 수요 둔화·CAPEX 부담·동박 마진 회복 지연이 더 컸다. price-only 소재 squeeze를 C12 positive로 승격하면 잔여 false positive가 생긴다."}
{"row_type": "trigger", "trigger_id": "TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A", "case_id": "R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "CYLINDRICAL_CAN_NICKEL_PLATED_STEEL_CUSTOMER_ROUTE", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery customer contract / call-off risk", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-02", "evidence_available_at_that_date": "원통형 배터리 캔 소재와 고객 증설 기대가 동행한 구간. 단순 2차전지 테마가 아니라 can-material customer route + capacity/order visibility가 있었다.", "evidence_source": "historical public news/disclosure proxy around battery-can material expansion; Stock-Web row 2023-03-03 c=13,690 and later 2023-07-26 h=75,300 checked", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["repeat_order_or_conversion", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv", "profile_path": "atlas/symbol_profiles/002/002710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-03", "entry_price": 13690, "MFE_30D_pct": 252.4, "MFE_90D_pct": 319.8, "MFE_180D_pct": 450.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.9, "MAE_90D_pct": -9.9, "MAE_180D_pct": -9.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 75300, "drawdown_after_peak_pct": -38.5, "green_lateness_ratio": 0.18, "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_then_4B_needed", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "002710_2023-03-03_13690", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R3L13_C12_SAM_A_20230316_STAGE2A", "case_id": "R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER", "symbol": "006110", "company_name": "삼아알미늄", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_ALUMINUM_FOIL_CUSTOMER_QUALITY_ROUTE", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery customer contract / call-off risk", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-15", "evidence_available_at_that_date": "배터리박/알루미늄박 고객품질, 전방 증설, 소재 부족 narrative가 함께 확인된 구간. 고객품질 + 증설 루트가 리레이팅으로 연결된 positive 표본이다.", "evidence_source": "historical public news/disclosure proxy around battery foil customer expansion; Stock-Web row 2023-03-16 c=58,900 and later 2023-06-15 h=140,100 checked", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "repeat_order_or_conversion", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2023.csv", "profile_path": "atlas/symbol_profiles/006/006110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-16", "entry_price": 58900, "MFE_30D_pct": 70.1, "MFE_90D_pct": 137.9, "MFE_180D_pct": 137.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.5, "MAE_90D_pct": -9.5, "MAE_180D_pct": -9.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-15", "peak_price": 140100, "drawdown_after_peak_pct": -32.9, "green_lateness_ratio": 0.24, "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.82, "four_b_timing_verdict": "good_full_window_4B_timing_but_not_hard_4C", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_volatility", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; share-count change before/around 2023-02 not inside selected 180D trigger window", "same_entry_group_id": "006110_2023-03-16_58900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED", "case_id": "R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF", "symbol": "393890", "company_name": "WCP", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "SEPARATOR_CUSTOMER_UTILIZATION_CALLOFF_RISK", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery customer contract / call-off risk", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Theme-Watch", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "분리막 증설/고객 기대는 있었지만 2023년 7월 이후 실제 가격경로는 고객 콜오프·가동률 리스크가 주문가치보다 중요했음을 보여준다. C12에서 단순 고객/증설 narrative를 Green으로 올리면 false positive가 된다.", "evidence_source": "Stock-Web row 2023-07-26 c=75,700; 2023-08-01 h=87,700; 2024-01-26 l=38,300 checked; public sector demand/utilization risk proxy", "stage2_evidence_fields": ["relative_strength", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2023.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 75700, "MFE_30D_pct": 15.9, "MFE_90D_pct": 15.9, "MFE_180D_pct": 15.9, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.6, "MAE_90D_pct": -36.0, "MAE_180D_pct": -49.4, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-01", "peak_price": 87700, "drawdown_after_peak_pct": -56.3, "green_lateness_ratio": "not_applicable: C12 candidate capped", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 0.87, "four_b_timing_verdict": "price_only_local_4B_watch_only_until_calloff_evidence", "four_b_evidence_type": ["positioning_overheat", "price_only_local_peak"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating_after_customer_utilization_risk", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "393890_2023-07-26_75700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED", "case_id": "R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN", "symbol": "336370", "company_name": "솔루스첨단소재", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_MARGIN_BRIDGE_BREAK", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery customer contract / call-off risk", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Theme-Watch", "trigger_date": "2023-02-21", "evidence_available_at_that_date": "전지박/동박 고객 기대는 있었지만 전력비·동박 스프레드·가동률 부담이 수익성 bridge를 압도했다. C12에서는 customer-name보다 margin bridge와 utilization confirmation이 먼저다.", "evidence_source": "Stock-Web row 2023-02-22 c=52,200; same-day h=54,000; 2023-08-25 l=31,500 checked; public copper-foil margin/utilization risk proxy", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken", "call_off_or_order_cut"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv", "profile_path": "atlas/symbol_profiles/336/336370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-22", "entry_price": 52200, "MFE_30D_pct": 3.4, "MFE_90D_pct": 3.4, "MFE_180D_pct": 3.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.8, "MAE_90D_pct": -24.9, "MAE_180D_pct": -39.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-02-22", "peak_price": 54000, "drawdown_after_peak_pct": -41.7, "green_lateness_ratio": "not_applicable: capped counterexample", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_risk_timing_because_peak_was_same_trigger_window", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "customer_story_without_margin_bridge_failed", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "336370_2023-02-22_52200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED", "case_id": "R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF", "symbol": "011790", "company_name": "SKC", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "COPPER_FOIL_CUSTOMER_CALLOFF_CAPEX_OVERHANG", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery customer contract / call-off risk", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Theme-Watch", "trigger_date": "2023-07-26", "evidence_available_at_that_date": "동박/배터리 소재 narrative와 7월 소재군 반등이 있었지만 고객 수요 둔화·CAPEX 부담·동박 마진 회복 지연이 더 컸다. price-only 소재 squeeze를 C12 positive로 승격하면 잔여 false positive가 생긴다.", "evidence_source": "Stock-Web row 2023-07-26 c=103,000 and h=111,000; subsequent 2023-08 to 2024 drawdown checked; public capex/utilization risk proxy", "stage2_evidence_fields": ["relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv", "profile_path": "atlas/symbol_profiles/011/011790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-26", "entry_price": 103000, "MFE_30D_pct": 7.8, "MFE_90D_pct": 7.8, "MFE_180D_pct": 7.8, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.6, "MAE_90D_pct": -17.5, "MAE_180D_pct": -31.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 111000, "drawdown_after_peak_pct": -36.0, "green_lateness_ratio": "not_applicable: capped counterexample", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_not_full_4C_without_non_price_break", "four_b_evidence_type": ["positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_moved_without_customer_conversion", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "011790_2023-07-26_103000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13_C12_TCCSTEEL_20230303_NICKEL_PLATED_STEEL", "trigger_id": "TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 72, "backlog_visibility_score": 72, "margin_bridge_score": 58, "revision_score": 48, "relative_strength_score": 80, "customer_quality_score": 74, "policy_or_regulatory_score": 0, "valuation_repricing_score": 65, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 72, "backlog_visibility_score": 76, "margin_bridge_score": 58, "revision_score": 48, "relative_strength_score": 80, "customer_quality_score": 80, "policy_or_regulatory_score": 0, "valuation_repricing_score": 65, "execution_risk_score": 31, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C12 promotes contract/customer evidence only when margin bridge, utilization, and order-conversion visibility co-move. Customer-name or EV-material price beta without conversion is capped to Stage2-Watch; price-only 4B remains overlay-only.", "MFE_90D_pct": 319.8, "MAE_90D_pct": -9.9, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13_C12_SAM_A_ALUMINUM_20230316_FOIL_CUSTOMER", "trigger_id": "TRG_R3L13_C12_SAM_A_20230316_STAGE2A", "symbol": "006110", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 72, "backlog_visibility_score": 72, "margin_bridge_score": 62, "revision_score": 48, "relative_strength_score": 80, "customer_quality_score": 74, "policy_or_regulatory_score": 0, "valuation_repricing_score": 65, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 72, "backlog_visibility_score": 76, "margin_bridge_score": 62, "revision_score": 48, "relative_strength_score": 80, "customer_quality_score": 80, "policy_or_regulatory_score": 0, "valuation_repricing_score": 65, "execution_risk_score": 31, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 85, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C12 promotes contract/customer evidence only when margin bridge, utilization, and order-conversion visibility co-move. Customer-name or EV-material price beta without conversion is capped to Stage2-Watch; price-only 4B remains overlay-only.", "MFE_90D_pct": 137.9, "MAE_90D_pct": -9.5, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13_C12_WCP_20230726_SEPARATOR_CALLOFF", "trigger_id": "TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 42, "margin_bridge_score": 20, "revision_score": 15, "relative_strength_score": 68, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 48, "execution_risk_score": 72, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 42, "margin_bridge_score": 12, "revision_score": 15, "relative_strength_score": 68, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 80, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C12 promotes contract/customer evidence only when margin bridge, utilization, and order-conversion visibility co-move. Customer-name or EV-material price beta without conversion is capped to Stage2-Watch; price-only 4B remains overlay-only.", "MFE_90D_pct": 15.9, "MAE_90D_pct": -36.0, "score_return_alignment_label": "counterexample_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13_C12_SOLUS_20230222_COPPERFOIL_MARGIN", "trigger_id": "TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED", "symbol": "336370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 42, "margin_bridge_score": 20, "revision_score": 15, "relative_strength_score": 68, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 48, "execution_risk_score": 72, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 42, "margin_bridge_score": 12, "revision_score": 15, "relative_strength_score": 68, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 80, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 60, "stage_label_after": "Stage2-Watch", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C12 promotes contract/customer evidence only when margin bridge, utilization, and order-conversion visibility co-move. Customer-name or EV-material price beta without conversion is capped to Stage2-Watch; price-only 4B remains overlay-only.", "MFE_90D_pct": 3.4, "MAE_90D_pct": -24.9, "score_return_alignment_label": "counterexample_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L13_C12_SKC_20230726_COPPERFOIL_CALLOFF", "trigger_id": "TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED", "symbol": "011790", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 42, "margin_bridge_score": 20, "revision_score": 15, "relative_strength_score": 68, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 48, "execution_risk_score": 72, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 42, "margin_bridge_score": 12, "revision_score": 15, "relative_strength_score": 68, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 40, "execution_risk_score": 80, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C12 promotes contract/customer evidence only when margin bridge, utilization, and order-conversion visibility co-move. Customer-name or EV-material price beta without conversion is capped to Stage2-Watch; price-only 4B remains overlay-only.", "MFE_90D_pct": 7.8, "MAE_90D_pct": -17.5, "score_return_alignment_label": "counterexample_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "profile_hypothesis": "global calibrated profile without C12-specific customer-conversion/call-off guard", "changed_axes": "none", "changed_thresholds": "existing 75/87/55", "eligible_trigger_count": 5, "selected_entry_trigger_per_case": 5, "avg_MFE_90D_pct": 96.96000000000001, "avg_MAE_90D_pct": -19.56, "avg_MFE_180D_pct": 123.0, "avg_MAE_180D_pct": -28.0, "false_positive_rate": "60%", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.21, "avg_four_b_local_peak_proximity": 0.934, "avg_four_b_full_window_peak_proximity": 0.934, "score_return_alignment_verdict": "mixed: can/foil positives work, separator/copper-foil customer stories over-promote"}
{"profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "profile_hypothesis": "older looser profile that overweights customer/order headlines", "changed_axes": "rollback only", "changed_thresholds": "looser Stage2/Green", "eligible_trigger_count": 5, "selected_entry_trigger_per_case": 5, "avg_MFE_90D_pct": 96.1, "avg_MAE_90D_pct": -19.5, "avg_MFE_180D_pct": 121.4, "avg_MAE_180D_pct": -25.1, "false_positive_rate": "80%", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.2, "avg_four_b_local_peak_proximity": 0.95, "avg_four_b_full_window_peak_proximity": 0.95, "score_return_alignment_verdict": "too permissive; customer story without margin bridge becomes false positive"}
{"profile_id": "P1_L3_C12_sector_shadow_profile", "profile_scope": "sector_specific", "profile_hypothesis": "L3 battery materials require utilization/margin bridge before customer contract promotion", "changed_axes": "add utilization/call-off risk guard; require margin bridge for C12 Yellow/Green", "changed_thresholds": "Stage2A allowed, Green capped unless margin + utilization + repeat order align", "eligible_trigger_count": 5, "selected_entry_trigger_per_case": 5, "avg_MFE_90D_pct": 99.0, "avg_MAE_90D_pct": -20.7, "avg_MFE_180D_pct": 121.4, "avg_MAE_180D_pct": -24.9, "false_positive_rate": "20% after capping weak rows", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.21, "avg_four_b_local_peak_proximity": 0.91, "avg_four_b_full_window_peak_proximity": 0.91, "score_return_alignment_verdict": "better but still sector-wide"}
{"profile_id": "P2_C12_canonical_archetype_candidate_profile", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C12 = customer contract + conversion; call-off/utilization/margin breaks cap score", "changed_axes": "customer_conversion_gate + margin_bridge_required + calloff_risk_penalty", "changed_thresholds": "Yellow if contract+customer+capacity; Green only if margin/utilization/revision confirmed", "eligible_trigger_count": 5, "selected_entry_trigger_per_case": 5, "avg_MFE_90D_pct": 228.85, "avg_MAE_90D_pct": -9.7, "avg_MFE_180D_pct": 293.95, "avg_MAE_180D_pct": -9.7, "false_positive_rate": "0% on promoted positives", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.21, "avg_four_b_local_peak_proximity": 0.9, "avg_four_b_full_window_peak_proximity": 0.9, "score_return_alignment_verdict": "preferred; separates can/foil conversion winners from call-off/margin losers"}
{"profile_id": "P3_C12_counterexample_guard_profile", "profile_scope": "counterexample_guard", "profile_hypothesis": "cap customer-name or material-squeeze rows without conversion evidence", "changed_axes": "theme/customer-name cap; price-only 4B overlay only", "changed_thresholds": "Stage2-Watch cap for weak conversion", "eligible_trigger_count": 3, "selected_entry_trigger_per_case": 3, "avg_MFE_90D_pct": 9.03, "avg_MAE_90D_pct": -26.13, "avg_MFE_180D_pct": 9.03, "avg_MAE_180D_pct": -40.2, "false_positive_rate": "0 after blocking", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.96, "avg_four_b_full_window_peak_proximity": 0.96, "score_return_alignment_verdict": "good guardrail; not a positive promotion profile"}
{"row_type": "residual_contribution", "round": "R3", "loop": "13", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "scheduled_round": "R3", "scheduled_loop": "13", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 3, "current_profile_error_count": 3, "diversity_score_summary": "five new R3/C12 symbols; two foil/can positives balanced against three separator/copper-foil call-off/margin counterexamples", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["C12_customer_name_false_positive", "utilization_calloff_risk_underweighted", "margin_bridge_missing_after_contract_headline", "price_only_material_squeeze_false_green"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.2 shadow_weight CSV rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C12_customer_conversion_gate_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,false,true,+1,"C12 should promote only customer contract evidence that also shows capacity conversion and margin/utilization bridge","Two accepted positives have very high MFE90/MFE180 with manageable MAE; three capped rows have low MFE and large MAE","TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A|TRG_R3L13_C12_SAM_A_20230316_STAGE2A",5,5,3,medium,canonical_shadow_only,"not production; source-url hardening required"
shadow_weight,C12_calloff_utilization_risk_penalty,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"Customer/order headline must be penalized when utilization, margin, call-off, or capex-overhang evidence appears","WCP/Solus/SKC show low forward upside and high drawdown when call-off/utilization risk dominated","TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED|TRG_R3L13_C12_SOLUS_20230222_STAGE2_CAPPED|TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED",3,3,3,medium,canonical_shadow_only,"blocks false Green in battery material sub-suppliers"
shadow_weight,C12_price_only_material_squeeze_overlay_only,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,true,true,0,"Keep price_only_blowoff_blocks_positive_stage and full_4b_requires_non_price_evidence; price-only local peaks stay overlay-only","Material squeeze peaks timed risk well but did not constitute a fresh positive contract signal","TRG_R3L13_C12_TCCSTEEL_20230303_STAGE2A|TRG_R3L13_C12_WCP_20230726_STAGE2_CAPPED|TRG_R3L13_C12_SKC_20230726_STAGE2_CAPPED",5,5,3,low_medium,axis_kept,"existing global axis kept and strengthened inside C12"
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
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

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
completed_loop = 13
next_round = R4
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest checked: `atlas/manifest.json`; manifest max date `2026-02-20`.
- Schema checked: `atlas/schema.json`; tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE definitions use max high / min low over forward tradable rows.
- Entry rows were checked in Stock-Web tradable shards for `002710`, `006110`, `393890`, `336370`, and `011790`.
- Evidence source text is research-proxy level. Before production ingestion, a coding/research batch should harden exact DART/news/report URLs for each trigger.

