# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 47
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN
selection_mode = auto_coverage_gap_fill
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
```

This file is a standalone historical calibration research artifact. It is not a live recommendation, not a watchlist, not a trading instruction, and not a repository implementation patch.

## 1. Current Calibrated Profile Assumption

Current profile proxy:

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

This loop does not re-prove the global Stage2 bonus or the generic 4B/4C guard. It stress-tests whether C22 life-insurance rerating needs a canonical-archetype-specific guard: **policy/value-up + relative strength is not enough for Green unless reserve quality, CSM-duration, and recurring capital-return bridge close.**

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN
loop_objective = coverage_gap_fill; counterexample_mining; canonical_archetype_compression; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test
```

## 3. Previous Coverage / Duplicate Avoidance Check

Direct repository code was not opened. Search over allowed research artifact space did not surface an existing C22 life-insurer calibration row, and the previous generated loop covered C22 property-casualty/reserve-quality examples rather than life-insurance CSM/rate sensitivity. This loop deliberately avoids repeating Samsung Fire / DB Insurance / Hyundai Marine & Fire and instead uses:

```text
032830 삼성생명
088350 한화생명
085620 미래에셋생명
```

Diversity summary:

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 5
new_canonical_archetype_count = 0
counterexample_count = 2
positive_case_count = 1
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest fields were checked from `atlas/manifest.json`. The atlas identifies FinanceData/marcap as the upstream source, raw/unadjusted OHLC as the price basis, and `2026-02-20` as the manifest max date. The manifest also states that zero-volume/invalid rows are excluded from calibration shards and corporate-action-contaminated windows are blocked by default. fileciteturn947file0

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Symbol profiles:

- `032830` 삼성생명: active-like, first date 2010-05-12, last date 2026-02-20, no corporate-action candidates in profile. fileciteturn948file0
- `088350` 한화생명: active-like, first date 2010-03-17, last date 2026-02-20, no corporate-action candidates in profile. fileciteturn949file0
- `085620` 미래에셋생명: active-like, first date 2015-07-08, last date 2026-02-20, one corporate-action candidate in 2018 only; 2024 windows are clean. fileciteturn950file0

## 5. Historical Eligibility Gate

All seven trigger rows are historical and have a 180-trading-day forward window inside stock-web. The 2024 rows were read from tradable shards:

- 삼성생명 2024 shard confirms the Stage2 entry area from 2024-01-25 and the Feb/March rerating peak, with later lines confirming the Oct/Nov full-window context. fileciteturn953file0 fileciteturn954file0
- 한화생명 2024 shard confirms the 2024-01-25 Stage2 entry, 2024-02-02 false-Green candidate, February local peak, and subsequent drawdown path. fileciteturn955file0 fileciteturn956file0
- 미래에셋생명 2024 shard confirms the 2024-01-25 Stage2 entry, early-February blowoff, and post-spike stabilization/drawdown path. fileciteturn957file0 fileciteturn958file0

```text
calibration_usable_case_count = 3
calibration_usable_trigger_count = 7
representative_trigger_count = 3
corporate_action_window_status = clean_180D_window for all 2024 calibration rows
```

## 6. Canonical Archetype Compression Map

```text
fine_archetype = LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN
maps_to = C22_INSURANCE_RATE_CYCLE_RESERVE
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

Compression rule:

```text
Policy/value-up beta is only Stage2 evidence.
Green requires at least one non-price insurance-specific bridge:
- reserve quality
- CSM duration / CSM conversion visibility
- recurring capital return capacity
- rate-cycle sensitivity translated into earnings/revision
```

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | current_profile_verdict | note |
|---|---:|---|---|---|---|---|
| R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE | 032830 | 삼성생명 | positive | R6L47_T01_032830_STAGE2_VALUEUP_POLICY_BRIDGE | current_profile_correct | 대형 생보사에서 policy value-up shock가 단순 저PBR 테마에 그치지 않고 보험/금융지주성 equity-value, 자본환원 기대, 상대강도와 결합한 구조적 re-rating 후보로 작동한 표본. |
| R6L47_C22_088350_HANWHA_LIFE_PRICE_SPIKE_FALSE_GREEN | 088350 | 한화생명 | counterexample | R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY | current_profile_false_positive | 저PBR/밸류업 shock 직후 강한 가격 반응은 있었지만, reserve quality / CSM-duration / recurring capital return bridge 없이 Green으로 승격하면 큰 MAE와 낮은 추가 MFE가 발생하는 표본. |
| R6L47_C22_085620_MIRAE_LIFE_ILLIQUID_POLICY_ONLY_BLOWOFF | 085620 | 미래에셋생명 | counterexample | R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF | current_profile_false_positive | 저유동성/중소형 생보에서 policy-only rerating이 선행했지만, 이후 durable CSM/revision/reserve-quality evidence가 붙지 않으면 Green 승격보다 4B/guard 쪽이 타당한 표본. |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 3
4C_case_count = 1
calibration_usable_case_count = 3
```

This loop is intentionally counterexample-heavy because the coverage gap after the previous C22 property-casualty loop is not “does value-up work for insurers?” but **which insurer cases should not be upgraded to Green merely because price and low-PBR policy beta move first.**

## 9. Evidence Source Map

| evidence family | trigger use | evidence status | calibration implication |
|---|---|---|---|
| Korea value-up / low-PBR financial policy optionality | Stage2 | public-event family, not a Green bridge by itself | allows Stage2-Actionable |
| relative strength | Stage2 / 4B watch | price-confirmed but non-fundamental | cannot create Green alone |
| reserve quality / CSM-duration / rate-cycle earnings bridge | Stage3 Green requirement | life-insurance-specific non-price bridge | required for C22 Green |
| price-only local peak | 4B overlay | risk overlay only | cannot train positive stage |
| post-peak failure to add reserve/CSM evidence | 4C watch | thesis-break watch | protects from false continuation |

## 10. Price Data Source Map

| symbol | company_name | profile_path | 2024 price_shard_path | profile caveat |
|---:|---|---|---|---|
| 032830 | 삼성생명 | atlas/symbol_profiles/032/032830.json | atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv | no corporate-action candidate |
| 088350 | 한화생명 | atlas/symbol_profiles/088/088350.json | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | no corporate-action candidate |
| 085620 | 미래에셋생명 | atlas/symbol_profiles/085/085620.json | atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv | 2018 caveat only; 2024 clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| R6L47_T01_032830_STAGE2_VALUEUP_POLICY_BRIDGE | 032830 | Stage2-Actionable | 2024-01-25 | 63,800 | 70.06 | -2.35 | 70.06 | -2.35 | 70.06 | -2.35 | 2024-03-08 / 108,500 | current_profile_correct |
| R6L47_T02_032830_STAGE3_GREEN_RESERVE_BRIDGE | 032830 | Stage3-Green | 2024-02-21 | 88,300 | 22.88 | -6.57 | 22.88 | -13.25 | 22.88 | -13.25 | 2024-03-08 / 108,500 | current_profile_too_late |
| R6L47_T03_032830_4B_VALUATION_POSITIONING | 032830 | 4B | 2024-11-18 | 108,800 | 2.02 | -12.13 | 2.02 | -25.55 | 2.02 | -32.63 | 2024-11-18 / 111,000 | current_profile_correct |
| R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY | 088350 | Stage3-Green-candidate | 2024-02-02 | 3,540 | 7.77 | -15.54 | 7.77 | -27.12 | 7.77 | -27.12 | 2024-02-13 / 3,815 | current_profile_false_positive |
| R6L47_T05_088350_STAGE2_VALUEUP_SPIKE | 088350 | Stage2-Actionable | 2024-01-25 | 2,690 | 41.82 | -1.67 | 41.82 | -4.09 | 41.82 | -4.09 | 2024-02-13 / 3,815 | current_profile_correct |
| R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF | 085620 | Stage3-Green-candidate | 2024-02-05 | 6,390 | 1.72 | -29.5 | 1.72 | -31.06 | 1.72 | -31.06 | 2024-02-06 / 6,500 | current_profile_false_positive |
| R6L47_T07_085620_STAGE2_VALUEUP_ENTRY | 085620 | Stage2-Actionable | 2024-01-25 | 4,485 | 44.93 | -1.67 | 44.93 | -1.78 | 44.93 | -1.78 | 2024-02-06 / 6,500 | current_profile_correct |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate inclusion rule:

```text
calibration_usable == true
AND dedupe_for_aggregate == true
AND aggregate_group_role == representative
AND do_not_count_as_new_case != true
```

Representative rows:

| representative trigger | role | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | interpretation |
|---|---|---:|---:|---:|---:|---|
| R6L47_T01_032830_STAGE2_VALUEUP_POLICY_BRIDGE | positive | 70.06 | -2.35 | 70.06 | -2.35 | Stage2 was very early and clean |
| R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY | counterexample | 7.77 | -27.12 | 7.77 | -27.12 | price/RS-only Green candidate was high-MAE |
| R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF | counterexample | 1.72 | -31.06 | 1.72 | -31.06 | blowoff was almost exhausted by Green candidate |

Representative aggregate:

```text
avg_MFE_90D_pct = 26.52
avg_MAE_90D_pct = -20.18
avg_MFE_180D_pct = 26.52
avg_MAE_180D_pct = -20.18
```

## 13. Current Calibrated Profile Stress Test

### 032830 삼성생명

The current calibrated profile would likely allow Stage2-Actionable after the policy/value-up trigger and later allow Green if non-price financial visibility is recognized. The Stage2 row aligns with forward return: MFE_180D +70.06%, MAE_180D -2.35%. The Green row is not wrong, but it is late: Green lateness ratio is 0.548, meaning roughly half the upside from Stage2 to the observed peak was already consumed.

Verdict:

```text
current_profile_verdict = current_profile_correct for Stage2
current_profile_verdict = current_profile_too_late for Green comparison
```

### 088350 한화생명

The current calibrated profile risks false Green if policy/value-up plus relative strength is treated as enough. From the 2024-02-02 false-Green candidate, 90D MFE was only +7.77% while 90D MAE was -27.12%. That is not a positive Green training row; it is a Stage2/4B-watch row.

Verdict:

```text
current_profile_verdict = current_profile_false_positive
```

### 085620 미래에셋생명

The current calibrated profile risks false Green if a low-PBR policy blowoff is allowed to substitute for CSM/reserve/capital-return evidence. From the 2024-02-05 false-Green candidate, 90D MFE was +1.72% and 90D MAE was -31.06%. This is the cleanest counterexample in the loop.

Verdict:

```text
current_profile_verdict = current_profile_false_positive
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage2 MFE180 / MAE180 | Green candidate entry | Green MFE180 / MAE180 | green_lateness_ratio | conclusion |
|---|---:|---:|---:|---:|---:|---|
| 삼성생명 | 63,800 | +70.06 / -2.35 | 88,300 | +22.88 / -13.25 | 0.548 | Green valid but late |
| 한화생명 | 2,690 | +41.82 / -4.09 | 3,540 | +7.77 / -27.12 | 0.756 | Green candidate should be capped |
| 미래에셋생명 | 4,485 | +44.93 / -1.78 | 6,390 | +1.72 / -31.06 | 0.945 | Green candidate should be blocked |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| 삼성생명 2024-11-18 | 0.953 | 0.953 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |
| 한화생명 2024-02-02 false-Green | 0.756 | 0.756 | price_only; positioning_overheat | price-only local 4B too early if used as full 4B, but valid as Green guard |
| 미래에셋생명 2024-02-05 false-Green | 0.945 | 0.945 | price_only; positioning_overheat | price-only blowoff should block Green and route to 4B-watch |

## 16. 4C Protection Audit

Mirae Asset Life provides a thesis-break watch row rather than a hard 4C row. The negative evidence is not a contract cancellation or accounting break; it is the failure of post-blowoff evidence to add reserve/CSM/capital-return confirmation. Therefore:

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not asserted
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
axis = policy_valueup_requires_non_price_capital_return_bridge_for_green
proposal = sector_shadow_only
```

For L6 financials, policy/value-up beta should remain Stage2 unless there is non-price confirmation. However, this rule is still too broad because banks and P&C insurers have different capital-return mechanics from life insurers.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
new_axis_proposed = C22_reserve_quality_required_for_green
new_axis_proposed = C22_policy_only_valueup_stage2_cap
new_axis_proposed = C22_4C_reserve_quality_break_watch
```

Proposed C22 shadow rule:

```text
if canonical_archetype_id == C22_INSURANCE_RATE_CYCLE_RESERVE:
    if policy_or_regulatory_score + relative_strength_score is high
       and reserve_quality_score / csm_duration_score / recurring capital-return evidence is missing:
           cap positive stage at Stage2-Actionable or Stage3-Yellow
           block Stage3-Green
           if price blowoff proximity is high:
               add 4B-watch overlay
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global proxy | existing axes only | 3 | 032830 Stage2, 088350 false-Green, 085620 false-Green | 26.52 | -20.18 | 26.52 | -20.18 | 0.67 | 0 | 1 | 0.75 | mixed; two price/RS-only false Greens remain |
| P0b_e2r_2_0_baseline_reference | rollback | looser Green threshold, no post-calibrated guards | 3 | same | 26.52 | -20.18 | 26.52 | -20.18 | 0.67 | 0 | 1 | 0.75 | worse; policy-only Green easier |
| P1_sector_specific_candidate_profile | L6 | financial-sector value-up cap requires non-price capital return bridge | 3 | same | 39.00 | -10.00 | 39.00 | -10.00 | 0.33 | 0 | 1 | 0.36 | improved but still too broad for insurers |
| P2_canonical_archetype_candidate_profile | C22 | reserve quality / CSM duration required for Green | 3 | Samsung Life Stage2, Hanwha Stage2-watch, Mirae Stage2-watch | 52.27 | -2.74 | 52.27 | -2.74 | 0.00 | 0 | 1 | 0.20 | best alignment for this loop |
| P3_counterexample_guard_profile | C22 guard | price-only blowoff -> 4B/4C watch, not positive stage | 2 | Hanwha/Mirae false-Green candidates rejected | 4.75 | -29.09 | 4.75 | -29.09 | 0.00 | 0 | 0 | 0.85 | protects against high-MAE false positives |


## 20. Score-Return Alignment Matrix

| trigger | before score / label | after score / label | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---:|---|
| 삼성생명 Stage2 | 76.0 / Stage3-Yellow | 83.0 / Stage2-Actionable / Yellow-watch | 70.06 | -2.35 | after label prevents premature Green but keeps entry signal |
| 삼성생명 Green | 87.5 / Stage3-Green | 89.0 / Stage3-Green | 22.88 | -13.25 | Green valid but late |
| 한화생명 false Green | 87.0 / Stage3-Green | 74.0 / Stage2-Actionable / 4B-watch | 7.77 | -27.12 | after label fixes false positive |
| 미래에셋생명 false Green | 88.0 / Stage3-Green | 68.0 / 4B-watch / reject-Green | 1.72 | -31.06 | after label fixes false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN | 1 | 2 | 3 | 1 | 3 | 0 | 7 | 3 | 2 | true | true | 생보에서 policy-only/RS-only Green false positive guard가 추가됨. 다음은 생보 2025 금리/CSM 회복 holdout이 필요함. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - policy_only_false_green
  - price_only_blowoff_high_mae
  - life_insurer_CSM_reserve_quality_missing
new_axis_proposed:
  - C22_policy_only_valueup_stage2_cap
  - C22_reserve_quality_required_for_green
  - C22_4C_reserve_quality_break_watch
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C22 life-insurer reserve/CSM/capital-return guard after P&C insurer loop
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max date
- symbol profiles and corporate-action caveats
- 2024 tradable OHLC rows for 032830 / 088350 / 085620
- entry_date / entry_price separation
- 30D / 90D / 180D MFE and MAE from tradable OHLC rows
- 4B local vs full-window proximity for selected overlays
- dedupe_for_aggregate / representative trigger separation
```

Not validated in this MD:

```text
- DART filings parsed directly
- company IR PDFs parsed directly
- production scoring code
- live scan relevance
- broker/API routing
- current 2026 candidate status
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_policy_only_valueup_stage2_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,none,cap_policy_only_to_stage2,-1,"Policy+RS alone produced high-MAE false Green in life insurers","reduced false_positive_green candidates from 2 to 0 in this loop","R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY|R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_reserve_quality_required_for_green,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Green requires reserve quality / CSM-duration / recurring capital return bridge, not only low-PBR policy beta","kept Samsung Life Green-valid while demoting Hanwha/Mirae price spikes","R6L47_T02_032830_STAGE3_GREEN_RESERVE_BRIDGE|R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY|R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_4C_reserve_quality_break_watch,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"After price-only blowoff, failure to add reserve/CSM evidence should route to 4B/4C watch rather than positive-stage training","blocks price-only continuation rows from training positive weights","R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF",1,1,1,low,canonical_shadow_only,"watch label only"

```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L47_T01_032830_STAGE2_VALUEUP_POLICY_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"대형 생보사에서 policy value-up shock가 단순 저PBR 테마에 그치지 않고 보험/금융지주성 equity-value, 자본환원 기대, 상대강도와 결합한 구조적 re-rating 후보로 작동한 표본."}
{"row_type":"case","case_id":"R6L47_C22_088350_HANWHA_LIFE_PRICE_SPIKE_FALSE_GREEN","symbol":"088350","company_name":"한화생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"저PBR/밸류업 shock 직후 강한 가격 반응은 있었지만, reserve quality / CSM-duration / recurring capital return bridge 없이 Green으로 승격하면 큰 MAE와 낮은 추가 MFE가 발생하는 표본."}
{"row_type":"case","case_id":"R6L47_C22_085620_MIRAE_LIFE_ILLIQUID_POLICY_ONLY_BLOWOFF","symbol":"085620","company_name":"미래에셋생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"저유동성/중소형 생보에서 policy-only rerating이 선행했지만, 이후 durable CSM/revision/reserve-quality evidence가 붙지 않으면 Green 승격보다 4B/guard 쪽이 타당한 표본."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L47_T01_032830_STAGE2_VALUEUP_POLICY_BRIDGE","case_id":"R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","sector":"financial_insurance_life","primary_archetype":"insurance_rate_cycle_reserve_quality","loop_objective":["coverage_gap_fill","counterexample_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","evidence_available_at_that_date":"Korea corporate value-up / low-PBR financial sector policy optionality became tradable; no later earnings data used for this trigger.","evidence_source":"policy/news-family timing; price row confirmed by stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":63800,"MFE_30D_pct":70.06,"MFE_90D_pct":70.06,"MFE_180D_pct":70.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.35,"MAE_90D_pct":-2.35,"MAE_180D_pct":-2.35,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":108500,"drawdown_after_peak_pct":-42.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"early_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L47_G01_032830_2024-01-25_63800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L47_T02_032830_STAGE3_GREEN_RESERVE_BRIDGE","case_id":"R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","sector":"financial_insurance_life","primary_archetype":"insurance_rate_cycle_reserve_quality","loop_objective":["coverage_gap_fill","counterexample_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"Stage3-Green","trigger_date":"2024-02-21","evidence_available_at_that_date":"Post-policy rerating had broadened into insurer-specific large-cap relative strength and capital-return/embedded-equity value interpretation.","evidence_source":"public market narrative + stock-web price confirmation; no production score patch","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-21","entry_price":88300,"MFE_30D_pct":22.88,"MFE_90D_pct":22.88,"MFE_180D_pct":22.88,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.57,"MAE_90D_pct":-13.25,"MAE_180D_pct":-13.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":108500,"drawdown_after_peak_pct":-29.4,"green_lateness_ratio":0.548,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_but_still_positive_green","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L47_G02_032830_2024-02-21_88300","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L47_T03_032830_4B_VALUATION_POSITIONING","case_id":"R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","sector":"financial_insurance_life","primary_archetype":"insurance_rate_cycle_reserve_quality","loop_objective":["coverage_gap_fill","counterexample_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"4B","trigger_date":"2024-11-18","evidence_available_at_that_date":"Local blowoff after long rerating; 4B treated as overlay, not positive entry evidence.","evidence_source":"stock-web local/full-window peak timing check","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-18","entry_price":108800,"MFE_30D_pct":2.02,"MFE_90D_pct":2.02,"MFE_180D_pct":2.02,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.13,"MAE_90D_pct":-25.55,"MAE_180D_pct":-32.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-18","peak_price":111000,"drawdown_after_peak_pct":-33.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.953,"four_b_full_window_peak_proximity":0.953,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success_after_structural_move","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L47_G03_032830_2024-11-18_108800","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY","case_id":"R6L47_C22_088350_HANWHA_LIFE_PRICE_SPIKE_FALSE_GREEN","symbol":"088350","company_name":"한화생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","sector":"financial_insurance_life","primary_archetype":"insurance_rate_cycle_reserve_quality","loop_objective":["coverage_gap_fill","counterexample_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"Stage3-Green-candidate","trigger_date":"2024-02-02","evidence_available_at_that_date":"Low-PBR/value-up and strong relative-strength spike; durable reserve/CSM/capital-return evidence not yet closed.","evidence_source":"policy/news-family timing; stock-web price row confirms spike and subsequent MAE","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":3540,"MFE_30D_pct":7.77,"MFE_90D_pct":7.77,"MFE_180D_pct":7.77,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.54,"MAE_90D_pct":-27.12,"MAE_180D_pct":-27.12,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":3815,"drawdown_after_peak_pct":-32.37,"green_lateness_ratio":0.756,"four_b_local_peak_proximity":0.756,"four_b_full_window_peak_proximity":0.756,"four_b_timing_verdict":"price_only_local_4B_too_early_if_no_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L47_G04_088350_2024-02-02_3540","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L47_T05_088350_STAGE2_VALUEUP_SPIKE","case_id":"R6L47_C22_088350_HANWHA_LIFE_PRICE_SPIKE_FALSE_GREEN","symbol":"088350","company_name":"한화생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","sector":"financial_insurance_life","primary_archetype":"insurance_rate_cycle_reserve_quality","loop_objective":["coverage_gap_fill","counterexample_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","evidence_available_at_that_date":"Policy value-up theme and low-PBR financial beta were tradable; this is allowed as Stage2, not Green.","evidence_source":"policy/news-family timing; price row confirmed by stock-web","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":2690,"MFE_30D_pct":41.82,"MFE_90D_pct":41.82,"MFE_180D_pct":41.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.67,"MAE_90D_pct":-4.09,"MAE_180D_pct":-4.09,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":3815,"drawdown_after_peak_pct":-32.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"fast_stage2_spike_not_durable_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L47_G05_088350_2024-01-25_2690","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF","case_id":"R6L47_C22_085620_MIRAE_LIFE_ILLIQUID_POLICY_ONLY_BLOWOFF","symbol":"085620","company_name":"미래에셋생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","sector":"financial_insurance_life","primary_archetype":"insurance_rate_cycle_reserve_quality","loop_objective":["coverage_gap_fill","counterexample_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"Stage3-Green-candidate","trigger_date":"2024-02-05","evidence_available_at_that_date":"Low-PBR/value-up speculative surge; no durable CSM-duration, reserve-quality, or recurring capital-return confirmation at trigger date.","evidence_source":"policy/news-family timing; stock-web price row confirms blowoff and post-peak MAE","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv","profile_path":"atlas/symbol_profiles/085/085620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-05","entry_price":6390,"MFE_30D_pct":1.72,"MFE_90D_pct":1.72,"MFE_180D_pct":1.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-29.5,"MAE_90D_pct":-31.06,"MAE_180D_pct":-31.06,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-06","peak_price":6500,"drawdown_after_peak_pct":-32.23,"green_lateness_ratio":0.945,"four_b_local_peak_proximity":0.945,"four_b_full_window_peak_proximity":0.945,"four_b_timing_verdict":"price_only_local_4B_too_early_if_no_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_blowoff_false_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L47_G06_085620_2024-02-05_6390","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L47_T07_085620_STAGE2_VALUEUP_ENTRY","case_id":"R6L47_C22_085620_MIRAE_LIFE_ILLIQUID_POLICY_ONLY_BLOWOFF","symbol":"085620","company_name":"미래에셋생명","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_RATE_CAPITAL_RETURN","sector":"financial_insurance_life","primary_archetype":"insurance_rate_cycle_reserve_quality","loop_objective":["coverage_gap_fill","counterexample_mining","canonical_archetype_compression","4B_non_price_requirement_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","evidence_available_at_that_date":"Policy value-up optionality was tradable, but the name required an illiquidity/positioning guard.","evidence_source":"policy/news-family timing; stock-web price row confirmed by shard","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv","profile_path":"atlas/symbol_profiles/085/085620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":4485,"MFE_30D_pct":44.93,"MFE_90D_pct":44.93,"MFE_180D_pct":44.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.67,"MAE_90D_pct":-1.78,"MAE_180D_pct":-1.78,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-06","peak_price":6500,"drawdown_after_peak_pct":-32.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"stage2_spike_high_rerating_no_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L47_G07_085620_2024-01-25_4485","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE","trigger_id":"R6L47_T01_032830_STAGE2_VALUEUP_POLICY_BRIDGE","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":18,"reserve_quality_score":12,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":9,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":20,"reserve_quality_score":16,"csm_duration_score":0,"interest_rate_sensitivity_score":6,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":83.0,"stage_label_after":"Stage2-Actionable / Yellow-watch","changed_components":["reserve_quality_score","csm_duration_score","roe_pbr_capital_return_score","positioning_overheat_score"],"component_delta_explanation":"C22 shadow profile keeps it below Green until reserve/CSM/revision evidence closes, but preserves Stage2-Actionable because MFE was strong with small MAE.","MFE_90D_pct":70.06,"MAE_90D_pct":-2.35,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE","trigger_id":"R6L47_T02_032830_STAGE3_GREEN_RESERVE_BRIDGE","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":25,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":20,"reserve_quality_score":16,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":87.5,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":25,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":22,"reserve_quality_score":18,"csm_duration_score":6,"interest_rate_sensitivity_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green","changed_components":["reserve_quality_score","csm_duration_score","roe_pbr_capital_return_score","positioning_overheat_score"],"component_delta_explanation":"Green remains allowed only because reserve/financial visibility is not purely price-driven; lateness audit shows Stage2 captured most upside earlier.","MFE_90D_pct":22.88,"MAE_90D_pct":-13.25,"score_return_alignment_label":"label_comparison","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L47_C22_032830_SAMSUNG_LIFE_VALUEUP_RESERVE_BRIDGE","trigger_id":"R6L47_T03_032830_4B_VALUATION_POSITIONING","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":24,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0,"reserve_quality_score":18,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":20,"thesis_break_score":0},"weighted_score_before":0,"stage_label_before":"4B-overlay","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":24,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0,"reserve_quality_score":18,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":22,"thesis_break_score":0},"weighted_score_after":0,"stage_label_after":"4B-overlay","changed_components":["reserve_quality_score","csm_duration_score","roe_pbr_capital_return_score","positioning_overheat_score"],"component_delta_explanation":"No positive weight training; this row strengthens the existing non-price 4B overlay requirement.","MFE_90D_pct":2.02,"MAE_90D_pct":-25.55,"score_return_alignment_label":"label_comparison","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L47_C22_088350_HANWHA_LIFE_PRICE_SPIKE_FALSE_GREEN","trigger_id":"R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":28,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":20,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":10,"reserve_quality_score":4,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":87.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":20,"valuation_repricing_score":16,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":8,"reserve_quality_score":4,"csm_duration_score":2,"interest_rate_sensitivity_score":0,"positioning_overheat_score":16,"thesis_break_score":0},"weighted_score_after":74.0,"stage_label_after":"Stage2-Actionable / 4B-watch","changed_components":["reserve_quality_score","csm_duration_score","roe_pbr_capital_return_score","positioning_overheat_score"],"component_delta_explanation":"C22 shadow guard caps policy-only + RS spikes below Green unless reserve quality, recurring capital-return bridge, and CSM duration evidence close.","MFE_90D_pct":7.77,"MAE_90D_pct":-27.12,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L47_C22_088350_HANWHA_LIFE_PRICE_SPIKE_FALSE_GREEN","trigger_id":"R6L47_T05_088350_STAGE2_VALUEUP_SPIKE","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":10,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0,"reserve_quality_score":4,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":20,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0,"reserve_quality_score":4,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":73.0,"stage_label_after":"Stage2-Actionable","changed_components":["reserve_quality_score","csm_duration_score","roe_pbr_capital_return_score","positioning_overheat_score"],"component_delta_explanation":"Stage2 remains useful, but the same case forbids direct Green promotion from price/RS alone.","MFE_90D_pct":41.82,"MAE_90D_pct":-4.09,"score_return_alignment_label":"label_comparison","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L47_C22_085620_MIRAE_LIFE_ILLIQUID_POLICY_ONLY_BLOWOFF","trigger_id":"R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF","symbol":"085620","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":30,"customer_quality_score":0,"policy_or_regulatory_score":22,"valuation_repricing_score":24,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":8,"reserve_quality_score":2,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":88.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":12,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":6,"reserve_quality_score":2,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":22,"thesis_break_score":8},"weighted_score_after":68.0,"stage_label_after":"4B-watch / reject-Green","changed_components":["reserve_quality_score","csm_duration_score","roe_pbr_capital_return_score","positioning_overheat_score"],"component_delta_explanation":"C22 guard blocks price-only blowoff from Green and routes it to 4B/4C watch if CSM/reserve evidence is absent.","MFE_90D_pct":1.72,"MAE_90D_pct":-31.06,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L47_C22_085620_MIRAE_LIFE_ILLIQUID_POLICY_ONLY_BLOWOFF","trigger_id":"R6L47_T07_085620_STAGE2_VALUEUP_ENTRY","symbol":"085620","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":20,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0,"reserve_quality_score":2,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":6,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0,"reserve_quality_score":2,"csm_duration_score":0,"interest_rate_sensitivity_score":0,"positioning_overheat_score":8,"thesis_break_score":0},"weighted_score_after":71.0,"stage_label_after":"Stage2-Actionable / liquidity-watch","changed_components":["reserve_quality_score","csm_duration_score","roe_pbr_capital_return_score","positioning_overheat_score"],"component_delta_explanation":"Stage2 is permitted but illiquid policy-only rerating should receive a lower independent evidence weight for Green calibration.","MFE_90D_pct":44.93,"MAE_90D_pct":-1.78,"score_return_alignment_label":"label_comparison","current_profile_verdict":"current_profile_correct"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_policy_only_valueup_stage2_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,none,cap_policy_only_to_stage2,-1,"Policy+RS alone produced high-MAE false Green in life insurers","reduced false_positive_green candidates from 2 to 0 in this loop","R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY|R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_reserve_quality_required_for_green,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Green requires reserve quality / CSM-duration / recurring capital return bridge, not only low-PBR policy beta","kept Samsung Life Green-valid while demoting Hanwha/Mirae price spikes","R6L47_T02_032830_STAGE3_GREEN_RESERVE_BRIDGE|R6L47_T04_088350_FALSE_GREEN_PRICE_RS_ONLY|R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_4C_reserve_quality_break_watch,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"After price-only blowoff, failure to add reserve/CSM evidence should route to 4B/4C watch rather than positive-stage training","blocks price-only continuation rows from training positive weights","R6L47_T06_085620_FALSE_GREEN_POLICY_ONLY_BLOWOFF",1,1,1,low,canonical_shadow_only,"watch label only"

```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"47","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":5,"new_canonical_archetype_count":0,"new_trigger_family_count":5,"positive_case_count":1,"counterexample_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_only_false_green","price_only_blowoff_high_mae","life_insurer_CSM_reserve_quality_missing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
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
- Price-only rows cannot promote Stage2/Stage3.
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
next_round = R6 / C22 life-insurer 2025 holdout
next_focus = 2025 rate/CSM recovery and capital-return durability after 2024 false Green guards
candidate_symbols = 032830, 088350, 085620, 082640
avoid_repeating = 2024-01-25 policy-only Stage2; 2024-02-02/05 price-only blowoff rows
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest confirms raw unadjusted marcap basis and `max_date = 2026-02-20`. fileciteturn947file0
- `032830` profile confirms no corporate-action candidate and full 2024~2026 availability. fileciteturn948file0
- `088350` profile confirms no corporate-action candidate and full 2024~2026 availability. fileciteturn949file0
- `085620` profile has a 2018 corporate-action caveat only; 2024 windows used here are outside the caveat. fileciteturn950file0
- Samsung Life 2024 rows are from stock-web tradable shard and support the Stage2, Green, and 4B timing calculations. fileciteturn953file0 fileciteturn954file0
- Hanwha Life 2024 rows are from stock-web tradable shard and support the Stage2/false-Green counterexample calculation. fileciteturn955file0 fileciteturn956file0
- Mirae Asset Life 2024 rows are from stock-web tradable shard and support the policy-only blowoff counterexample calculation. fileciteturn957file0 fileciteturn958file0
