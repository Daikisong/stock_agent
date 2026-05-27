# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 45
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN
output_file = e2r_stock_web_v12_residual_round_R6_loop_45_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a current stock recommendation, not a live watchlist, and not a production patch.

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

This loop does not re-prove the already-applied global Stage2 bonus or global Green/4B rules. It looks for a C21-specific residual: **financial-sector policy value-up exposure works only when the low-PBR/ROE thesis is tied to explicit shareholder-return capacity**. A sector label alone is not enough.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN
loop_objective = coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test
```

C21 compresses multiple financial rerating paths into one scoring surface:

```text
1. low-PBR / capital efficiency policy optionality
2. ROE stability or improvement
3. shareholder-return bridge: dividend, buyback, cancellation, CET1 room, payout visibility
4. valuation rerating without treating policy headlines as standalone Stage3 evidence
5. 4B distinction between local blowoff and full-window thesis exhaustion
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were used only for duplicate/coverage checks. The registry head showed many R10/R11/R12/R13 loops and repeated hashes in those sectors, while targeted repository search for `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN KB금융 하나금융 카카오뱅크` returned no direct prior C21 hit in the available index. Therefore this loop is treated as a new coverage-gap fill rather than schema rematerialization.

```text
auto_selected_coverage_gap =
  L6/C21 had no visible direct coverage in accessible registry/search snippets;
  financial value-up policy created both positive bank-holding-company reratings
  and a digital-bank false-positive risk that current global rules do not fully distinguish.
```

Novelty gate:

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
minimum_new_independent_case_ratio = 1.00
minimum_counterexample_count = 1
minimum_positive_case_count = 2
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

The price atlas manifest states:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Source validation row:

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All representative triggers satisfy:

```text
trigger_date is historical
entry_date exists in stock-web tradable shard
entry_date + 180 trading days is available before manifest max_date 2026-02-20
high / low / close / volume fields are present
30D / 90D / 180D MFE and MAE were calculated from actual stock-web rows
corporate_action_candidate_dates do not overlap representative 180D windows
```

Symbol profile checks:

| symbol | company | profile_path | profile last_date | corporate_action_candidate_count | corporate_action_window_status |
|---|---|---|---|---:|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | 2026-02-20 | 0 | clean_180D_window |
| 086790 | 하나금융지주 | atlas/symbol_profiles/086/086790.json | 2026-02-20 | 0 | clean_180D_window |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | 2026-02-20 | 0 | clean_180D_window |

## 6. Canonical Archetype Compression Map

```text
BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN
  -> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

DIGITAL_BANK_POLICY_EXPOSURE_WITHOUT_CAPITAL_RETURN_BRIDGE
  -> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN as counterexample guard

PRICE_ONLY_LOCAL_VALUEUP_BLOWOFF
  -> C21 4B overlay only, not full 4B unless non-price deterioration exists
```

Mechanism:

A financial holding company rerates when the market can connect the policy catalyst to a capital-return machine. The policy is the match, but the fuel is still ROE, capital ratio, payout capacity, and cancellation/dividend visibility. KakaoBank shows the opposite: the same sector headline without the low-PBR/capital-return bridge becomes a bright sign over an empty road.

## 7. Case Selection Summary

| company | symbol | role | best trigger | entry_date | MFE_180D | MAE_180D | current verdict | why selected |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KB금융 | 105560 | positive | Stage2-Actionable | 2024-02-27 | +66.51% | -2.40% | current_profile_correct | explicit low-PBR/capital-return bridge |
| 하나금융지주 | 086790 | positive | Stage2-Actionable | 2024-02-27 | +26.69% | -5.67% | current_profile_too_late | Stage3 Green lateness |
| 카카오뱅크 | 323410 | counterexample | Stage2 rejected | 2024-02-27 | +3.72% | -37.43% | current_profile_false_positive | policy exposure without capital-return bridge |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
```

The positive set is not “banks went up.” It is narrower: **traditional financial holding companies with low-PBR/value-up capital-return optionality rerated with acceptable MAE**. The counterexample is not “financials failed.” It is narrower too: **a financial/digital-bank symbol exposed to the same policy story but lacking the same PBR/capital-return bridge showed poor score-return alignment.**

## 9. Evidence Source Map

| evidence family | source type | timing rule | cases |
|---|---|---|---|
| Corporate Value-up Programme launch | public policy event / press reporting | 2024-02-26 announcement, next trading close for entry | KB금융, 하나금융지주, 카카오뱅크 |
| Low-PBR / shareholder-return bridge | company/sector financial visibility, not price-only | must be visible by trigger date or near-term confirmed | KB금융, 하나금융지주 |
| Digital-bank policy exposure without traditional capital-return bridge | counterexample guard | sector headline is insufficient | 카카오뱅크 |
| Local price blowoff after rerating | 4B overlay only | not full 4B without non-price thesis deterioration | KB금융 2024-10-25 |

External context used: Reuters/FSC reporting on the Corporate Value-up Programme and follow-up discussion; stock-web OHLC is the quantitative source of record.

## 10. Price Data Source Map

| symbol | tradable shard used | 2025 continuation shard | profile |
|---|---|---|---|
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv | atlas/symbol_profiles/105/105560.json |
| 086790 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/ohlcv_tradable_by_symbol_year/086/086790/2025.csv | atlas/symbol_profiles/086/086790.json |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/ohlcv_tradable_by_symbol_year/323/323410/2025.csv | atlas/symbol_profiles/323/323410.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict | dedupe | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L45_T01_KBFG_VALUEUP_STAGE2 | 105560 | KB금융 | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 62400 | 25.96 | 44.23 | 66.51 | -2.4 | -2.4 | -2.4 | 2024-10-25 | 103900 | current_profile_correct | True | structural_success |
| R6L45_T02_KBFG_LOCAL_4B_STRESS | 105560 | KB금융 | Stage4B-Overlay | 2024-10-25 | 2024-10-25 | 101000 | 2.87 | 2.87 | 20.79 | -15.94 | -24.36 | -31.19 | 2025-07-25 | 126600 | current_profile_4B_too_early | False | 4B_too_early |
| R6L45_T03_HANA_VALUEUP_STAGE2 | 086790 | 하나금융지주 | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 54700 | 19.2 | 23.95 | 26.69 | -3.47 | -5.67 | -5.67 | 2024-08-27 | 69300 | current_profile_too_late | True | structural_success_green_late |
| R6L45_T04_HANA_CONFIRMED_GREEN | 086790 | 하나금융지주 | Stage3-Green | 2024-07-03 | 2024-07-03 | 64600 | 7.28 | 7.28 | 7.28 | -13.47 | -13.47 | -13.47 | 2024-08-27 | 69300 | current_profile_too_late | False | late_green_low_incremental_reward |
| R6L45_T05_KAKAOBANK_VALUEUP_FALSE_STAGE2 | 323410 | 카카오뱅크 | Stage2-Actionable-Rejected | 2024-02-26 | 2024-02-27 | 29550 | 3.72 | 3.72 | 3.72 | -16.07 | -32.15 | -37.43 | 2024-02-27 | 30650 | current_profile_false_positive | True | failed_rerating_counterexample |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger metrics

| case | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 1Y MFE/MAE | interpretation |
|---|---:|---:|---:|---:|---:|---|
| KB금융 Stage2 | 62,400 | +25.96 / -2.40 | +44.23 / -2.40 | +66.51 / -2.40 | +66.51 / -2.40 | clean structural positive |
| 하나금융 Stage2 | 54,700 | +19.20 / -3.47 | +23.95 / -5.67 | +26.69 / -5.67 | +26.69 / -5.67 | positive but Green lateness risk |
| 카카오뱅크 false Stage2 | 29,550 | +3.72 / -16.07 | +3.72 / -32.15 | +3.72 / -37.43 | +3.72 / -37.43 | counterexample; policy-only exposure failed |

### 4B stress trigger

| case | 4B entry | local peak proximity | full-window peak proximity | verdict |
|---|---:|---:|---:|---|
| KB금융 2024-10-25 local blowoff | 101,000 | 0.93 | 0.60 | price_only_local_4B_too_early |

The 2024 local top behaved like a 4B watch, but not like a full-cycle 4B. The later 2025 full-window high means the system should keep price-only overheat as an overlay unless non-price deterioration appears.

## 13. Current Calibrated Profile Stress Test

| question | KB금융 | 하나금융지주 | 카카오뱅크 |
|---|---|---|---|
| current profile likely label | Stage2/Yellow, near Green | Stage2/Yellow, Green later | Watch or false Stage2 if sector bonus overfires |
| matched actual MFE/MAE? | yes | partially; Stage2 yes, Green late | no |
| Stage2 bonus too high/low? | appropriate | appropriate | too high if policy-only |
| Yellow 75 too high/low? | appropriate | appropriate | should not clear without bridge |
| Green 87/revision 55? | kept | Green can be late | should block |
| price-only blowoff guard? | strengthened | kept | kept |
| full 4B non-price requirement? | strengthened | kept | kept |
| hard 4C routing? | not needed | not needed | useful as rejected Stage2 / thesis-broken watch |
| final verdict | current_profile_correct | current_profile_too_late | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

```text
KB:
Stage2 entry = 62,400
Stage3-Green proxy = 76,000
full observed peak used for Stage2 window = 103,900
green_lateness_ratio = (76,000 - 62,400) / (103,900 - 62,400) = 0.33
verdict = Green somewhat late but acceptable

Hana:
Stage2 entry = 54,700
Stage3-Green proxy = 64,600
full observed peak used for Stage2 window = 69,300
green_lateness_ratio = (64,600 - 54,700) / (69,300 - 54,700) = 0.68
verdict = Green missed most of the move

KakaoBank:
No confirmed Stage3-Green trigger. Sector headline did not become C21 capital-return rerating.
```

C21-specific reading: Stage2-Actionable should remain valuable in financial value-up cases, but Green must not be granted merely because the policy headline exists. Green is not a louder version of the headline; it is the point where the capital-return bridge has closed.

## 15. 4B Local vs Full-window Timing Audit

```text
KB금융 local 4B candidate:
Stage2_Actionable_entry_price = 62,400
Stage4B_entry_price = 101,000
local_peak_price_after_Stage2 = 103,900
full_window_peak_price_after_Stage2 = 126,600

four_b_local_peak_proximity =
(101,000 - 62,400) / (103,900 - 62,400) = 0.93

four_b_full_window_peak_proximity =
(101,000 - 62,400) / (126,600 - 62,400) = 0.60

four_b_timing_verdict = price_only_local_4B_too_early
```

Rule implication: In C21, local overheat after value-up rerating should be treated like a yellow traffic light, not a stop sign. Full 4B needs non-price fatigue: slowing ROE, payout disappointment, CET1 constraint, regulatory cap, credit cost shock, or explicit deterioration in the shareholder-return path.

## 16. 4C Protection Audit

KakaoBank acts as a soft 4C / thesis-break watch case. The failure was not a sudden hard rejection event; it was the absence of the C21 bridge. The model should route it as `Rejected-Stage2` or `thesis_break_watch_only`, not as a positive Stage2. Its 180D path from the value-up entry had MFE +3.72% and MAE -37.43%, so early rejection would have protected the calibration set from a bad positive row.

```text
four_c_protection_label = hard_4c_success for rejected false Stage2
reason = sector policy exposure did not close into capital-return/valuation-repricing evidence
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
candidate_axis = financial_valueup_policy_needs_capital_return_bridge
```

Candidate:

```text
If sector = L6 and trigger_family = value-up / low-PBR policy:
    Stage2-Actionable bonus may apply only when at least two of the following are visible:
        1. low PBR / capital efficiency rerating basis
        2. explicit shareholder-return route: dividend, buyback, cancellation, payout policy
        3. stable or improving ROE / financial visibility
        4. relative strength versus financial peers
    If only public policy headline is present:
        cap at Watch / Stage2-Rejected
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

Candidate C21 rule:

```text
C21_positive_promotion =
    policy_or_regulatory_score
  + valuation_repricing_score
  + roe_pbr_capital_return_score
  + financial_visibility_score

C21_rejection_guard =
    if policy_or_regulatory_score exists
    but roe_pbr_capital_return_score is missing
    and valuation_repricing_score is unsupported:
        reject positive Stage2/3 promotion
```

This is not a global rule. It is a financial-capital-return archetype rule. In other sectors, policy optionality may map through order backlog, capacity, subsidy, or customer quality; here it must map through capital return and ROE/PBR mechanics.

## 19. Before / After Backtest Comparison

| profile | profile_id | scope | hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_4B_local_prox | avg_4B_full_prox | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | global calibrated | 현행 적용 profile | 3 | KB/Hana Stage2, Kakao Watch | 23.97 | -13.41 | 32.31 | -15.17 | 33% | 0 | 1 | 0.50 | 0.93 | 0.60 | mixed: positive OK, Kakao false-positive risk |
| P0b | e2r_2_0_baseline_reference | rollback reference | old lower evidence gate | 3 | broader Stage2/Green | 23.97 | -13.41 | 32.31 | -15.17 | 33%+ | 0 | 2 | 0.50 | 0.93 | 0.60 | worse false-positive control |
| P1 | sector_specific_candidate_profile | L6 sector shadow | financial value-up requires capital-return bridge | 3 | KB/Hana Stage2, Kakao rejected | 34.09 | -4.04 | 46.60 | -4.04 | 0% | 0 | 1 | 0.50 | 0.93 | 0.60 | better risk-adjusted alignment |
| P2 | canonical_archetype_candidate_profile | C21 archetype shadow | low-PBR + ROE + explicit shareholder return | 3 | KB/Hana selected | 34.09 | -4.04 | 46.60 | -4.04 | 0% | 0 | 1 | 0.50 | 0.93 | 0.60 | best explanatory compression |
| P3 | counterexample_guard_profile | C21 guard | reject digital-bank value-up narrative without repricing bridge | 3 | Kakao rejected; KB/Hana retained | 34.09 | -4.04 | 46.60 | -4.04 | 0% | 0 | 1 | 0.50 | 0.93 | 0.60 | best false-positive suppression |

## 20. Score-Return Alignment Matrix

| case | score behavior | MFE_90D | MAE_90D | MFE_180D | MAE_180D | alignment |
| --- | --- | --- | --- | --- | --- | --- |
| KB금융 | Stage2 score high / Green near | +44.23% | -2.40% | +66.51% | -2.40% | aligned_positive |
| 하나금융지주 | Stage2 good / Green late | +23.95% | -5.67% | +26.69% | -5.67% | aligned_stage2_but_green_late |
| 카카오뱅크 | policy-only false positive risk | +3.72% | -32.15% | +3.72% | -37.43% | reject_without_capital_return_bridge |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN | 2 | 1 | 1 | 1 | 3 | 0 | 5 | 3 | 2 | True | True | positive/counterexample filled; needs insurers and securities holdout |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence

residual_error_types_found:
  - sector_policy_false_positive_without_capital_return_bridge
  - green_late_for_financial_valueup
  - price_only_local_4B_too_early

new_axis_proposed:
  - C21_explicit_capital_return_bridge
  - C21_no_green_without_revision_or_capital_return
  - C21_price_only_local_4B_guard

existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage

existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
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
- stock-web manifest max_date
- symbol profile availability and corporate-action candidate counts
- actual tradable OHLC rows for each entry window
- 30D/90D/180D representative MFE/MAE
- positive/counterexample balance
- C21-specific residual logic
- same_entry_group dedupe flags
```

Not validated:

```text
- live 2026 candidate scan
- production scoring implementation
- any brokerage execution
- exact company fundamental model
- revised-price adjustment
- whether the source company policies remain current after manifest max_date
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_explicit_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Policy value-up exposure only works when paired with low-PBR/ROE and explicit shareholder-return bridge.","KB/Hana positive while KakaoBank false-positive is rejected.","R6L45_T01_KBFG_VALUEUP_STAGE2|R6L45_T03_HANA_VALUEUP_STAGE2|R6L45_T05_KAKAOBANK_VALUEUP_FALSE_STAGE2",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_no_green_without_revision_or_capital_return,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Green needs capital return + financial visibility/revision; sector policy alone remains Yellow/Watch.","Prevents KakaoBank-style false Stage2/Green and explains Hana Green lateness.","R6L45_T03_HANA_VALUEUP_STAGE2|R6L45_T04_HANA_CONFIRMED_GREEN|R6L45_T05_KAKAOBANK_VALUEUP_FALSE_STAGE2",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_price_only_local_4B_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Local blowoff after value-up rerating should not become full 4B unless full-window non-price deterioration is present.","KB 2024-10 local peak was followed by higher 2025 full-window high.","R6L45_T02_KBFG_LOCAL_4B_STRESS",1,1,0,low,canonical_shadow_only,"4B overlay only; not entry promotion"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L45_C21_KBFG_20240227_STAGE2", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "45", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L45_T01_KBFG_VALUEUP_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Value-up 정책 충격과 금융지주 자본환원 기대가 결합된 대표 positive. Stage2에서 충분히 포착 가능했고 Green은 늦지 않았으나, 2024-10 local 4B는 full-window 기준으로 너무 이른 오탐 성격을 보였다."}
{"row_type": "case", "case_id": "R6L45_C21_HANA_20240227_STAGE2", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "45", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L45_T03_HANA_VALUEUP_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "stage2_positive_green_late", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "저 PBR·고배당·자본환원 기대는 Stage2 성공으로 분류되지만, Stage3 Green 확인은 이미 upside 상당 부분을 사용한 뒤라 green_lateness가 커진 표본."}
{"row_type": "case", "case_id": "R6L45_C21_KAKAOBANK_20240227_FALSE_STAGE2", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "45", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R6L45_T05_KAKAOBANK_VALUEUP_FALSE_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "negative_alignment_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "같은 금융 섹터 value-up 담론에 노출되었지만 PBR/ROE 자본환원형 재평가 조건이 닫히지 않아 Stage2 보너스가 과하면 false positive가 되는 반례."}
{"row_type": "trigger", "round": "R6", "loop": "45", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본환원·디지털금융", "primary_archetype": "ROE/PBR capital return rerating", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_2Y_pct": null, "MAE_2Y_pct": null, "calibration_block_reasons": [], "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R6L45_T01_KBFG_VALUEUP_STAGE2", "case_id": "R6L45_C21_KBFG_20240227_STAGE2", "symbol": "105560", "company_name": "KB금융", "loop_objective": "coverage_gap_fill; sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 62400, "evidence_available_at_that_date": "Corporate Value-up Programme launch shock plus bank-sector low-PBR / shareholder-return repricing setup; entry uses next trading close after policy announcement.", "evidence_source": "Reuters/FSC policy reporting; stock-web OHLC shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "MFE_30D_pct": 25.96, "MFE_90D_pct": 44.23, "MFE_180D_pct": 66.51, "MFE_1Y_pct": 66.51, "MAE_30D_pct": -2.4, "MAE_90D_pct": -2.4, "MAE_180D_pct": -2.4, "MAE_1Y_pct": -2.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -15.5, "green_lateness_ratio": 0.33, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R6L45_G01_KBFG_20240227_62400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "round": "R6", "loop": "45", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본환원·디지털금융", "primary_archetype": "ROE/PBR capital return rerating", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_2Y_pct": null, "MAE_2Y_pct": null, "calibration_block_reasons": [], "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "trigger_id": "R6L45_T02_KBFG_LOCAL_4B_STRESS", "case_id": "R6L45_C21_KBFG_20240227_STAGE2", "symbol": "105560", "company_name": "KB금융", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-10-25", "entry_date": "2024-10-25", "entry_price": 101000, "evidence_available_at_that_date": "Local blowoff after capital-return/value-up repricing; later full-window peak exceeded the 2024 local peak, so price-only local 4B was too early.", "evidence_source": "stock-web OHLC shard; policy/valuation context.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "MFE_30D_pct": 2.87, "MFE_90D_pct": 2.87, "MFE_180D_pct": 20.79, "MFE_1Y_pct": 25.35, "MAE_30D_pct": -15.94, "MAE_90D_pct": -24.36, "MAE_180D_pct": -31.19, "MAE_1Y_pct": -31.19, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-07-25", "peak_price": 126600, "drawdown_after_peak_pct": -16.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.6, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "same_entry_group_id": "R6L45_G01_KBFG_20240227_62400", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only"}
{"row_type": "trigger", "round": "R6", "loop": "45", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본환원·디지털금융", "primary_archetype": "ROE/PBR capital return rerating", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_2Y_pct": null, "MAE_2Y_pct": null, "calibration_block_reasons": [], "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R6L45_T03_HANA_VALUEUP_STAGE2", "case_id": "R6L45_C21_HANA_20240227_STAGE2", "symbol": "086790", "company_name": "하나금융지주", "loop_objective": "coverage_gap_fill; yellow_threshold_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 54700, "evidence_available_at_that_date": "Corporate Value-up Programme launch shock plus traditional financial holding company low-PBR / shareholder-return repricing setup.", "evidence_source": "Reuters/FSC policy reporting; stock-web OHLC shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "MFE_30D_pct": 19.2, "MFE_90D_pct": 23.95, "MFE_180D_pct": 26.69, "MFE_1Y_pct": 26.69, "MAE_30D_pct": -3.47, "MAE_90D_pct": -5.67, "MAE_180D_pct": -5.67, "MAE_1Y_pct": -5.67, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": 0.68, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_green_late", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "R6L45_G02_HANA_20240227_54700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "trigger", "round": "R6", "loop": "45", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본환원·디지털금융", "primary_archetype": "ROE/PBR capital return rerating", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_2Y_pct": null, "MAE_2Y_pct": null, "calibration_block_reasons": [], "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "trigger_id": "R6L45_T04_HANA_CONFIRMED_GREEN", "case_id": "R6L45_C21_HANA_20240227_STAGE2", "symbol": "086790", "company_name": "하나금융지주", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-07-03", "entry_date": "2024-07-03", "entry_price": 64600, "evidence_available_at_that_date": "Post-Stage2 continuation and visible market confirmation; used only as label-comparison trigger because Stage2 had already captured most of the move.", "evidence_source": "stock-web OHLC shard; company/sector follow-through context.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "MFE_30D_pct": 7.28, "MFE_90D_pct": 7.28, "MFE_180D_pct": 7.28, "MFE_1Y_pct": 7.28, "MAE_30D_pct": -13.47, "MAE_90D_pct": -13.47, "MAE_180D_pct": -13.47, "MAE_1Y_pct": -15.17, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": 0.68, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_low_incremental_reward", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "R6L45_G02_HANA_20240703_64600", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only"}
{"row_type": "trigger", "round": "R6", "loop": "45", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본환원·디지털금융", "primary_archetype": "ROE/PBR capital return rerating", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_2Y_pct": null, "MAE_2Y_pct": null, "calibration_block_reasons": [], "calibration_usable": true, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R6L45_T05_KAKAOBANK_VALUEUP_FALSE_STAGE2", "case_id": "R6L45_C21_KAKAOBANK_20240227_FALSE_STAGE2", "symbol": "323410", "company_name": "카카오뱅크", "loop_objective": "counterexample_mining; residual_false_positive_mining", "trigger_type": "Stage2-Actionable-Rejected", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 29550, "evidence_available_at_that_date": "Sector-level value-up narrative without a traditional low-PBR capital-return bridge; digital-bank growth valuation did not map into the same ROE/PBR rerating path.", "evidence_source": "Reuters/FSC policy reporting; stock-web OHLC shard.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "MFE_30D_pct": 3.72, "MFE_90D_pct": 3.72, "MFE_180D_pct": 3.72, "MFE_1Y_pct": 3.72, "MAE_30D_pct": -16.07, "MAE_90D_pct": -32.15, "MAE_180D_pct": -37.43, "MAE_1Y_pct": -37.43, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-27", "peak_price": 30650, "drawdown_after_peak_pct": -39.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating_counterexample", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "R6L45_G03_KAKAOBANK_20240227_29550", "dedupe_for_aggregate": true, "aggregate_group_role": "representative"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L45_C21_KBFG_20240227_STAGE2", "trigger_id": "R6L45_T01_KBFG_VALUEUP_STAGE2", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 58, "revision_score": 54, "relative_strength_score": 78, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 75, "valuation_repricing_score": 82, "execution_risk_score": 20, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 58, "revision_score": 54, "relative_strength_score": 78, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 80, "valuation_repricing_score": 86, "execution_risk_score": 20, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 86.0, "stage_label_after": "Stage3-Yellow/near-Green", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score"], "component_delta_explanation": "C21에서는 low-PBR 정책 optionality가 있어도 confirmed revision 55 미만이면 Green을 강제하지 않는다. Stage2/Yellow는 적절했고 가격경로도 180D +66.51%로 양호했다.", "MFE_90D_pct": 44.23, "MAE_90D_pct": -2.4, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R6L45_C21_HANA_20240227_STAGE2", "trigger_id": "R6L45_T03_HANA_VALUEUP_STAGE2", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 52, "revision_score": 50, "relative_strength_score": 72, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 75, "valuation_repricing_score": 76, "execution_risk_score": 24, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 52, "revision_score": 50, "relative_strength_score": 72, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 80, "valuation_repricing_score": 79, "execution_risk_score": 24, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 81.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score"], "component_delta_explanation": "Stage2/Yellow는 맞지만 Green을 기다리면 green_lateness_ratio 0.68로 늦다. C21에서는 Stage2-Actionable을 유지하되 Green은 자본환원+revision bridge가 모두 필요하다.", "MFE_90D_pct": 23.95, "MAE_90D_pct": -5.67, "score_return_alignment_label": "aligned_stage2_green_late", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R6L45_C21_KAKAOBANK_20240227_FALSE_STAGE2", "trigger_id": "R6L45_T05_KAKAOBANK_VALUEUP_FALSE_STAGE2", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 20, "revision_score": 35, "relative_strength_score": 28, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 72, "valuation_repricing_score": 20, "execution_risk_score": 55, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 63.0, "stage_label_before": "Watch/False-Stage2 risk", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": 20, "revision_score": 35, "relative_strength_score": 28, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 50, "valuation_repricing_score": 12, "execution_risk_score": 60, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 55.0, "stage_label_after": "Rejected-Stage2", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "금융 섹터 value-up 정책 노출만으로 Stage2 bonus를 주면 MAE_180D -37.43%의 false positive가 된다. C21은 low-PBR + explicit capital return bridge를 요구해야 한다.", "MFE_90D_pct": 3.72, "MAE_90D_pct": -32.15, "score_return_alignment_label": "counterexample_guard_success", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P3_counterexample_guard_profile", "case_id": "R6L45_C21_KBFG_20240227_STAGE2", "trigger_id": "R6L45_T02_KBFG_LOCAL_4B_STRESS", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": 90, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 92, "execution_risk_score": 35, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 79.0, "stage_label_before": "Local 4B Watch", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": 90, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 92, "execution_risk_score": 45, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 74.0, "stage_label_after": "4B Watch Only", "changed_components": ["execution_risk_score"], "component_delta_explanation": "2024-10-25 local peak proximity는 높지만 2025 full-window peak가 더 높아 price-only local 4B를 full 4B로 취급하면 너무 이르다.", "MFE_90D_pct": 2.87, "MAE_90D_pct": -24.36, "score_return_alignment_label": "4B_local_too_early_guard_needed", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "residual_contribution", "round": "R6", "loop": "45", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_canonical_archetype_count": 1, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["sector_policy_false_positive_without_capital_return_bridge", "green_late_for_financial_valueup", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round_suggestion_1 = R6 / C22_INSURANCE_RATE_CYCLE_RESERVE / insurers value-up vs reserve-cycle counterexamples
next_round_suggestion_2 = R6 / C21 securities holding companies / buyback announcements vs brokerage beta false positives
next_round_suggestion_3 = R10 / C30 construction PF balance-sheet break / financial-stress counterexamples
```

## 28. Source Notes

Stock-web source files inspected:

```text
atlas/manifest.json
atlas/symbol_profiles/105/105560.json
atlas/symbol_profiles/086/086790.json
atlas/symbol_profiles/323/323410.json
atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv
atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv
atlas/ohlcv_tradable_by_symbol_year/086/086790/2025.csv
atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv
atlas/ohlcv_tradable_by_symbol_year/323/323410/2025.csv
```

External historical context used:

```text
- Reuters reporting on Korea Corporate Value-up Programme launch / follow-up.
- Financial Services Commission policy context as reported in public news.
```
