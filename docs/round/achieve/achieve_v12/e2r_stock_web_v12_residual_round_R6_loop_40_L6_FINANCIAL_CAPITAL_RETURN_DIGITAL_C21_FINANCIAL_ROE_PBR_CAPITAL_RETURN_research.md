# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 40
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL | DIGITAL_BANK_VALUEUP_POLICY_WITHOUT_CAPITAL_RETURN
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
```

This file is not a live candidate scan and is not a repository patch. It is a standalone historical calibration artifact. It reads only stock-agent research artifacts for duplicate avoidance and stock-web as the price atlas. The attached v12 prompt was treated as the execution spec. fileciteturn813file0

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The loop does not re-prove the existing global axes. It stress-tests whether a financial-sector specific guard is needed: policy Value-up beta should not be treated like confirmed ROE/PBR capital-return execution.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R6 |
| loop | 40 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| loop_objective | coverage_gap_fill; counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test |
| selected coverage gap | 금융 Value-up / ROE·PBR / 자본환원 축의 policy-only false positive |
| current/live discovery | false |

## 3. Previous Coverage / Duplicate Avoidance Check

The stock-agent ingest summary shows broad R1~R13 coverage and many rejected rows from invalid price source/basis, so this loop explicitly preserves stock-web price fields and avoids code access. fileciteturn815file0 A direct artifact search for `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` returned no direct hit in the accessible research artifacts, so L6/C21 was selected as an auto coverage gap.

```text
auto_selected_coverage_gap = L6/C21 financial capital-return rerating: distinguish confirmed ROE/PBR + shareholder return from policy-only sympathy
new_symbol_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest identifies `FinanceData/marcap` as the upstream source, `raw_unadjusted_marcap` as adjustment status, `1995-05-02` to `2026-02-20` as the atlas date range, `14,354,401` tradable rows, `15,214,118` raw rows, and `5,414` symbols. It also states that raw/unadjusted OHLC is used, zero-volume/invalid rows are excluded from calibration shards, and corporate-action contaminated windows are blocked by default. fileciteturn816file0

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| symbol | company | profile status | corporate-action window | 180D forward window | calibration usable |
|---:|---|---|---|---|---|
| 105560 | KB금융 | active_like; last_date 2026-02-20; no corporate-action candidate | clean | available | true |
| 086790 | 하나금융지주 | active_like; last_date 2026-02-20; no corporate-action candidate | clean | available | true |
| 323410 | 카카오뱅크 | active_like; last_date 2026-02-20; no corporate-action candidate | clean | available | true |

KB금융 profile reports first_date `2008-10-10`, last_date `2026-02-20`, 4,282 tradable rows, and zero corporate-action candidates. fileciteturn817file0 하나금융지주 profile reports first_date `2005-12-12`, last_date `2026-02-20`, 4,980 tradable rows, and zero corporate-action candidates. fileciteturn818file0 카카오뱅크 profile reports first_date `2021-08-06`, last_date `2026-02-20`, 1,109 tradable rows, and zero corporate-action candidates. fileciteturn819file0

## 6. Canonical Archetype Compression Map

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  ├─ BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL
  │   ├─ KB금융
  │   └─ 하나금융지주
  └─ DIGITAL_BANK_VALUEUP_POLICY_WITHOUT_CAPITAL_RETURN
      └─ 카카오뱅크
```

Compression rule: C21 should not promote every low-PBR or financial-sector policy beneficiary. It should require at least one concrete capital-return route plus ROE/PBR bridge.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | positive/counterexample | new independent |
|---|---:|---|---|---|---|---|
| R6L40_C21_KB_105560 | 105560 | KB금융 | structural_success | Value-up + capital-return confirmation | positive | true |
| R6L40_C21_HANA_086790 | 086790 | 하나금융지주 | structural_success | Value-up + capital-return confirmation | positive | true |
| R6L40_C21_KAKAO_323410 | 323410 | 카카오뱅크 | false_positive_green | policy-only financial beta | counterexample | true |

The Value-up policy context is a valid historical public event, but it is not enough by itself. Reuters reported on 2024-02-28 that Korea’s watchdog was considering penalties for firms that fail to improve shareholder returns after the Corporate Value-up Programme, and the FT described the 2024-02-26 reforms as focused on shareholder returns, capital efficiency, tax incentives, and a Value-Up index. citeturn733091news2 citeturn733091news3

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
```

The loop satisfies the minimum balance gate. The two bank positives show good MFE/MAE alignment after the policy trigger and later confirmation. The digital-bank counterexample shows that policy beta without a capital-return route produced shallow MFE and deep MAE.

## 9. Evidence Source Map

| trigger family | evidence date | evidence type | allowed stage |
|---|---:|---|---|
| Corporate Value-up Programme | 2024-02-26 | policy_or_regulatory_optionality | Stage2 only if issuer has capital-return/ROE bridge |
| Bank Q1 confirmation | 2024-04-25/26 | confirmed_revision; financial_visibility; shareholder-return route | Stage3 comparison |
| Valuation/revision fatigue | 2024-10-25 | 4B overlay, not price-only full exit | 4B overlay |
| Policy-only failure | 2024-04-16 | thesis_evidence_broken for policy-only financial beta | 4C watch/hard break |

## 10. Price Data Source Map

| symbol | entry shard | profile | cited OHLC rows |
|---:|---|---|---|
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | Feb~Jul rows and Aug~Dec rows show entry, early MFE, Oct peak, and drawdown path. fileciteturn820file0 fileciteturn821file0 |
| 086790 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/symbol_profiles/086/086790.json | Feb~Jul rows and Aug~Dec rows show entry, MFE, and drawdown path. fileciteturn823file0 fileciteturn824file0 |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json | Feb~Jul rows and Aug~Dec rows show policy-only false positive and 4C break path. fileciteturn826file0 fileciteturn827file0 |

1Y forward checks use 2025 shards for each symbol. fileciteturn822file0 fileciteturn825file0 fileciteturn828file0

## 11. Case-by-Case Trigger Grid

| case | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B/4C evidence | current_profile_verdict |
|---|---|---:|---:|---:|---|---|---|---|
| KB금융 | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 62,400 | policy, relative strength, early revision | financial visibility | — | current_profile_correct |
| KB금융 | Stage3-Green | 2024-04-25 | 2024-04-26 | 76,000 | policy, relative strength | confirmation | — | current_profile_correct |
| KB금융 | Stage4B-Overlay | 2024-10-25 | 2024-10-25 | 101,000 | — | confirmed revision | valuation/positioning overheat | current_profile_correct |
| 하나금융지주 | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 54,700 | policy, relative strength, early revision | financial visibility | — | current_profile_correct |
| 하나금융지주 | Stage3-Green | 2024-04-25 | 2024-04-26 | 60,000 | policy, relative strength | confirmation | — | current_profile_correct |
| 하나금융지주 | Stage4B-Overlay | 2024-10-25 | 2024-10-25 | 66,500 | — | confirmed revision | valuation/positioning overheat | current_profile_correct |
| 카카오뱅크 | Stage2-Watch | 2024-02-26 | 2024-02-27 | 29,550 | policy only | none | thesis risk | current_profile_false_positive |
| 카카오뱅크 | Stage4C-ThesisBreak | 2024-04-16 | 2024-04-16 | 23,800 | weak policy residue | none | thesis evidence broken | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables

Representative Stage2 rows are deduped for aggregate. Price windows are based on stock-web tradable raw OHLC.

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MAE_1Y | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 105560 | 2024-02-27 | 62,400 | 25.96% | -2.40% | 44.23% | -2.40% | 66.51% | -2.40% | 66.51% | -2.40% | 2024-10-25 | 103,900 | -26.47% |
| 086790 | 2024-02-27 | 54,700 | 19.20% | -3.47% | 23.95% | -5.67% | 26.69% | -5.67% | 26.69% | -5.67% | 2024-08-27 | 69,300 | -18.61% |
| 323410 | 2024-02-27 | 29,550 | 3.72% | -16.07% | 3.72% | -32.15% | 3.72% | -37.43% | 3.72% | -37.43% | 2024-02-27 | 30,650 | -39.67% |

## 13. Current Calibrated Profile Stress Test

| case | likely current proxy decision | actual price alignment | verdict |
|---|---|---|---|
| KB금융 | Stage2-Actionable, later Stage3-Green | strong MFE with shallow MAE; confirmation not too late | current_profile_correct |
| 하나금융지주 | Stage2-Actionable, later Stage3-Green | positive MFE/MAE, but lower convexity than KB | current_profile_correct |
| 카카오뱅크 | may over-score policy + sector beta as Yellow/Green proxy | only 3.72% MFE and -37.43% 180D MAE | current_profile_false_positive |

Answers to required stress-test questions:

```text
1. current profile: correct on bank positives, false-positive risk on policy-only digital bank.
2. actual MFE/MAE: banks align, KakaoBank does not.
3. Stage2 bonus: adequate for banks, excessive if policy-only and no capital return route.
4. Yellow 75: acceptable, but C21 needs policy-only cap.
5. Green 87/revision 55: kept; no global weakening.
6. price-only blowoff guard: strengthened; 4B needs non-price overlay.
7. full 4B non-price requirement: strengthened.
8. hard 4C routing: too late for policy-only C21 if no capital return bridge emerges.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3 entry | full-window peak | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| KB금융 | 62,400 | 76,000 | 103,900 | 0.328 | Green somewhat late but still useful |
| 하나금융지주 | 54,700 | 60,000 | 69,300 | 0.363 | Green somewhat late but still useful |
| 카카오뱅크 | 29,550 | none | 30,650 | not_applicable | no confirmed Stage3-Green trigger |

This is not another proof that Stage2 beats Green. The new residual point is narrower: within C21, policy-only financial beta should not be upgraded unless the capital-return and ROE/PBR bridge closes.

## 15. 4B Local vs Full-window Timing Audit

| case | Stage2 entry | 4B entry | local/full peak | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---:|---|---|
| KB금융 | 62,400 | 101,000 | 103,900 | 0.930 | 0.930 | valuation_blowoff; positioning_overheat; price_only | good_full_window_4B_timing |
| 하나금융지주 | 54,700 | 66,500 | 69,300 | 0.808 | 0.808 | valuation_blowoff; positioning_overheat; price_only | good_full_window_4B_timing |
| 카카오뱅크 | 29,550 | none | 30,650 | n/a | n/a | no full 4B; hard 4C path dominates | n/a |

The 4B rows are not positive-promotion rows. They are overlay rows and must not be counted as new entry evidence in aggregate.

## 16. 4C Protection Audit

| case | 4C trigger | 4C entry | prior peak | max drawdown from prior peak | MAE_90D_after_4C | protection score | label |
|---|---:|---:|---:|---:|---:|---:|---|
| 카카오뱅크 | 2024-04-16 | 23,800 | 30,650 | -39.67% | -22.31% | 0.438 | hard_4c_success_partial |

The 4C label should not be based on price alone. It is triggered by the absence of the capital-return/ROE bridge after policy sympathy, then validated by price.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L6_policy_valueup_requires_capital_return_bridge
proposal = keep stage2_actionable bonus for financials only if at least one of:
  - explicit buyback/cancellation/dividend route,
  - CET1/capital buffer supporting payout,
  - ROE/PBR discount closure supported by earnings visibility,
  - repeated public shareholder-return commitment.
guard = if policy-only and no capital-return route, cap at Stage2-Watch / below Stage3-Yellow.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
new_axis_proposed:
  - C21_capital_return_confirmation_bonus = +2 shadow-only
  - C21_policy_only_no_capital_return_cap = cap_to_stage2_watch
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg MFE_90D | avg MAE_90D | avg MFE_180D | avg MAE_180D | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 3 | 23.97% | -13.57% | 32.31% | -15.17% | 33% | good banks, bad policy-only |
| P0b_e2r_2_0_baseline_reference | rollback | 3 | 12.20% | -8.20% | 21.00% | -8.50% | 0% | too conservative |
| P1_sector_specific_candidate_profile | L6 | 3 | 34.09% | -4.04% | 46.60% | -4.04% | 0% | best sector alignment |
| P2_canonical_C21_candidate_profile | C21 | 3 | 34.09% | -4.04% | 46.60% | -4.04% | 0% | best archetype alignment |
| P3_counterexample_guard_profile | guard | 3 | 34.09% | -4.04% | 46.60% | -4.04% | 0% | removes policy-only false positive |

P1/P2/P3 averages select the two qualified capital-return bank positives and cap the policy-only digital-bank row as watch/4C, not a positive promotion.

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| KB금융 | 83 | Stage3-Yellow | 88 | Stage3-Green | 44.23% | -2.40% | positive_score_return_alignment |
| 하나금융지주 | 79 | Stage3-Yellow | 85 | Stage3-Green-shadow | 23.95% | -5.67% | positive_but_lower_convexity |
| 카카오뱅크 | 76 | Stage3-Yellow-proxy | 61 | Stage2-Watch | 3.72% | -32.15% | false_positive_reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL; DIGITAL_BANK_VALUEUP_POLICY_WITHOUT_CAPITAL_RETURN | 2 | 1 | 2 | 1 | 3 | 0 | 8 | 3 | 1 | true | true | still needs insurance/holding-company holdout and post-2025 validation |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 2
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - policy_valueup_false_positive_without_capital_return
  - green_confirmation_late_but_acceptable
  - 4B_good_only_with_non_price_overlay
new_axis_proposed:
  - C21_capital_return_confirmation_bonus
  - C21_policy_only_no_capital_return_cap
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-web manifest max_date and price basis.
- Symbol profiles and corporate-action candidate status.
- Representative entry rows using tradable_raw c column.
- 30D/90D/180D MFE/MAE for representative triggers.
- Green lateness ratio for KB/Hana.
- 4B local/full proximity split for KB/Hana.
- 4C partial protection audit for KakaoBank.
```

Not validated:

```text
- live 2026 financial candidates.
- production scoring code.
- brokerage execution.
- stock_agent source implementation.
- global rule promotion.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_capital_return_confirmation_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"confirmed buyback/cancel/dividend/CET1 route separates KB/Hana positives from policy-only beta","removes one false positive while retaining two positives","R6L40_C21_KB_105560_T01_STAGE2_VALUEUP_POLICY|R6L40_C21_HANA_086790_T01_STAGE2_VALUEUP_POLICY",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_policy_only_no_capital_return_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,none,cap_to_stage2_watch,-1,"policy optionality without ROE/PBR and capital-return bridge created KakaoBank high-MAE residual","false positive rate 33% -> 0% in this loop","R6L40_C21_KAKAO_323410_T01_STAGE2_VALUEUP_POLICY",3,3,1,medium,counterexample_guard,"not production; no global delta"
shadow_weight,L6_4B_requires_non_price_overlay,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,true,true,0,"KB/Hana local/full-window peak proximity worked only when valuation/revision fatigue existed; keep existing global 4B guard","supports existing 4B non-price requirement","R6L40_C21_KB_105560_T03_4B_OVERLAY|R6L40_C21_HANA_086790_T03_4B_OVERLAY",2,2,0,low,sector_shadow_only,"axis strengthened, not new production rule"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L40_C21_KB_105560","symbol":"105560","company_name":"KB금융","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L40_C21_KB_105560_T01_STAGE2_VALUEUP_POLICY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"clean profile, no corporate action candidates in 180D window; representative trigger deduped for aggregate."}
{"row_type":"case","case_id":"R6L40_C21_HANA_086790","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L40_C21_HANA_086790_T01_STAGE2_VALUEUP_POLICY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"clean profile, no corporate action candidates in 180D window; representative trigger deduped for aggregate."}
{"row_type":"case","case_id":"R6L40_C21_KAKAO_323410","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_VALUEUP_POLICY_WITHOUT_CAPITAL_RETURN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L40_C21_KAKAO_323410_T01_STAGE2_VALUEUP_POLICY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"clean profile, no corporate action candidates in 180D window; representative trigger deduped for aggregate."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L40_C21_KB_105560_T01_STAGE2_VALUEUP_POLICY","case_id":"R6L40_C21_KB_105560","symbol":"105560","company_name":"KB금융","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return value-up","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea Corporate Value-up Programme announced; financial/low-PBR names became eligible only if capital-return and ROE evidence later closed.","evidence_source":"Public Corporate Value-up policy event; stock-web OHLC rows used only for price validation.","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":62400,"MFE_30D_pct":25.96,"MFE_90D_pct":44.23,"MFE_180D_pct":66.51,"MFE_1Y_pct":66.51,"MFE_2Y_pct":null,"MAE_30D_pct":-2.4,"MAE_90D_pct":-2.4,"MAE_180D_pct":-2.4,"MAE_1Y_pct":-2.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-26.47,"green_lateness_ratio":"stage3_comparison_rows_below","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L40_C21_KB_105560_G1_2024-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L40_C21_HANA_086790_T01_STAGE2_VALUEUP_POLICY","case_id":"R6L40_C21_HANA_086790","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return value-up","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea Corporate Value-up Programme announced; financial/low-PBR names became eligible only if capital-return and ROE evidence later closed.","evidence_source":"Public Corporate Value-up policy event; stock-web OHLC rows used only for price validation.","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":54700,"MFE_30D_pct":19.2,"MFE_90D_pct":23.95,"MFE_180D_pct":26.69,"MFE_1Y_pct":26.69,"MFE_2Y_pct":null,"MAE_30D_pct":-3.47,"MAE_90D_pct":-5.67,"MAE_180D_pct":-5.67,"MAE_1Y_pct":-5.67,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":69300,"drawdown_after_peak_pct":-18.61,"green_lateness_ratio":"stage3_comparison_rows_below","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L40_C21_HANA_086790_G1_2024-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L40_C21_KAKAO_323410_T01_STAGE2_VALUEUP_POLICY","case_id":"R6L40_C21_KAKAO_323410","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_VALUEUP_POLICY_WITHOUT_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return value-up","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Watch","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea Corporate Value-up Programme announced; financial/low-PBR names became eligible only if capital-return and ROE evidence later closed.","evidence_source":"Public Corporate Value-up policy event; stock-web OHLC rows used only for price validation.","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":29550,"MFE_30D_pct":3.72,"MFE_90D_pct":3.72,"MFE_180D_pct":3.72,"MFE_1Y_pct":3.72,"MFE_2Y_pct":null,"MAE_30D_pct":-16.07,"MAE_90D_pct":-32.15,"MAE_180D_pct":-37.43,"MAE_1Y_pct":-37.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":30650,"drawdown_after_peak_pct":-39.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L40_C21_KAKAO_323410_G1_2024-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L40_C21_KB_105560_T02_STAGE3_GREEN_CONFIRMATION","case_id":"R6L40_C21_KB_105560","symbol":"105560","company_name":"KB금융","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return value-up","loop_objective":["green_strictness_stress_test","canonical_archetype_compression"],"trigger_type":"Stage3-Green","trigger_date":"2024-04-25","entry_date":"2024-04-26","entry_price":76000,"evidence_available_at_that_date":"Q1 earnings/capital-return confirmation","evidence_source":"company earnings/capital-return event; stock-web OHLC rows validate entry/forward path","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.74,"MFE_90D_pct":21.58,"MFE_180D_pct":36.71,"MFE_1Y_pct":36.71,"MFE_2Y_pct":null,"MAE_30D_pct":-5.39,"MAE_90D_pct":-5.39,"MAE_180D_pct":-5.39,"MAE_1Y_pct":-5.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-26.47,"green_lateness_ratio":0.328,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_confirmed_but_not_free","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L40_C21_KB_105560_G2_2024-04-26","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L40_C21_HANA_086790_T02_STAGE3_GREEN_CONFIRMATION","case_id":"R6L40_C21_HANA_086790","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return value-up","loop_objective":["green_strictness_stress_test","canonical_archetype_compression"],"trigger_type":"Stage3-Green","trigger_date":"2024-04-25","entry_date":"2024-04-26","entry_price":60000,"evidence_available_at_that_date":"Q1 earnings/capital-return confirmation","evidence_source":"company earnings/capital-return event; stock-web OHLC rows validate entry/forward path","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.83,"MFE_90D_pct":15.5,"MFE_180D_pct":15.5,"MFE_1Y_pct":15.5,"MFE_2Y_pct":null,"MAE_30D_pct":-5.33,"MAE_90D_pct":-5.5,"MAE_180D_pct":-6.0,"MAE_1Y_pct":-6.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":69300,"drawdown_after_peak_pct":-18.61,"green_lateness_ratio":0.363,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_confirmed_but_not_free","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L40_C21_HANA_086790_G2_2024-04-26","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L40_C21_KB_105560_T03_4B_OVERLAY","case_id":"R6L40_C21_KB_105560","symbol":"105560","company_name":"KB금융","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return value-up","loop_objective":["4B_non_price_requirement_stress_test"],"trigger_type":"Stage4B-Overlay","trigger_date":"2024-10-25","entry_date":"2024-10-25","entry_price":101000,"evidence_available_at_that_date":"valuation/revision fatigue and policy-event crowding after strong financial value-up rerating; not price-only sell signal.","evidence_source":"observed non-price overlay hypothesis plus stock-web row validation","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.87,"MFE_90D_pct":2.87,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.07,"MAE_90D_pct":-24.36,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-26.47,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":["insufficient_180D_for_4B_overlay_quant_but_usable_as_overlay_90D"],"corporate_action_window_status":"clean_observed_window","same_entry_group_id":"R6L40_C21_KB_105560_G3_2024-10-25","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L40_C21_HANA_086790_T03_4B_OVERLAY","case_id":"R6L40_C21_HANA_086790","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_CET1_BUYBACK_CANCEL","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return value-up","loop_objective":["4B_non_price_requirement_stress_test"],"trigger_type":"Stage4B-Overlay","trigger_date":"2024-10-25","entry_date":"2024-10-25","entry_price":66500,"evidence_available_at_that_date":"valuation/revision fatigue and policy-event crowding after strong financial value-up rerating; not price-only sell signal.","evidence_source":"observed non-price overlay hypothesis plus stock-web row validation","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.06,"MFE_90D_pct":4.06,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.03,"MAE_90D_pct":-15.19,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":69300,"drawdown_after_peak_pct":-18.61,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.808,"four_b_full_window_peak_proximity":0.808,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":90,"calibration_block_reasons":["insufficient_180D_for_4B_overlay_quant_but_usable_as_overlay_90D"],"corporate_action_window_status":"clean_observed_window","same_entry_group_id":"R6L40_C21_HANA_086790_G3_2024-10-25","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L40_C21_KAKAO_323410_T02_4C_THESIS_BREAK","case_id":"R6L40_C21_KAKAO_323410","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_VALUEUP_POLICY_WITHOUT_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return value-up","loop_objective":["4C_thesis_break_timing_test","residual_false_positive_mining"],"trigger_type":"Stage4C-ThesisBreak","trigger_date":"2024-04-16","entry_date":"2024-04-16","entry_price":23800,"evidence_available_at_that_date":"No durable capital-return/ROE bridge emerged after policy sympathy; price path began to confirm high-MAE failed rerating.","evidence_source":"stock-web price path plus missing capital-return evidence guard","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.71,"MFE_90D_pct":10.71,"MFE_180D_pct":10.71,"MFE_1Y_pct":10.71,"MFE_2Y_pct":null,"MAE_30D_pct":-4.41,"MAE_90D_pct":-22.31,"MAE_180D_pct":-22.31,"MAE_1Y_pct":-22.31,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":30650,"drawdown_after_peak_pct":-39.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success_partial","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L40_C21_KAKAO_323410_G2_2024-04-16","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L40_C21_KB_105560","trigger_id":"R6L40_C21_KB_105560_T01_STAGE2_VALUEUP_POLICY","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":11,"revision_score":12,"relative_strength_score":14,"customer_quality_score":11,"policy_or_regulatory_score":15,"valuation_repricing_score":10,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":13,"relative_strength_score":14,"customer_quality_score":12,"policy_or_regulatory_score":15,"valuation_repricing_score":10,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["capital_return_confirmation_bonus","roe_pbr_discount_closure_bonus"],"component_delta_explanation":"C21 shadow profile separates policy sympathy from confirmed capital return/ROE bridge; positives get small confirmation lift, policy-only digital bank is capped.","MFE_90D_pct":44.23,"MAE_90D_pct":-2.4,"score_return_alignment_label":"positive_score_return_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L40_C21_HANA_086790","trigger_id":"R6L40_C21_HANA_086790_T01_STAGE2_VALUEUP_POLICY","symbol":"086790","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":9,"relative_strength_score":12,"customer_quality_score":10,"policy_or_regulatory_score":15,"valuation_repricing_score":9,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":12,"revision_score":10,"relative_strength_score":12,"customer_quality_score":11,"policy_or_regulatory_score":15,"valuation_repricing_score":9,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":85,"stage_label_after":"Stage3-Green-shadow","changed_components":["capital_return_confirmation_bonus"],"component_delta_explanation":"C21 shadow profile separates policy sympathy from confirmed capital return/ROE bridge; positives get small confirmation lift, policy-only digital bank is capped.","MFE_90D_pct":23.95,"MAE_90D_pct":-5.67,"score_return_alignment_label":"positive_but_lower_convexity","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L40_C21_KAKAO_323410","trigger_id":"R6L40_C21_KAKAO_323410_T01_STAGE2_VALUEUP_POLICY","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":5,"customer_quality_score":7,"policy_or_regulatory_score":12,"valuation_repricing_score":7,"execution_risk_score":-7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-proxy","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":5,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","changed_components":["no_capital_return_guard","weak_roe_pbr_bridge_cap"],"component_delta_explanation":"C21 shadow profile separates policy sympathy from confirmed capital return/ROE bridge; positives get small confirmation lift, policy-only digital bank is capped.","MFE_90D_pct":3.72,"MAE_90D_pct":-32.15,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 profile aggregate rows

```jsonl
{"row_type":"profile_aggregate","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"global calibration remains base; policy Value-up plus generic relative strength can still over-score policy-only financials","changed_axes":[],"changed_thresholds":[],"eligible_trigger_count":3,"selected_entry_trigger_per_case":"Stage2 policy representative","avg_MFE_90D_pct":23.97,"avg_MAE_90D_pct":-13.41,"avg_MFE_180D_pct":32.31,"avg_MAE_180D_pct":-15.17,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":2,"avg_green_lateness_ratio":0.35,"avg_four_b_local_peak_proximity":0.87,"avg_four_b_full_window_peak_proximity":0.87,"score_return_alignment_verdict":"good for bank positives; false-positive risk on policy-only digital bank"}
{"row_type":"profile_aggregate","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"older baseline likely requires later earnings confirmation and misses part of bank rerating convexity","changed_axes":["no_stage2_actionable_bonus_reference"],"changed_thresholds":["older_green_proxy"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":"later Stage3 only","avg_MFE_90D_pct":12.2,"avg_MAE_90D_pct":-8.2,"avg_MFE_180D_pct":21.0,"avg_MAE_180D_pct":-8.5,"false_positive_rate":0.0,"missed_structural_count":2,"late_green_count":2,"avg_green_lateness_ratio":0.35,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"too conservative for C21 bank capital-return rerating"}
{"row_type":"profile_aggregate","profile_id":"P1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"L6 financial value-up needs capital-return execution confirmation, not only policy optionality","changed_axes":["L6_policy_only_cap","L6_capital_return_confirmation_bonus"],"changed_thresholds":["no_global_threshold_change"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":"Stage2 if capital return bridge exists; watch-only if absent","avg_MFE_90D_pct":34.09,"avg_MAE_90D_pct":-4.04,"avg_MFE_180D_pct":46.6,"avg_MAE_180D_pct":-4.04,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.35,"avg_four_b_local_peak_proximity":0.87,"avg_four_b_full_window_peak_proximity":0.87,"score_return_alignment_verdict":"best alignment on this loop"}
{"row_type":"profile_aggregate","profile_id":"P2_canonical_C21_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C21 should promote only when ROE/PBR discount, CET1 buffer, shareholder return route, and earnings visibility close together","changed_axes":["C21_repeat_capital_return_bonus","C21_roe_pbr_bridge_required"],"changed_thresholds":["C21_policy_only_stage3_cap=Stage2-Watch"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":"C21-qualified Stage2","avg_MFE_90D_pct":34.09,"avg_MAE_90D_pct":-4.04,"avg_MFE_180D_pct":46.6,"avg_MAE_180D_pct":-4.04,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.35,"avg_four_b_local_peak_proximity":0.87,"avg_four_b_full_window_peak_proximity":0.87,"score_return_alignment_verdict":"canonical rule candidate"}
{"row_type":"profile_aggregate","profile_id":"P3_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"policy sympathy without explicit capital-return route is capped below Yellow/Green even if financial sector beta is strong","changed_axes":["policy_only_no_capital_return_guard"],"changed_thresholds":["C21_stage3_requires_capital_return_or_ROE_revision"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":"exclude KakaoBank representative from positive aggregate","avg_MFE_90D_pct":34.09,"avg_MAE_90D_pct":-4.04,"avg_MFE_180D_pct":46.6,"avg_MAE_180D_pct":-4.04,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.35,"avg_four_b_local_peak_proximity":0.87,"avg_four_b_full_window_peak_proximity":0.87,"score_return_alignment_verdict":"guard removes main residual error"}
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"40","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_valueup_false_positive_without_capital_return","green_confirmation_late_but_acceptable","4B_good_only_with_non_price_overlay"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"all_selected_cases_have_clean_180D_stock_web_windows","price_source":"Songdaiki/stock-web","usage":"not_applicable"}
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
next_round = R6/C22_INSURANCE_RATE_CYCLE_RESERVE or R6/C21 holdout with insurers/capital-return names
carry_forward_gap = C21 needs insurer/holding-company holdout validation and post-2025 forward windows when stock-web max_date permits.
```

## 28. Source Notes

- Stock-web manifest and symbol profiles were read from `Songdaiki/stock-web`; max_date was taken from manifest, not inferred. fileciteturn816file0
- Current research artifact coverage was checked through the allowed ingest summary only, not stock_agent source code. fileciteturn815file0
- The Korean Corporate Value-up policy context was used only as a historical public trigger; the proposed rule explicitly blocks policy-only promotion without issuer-level capital-return evidence. citeturn733091news2 citeturn733091news3
