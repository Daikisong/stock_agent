# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "scheduled_round": "R6",
  "scheduled_loop": 11,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 11,
  "computed_next_round": "R7",
  "computed_next_loop": 11,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "K_FINANCIAL_HOLDING_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_FALSE_PREMIUM",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "residual_false_positive_mining",
    "residual_missed_structural_mining",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "4B_non_price_requirement_stress_test",
    "green_strictness_stress_test"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 4,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 3,
  "diversity_score_summary": "estimated +48; wrong_round_penalty=0; repeated_same_symbol_penalty=0; repeated_same_trigger_date_penalty=0; schema_rematerialization_penalty=0",
  "do_not_propose_new_weight_delta": false,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

This loop adds 3 new independent cases, 1 counterexamples, and 3 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

No production scoring is changed. This file only proposes shadow-only sector/canonical rules.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 11
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = K_FINANCIAL_HOLDING_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_FALSE_PREMIUM
round_schedule_status = valid
round_sector_consistency = pass
```

This file follows the prior R5 loop 11 next state and advances to R6. It does not jump to R13 or another sector.

## 3. Previous Coverage / Duplicate Avoidance Check

The prior generated MD was R5 / L5 / C20. This loop moves to the scheduled R6 financial-capital-return round and selects C21. It does not repeat the C20 consumer cases, nor does it perform a live scan.

```text
same_canonical_archetype_research = allowed
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
wrong_round_penalty = 0
schema_rematerialization_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Profile checks:

| symbol | company | profile_path | corporate-action candidates | selected window status |
|---:|---|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | none | clean |
| 086790 | 하나금융지주 | atlas/symbol_profiles/086/086790.json | none | clean |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | none | clean |
| 055550 | 신한지주 | atlas/symbol_profiles/055/055550.json | not aggregated | narrative holdout only |

## 5. Historical Eligibility Gate

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward 180D trading window available = true
required OHLC fields available = true
corporate_action_contaminated_180D_window = false
calibration_usable = true for representative rows
```

The 180D representative windows are all before the stock-web manifest max_date and do not overlap any selected profile corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| BANK_HOLDING_VALUEUP_ROE_PBR_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Bank holding rerating driven by ROE/PBR self-help, payout, buyback, and capital buffer evidence. |
| DIGITAL_BANK_GROWTH_PREMIUM_WITHOUT_CAPITAL_RETURN_FALSE_POSITIVE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Digital-finance growth narrative is a counterexample when it lacks payout/PBR self-help. |
| BANK_HOLDING_PRICE_ONLY_LOCAL_4B_TOO_EARLY | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Capital-return compounders can show local overheat before the thesis is exhausted. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---:|---|---|---|
| R6L11_C21_105560_KB_VALUEUP_CAPITAL_RETURN_20240226 | 105560 | KB금융 | positive / structural success | Strongest clean R6 example of bank-holding capital-return rerating. |
| R6L11_C21_086790_HANA_VALUEUP_ROE_PBR_CAPITAL_RETURN_20240226 | 086790 | 하나금융지주 | positive / stage2 promote candidate | Lower-intensity but clean PBR/ROE/capital-return candidate. |
| R6L11_C21_323410_KAKAOBANK_DIGITAL_PREMIUM_FALSE_STAGE2_20240226 | 323410 | 카카오뱅크 | counterexample / false positive | Digital-finance growth premium did not map to capital-return rerating. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
4B_case_count = 1
4C_case_count = 0
```

The C21 distinction is the difference between a bank that starts returning excess capital like a reservoir opening its gates, and a fintech-looking bank whose story is still mostly the shape of the pipe. KB금융 and 하나금융지주는 ROE/PBR/capital-return evidence converted policy optionality into rerating. 카카오뱅크 had digital-bank growth language, but not the same payout/PBR self-help proof.

## 9. Evidence Source Map

| symbol | evidence family | source status | use |
|---:|---|---|---|
| 105560 | value-up policy optionality, bank-holding PBR/ROE rerating, shareholder return, capital buffer | public policy/news/issuer evidence family; exact issuer payout URLs require enrichment before production promotion | quantitative |
| 086790 | low-PBR bank holding, shareholder-return optionality, capital-return rerating | public policy/news/issuer evidence family; exact issuer payout URLs require enrichment before production promotion | quantitative |
| 323410 | digital-bank growth premium without capital-return/PBR self-help proof | public policy/news/research-summary family; exact URLs require enrichment before production promotion | quantitative counterexample |
| 055550 | same-family financial-holding holdout | checked but not aggregated | narrative-only |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | forward window |
|---:|---|---|---|---|
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | 2024-02-27 | usable |
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | 2024-03-14 | usable 4B overlay |
| 086790 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/symbol_profiles/086/086790.json | 2024-02-27 | usable |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json | 2024-02-27 | usable |

## 11. Case-by-Case Trigger Grid

| case | symbol | trigger | entry | entry_price | MFE_30 | MFE_90 | MFE_180 | MAE_30 | MAE_90 | MAE_180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| KB금융 value-up capital return | 105560 | Stage2-Actionable | 2024-02-27 | 62,400 | +25.96% | +44.23% | +66.51% | -2.40% | -2.40% | -2.40% | structural success / Green too late |
| 하나금융지주 ROE/PBR capital return | 086790 | Stage2-Actionable | 2024-02-27 | 54,700 | +19.20% | +23.95% | +26.69% | -3.47% | -4.57% | -4.57% | stage2 promote candidate |
| 카카오뱅크 digital premium false Stage2 | 323410 | false Stage2 | 2024-02-27 | 29,550 | +3.72% | +3.72% | +3.72% | -7.61% | -32.15% | -37.43% | false positive |
| KB금융 price-only local 4B | 105560 | 4B price-only local peak | 2024-03-14 | 78,600 | +0.00% | +14.50% | +32.19% | -21.12% | -21.12% | -21.12% | 4B too early |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows only:

| metric | 105560 KB금융 | 086790 하나금융지주 | 323410 카카오뱅크 |
|---|---:|---:|---:|
| entry_price | 62,400 | 54,700 | 29,550 |
| MFE_30D_pct | +25.96 | +19.20 | +3.72 |
| MFE_90D_pct | +44.23 | +23.95 | +3.72 |
| MFE_180D_pct | +66.51 | +26.69 | +3.72 |
| MAE_30D_pct | -2.40 | -3.47 | -7.61 |
| MAE_90D_pct | -2.40 | -4.57 | -32.15 |
| MAE_180D_pct | -2.40 | -4.57 | -37.43 |

Aggregate interpretation:

```text
positive_structural_avg_MFE_90D_pct = 34.09
positive_structural_avg_MAE_90D_pct = -3.49
counterexample_MFE_90D_pct = 3.72
counterexample_MAE_90D_pct = -32.15
```

## 13. Current Calibrated Profile Stress Test

| case | likely current profile behavior | actual OHLC alignment | verdict |
|---|---|---|---|
| KB금융 value-up capital return | likely waits for stronger reported revision / generic Green confirmation | +44.23% MFE90 / -2.40% MAE90 | current_profile_too_late |
| 하나금융지주 ROE/PBR capital return | likely recognizes value-up theme but underweights capital-return specificity | +23.95% MFE90 / -4.57% MAE90 | current_profile_too_late |
| 카카오뱅크 digital-bank premium | may over-credit digital-finance relative strength or fintech growth narrative | +3.72% MFE90 / -32.15% MAE90 | current_profile_false_positive |
| KB금융 2024 local 4B | price-only local blowoff looked hot, but full observed window later reached 170,500 | local proximity 1.00 / full-window proximity 0.15 | current_profile_4B_too_early |

Axis verdict:

```text
stage2_actionable_evidence_bonus = existing_axis_strengthened for capital-return evidence
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_weakened only for C21 payout/PBR/ROE self-help exception
stage3_green_revision_min = existing_axis_weakened only when payout/capital-buffer proof is independently strong
stage3_cross_evidence_green_buffer = existing_axis_strengthened
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = not_primary_tested
```

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2 / Watch:
  generic financial beta, policy headline only, digital bank growth premium without capital-return evidence

Stage2-Actionable:
  low-PBR/ROE financial holding + credible shareholder-return optionality + capital buffer evidence

Stage3-Yellow:
  payout/buyback plan visible, but execution cadence or CET1/capital-buffer durability still incomplete

Stage3-Green:
  capital-return evidence + PBR/ROE rerating + financial visibility + low red-team risk

False Green guard:
  digital bank / fintech growth premium without dividend-buyback or capital-return self-help proof

4B overlay:
  valuation blowoff or local price peak only becomes full 4B when non-price evidence also shows payout slowdown, capital-buffer deterioration, regulatory cap, or asset-quality break
```

Green lateness:

| case | early actionable entry | later Green/proxy | full observed peak | green_lateness_ratio | read |
|---|---:|---:|---:|---:|---|
| 105560 KB금융 | 62,400 | 78,600 proxy after March confirmation | 170,500 | 0.15 | Green was early enough only if C21 capital-return exception exists |
| 086790 하나금융지주 | 54,700 | 68,800 proxy after August confirmation | 132,200 | 0.18 | capital-return/PBR evidence should have promoted earlier |
| 323410 카카오뱅크 | not_applicable | false Stage2 | 30,650 local high | not_applicable | false positive |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R6L11_T01B_KB_20240314_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 1.00 | 0.15 | price_only_local_4B_too_early |

In C21, a sharp bank-holding rally can look like a stretched rubber band, but if shareholder-return evidence is still tightening the mechanism, the first local peak is not the same thing as thesis exhaustion. Price-only 4B needs non-price deterioration.

## 16. 4C Protection Audit

```text
hard_4c_success = not_primary_tested
hard_4c_late = not_primary_tested
false_break = not_primary_tested
thesis_break_watch_only = KakaoBank false-positive guard and KB price-only 4B overlay
```

This is a C21 positive-stage and 4B-guard loop, not a hard-4C thesis-break loop.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
candidate_axis = financial_capital_return_self_help_vs_digital_growth_premium
```

Candidate rule:

```text
In L6 financial names, positive-stage promotion should distinguish ROE/PBR self-help and visible shareholder return from digital-finance or policy-headline beta.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
new_axis_proposed:
  - c21_capital_return_pbr_roe_self_help_boost
  - c21_digital_bank_growth_premium_guard
  - c21_price_only_local_4b_too_early_guard
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | current representative | +23.97 | -13.04 | +32.31 | -14.97 | 0.33 | 1 | 2 | 0.17 | mixed; bank rerating late and digital premium false positive |
| P0b e2r_2_0_baseline_reference | 3 | baseline representative | +23.97 | -13.04 | +32.31 | -14.97 | 0.33 | 1 | 2 | 0.17 | overcredits generic financial beta and undercredits payout specificity |
| P1 sector_specific_candidate_profile | 3 | capital-return self-help guard | +34.09 positive / +3.72 blocked | -3.49 positive / -32.15 blocked | +46.60 positive / +3.72 blocked | -3.49 positive / -37.43 blocked | 0.00 | 0 | 0 | 0.17 | better positive/counterexample separation |
| P2 canonical_archetype_candidate_profile | 3 | C21 payout/PBR/ROE boost + digital-premium guard | +34.09 positive / +3.72 blocked | -3.49 positive / -32.15 blocked | +46.60 positive / +3.72 blocked | -3.49 positive / -37.43 blocked | 0.00 | 0 | 0 | 0.17 | best explanatory fit |
| P3 counterexample_guard_profile | 3 | digital-premium guard only | +23.97 | -13.04 | +32.31 | -14.97 | 0.00 false-stage | 1 | 2 | 0.17 | safer, but still under-promotes capital-return positives |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90/MAE90 | alignment |
|---|---:|---|---:|---|---|---|
| 105560 | 83.0 | Stage3-Yellow | 90.0 | Stage3-Green | +44.23 / -2.40 | capital-return rerating captured |
| 086790 | 79.0 | Stage3-Yellow_low | 87.5 | Stage3-Green | +23.95 / -4.57 | stage2 promote candidate aligned |
| 323410 | 72.0 | Stage2-Actionable_false | 55.0 | Stage2-Watch_or_blocked | +3.72 / -32.15 | false positive avoided |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | K_FINANCIAL_HOLDING_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN_VS_DIGITAL_BANK_FALSE_PREMIUM | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 3 | true | true | C21 now has bank-holding capital-return positives, digital-bank false-positive guard, and price-only local 4B too-early overlay. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - capital_return_rerating_too_late
  - digital_bank_premium_false_positive
  - price_only_local_4B_too_early
new_axis_proposed:
  - c21_capital_return_pbr_roe_self_help_boost
  - c21_digital_bank_growth_premium_guard
  - c21_price_only_local_4b_too_early_guard
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened:
  - stage3_green_total_min, only under C21 payout/PBR/ROE self-help exception
  - stage3_green_revision_min, only when payout/capital-buffer evidence is independently strong
existing_axis_kept:
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and raw/unadjusted price basis
- profile availability and corporate-action caveats for 105560, 086790, 323410
- representative entry prices from stock-web tradable shards
- 30D/90D/180D MFE/MAE calculations from stock-web OHLC rows
- clean 180D corporate-action windows for selected quantitative rows
- R6/L6/C21 schedule consistency
```

Not validated:

```text
- production stock_agent source code
- live watchlist or current candidates
- brokerage execution
- exact issuer-specific capital-return filings for production promotion
- post-2026-02-20 price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_capital_return_pbr_roe_self_help_boost,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+1,+1,"ROE/PBR self-help plus payout/buyback visibility separated clean bank-holding rerating from generic financial beta","KB MFE90 +44.23 / MAE90 -2.40; Hana MFE90 +23.95 / MAE90 -4.57","R6L11_T01_KB_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN|R6L11_T02_HANA_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN",3,3,1,medium,canonical_shadow_only,"not production; issuer-specific payout details need enrichment"
shadow_weight,c21_digital_bank_growth_premium_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+1,+1,"Digital-bank growth narrative without capital-return evidence created false-positive Stage2/Green risk","KakaoBank MFE90 +3.72 / MAE90 -32.15","R6L11_T03_KAKAOBANK_20240226_FALSE_STAGE2_DIGITAL_PREMIUM",3,3,1,medium,guardrail_shadow_only,"cap positive-stage promotion unless payout/ROE/PBR self-help is visible"
shadow_weight,c21_price_only_local_4b_too_early_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+0.5,+0.5,"Early valuation blowoff in capital-return bank holdings can be only a local peak when non-price capital-return evidence remains intact","KB local 4B proximity 1.00 but full observed proximity 0.15","R6L11_T01B_KB_20240314_PRICE_ONLY_LOCAL_4B_TOO_EARLY",3,3,1,low,overlay_guard_shadow_only,"strengthens full_4b_requires_non_price_evidence; not standalone exit"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L11_C21_105560_KB_VALUEUP_CAPITAL_RETURN_20240226","symbol":"105560","company_name":"KB금융","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_VALUEUP_ROE_PBR_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L11_T01_KB_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ROE/PBR capital return and policy optionality produced durable rerating; generic revision gates lagged the capital-return signal.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Positive C21 case: financial holding rerating followed shareholder-return proof rather than simple price momentum."}
{"row_type":"case","case_id":"R6L11_C21_086790_HANA_VALUEUP_ROE_PBR_CAPITAL_RETURN_20240226","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_VALUEUP_ROE_PBR_CAPITAL_RETURN","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R6L11_T02_HANA_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"The low-PBR financial holding + capital return evidence generated clean MFE with modest MAE.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Positive C21 case: PBR/ROE/capital-return evidence had better explanatory power than plain financial-sector beta."}
{"row_type":"case","case_id":"R6L11_C21_323410_KAKAOBANK_DIGITAL_PREMIUM_FALSE_STAGE2_20240226","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_GROWTH_PREMIUM_WITHOUT_CAPITAL_RETURN_FALSE_POSITIVE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L11_T03_KAKAOBANK_20240226_FALSE_STAGE2_DIGITAL_PREMIUM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Digital-bank growth premium did not behave like ROE/PBR capital-return rerating; the same policy theme became a trap without payout/capital proof.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample C21 case: digital finance narrative should not substitute for capital-return evidence."}
{"row_type":"trigger","trigger_id":"R6L11_T01_KB_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN","case_id":"R6L11_C21_105560_KB_VALUEUP_CAPITAL_RETURN_20240226","symbol":"105560","company_name":"KB금융","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_VALUEUP_ROE_PBR_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"FINANCIAL_ROE_PBR_CAPITAL_RETURN","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","green_strictness_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea Value-up policy context plus bank-holding capital-return/PBR rerating evidence; timing treated conservatively with next-trading-day close entry.","evidence_source":"Corporate Value-up Programme / shareholder-return public evidence family; Reuters 2024-02-28 and 2024-05-02 used as policy context; issuer-specific payout details require enrichment before production promotion","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal","relative_strength"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":62400,"MFE_30D_pct":25.96,"MFE_90D_pct":44.23,"MFE_180D_pct":66.51,"MFE_1Y_pct":66.51,"MFE_2Y_pct":null,"MAE_30D_pct":-2.4,"MAE_90D_pct":-2.4,"MAE_180D_pct":-2.4,"MAE_1Y_pct":-2.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-13","peak_price":170500,"drawdown_after_peak_pct":-3.99,"green_lateness_ratio":0.15,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_105560_20240227_62400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L11_T01B_KB_20240314_PRICE_ONLY_LOCAL_4B_TOO_EARLY","case_id":"R6L11_C21_105560_KB_VALUEUP_CAPITAL_RETURN_20240226","symbol":"105560","company_name":"KB금융","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_VALUEUP_ROE_PBR_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"FINANCIAL_ROE_PBR_CAPITAL_RETURN","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","green_strictness_stress_test"],"trigger_type":"4B-PriceOnlyLocalPeak","trigger_date":"2024-03-14","evidence_available_at_that_date":"KB had already run sharply by mid-March 2024, but the move was not exhausted: capital-return/value-up evidence later produced a much higher full observed window peak.","evidence_source":"Corporate Value-up Programme / shareholder-return public evidence family; Reuters 2024-02-28 and 2024-05-02 used as policy context; issuer-specific payout details require enrichment before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-14","entry_price":78600,"MFE_30D_pct":0.0,"MFE_90D_pct":14.5,"MFE_180D_pct":32.19,"MFE_1Y_pct":32.19,"MFE_2Y_pct":null,"MAE_30D_pct":-21.12,"MAE_90D_pct":-21.12,"MAE_180D_pct":-21.12,"MAE_1Y_pct":-21.12,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-13","peak_price":170500,"drawdown_after_peak_pct":-3.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.15,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_105560_20240314_78600","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same KB case, different 4B timing family; not representative for aggregate entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R6L11_T02_HANA_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN","case_id":"R6L11_C21_086790_HANA_VALUEUP_ROE_PBR_CAPITAL_RETURN_20240226","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_VALUEUP_ROE_PBR_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"FINANCIAL_ROE_PBR_CAPITAL_RETURN","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","green_strictness_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Low-PBR bank holding + capital-return/value-up policy optionality; entry is next trading day close because public timing is treated conservatively.","evidence_source":"Corporate Value-up Programme / shareholder-return public evidence family; Reuters 2024-02-28 and 2024-05-02 used as policy context; issuer-specific payout details require enrichment before production promotion","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":54700,"MFE_30D_pct":19.2,"MFE_90D_pct":23.95,"MFE_180D_pct":26.69,"MFE_1Y_pct":26.69,"MFE_2Y_pct":null,"MAE_30D_pct":-3.47,"MAE_90D_pct":-4.57,"MAE_180D_pct":-4.57,"MAE_1Y_pct":-4.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-13","peak_price":132200,"drawdown_after_peak_pct":-4.16,"green_lateness_ratio":0.18,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_promote_candidate","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_086790_20240227_54700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L11_T03_KAKAOBANK_20240226_FALSE_STAGE2_DIGITAL_PREMIUM","case_id":"R6L11_C21_323410_KAKAOBANK_DIGITAL_PREMIUM_FALSE_STAGE2_20240226","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_GROWTH_PREMIUM_WITHOUT_CAPITAL_RETURN_FALSE_POSITIVE","sector":"금융·자본배분·디지털금융","primary_archetype":"FINANCIAL_ROE_PBR_CAPITAL_RETURN","loop_objective":["coverage_gap_fill","counterexample_mining","residual_false_positive_mining","residual_missed_structural_mining","sector_specific_rule_discovery","canonical_archetype_compression","4B_non_price_requirement_stress_test","green_strictness_stress_test"],"trigger_type":"FalseStage2-DigitalPremium","trigger_date":"2024-02-26","evidence_available_at_that_date":"Digital bank growth/fintech premium was not the same as capital-return rerating; no strong payout/PBR self-help evidence was visible.","evidence_source":"Corporate Value-up Programme / shareholder-return public evidence family; Reuters 2024-02-28 and 2024-05-02 used as policy context; issuer-specific payout details require enrichment before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":29550,"MFE_30D_pct":3.72,"MFE_90D_pct":3.72,"MFE_180D_pct":3.72,"MFE_1Y_pct":3.72,"MFE_2Y_pct":null,"MAE_30D_pct":-7.61,"MAE_90D_pct":-32.15,"MAE_180D_pct":-37.43,"MAE_1Y_pct":-41.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":30650,"drawdown_after_peak_pct":-39.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"false_positive_guard_needed","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L11_323410_20240227_29550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C21_105560_KB_VALUEUP_CAPITAL_RETURN_20240226","trigger_id":"R6L11_T01_KB_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":50,"relative_strength_score":76,"customer_quality_score":0,"policy_or_regulatory_score":68,"valuation_repricing_score":72,"execution_risk_score":36,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":66,"cet1_or_capital_buffer_score":68,"dividend_buyback_visibility_score":64,"valueup_policy_optionality_score":76,"digital_bank_growth_score":0,"rate_or_nim_tailwind_score":58,"asset_quality_risk_score":36,"positioning_overheat_score":0},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":58,"relative_strength_score":84,"customer_quality_score":0,"policy_or_regulatory_score":82,"valuation_repricing_score":84,"execution_risk_score":34,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":90,"cet1_or_capital_buffer_score":82,"dividend_buyback_visibility_score":88,"valueup_policy_optionality_score":88,"digital_bank_growth_score":0,"rate_or_nim_tailwind_score":64,"asset_quality_risk_score":34,"positioning_overheat_score":0},"weighted_score_after":90.0,"stage_label_after":"Stage3-Green","changed_components":["roe_pbr_capital_return_score","dividend_buyback_visibility_score","cet1_or_capital_buffer_score","valueup_policy_optionality_score"],"component_delta_explanation":"Capital-return and PBR/ROE self-help evidence deserves an earlier C21 promotion than generic revision confirmation alone.","MFE_90D_pct":44.23,"MAE_90D_pct":-2.4,"score_return_alignment_label":"capital-return rerating captured","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C21_086790_HANA_VALUEUP_ROE_PBR_CAPITAL_RETURN_20240226","trigger_id":"R6L11_T02_HANA_20240226_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN","symbol":"086790","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":48,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":66,"valuation_repricing_score":70,"execution_risk_score":38,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":62,"cet1_or_capital_buffer_score":66,"dividend_buyback_visibility_score":62,"valueup_policy_optionality_score":74,"digital_bank_growth_score":0,"rate_or_nim_tailwind_score":56,"asset_quality_risk_score":38,"positioning_overheat_score":0},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow_low","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":54,"relative_strength_score":76,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":78,"execution_risk_score":36,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":84,"cet1_or_capital_buffer_score":80,"dividend_buyback_visibility_score":82,"valueup_policy_optionality_score":86,"digital_bank_growth_score":0,"rate_or_nim_tailwind_score":60,"asset_quality_risk_score":36,"positioning_overheat_score":0},"weighted_score_after":87.5,"stage_label_after":"Stage3-Green","changed_components":["roe_pbr_capital_return_score","dividend_buyback_visibility_score","cet1_or_capital_buffer_score","valueup_policy_optionality_score"],"component_delta_explanation":"The signal is weaker than KB but still aligned: low-PBR capital return evidence created clean upside with limited MAE.","MFE_90D_pct":23.95,"MAE_90D_pct":-4.57,"score_return_alignment_label":"capital-return stage2 promote candidate aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L11_C21_323410_KAKAOBANK_DIGITAL_PREMIUM_FALSE_STAGE2_20240226","trigger_id":"R6L11_T03_KAKAOBANK_20240226_FALSE_STAGE2_DIGITAL_PREMIUM","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":42,"relative_strength_score":48,"customer_quality_score":0,"policy_or_regulatory_score":52,"valuation_repricing_score":58,"execution_risk_score":56,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":22,"cet1_or_capital_buffer_score":50,"dividend_buyback_visibility_score":12,"valueup_policy_optionality_score":38,"digital_bank_growth_score":82,"rate_or_nim_tailwind_score":0,"asset_quality_risk_score":52,"positioning_overheat_score":0},"weighted_score_before":72.0,"stage_label_before":"Stage2-Actionable_false","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":34,"relative_strength_score":34,"customer_quality_score":0,"policy_or_regulatory_score":40,"valuation_repricing_score":36,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":10,"cet1_or_capital_buffer_score":48,"dividend_buyback_visibility_score":6,"valueup_policy_optionality_score":24,"digital_bank_growth_score":76,"rate_or_nim_tailwind_score":0,"asset_quality_risk_score":66,"positioning_overheat_score":0},"weighted_score_after":55.0,"stage_label_after":"Stage2-Watch_or_blocked","changed_components":["digital_bank_growth_score","dividend_buyback_visibility_score","roe_pbr_capital_return_score","valuation_repricing_score","asset_quality_risk_score"],"component_delta_explanation":"Digital-bank growth premium should not substitute for payout/ROE/PBR capital-return evidence under C21.","MFE_90D_pct":3.72,"MAE_90D_pct":-32.15,"score_return_alignment_label":"false positive blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R6","loop":"11","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["capital_return_rerating_too_late","digital_bank_premium_false_positive","price_only_local_4B_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R6L11_C21_055550_SHINHAN_HOLDOUT_NOT_AGGREGATED","symbol":"055550","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"same financial holding/capital-return family candidate, deliberately not aggregated to avoid over-weighting bank holdings in one loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R6
completed_loop = 11
next_round = R7
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- stock-web manifest: atlas/manifest.json.
- 105560 profile: atlas/symbol_profiles/105/105560.json.
- 086790 profile: atlas/symbol_profiles/086/086790.json.
- 323410 profile: atlas/symbol_profiles/323/323410.json.
- 105560 OHLC: atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv, 2025.csv, and 2026.csv.
- 086790 OHLC: atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv and 2026.csv.
- 323410 OHLC: atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv.
- Policy context: Reuters 2024-02-28 and 2024-05-02 Corporate Value-up coverage.
- Issuer-specific capital-return URLs require enrichment before production promotion.
- No live candidate scan, no production patch, no brokerage action.
