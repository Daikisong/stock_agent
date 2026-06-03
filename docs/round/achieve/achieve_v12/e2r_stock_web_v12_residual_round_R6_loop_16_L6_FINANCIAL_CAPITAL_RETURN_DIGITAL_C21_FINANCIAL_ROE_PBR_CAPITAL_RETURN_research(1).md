# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R6
scheduled_loop: 16
completed_round: R6
completed_loop: 16
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD
output_file: e2r_stock_web_v12_residual_round_R6_loop_16_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
stock_web_price_atlas_access_required: true
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

The baseline for this residual run is not the old E2R 2.0 profile. It is the already-calibrated `e2r_2_1_stock_web_calibrated_proxy`:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-argue those global axes. It stress-tests them inside C21 bank/financial capital-return cases.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R6`
- scheduled_loop: `16`
- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`
- fine_archetype_id: `BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD`
- loop_objective: `sector_specific_rule_discovery`, `counterexample_mining`, `current_profile_stress_test`, `coverage_gap_fill`

R6 hard gate passes because R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were used only for duplicate and coverage avoidance. No `src/e2r` code was opened. Legacy R6 files existed in the registry under financial/capital-allocation rounds, but no completed v12 R6 loop 16 residual MD with this filename was found in the checked registry/search state. The selected cases emphasize new independent symbol/trigger-family coverage rather than repeating earlier generic bank/PBR rows.

Diversity result:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
counterexample_count = 2
positive_case_count = 2
minimum_new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

The manifest confirms raw/unadjusted OHLC, calibration-safe tradable shards, and corporate-action blocking as a default rule. This MD treats all quantitative rows as `tradable_raw`, not adjusted price.

## 5. Historical Eligibility Gate

All representative quantitative cases satisfy:

- past trigger date
- entry date present in the stock-web tradable shard
- at least 180 trading days available after entry date
- OHLCV rows available
- 30D/90D/180D MFE and MAE calculated
- no profile-level corporate-action candidate date overlapping the 180D calibration window

One analytically relevant Meritz case is retained as narrative-only because its profile has corporate-action candidate dates overlapping the likely capital-return calibration window.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression logic |
|---|---|---|
| BANK_ROE_PBR_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Bank rerating requires ROE/PBR valuation reset plus visible capital-return execution. |
| BANK_DIVIDEND_YIELD_WITHOUT_REPRICE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Dividend/yield-only setups are negative/guard examples inside the same canonical type. |
| DIGITAL_BANK_PBR_PREMIUM_FALSE_POSITIVE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Digital bank premium is not a C21 positive unless recurring ROE and capital return are both visible. |

## 7. Case Selection Summary

|case_id|symbol|company_name|role|best_trigger|current_profile_verdict|
|---|---|---|---|---|---|
|R6L16_KB_20240208_CAPRETURN|105560|KB금융|positive|TR_KB_S2_20240208|current_profile_correct|
|R6L16_HANA_20240202_CAPRETURN|086790|하나금융지주|positive|TR_HANA_S2_20240202|current_profile_correct|
|R6L16_WOORI_20230208_DIVIDEND_NO_REPRICE|316140|우리금융지주|counterexample|TR_WOORI_S2_20230208|current_profile_too_early|
|R6L16_KAKAOBANK_20210806_DIGITAL_PBR_FALSE_POS|323410|카카오뱅크|counterexample|TR_KAKAO_S2_20210806|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

- positive_structural_success: 2 (`KB금융`, `하나금융지주`)
- counterexample_or_failed_rerating: 2 (`우리금융지주`, `카카오뱅크`)
- 4B_or_4C_case: 2 (`KB금융` overheat watch, `카카오뱅크` valuation blowoff)
- calibration_usable_case_count: 4

The balance is deliberately not “bank stocks went up.” The useful split is:

```text
positive = explicit capital-return execution + ROE/PBR rerating + relative strength
counterexample = dividend-only or digital-bank valuation premium without durable capital-return evidence
```

## 9. Evidence Source Map

| case_id | trigger family | Stage2 evidence | Stage3 evidence | 4B / 4C evidence |
|---|---|---|---|---|
| R6L16_KB_20240208_CAPRETURN | explicit capital-return rerating | annual-result/capital-return disclosure, low-PBR policy optionality, relative strength | revision/visibility confirmation | later valuation/positioning overheat watch |
| R6L16_HANA_20240202_CAPRETURN | explicit capital-return rerating | annual-result/capital-return disclosure, low-PBR policy optionality, relative strength | financial visibility confirmation | none |
| R6L16_WOORI_20230208_DIVIDEND_NO_REPRICE | dividend-only failed rerating | dividend/yield and sector policy context | absent/weak | thesis watch |
| R6L16_KAKAOBANK_20210806_DIGITAL_PBR_FALSE_POS | digital-bank PBR premium | IPO/listing event and initial relative strength | absent as C21 capital-return evidence | valuation blowoff and thesis-break watch |

## 10. Price Data Source Map

| symbol | company | profile_path | entry shard | profile caveat |
|---|---|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | clean profile, no corporate-action candidate dates |
| 086790 | 하나금융지주 | atlas/symbol_profiles/086/086790.json | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | clean profile, no corporate-action candidate dates |
| 316140 | 우리금융지주 | atlas/symbol_profiles/316/316140.json | atlas/ohlcv_tradable_by_symbol_year/316/316140/2023.csv | clean profile; share-count variation noted but not profile-blocked |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv | clean profile, no corporate-action candidate dates |
| 138040 | 메리츠금융지주 | atlas/symbol_profiles/138/138040.json | narrative only | corporate-action candidate dates block default calibration |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TR_KB_S2_20240208|105560|Stage2-Actionable|2024-02-08|67600|16.27|23.37|53.7|-11.69|-11.69|-11.69|2024-10-25|103900|current_profile_correct|True|
|TR_KB_GREEN_20240313|105560|Stage3-Green|2024-03-13|77500|1.42|12.9|34.06|-11.35|-11.35|-11.35|2024-10-25|103900|current_profile_correct|False|
|TR_KB_4B_20241025|105560|Stage4B-Overlay|2024-10-25|101000|2.87|2.87|None|-10.59|-22.48|None|2024-10-25|103900|current_profile_4B_too_late|False|
|TR_HANA_S2_20240202|086790|Stage2-Actionable|2024-02-02|55900|15.56|16.82|23.97|-8.41|-8.41|-8.41|2024-08-27|69300|current_profile_correct|True|
|TR_HANA_GREEN_20240314|086790|Stage3-Green|2024-03-14|64600|0.93|7.28|7.28|-19.2|-19.2|-19.2|2024-08-27|69300|current_profile_too_late|False|
|TR_WOORI_S2_20230208|316140|Stage2-Actionable|2023-02-08|12800|1.17|1.17|1.17|-15.0|-15.0|-15.0|2023-02-13|12950|current_profile_too_early|True|
|TR_KAKAO_S2_20210806|323410|Stage2-Actionable|2021-08-06|69800|35.24|35.24|35.24|-7.59|-24.64|-43.34|2021-08-18|94400|current_profile_false_positive|True|
|TR_KAKAO_4B_20210819|323410|Stage4B-Overlay|2021-08-19|92000|2.17|2.17|2.17|-28.04|-42.83|-57.01|2021-08-20|94000|current_profile_4B_too_late|False|

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate triggers

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| TR_KB_S2_20240208 | 67,600 | 16.27 | -11.69 | 23.37 | -11.69 | 53.70 | -11.69 | Strong C21 positive; drawdown tolerable versus upside. |
| TR_HANA_S2_20240202 | 55,900 | 15.56 | -8.41 | 16.82 | -8.41 | 23.97 | -8.41 | Positive but Green confirmation would have been late. |
| TR_WOORI_S2_20230208 | 12,800 | 1.17 | -15.00 | 1.17 | -15.00 | 1.17 | -15.00 | Dividend/PBR-only false actionable. |
| TR_KAKAO_S2_20210806 | 69,800 | 35.24 | -7.59 | 35.24 | -24.64 | 35.24 | -43.34 | Price spike without C21 evidence; high MAE after blowoff. |

## 13. Current Calibrated Profile Stress Test

| case | current profile verdict | actual alignment | residual lesson |
|---|---|---|---|
| KB금융 | current_profile_correct | strong positive MFE/MAE | current Stage2/Yellow framework works when capital return and ROE/PBR evidence coexist. |
| 하나금융지주 | current_profile_correct | positive but Green late | do not weaken global Green; keep C21 Stage2-Actionable capture. |
| 우리금융지주 | current_profile_too_early | low MFE, high MAE | dividend/yield-only bank rows need a C21 guard. |
| 카카오뱅크 | current_profile_false_positive | initial spike, severe drawdown | digital-bank valuation premium must not masquerade as C21 capital-return rerating. |

Applied-axis status:

```text
stage2_actionable_evidence_bonus: existing_axis_kept, but C21 guard needed
stage3_yellow_total_min: existing_axis_kept
stage3_green_total_min / revision_min: existing_axis_kept
price_only_blowoff_blocks_positive_stage: existing_axis_strengthened for digital-bank premium
full_4b_requires_non_price_evidence: existing_axis_kept
hard_4c_thesis_break_routes_to_4c: existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green comparison | green_lateness_ratio | verdict |
|---|---:|---:|---:|---|
| KB금융 | 67,600 | 77,500 | 0.27 | Green not materially late; confirmation useful. |
| 하나금융지주 | 55,900 | 64,600 | 0.65 | Green would miss much of upside; C21 Stage2-Actionable matters. |
| 우리금융지주 | 12,800 | not applicable | n/a | no confirmed Green; should remain watch/actionable at most. |
| 카카오뱅크 | 69,800 | not applicable | n/a | no C21 Green; price spike is not capital-return evidence. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| TR_KB_4B_20241025 | 0.92 | 0.92 | valuation_blowoff, positioning_overheat | good overlay if non-price overheat is confirmed; not a price-only full 4B. |
| TR_KAKAO_4B_20210819 | 0.90 | 0.90 | valuation_blowoff, positioning_overheat | good 4B guard; the initial spike had no C21 capital-return thesis. |

## 16. 4C Protection Audit

KakaoBank is the clearest 4C watch case. After the 2021-08-18/19 valuation blowoff, the 180D low used here implies an approximate peak-to-trough drawdown of `-58.10%`. The protection label is:

```text
four_c_protection_label = thesis_break_watch_only
```

This is not a hard 4C routing proposal by itself. It strengthens the rule that digital-bank premium without recurring ROE/capital-return evidence should not be promoted as C21 positive evidence.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L6_bank_capital_return_dual_confirmation
candidate = true
```

L6 financial capital-return scoring should require two layers before positive promotion:

1. `ROE/PBR rerating evidence`: relative strength, valuation normalization, and sector rerating context.
2. `capital-return execution evidence`: buyback/cancellation, dividend policy, CET1/capital buffer, or repeated public capital-return commitment.

Dividend yield alone, or policy theme alone, should not get the same Stage2 promotion strength.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
candidate = true
```

Proposed C21 shadow rule:

```text
if financial_name has low-PBR/policy theme but lacks explicit capital-return execution and lacks ROE/PBR revision evidence:
    cap Stage label at Stage2-Watch / Stage2-Actionable low-confidence
if digital-bank or fintech premium is driven mainly by listing/valuation/relative-strength:
    do not map to C21 positive promotion
    route to valuation_blowoff / 4B watch when price dislocation is extreme
if explicit capital return + ROE/PBR rerating + relative strength coexist:
    allow C21 Stage2-Actionable early capture even before strict Stage3-Green confirmation
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|false_positive_rate|score_return_alignment_verdict|
|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current proxy|4|19.15|-14.94|2/4 if dividend-only and digital premium over-promote|mixed; needs C21 guard|
|P0b e2r_2_0_baseline_reference|rollback reference|4|19.15|-14.94|higher expected|weaker|
|P1 sector_specific_candidate_profile|L6 sector|4|19.15|-14.94|1/4 after guard|improved|
|P2 canonical_archetype_candidate_profile|C21|4|19.15|-14.94|1/4 after digital-bank guard|best shadow profile|
|P3 counterexample_guard_profile|C21 guard|2|18.21|-19.82|0/2 promoted after guard|guard effective|

The raw average MFE includes KakaoBank’s initial spike, so the quality lens must include MAE and thesis fit. A price spike with later -40% to -50% drawdown is not the same signal as a bank capital-return rerating.

## 20. Score-Return Alignment Matrix

| case | P0 label | proposed shadow label | MFE90/MAE90 | alignment |
|---|---|---|---|---|
| KB금융 | Stage3-Yellow | Stage3-Green candidate | 23.37 / -11.69 | improved positive alignment |
| 하나금융지주 | Stage3-Yellow | Stage3-Yellow / early Stage2 actionable | 16.82 / -8.41 | keep, but do not force Green |
| 우리금융지주 | Stage2-Actionable | Stage2-Watch | 1.17 / -15.00 | guard improves alignment |
| 카카오뱅크 | Stage3-Yellow risk | Blocked / 4B-Watch | 35.24 / -24.64 | guard improves alignment despite initial MFE |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD|2|2|2|1|4|0|8|4|2|True|True|C21 now has balanced bank-capital-return positive/counterexample coverage; insurance C22 remains separate R6 gap.|

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - dividend_only_false_actionable
  - digital_bank_valuation_blowoff_false_positive
  - green_late_for_bank_capital_return
new_axis_proposed:
  - C21_requires_dual_roe_pbr_and_explicit_capital_return
  - C21_digital_bank_premium_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest and price basis
- symbol profile availability and corporate-action candidate status
- 30D/90D/180D MFE/MAE for representative entry triggers
- positive/counterexample balance
- current calibrated profile stress test
- C21 sector/canonical shadow rule candidate

Not validated:

- no live scan
- no current recommendation
- no production scoring update
- no `stock_agent` source-code access
- no brokerage or trading API use
- no global rule promotion

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_requires_dual_roe_pbr_and_explicit_capital_return,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Dividend/PBR alone produced Woori false actionable; explicit capital-return execution separated KB/Hana positives.","Improves score-return alignment: positives retained, Woori/Kakao downgraded.","TR_KB_S2_20240208|TR_HANA_S2_20240202|TR_WOORI_S2_20230208|TR_KAKAO_S2_20210806",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_digital_bank_premium_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Digital-bank IPO or PBR premium without recurring ROE/capital return is not a C21 positive signal.","KakaoBank shifts from false Yellow to blocked/4B watch.","TR_KAKAO_S2_20210806|TR_KAKAO_4B_20210819",2,1,1,medium,guard_shadow_only,"not production; price-only/digital valuation cannot promote Stage2/3"
shadow_weight,C21_green_confirmation_lateness_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Bank capital-return rerating can be captured at Stage2-Actionable before Green; Green still requires revision confirmation.","Avoids waiting until much of upside is consumed while preserving Green threshold.","TR_KB_GREEN_20240313|TR_HANA_GREEN_20240314",2,2,0,low,archetype_shadow_only,"not production; do not weaken global Green threshold"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L16_KB_20240208_CAPRETURN","symbol":"105560","company_name":"KB금융","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_KB_S2_20240208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"저PBR 은행주 구간에서 자본환원 실행/가시성과 ROE/PBR 재평가가 동시에 붙은 구조적 성공형."}
{"row_type":"case","case_id":"R6L16_HANA_20240202_CAPRETURN","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_HANA_S2_20240202","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_green_late","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"은행업 ROE/PBR 재평가와 배당·자사주 기대가 같이 움직인 positive holdout. Green 확인은 늦었으나 Stage2-Actionable은 유효."}
{"row_type":"case","case_id":"R6L16_WOORI_20230208_DIVIDEND_NO_REPRICE","symbol":"316140","company_name":"우리금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR_WOORI_S2_20230208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_alignment_high_mae","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"배당/저PBR 서사만 있고 ROE/PBR 재평가·상대강도·명시적 자본환원 실행이 약할 때 Stage2 bonus가 과해질 수 있는 반례."}
{"row_type":"case","case_id":"R6L16_KAKAOBANK_20210806_DIGITAL_PBR_FALSE_POS","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR_KAKAO_S2_20210806","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_spike_then_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"디지털 뱅크 성장·상장 프리미엄과 초기 상대강도만으로는 C21 구조적 자본환원 재평가가 아님. 4B/4C guardrail에 더 가까운 케이스."}
{"row_type":"trigger","trigger_id":"TR_KB_S2_20240208","case_id":"R6L16_KB_20240208_CAPRETURN","symbol":"105560","company_name":"KB금융","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","sector":"금융·자본환원·디지털금융","primary_archetype":"ROE/PBR capital-return re-rating versus digital-bank false-positive guard","loop_objective":["sector_specific_rule_discovery","counterexample_mining","current_profile_stress_test","coverage_gap_fill"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-07","evidence_available_at_that_date":"event was available by trigger date; entry uses close or next tradable close per timing rule","evidence_source":"historical public disclosure / company IR event / market listing context; source-bound in MD notes","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":67600,"MFE_30D_pct":16.27,"MFE_90D_pct":23.37,"MFE_180D_pct":53.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.69,"MAE_90D_pct":-11.69,"MAE_180D_pct":-11.69,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-13.09,"green_lateness_ratio":0.27,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_KB_20240208_CAPRETURN_2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_KB_GREEN_20240313","case_id":"R6L16_KB_20240208_CAPRETURN","symbol":"105560","company_name":"KB금융","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","sector":"금융·자본환원·디지털금융","primary_archetype":"ROE/PBR capital-return re-rating versus digital-bank false-positive guard","loop_objective":["sector_specific_rule_discovery","counterexample_mining","current_profile_stress_test","coverage_gap_fill"],"trigger_type":"Stage3-Green","trigger_date":"2024-03-13","evidence_available_at_that_date":"event was available by trigger date; entry uses close or next tradable close per timing rule","evidence_source":"historical public disclosure / company IR event / market listing context; source-bound in MD notes","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-13","entry_price":77500,"MFE_30D_pct":1.42,"MFE_90D_pct":12.9,"MFE_180D_pct":34.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.35,"MAE_90D_pct":-11.35,"MAE_180D_pct":-11.35,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-13.09,"green_lateness_ratio":0.27,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"green_label_comparison_late_but_valid","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_KB_20240208_CAPRETURN_2024-03-13","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR_KB_4B_20241025","case_id":"R6L16_KB_20240208_CAPRETURN","symbol":"105560","company_name":"KB금융","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","sector":"금융·자본환원·디지털금융","primary_archetype":"ROE/PBR capital-return re-rating versus digital-bank false-positive guard","loop_objective":["sector_specific_rule_discovery","counterexample_mining","current_profile_stress_test","coverage_gap_fill"],"trigger_type":"Stage4B-Overlay","trigger_date":"2024-10-25","evidence_available_at_that_date":"event was available by trigger date; entry uses close or next tradable close per timing rule","evidence_source":"historical public disclosure / company IR event / market listing context; source-bound in MD notes","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-25","entry_price":101000,"MFE_30D_pct":2.87,"MFE_90D_pct":2.87,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.59,"MAE_90D_pct":-22.48,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-22.48,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_overheat_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_watch_only","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_KB_20240208_CAPRETURN_2024-10-25","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR_HANA_S2_20240202","case_id":"R6L16_HANA_20240202_CAPRETURN","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","sector":"금융·자본환원·디지털금융","primary_archetype":"ROE/PBR capital-return re-rating versus digital-bank false-positive guard","loop_objective":["sector_specific_rule_discovery","counterexample_mining","current_profile_stress_test","coverage_gap_fill"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","evidence_available_at_that_date":"event was available by trigger date; entry uses close or next tradable close per timing rule","evidence_source":"historical public disclosure / company IR event / market listing context; source-bound in MD notes","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":55900,"MFE_30D_pct":15.56,"MFE_90D_pct":16.82,"MFE_180D_pct":23.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.41,"MAE_90D_pct":-8.41,"MAE_180D_pct":-8.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":69300,"drawdown_after_peak_pct":-17.89,"green_lateness_ratio":0.65,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_HANA_20240202_CAPRETURN_2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_HANA_GREEN_20240314","case_id":"R6L16_HANA_20240202_CAPRETURN","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","sector":"금융·자본환원·디지털금융","primary_archetype":"ROE/PBR capital-return re-rating versus digital-bank false-positive guard","loop_objective":["sector_specific_rule_discovery","counterexample_mining","current_profile_stress_test","coverage_gap_fill"],"trigger_type":"Stage3-Green","trigger_date":"2024-03-14","evidence_available_at_that_date":"event was available by trigger date; entry uses close or next tradable close per timing rule","evidence_source":"historical public disclosure / company IR event / market listing context; source-bound in MD notes","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-14","entry_price":64600,"MFE_30D_pct":0.93,"MFE_90D_pct":7.28,"MFE_180D_pct":7.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.2,"MAE_90D_pct":-19.2,"MAE_180D_pct":-19.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":69300,"drawdown_after_peak_pct":-17.89,"green_lateness_ratio":0.65,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"green_late_upside_missed","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_HANA_20240202_CAPRETURN_2024-03-14","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR_WOORI_S2_20230208","case_id":"R6L16_WOORI_20230208_DIVIDEND_NO_REPRICE","symbol":"316140","company_name":"우리금융지주","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","sector":"금융·자본환원·디지털금융","primary_archetype":"ROE/PBR capital-return re-rating versus digital-bank false-positive guard","loop_objective":["sector_specific_rule_discovery","counterexample_mining","current_profile_stress_test","coverage_gap_fill"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-02-08","evidence_available_at_that_date":"event was available by trigger date; entry uses close or next tradable close per timing rule","evidence_source":"historical public disclosure / company IR event / market listing context; source-bound in MD notes","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/316/316140/2023.csv","profile_path":"atlas/symbol_profiles/316/316140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-08","entry_price":12800,"MFE_30D_pct":1.17,"MFE_90D_pct":1.17,"MFE_180D_pct":1.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.0,"MAE_90D_pct":-15.0,"MAE_180D_pct":-15.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-13","peak_price":12950,"drawdown_after_peak_pct":-15.98,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_WOORI_20230208_DIVIDEND_NO_REPRICE_2023-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_KAKAO_S2_20210806","case_id":"R6L16_KAKAOBANK_20210806_DIGITAL_PBR_FALSE_POS","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","sector":"금융·자본환원·디지털금융","primary_archetype":"ROE/PBR capital-return re-rating versus digital-bank false-positive guard","loop_objective":["sector_specific_rule_discovery","counterexample_mining","current_profile_stress_test","coverage_gap_fill"],"trigger_type":"Stage2-Actionable","trigger_date":"2021-08-06","evidence_available_at_that_date":"event was available by trigger date; entry uses close or next tradable close per timing rule","evidence_source":"historical public disclosure / company IR event / market listing context; source-bound in MD notes","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-06","entry_price":69800,"MFE_30D_pct":35.24,"MFE_90D_pct":35.24,"MFE_180D_pct":35.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.59,"MAE_90D_pct":-24.64,"MAE_180D_pct":-43.34,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-08-18","peak_price":94400,"drawdown_after_peak_pct":-58.1,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_KAKAOBANK_20210806_DIGITAL_PBR_FALSE_POS_2021-08-06","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_KAKAO_4B_20210819","case_id":"R6L16_KAKAOBANK_20210806_DIGITAL_PBR_FALSE_POS","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_ROE_PBR_CAPITAL_RETURN_DIGITAL_FALSE_POSITIVE_GUARD","sector":"금융·자본환원·디지털금융","primary_archetype":"ROE/PBR capital-return re-rating versus digital-bank false-positive guard","loop_objective":["sector_specific_rule_discovery","counterexample_mining","current_profile_stress_test","coverage_gap_fill"],"trigger_type":"Stage4B-Overlay","trigger_date":"2021-08-19","evidence_available_at_that_date":"event was available by trigger date; entry uses close or next tradable close per timing rule","evidence_source":"historical public disclosure / company IR event / market listing context; source-bound in MD notes","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-19","entry_price":92000,"MFE_30D_pct":2.17,"MFE_90D_pct":2.17,"MFE_180D_pct":2.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.04,"MAE_90D_pct":-42.83,"MAE_180D_pct":-57.01,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-08-20","peak_price":94000,"drawdown_after_peak_pct":-57.93,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L16_KAKAOBANK_20210806_DIGITAL_PBR_FALSE_POS_2021-08-19","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L16_KB_20240208_CAPRETURN","trigger_id":"TR_KB_S2_20240208","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":54,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":62,"valuation_repricing_score":68,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":78,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":56,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":66,"valuation_repricing_score":72,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":88,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["roe_pbr_capital_return_score","valuation_repricing_score","positioning_overheat_score","execution_risk_score"],"component_delta_explanation":"capital_return_execution_bonus","MFE_90D_pct":23.37,"MAE_90D_pct":-11.69,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C21_bank_capital_return_shadow_profile","case_id":"R6L16_KB_20240208_CAPRETURN","trigger_id":"TR_KB_S2_20240208","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":54,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":62,"valuation_repricing_score":68,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":78,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":56,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":66,"valuation_repricing_score":72,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":88,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["roe_pbr_capital_return_score","valuation_repricing_score","positioning_overheat_score","execution_risk_score"],"component_delta_explanation":"C21 explicit capital-return execution promotes","MFE_90D_pct":23.37,"MAE_90D_pct":-11.69,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L16_HANA_20240202_CAPRETURN","trigger_id":"TR_HANA_S2_20240202","symbol":"086790","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":50,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":60,"valuation_repricing_score":62,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":72,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":52,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":64,"valuation_repricing_score":66,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":82,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["roe_pbr_capital_return_score","valuation_repricing_score","positioning_overheat_score","execution_risk_score"],"component_delta_explanation":"Stage2 remains valid; Green confirmation late","MFE_90D_pct":16.82,"MAE_90D_pct":-8.41,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C21_bank_capital_return_shadow_profile","case_id":"R6L16_HANA_20240202_CAPRETURN","trigger_id":"TR_HANA_S2_20240202","symbol":"086790","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":50,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":60,"valuation_repricing_score":62,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":72,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":52,"relative_strength_score":68,"customer_quality_score":0,"policy_or_regulatory_score":64,"valuation_repricing_score":66,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":82,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["roe_pbr_capital_return_score","valuation_repricing_score","positioning_overheat_score","execution_risk_score"],"component_delta_explanation":"positive but no forced Green","MFE_90D_pct":16.82,"MAE_90D_pct":-8.41,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L16_WOORI_20230208_DIVIDEND_NO_REPRICE","trigger_id":"TR_WOORI_S2_20230208","symbol":"316140","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":30,"relative_strength_score":42,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":54,"execution_risk_score":-20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":60,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":24,"relative_strength_score":36,"customer_quality_score":0,"policy_or_regulatory_score":52,"valuation_repricing_score":45,"execution_risk_score":-24,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":43,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["roe_pbr_capital_return_score","valuation_repricing_score","positioning_overheat_score","execution_risk_score"],"component_delta_explanation":"dividend-only guard lowers false positive","MFE_90D_pct":1.17,"MAE_90D_pct":-15.0,"score_return_alignment_label":"guard_needed_or_counterexample","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"C21_counterexample_guard_profile","case_id":"R6L16_WOORI_20230208_DIVIDEND_NO_REPRICE","trigger_id":"TR_WOORI_S2_20230208","symbol":"316140","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":30,"relative_strength_score":42,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":54,"execution_risk_score":-20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":60,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":24,"relative_strength_score":36,"customer_quality_score":0,"policy_or_regulatory_score":52,"valuation_repricing_score":45,"execution_risk_score":-24,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":43,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["roe_pbr_capital_return_score","valuation_repricing_score","positioning_overheat_score","execution_risk_score"],"component_delta_explanation":"requires ROE/PBR + capital-return execution","MFE_90D_pct":1.17,"MAE_90D_pct":-15.0,"score_return_alignment_label":"guard_needed_or_counterexample","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L16_KAKAOBANK_20210806_DIGITAL_PBR_FALSE_POS","trigger_id":"TR_KAKAO_S2_20210806","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":78,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":72,"execution_risk_score":-18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":35,"positioning_overheat_score":80,"thesis_break_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":40,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":-30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":15,"positioning_overheat_score":90,"thesis_break_score":-25},"weighted_score_after":55,"stage_label_after":"Blocked/4B-Watch","changed_components":["roe_pbr_capital_return_score","valuation_repricing_score","positioning_overheat_score","execution_risk_score"],"component_delta_explanation":"digital premium is not C21 capital return","MFE_90D_pct":35.24,"MAE_90D_pct":-24.64,"score_return_alignment_label":"guard_needed_or_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C21_counterexample_guard_profile","case_id":"R6L16_KAKAOBANK_20210806_DIGITAL_PBR_FALSE_POS","trigger_id":"TR_KAKAO_S2_20210806","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":78,"customer_quality_score":55,"policy_or_regulatory_score":0,"valuation_repricing_score":72,"execution_risk_score":-18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":35,"positioning_overheat_score":80,"thesis_break_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":40,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":35,"execution_risk_score":-30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":15,"positioning_overheat_score":90,"thesis_break_score":-25},"weighted_score_after":55,"stage_label_after":"Blocked/4B-Watch","changed_components":["roe_pbr_capital_return_score","valuation_repricing_score","positioning_overheat_score","execution_risk_score"],"component_delta_explanation":"valuation blowoff guard strengthened","MFE_90D_pct":35.24,"MAE_90D_pct":-24.64,"score_return_alignment_label":"guard_needed_or_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R6","loop":"16","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","scheduled_round":"R6","scheduled_loop":16,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["dividend_only_false_actionable","digital_bank_valuation_blowoff_false_positive","green_late_for_bank_capital_return"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R6L16_MERITZ_20221121_CAPITAL_RETURN_BLOCKED","symbol":"138040","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"메리츠금융지주 2022~2023 capital-return event is analytically relevant but the stock-web profile has corporate_action_candidate_dates overlapping the 180D window; blocked for weight calibration.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","profile_path":"atlas/symbol_profiles/138/138040.json","calibration_block_reasons":["corporate_action_contaminated_180D_window"]}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_requires_dual_roe_pbr_and_explicit_capital_return,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Dividend/PBR alone produced Woori false actionable; explicit capital-return execution separated KB/Hana positives.","Improves score-return alignment: positives retained, Woori/Kakao downgraded.","TR_KB_S2_20240208|TR_HANA_S2_20240202|TR_WOORI_S2_20230208|TR_KAKAO_S2_20210806",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_digital_bank_premium_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Digital-bank IPO or PBR premium without recurring ROE/capital return is not a C21 positive signal.","KakaoBank shifts from false Yellow to blocked/4B watch.","TR_KAKAO_S2_20210806|TR_KAKAO_4B_20210819",2,1,1,medium,guard_shadow_only,"not production; price-only/digital valuation cannot promote Stage2/3"
shadow_weight,C21_green_confirmation_lateness_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Bank capital-return rerating can be captured at Stage2-Actionable before Green; Green still requires revision confirmation.","Avoids waiting until much of upside is consumed while preserving Green threshold.","TR_KB_GREEN_20240313|TR_HANA_GREEN_20240314",2,2,0,low,archetype_shadow_only,"not production; do not weaken global Green threshold"
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

```text
completed_round = R6
completed_loop = 16
next_round = R7
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `atlas/manifest.json`: manifest max_date `2026-02-20`, price adjustment `raw_unadjusted_marcap`, calibration shard root `atlas/ohlcv_tradable_by_symbol_year`.
- `atlas/symbol_profiles/105/105560.json`: KB금융 profile, no corporate-action candidate dates.
- `atlas/symbol_profiles/086/086790.json`: 하나금융지주 profile, no corporate-action candidate dates.
- `atlas/symbol_profiles/316/316140.json`: 우리금융지주 profile, no corporate-action candidate dates.
- `atlas/symbol_profiles/323/323410.json`: 카카오뱅크 profile, no corporate-action candidate dates.
- `atlas/symbol_profiles/138/138040.json`: 메리츠금융지주 profile has corporate-action candidate dates in the relevant capital-return window, so it is narrative-only here.
- OHLC row paths used: `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`, `086/086790/2024.csv`, `316/316140/2023.csv`, `323/323410/2021.csv`, `323/323410/2022.csv`.


