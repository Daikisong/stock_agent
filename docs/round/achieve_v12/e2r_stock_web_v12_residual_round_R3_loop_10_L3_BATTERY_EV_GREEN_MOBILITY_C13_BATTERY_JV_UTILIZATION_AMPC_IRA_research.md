# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = IRA_AMPC_JV_UTILIZATION_CAPEX_PACE
output_file = e2r_stock_web_v12_residual_round_R3_loop_10_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **3 new independent cases**, **2 counterexamples**, and **2 residual errors** for `R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA`.

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

The applied global axes are treated as already-calibrated facts, not rediscovered findings. This MD stress-tests how those axes behave inside battery JV / utilization / AMPC cases.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R3
allowed_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
round_sector_consistency = pass
```

C13 is selected because the remaining R3 residual is not simply "battery orderbook good/bad." The useful split is whether IRA/AMPC and JV capacity are backed by near-term utilization, customer draw, capex pace, and margin bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts reviewed:

- `reports/e2r_calibration/ingest_summary.md`: R1~R13 and loops 1~9 are covered; therefore after the session-created R1/R2 loop10 outputs, this run uses R3 loop10.
- `reports/e2r_calibration/applied_scoring_diff.md`: global axes already applied; no global re-proposal.
- `data/e2r/calibration/md_registry.jsonl`: R3 previous loops exist and contain duplicated secondary-battery research patterns, so this run chooses a stricter C13 utilization/capex split.

Novelty check:

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
duplicate_low_value_loop = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

All quantitative rows use stock-web tradable shards only. Raw shards are not used for weight calibration.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | entry_date | 180D window | corporate action status | calibration_usable |
|---|---:|---|---:|---:|---|---:|
| R3L10-C13-373220-IRA-AMPC-20220817 | 373220 | atlas/symbol_profiles/373/373220.json | 2022-08-17 | available | clean_180D_window | true |
| R3L10-C13-006400-STELLANTIS-KOKOMO-20231012 | 006400 | atlas/symbol_profiles/006/006400.json | 2023-10-12 | available | clean_180D_window | true |
| R3L10-C13-373220-SLOW-EV-CAPEX-20240425 | 373220 | atlas/symbol_profiles/373/373220.json | 2024-04-25 | available | clean_180D_window | true |
| R3L10-C13-096770-SKON-EMERGENCY-20240708 | 096770 | atlas/symbol_profiles/096/096770.json | narrative only | blocked | corporate_action_candidate_date=2024-11-20 overlaps 180D | false |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA

fine_archetype compression:
- IRA_AMPC_US_CAPACITY_BRIDGE -> C13
- FUTURE_DATED_JV_CAPACITY_WITHOUT_UTILIZATION -> C13
- IRA_CREDIT_WITH_LOW_UTILIZATION_HIGH_MAE -> C13
- SKON_EV_DEMAND_SLOWDOWN_BALANCE_SHEET_STRESS -> C13 narrative-only guardrail
```

Compression rule:

```text
C13 should not score "subsidy/JV/capacity" as a single positive bucket.
It needs a four-part bridge:
1. policy subsidy or JV exists,
2. production/utilization date is near enough,
3. customer draw or order conversion is visible,
4. core margin/OP improves without relying only on AMPC accounting credit.
```

## 7. Case Selection Summary

| case_id | symbol | company | role | case_type | trigger | entry_date | MFE_90D | MAE_90D | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| R3L10-C13-373220-IRA-AMPC-20220817 | 373220 | LG에너지솔루션 | positive | structural_success | Stage2-Actionable | 2022-08-17 | 38.7 | -7.39 | current_profile_correct |
| R3L10-C13-006400-STELLANTIS-KOKOMO-20231012 | 006400 | 삼성SDI | counterexample | failed_rerating | Stage2-Headline-JV | 2023-10-12 | 0.75 | -36.07 | current_profile_false_positive |
| R3L10-C13-373220-SLOW-EV-CAPEX-20240425 | 373220 | LG에너지솔루션 | counterexample | high_mae_success | 4C-Thesis-Break-Watch | 2024-04-25 | 11.81 | -16.51 | current_profile_too_early |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
counterexample_search_incomplete = false
positive_case_missing = false
```

Interpretation:

- LGES 2022 shows that IRA/AMPC + US capacity exposure can be a valid Stage2/Yellow bridge.
- Samsung SDI 2023 shows that a future-dated JV headline should not become Green without utilization timing.
- LGES 2024 shows that AMPC credit can mask weak core profitability; this should cap positive stage promotion until utilization and margin recover.
- SK Innovation / SK On 2024 would be a strong thesis-break example, but stock-web corporate-action contamination blocks the 180D quantitative window.

## 9. Evidence Source Map

| evidence family | case_id | source status | use |
|---|---|---|---|
| IRA enacted / policy subsidy | LGES 2022 | source_url_verified_external | Stage2 policy optionality |
| Honda/LGES US battery JV context | LGES 2022 | source_url_verified_external but not sole trigger | capacity route |
| Samsung SDI / Stellantis second Kokomo JV | Samsung SDI 2023 | source_url_verified_external | counterexample: future-dated production |
| LGES Q1 2024 EV slowdown / capex minimization | LGES 2024 | source_url_verified_external | 4C watch and stage cap |
| SK On emergency management due EV sales disappointment | SKI 2024 | source_url_verified_external + stock_web_contaminated | narrative-only |

External evidence references used by this MD:

- IRA signed into law on 2022-08-16: Axios / Investopedia summary sources.
- Samsung SDI / Stellantis second Kokomo plant: AP, 2023-10-11.
- LGES 2024 Q1 slowdown and capex minimization: Reuters, 2024-04-25.
- SK On emergency management: Financial Times, 2024-07-07.
- Samsung SDI / GM 2024 JV finalization with 2027 mass production and GM EV forecast cut: Reuters, 2024-08-28.

## 10. Price Data Source Map

| symbol | company | profile_path | tradable_shard_used | profile caveat |
|---:|---|---|---|---|
| 373220 | LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | 2022, 2024, 2025 shards | no corporate-action candidate dates |
| 006400 | 삼성SDI | atlas/symbol_profiles/006/006400.json | 2023, 2024 shards | old corporate-action dates, none in tested window |
| 096770 | SK이노베이션 | atlas/symbol_profiles/096/096770.json | narrative only | 2024-11-20 corporate-action candidate blocks 180D window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | DD_after_peak | corp_status |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R3L10-C13-373220-T1 | 373220 | Stage2-Actionable | 2022-08-16 | 2022-08-17 | 453,500 | 13.78 | -5.84 | 38.7 | -7.39 | 38.7 | -7.39 | 2022-11-11 | 629,000 | -33.23 | clean_180D_window |
| R3L10-C13-006400-T1 | 006400 | Stage2-Headline-JV | 2023-10-11 | 2023-10-12 | 535,000 | 0.75 | -22.06 | 0.75 | -36.07 | 0.75 | -36.07 | 2023-10-12 | 539,000 | -45.36 | clean_180D_window |
| R3L10-C13-373220-T2 | 373220 | 4C-Thesis-Break-Watch | 2024-04-25 | 2024-04-25 | 372,500 | 6.58 | -12.48 | 11.81 | -16.51 | 19.19 | -16.51 | 2024-10-08 | 444,000 | -29.95 | clean_180D_window |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 LGES 2022 IRA/AMPC bridge

```text
symbol = 373220
entry_date = 2022-08-17
entry_price = 453500
30D high/low = 516000 / 427000
90D high/low = 629000 / 420000
180D high/low = 629000 / 420000
MFE_30D = 13.78
MAE_30D = -5.84
MFE_90D = 38.70
MAE_90D = -7.39
MFE_180D = 38.70
MAE_180D = -7.39
```

### 12.2 Samsung SDI 2023 future-dated JV headline

```text
symbol = 006400
entry_date = 2023-10-12
entry_price = 535000
30D high/low = 539000 / 417000
90D high/low = 539000 / 342000
180D high/low = 539000 / 342000
MFE_30D = 0.75
MAE_30D = -22.06
MFE_90D = 0.75
MAE_90D = -36.07
MFE_180D = 0.75
MAE_180D = -36.07
```

### 12.3 LGES 2024 slow-EV / capex-cut watch

```text
symbol = 373220
entry_date = 2024-04-25
entry_price = 372500
30D high/low = 397000 / 326000
90D high/low = 416500 / 311000
180D high/low = 444000 / 311000
MFE_30D = 6.58
MAE_30D = -12.48
MFE_90D = 11.81
MAE_90D = -16.51
MFE_180D = 19.19
MAE_180D = -16.51
```

## 13. Current Calibrated Profile Stress Test

| case_id | likely current profile behavior | actual OHLC alignment | verdict |
|---|---|---|---|
| LGES 2022 | Stage2-Actionable or Yellow due policy + relative strength | strong 90/180D MFE with controlled MAE | current_profile_correct |
| Samsung SDI 2023 | may over-credit JV / customer / capacity and allow Yellow | almost no MFE, large MAE | current_profile_false_positive |
| LGES 2024 | may keep too much subsidy/orderbook credit despite core slowdown | rebound exists but with high MAE; should be watch, not promotion | current_profile_too_early |
| SKI 2024 | would be 4C watch | stock-web contaminated, not quantitative | current_profile_data_insufficient |

Stress-test answers:

```text
1. current calibrated profile is broadly correct for LGES 2022.
2. It remains too permissive when future-dated JV capacity is scored like near-term utilization.
3. Stage2 bonus is useful only if policy/JV evidence has an operating bridge.
4. Yellow 75 is too low for future-dated JV cases without utilization.
5. Green 87 / revision 55 should remain strict.
6. price-only blowoff guard is appropriate.
7. full 4B non-price requirement is strengthened, not weakened.
8. hard 4C routing should trigger earlier as watch when EV demand slowdown changes capex/utilization plans.
```

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2-Actionable works in C13 when:
- policy/JV evidence is public,
- stock shows early relative strength,
- capacity route is near enough,
- utilization or customer draw is at least plausible.

Stage3-Yellow should require:
- customer draw or production ramp visibility,
- AMPC effect not being the only operating-profit bridge,
- no explicit capex slowdown.

Stage3-Green should require:
- revision and margin bridge,
- sustained utilization,
- low call-off risk,
- multiple evidence families beyond policy subsidy.
```

Green lateness ratio:

```text
LGES 2022 = not_applicable; no clean Green trigger in this MD
Samsung SDI 2023 = not_applicable; no confirmed Green trigger
LGES 2024 = not_applicable; trigger is slowdown/4C watch
```

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence type | local peak proximity | full-window peak proximity | verdict |
|---|---|---:|---:|---|
| Samsung SDI 2023 | price_only + explicit_event_cap | 1.00 | 1.00 | price-only local peak is useful as event-cap, not full 4B |
| LGES 2022 | valuation_blowoff only after run | not primary | not primary | no full 4B without non-price overheat |
| LGES 2024 | revision_slowdown / margin slowdown | n/a | n/a | this is 4C watch, not 4B exit |

Conclusion:

```text
existing_axis_strengthened = full_4b_requires_non_price_evidence
```

## 16. 4C Protection Audit

LGES 2024 and SK On 2024 demonstrate the 4C watch shape:

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not fully asserted
reason = EV demand slowdown / capex minimization / emergency management evidence should cap positive stage before hard cancellation evidence.
```

For SK Innovation / SK On, the evidence is qualitatively strong, but the stock-web profile has a 2024-11-20 corporate-action candidate inside the July 2024 forward window, so it is narrative-only.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L3_C13_JV_AMPC_UTILIZATION_BRIDGE
proposal_type = sector_shadow_only
production_scoring_changed = false
```

Rule candidate:

```text
In L3 battery/EV cases, IRA/AMPC or JV capacity evidence may add Stage2 support only when paired with at least one operating bridge:
- near-term SOP / production start,
- utilization or shipment path,
- customer draw/order conversion,
- margin bridge excluding subsidy-only effect,
- capex pace not being cut due to EV demand slowdown.
```

If the bridge is absent:

```text
cap_positive_stage = Stage2-watch_only
block_Stage3_Yellow = true unless revision/margin evidence exists
block_Stage3_Green = true
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rule_id = C13_AMPC_JV_UTILIZATION_GATE
```

Canonical rule:

```text
C13 should use separate components:
- ampC_or_ira_score
- jv_capacity_score
- utilization_score
- customer_draw_score
- core_margin_ex_subsidy_score

ampC_or_ira_score alone cannot promote positive Stage2/3.
future_dated_jv_capacity_without_utilization becomes event-watch, not rerating signal.
capex cut / low utilization / subsidy-only operating profit becomes 4C watch or counterexample guard.
```

## 19. Before / After Backtest Comparison

| profile | selected entries | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | missed structural | score-return alignment |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 17.09 | -19.99 | 19.55 | -19.99 | 0.67 | 0 | mixed; overcredits JV/AMPC headline |
| P0b e2r_2_0_baseline_reference | 3 | 17.09 | -19.99 | 19.55 | -19.99 | 0.67 | 1 | worse; lacks calibrated guardrails |
| P1 sector_specific_candidate_profile | 3 | 17.09 | -19.99 | 19.55 | -19.99 | 0.33 | 0 | better: demotes future-dated JV |
| P2 canonical_archetype_candidate_profile | 3 | 17.09 | -19.99 | 19.55 | -19.99 | 0.33 | 0 | best explanatory compression |
| P3 counterexample_guard_profile | 2 counterexamples selected | 6.28 | -26.29 | 9.97 | -26.29 | 0.00 | 0 | useful for guardrail, not entry promotion |

## 20. Score-Return Alignment Matrix

| case_id | before score/stage | after score/stage | MFE90/MAE90 | alignment label |
|---|---|---|---|---|
| LGES 2022 | 76 / Stage3-Yellow | 78 / Stage2-Actionable_to_Yellow_watch | 38.70 / -7.39 | good_positive_alignment_but_green_requires_later_utilization |
| Samsung SDI 2023 | 75 / false-positive Yellow risk | 65 / Stage2-watch_only | 0.75 / -36.07 | correctly_demoted_by_utilization_guard |
| LGES 2024 | 74 / too-early Stage2 | 62 / Stage1_to_Stage2_watch_only | 11.81 / -16.51 | demotion_reduces_high_mae_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | IRA_AMPC_JV_UTILIZATION_CAPEX_PACE | 1 | 2 | 1 | 1 | 3 | 0 | 4 | 3 | 2 | true | true | need more pure positive C13 cases with exact AMPC ex-subsidy OP bridge |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - future_dated_jv_false_positive
  - ampc_without_utilization_high_mae
  - slow_ev_demand_capex_cut_should_cap_positive_stage
new_axis_proposed:
  - c13_utilization_required_bridge
  - c13_ampc_without_operating_profit_cap
  - c13_future_dated_jv_event_cap
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
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
- scheduled_round = R3
- scheduled_loop = 10
- round_sector_consistency = pass
- large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
- canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
- stock-web manifest max_date = 2026-02-20
- tradable_raw OHLC rows checked for 373220 and 006400
- profile corporate-action windows checked for 373220, 006400, 096770
- 30D/90D/180D MFE/MAE calculated for usable triggers
```

Not validated:

```text
- no production scoring changed
- no stock_agent src/e2r code accessed
- no live candidate scan
- no brokerage / auto-trading
- no adjusted-price recalculation
- no 1Y/2Y primary calibration in this loop
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c13_utilization_required_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,Future-dated JV/AMPC headline must be bridged by utilization or near-term production path.,Demotes Samsung SDI-style future-dated JV false positive while keeping LGES IRA/AMPC success as Stage2/Yellow watch.,R3L10-C13-373220-T1|R3L10-C13-006400-T1|R3L10-C13-373220-T2,3,3,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c13_ampc_without_operating_profit_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,none,cap_stage2_watch,+1,"If IRA/AMPC credit prevents loss but core profit and capex are cut, cap positive stage promotion.",Reduces high-MAE false positive risk in LGES 2024 slowdown case.,R3L10-C13-373220-T2,1,1,1,low_medium,canonical_shadow_only,exact evidence URL enrichment required before production promotion
shadow_weight,c13_future_dated_jv_event_cap,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,none,stage2_watch_only,+1,JV start date beyond two-year horizon with no confirmed utilization should not train Stage3/Green.,Converts Samsung SDI 2023 Kokomo headline from false Stage3-Yellow to Stage2 watch.,R3L10-C13-006400-T1,1,1,1,medium,sector_shadow_only,not production; 4B rows remain overlay only
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L10-C13-373220-IRA-AMPC-20220817","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_AMPC_US_CAPACITY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R3L10-C13-373220-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_positive_alignment_but_green_requires_later_utilization","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"IRA signed into law; LGES already had/announced US battery capacity/JV exposure. Treat as Stage2 only until AMPC/revenue visibility arrives."}
{"row_type":"trigger","trigger_id":"R3L10-C13-373220-T1","case_id":"R3L10-C13-373220-IRA-AMPC-20220817","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_AMPC_US_CAPACITY_BRIDGE","sector":"2차전지·전기차·친환경","primary_archetype":"BATTERY_JV_UTILIZATION_AMPC_IRA","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","counterexample_mining"],"trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","evidence_available_at_that_date":"IRA signed into law; LGES already had/announced US battery capacity/JV exposure. Treat as Stage2 only until AMPC/revenue visibility arrives.","evidence_source":"Investopedia/Axios/IRA signing summaries; LGES/Honda JV context sources","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-17","entry_price":453500,"MFE_30D_pct":13.78,"MFE_90D_pct":38.7,"MFE_180D_pct":38.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.84,"MAE_90D_pct":-7.39,"MAE_180D_pct":-7.39,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-11-11","peak_price":629000,"drawdown_after_peak_pct":-33.23,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger_at_entry","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L10-C13-373220-20220817-453500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L10-C13-373220-IRA-AMPC-20220817","trigger_id":"R3L10-C13-373220-T1","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":48,"margin_bridge_score":40,"revision_score":44,"relative_strength_score":67,"customer_quality_score":55,"policy_or_regulatory_score":84,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8,"utilization_score":42,"ampC_or_ira_score":82},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":48,"margin_bridge_score":40,"revision_score":44,"relative_strength_score":67,"customer_quality_score":55,"policy_or_regulatory_score":84,"valuation_repricing_score":65,"execution_risk_score":34,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8,"utilization_score":48,"ampC_or_ira_score":86},"weighted_score_after":78.0,"stage_label_after":"Stage2-Actionable_to_Stage3-Yellow_watch","changed_components":["utilization_score","ampC_or_ira_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile separates subsidy/JV headline from utilization, near-term production, customer draw, and margin conversion.","MFE_90D_pct":38.7,"MAE_90D_pct":-7.39,"score_return_alignment_label":"good_positive_alignment_but_green_requires_later_utilization","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"R3L10-C13-006400-STELLANTIS-KOKOMO-20231012","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"FUTURE_DATED_JV_CAPACITY_WITHOUT_UTILIZATION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R3L10-C13-006400-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"correctly_demoted_by_utilization_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Stellantis/Samsung SDI second Kokomo JV, but start of production was early 2027; headline capacity did not equal near-term utilization or earnings revision."}
{"row_type":"trigger","trigger_id":"R3L10-C13-006400-T1","case_id":"R3L10-C13-006400-STELLANTIS-KOKOMO-20231012","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"FUTURE_DATED_JV_CAPACITY_WITHOUT_UTILIZATION","sector":"2차전지·전기차·친환경","primary_archetype":"BATTERY_JV_UTILIZATION_AMPC_IRA","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","counterexample_mining"],"trigger_type":"Stage2-Headline-JV","trigger_date":"2023-10-11","evidence_available_at_that_date":"Stellantis/Samsung SDI second Kokomo JV, but start of production was early 2027; headline capacity did not equal near-term utilization or earnings revision.","evidence_source":"AP 2023-10-11 Stellantis/Samsung SDI Kokomo second plant","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-12","entry_price":535000,"MFE_30D_pct":0.75,"MFE_90D_pct":0.75,"MFE_180D_pct":0.75,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.06,"MAE_90D_pct":-36.07,"MAE_180D_pct":-36.07,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-12","peak_price":539000,"drawdown_after_peak_pct":-45.36,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger_at_entry","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":["explicit_event_cap","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L10-C13-006400-20231012-535000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L10-C13-006400-STELLANTIS-KOKOMO-20231012","trigger_id":"R3L10-C13-006400-T1","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":58,"backlog_visibility_score":54,"margin_bridge_score":32,"revision_score":28,"relative_strength_score":42,"customer_quality_score":62,"policy_or_regulatory_score":66,"valuation_repricing_score":51,"execution_risk_score":55,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":6,"accounting_trust_risk_score":6,"utilization_score":18,"ampC_or_ira_score":55},"weighted_score_before":75.0,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":42,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":35,"customer_quality_score":45,"policy_or_regulatory_score":58,"valuation_repricing_score":43,"execution_risk_score":64,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":6,"accounting_trust_risk_score":6,"utilization_score":10,"ampC_or_ira_score":45},"weighted_score_after":65.0,"stage_label_after":"Stage2-watch_only","changed_components":["utilization_score","ampC_or_ira_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile separates subsidy/JV headline from utilization, near-term production, customer draw, and margin conversion.","MFE_90D_pct":0.75,"MAE_90D_pct":-36.07,"score_return_alignment_label":"correctly_demoted_by_utilization_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"R3L10-C13-373220-SLOW-EV-CAPEX-20240425","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_CREDIT_WITH_LOW_UTILIZATION_HIGH_MAE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R3L10-C13-373220-T2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_as_positive_case_but_opposite_regime_and_new_trigger_family","independent_evidence_weight":0.5,"score_price_alignment":"demotion_reduces_high_mae_false_positive","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Q1 2024 profit plunge, EV demand slowdown, capex minimization; IRA credit made the difference between profit and loss."}
{"row_type":"trigger","trigger_id":"R3L10-C13-373220-T2","case_id":"R3L10-C13-373220-SLOW-EV-CAPEX-20240425","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"IRA_CREDIT_WITH_LOW_UTILIZATION_HIGH_MAE","sector":"2차전지·전기차·친환경","primary_archetype":"BATTERY_JV_UTILIZATION_AMPC_IRA","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","counterexample_mining"],"trigger_type":"4C-Thesis-Break-Watch","trigger_date":"2024-04-25","evidence_available_at_that_date":"Q1 2024 profit plunge, EV demand slowdown, capex minimization; IRA credit made the difference between profit and loss.","evidence_source":"Reuters 2024-04-25 LGES Q1 / slow EV demand / capex minimization","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","revision_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":372500,"MFE_30D_pct":6.58,"MFE_90D_pct":11.81,"MFE_180D_pct":19.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.48,"MAE_90D_pct":-16.51,"MAE_180D_pct":-16.51,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000,"drawdown_after_peak_pct":-29.95,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger_at_entry","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":["margin_or_backlog_slowdown","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L10-C13-373220-20240425-372500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_as_positive_case_but_opposite_regime_and_new_trigger_family","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L10-C13-373220-SLOW-EV-CAPEX-20240425","trigger_id":"R3L10-C13-373220-T2","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":52,"backlog_visibility_score":48,"margin_bridge_score":38,"revision_score":42,"relative_strength_score":40,"customer_quality_score":55,"policy_or_regulatory_score":75,"valuation_repricing_score":48,"execution_risk_score":58,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":5,"accounting_trust_risk_score":7,"utilization_score":16,"ampC_or_ira_score":78},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable_too_early","raw_component_scores_after":{"contract_score":42,"backlog_visibility_score":38,"margin_bridge_score":22,"revision_score":18,"relative_strength_score":35,"customer_quality_score":45,"policy_or_regulatory_score":70,"valuation_repricing_score":42,"execution_risk_score":70,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":5,"accounting_trust_risk_score":7,"utilization_score":8,"ampC_or_ira_score":62},"weighted_score_after":62.0,"stage_label_after":"Stage1_to_Stage2_watch_only","changed_components":["utilization_score","ampC_or_ira_score","margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile separates subsidy/JV headline from utilization, near-term production, customer draw, and margin conversion.","MFE_90D_pct":11.81,"MAE_90D_pct":-16.51,"score_return_alignment_label":"demotion_reduces_high_mae_false_positive","current_profile_verdict":"current_profile_too_early"}
{"row_type":"trigger","trigger_id":"R3L10-C13-006400-T1-4B-OVERLAY","case_id":"R3L10-C13-006400-STELLANTIS-KOKOMO-20231012","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"FUTURE_DATED_JV_CAPACITY_WITHOUT_UTILIZATION","sector":"2차전지·전기차·친환경","primary_archetype":"BATTERY_JV_UTILIZATION_AMPC_IRA","loop_objective":["4B_non_price_requirement_stress_test","counterexample_mining"],"trigger_type":"4B-Overlay-PriceOnly-LocalPeak","trigger_date":"2023-10-12","evidence_available_at_that_date":"Same-entry local peak after future-dated JV headline; no non-price 4B evidence beyond event premium.","evidence_source":"stock-web OHLC + AP JV timing source","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-12","entry_price":535000,"MFE_30D_pct":0.75,"MFE_90D_pct":0.75,"MFE_180D_pct":0.75,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.06,"MAE_90D_pct":-36.07,"MAE_180D_pct":-36.07,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-10-12","peak_price":539000,"drawdown_after_peak_pct":-45.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","explicit_event_cap"],"four_c_protection_label":null,"trigger_outcome_label":"4B_too_early_as_full_exit_but_valid_as_event_cap","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L10-C13-006400-20231012-535000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_entry_group_as_samsung_sdi_representative_trigger_for_4B_split","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"narrative_only","case_id":"R3L10-C13-096770-SKON-EMERGENCY-20240708","symbol":"096770","company_name":"SK이노베이션","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SKON_EV_DEMAND_SLOWDOWN_BALANCE_SHEET_STRESS","reason":"SK On emergency-management evidence is relevant to utilization/capex guardrail, but 096770 profile has corporate_action_candidate_date=2024-11-20, which overlaps the 180D window from a July 2024 trigger.","price_source":"Songdaiki/stock-web","profile_path":"atlas/symbol_profiles/096/096770.json","usage":"not_weight_calibration"}
{"row_type":"residual_contribution","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["future_dated_jv_false_positive","ampc_without_utilization_high_mae","slow_ev_demand_capex_cut_should_cap_positive_stage"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 10
next_round = R4
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

### Stock-agent research artifacts

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`
- `data/e2r/calibration/md_registry.jsonl`

### Stock-web price atlas files

- `atlas/manifest.json`
- `atlas/symbol_profiles/373/373220.json`
- `atlas/symbol_profiles/006/006400.json`
- `atlas/symbol_profiles/096/096770.json`
- `atlas/ohlcv_tradable_by_symbol_year/373/373220/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv`

### External evidence sources

- Axios / Investopedia summaries for 2022-08-16 IRA signing.
- AP 2023-10-11: Stellantis and Samsung SDI second Kokomo battery plant, expected early 2027 start.
- Reuters 2024-04-25: LG Energy Solution Q1 profit plunge, slow EV demand, capex minimization, IRA credit effect.
- Reuters 2024-08-28: Samsung SDI / GM JV finalization, 2027 mass production timing and GM EV forecast cut.
- Financial Times 2024-07-07: SK On emergency management due disappointing EV sales; narrative-only because 096770 stock-web 180D window is corporate-action contaminated.
