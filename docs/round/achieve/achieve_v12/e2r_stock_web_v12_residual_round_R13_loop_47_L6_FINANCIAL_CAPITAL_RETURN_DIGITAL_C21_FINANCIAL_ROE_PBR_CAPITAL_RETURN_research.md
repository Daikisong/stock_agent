# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 47
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = K_BANK_VALUEUP_CET1_CAPITAL_RETURN, FINANCIAL_HOLDING_ROE_PBR_REPRICING, STATE_OR_PLATFORM_BANK_CAPITAL_RETURN_GUARD, NONBANK_EXPANSION_CET1_OVERHANG_4B4C
selection_mode = auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

이번 loop는 `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` 안에서 신규 symbol과 신규 trigger family를 채우는 잔여 연구다. 같은 canonical archetype을 반복하는 것이 아니라, 은행/금융지주 안에서 **자본환원 bridge가 닫힌 경우**와 **저PBR narrative만 있고 CET1·ROE·자사주/배당 경로가 닫히지 않은 경우**의 가격 차이를 분리했다.

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

핵심 stress test는 단순한 저PBR·정책 beta가 Stage2/3까지 올라가도 되는지가 아니라, **ROE/PBR gap → CET1 여력 → 반복 자본환원 → 실제 180D MFE/MAE**가 하나의 다리처럼 연결되는지다. 다리가 한 칸이라도 비면 가격은 한동안 들릴 수 있어도, 하중을 받으면 내려앉았다.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop_objective = auto_coverage_gap_fill, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, residual_false_positive_mining, 4B_non_price_requirement_stress_test, yellow_threshold_stress_test
rule_scope_preference = sector_specific or canonical_archetype_specific
```

C21은 금융주의 “저평가”를 그대로 매수 신호로 보는 archetype이 아니다. 은행·금융지주에서 중요한 것은 장부가치 자체가 아니라, 그 장부가치를 주주에게 돌려줄 수 있는 **자본 여력과 의지**다. 금고가 크다고 모두 현금흐름이 되는 것은 아니다. 금고의 문이 열리는 구조, 즉 CET1 buffer와 배당/자사주 정책이 확인되어야 한다.

## 3. Previous Coverage / Duplicate Avoidance Check

stock_agent research artifact 검색은 다음 키워드 기준으로 수행했다.

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
105560
086790
316140
323410
```

직접 매칭되는 기존 연구 산출물이 검색되지 않았다. 따라서 이번 loop는 다음 coverage gap을 자동 선택했다.

```text
auto_selected_coverage_gap = L6/C21 undercovered vs R1/R2-style industrial/semiconductor/power-grid loops; especially counterexample and 4B/4C paths.
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

|row_type|source|path|validation|
|---|---|---|---|
|price_source_validation|manifest/schema|atlas/manifest.json; atlas/schema.json|manifest max_date=2026-02-20; raw_unadjusted_marcap; tradable_raw|
|KB금융|profile/OHLC|atlas/symbol_profiles/105/105560.json; atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv|clean profile; 0 corporate-action candidates; 2024-02-08 close 67,600; 2024-10-25 high 103,900|
|하나금융지주|profile/OHLC|atlas/symbol_profiles/086/086790.json; atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv|clean profile; 0 corporate-action candidates; 2024-02-08 close 56,600; 2024-08-27 high 69,300|
|우리금융지주|profile/OHLC|atlas/symbol_profiles/316/316140.json; atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv; 2025.csv|clean profile; 0 corporate-action candidates; 2024-07-29 close 16,330|
|카카오뱅크|profile/OHLC|atlas/symbol_profiles/323/323410.json; atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv|clean profile; 0 corporate-action candidates; 2024-02-08 close 29,100; 2024-08-05 low 18,490|
|policy context|external evidence|Reuters / Financial Times public coverage|Corporate Value-up was proposed in Feb 2024 and emphasised shareholder return, capital efficiency and voluntary plans.|

`stock-web` manifest 기준 max_date는 2026-02-20이다. 이번 연구는 2024년 및 2025년 1D tradable shard만 사용했으며, manifest 이후 가격을 만들지 않았다.

## 5. Historical Eligibility Gate

모든 representative trigger는 다음 조건을 만족한다.

```text
entry row exists in tradable shard = true
minimum forward 180 trading days = true
raw OHLC adjusted = false
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Profile 기준 corporate-action candidate는 KB금융, 하나금융지주, 우리금융지주, 카카오뱅크 모두 2024~2025 calibration window에 없다. 기업은행은 보조 후보로 검토했지만 이번 MD의 representative set에서는 제외했다.

## 6. Canonical Archetype Compression Map

```text
K_BANK_VALUEUP_CET1_CAPITAL_RETURN
  -> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

FINANCIAL_HOLDING_ROE_PBR_REPRICING
  -> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

NONBANK_EXPANSION_CET1_OVERHANG_4B4C
  -> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN as counterexample / guard

STATE_OR_PLATFORM_BANK_CAPITAL_RETURN_GUARD
  -> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN as false-positive guard
```

압축 규칙은 명확하다. 저PBR 금융주라는 이름은 같은 간판이지만, 내부 엔진은 다르다. KB금융·하나금융은 자본환원 bridge가 닫혔고, 우리금융은 비은행 확장과 CET1 부담이 bridge를 흔들었다. 카카오뱅크는 은행주라는 간판은 있으나 저PBR/자본환원 archetype이 아니라 성장은행/고PBR에 가깝다.

## 7. Case Selection Summary

|case_id|symbol|company|case_type|role|entry_date|MFE_180D|MAE_180D|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|
|C21_KBFG_2024_CAPITAL_RETURN_POS|105560|KB금융|structural_success|positive|2024-02-08|53.7|-11.69|current_profile_correct|
|C21_HANA_2024_CAPITAL_RETURN_POS|086790|하나금융지주|structural_success|positive|2024-02-08|22.44|-8.83|current_profile_correct|
|C21_WOORI_2024_NONBANK_OVERHANG_CE|316140|우리금융지주|failed_rerating|counterexample|2024-07-29|7.16|-15.86|current_profile_false_positive|
|C21_KAKAOBANK_2024_PBR_FALSE_POS|323410|카카오뱅크|false_positive_green|counterexample|2024-02-08|7.22|-36.46|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 2
minimum_positive_case_count = passed
minimum_counterexample_count = passed
minimum_calibration_usable_case_count = passed
```

이번 loop의 균형은 좋다. positive 두 개는 같은 policy context 안에서도 non-price capital-return bridge가 닫힌 경우이고, counterexample 두 개는 policy beta 또는 금융주 narrative가 있으나 bridge가 닫히지 않은 경우다.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| KB금융 | policy/value-up + shareholder return + bank ROE/CET1 visibility | Q1/forward financial visibility | valuation/positioning heat near full-window peak | watch only |
| 하나금융지주 | policy/value-up + shareholder return + bank ROE/CET1 visibility | profit/capital-return confirmation | valuation/positioning heat near local/full-window peak | watch only |
| 우리금융지주 | low-PBR financial holding narrative + nonbank expansion | insufficient | CET1/M&A overhang | thesis watch / no Stage3 promotion |
| 카카오뱅크 | bank/platform narrative + policy beta | insufficient | high-PBR / no capital-return route | false positive / thesis-break guard |

## 10. Price Data Source Map

| symbol | profile_path | 2024 shard | 2025 shard used | profile caveat |
|---|---|---|---|---|
| 105560 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | not primary | clean |
| 086790 | atlas/symbol_profiles/086/086790.json | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | not primary | clean |
| 316140 | atlas/symbol_profiles/316/316140.json | atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv | atlas/ohlcv_tradable_by_symbol_year/316/316140/2025.csv | clean |
| 323410 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | not primary | clean |

## 11. Case-by-Case Trigger Grid

|trigger_id|company|type|trigger_date|entry_date|entry|MFE90|MAE90|MFE180|MAE180|current_profile|outcome|aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|T_C21_KB_20240208_STAGE2A|KB금융|Stage2-Actionable|2024-02-07|2024-02-08|67600|23.37|-11.69|53.7|-11.69|current_profile_correct|structural_success|True|
|T_C21_KB_20240426_STAGE3G|KB금융|Stage3-Green|2024-04-25|2024-04-26|76000|21.58|-5.39|36.71|-5.39|current_profile_correct|green_not_too_late|False|
|T_C21_KB_20241025_4B|KB금융|4B|2024-10-25|2024-10-25|101000|2.87|-19.21|None|None|current_profile_correct|4B_overlay_success|False|
|T_C21_HANA_20240208_STAGE2A|하나금융지주|Stage2-Actionable|2024-02-07|2024-02-08|56600|15.37|-8.83|22.44|-8.83|current_profile_correct|structural_success|True|
|T_C21_HANA_20240426_STAGE3G|하나금융지주|Stage3-Green|2024-04-25|2024-04-26|60000|13.0|-5.33|15.5|-6.83|current_profile_correct|green_not_too_late|False|
|T_C21_HANA_20240827_4B|하나금융지주|4B|2024-08-27|2024-08-27|66000|5.0|-14.55|None|None|current_profile_correct|4B_overlay_success|False|
|T_C21_WOORI_20240729_STAGE2A|우리금융지주|Stage2-Actionable|2024-07-26|2024-07-29|16330|5.94|-15.86|7.16|-15.86|current_profile_false_positive|failed_rerating_high_mae|True|
|T_C21_KAKAOBANK_20240208_STAGE2A|카카오뱅크|Stage2-Actionable|2024-02-07|2024-02-08|29100|7.22|-28.52|7.22|-36.46|current_profile_false_positive|false_positive_green|True|

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger returns

|company|entry_date|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|
|---|---|---|---|---|---|---|---|---|---|---|
|KB금융|2024-02-08|67600|16.27|-11.69|23.37|-11.69|53.7|-11.69|2024-10-25|103900|
|하나금융지주|2024-02-08|56600|14.84|-6.71|15.37|-8.83|22.44|-8.83|2024-08-27|69300|
|우리금융지주|2024-07-29|16330|3.86|-15.86|5.94|-15.86|7.16|-15.86|2025-02-19|17500|
|카카오뱅크|2024-02-08|29100|7.22|-6.19|7.22|-28.52|7.22|-36.46|2024-02-15|31200|

### 12.2 Interpretation

KB금융과 하나금융지주는 Stage2 entry 이후 180D MFE가 각각 +53.70%, +22.44%였다. 둘 다 initial policy beta 이후에도 ROE/PBR gap과 자본환원 bridge가 실제 가격을 지탱했다.

우리금융지주는 2024-07-29 entry 후 180D MFE가 +7.16%에 그쳤고, MAE는 -15.86%였다. 카카오뱅크는 entry 후 180D MFE가 +7.22%인데 MAE는 -36.46%였다. 둘은 “금융주/정책”이라는 표면 evidence만으로 C21 positive gate를 열면 안 된다는 잔여 오류다.

## 13. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| current calibrated profile이 어떻게 판단했을 것인가? | KB/Hana는 Stage2-Actionable 또는 Yellow로 적절히 진입, Woori/KakaoBank는 policy/PBR narrative 때문에 과승격 위험 |
| 실제 MFE/MAE와 맞았는가? | KB/Hana는 맞음. Woori/KakaoBank는 90D/180D MAE가 커서 과승격 방지 필요 |
| Stage2 bonus가 과했는가? | C21에서 capital-return bridge가 없으면 과함 |
| Yellow threshold 75가 과했는가? | Woori/KakaoBank에는 낮음; KB/Hana에는 적절 |
| Green threshold 87/revision 55가 과했는가? | KB/Hana는 지나치게 늦지 않음. Woori/KakaoBank는 Green 금지 |
| price-only blowoff guard가 적절했는가? | 적절. 특히 KakaoBank의 early local rally를 positive evidence로 쓰면 안 됨 |
| full 4B non-price requirement가 적절했는가? | 적절. KB/Hana 4B는 valuation/positioning overlay로 기록해야 함 |
| hard 4C routing이 늦거나 과했는가? | KakaoBank는 hard 4C thesis-break guard가 유효. Woori는 watch-only/overhang guard가 우선 |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3-Green entry | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| KB금융 | 67,600 | 76,000 | 103,900 | 0.23 | Green not too late |
| 하나금융지주 | 56,600 | 60,000 | 69,300 | 0.27 | Green not too late |
| 우리금융지주 | 16,330 | no valid Green | 17,500 | n/a | Green blocked by overhang |
| 카카오뱅크 | 29,100 | no valid Green | 31,200 | n/a | Green blocked by no capital-return bridge |

## 15. 4B Local vs Full-window Timing Audit

| trigger | Stage2 entry | 4B entry | local peak | full-window peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| T_C21_KB_20241025_4B | 67,600 | 101,000 | 103,900 | 103,900 | 0.92 | 0.92 | good_full_window_4B_timing |
| T_C21_HANA_20240827_4B | 56,600 | 66,000 | 69,300 | 69,300 | 0.74 | 0.74 | good_full_window_4B_timing |

4B는 매도 신호가 아니라 overlay다. KB/Hana 모두 Stage3 thesis가 살아 있었지만 가격이 capital-return bridge보다 앞서 달린 시점이 있었다. 이 시점에는 positive promotion이 아니라 risk overlay로 다뤄야 한다.

## 16. 4C Protection Audit

| case | 4C label | reason |
|---|---|---|
| KB금융 | thesis_break_watch_only | 4B 이후 drawdown은 있었지만 capital-return thesis 자체 파괴는 아님 |
| 하나금융지주 | thesis_break_watch_only | rerating fatigue, thesis intact |
| 우리금융지주 | thesis_break_watch_only | M&A/CET1 overhang; hard 4C보다는 promotion guard |
| 카카오뱅크 | hard_4c_success | no low-PBR capital-return bridge + -36.46% 180D MAE; positive thesis should be broken early |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = C21_CET1_MA_overhang_guard
proposal = If a financial holding company’s rerating thesis depends on shareholder return but evidence shows nonbank acquisition, insurance M&A, capital consumption, or CET1 uncertainty, cap Stage at Stage2-Watch until CET1/shareholder-return path is explicitly re-confirmed.
expected_effect = reduce Woori-like false positives
confidence = low_to_medium
production_change = false
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = C21_CET1_ROE_capital_return_bridge_bonus
axis_2 = C21_no_lowPBR_capital_return_guard

positive gate:
  Require at least two of:
  - low or discounted PBR relative to ROE
  - CET1 or capital surplus visibility
  - explicit dividend/buyback/cancellation route
  - repeatable bank/holding ROE visibility
  - nonbank execution risk low

counterexample guard:
  If high-PBR platform bank or policy beta has no capital-return bridge, block Stage3-Green and cap to Stage2-Watch.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|changed_axes|thresholds|eligible|selected|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|late_green|avg_green_lateness|avg_4B_local|avg_4B_full|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|default current proxy|none|default thresholds|4|KB/Hana/Woori/KakaoBank|12.97|-16.23|22.63|-18.21|50.0%|2|0|0.25|0.83|0.83|mixed: positives work, but Woori/KakaoBank overpromotion remains|
|P0b|e2r_2_0_baseline_reference|rollback comparison|lower old gates / no stock-web calibration|old thresholds|4|same|12.97|-16.23|22.63|-18.21|50.0%|2|1|0.55|0.83|0.83|worse: false positives and late/unclean green promotion|
|P1|sector_specific_candidate_profile|L6 bank/financial holding CET1 guard|add CET1/ROE/capital-return bridge and M&A overhang guard|shadow only|4|same|12.97|-16.23|22.63|-18.21|25.0%|1|0|0.25|0.83|0.83|better: promotes KB/Hana and demotes Woori overhang|
|P2|canonical_archetype_candidate_profile|C21 low-PBR rerating requires capital-return bridge|capital-return bridge bonus; no-return/high-PBR guard|shadow only|4|same|12.97|-16.23|22.63|-18.21|0.0%|0|0|0.25|0.83|0.83|best conceptual alignment for C21|
|P3|counterexample_guard_profile|false positive minimizer|high-PBR/no capital return cap; M&A CET1 drag cap|shadow only|4|same|12.97|-16.23|22.63|-18.21|0.0%|0|0|0.25|0.83|0.83|good guard, but may be conservative for early positives|

## 20. Score-Return Alignment Matrix

| case | before label | after label | return alignment |
|---|---|---|---|
| KB금융 | Stage3-Yellow | Stage3-Yellow | correct positive |
| 하나금융지주 | Stage3-Yellow | Stage3-Yellow | correct positive |
| 우리금융지주 | Stage3-Yellow | Stage2-Watch | false positive reduced |
| 카카오뱅크 | Stage3-Yellow | Stage2-Watch | false positive reduced |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|multi|2|2|2|2|4|0|8|4|2|True|True|positive/counterexample balance improved; still needs insurance-rate-cycle separation under C22|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - capital_return_bridge_false_positive
  - nonbank_MA_CET1_overhang
  - highPBR_no_return_false_positive
new_axis_proposed:
  - C21_CET1_ROE_capital_return_bridge_bonus
  - C21_no_lowPBR_capital_return_guard
  - C21_CET1_MA_overhang_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
diversity_score_summary: avg≈19; same canonical archetype but 4 new symbols, 4 new trigger families, 2 positive and 2 counterexamples.
auto_selected_coverage_gap: L6/C21 undercovered vs R1/R2-style industrial/semiconductor/power-grid loops; especially counterexample and 4B/4C paths.
```

## 23. Validation Scope / Non-Validation Scope

### Validated

```text
- stock-web manifest/schema fields
- symbol profiles
- actual tradable OHLC rows
- entry_date and entry_price
- MFE/MAE 30D/90D/180D for representative triggers
- same_entry_group_id dedupe
- current profile stress-test labels
- shadow-only score simulation
```

### Not validated

```text
- live stock recommendation
- current 2026 Stage3 candidate scan
- broker API or execution route
- production scoring code
- exact production score internals
- intraday disclosure timestamps beyond next-trading-day rule
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
"shadow_weight","C21_CET1_ROE_capital_return_bridge_bonus","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","Positive cases had non-price capital-return bridge and clean 180D MFE/MAE.","KB/Hana promoted without excessive green lateness.","T_C21_KB_20240208_STAGE2A|T_C21_HANA_20240208_STAGE2A","4","4","2","medium","archetype_shadow_only","not production; post-calibrated residual"
"shadow_weight","C21_no_lowPBR_capital_return_guard","canonical_archetype_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","High-PBR or no shareholder-return route did not align with 90D/180D returns.","KakaoBank false positive reduced.","T_C21_KAKAOBANK_20240208_STAGE2A","4","4","2","medium","archetype_shadow_only","guard for platform/growth banks"
"shadow_weight","C21_CET1_MA_overhang_guard","sector_specific","L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","0","1","+1","Nonbank expansion / acquisition overhang reduced capital-return visibility.","Woori false positive reduced; avoid Stage3 promotion before CET1 closure.","T_C21_WOORI_20240729_STAGE2A","4","4","2","low_to_medium","sector_shadow_only","not global"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C21_KBFG_2024_CAPITAL_RETURN_POS", "symbol": "105560", "company_name": "KB금융", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_C21_KB_20240208_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "good: Stage2 entry retained 180D upside and 4B overlay arrived near full-window peak.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "저PBR 정책 수혜만이 아니라 은행계 금융지주의 CET1/ROE/자사주·배당 경로가 함께 닫힌 positive 표본.", "same_archetype_new_symbol": true, "same_archetype_new_trigger_family": true}
{"row_type": "case", "case_id": "C21_HANA_2024_CAPITAL_RETURN_POS", "symbol": "086790", "company_name": "하나금융지주", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_C21_HANA_20240208_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "good: positive MFE with manageable 180D MAE, but 4B local/full-window split needed.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "저PBR/배당/자사주 기대가 ROE·CET1 가시성과 결합될 때 Stage2-Actionable이 유효했던 positive 표본.", "same_archetype_new_symbol": true, "same_archetype_new_trigger_family": true}
{"row_type": "case", "case_id": "C21_WOORI_2024_NONBANK_OVERHANG_CE", "symbol": "316140", "company_name": "우리금융지주", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "NONBANK_EXPANSION_CET1_OVERHANG_4B4C", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T_C21_WOORI_20240729_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "bad: valuation/PBR theme alone overpromotes; capital-return visibility should be capped by CET1/M&A overhang.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "저PBR 금융지주라는 표면 evidence가 있어도 비은행 확장·보험 인수·CET1 부담이 자본환원 가시성을 잠식하면 MFE가 낮고 MAE가 커지는 반례.", "same_archetype_new_symbol": true, "same_archetype_new_trigger_family": true}
{"row_type": "case", "case_id": "C21_KAKAOBANK_2024_PBR_FALSE_POS", "symbol": "323410", "company_name": "카카오뱅크", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "STATE_OR_PLATFORM_BANK_CAPITAL_RETURN_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T_C21_KAKAOBANK_20240208_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "bad: price/local policy beta did not translate into 90D/180D return alignment.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "금융주/은행주 랠리와 성장은행 narrative가 있었지만 낮은 PBR·반복 자본환원·CET1 surplus 축이 약한 counterexample.", "same_archetype_new_symbol": true, "same_archetype_new_trigger_family": true}
{"trigger_id": "T_C21_KB_20240208_STAGE2A", "case_id": "C21_KBFG_2024_CAPITAL_RETURN_POS", "symbol": "105560", "company_name": "KB금융", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "entry_date": "2024-02-08", "entry_price": 67600, "evidence_available_at_that_date": "FY2023/early-2024 shareholder-return route, low-PBR policy beta, bank ROE/CET1 visibility; next tradable close used.", "evidence_source": "company IR/earnings release context; Korea Corporate Value-up policy context; stock-web OHLC shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 16.27, "MFE_90D_pct": 23.37, "MFE_180D_pct": 53.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.69, "MAE_90D_pct": -11.69, "MAE_180D_pct": -11.69, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_C21_KB_20240208", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN", "sector": "Financials / Korean banks and financial holdings", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": ["auto_coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "residual_false_positive_mining", "4B_non_price_requirement_stress_test", "yellow_threshold_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": []}
{"trigger_id": "T_C21_KB_20240426_STAGE3G", "case_id": "C21_KBFG_2024_CAPITAL_RETURN_POS", "symbol": "105560", "company_name": "KB금융", "trigger_type": "Stage3-Green", "trigger_date": "2024-04-25", "entry_date": "2024-04-26", "entry_price": 76000, "evidence_available_at_that_date": "Q1/forward capital-return confirmation; stronger financial visibility after initial Stage2.", "evidence_source": "company IR/earnings release context; stock-web OHLC shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 9.74, "MFE_90D_pct": 21.58, "MFE_180D_pct": 36.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.39, "MAE_90D_pct": -5.39, "MAE_180D_pct": -5.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": 0.23, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "green_not_too_late", "current_profile_verdict": "current_profile_correct", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_C21_KB_20240426", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN", "sector": "Financials / Korean banks and financial holdings", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": ["auto_coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "residual_false_positive_mining", "4B_non_price_requirement_stress_test", "yellow_threshold_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": []}
{"trigger_id": "T_C21_KB_20241025_4B", "case_id": "C21_KBFG_2024_CAPITAL_RETURN_POS", "symbol": "105560", "company_name": "KB금융", "trigger_type": "4B", "trigger_date": "2024-10-25", "entry_date": "2024-10-25", "entry_price": 101000, "evidence_available_at_that_date": "valuation/positioning heat after long rerating leg; 4B overlay, not positive-stage promotion.", "evidence_source": "stock-web OHLC peak behavior plus valuation/positioning overlay context.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "MFE_30D_pct": 2.87, "MFE_90D_pct": 2.87, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.21, "MAE_90D_pct": -19.21, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "forward_window_trading_days": 90, "corporate_action_window_status": "clean_90D_window", "same_entry_group_id": "SEG_C21_KB_20241025", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN", "sector": "Financials / Korean banks and financial holdings", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": ["auto_coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "residual_false_positive_mining", "4B_non_price_requirement_stress_test", "yellow_threshold_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": []}
{"trigger_id": "T_C21_HANA_20240208_STAGE2A", "case_id": "C21_HANA_2024_CAPITAL_RETURN_POS", "symbol": "086790", "company_name": "하나금융지주", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "entry_date": "2024-02-08", "entry_price": 56600, "evidence_available_at_that_date": "low-PBR/value-up policy beta with bank ROE and shareholder-return visibility.", "evidence_source": "company IR/earnings release context; Korea Corporate Value-up policy context; stock-web OHLC shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 14.84, "MFE_90D_pct": 15.37, "MFE_180D_pct": 22.44, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.71, "MAE_90D_pct": -8.83, "MAE_180D_pct": -8.83, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -18.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_C21_HANA_20240208", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN", "sector": "Financials / Korean banks and financial holdings", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": ["auto_coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "residual_false_positive_mining", "4B_non_price_requirement_stress_test", "yellow_threshold_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": []}
{"trigger_id": "T_C21_HANA_20240426_STAGE3G", "case_id": "C21_HANA_2024_CAPITAL_RETURN_POS", "symbol": "086790", "company_name": "하나금융지주", "trigger_type": "Stage3-Green", "trigger_date": "2024-04-25", "entry_date": "2024-04-26", "entry_price": 60000, "evidence_available_at_that_date": "post-initial confirmation of profit/capital-return route.", "evidence_source": "company IR/earnings release context; stock-web OHLC shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 8.83, "MFE_90D_pct": 13.0, "MFE_180D_pct": 15.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.33, "MAE_90D_pct": -5.33, "MAE_180D_pct": -6.83, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -18.61, "green_lateness_ratio": 0.27, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "green_not_too_late", "current_profile_verdict": "current_profile_correct", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_C21_HANA_20240426", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN", "sector": "Financials / Korean banks and financial holdings", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": ["auto_coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "residual_false_positive_mining", "4B_non_price_requirement_stress_test", "yellow_threshold_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": []}
{"trigger_id": "T_C21_HANA_20240827_4B", "case_id": "C21_HANA_2024_CAPITAL_RETURN_POS", "symbol": "086790", "company_name": "하나금융지주", "trigger_type": "4B", "trigger_date": "2024-08-27", "entry_date": "2024-08-27", "entry_price": 66000, "evidence_available_at_that_date": "rerating leg had reached local/full-window peak zone; valuation/positioning overlay.", "evidence_source": "stock-web OHLC peak behavior plus valuation/positioning overlay context.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "MFE_30D_pct": 5.0, "MFE_90D_pct": 5.0, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.79, "MAE_90D_pct": -14.55, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -18.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.74, "four_b_full_window_peak_proximity": 0.74, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "forward_window_trading_days": 90, "corporate_action_window_status": "clean_90D_window", "same_entry_group_id": "SEG_C21_HANA_20240827", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_BANK_VALUEUP_CET1_CAPITAL_RETURN", "sector": "Financials / Korean banks and financial holdings", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": ["auto_coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "residual_false_positive_mining", "4B_non_price_requirement_stress_test", "yellow_threshold_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": []}
{"trigger_id": "T_C21_WOORI_20240729_STAGE2A", "case_id": "C21_WOORI_2024_NONBANK_OVERHANG_CE", "symbol": "316140", "company_name": "우리금융지주", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-26", "entry_date": "2024-07-29", "entry_price": 16330, "evidence_available_at_that_date": "nonbank expansion / insurance acquisition route and low-PBR financial holding narrative; CET1 and capital-return visibility not yet closed.", "evidence_source": "company/press context; stock-web OHLC shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital_raise_or_overhang", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "MFE_30D_pct": 3.86, "MFE_90D_pct": 5.94, "MFE_180D_pct": 7.16, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.86, "MAE_90D_pct": -15.86, "MAE_180D_pct": -15.86, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-19", "peak_price": 17500, "drawdown_after_peak_pct": -14.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "overhang_blocked_positive_promotion", "four_b_evidence_type": ["capital_raise_or_overhang", "execution_risk_score"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_high_mae", "current_profile_verdict": "current_profile_false_positive", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_C21_WOORI_20240729", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "NONBANK_EXPANSION_CET1_OVERHANG_4B4C", "sector": "Financials / Korean banks and financial holdings", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": ["auto_coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "residual_false_positive_mining", "4B_non_price_requirement_stress_test", "yellow_threshold_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv", "profile_path": "atlas/symbol_profiles/316/316140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": []}
{"trigger_id": "T_C21_KAKAOBANK_20240208_STAGE2A", "case_id": "C21_KAKAOBANK_2024_PBR_FALSE_POS", "symbol": "323410", "company_name": "카카오뱅크", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "entry_date": "2024-02-08", "entry_price": 29100, "evidence_available_at_that_date": "financial/online-bank narrative and policy beta, but no low-PBR capital-return bridge and no surplus capital return route.", "evidence_source": "public market/policy context; stock-web OHLC shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "MFE_30D_pct": 7.22, "MFE_90D_pct": 7.22, "MFE_180D_pct": 7.22, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.19, "MAE_90D_pct": -28.52, "MAE_180D_pct": -36.46, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 31200, "drawdown_after_peak_pct": -40.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "valuation_without_capital_return_guard_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_C21_KAKAOBANK_20240208", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "STATE_OR_PLATFORM_BANK_CAPITAL_RETURN_GUARD", "sector": "Financials / Korean banks and financial holdings", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": ["auto_coverage_gap_fill", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "residual_false_positive_mining", "4B_non_price_requirement_stress_test", "yellow_threshold_stress_test"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "calibration_block_reasons": []}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_KBFG_2024_CAPITAL_RETURN_POS", "trigger_id": "T_C21_KB_20240208_STAGE2A", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 48, "relative_strength_score": 62, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 75, "valuation_repricing_score": 68, "execution_risk_score": 18, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 5}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 50, "relative_strength_score": 62, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 75, "valuation_repricing_score": 70, "execution_risk_score": 15, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 5}, "weighted_score_after": 85, "stage_label_after": "Stage3-Yellow", "changed_components": ["C21_CET1_ROE_capital_return_bridge_bonus"], "component_delta_explanation": "shadow-only research proxy: reward CET1/ROE/shareholder-return bridge; penalize nonbank M&A capital drag and high-PBR/no-return platform bank narratives.", "MFE_90D_pct": 23.37, "MAE_90D_pct": -11.69, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_HANA_2024_CAPITAL_RETURN_POS", "trigger_id": "T_C21_HANA_20240208_STAGE2A", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 44, "relative_strength_score": 58, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 74, "valuation_repricing_score": 65, "execution_risk_score": 20, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 46, "relative_strength_score": 58, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 74, "valuation_repricing_score": 67, "execution_risk_score": 18, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 81, "stage_label_after": "Stage3-Yellow", "changed_components": ["C21_CET1_ROE_capital_return_bridge_bonus"], "component_delta_explanation": "shadow-only research proxy: reward CET1/ROE/shareholder-return bridge; penalize nonbank M&A capital drag and high-PBR/no-return platform bank narratives.", "MFE_90D_pct": 15.37, "MAE_90D_pct": -8.83, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_WOORI_2024_NONBANK_OVERHANG_CE", "trigger_id": "T_C21_WOORI_20240729_STAGE2A", "symbol": "316140", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 33, "relative_strength_score": 55, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 65, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 15, "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 30, "relative_strength_score": 40, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 55, "valuation_repricing_score": 52, "execution_risk_score": 75, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 22, "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 68, "stage_label_after": "Stage2-Watch", "changed_components": ["C21_CET1_MA_overhang_guard"], "component_delta_explanation": "shadow-only research proxy: reward CET1/ROE/shareholder-return bridge; penalize nonbank M&A capital drag and high-PBR/no-return platform bank narratives.", "MFE_90D_pct": 5.94, "MAE_90D_pct": -15.86, "score_return_alignment_label": "counterexample_guard_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21_KAKAOBANK_2024_PBR_FALSE_POS", "trigger_id": "T_C21_KAKAOBANK_20240208_STAGE2A", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 35, "relative_strength_score": 50, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 58, "valuation_repricing_score": 45, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 5}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 32, "relative_strength_score": 35, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 45, "valuation_repricing_score": 20, "execution_risk_score": 65, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 5}, "weighted_score_after": 61, "stage_label_after": "Stage2-Watch", "changed_components": ["C21_no_lowPBR_capital_return_guard"], "component_delta_explanation": "shadow-only research proxy: reward CET1/ROE/shareholder-return bridge; penalize nonbank M&A capital drag and high-PBR/no-return platform bank narratives.", "MFE_90D_pct": 7.22, "MAE_90D_pct": -28.52, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R13", "loop": "47", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["capital_return_bridge_false_positive", "nonbank_MA_CET1_overhang", "highPBR_no_return_false_positive"], "new_axis_proposed": ["C21_CET1_ROE_capital_return_bridge_bonus", "C21_no_lowPBR_capital_return_guard", "C21_CET1_MA_overhang_guard"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "avg≈19; same canonical archetype but 4 new symbols, 4 new trigger families, 2 positive and 2 counterexamples.", "auto_selected_coverage_gap": "L6/C21 undercovered vs R1/R2-style industrial/semiconductor/power-grid loops; especially counterexample and 4B/4C paths."}
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
next_round = R13_loop_48
suggested_large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
suggested_canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
reason = C21 now has balanced positive/counterexample/4B coverage; next uncovered residual area should test approval-to-commercialization vs event-risk confusion.
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`.
- Stock-Web schema: `atlas/schema.json`.
- Stock-Web profiles:
  - `atlas/symbol_profiles/105/105560.json`
  - `atlas/symbol_profiles/086/086790.json`
  - `atlas/symbol_profiles/316/316140.json`
  - `atlas/symbol_profiles/323/323410.json`
- Stock-Web OHLC shards:
  - `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/316/316140/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv`
- External policy context used only for evidence dating/narrative framing:
  - Reuters, 2024-04-02: Korea Corporate Value-up incentives and quarterly dividend amendment discussion.
  - Reuters, 2024-05-02: voluntary guidelines, shareholder return and corporate value-up programme.
  - Financial Times, 2024-02-26 / 2024-09-15: Korea value-up / Korea discount context.
- This MD is not an investment recommendation and does not modify production scoring.
