# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

|field|value|
|---|---|
|mode|historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12|
|research_session|post_calibrated_sector_archetype_residual_research|
|round|R13|
|loop|30|
|large_sector_id|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|
|canonical_archetype_id|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|
|fine_archetype_id|BANK_HOLDCO_AND_REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE|
|output_format|one_standalone_markdown_file|
|production_scoring_changed|false|
|shadow_weight_only|true|
|handoff_prompt_embedded|true|
|handoff_prompt_executed_now|false|


## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`, not the old E2R 2.0 baseline. Existing global axes are retained: Stage2 actionable evidence bonus, Yellow/Green thresholds, cross-evidence Green buffer, price-only blowoff guard, full 4B non-price evidence requirement, and hard 4C thesis-break routing. This loop does not re-prove those global axes. It stress-tests whether C21 financial capital-return rerating needs a **company-level capital-return bridge** so that low-PBR policy beta is not mistaken for durable ROE/PBR rerating.


## 2. Round / Large Sector / Canonical Archetype Scope

- **Round / loop:** R13 / 30
- **Large sector:** L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
- **Canonical archetype:** C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
- **Loop objectives:** holdout_validation, residual_false_positive_mining, yellow_threshold_stress_test, green_strictness_stress_test, stage2_actionable_bonus_stress_test, 4B_non_price_requirement_stress_test, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, coverage_gap_fill.


## 3. Previous Coverage / Duplicate Avoidance Check

`stock_agent` source code was not opened and no production patch was written. Research artifacts were treated as unavailable in this execution, so duplicate avoidance used the prior conversation state: previous v12 output ended with `next_round = R13_loop_30 — L6_FINANCIAL_CAPITAL_RETURN_DIGITAL / C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`. This loop therefore uses four new independent symbols and a new canonical sector path: financial-holding company capital-return rerating versus policy-only low-PBR beta.


## 4. Stock-Web OHLC Input / Price Source Validation

|manifest_field|value|
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
|markets|["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"]|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|


Stock-web schema validation used the declared tradable shard columns `d,o,h,l,c,v,a,mc,s,m`, raw shard columns with `rs`, `price_adjustment_status=raw_unadjusted_marcap`, and `calibration_basis=tradable_raw`. The schema states that calibration requires positive OHLC/volume, an existing entry row, at least 180 forward tradable days, computed MFE/MAE 30/90/180D, and no 180D corporate-action contamination.


## 5. Historical Eligibility Gate

|symbol|company|profile_path|entry windows|corporate action status|calibration_usable|
|---|---|---|---|---|---|
|105560|KB금융|atlas/symbol_profiles/105/105560.json|180D available before manifest max_date 2026-02-20|clean_180D_window|True|
|175330|JB금융지주|atlas/symbol_profiles/175/175330.json|180D available before manifest max_date 2026-02-20|clean_180D_window; old profile caveat only|True|
|316140|우리금융지주|atlas/symbol_profiles/316/316140.json|180D available before manifest max_date 2026-02-20|clean_180D_window|True|
|138930|BNK금융지주|atlas/symbol_profiles/138/138930.json|180D available before manifest max_date 2026-02-20|clean_180D_window; old profile caveat only|True|


## 6. Canonical Archetype Compression Map

|fine_archetype_id|canonical_archetype_id|compression logic|
|---|---|---|
|BANK_HOLDCO_VALUEUP_CET1_BUYBACK_CANCEL_ROUTE|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|Large bank holdco rerating when low-PBR policy beta is backed by CET1 room and explicit buyback/cancel/dividend execution.|
|REGIONAL_BANK_HIGH_ROE_CAPITAL_RETURN_COMPRESSION|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|Small/regional bank rerating when high ROE persistence and capital return create a visible PBR compression path.|
|BANK_HOLDCO_POLICY_ONLY_WITH_CAPITAL_DRAG|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|Counterexample where policy beta exists but capital drag/execution risk weakens Stage2-Actionable or Green.|
|REGIONAL_BANK_POLICY_BETA_WITH_WEAKER_ROE_SPREAD|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|Counterexample where regional-bank low-PBR beta rises, but weaker ROE spread/return execution should cap promotion.|


## 7. Case Selection Summary

|case_id|symbol|company|role|fine_archetype|best_trigger|MFE90|MFE180|MAE90|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|
|R13L30_C21_KB_105560_VALUEUP_CET1_BUYBACK_2024|105560|KB금융|positive|BANK_HOLDCO_VALUEUP_CET1_BUYBACK_CANCEL_ROUTE|R13L30_C21_KB_S2A_20240208|23.37|53.7|-11.69|current_profile_correct|
|R13L30_C21_JB_175330_ROE_SMALLBANK_RERATING_2024|175330|JB금융지주|positive|REGIONAL_BANK_HIGH_ROE_CAPITAL_RETURN_COMPRESSION|R13L30_C21_JB_S2A_20240208|20.76|51.74|-7.62|current_profile_correct|
|R13L30_C21_WOORI_316140_POLICY_ONLY_CAPITAL_DRAG_2024|316140|우리금융지주|counterexample|BANK_HOLDCO_POLICY_ONLY_WITH_CAPITAL_DRAG|R13L30_C21_WOORI_POLICY_S2_20240208|6.09|17.04|-9.99|current_profile_too_early|
|R13L30_C21_BNK_138930_REGIONAL_POLICY_BETA_2024|138930|BNK금융지주|counterexample|REGIONAL_BANK_POLICY_BETA_WITH_WEAKER_ROE_SPREAD|R13L30_C21_BNK_POLICY_S2_20240208|11.89|32.23|-6.39|current_profile_too_early|


## 8. Positive vs Counterexample Balance

Positive structural successes: KB금융 and JB금융지주. Counterexamples / partial rerating traps: 우리금융지주 and BNK금융지주. The distinction is not “bank stocks went up or down.” The distinction is whether **policy beta became a company-level capital-return bridge**. KB/JB converted low-PBR attention into higher confidence on capital return and ROE/PBR compression. Woori/BNK moved, but their evidence was weaker or more policy-beta-like, so Green promotion should be guarded.


## 9. Evidence Source Map

|case|Stage2 evidence|Stage3 evidence|4B/4C evidence separation|
|---|---|---|---|
|KB금융|Value-up / low-PBR policy attention, relative strength, explicit shareholder-return quality proxy.|Q1/return update confirmation; financial visibility.|4B overlay near full-window peak from valuation/positioning, not price-only.|
|JB금융지주|High ROE small-bank rerating, low-PBR policy beta, early relative strength.|Confirmed persistence / shareholder-return confidence proxy.|No hard 4C; late Green audit only.|
|우리금융지주|Policy beta and low-PBR attention.|Insufficient company-level capital-return bridge; non-bank/capital drag risk.|No full 4B; no hard 4C.|
|BNK금융지주|Regional-bank policy beta and dividend expectation.|Partial Yellow only; weaker ROE/capital-return spread than JB.|No full 4B; no hard 4C.|


## 10. Price Data Source Map

|symbol|price_shard_path examples|profile_path|price_basis|adjustment|
|---|---|---|---|---|
|105560|atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv|atlas/symbol_profiles/105/105560.json|tradable_raw|raw_unadjusted_marcap|
|175330|atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv|atlas/symbol_profiles/175/175330.json|tradable_raw|raw_unadjusted_marcap|
|316140|atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv|atlas/symbol_profiles/316/316140.json|tradable_raw|raw_unadjusted_marcap|
|138930|atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv|atlas/symbol_profiles/138/138930.json|tradable_raw|raw_unadjusted_marcap|


## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|type|entry|entry_price|MFE30|MFE90|MFE180|MAE90|green_lateness|current_verdict|role|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L30_C21_KB_S2A_20240208|105560|Stage2-Actionable|2024-02-08|67600|16.27|23.37|53.7|-11.69|None|current_profile_correct|representative|
|R13L30_C21_KB_GREEN_20240426|105560|Stage3-Green|2024-04-26|76000|9.74|21.58|36.71|-5.39|0.231|current_profile_too_late|label_comparison_only|
|R13L30_C21_KB_4B_20241025|105560|Stage4B|2024-10-25|101000|2.87|2.87|2.87|-28.91|None|current_profile_4B_too_late|4B_overlay_only|
|R13L30_C21_JB_S2A_20240208|175330|Stage2-Actionable|2024-02-08|12330|14.36|20.76|51.74|-7.62|None|current_profile_correct|representative|
|R13L30_C21_JB_GREEN_20240531|175330|Stage3-Green|2024-05-31|14620|10.47|27.98|40.22|-11.22|0.359|current_profile_correct|label_comparison_only|
|R13L30_C21_WOORI_POLICY_S2_20240208|316140|Stage2|2024-02-08|14610|6.09|6.09|17.04|-9.99|None|current_profile_too_early|representative|
|R13L30_C21_WOORI_FALSE_GREEN_20240726|316140|Stage3-Yellow|2024-07-26|16180|4.82|5.69|6.92|-15.08|0.631|current_profile_false_positive|label_comparison_only|
|R13L30_C21_BNK_POLICY_S2_20240208|138930|Stage2|2024-02-08|7820|7.54|11.89|32.23|-6.39|None|current_profile_too_early|representative|
|R13L30_C21_BNK_YELLOW_20240729|138930|Stage3-Yellow|2024-07-29|9430|9.65|26.19|26.19|-8.8|0.639|current_profile_too_late|label_comparison_only|


## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE calculations follow `MFE_N_pct=(max high from entry_date through N trading days / entry_price - 1)*100` and `MAE_N_pct=(min low from entry_date through N trading days / entry_price - 1)*100`. Entry price is the stock-web `c` column on the chosen entry date.


|trigger_id|entry|entry_price|peak_date|peak_price|MFE30|MFE90|MFE180|MFE1Y|MAE30|MAE90|MAE180|MAE1Y|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L30_C21_KB_S2A_20240208|2024-02-08|67600|2024-10-25|103900|16.27|23.37|53.7|53.7|-11.69|-11.69|-11.69|-11.69|-17.42|
|R13L30_C21_KB_GREEN_20240426|2024-04-26|76000|2024-10-25|103900|9.74|21.58|36.71|36.71|-5.39|-5.39|-5.39|-8.55|-17.42|
|R13L30_C21_KB_4B_20241025|2024-10-25|101000|2024-10-25|103900|2.87|2.87|2.87|2.87|-11.58|-28.91|-31.19|-31.19|-33.11|
|R13L30_C21_JB_S2A_20240208|2024-02-08|12330|2024-10-25|18710|14.36|20.76|51.74|66.26|-4.7|-7.62|-7.62|-7.62|-30.41|
|R13L30_C21_JB_GREEN_20240531|2024-05-31|14620|2025-02-07|20500|10.47|27.98|40.22|40.22|-8.28|-11.22|-11.22|-11.22|-18.93|
|R13L30_C21_WOORI_POLICY_S2_20240208|2024-02-08|14610|2024-10-25|17100|6.09|6.09|17.04|18.41|-4.24|-9.99|-9.99|-9.99|-19.65|
|R13L30_C21_WOORI_FALSE_GREEN_20240726|2024-07-26|16180|2024-12-03|17300|4.82|5.69|6.92|6.92|-15.08|-15.08|-15.08|-15.08|-24.45|
|R13L30_C21_BNK_POLICY_S2_20240208|2024-02-08|7820|2024-08-26|10340|7.54|11.89|32.23|52.17|-6.39|-6.39|-6.39|-6.39|-16.92|
|R13L30_C21_BNK_YELLOW_20240729|2024-07-29|9430|2024-12-03|11900|9.65|26.19|26.19|26.19|-8.8|-8.8|-8.8|-8.8|-23.19|


## 13. Current Calibrated Profile Stress Test

|case|current profile expected judgment|actual alignment|residual verdict|
|---|---|---|---|
|KB금융|Stage2-Actionable is justified; Green confirmation is useful but late; 4B needs non-price valuation/positioning overlay.|Aligned. 180D MFE from Stage2 was 53.70%, but Green at 76,000 used 23.1% of the available cycle spread.|current_profile_correct / current_profile_too_late on Green / current_profile_4B_too_late|
|JB금융지주|Stage2-Actionable justified if high ROE and capital-return bridge are recognized early.|Aligned. Stage2 180D MFE was 51.74%; Green lateness ratio was 0.359.|current_profile_correct|
|우리금융지주|Policy-only score should not become Green. Stage2-watch only.|Residual error. 90D MFE only 6.09% with -9.99% MAE; false-Green row has unfavorable MAE.|current_profile_too_early / current_profile_false_positive|
|BNK금융지주|Stage2 is acceptable, but Green should require stronger ROE/capital-return spread.|Partial. 180D MFE 32.23%, but Stage3-Yellow lateness ratio 0.639 and MAE remained material.|current_profile_too_early / current_profile_too_late|


Answers to mandatory stress-test questions: Stage2 bonus is useful for KB/JB but excessive for Woori/BNK unless the C21 bridge exists. Yellow threshold 75 is not the issue by itself; the missing dimension is **component quality**. Green threshold 87/revision 55 remains appropriate but must not be reached by policy beta and relative strength alone. Price-only blowoff guard and full 4B non-price requirement are kept. No hard 4C routing change is proposed.


## 14. Stage2 / Yellow / Green Comparison

|case|Stage2 entry|Green/Yellow entry|green_lateness_ratio|interpretation|
|---|---|---|---|---|
|KB금융|67,600|76,000|0.231|Green not very late, but Stage2 captured materially better entry.|
|JB금융지주|12,330|14,620|0.359|Green somewhat late; Stage2-Actionable captures high-ROE rerating earlier.|
|우리금융지주|14,610|16,180|0.631|Promotion after policy rally consumes much of the modest cycle and increases downside risk.|
|BNK금융지주|7,820|9,430|0.639|Yellow/Green-like promotion is late and should be capped unless stronger ROE/capital-return evidence appears.|


## 15. 4B Local vs Full-window Timing Audit

Only KB produced a usable 4B overlay row in this loop. It is not treated as a standalone sell signal and not a price-only rule. The row combines valuation/positioning overheat with full-window proximity. `four_b_local_peak_proximity=0.92` and `four_b_full_window_peak_proximity=0.92`; verdict: `good_full_window_4B_timing`.


## 16. 4C Protection Audit

No hard 4C thesis-break row is promoted. Woori and BNK are **Green guard** cases, not hard 4C cases. `hard_4c_thesis_break_routes_to_4c` is kept unchanged.


## 17. Sector-Specific Rule Candidate

**Rule candidate — L6 capital-return bridge:** In L6 financials, Stage2-Actionable promotion should require at least two of: explicit buyback/cancel or rising payout commitment, CET1/capital-ratio room, high or improving ROE persistence, and evidence that policy beta is translating into company-specific shareholder-return execution. Policy/regulatory score alone should not receive full Stage2-Actionable bonus.


## 18. Canonical-Archetype Rule Candidate

**Rule candidate — C21 policy-only Green block:** For `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`, block Green if `policy_or_regulatory_score` and `relative_strength_score` are high but `revision_score`, ROE/payout execution, or CET1/capital-return bridge is not confirmed. Cap the row at Stage2-watch or Yellow until company-level evidence appears.


## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|alignment|
|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global_current_proxy|Current global calibration catches Stage2 but over-rewards policy-only C21 rows unless a company-level capital return bridge is separated.|4|15.53|-8.92|38.68|-8.92|2/4 if policy-only rows are promoted beyond Stage2|mixed|
|P0b_e2r_2_0_baseline_reference|rollback_reference|Old baseline under-weights actionable shareholder-return evidence and treats policy beta too similarly to durable capital return.|4|15.53|-8.92|38.68|-8.92|2/4|weaker|
|P1_sector_specific_candidate_profile|L6 sector-specific|L6 promotion requires capital-return execution quality: CET1 surplus, explicit buyback/cancel or rising payout capacity, and ROE persistence.|4|22.07|-9.65|52.72|-9.65|0/4 under guard|improved|
|P2_canonical_archetype_candidate_profile|C21 canonical-archetype-specific|C21 should split policy beta from company-level ROE/PBR capital return bridge. Stage2 bonus applies only to explicit bridge; Green requires confirmed capital-return execution.|4|22.07|-9.65|52.72|-9.65|0/4|best|
|P3_counterexample_guard_profile|guard|If policy_or_regulatory_score is high but revision/ROE/CET1 bridge is weak, cap label at Stage2-watch or Yellow and block Green.|4|8.99|-8.19|24.63|-8.19|0/4 after guard|guard useful|


## 20. Score-Return Alignment Matrix

|axis|positive evidence|counterexample evidence|decision|
|---|---|---|---|
|stage2_actionable_evidence_bonus|KB/JB: high MFE with early evidence.|Woori/BNK: policy-only beta underperforms positives.|Keep global axis; add C21 bridge guard.|
|stage3_yellow_total_min / green thresholds|Green confirmation works when it follows real capital-return execution.|Policy beta can pass Yellow-like score without enough durable bridge.|Keep thresholds; modify component eligibility.|
|price_only_blowoff_blocks_positive_stage|KB 4B overlay shows high full-window proximity.|No counterexample weakening found.|Strengthen in C21 with valuation/positioning non-price overlay.|
|full_4b_requires_non_price_evidence|Prevents local price spikes from becoming full 4B.|No weakening evidence.|Keep.|


## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|BANK_HOLDCO_AND_REGIONAL_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE|2|2|1|0|4|0|9|4|3|True|True|Needs additional insurance/brokerage/non-bank financial cases and 2025+ holdout after manifest max advances.|


## 22. Residual Contribution Summary

new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: policy_only_false_positive_green, capital_return_bridge_missed, late_green_for_small_high_ROE_financial, 4B_full_window_timing_needs_valuation_overlay
new_axis_proposed: c21_company_level_capital_return_bridge; c21_policy_only_green_block; l6_capital_drag_execution_risk
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; yellow/green thresholds; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate


## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest/schema assumptions, symbol profile availability, 2024/2025 tradable shard rows, entry close, 30D/90D/180D/1Y MFE/MAE approximated from observed shard windows, corporate-action exclusion for entry~D+180. Not validated: live candidates, broker API data, production scoring code, exact official filing timestamps, or investment suitability. No current-stock recommendation is made.


## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_company_level_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Require explicit ROE/CET1/shareholder-return bridge before Stage2-Actionable+ or Green","Positive KB/JB rows had avg 180D MFE above 50% while Woori/BNK policy-only rows had weaker or riskier paths","R13L30_C21_KB_S2A_20240208|R13L30_C21_JB_S2A_20240208|R13L30_C21_WOORI_POLICY_S2_20240208|R13L30_C21_BNK_POLICY_S2_20240208",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_policy_only_green_block,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,false,true,+1,"Policy/regulatory score without confirmed capital-return execution should not promote Green","Reduces Woori/BNK false-positive Green risk and preserves KB/JB positives","R13L30_C21_WOORI_FALSE_GREEN_20240726|R13L30_C21_BNK_YELLOW_20240729",2,2,2,medium,counterexample_guard,"block only Green, not Stage2 watch"
shadow_weight,l6_capital_drag_execution_risk,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Non-bank acquisition/capital-ratio drag should raise execution risk when buyback/cancel evidence is missing","Explains lower 90D/180D score-return alignment for Woori vs KB/JB","R13L30_C21_WOORI_POLICY_S2_20240208",1,1,1,low,sector_shadow_only,"needs more bank/insurance holdout rows"
```


## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"R13L30_C21_KB_105560_VALUEUP_CET1_BUYBACK_2024","symbol":"105560","company_name":"KB금융","round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUEUP_CET1_BUYBACK_CANCEL_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L30_C21_KB_S2A_20240208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Value-up 정책 랠리와 별개로 CET1 여력, 자사주 매입·소각, 분기 자본환원 반복성이 결합된 케이스. current profile은 Stage2는 맞지만 Green이 지나치게 보수적이면 180D upside 대부분을 뒤늦게 포착한다."}
{"row_type":"case","case_id":"R13L30_C21_JB_175330_ROE_SMALLBANK_RERATING_2024","symbol":"175330","company_name":"JB금융지주","round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_HIGH_ROE_CAPITAL_RETURN_COMPRESSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L30_C21_JB_S2A_20240208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"대형 금융지주보다 작은 시총이지만 ROE·자본환원·저PBR 압축이 동시에 작동했다. Stage3 확인을 기다리면 수익의 상당 부분을 놓치므로, C21에서는 높은 ROE 지속성과 명시적 환원정책을 Stage2-Actionable로 승격할 수 있다."}
{"row_type":"case","case_id":"R13L30_C21_WOORI_316140_POLICY_ONLY_CAPITAL_DRAG_2024","symbol":"316140","company_name":"우리금융지주","round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_POLICY_ONLY_WITH_CAPITAL_DRAG","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R13L30_C21_WOORI_POLICY_S2_20240208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_beta_partial_or_false_positive","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"저PBR·밸류업 헤드라인에는 반응했지만, 비은행 인수·자본비율 부담·환원 여력의 질이 KB/JB 대비 약해 MFE 대비 체류기간과 MAE가 불리했다. current profile이 정책+가격만으로 Green을 허용하면 false-positive 성격이 강해진다."}
{"row_type":"case","case_id":"R13L30_C21_BNK_138930_REGIONAL_POLICY_BETA_2024","symbol":"138930","company_name":"BNK금융지주","round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_POLICY_BETA_WITH_WEAKER_ROE_SPREAD","case_type":"stage2_promote_candidate","positive_or_counterexample":"counterexample","best_trigger":"R13L30_C21_BNK_POLICY_S2_20240208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_beta_partial_or_false_positive","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"정책 베타와 배당 기대는 충분했지만, JB처럼 높은 ROE·환원 신뢰·시장 압축이 한꺼번에 붙은 구조는 아니었다. 상승은 있었으나 C21 Green 승격에는 추가적인 ROE/CET1/소각 증거가 필요하다."}
```

### 25.3 trigger rows
```jsonl
{"round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"financials","primary_archetype":"financial ROE/PBR capital return","loop_objective":["holdout_validation","residual_false_positive_mining","yellow_threshold_stress_test","green_strictness_stress_test","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"R13L30_C21_KB_S2A_20240208","case_id":"R13L30_C21_KB_105560_VALUEUP_CET1_BUYBACK_2024","symbol":"105560","company_name":"KB금융","fine_archetype_id":"BANK_HOLDCO_VALUEUP_CET1_BUYBACK_CANCEL_ROUTE","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-07","entry_date":"2024-02-08","entry_price":67600,"evidence_available_at_that_date":"정책/밸류업 기대가 주가에 반영되기 시작했고, KB는 업종 내 CET1·자사주 소각·반복 환원 가능성이 상대적으로 선명했다.","evidence_source":"historical public disclosure / earnings / shareholder-return evidence proxy; price from stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","MFE_30D_pct":16.27,"MFE_90D_pct":23.37,"MFE_180D_pct":53.7,"MFE_1Y_pct":53.7,"MFE_2Y_pct":null,"MAE_30D_pct":-11.69,"MAE_90D_pct":-11.69,"MAE_180D_pct":-11.69,"MAE_1Y_pct":-11.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-17.42,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L30_C21_KB_105560_VALUEUP_CET1_BUYBACK_2024_2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"financials","primary_archetype":"financial ROE/PBR capital return","loop_objective":["holdout_validation","residual_false_positive_mining","yellow_threshold_stress_test","green_strictness_stress_test","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"R13L30_C21_KB_GREEN_20240426","case_id":"R13L30_C21_KB_105560_VALUEUP_CET1_BUYBACK_2024","symbol":"105560","company_name":"KB금융","fine_archetype_id":"BANK_HOLDCO_VALUEUP_CET1_BUYBACK_CANCEL_ROUTE","trigger_type":"Stage3-Green","trigger_date":"2024-04-25","entry_date":"2024-04-26","entry_price":76000,"evidence_available_at_that_date":"1Q 실적·환원 업데이트로 Stage3 확인 성격의 증거가 붙었다. 그러나 Stage2 대비 이미 23%의 cycle upside를 소모했다.","evidence_source":"historical public disclosure / earnings / shareholder-return evidence proxy; price from stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","MFE_30D_pct":9.74,"MFE_90D_pct":21.58,"MFE_180D_pct":36.71,"MFE_1Y_pct":36.71,"MFE_2Y_pct":null,"MAE_30D_pct":-5.39,"MAE_90D_pct":-5.39,"MAE_180D_pct":-5.39,"MAE_1Y_pct":-8.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-17.42,"green_lateness_ratio":0.231,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L30_C21_KB_105560_VALUEUP_CET1_BUYBACK_2024_2024-04-26","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"financials","primary_archetype":"financial ROE/PBR capital return","loop_objective":["holdout_validation","residual_false_positive_mining","yellow_threshold_stress_test","green_strictness_stress_test","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"R13L30_C21_KB_4B_20241025","case_id":"R13L30_C21_KB_105560_VALUEUP_CET1_BUYBACK_2024","symbol":"105560","company_name":"KB금융","fine_archetype_id":"BANK_HOLDCO_VALUEUP_CET1_BUYBACK_CANCEL_ROUTE","trigger_type":"Stage4B","trigger_date":"2024-10-25","entry_date":"2024-10-25","entry_price":101000,"evidence_available_at_that_date":"주가가 Stage2 대비 full-window peak 근처에 진입했고, 정책/환원 기대가 상당 부분 가격에 반영되었다. 가격만이 아니라 valuation/positioning overlay로 처리해야 한다.","evidence_source":"historical public disclosure / earnings / shareholder-return evidence proxy; price from stock-web tradable shard","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","MFE_30D_pct":2.87,"MFE_90D_pct":2.87,"MFE_180D_pct":2.87,"MFE_1Y_pct":2.87,"MFE_2Y_pct":null,"MAE_30D_pct":-11.58,"MAE_90D_pct":-28.91,"MAE_180D_pct":-31.19,"MAE_1Y_pct":-31.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-33.11,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L30_C21_KB_105560_VALUEUP_CET1_BUYBACK_2024_2024-10-25","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"financials","primary_archetype":"financial ROE/PBR capital return","loop_objective":["holdout_validation","residual_false_positive_mining","yellow_threshold_stress_test","green_strictness_stress_test","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"R13L30_C21_JB_S2A_20240208","case_id":"R13L30_C21_JB_175330_ROE_SMALLBANK_RERATING_2024","symbol":"175330","company_name":"JB금융지주","fine_archetype_id":"REGIONAL_BANK_HIGH_ROE_CAPITAL_RETURN_COMPRESSION","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-07","entry_date":"2024-02-08","entry_price":12330,"evidence_available_at_that_date":"대형 금융주 value-up 랠리와 동시에 높은 ROE·작은 시총·자본환원 가시성이 압축적으로 반영되기 시작했다.","evidence_source":"historical public disclosure / earnings / shareholder-return evidence proxy; price from stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv","profile_path":"atlas/symbol_profiles/175/175330.json","MFE_30D_pct":14.36,"MFE_90D_pct":20.76,"MFE_180D_pct":51.74,"MFE_1Y_pct":66.26,"MFE_2Y_pct":null,"MAE_30D_pct":-4.7,"MAE_90D_pct":-7.62,"MAE_180D_pct":-7.62,"MAE_1Y_pct":-7.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":18710,"drawdown_after_peak_pct":-30.41,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L30_C21_JB_175330_ROE_SMALLBANK_RERATING_2024_2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"financials","primary_archetype":"financial ROE/PBR capital return","loop_objective":["holdout_validation","residual_false_positive_mining","yellow_threshold_stress_test","green_strictness_stress_test","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"R13L30_C21_JB_GREEN_20240531","case_id":"R13L30_C21_JB_175330_ROE_SMALLBANK_RERATING_2024","symbol":"175330","company_name":"JB금융지주","fine_archetype_id":"REGIONAL_BANK_HIGH_ROE_CAPITAL_RETURN_COMPRESSION","trigger_type":"Stage3-Green","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":14620,"evidence_available_at_that_date":"이익/환원 경로가 더 확인된 뒤의 Green 트리거. Stage2 대비 늦지만 아직 구조적 수익은 남아 있었다.","evidence_source":"historical public disclosure / earnings / shareholder-return evidence proxy; price from stock-web tradable shard","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv","profile_path":"atlas/symbol_profiles/175/175330.json","MFE_30D_pct":10.47,"MFE_90D_pct":27.98,"MFE_180D_pct":40.22,"MFE_1Y_pct":40.22,"MFE_2Y_pct":null,"MAE_30D_pct":-8.28,"MAE_90D_pct":-11.22,"MAE_180D_pct":-11.22,"MAE_1Y_pct":-11.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-07","peak_price":20500,"drawdown_after_peak_pct":-18.93,"green_lateness_ratio":0.359,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L30_C21_JB_175330_ROE_SMALLBANK_RERATING_2024_2024-05-31","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"financials","primary_archetype":"financial ROE/PBR capital return","loop_objective":["holdout_validation","residual_false_positive_mining","yellow_threshold_stress_test","green_strictness_stress_test","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"R13L30_C21_WOORI_POLICY_S2_20240208","case_id":"R13L30_C21_WOORI_316140_POLICY_ONLY_CAPITAL_DRAG_2024","symbol":"316140","company_name":"우리금융지주","fine_archetype_id":"BANK_HOLDCO_POLICY_ONLY_WITH_CAPITAL_DRAG","trigger_type":"Stage2","trigger_date":"2024-02-07","entry_date":"2024-02-08","entry_price":14610,"evidence_available_at_that_date":"정책/저PBR 베타에는 반응했지만, KB/JB 대비 CET1·소각·ROE 차별화가 약했다. Stage2는 가능하나 Stage2-Actionable bonus를 강하게 주면 과하다.","evidence_source":"historical public disclosure / earnings / shareholder-return evidence proxy; price from stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv","profile_path":"atlas/symbol_profiles/316/316140.json","MFE_30D_pct":6.09,"MFE_90D_pct":6.09,"MFE_180D_pct":17.04,"MFE_1Y_pct":18.41,"MFE_2Y_pct":null,"MAE_30D_pct":-4.24,"MAE_90D_pct":-9.99,"MAE_180D_pct":-9.99,"MAE_1Y_pct":-9.99,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":17100,"drawdown_after_peak_pct":-19.65,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L30_C21_WOORI_316140_POLICY_ONLY_CAPITAL_DRAG_2024_2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"financials","primary_archetype":"financial ROE/PBR capital return","loop_objective":["holdout_validation","residual_false_positive_mining","yellow_threshold_stress_test","green_strictness_stress_test","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"R13L30_C21_WOORI_FALSE_GREEN_20240726","case_id":"R13L30_C21_WOORI_316140_POLICY_ONLY_CAPITAL_DRAG_2024","symbol":"316140","company_name":"우리금융지주","fine_archetype_id":"BANK_HOLDCO_POLICY_ONLY_WITH_CAPITAL_DRAG","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":16180,"evidence_available_at_that_date":"비은행/증권 보강 기대와 정책 베타가 겹쳤지만 capital drag를 해소하는 증거가 부족했다. Green으로 올리면 upside 대비 MAE가 커진다.","evidence_source":"historical public disclosure / earnings / shareholder-return evidence proxy; price from stock-web tradable shard","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv","profile_path":"atlas/symbol_profiles/316/316140.json","MFE_30D_pct":4.82,"MFE_90D_pct":5.69,"MFE_180D_pct":6.92,"MFE_1Y_pct":6.92,"MFE_2Y_pct":null,"MAE_30D_pct":-15.08,"MAE_90D_pct":-15.08,"MAE_180D_pct":-15.08,"MAE_1Y_pct":-15.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":17300,"drawdown_after_peak_pct":-24.45,"green_lateness_ratio":0.631,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L30_C21_WOORI_316140_POLICY_ONLY_CAPITAL_DRAG_2024_2024-07-26","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"financials","primary_archetype":"financial ROE/PBR capital return","loop_objective":["holdout_validation","residual_false_positive_mining","yellow_threshold_stress_test","green_strictness_stress_test","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"R13L30_C21_BNK_POLICY_S2_20240208","case_id":"R13L30_C21_BNK_138930_REGIONAL_POLICY_BETA_2024","symbol":"138930","company_name":"BNK금융지주","fine_archetype_id":"REGIONAL_BANK_POLICY_BETA_WITH_WEAKER_ROE_SPREAD","trigger_type":"Stage2","trigger_date":"2024-02-07","entry_date":"2024-02-08","entry_price":7820,"evidence_available_at_that_date":"지역은행 value-up 베타와 배당 기대가 붙었지만 JB 대비 ROE·환원 신뢰·시장 압축이 약했다. Stage2까지만 허용하는 게 적절하다.","evidence_source":"historical public disclosure / earnings / shareholder-return evidence proxy; price from stock-web tradable shard","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv","profile_path":"atlas/symbol_profiles/138/138930.json","MFE_30D_pct":7.54,"MFE_90D_pct":11.89,"MFE_180D_pct":32.23,"MFE_1Y_pct":52.17,"MFE_2Y_pct":null,"MAE_30D_pct":-6.39,"MAE_90D_pct":-6.39,"MAE_180D_pct":-6.39,"MAE_1Y_pct":-6.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":10340,"drawdown_after_peak_pct":-16.92,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_promote_candidate","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L30_C21_BNK_138930_REGIONAL_POLICY_BETA_2024_2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"financials","primary_archetype":"financial ROE/PBR capital return","loop_objective":["holdout_validation","residual_false_positive_mining","yellow_threshold_stress_test","green_strictness_stress_test","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","coverage_gap_fill"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","row_type":"trigger","trigger_id":"R13L30_C21_BNK_YELLOW_20240729","case_id":"R13L30_C21_BNK_138930_REGIONAL_POLICY_BETA_2024","symbol":"138930","company_name":"BNK금융지주","fine_archetype_id":"REGIONAL_BANK_POLICY_BETA_WITH_WEAKER_ROE_SPREAD","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-29","entry_date":"2024-07-29","entry_price":9430,"evidence_available_at_that_date":"정책 베타가 한 번 더 붙은 Yellow 후보. 30D 이후 상승은 있었지만, Stage2 대비 Green lateness가 높고 MAE가 크다.","evidence_source":"historical public disclosure / earnings / shareholder-return evidence proxy; price from stock-web tradable shard","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv","profile_path":"atlas/symbol_profiles/138/138930.json","MFE_30D_pct":9.65,"MFE_90D_pct":26.19,"MFE_180D_pct":26.19,"MFE_1Y_pct":26.19,"MFE_2Y_pct":null,"MAE_30D_pct":-8.8,"MAE_90D_pct":-8.8,"MAE_180D_pct":-8.8,"MAE_1Y_pct":-8.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":11900,"drawdown_after_peak_pct":-23.19,"green_lateness_ratio":0.639,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_yellow_partial_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L30_C21_BNK_138930_REGIONAL_POLICY_BETA_2024_2024-07-29","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L30_C21_KB_105560_VALUEUP_CET1_BUYBACK_2024","trigger_id":"R13L30_C21_KB_S2A_20240208","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":50,"relative_strength_score":64,"customer_quality_score":0,"policy_or_regulatory_score":60,"valuation_repricing_score":55,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":54,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":64,"valuation_repricing_score":59,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable+","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"C21 shadow profile separates explicit ROE/CET1/shareholder-return bridge from policy-only low-PBR beta. Positive cases keep/raise score; Woori/BNK policy-only rows are de-risked.","MFE_90D_pct":23.37,"MAE_90D_pct":-11.69,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L30_C21_JB_175330_ROE_SMALLBANK_RERATING_2024","trigger_id":"R13L30_C21_JB_S2A_20240208","symbol":"175330","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":52,"relative_strength_score":62,"customer_quality_score":0,"policy_or_regulatory_score":57,"valuation_repricing_score":64,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":57,"relative_strength_score":67,"customer_quality_score":0,"policy_or_regulatory_score":60,"valuation_repricing_score":68,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":83,"stage_label_after":"Stage2-Actionable+","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"C21 shadow profile separates explicit ROE/CET1/shareholder-return bridge from policy-only low-PBR beta. Positive cases keep/raise score; Woori/BNK policy-only rows are de-risked.","MFE_90D_pct":20.76,"MAE_90D_pct":-7.62,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L30_C21_WOORI_316140_POLICY_ONLY_CAPITAL_DRAG_2024","trigger_id":"R13L30_C21_WOORI_POLICY_S2_20240208","symbol":"316140","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":38,"relative_strength_score":56,"customer_quality_score":0,"policy_or_regulatory_score":62,"valuation_repricing_score":45,"execution_risk_score":35,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":36,"relative_strength_score":54,"customer_quality_score":0,"policy_or_regulatory_score":54,"valuation_repricing_score":39,"execution_risk_score":42,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-watch","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"C21 shadow profile separates explicit ROE/CET1/shareholder-return bridge from policy-only low-PBR beta. Positive cases keep/raise score; Woori/BNK policy-only rows are de-risked.","MFE_90D_pct":6.09,"MAE_90D_pct":-9.99,"score_return_alignment_label":"residual_error_or_guard_needed","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L30_C21_WOORI_316140_POLICY_ONLY_CAPITAL_DRAG_2024","trigger_id":"R13L30_C21_WOORI_FALSE_GREEN_20240726","symbol":"316140","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":42,"relative_strength_score":63,"customer_quality_score":0,"policy_or_regulatory_score":62,"valuation_repricing_score":52,"execution_risk_score":48,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":38,"relative_strength_score":58,"customer_quality_score":0,"policy_or_regulatory_score":52,"valuation_repricing_score":45,"execution_risk_score":58,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-watch","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"C21 shadow profile separates explicit ROE/CET1/shareholder-return bridge from policy-only low-PBR beta. Positive cases keep/raise score; Woori/BNK policy-only rows are de-risked.","MFE_90D_pct":5.69,"MAE_90D_pct":-15.08,"score_return_alignment_label":"residual_error_or_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L30_C21_BNK_138930_REGIONAL_POLICY_BETA_2024","trigger_id":"R13L30_C21_BNK_POLICY_S2_20240208","symbol":"138930","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":34,"relative_strength_score":55,"customer_quality_score":0,"policy_or_regulatory_score":58,"valuation_repricing_score":42,"execution_risk_score":32,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":35,"relative_strength_score":56,"customer_quality_score":0,"policy_or_regulatory_score":53,"valuation_repricing_score":43,"execution_risk_score":36,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-watch","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"C21 shadow profile separates explicit ROE/CET1/shareholder-return bridge from policy-only low-PBR beta. Positive cases keep/raise score; Woori/BNK policy-only rows are de-risked.","MFE_90D_pct":11.89,"MAE_90D_pct":-6.39,"score_return_alignment_label":"residual_error_or_guard_needed","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L30_C21_BNK_138930_REGIONAL_POLICY_BETA_2024","trigger_id":"R13L30_C21_BNK_YELLOW_20240729","symbol":"138930","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":39,"relative_strength_score":62,"customer_quality_score":0,"policy_or_regulatory_score":58,"valuation_repricing_score":51,"execution_risk_score":42,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":38,"relative_strength_score":58,"customer_quality_score":0,"policy_or_regulatory_score":52,"valuation_repricing_score":47,"execution_risk_score":48,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-watch","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"C21 shadow profile separates explicit ROE/CET1/shareholder-return bridge from policy-only low-PBR beta. Positive cases keep/raise score; Woori/BNK policy-only rows are de-risked.","MFE_90D_pct":26.19,"MAE_90D_pct":-8.8,"score_return_alignment_label":"residual_error_or_guard_needed","current_profile_verdict":"current_profile_too_late"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_company_level_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Require explicit ROE/CET1/shareholder-return bridge before Stage2-Actionable+ or Green","Positive KB/JB rows had avg 180D MFE above 50% while Woori/BNK policy-only rows had weaker or riskier paths","R13L30_C21_KB_S2A_20240208|R13L30_C21_JB_S2A_20240208|R13L30_C21_WOORI_POLICY_S2_20240208|R13L30_C21_BNK_POLICY_S2_20240208",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_policy_only_green_block,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,false,true,+1,"Policy/regulatory score without confirmed capital-return execution should not promote Green","Reduces Woori/BNK false-positive Green risk and preserves KB/JB positives","R13L30_C21_WOORI_FALSE_GREEN_20240726|R13L30_C21_BNK_YELLOW_20240729",2,2,2,medium,counterexample_guard,"block only Green, not Stage2 watch"
shadow_weight,l6_capital_drag_execution_risk,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Non-bank acquisition/capital-ratio drag should raise execution risk when buyback/cancel evidence is missing","Explains lower 90D/180D score-return alignment for Woori vs KB/JB","R13L30_C21_WOORI_POLICY_S2_20240208",1,1,1,low,sector_shadow_only,"needs more bank/insurance holdout rows"
```

### 25.6 residual_contribution row
```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"30","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["policy_only_false_positive_green","capital_return_bridge_missed","late_green_for_small_high_ROE_financial","4B_full_window_timing_needs_valuation_overlay"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows
```jsonl
```


## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

next_round: R13_loop_31 — L7_BIO_HEALTHCARE_MEDICAL / C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.


## 28. Source Notes

Stock-web files inspected in this run: `atlas/manifest.json`; `atlas/schema.json`; symbol profiles for 105560, 175330, 316140, 138930, 055550; tradable shards for 105560/2024 and 2025, 175330/2024 and 2025, 316140/2024, 138930/2024. The final calibration rows use only the four C21 target symbols 105560, 175330, 316140, and 138930. Research artifacts from `stock_agent` were not opened; no source code was opened; no patch was produced.
