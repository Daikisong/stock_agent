# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
scheduled_round: R3
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD
loop_objective:
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

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

The research question is not whether Stage2 is earlier than Green. It is whether C12 battery-material cases need a separate customer-conversion / call-off guard that distinguishes real customer-qualified capacity from theme-only battery exposure.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R3`
- scheduled_loop: `74`
- large_sector_id: `L3_BATTERY_EV_GREEN_MOBILITY`
- canonical_archetype_id: `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`
- fine_archetype_id: `ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD`
- valid round-sector pair: `R3 -> L3_BATTERY_EV_GREEN_MOBILITY`

## 3. Previous Coverage / Duplicate Avoidance Check

The no-repeat index showed C12 as a covered but still useful archetype: 53 rows / 17 symbols, with top-covered symbols concentrated in 393890, 361610, 011790, 336370, 006110. This loop avoids those top repeated C12 symbols and uses four different symbols:

| symbol | company | novelty reason |
|---|---|---|
| 348370 | 엔켐 | C12 electrolyte customer/capacity success path, not just C11 orderbook rerating |
| 020150 | 롯데에너지머티리얼즈 | copper-foil utilization recovery / call-off reversal path |
| 278280 | 천보 | electrolyte exposure without conversion; call-off counterexample |
| 121600 | 나노신소재 | CNT theme spike with later high-MAE counterexample |

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Schema check:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

## 5. Historical Eligibility Gate

|symbol|entry|entry_in_tradable|forward_180D|corp_action_window|calibration_usable|
|---|---|---|---|---|---|
|348370|2024-01-03|true|true|clean_180D_window; corporate_action_candidate_count=0|true|
|020150|2024-03-20|true|true|clean_180D_window; corporate_action_candidate_count=0|true|
|278280|2024-01-03|true|true|clean_180D_window; corporate_action_candidate_count=0|true|
|121600|2024-02-21|true|true|clean_180D_window; 2015-12-17 corporate-action candidate outside calibration window|true|

## 6. Canonical Archetype Compression Map

```text
fine_archetype = ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
compression_logic =
  battery material exposure alone is not enough;
  usable promotion requires customer-quality or capacity/utilization conversion evidence;
  absent those, high relative strength is treated as a call-off-risk watch or 4B/4C overlay.
```

## 7. Case Selection Summary

|case_id|symbol|name|trigger|entry|entry_price|MFE90|MAE90|MFE180|MAE180|outcome|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R3L74_C12_348370_20240103|348370|엔켐|Stage2-Actionable|2024-01-03|84600|366.31|-6.86|366.31|-6.86|positive_structural_success_with_later_4B_blowoff|current_profile_correct|
|R3L74_C12_020150_20240320|020150|롯데에너지머티리얼즈|Stage2-Actionable|2024-03-20|42350|39.79|-14.29|39.79|-27.98|high_mae_success_after_missed_structural_reversal|current_profile_missed_structural|
|R3L74_C12_278280_20240103|278280|천보|Stage2-FalsePositive|2024-01-03|104800|4.1|-32.16|4.1|-53.24|failed_rerating_call_off_counterexample|current_profile_correct|
|R3L74_C12_121600_20240221|121600|나노신소재|Stage3-Yellow-FalsePositive|2024-02-21|134000|17.76|-25.22|17.76|-48.88|false_positive_green_high_mae_after_initial_spike|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 4
4C_case_count = 2
calibration_usable_case_count = 4
minimum_new_independent_case_ratio = 1.00
```

Positive cases:
- `348370` showed extreme MFE with tolerable initial MAE, but required a 4B overlay after the April valuation blowoff.
- `020150` showed a cleaner March recovery trigger with strong 90D MFE, but later 180D drawdown warns against holding after utilization/margin evidence stalls.

Counterexamples:
- `278280` had theme exposure but no customer-conversion proof; low MFE and deep MAE support blocking theme-only Stage2.
- `121600` had high initial MFE but later severe MAE; it should not become Green without durable customer/call-off protection evidence.

## 9. Evidence Source Map

| symbol | stage2 evidence family | stage3 evidence family | 4B/4C evidence family | evidence_source_status |
|---|---|---|---|---|
| 348370 | customer quality, capacity route, IRA optionality | financial visibility watch | valuation blowoff | source_proxy_only / URL pending |
| 020150 | capacity recovery, customer qualification, early revision | financial visibility watch | margin/backlog slowdown | source_proxy_only / URL pending |
| 278280 | battery-material exposure only | none | call-off / thesis break | source_proxy_only / URL pending |
| 121600 | relative strength, CNT capacity route | weak multi-source narrative | valuation spike then call-off risk | source_proxy_only / URL pending |

## 10. Price Data Source Map

|symbol|price_shard_path|profile_path|basis|adjustment|
|---|---|---|---|---|
|348370|atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv|atlas/symbol_profiles/348/348370.json|tradable_raw|raw_unadjusted_marcap|
|020150|atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv|atlas/symbol_profiles/020/020150.json|tradable_raw|raw_unadjusted_marcap|
|278280|atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv|atlas/symbol_profiles/278/278280.json|tradable_raw|raw_unadjusted_marcap|
|121600|atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv|atlas/symbol_profiles/121/121600.json|tradable_raw|raw_unadjusted_marcap|

## 11. Case-by-Case Trigger Grid

|case_id|symbol|name|trigger|entry|entry_price|MFE90|MAE90|MFE180|MAE180|outcome|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R3L74_C12_348370_20240103|348370|엔켐|Stage2-Actionable|2024-01-03|84600|366.31|-6.86|366.31|-6.86|positive_structural_success_with_later_4B_blowoff|current_profile_correct|
|R3L74_C12_020150_20240320|020150|롯데에너지머티리얼즈|Stage2-Actionable|2024-03-20|42350|39.79|-14.29|39.79|-27.98|high_mae_success_after_missed_structural_reversal|current_profile_missed_structural|
|R3L74_C12_278280_20240103|278280|천보|Stage2-FalsePositive|2024-01-03|104800|4.1|-32.16|4.1|-53.24|failed_rerating_call_off_counterexample|current_profile_correct|
|R3L74_C12_121600_20240221|121600|나노신소재|Stage3-Yellow-FalsePositive|2024-02-21|134000|17.76|-25.22|17.76|-48.88|false_positive_green_high_mae_after_initial_spike|current_profile_false_positive|

## 12. Trigger-Level OHLC Backtest Tables

|symbol|entry|price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak|dd_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|
|348370|2024-01-03|84600|252.25|-6.86|366.31|-6.86|366.31|-6.86|2024-04-08/394500|-62.23|
|020150|2024-03-20|42350|23.73|-5.67|39.79|-14.29|39.79|-27.98|2024-06-18/59200|-48.48|
|278280|2024-01-03|104800|4.1|-22.71|4.1|-32.16|4.1|-53.24|2024-01-03/109100|-55.09|
|121600|2024-02-21|134000|17.76|-7.61|17.76|-25.22|17.76|-48.88|2024-02-22/157800|-56.59|

## 13. Current Calibrated Profile Stress Test

| symbol | current profile behavior | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| 348370 | Allows Stage2/Yelllow because non-price capacity/customer route exists; blocks price-only 4B until non-price risk appears. | Correct: very strong MFE, tolerable initial MAE, later blowoff overlay needed. | current_profile_correct |
| 020150 | Too slow to treat copper-foil utilization recovery as C12 reversal. | Missed 90D MFE +39.79% from March trigger, although 180D MAE warns against late holding. | current_profile_missed_structural |
| 278280 | Blocks exposure-only promotion because customer/order conversion is weak. | Correct: MFE180 only +4.10%, MAE180 -53.24%. | current_profile_correct |
| 121600 | Yellow-like response can be over-credited if relative strength substitutes for customer conversion. | False positive risk: MFE30 +17.76%, but MAE180 -48.88%. | current_profile_false_positive |

Answers to the calibrated-axis stress questions:

```text
stage2_actionable_evidence_bonus: kept, but must require customer/capacity conversion in C12.
yellow_threshold_75: kept; C12 needs a quality guard, not a lower threshold.
green_threshold_87 / revision_55: kept; weak customer quality should cap Green.
price_only_blowoff_guard: strengthened for C12.
full_4b_requires_non_price_evidence: strengthened; 348370/020150 need full-window 4B only when valuation + utilization/margin risk appears.
hard_4c_routing: kept; 278280 and 121600 are useful 4C/watch examples.
```

## 14. Stage2 / Yellow / Green Comparison

`green_lateness_ratio` is marked not_applicable for this MD because no separate confirmed Stage3-Green trigger is used as a representative aggregate row. The useful comparison is Stage2/Yelllow admissibility versus later 4B/4C overlay.

```text
348370: Stage2/Yelllow acceptable; 4B overlay after valuation blowoff.
020150: Stage2-Actionable reversal acceptable; Green still requires confirmed revision.
278280: Stage2 promotion blocked; exposure-only signal fails.
121600: Yellow must be capped; relative strength alone produces high-MAE false positive.
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B date | 4B evidence type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---|---:|---:|---|
| 348370 | 2024-04-08 | valuation_blowoff, positioning_overheat | 0.884 | 0.884 | good_full_window_4B_timing |
| 020150 | 2024-06-18 | margin_or_backlog_slowdown, positioning_overheat | 0.887 | 0.887 | good_full_window_4B_timing |
| 278280 | 2024-01-03 | price_only, margin_or_backlog_slowdown | 0.000 | 0.000 | 4C/watch, not full positive 4B |
| 121600 | 2024-02-22 | valuation_blowoff, positioning_overheat | 0.174 | 0.174 | early spike; later 4C needed |

## 16. 4C Protection Audit

| symbol | 4C label | protection interpretation |
|---|---|---|
| 348370 | thesis_break_watch_only | 4B captured overheat; hard 4C not required inside 180D entry calibration. |
| 020150 | thesis_break_watch_only | 4B after June peak would have reduced later MAE; hard 4C should wait for utilization thesis break. |
| 278280 | hard_4c_success | Weak customer conversion and low MFE support thesis-break protection. |
| 121600 | hard_4c_late | 4C after the August drawdown would be late; C12 guard should cap promotion earlier. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L3_battery_material_customer_conversion_guard
candidate =
  In L3 battery-material names, Stage2-Actionable may remain valid only when at least two of:
  customer_quality, capacity/utilization route, policy/IRA optionality, financial visibility
  are non-price supported.
effect =
  keeps 348370 and 020150;
  blocks or caps 278280 and 121600;
  does not change global profile.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
candidate =
  if customer_quality_score <= 4 and call_off_risk_guard_score >= 6:
      cap at Stage2-Watch or Stage3-Yellow-watch;
      require confirmed_revision or customer conversion before Green.
```

## 19. Before / After Backtest Comparison

| profile | scope | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 | current calibrated proxy | 106.99 | -19.63 | 106.99 | -34.24 | 0.50 | mixed |
| P0b | baseline reference | 106.99 | -19.63 | 106.99 | -34.24 | 0.75 | worse |
| P1 | sector candidate | 110.05 | -11.58 | 101.55 | -34.28 | 0.25 | better sector separation |
| P2 | canonical candidate | 110.05 | -11.58 | 101.55 | -34.28 | 0.25 | best C12 candidate |
| P3 | counterexample guard | 203.05 | -10.58 | 203.05 | -17.42 | 0.00 | conservative; may miss 020150 |

## 20. Score-Return Alignment Matrix

|symbol|score_before|stage_before|score_after|stage_after|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|---|
|348370|84|Stage3-Yellow|86|Stage3-Yellow / Green-watch|366.31|-6.86|strong positive MFE with tolerable initial MAE; later valuation blowoff needs 4B overlay|
|020150|72|Stage2-Actionable|76|Stage3-Yellow|39.79|-14.29|90D MFE was strong, but 180D MAE after the peak shows the need for a 4B/4C overlay when utilization evidence stalls.|
|278280|58|Stage2-Watch|52|Blocked / 4C-watch|4.1|-32.16|low MFE and deep MAE confirm that exposure-only Stage2 must be blocked unless customer/order conversion is visible.|
|121600|76|Stage3-Yellow|68|Stage2-Watch / Green-blocked|17.76|-25.22|initial MFE was acceptable but later 180D drawdown shows that weak customer conversion should not reach Green.|

## 21. Coverage Matrix

```json
{
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD",
  "positive_case_count": 2,
  "counterexample_count": 2,
  "4B_case_count": 4,
  "4C_case_count": 2,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "calibration_usable_trigger_count": 4,
  "representative_trigger_count": 4,
  "current_profile_error_count": 2,
  "sector_rule_candidate": true,
  "canonical_rule_candidate": true,
  "coverage_gap_after_this_loop": "C12 gets four new symbols/failure modes focused on customer call-off rather than broad C11 orderbook beta."
}
```

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_false_positive
  - high_MAE_after_initial_MFE
new_axis_proposed:
  - c12_customer_conversion_min_evidence_family_count
  - c12_call_off_guard_for_weak_customer_quality
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Actual stock-web tradable_raw OHLC rows were used for entry price, MFE, MAE, peak and drawdown calculations.
- 180D windows are clean from corporate-action contamination according to symbol profiles.
- Same-entry groups are deduplicated; each case has one representative trigger.

Not validated:
- This MD does not patch `stock_agent`.
- This MD does not run live scans.
- This MD uses `source_proxy_only` evidence narratives; the implementation batch must replace these with DART/KRX/company IR URL-backed evidence before any promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c12_customer_conversion_min_evidence_family_count,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,1,2,+1,"Theme-only battery exposure had low MFE or high MAE; customer/capacity conversion separated Enchem and Lotte Energy Materials from Chunbo/Nano counterexamples.","Improves false-positive blocking while keeping two positive 90D MFE cases.","T_R3L74_C12_348370_20240103|T_R3L74_C12_020150_20240320|T_R3L74_C12_278280_20240103|T_R3L74_C12_121600_20240221",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c12_call_off_guard_for_weak_customer_quality,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"When customer quality <=4 and call-off risk >=6, Stage3-Yellow/Green should be capped unless confirmed revision exists.","Would have capped 121600 and blocked 278280 without suppressing 348370.","T_R3L74_C12_278280_20240103|T_R3L74_C12_121600_20240221",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L74_C12_348370_20240103", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong positive MFE with tolerable initial MAE; later valuation blowoff needs 4B overlay", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "first_date=2021-11-01; last_date=2026-02-20; trading_day_count=1053; row_status tradable=1053; no corporate-action candidates."}
{"row_type": "case", "case_id": "R3L74_C12_020150_20240320", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "90D MFE was strong, but 180D MAE after the peak shows the need for a 4B/4C overlay when utilization evidence stalls.", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "first_date=2011-03-04; last_date=2026-02-20; trading_day_count=3681; no corporate-action candidates."}
{"row_type": "case", "case_id": "R3L74_C12_278280_20240103", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low MFE and deep MAE confirm that exposure-only Stage2 must be blocked unless customer/order conversion is visible.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "first_date=2019-02-11; last_date=2026-02-20; trading_day_count=1727; no corporate-action candidates."}
{"row_type": "case", "case_id": "R3L74_C12_121600_20240221", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "Stage3-Yellow-FalsePositive", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "initial MFE was acceptable but later 180D drawdown shows that weak customer conversion should not reach Green.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "first_date=2011-02-09; last_date=2026-02-20; trading_day_count=3697; one old corporate-action candidate on 2015-12-17, not in 2024 forward windows."}
{"row_type": "trigger", "trigger_id": "T_R3L74_C12_348370_20240103", "case_id": "R3L74_C12_348370_20240103", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD", "sector": "2차전지 전해액", "primary_archetype": "battery_customer_contract_call_off_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 84600, "evidence_available_at_that_date": "US electrolyte supply-chain localization, customer-proximity capacity route, and IRA optionality were already part of the public thesis; the key distinction was non-price capacity/customer visibility rather than simple EV-theme beta.", "evidence_source": "source_proxy_only: stock-web price path + public business narrative; evidence URL verification deferred to implementation batch", "stage2_evidence_fields": ["customer_or_order_quality", "capacity_or_volume_route", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv", "profile_path": "atlas/symbol_profiles/348/348370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 252.25, "MFE_90D_pct": 366.31, "MFE_180D_pct": 366.31, "MFE_1Y_pct": "not_calculated_scope_180D_primary", "MFE_2Y_pct": "not_calculated_scope_180D_primary", "MAE_30D_pct": -6.86, "MAE_90D_pct": -6.86, "MAE_180D_pct": -6.86, "MAE_1Y_pct": "not_calculated_scope_180D_primary", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 394500, "drawdown_after_peak_pct": -62.23, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.882, "four_b_full_window_peak_proximity": 0.882, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_structural_success_with_later_4B_blowoff", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; corporate_action_candidate_count=0", "same_entry_group_id": "R3L74_C12_348370_20240103_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R3L74_C12_020150_20240320", "case_id": "R3L74_C12_020150_20240320", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD", "sector": "2차전지 동박", "primary_archetype": "battery_customer_contract_call_off_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 42350, "evidence_available_at_that_date": "Copper-foil recovery was not a clean battery beta; the usable signal was customer qualification / utilization recovery after a washed-out inventory cycle. The March trigger is treated as a call-off-risk reversal candidate, not as a broad EV demand rebound.", "evidence_source": "source_proxy_only: stock-web price path + public business narrative; evidence URL verification deferred to implementation batch", "stage2_evidence_fields": ["capacity_or_volume_route", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["call_off_or_order_cut"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.73, "MFE_90D_pct": 39.79, "MFE_180D_pct": 39.79, "MFE_1Y_pct": "not_calculated_scope_180D_primary", "MFE_2Y_pct": "not_calculated_scope_180D_primary", "MAE_30D_pct": -5.67, "MAE_90D_pct": -14.29, "MAE_180D_pct": -27.98, "MAE_1Y_pct": "not_calculated_scope_180D_primary", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 59200, "drawdown_after_peak_pct": -48.48, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.887, "four_b_full_window_peak_proximity": 0.887, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success_after_missed_structural_reversal", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; corporate_action_candidate_count=0", "same_entry_group_id": "R3L74_C12_020150_20240320_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R3L74_C12_278280_20240103", "case_id": "R3L74_C12_278280_20240103", "symbol": "278280", "company_name": "천보", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD", "sector": "2차전지 전해질/첨가제", "primary_archetype": "battery_customer_contract_call_off_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-03", "entry_date": "2024-01-03", "entry_price": 104800, "evidence_available_at_that_date": "Electrolyte material exposure existed, but the trigger lacked customer conversion, take-or-pay visibility, and margin recovery. This is a call-off-risk counterexample where theme exposure did not equal orderbook rerating.", "evidence_source": "source_proxy_only: stock-web price path + public business narrative; evidence URL verification deferred to implementation batch", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv", "profile_path": "atlas/symbol_profiles/278/278280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.1, "MFE_90D_pct": 4.1, "MFE_180D_pct": 4.1, "MFE_1Y_pct": "not_calculated_scope_180D_primary", "MFE_2Y_pct": "not_calculated_scope_180D_primary", "MAE_30D_pct": -22.71, "MAE_90D_pct": -32.16, "MAE_180D_pct": -53.24, "MAE_1Y_pct": "not_calculated_scope_180D_primary", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-03", "peak_price": 109100, "drawdown_after_peak_pct": -55.09, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "4B_or_4C_risk_confirmed_after_weak_entry", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating_call_off_counterexample", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; corporate_action_candidate_count=0", "same_entry_group_id": "R3L74_C12_278280_20240103_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_R3L74_C12_121600_20240221", "case_id": "R3L74_C12_121600_20240221", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "ELECTROLYTE_COPPER_FOIL_CNT_CUSTOMER_CALL_OFF_GUARD", "sector": "CNT 도전재/배터리 소재", "primary_archetype": "battery_customer_contract_call_off_risk", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining", "trigger_type": "Stage3-Yellow-FalsePositive", "trigger_date": "2024-02-21", "entry_date": "2024-02-21", "entry_price": 134000, "evidence_available_at_that_date": "CNT conductive-additive rerating showed strong price response, but public trigger evidence still did not prove durable customer call-off protection. This is a high initial MFE / later MAE counterexample.", "evidence_source": "source_proxy_only: stock-web price path + public business narrative; evidence URL verification deferred to implementation batch", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv", "profile_path": "atlas/symbol_profiles/121/121600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.76, "MFE_90D_pct": 17.76, "MFE_180D_pct": 17.76, "MFE_1Y_pct": "not_calculated_scope_180D_primary", "MFE_2Y_pct": "not_calculated_scope_180D_primary", "MAE_30D_pct": -7.61, "MAE_90D_pct": -25.22, "MAE_180D_pct": -48.88, "MAE_1Y_pct": "not_calculated_scope_180D_primary", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-22", "peak_price": 157800, "drawdown_after_peak_pct": -56.59, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.168, "four_b_full_window_peak_proximity": 0.168, "four_b_timing_verdict": "4B_or_4C_risk_confirmed_after_weak_entry", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "false_positive_green_high_mae_after_initial_spike", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2015-12-17 corporate-action candidate outside calibration window", "same_entry_group_id": "R3L74_C12_121600_20240221_G1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L74_C12_348370_20240103", "trigger_id": "T_R3L74_C12_348370_20240103", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 7, "relative_strength_score": 12, "customer_quality_score": 11, "policy_or_regulatory_score": 9, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 2, "accounting_trust_risk_score": 1, "capacity_or_shipment_score": 10, "call_off_risk_guard_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 7, "relative_strength_score": 12, "customer_quality_score": 12, "policy_or_regulatory_score": 9, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 2, "accounting_trust_risk_score": 1, "capacity_or_shipment_score": 12, "call_off_risk_guard_score": 1}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow / Green-watch", "changed_components": ["customer_quality_score", "capacity_or_shipment_score", "call_off_risk_guard_score"], "component_delta_explanation": "C12 shadow test: distinguish contracted/customer-qualified capacity from theme-only battery exposure; raise call-off guard when customer conversion and margin bridge are weak.", "MFE_90D_pct": 366.31, "MAE_90D_pct": -6.86, "score_return_alignment_label": "strong positive MFE with tolerable initial MAE; later valuation blowoff needs 4B overlay", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L74_C12_020150_20240320", "trigger_id": "T_R3L74_C12_020150_20240320", "symbol": "020150", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 6, "policy_or_regulatory_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 6, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1, "capacity_or_shipment_score": 7, "call_off_risk_guard_score": 5}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 7, "policy_or_regulatory_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 6, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1, "capacity_or_shipment_score": 9, "call_off_risk_guard_score": 4}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "capacity_or_shipment_score", "call_off_risk_guard_score"], "component_delta_explanation": "C12 shadow test: distinguish contracted/customer-qualified capacity from theme-only battery exposure; raise call-off guard when customer conversion and margin bridge are weak.", "MFE_90D_pct": 39.79, "MAE_90D_pct": -14.29, "score_return_alignment_label": "90D MFE was strong, but 180D MAE after the peak shows the need for a 4B/4C overlay when utilization evidence stalls.", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L74_C12_278280_20240103", "trigger_id": "T_R3L74_C12_278280_20240103", "symbol": "278280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 1, "customer_quality_score": 1, "policy_or_regulatory_score": 2, "valuation_repricing_score": 1, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1, "capacity_or_shipment_score": 1, "call_off_risk_guard_score": 9}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 1, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 1, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1, "capacity_or_shipment_score": 0, "call_off_risk_guard_score": 11}, "weighted_score_after": 52, "stage_label_after": "Blocked / 4C-watch", "changed_components": ["customer_quality_score", "capacity_or_shipment_score", "call_off_risk_guard_score"], "component_delta_explanation": "C12 shadow test: distinguish contracted/customer-qualified capacity from theme-only battery exposure; raise call-off guard when customer conversion and margin bridge are weak.", "MFE_90D_pct": 4.1, "MAE_90D_pct": -32.16, "score_return_alignment_label": "low MFE and deep MAE confirm that exposure-only Stage2 must be blocked unless customer/order conversion is visible.", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L74_C12_121600_20240221", "trigger_id": "T_R3L74_C12_121600_20240221", "symbol": "121600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 11, "customer_quality_score": 4, "policy_or_regulatory_score": 4, "valuation_repricing_score": 7, "execution_risk_score": 5, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1, "capacity_or_shipment_score": 6, "call_off_risk_guard_score": 6}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 11, "customer_quality_score": 2, "policy_or_regulatory_score": 4, "valuation_repricing_score": 7, "execution_risk_score": 5, "legal_or_contract_risk_score": 1, "dilution_cb_risk_score": 1, "accounting_trust_risk_score": 1, "capacity_or_shipment_score": 5, "call_off_risk_guard_score": 9}, "weighted_score_after": 68, "stage_label_after": "Stage2-Watch / Green-blocked", "changed_components": ["customer_quality_score", "capacity_or_shipment_score", "call_off_risk_guard_score"], "component_delta_explanation": "C12 shadow test: distinguish contracted/customer-qualified capacity from theme-only battery exposure; raise call-off guard when customer conversion and margin bridge are weak.", "MFE_90D_pct": 17.76, "MAE_90D_pct": -25.22, "score_return_alignment_label": "initial MFE was acceptable but later 180D drawdown shows that weak customer conversion should not reach Green.", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_false_positive", "high_MAE_after_initial_MFE"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R3
completed_loop = 74
next_round = R4
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes


- Stock-web manifest was read from `atlas/manifest.json`: source_name=FinanceData/marcap, max_date=2026-02-20, tradable_row_count=14,354,401, price_adjustment_status=raw_unadjusted_marcap.
- Stock-web schema was read from `atlas/schema.json`: tradable shard columns are d/o/h/l/c/v/a/mc/s/m and MFE/MAE formulas are max-high/min-low over N tradable rows.
- Duplicate avoidance used `docs/core/V12_Research_No_Repeat_Index.md`. C12 coverage was listed as 53 rows / 17 symbols with top-covered symbols 393890, 361610, 011790, 336370, 006110. This loop deliberately used 348370, 020150, 278280, 121600 to reduce top-symbol repetition.
- Evidence text in this MD is marked `source_proxy_only`; implementation batch should replace proxy descriptions with DART/KRX/company IR URLs before promotion.


