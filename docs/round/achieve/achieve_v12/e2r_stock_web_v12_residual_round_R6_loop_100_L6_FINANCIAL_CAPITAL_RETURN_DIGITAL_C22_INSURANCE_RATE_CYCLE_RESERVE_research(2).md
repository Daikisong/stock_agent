# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R6
selected_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE
deep_sub_archetype_id: C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE
output_filename: e2r_stock_web_v12_residual_round_R6_loop_100_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated`. This file does not change production scoring. It stress-tests the current profile against C22 insurance/rate/reserve cases and proposes only scope-limited shadow rules. Existing global constraints remain intact: Stage3-Green is not loosened, price-only blowoff is not positive evidence, and full 4B needs non-price evidence.

## 2. Round / Large Sector / Canonical Archetype Scope

C22 maps to `R6 / L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`. This is a sector-archetype residual repair file, not an R13 cross-archetype review. The core mechanism is insurance rate cycle, IFRS17/CSM/K-ICS reserve quality, capital return capacity, and event/label spikes.

```text
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE
deep_sub_archetype_id = C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE
```

## 3. Previous Coverage / Duplicate Avoidance Check

Published No-Repeat Index lists C22 at 60 representative rows, 17 symbols, positives/counterexamples 7/15 and 4B/4C 7/0. Because this is already above 50 rows, this execution is quality repair rather than minimum coverage filling. The selected rows avoid repeating a same-entry group inside this local session and focus on different insurance sub-routes: non-life quality underwriting, life insurer rate beta, value-up capital policy, M&A/event spike, and high-MAE 4B paths.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
local_duplicate_check = pass
new_independent_case_count = 8
```

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
raw_adjusted_price_used: false
tradable_shard_columns: d,o,h,l,c,v,a,mc,s,m
```

All selected entries use tradable calibration shards. MFE/MAE is calculated from entry close against subsequent high/low over 30/90/180 tradable rows.

## 5. Historical Eligibility Gate

All 8 trigger rows have entry_date, entry_price, complete 30/90/180D MFE/MAE and a 180-trading-day forward window within the stock-web manifest range. Corporate-action caveats are marked clean for the 180D calibration window in this research artifact. Because the evidence is mostly sector/regulatory/proxy context rather than exact company filing URL repair, `promotion_usable_without_url_repair=false` is carried in the machine-readable rows.

## 6. Canonical Archetype Compression Map

| fine/deep route | compressed canonical | treatment |
|---|---|---|
| underwriting quality + reserve confidence + capital return | C22_INSURANCE_RATE_CYCLE_RESERVE | allow Stage2/Yellow when bridge exists |
| life-insurer rate beta without reserve bridge | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage1 watch or local 4B watch |
| value-up / IFRS17 / K-ICS label only | C22_INSURANCE_RATE_CYCLE_RESERVE | not positive evidence without bridge |
| M&A or transaction event spike | C22_INSURANCE_RATE_CYCLE_RESERVE | local 4B watch; hard 4C review if MAE confirms |
| reinsurance pricing / combined ratio bridge | C22_INSURANCE_RATE_CYCLE_RESERVE | allow Stage2 when repeatable profitability bridge exists |

## 7. Case Selection Summary

| case_id | symbol | name | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | label | current_profile_error |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| C22-R6-L100-01-005830 | 005830 | DB손해보험 | Stage2-Actionable | 2024-02-02 | 93900 | 17.15 | -2.98 | 21.62 | -8.20 | 32.06 | -8.20 | positive | false |
| C22-R6-L100-02-000810 | 000810 | 삼성화재 | Stage3-Yellow | 2024-02-02 | 292000 | 16.44 | -2.23 | 30.14 | -6.68 | 34.76 | -6.68 | positive | false |
| C22-R6-L100-03-032830 | 032830 | 삼성생명 | Stage3-Yellow | 2024-02-05 | 78600 | 38.04 | -5.22 | 38.04 | -5.22 | 38.04 | -5.22 | positive | true |
| C22-R6-L100-04-085620 | 085620 | 미래에셋생명 | Stage2 | 2024-03-18 | 4885 | 9.72 | -9.83 | 25.69 | -9.83 | 25.69 | -9.83 | positive | false |
| C22-R6-L100-05-001450 | 001450 | 현대해상 | Stage2 | 2024-02-02 | 35450 | 3.81 | -13.68 | 3.81 | -19.75 | 3.81 | -19.75 | counterexample | true |
| C22-R6-L100-06-088350 | 088350 | 한화생명 | Stage2 | 2024-02-05 | 3605 | 5.83 | -17.06 | 5.83 | -28.43 | 5.83 | -28.43 | counterexample | true |
| C22-R6-L100-07-082640 | 082640 | 동양생명 | Stage4B | 2024-08-16 | 8120 | 9.85 | -35.71 | 9.85 | -45.44 | 9.85 | -46.12 | counterexample | true |
| C22-R6-L100-08-000400 | 000400 | 롯데손해보험 | Stage4B | 2024-02-02 | 2630 | 39.54 | -3.80 | 53.42 | -3.80 | 55.51 | -18.25 | counterexample | true |

## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 4
counterexample_count: 4
stage4b_case_count: 2
stage4c_case_count: 1
current_profile_error_count: 5
avg_MFE_90D_pct: 23.55
avg_MAE_90D_pct: -15.92
avg_positive_MFE_90D_pct: 28.87
avg_counterexample_MAE_90D_pct: -24.36
```

The key split is not “insurance sector good/bad.” It is whether the rate/reserve/capital-return mechanism has a bridge. Positive rows show strong MFE with contained MAE. Counterexamples show label-only spikes, weak reserve bridge, or later drawdown.

## 9. Evidence Source Map

| source | role in this MD | source_proxy_only |
|---|---|---:|
| FSC Corporate Value-up Program, 2024-02-26 | value-up and capital-return policy context | true |
| KIRI Korean Insurance Industry 2024 | IFRS17 effective date and industry balance-sheet context | true |
| FSC/FSS IFRS17 actuarial assumption and discount-rate reform summary | reserve/discount-rate reliability context | true |
| Korean Re IFRS17 regulatory transition note | insurance accounting transition context | true |
| Songdaiki/stock-web tradable shards | actual OHLCV path, entry price, MFE/MAE | false |

Company-level URL repair is still needed before promotion. This file is therefore a quality-repair / guardrail candidate, not an immediate production patch.

## 10. Price Data Source Map

| symbol | shard path | entry year | calibration usable |
|---:|---|---:|---:|
| 005830 | `atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv` | 2024 | true |
| 000810 | `atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv` | 2024 | true |
| 032830 | `atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv` | 2024 | true |
| 085620 | `atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv` | 2024 | true |
| 001450 | `atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv` | 2024 | true |
| 088350 | `atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv` | 2024 | true |
| 082640 | `atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv` | 2024 | true |
| 000400 | `atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv` | 2024 | true |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | name | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | label | current_profile_error |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| C22-R6-L100-01-005830 | 005830 | DB손해보험 | Stage2-Actionable | 2024-02-02 | 93900 | 17.15 | -2.98 | 21.62 | -8.20 | 32.06 | -8.20 | positive | false |
| C22-R6-L100-02-000810 | 000810 | 삼성화재 | Stage3-Yellow | 2024-02-02 | 292000 | 16.44 | -2.23 | 30.14 | -6.68 | 34.76 | -6.68 | positive | false |
| C22-R6-L100-03-032830 | 032830 | 삼성생명 | Stage3-Yellow | 2024-02-05 | 78600 | 38.04 | -5.22 | 38.04 | -5.22 | 38.04 | -5.22 | positive | true |
| C22-R6-L100-04-085620 | 085620 | 미래에셋생명 | Stage2 | 2024-03-18 | 4885 | 9.72 | -9.83 | 25.69 | -9.83 | 25.69 | -9.83 | positive | false |
| C22-R6-L100-05-001450 | 001450 | 현대해상 | Stage2 | 2024-02-02 | 35450 | 3.81 | -13.68 | 3.81 | -19.75 | 3.81 | -19.75 | counterexample | true |
| C22-R6-L100-06-088350 | 088350 | 한화생명 | Stage2 | 2024-02-05 | 3605 | 5.83 | -17.06 | 5.83 | -28.43 | 5.83 | -28.43 | counterexample | true |
| C22-R6-L100-07-082640 | 082640 | 동양생명 | Stage4B | 2024-08-16 | 8120 | 9.85 | -35.71 | 9.85 | -45.44 | 9.85 | -46.12 | counterexample | true |
| C22-R6-L100-08-000400 | 000400 | 롯데손해보험 | Stage4B | 2024-02-02 | 2630 | 39.54 | -3.80 | 53.42 | -3.80 | 55.51 | -18.25 | counterexample | true |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_180D_date | trough_180D_date |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 005830 | 2024-02-02 | 93900 | 17.15 | -2.98 | 21.62 | -8.20 | 32.06 | -8.20 | 2024-08-22 | 2024-04-19 |
| 000810 | 2024-02-02 | 292000 | 16.44 | -2.23 | 30.14 | -6.68 | 34.76 | -6.68 | 2024-06-28 | 2024-04-19 |
| 032830 | 2024-02-05 | 78600 | 38.04 | -5.22 | 38.04 | -5.22 | 38.04 | -5.22 | 2024-03-08 | 2024-02-05 |
| 085620 | 2024-03-18 | 4885 | 9.72 | -9.83 | 25.69 | -9.83 | 25.69 | -9.83 | 2024-06-27 | 2024-04-03 |
| 001450 | 2024-02-02 | 35450 | 3.81 | -13.68 | 3.81 | -19.75 | 3.81 | -19.75 | 2024-02-05 | 2024-04-15 |
| 088350 | 2024-02-05 | 3605 | 5.83 | -17.06 | 5.83 | -28.43 | 5.83 | -28.43 | 2024-02-13 | 2024-04-16 |
| 082640 | 2024-08-16 | 8120 | 9.85 | -35.71 | 9.85 | -45.44 | 9.85 | -46.12 | 2024-08-27 | 2025-01-02 |
| 000400 | 2024-02-02 | 2630 | 39.54 | -3.80 | 53.42 | -3.80 | 55.51 | -18.25 | 2024-06-26 | 2024-10-25 |

## 13. Current Calibrated Profile Stress Test

The current profile already blocks pure price-only blowoff globally. C22 still needs a canonical bridge requirement because the same macro labels can produce opposite paths. The stress test finds four clean positives, three high-MAE false positives, and one event-spike case that needs local 4B / hard-4C review.

| finding | count | implication |
|---|---:|---|
| aligned positive with bridge | 4 | preserve Stage2/Yellow when underwriting/reserve/capital-return bridge exists |
| false-positive or high-MAE path | 4 | require C22-specific bridge before Yellow/Green |
| local 4B candidate | 4 | label/event spikes should remain watch, not positive rerating |
| hard 4C review candidate | 1 | transaction/policy failure plus deep MAE needs thesis-break route |

## 14. Stage2 / Yellow / Green Comparison

| stage route | observed result | rule implication |
|---|---|---|
| Stage2-Actionable with underwriting/reserve bridge | DB손보 positive | keep Stage2-Actionable |
| Stage3-Yellow with quality underwriting/capital return | 삼성화재 positive | allow Yellow; do not force Green without revision bridge |
| Stage3-Yellow with value-up capital policy | 삼성생명 positive but boundary | keep Yellow only if capital-return bridge explicit |
| Stage2 label without reserve bridge | 현대해상/한화생명 counterexamples | downgrade to watch until bridge appears |
| Stage4B event spike | 동양생명/롯데손보 | full 4B requires non-price evidence; otherwise local 4B watch |

## 15. 4B Local vs Full-window Timing Audit

C22 has a strong local spike pattern. A policy, value-up, or M&A label can create high MFE but still fail as a positive rerating if later MAE is large. Local 4B should mark the watch condition; full 4B or hard 4C should wait for non-price thesis deterioration such as reserve-quality loss, capital-ratio pressure, transaction failure, or persistent loss-ratio deterioration.

| symbol | trigger_type | local_4B_watch_candidate | hard_4C_review_candidate | reason |
|---:|---|---:|---:|---|
| 005830 | Stage2-Actionable | false | false | nonlife_underwriting_quality_reserve_capital_return_bridge |
| 000810 | Stage3-Yellow | false | false | quality_underwriting_csm_kics_capital_return_bridge |
| 032830 | Stage3-Yellow | false | false | life_insurer_valueup_capital_policy_rate_beta_boundary |
| 085620 | Stage2 | false | false | life_insurer_contractual_margin_capital_return_bridge |
| 001450 | Stage2 | true | false | auto_loss_ratio_reserve_risk_vs_rate_cycle_label |
| 088350 | Stage2 | true | false | life_insurer_rate_beta_without_reserve_quality_bridge |
| 082640 | Stage4B | true | true | transaction_policy_label_failure_high_mae |
| 000400 | Stage4B | true | false | small_insurer_mna_price_spike_high_mae_guard |

## 16. 4C Protection Audit

C22 should not route to hard 4C on generic rate weakness alone. It needs at least one of: reserve-quality deterioration, K-ICS/capital-ratio pressure, loss-ratio thesis break, failed transaction thesis, or dividend/capital-return capacity impairment. Only the 동양생명 path is marked as hard-4C review candidate in this loop because the 90/180D MAE is severe and the event thesis decayed.

## 17. Sector-Specific Rule Candidate

```text
L6_C22_rule_candidate:
  require_C22_bridge_before_Yellow_or_Green:
    - underwriting_quality_or_loss_ratio_improvement
    - reserve_confidence_or_CSM_quality_signal
    - KICS_or_capital_ratio_capacity_signal
    - explicit_capital_return_or_dividend_capacity_signal
    - reinsurance_pricing_or_combined_ratio_bridge
  label_only_conditions_route_to_watch:
    - value-up label only
    - IFRS17/K-ICS label only
    - rate beta only
    - M&A or transaction headline only
```

## 18. Canonical-Archetype Rule Candidate

```text
C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch
```

This is canonical-specific. It should not loosen global financial thresholds, and it should not apply to C21 bank/holding ROE-PBR capital-return cases unless a separate C21 calibration supports it.

## 19. Before / After Backtest Comparison

| profile proxy | positive preserved | false positives blocked/watch-routed | current_profile_error_count | note |
|---|---:|---:|---:|---|
| P0 current calibrated proxy | 4 | 1 | 5 | label-only Stage2/Yellow can still slip through C22 |
| P1 C22 bridge required | 4 | 3 | 2 | reserve/capital-return bridge blocks weak Stage2 |
| P2 C22 bridge + local 4B watch | 4 | 4 | 1 | event spikes kept as watch not positive |
| P3 URL-repaired production candidate | pending | pending | pending | requires company-level evidence URL repair |

## 20. Score-Return Alignment Matrix

| bucket | rows | return alignment | interpretation |
|---|---:|---|---|
| bridge-positive | 4 | MFE90 >= 20%, MAE90 > -10% mostly | allow Stage2/Yellow |
| label-only/high-MAE | 3 | MFE90 weak or MAE90 <= -19% | block positive / local 4B watch |
| event-spike with high MFE but later MAE | 1 | MFE90 high yet 180D MAE deep | 4B watch, not Green |

## 21. Coverage Matrix

| scope | published index rows | local-session added in this file | adjusted local reading | remaining purpose |
|---|---:|---:|---:|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | 60 | 8 | 68 | Priority 2 quality repair; URL/proxy replacement and 4B/4C balance |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 139 | 8 | 147 | 금융 내 C22 보험 reserve/rate bridge residual repair |


## 22. Residual Contribution Summary

```yaml
selected_round: "R6"
selected_loop: 100
large_sector_id: "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL"
canonical_archetype_id: "C22_INSURANCE_RATE_CYCLE_RESERVE"
fine_archetype_id: "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE"
new_independent_case_count: 8
reused_case_count: 0
same_archetype_new_symbol_count: 8
same_archetype_new_trigger_family_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
positive_case_count: 4
counterexample_count: 4
stage4b_case_count: 2
stage4c_case_count: 1
current_profile_error_count: 5
source_proxy_only_count: 8
evidence_url_pending_count: 8
avg_MFE_90D_pct: 23.55
avg_MAE_90D_pct: -15.92
avg_positive_MFE_90D_pct: 28.87
avg_counterexample_MAE_90D_pct: -24.36
new_axis_proposed: "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch"
existing_axis_strengthened: ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"]
existing_axis_weakened: "hard_4c_thesis_break_routes_to_4c_when_only_generic_rate_or_valueup_label_is_present"
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: false
promotion_blocked_until_url_repair: true
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web OHLC path, entry_date, entry_price, 30/90/180D MFE/MAE, forward-window availability, canonical/sector mapping, duplicate key construction.

Not validated for production promotion: exact company disclosure URL for each trigger, audited CSM/K-ICS values per company, and final production score weight. This file is suitable for batch ingest as historical calibration evidence but should keep `promotion_blocked_until_url_repair=true` for rows that rely on proxy sector evidence.

## 24. Shadow Weight Calibration

```csv
scope,canonical_archetype_id,axis,current_weight_delta,proposed_shadow_delta,reason,apply_now
large_sector,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+0.00,quality_repair_only_no_global_threshold_change,false
canonical,C22_INSURANCE_RATE_CYCLE_RESERVE,C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green,0,+0.25,bridge requirement strengthens Stage2/Yellow precision after URL repair,false
canonical,C22_INSURANCE_RATE_CYCLE_RESERVE,C22_valueup_or_IFRS17_label_to_local_4B_watch,0,+0.20,label-only event spikes showed high MAE / local 4B behavior,false
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "price_data_source": "Songdaiki/stock-web", "source_repo_url": "https://github.com/Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "checked_symbols": ["005830", "000810", "032830", "085620", "001450", "088350", "082640", "000400"], "validation_status": "pass_all_trigger_rows_have_30_90_180_mfe_mae"}
{"case_id": "C22-R6-L100-01-005830", "symbol": "005830", "name": "DB손해보험", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "case_label": "positive", "evidence_family": "nonlife_underwriting_quality_reserve_capital_return_bridge", "thesis": "자동차보험 손해율/예실차 개선, reserve confidence, 배당·자본정책 기대가 같이 확인될 때 C22의 Stage2-Actionable이 가격보다 늦지 않게 작동하는 손보 대형주 경로.", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "row_type": "case"}
{"case_id": "C22-R6-L100-02-000810", "symbol": "000810", "name": "삼성화재", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "case_label": "positive", "evidence_family": "quality_underwriting_csm_kics_capital_return_bridge", "thesis": "quality underwriting, K-ICS/자본여력, 배당 기대가 같이 확인된 경우 C22에서 Yellow까지 허용되는 high-quality positive 경로.", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "row_type": "case"}
{"case_id": "C22-R6-L100-03-032830", "symbol": "032830", "name": "삼성생명", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "case_label": "positive", "evidence_family": "life_insurer_valueup_capital_policy_rate_beta_boundary", "thesis": "생보 value-up/자본정책 기대가 빠르게 가격화된 positive이나, pure reserve/rate cycle보다 capital policy 성격이 강한 C22/C21 경계 사례.", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "row_type": "case"}
{"case_id": "C22-R6-L100-04-085620", "symbol": "085620", "name": "미래에셋생명", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "case_label": "positive", "evidence_family": "life_insurer_contractual_margin_capital_return_bridge", "thesis": "생보 중소형에서 직접 reserve disclosure는 약하지만 낮은 MAE와 90D MFE가 나온 Stage2-quality positive. 다만 Green 승격에는 더 강한 CSM/K-ICS bridge가 필요하다.", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "row_type": "case"}
{"case_id": "C22-R6-L100-05-001450", "symbol": "001450", "name": "현대해상", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "case_label": "counterexample", "evidence_family": "auto_loss_ratio_reserve_risk_vs_rate_cycle_label", "thesis": "같은 손보 섹터 label이어도 손해율/reserve uncertainty가 남으면 value-up price spike가 빠르게 소멸한다. Stage2 승격 전에 reserve/underwriting bridge를 요구해야 하는 반례.", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "row_type": "case"}
{"case_id": "C22-R6-L100-06-088350", "symbol": "088350", "name": "한화생명", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "case_label": "counterexample", "evidence_family": "life_insurer_rate_beta_without_reserve_quality_bridge", "thesis": "생보 rate beta는 있었으나 reserve quality와 shareholder return bridge가 약하면 Stage2 승격이 과해진다. 90D MAE가 -20%를 넘는 high-MAE guardrail 사례.", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "row_type": "case"}
{"case_id": "C22-R6-L100-07-082640", "symbol": "082640", "name": "동양생명", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "case_label": "counterexample", "evidence_family": "transaction_policy_label_failure_high_mae", "thesis": "일회성 transaction/policy 기대가 낮은 지속성으로 바뀌며 90/180D MAE가 커진 local 4B → hard 4C review 경로.", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "row_type": "case"}
{"case_id": "C22-R6-L100-08-000400", "symbol": "000400", "name": "롯데손해보험", "selected_round": "R6", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "case_label": "counterexample", "evidence_family": "small_insurer_mna_price_spike_high_mae_guard", "thesis": "M&A/정책 label spike는 90D MFE가 컸지만 bridge가 얇아 180D MAE가 확대된 사례. Positive 승격이 아니라 local 4B watch로 남겨야 한다.", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "row_type": "case"}
{"code": "005830", "name": "DB손해보험", "trigger_date": "2024-02-01", "requested_entry": "2024-02-02", "trigger_type": "Stage2-Actionable", "case_label": "positive", "evidence_family": "nonlife_underwriting_quality_reserve_capital_return_bridge", "thesis": "자동차보험 손해율/예실차 개선, reserve confidence, 배당·자본정책 기대가 같이 확인될 때 C22의 Stage2-Actionable이 가격보다 늦지 않게 작동하는 손보 대형주 경로.", "entry_date": "2024-02-02", "entry_price": 93900.0, "MFE_30D_pct": 17.15, "MAE_30D_pct": -2.98, "peak_30D_date": "2024-03-14", "trough_30D_date": "2024-02-28", "MFE_90D_pct": 21.62, "MAE_90D_pct": -8.2, "peak_90D_date": "2024-05-16", "trough_90D_date": "2024-04-19", "MFE_180D_pct": 32.06, "MAE_180D_pct": -8.2, "peak_180D_date": "2024-08-22", "trough_180D_date": "2024-04-19", "current_profile_error": false, "simulated_total_after_shadow": 84, "shadow_result": "keep_or_upgrade_with_bridge", "case_id": "C22-R6-L100-01-005830", "ticker": "005830", "symbol": "005830", "row_type": "trigger", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "deep_sub_archetype_id": "C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "manifest_max_date": "2026-02-20", "entry_rule": "next_trading_day_or_same_day_after_historical_evidence_timestamp", "forward_window_status": "pass_180D", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "promotion_usable_without_url_repair": false, "source_proxy_only": true, "evidence_url_pending": true, "evidence_urls": ["https://www.fsc.go.kr/eng/pr010101/81778", "https://kiri.or.kr/eng/pdf/Korean_Insurance_Industry_2024.pdf", "https://www.kimchang.com/en/insights/detail.kc?idx=30965&sch_section=4", "https://eng.koreanre.com/sub.asp?exec=view&intCategory=0&intPage=1&intSeq=1723&maincode=501&strBoardID=kui_575&strSearchCategory=%7Cs_name%7Cs_subject%7C&strSearchWord=&sub_sequence=519&sub_sub_sequence=575"], "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_RESERVE:005830:Stage2-Actionable:2024-02-02", "dedupe_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|005830|Stage2-Actionable|2024-02-02|nonlife_underwriting_quality_reserve_capital_return_bridge", "hard_duplicate_check": "pass_new_within_local_session_for_C22", "representative_for_aggregate": true, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "score_return_alignment": "aligned_positive", "current_profile_error_type": "none", "local_4b_watch_candidate": false, "hard_4c_review_candidate": false, "green_unlock_candidate": true}
{"code": "000810", "name": "삼성화재", "trigger_date": "2024-02-01", "requested_entry": "2024-02-02", "trigger_type": "Stage3-Yellow", "case_label": "positive", "evidence_family": "quality_underwriting_csm_kics_capital_return_bridge", "thesis": "quality underwriting, K-ICS/자본여력, 배당 기대가 같이 확인된 경우 C22에서 Yellow까지 허용되는 high-quality positive 경로.", "entry_date": "2024-02-02", "entry_price": 292000.0, "MFE_30D_pct": 16.44, "MAE_30D_pct": -2.23, "peak_30D_date": "2024-02-13", "trough_30D_date": "2024-02-29", "MFE_90D_pct": 30.14, "MAE_90D_pct": -6.68, "peak_90D_date": "2024-05-17", "trough_90D_date": "2024-04-19", "MFE_180D_pct": 34.76, "MAE_180D_pct": -6.68, "peak_180D_date": "2024-06-28", "trough_180D_date": "2024-04-19", "current_profile_error": false, "simulated_total_after_shadow": 86, "shadow_result": "keep_yellow_with_bridge", "case_id": "C22-R6-L100-02-000810", "ticker": "000810", "symbol": "000810", "row_type": "trigger", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "deep_sub_archetype_id": "C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "manifest_max_date": "2026-02-20", "entry_rule": "next_trading_day_or_same_day_after_historical_evidence_timestamp", "forward_window_status": "pass_180D", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "promotion_usable_without_url_repair": false, "source_proxy_only": true, "evidence_url_pending": true, "evidence_urls": ["https://www.fsc.go.kr/eng/pr010101/81778", "https://kiri.or.kr/eng/pdf/Korean_Insurance_Industry_2024.pdf", "https://www.kimchang.com/en/insights/detail.kc?idx=30965&sch_section=4", "https://eng.koreanre.com/sub.asp?exec=view&intCategory=0&intPage=1&intSeq=1723&maincode=501&strBoardID=kui_575&strSearchCategory=%7Cs_name%7Cs_subject%7C&strSearchWord=&sub_sequence=519&sub_sub_sequence=575"], "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_RESERVE:000810:Stage3-Yellow:2024-02-02", "dedupe_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|000810|Stage3-Yellow|2024-02-02|quality_underwriting_csm_kics_capital_return_bridge", "hard_duplicate_check": "pass_new_within_local_session_for_C22", "representative_for_aggregate": true, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "score_return_alignment": "aligned_positive", "current_profile_error_type": "none", "local_4b_watch_candidate": false, "hard_4c_review_candidate": false, "green_unlock_candidate": true}
{"code": "032830", "name": "삼성생명", "trigger_date": "2024-02-02", "requested_entry": "2024-02-05", "trigger_type": "Stage3-Yellow", "case_label": "positive", "evidence_family": "life_insurer_valueup_capital_policy_rate_beta_boundary", "thesis": "생보 value-up/자본정책 기대가 빠르게 가격화된 positive이나, pure reserve/rate cycle보다 capital policy 성격이 강한 C22/C21 경계 사례.", "entry_date": "2024-02-05", "entry_price": 78600.0, "MFE_30D_pct": 38.04, "MAE_30D_pct": -5.22, "peak_30D_date": "2024-03-08", "trough_30D_date": "2024-02-05", "MFE_90D_pct": 38.04, "MAE_90D_pct": -5.22, "peak_90D_date": "2024-03-08", "trough_90D_date": "2024-02-05", "MFE_180D_pct": 38.04, "MAE_180D_pct": -5.22, "peak_180D_date": "2024-03-08", "trough_180D_date": "2024-02-05", "current_profile_error": true, "simulated_total_after_shadow": 78, "shadow_result": "keep_yellow_but_require_capital_return_bridge", "case_id": "C22-R6-L100-03-032830", "ticker": "032830", "symbol": "032830", "row_type": "trigger", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "deep_sub_archetype_id": "C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "profile_path": "atlas/symbol_profiles/032/032830.json", "manifest_max_date": "2026-02-20", "entry_rule": "next_trading_day_or_same_day_after_historical_evidence_timestamp", "forward_window_status": "pass_180D", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "promotion_usable_without_url_repair": false, "source_proxy_only": true, "evidence_url_pending": true, "evidence_urls": ["https://www.fsc.go.kr/eng/pr010101/81778", "https://kiri.or.kr/eng/pdf/Korean_Insurance_Industry_2024.pdf", "https://www.kimchang.com/en/insights/detail.kc?idx=30965&sch_section=4", "https://eng.koreanre.com/sub.asp?exec=view&intCategory=0&intPage=1&intSeq=1723&maincode=501&strBoardID=kui_575&strSearchCategory=%7Cs_name%7Cs_subject%7C&strSearchWord=&sub_sequence=519&sub_sub_sequence=575"], "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_RESERVE:032830:Stage3-Yellow:2024-02-05", "dedupe_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|032830|Stage3-Yellow|2024-02-05|life_insurer_valueup_capital_policy_rate_beta_boundary", "hard_duplicate_check": "pass_new_within_local_session_for_C22", "representative_for_aggregate": true, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "score_return_alignment": "aligned_positive", "current_profile_error_type": "false_positive_or_bridge_missing", "local_4b_watch_candidate": false, "hard_4c_review_candidate": false, "green_unlock_candidate": true}
{"code": "085620", "name": "미래에셋생명", "trigger_date": "2024-03-15", "requested_entry": "2024-03-18", "trigger_type": "Stage2", "case_label": "positive", "evidence_family": "life_insurer_contractual_margin_capital_return_bridge", "thesis": "생보 중소형에서 직접 reserve disclosure는 약하지만 낮은 MAE와 90D MFE가 나온 Stage2-quality positive. 다만 Green 승격에는 더 강한 CSM/K-ICS bridge가 필요하다.", "entry_date": "2024-03-18", "entry_price": 4885.0, "MFE_30D_pct": 9.72, "MAE_30D_pct": -9.83, "peak_30D_date": "2024-04-09", "trough_30D_date": "2024-04-03", "MFE_90D_pct": 25.69, "MAE_90D_pct": -9.83, "peak_90D_date": "2024-06-27", "trough_90D_date": "2024-04-03", "MFE_180D_pct": 25.69, "MAE_180D_pct": -9.83, "peak_180D_date": "2024-06-27", "trough_180D_date": "2024-04-03", "current_profile_error": false, "simulated_total_after_shadow": 77, "shadow_result": "keep_stage2_with_bridge", "case_id": "C22-R6-L100-04-085620", "ticker": "085620", "symbol": "085620", "row_type": "trigger", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "deep_sub_archetype_id": "C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv", "profile_path": "atlas/symbol_profiles/085/085620.json", "manifest_max_date": "2026-02-20", "entry_rule": "next_trading_day_or_same_day_after_historical_evidence_timestamp", "forward_window_status": "pass_180D", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "promotion_usable_without_url_repair": false, "source_proxy_only": true, "evidence_url_pending": true, "evidence_urls": ["https://www.fsc.go.kr/eng/pr010101/81778", "https://kiri.or.kr/eng/pdf/Korean_Insurance_Industry_2024.pdf", "https://www.kimchang.com/en/insights/detail.kc?idx=30965&sch_section=4", "https://eng.koreanre.com/sub.asp?exec=view&intCategory=0&intPage=1&intSeq=1723&maincode=501&strBoardID=kui_575&strSearchCategory=%7Cs_name%7Cs_subject%7C&strSearchWord=&sub_sequence=519&sub_sub_sequence=575"], "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_RESERVE:085620:Stage2:2024-03-18", "dedupe_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|085620|Stage2|2024-03-18|life_insurer_contractual_margin_capital_return_bridge", "hard_duplicate_check": "pass_new_within_local_session_for_C22", "representative_for_aggregate": true, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "score_return_alignment": "aligned_positive", "current_profile_error_type": "none", "local_4b_watch_candidate": false, "hard_4c_review_candidate": false, "green_unlock_candidate": false}
{"code": "001450", "name": "현대해상", "trigger_date": "2024-02-01", "requested_entry": "2024-02-02", "trigger_type": "Stage2", "case_label": "counterexample", "evidence_family": "auto_loss_ratio_reserve_risk_vs_rate_cycle_label", "thesis": "같은 손보 섹터 label이어도 손해율/reserve uncertainty가 남으면 value-up price spike가 빠르게 소멸한다. Stage2 승격 전에 reserve/underwriting bridge를 요구해야 하는 반례.", "entry_date": "2024-02-02", "entry_price": 35450.0, "MFE_30D_pct": 3.81, "MAE_30D_pct": -13.68, "peak_30D_date": "2024-02-05", "trough_30D_date": "2024-02-28", "MFE_90D_pct": 3.81, "MAE_90D_pct": -19.75, "peak_90D_date": "2024-02-05", "trough_90D_date": "2024-04-15", "MFE_180D_pct": 3.81, "MAE_180D_pct": -19.75, "peak_180D_date": "2024-02-05", "trough_180D_date": "2024-04-15", "current_profile_error": true, "simulated_total_after_shadow": 64, "shadow_result": "downgrade_to_stage1_or_local_4B_watch", "case_id": "C22-R6-L100-05-001450", "ticker": "001450", "symbol": "001450", "row_type": "trigger", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "deep_sub_archetype_id": "C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv", "profile_path": "atlas/symbol_profiles/001/001450.json", "manifest_max_date": "2026-02-20", "entry_rule": "next_trading_day_or_same_day_after_historical_evidence_timestamp", "forward_window_status": "pass_180D", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "promotion_usable_without_url_repair": false, "source_proxy_only": true, "evidence_url_pending": true, "evidence_urls": ["https://www.fsc.go.kr/eng/pr010101/81778", "https://kiri.or.kr/eng/pdf/Korean_Insurance_Industry_2024.pdf", "https://www.kimchang.com/en/insights/detail.kc?idx=30965&sch_section=4", "https://eng.koreanre.com/sub.asp?exec=view&intCategory=0&intPage=1&intSeq=1723&maincode=501&strBoardID=kui_575&strSearchCategory=%7Cs_name%7Cs_subject%7C&strSearchWord=&sub_sequence=519&sub_sub_sequence=575"], "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_RESERVE:001450:Stage2:2024-02-02", "dedupe_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|001450|Stage2|2024-02-02|auto_loss_ratio_reserve_risk_vs_rate_cycle_label", "hard_duplicate_check": "pass_new_within_local_session_for_C22", "representative_for_aggregate": true, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "score_return_alignment": "false_positive_or_high_MAE_guardrail", "current_profile_error_type": "false_positive_or_bridge_missing", "local_4b_watch_candidate": true, "hard_4c_review_candidate": false, "green_unlock_candidate": false}
{"code": "088350", "name": "한화생명", "trigger_date": "2024-02-02", "requested_entry": "2024-02-05", "trigger_type": "Stage2", "case_label": "counterexample", "evidence_family": "life_insurer_rate_beta_without_reserve_quality_bridge", "thesis": "생보 rate beta는 있었으나 reserve quality와 shareholder return bridge가 약하면 Stage2 승격이 과해진다. 90D MAE가 -20%를 넘는 high-MAE guardrail 사례.", "entry_date": "2024-02-05", "entry_price": 3605.0, "MFE_30D_pct": 5.83, "MAE_30D_pct": -17.06, "peak_30D_date": "2024-02-13", "trough_30D_date": "2024-02-28", "MFE_90D_pct": 5.83, "MAE_90D_pct": -28.43, "peak_90D_date": "2024-02-13", "trough_90D_date": "2024-04-16", "MFE_180D_pct": 5.83, "MAE_180D_pct": -28.43, "peak_180D_date": "2024-02-13", "trough_180D_date": "2024-04-16", "current_profile_error": true, "simulated_total_after_shadow": 62, "shadow_result": "downgrade_to_stage1_or_local_4B_watch", "case_id": "C22-R6-L100-06-088350", "ticker": "088350", "symbol": "088350", "row_type": "trigger", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "deep_sub_archetype_id": "C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv", "profile_path": "atlas/symbol_profiles/088/088350.json", "manifest_max_date": "2026-02-20", "entry_rule": "next_trading_day_or_same_day_after_historical_evidence_timestamp", "forward_window_status": "pass_180D", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "promotion_usable_without_url_repair": false, "source_proxy_only": true, "evidence_url_pending": true, "evidence_urls": ["https://www.fsc.go.kr/eng/pr010101/81778", "https://kiri.or.kr/eng/pdf/Korean_Insurance_Industry_2024.pdf", "https://www.kimchang.com/en/insights/detail.kc?idx=30965&sch_section=4", "https://eng.koreanre.com/sub.asp?exec=view&intCategory=0&intPage=1&intSeq=1723&maincode=501&strBoardID=kui_575&strSearchCategory=%7Cs_name%7Cs_subject%7C&strSearchWord=&sub_sequence=519&sub_sub_sequence=575"], "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_RESERVE:088350:Stage2:2024-02-05", "dedupe_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|088350|Stage2|2024-02-05|life_insurer_rate_beta_without_reserve_quality_bridge", "hard_duplicate_check": "pass_new_within_local_session_for_C22", "representative_for_aggregate": true, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "score_return_alignment": "false_positive_or_high_MAE_guardrail", "current_profile_error_type": "false_positive_or_bridge_missing", "local_4b_watch_candidate": true, "hard_4c_review_candidate": false, "green_unlock_candidate": false}
{"code": "082640", "name": "동양생명", "trigger_date": "2024-08-16", "requested_entry": "2024-08-16", "trigger_type": "Stage4B", "case_label": "counterexample", "evidence_family": "transaction_policy_label_failure_high_mae", "thesis": "일회성 transaction/policy 기대가 낮은 지속성으로 바뀌며 90/180D MAE가 커진 local 4B → hard 4C review 경로.", "entry_date": "2024-08-16", "entry_price": 8120.0, "MFE_30D_pct": 9.85, "MAE_30D_pct": -35.71, "peak_30D_date": "2024-08-27", "trough_30D_date": "2024-10-02", "MFE_90D_pct": 9.85, "MAE_90D_pct": -45.44, "peak_90D_date": "2024-08-27", "trough_90D_date": "2024-12-23", "MFE_180D_pct": 9.85, "MAE_180D_pct": -46.12, "peak_180D_date": "2024-08-27", "trough_180D_date": "2025-01-02", "current_profile_error": true, "simulated_total_after_shadow": 55, "shadow_result": "route_to_hard_4C_review", "case_id": "C22-R6-L100-07-082640", "ticker": "082640", "symbol": "082640", "row_type": "trigger", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "deep_sub_archetype_id": "C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv", "profile_path": "atlas/symbol_profiles/082/082640.json", "manifest_max_date": "2026-02-20", "entry_rule": "next_trading_day_or_same_day_after_historical_evidence_timestamp", "forward_window_status": "pass_180D", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "promotion_usable_without_url_repair": false, "source_proxy_only": true, "evidence_url_pending": true, "evidence_urls": ["https://www.fsc.go.kr/eng/pr010101/81778", "https://kiri.or.kr/eng/pdf/Korean_Insurance_Industry_2024.pdf", "https://www.kimchang.com/en/insights/detail.kc?idx=30965&sch_section=4", "https://eng.koreanre.com/sub.asp?exec=view&intCategory=0&intPage=1&intSeq=1723&maincode=501&strBoardID=kui_575&strSearchCategory=%7Cs_name%7Cs_subject%7C&strSearchWord=&sub_sequence=519&sub_sub_sequence=575"], "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_RESERVE:082640:Stage4B:2024-08-16", "dedupe_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|082640|Stage4B|2024-08-16|transaction_policy_label_failure_high_mae", "hard_duplicate_check": "pass_new_within_local_session_for_C22", "representative_for_aggregate": true, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "score_return_alignment": "false_positive_or_high_MAE_guardrail", "current_profile_error_type": "local_4B_or_4C_needed", "local_4b_watch_candidate": true, "hard_4c_review_candidate": true, "green_unlock_candidate": false}
{"code": "000400", "name": "롯데손해보험", "trigger_date": "2024-02-01", "requested_entry": "2024-02-02", "trigger_type": "Stage4B", "case_label": "counterexample", "evidence_family": "small_insurer_mna_price_spike_high_mae_guard", "thesis": "M&A/정책 label spike는 90D MFE가 컸지만 bridge가 얇아 180D MAE가 확대된 사례. Positive 승격이 아니라 local 4B watch로 남겨야 한다.", "entry_date": "2024-02-02", "entry_price": 2630.0, "MFE_30D_pct": 39.54, "MAE_30D_pct": -3.8, "peak_30D_date": "2024-02-16", "trough_30D_date": "2024-02-07", "MFE_90D_pct": 53.42, "MAE_90D_pct": -3.8, "peak_90D_date": "2024-04-25", "trough_90D_date": "2024-02-07", "MFE_180D_pct": 55.51, "MAE_180D_pct": -18.25, "peak_180D_date": "2024-06-26", "trough_180D_date": "2024-10-25", "current_profile_error": true, "simulated_total_after_shadow": 58, "shadow_result": "local_4B_watch_not_positive", "case_id": "C22-R6-L100-08-000400", "ticker": "000400", "symbol": "000400", "row_type": "trigger", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "deep_sub_archetype_id": "C22_DEEP_NONLIFE_LIFE_REINSURANCE_CSM_KICS_DISCOUNT_RATE_RESERVE_VS_VALUEUP_LABEL_SPIKE", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "manifest_max_date": "2026-02-20", "entry_rule": "next_trading_day_or_same_day_after_historical_evidence_timestamp", "forward_window_status": "pass_180D", "window_180D_corporate_action_contaminated": false, "calibration_usable": true, "promotion_usable_without_url_repair": false, "source_proxy_only": true, "evidence_url_pending": true, "evidence_urls": ["https://www.fsc.go.kr/eng/pr010101/81778", "https://kiri.or.kr/eng/pdf/Korean_Insurance_Industry_2024.pdf", "https://www.kimchang.com/en/insights/detail.kc?idx=30965&sch_section=4", "https://eng.koreanre.com/sub.asp?exec=view&intCategory=0&intPage=1&intSeq=1723&maincode=501&strBoardID=kui_575&strSearchCategory=%7Cs_name%7Cs_subject%7C&strSearchWord=&sub_sequence=519&sub_sub_sequence=575"], "same_entry_group_id": "C22_INSURANCE_RATE_CYCLE_RESERVE:000400:Stage4B:2024-02-02", "dedupe_key": "C22_INSURANCE_RATE_CYCLE_RESERVE|000400|Stage4B|2024-02-02|small_insurer_mna_price_spike_high_mae_guard", "hard_duplicate_check": "pass_new_within_local_session_for_C22", "representative_for_aggregate": true, "MFE_1Y_pct": null, "MAE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_2Y_pct": null, "score_return_alignment": "false_positive_or_high_MAE_guardrail", "current_profile_error_type": "local_4B_or_4C_needed", "local_4b_watch_candidate": true, "hard_4c_review_candidate": false, "green_unlock_candidate": false}
{"row_type": "score_simulation", "case_id": "C22-R6-L100-01-005830", "symbol": "005830", "profile_reference": "e2r_2_1_stock_web_calibrated_current_proxy", "raw_component_score_breakdown": {"contract_score": 55, "backlog_visibility_score": 35, "margin_bridge_score": 82, "revision_score": 66, "relative_strength_score": 76, "customer_quality_score": 70, "policy_or_regulatory_score": 72, "valuation_repricing_score": 70, "execution_risk_score": 28, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 28}, "baseline_total_proxy": 78, "shadow_total_proxy": 84, "shadow_result": "keep_or_upgrade_with_bridge", "score_return_alignment": "aligned_positive", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C22-R6-L100-02-000810", "symbol": "000810", "profile_reference": "e2r_2_1_stock_web_calibrated_current_proxy", "raw_component_score_breakdown": {"contract_score": 55, "backlog_visibility_score": 35, "margin_bridge_score": 82, "revision_score": 66, "relative_strength_score": 76, "customer_quality_score": 70, "policy_or_regulatory_score": 72, "valuation_repricing_score": 70, "execution_risk_score": 28, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 28}, "baseline_total_proxy": 78, "shadow_total_proxy": 86, "shadow_result": "keep_yellow_with_bridge", "score_return_alignment": "aligned_positive", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C22-R6-L100-03-032830", "symbol": "032830", "profile_reference": "e2r_2_1_stock_web_calibrated_current_proxy", "raw_component_score_breakdown": {"contract_score": 55, "backlog_visibility_score": 35, "margin_bridge_score": 82, "revision_score": 66, "relative_strength_score": 76, "customer_quality_score": 70, "policy_or_regulatory_score": 72, "valuation_repricing_score": 70, "execution_risk_score": 28, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 28}, "baseline_total_proxy": 78, "shadow_total_proxy": 78, "shadow_result": "keep_yellow_but_require_capital_return_bridge", "score_return_alignment": "aligned_positive", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C22-R6-L100-04-085620", "symbol": "085620", "profile_reference": "e2r_2_1_stock_web_calibrated_current_proxy", "raw_component_score_breakdown": {"contract_score": 55, "backlog_visibility_score": 35, "margin_bridge_score": 82, "revision_score": 66, "relative_strength_score": 76, "customer_quality_score": 70, "policy_or_regulatory_score": 72, "valuation_repricing_score": 70, "execution_risk_score": 28, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 28}, "baseline_total_proxy": 78, "shadow_total_proxy": 77, "shadow_result": "keep_stage2_with_bridge", "score_return_alignment": "aligned_positive", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C22-R6-L100-05-001450", "symbol": "001450", "profile_reference": "e2r_2_1_stock_web_calibrated_current_proxy", "raw_component_score_breakdown": {"contract_score": 35, "backlog_visibility_score": 20, "margin_bridge_score": 48, "revision_score": 42, "relative_strength_score": 69, "customer_quality_score": 45, "policy_or_regulatory_score": 60, "valuation_repricing_score": 68, "execution_risk_score": 62, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 58}, "baseline_total_proxy": 74, "shadow_total_proxy": 64, "shadow_result": "downgrade_to_stage1_or_local_4B_watch", "score_return_alignment": "false_positive_or_high_MAE_guardrail", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C22-R6-L100-06-088350", "symbol": "088350", "profile_reference": "e2r_2_1_stock_web_calibrated_current_proxy", "raw_component_score_breakdown": {"contract_score": 35, "backlog_visibility_score": 20, "margin_bridge_score": 48, "revision_score": 42, "relative_strength_score": 69, "customer_quality_score": 45, "policy_or_regulatory_score": 60, "valuation_repricing_score": 68, "execution_risk_score": 62, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 58}, "baseline_total_proxy": 74, "shadow_total_proxy": 62, "shadow_result": "downgrade_to_stage1_or_local_4B_watch", "score_return_alignment": "false_positive_or_high_MAE_guardrail", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C22-R6-L100-07-082640", "symbol": "082640", "profile_reference": "e2r_2_1_stock_web_calibrated_current_proxy", "raw_component_score_breakdown": {"contract_score": 35, "backlog_visibility_score": 20, "margin_bridge_score": 48, "revision_score": 42, "relative_strength_score": 69, "customer_quality_score": 45, "policy_or_regulatory_score": 60, "valuation_repricing_score": 68, "execution_risk_score": 62, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 58}, "baseline_total_proxy": 74, "shadow_total_proxy": 55, "shadow_result": "route_to_hard_4C_review", "score_return_alignment": "false_positive_or_high_MAE_guardrail", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "production_scoring_changed": false}
{"row_type": "score_simulation", "case_id": "C22-R6-L100-08-000400", "symbol": "000400", "profile_reference": "e2r_2_1_stock_web_calibrated_current_proxy", "raw_component_score_breakdown": {"contract_score": 35, "backlog_visibility_score": 20, "margin_bridge_score": 48, "revision_score": 42, "relative_strength_score": 69, "customer_quality_score": 45, "policy_or_regulatory_score": 60, "valuation_repricing_score": 68, "execution_risk_score": 62, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 58}, "baseline_total_proxy": 74, "shadow_total_proxy": 58, "shadow_result": "local_4B_watch_not_positive", "score_return_alignment": "false_positive_or_high_MAE_guardrail", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "production_scoring_changed": false}
{"row_type": "residual_contribution", "case_id": "C22-R6-L100-01-005830", "symbol": "005830", "case_label": "positive", "residual_error_type": "none", "guardrail_candidate": "C22_bridge_required_or_local_4B_watch", "new_axis_proposed": "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_proxy_only": true, "promotion_blocked_until_url_repair": true}
{"row_type": "residual_contribution", "case_id": "C22-R6-L100-02-000810", "symbol": "000810", "case_label": "positive", "residual_error_type": "none", "guardrail_candidate": "C22_bridge_required_or_local_4B_watch", "new_axis_proposed": "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_proxy_only": true, "promotion_blocked_until_url_repair": true}
{"row_type": "residual_contribution", "case_id": "C22-R6-L100-03-032830", "symbol": "032830", "case_label": "positive", "residual_error_type": "false_positive_or_bridge_missing", "guardrail_candidate": "C22_bridge_required_or_local_4B_watch", "new_axis_proposed": "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_proxy_only": true, "promotion_blocked_until_url_repair": true}
{"row_type": "residual_contribution", "case_id": "C22-R6-L100-04-085620", "symbol": "085620", "case_label": "positive", "residual_error_type": "none", "guardrail_candidate": "C22_bridge_required_or_local_4B_watch", "new_axis_proposed": "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_proxy_only": true, "promotion_blocked_until_url_repair": true}
{"row_type": "residual_contribution", "case_id": "C22-R6-L100-05-001450", "symbol": "001450", "case_label": "counterexample", "residual_error_type": "false_positive_or_bridge_missing", "guardrail_candidate": "C22_bridge_required_or_local_4B_watch", "new_axis_proposed": "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_proxy_only": true, "promotion_blocked_until_url_repair": true}
{"row_type": "residual_contribution", "case_id": "C22-R6-L100-06-088350", "symbol": "088350", "case_label": "counterexample", "residual_error_type": "false_positive_or_bridge_missing", "guardrail_candidate": "C22_bridge_required_or_local_4B_watch", "new_axis_proposed": "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_proxy_only": true, "promotion_blocked_until_url_repair": true}
{"row_type": "residual_contribution", "case_id": "C22-R6-L100-07-082640", "symbol": "082640", "case_label": "counterexample", "residual_error_type": "local_4B_or_4C_needed", "guardrail_candidate": "C22_bridge_required_or_local_4B_watch", "new_axis_proposed": "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_proxy_only": true, "promotion_blocked_until_url_repair": true}
{"row_type": "residual_contribution", "case_id": "C22-R6-L100-08-000400", "symbol": "000400", "case_label": "counterexample", "residual_error_type": "local_4B_or_4C_needed", "guardrail_candidate": "C22_bridge_required_or_local_4B_watch", "new_axis_proposed": "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "source_proxy_only": true, "promotion_blocked_until_url_repair": true}
{"row_type": "residual_contribution", "selected_round": "R6", "selected_loop": 100, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "C22_IFRS17_CSM_KICS_RATE_CYCLE_RESERVE_CAPITAL_RETURN_BRIDGE", "new_independent_case_count": 8, "reused_case_count": 0, "same_archetype_new_symbol_count": 8, "same_archetype_new_trigger_family_count": 8, "calibration_usable_trigger_count": 8, "representative_trigger_count": 8, "positive_case_count": 4, "counterexample_count": 4, "stage4b_case_count": 2, "stage4c_case_count": 1, "current_profile_error_count": 5, "source_proxy_only_count": 8, "evidence_url_pending_count": 8, "avg_MFE_90D_pct": 23.55, "avg_MAE_90D_pct": -15.92, "avg_positive_MFE_90D_pct": 28.87, "avg_counterexample_MAE_90D_pct": -24.36, "new_axis_proposed": "C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_when_only_generic_rate_or_valueup_label_is_present", "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "do_not_propose_new_weight_delta": false, "promotion_blocked_until_url_repair": true}
```

## 26. Deferred Coding Agent Handoff Prompt

```text
You are a later batch implementation agent for Songdaiki/stock_agent. Do not execute this handoff inside the research session that generated it.

Read this MD as one C22_INSURANCE_RATE_CYCLE_RESERVE residual calibration artifact. Parse the price_source_validation, case, trigger, score_simulation, residual_contribution, and shadow_weight rows. If rows pass v12 validation gates, add this artifact to the next calibration batch and consider only a scope-limited shadow patch.

Scope:
- large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
- canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE

Candidate axis:
- C22_verified_CSM_KICS_rate_reserve_capital_return_bridge_required_before_Yellow_or_Green_plus_valueup_or_IFRS17_label_to_local_4B_watch

Rules:
- Do not change global Stage3-Green thresholds.
- Do not loosen stage3_green_revision_min.
- Do not promote value-up label-only, IFRS17 label-only, K-ICS label-only, or M&A label-only insurance cases.
- Preserve quality underwriting / reserve / capital-return positives.
- Route label-only high-MAE cases to local 4B watch or hard 4C review only when reserve/capital-return bridge is absent.
- Keep promotion blocked for source_proxy_only rows until company-level URL repair is complete.
```

## 27. Next Round State

```text
completed_round = R6
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C24_BIO_TRIAL_DATA_EVENT_RISK, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C19_BRAND_RETAIL_INVENTORY_MARGIN, C22_INSURANCE_RATE_CYCLE_RESERVE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
STOCK_WEB_MANIFEST = https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
FSC_VALUE_UP_CONTEXT = https://www.fsc.go.kr/eng/pr010101/81778
KIRI_INSURANCE_INDUSTRY_2024 = https://kiri.or.kr/eng/pdf/Korean_Insurance_Industry_2024.pdf
IFRS17_REFORM_CONTEXT = https://www.kimchang.com/en/insights/detail.kc?idx=30965&sch_section=4
KOREAN_RE_IFRS17_TRANSITION_CONTEXT = https://eng.koreanre.com/sub.asp?exec=view&intCategory=0&intPage=1&intSeq=1723&maincode=501&strBoardID=kui_575&strSearchCategory=%7Cs_name%7Cs_subject%7C&strSearchWord=&sub_sequence=519&sub_sub_sequence=575
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 8
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
source_proxy_only_count: 8
evidence_url_pending_count: 8
promotion_blocked_until_url_repair: true
ready_for_batch_ingest: true
```
