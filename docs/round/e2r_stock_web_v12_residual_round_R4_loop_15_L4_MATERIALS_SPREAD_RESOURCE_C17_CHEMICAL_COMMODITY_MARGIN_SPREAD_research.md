# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
output_file: e2r_stock_web_v12_residual_round_R4_loop_15_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
scheduled_round: R4
scheduled_loop: 15
completed_round: R4
completed_loop: 15
next_round: R5
next_loop: 15
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: ALKALI_PVC_PLASTICIZER_TIRECORD_MARGIN_BRIDGE
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - green_strictness_stress_test
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **5** new independent cases, **2** counterexamples, and **2** residual errors for `R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`.

## 1. Current Calibrated Profile Assumption

The current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`.

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

This MD does not re-prove the global rules. It stress-tests whether chemical and commodity-spread cases need a C17-specific rule: **spread headline alone is not evidence; spread must travel into margin bridge and revision**. The mechanism is like a pump connected to a pipe: commodity price can create pressure, but unless the pipe reaches gross margin and then analyst revision, the pressure never reaches the scoring chamber.

## 2. Round / Large Sector / Canonical Archetype Scope

- `scheduled_round = R4`
- `scheduled_loop = 15`
- `large_sector_id = L4_MATERIALS_SPREAD_RESOURCE`
- `canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`
- `fine_archetype_id = ALKALI_PVC_PLASTICIZER_TIRECORD_MARGIN_BRIDGE`

R4 maps to materials / spread / strategic resources. The chosen canonical is C17 because all selected cases depend on whether chemical product spread becomes operating margin and revision rather than only relative-strength price action.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` inspection was limited to research artifacts. The registry currently visible through `data/e2r/calibration/md_registry.jsonl` contains earlier parsed historical calibration records and row counts, but not a committed v12 R4 Loop 15 artifact. The local sandbox has R4 loops 10~14, ending with `R4 loop 14 / C16`, while the immediately preceding generated file ended at `R3 loop 15` and set `next_round = R4`.

```text
previous_completed_round = R3
previous_completed_loop = 15
scheduled_round = R4
scheduled_loop = 15
same_symbol_same_trigger_date_duplicate = false
same_canonical_archetype_research = allowed
new_symbol_count = 5
new_trigger_family_count = 5
reused_case_count = 0
schema_rematerialization_only = false
```

The selected symbols are not the prior C17 loop-12 core set of 효성티앤씨 / 금호석유화학 / 롯데케미칼 / 대한유화. This loop therefore adds new independent C17 surface area.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14,354,401
raw_row_count = 15,214,118
symbol_count = 5,414
active_like_symbol_count = 2,868
inactive_or_delisted_like_symbol_count = 2,546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Stock-Web manifest confirms `max_date = 2026-02-20`, raw/unadjusted marcap basis, tradable and raw row counts, markets, and shard roots. It also states that zero-volume / zero-OHLC rows are excluded from calibration shards and corporate-action contaminated windows are blocked by default. fileciteturn1304file0L4-L13 fileciteturn1304file0L30-L45 fileciteturn1304file0L53-L58

## 5. Historical Eligibility Gate

| case_id | entry row exists | 180D forward available | OHLC/V positive | corporate-action 180D window | calibration_usable |
|---|---:|---:|---:|---|---:|
| R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE | yes | yes | yes | clean | true |
| R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE | yes | yes | yes | clean | true |
| R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE | yes | yes | yes | clean | true |
| R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE | yes | yes | yes | clean | true |
| R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER | yes | yes | yes | clean | true |

Profile caveats checked:

- `004000` has corporate-action candidates only in legacy 1996~1999 dates, not the 2021 window. fileciteturn1305file0L204-L222 fileciteturn1306file0L3-L11
- `120110` has a 2010-12-27 candidate only; 2021 is clean. fileciteturn1314file0L124-L141
- `009830` has candidates in 1999 and 2008 only; 2020 is clean. fileciteturn1311file0L219-L232 fileciteturn1312file0L9-L15
- `161000` has 2016 and 2021 candidates, not 2023. fileciteturn1317file0L119-L137
- `298000` has no corporate-action candidates in the profile. fileciteturn1319file0L81-L98

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rationale |
|---|---|---|
| ECH_CAUSTIC_SODA_MARGIN_BRIDGE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Product spread moves into earnings visibility. |
| TIRECORD_ARAMID_MARGIN_BRIDGE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Industrial material cycle creates operating leverage. |
| PVC_CAUSTIC_SOLAR_SPREAD_OPERATING_LEVERAGE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Commodity spread and downstream demand jointly move margin. |
| PLASTICIZER_BATTERY_PROXY_PRICE_ONLY_FALSE_POSITIVE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Price-only proxy without margin bridge is a C17 counterexample. |
| PDH_PP_SPREAD_OVERBUILD_HIGH_MAE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Spread headline fails when overbuild/execution risk dominates. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | pos/counter | trigger | MFE90 | MAE90 | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---|
| R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE | 004000 | 롯데정밀화학 | structural_success | positive | R4L15_C17_T01_LOTTEFINE_20210901_STAGE2 | 43.97 | -0.99 | current_profile_correct |
| R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE | 120110 | 코오롱인더 | structural_success | positive | R4L15_C17_T02_KOLONIND_20210202_STAGE2 | 68.84 | -1.63 | current_profile_correct |
| R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE | 009830 | 한화솔루션 | structural_success | positive | R4L15_C17_T03_HANWHA_20200803_STAGE2 | 102.32 | -3.29 | current_profile_correct |
| R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE | 161000 | 애경케미칼 | false_positive_green | counterexample | R4L15_C17_T04_AEKYUNG_20230411_FALSE_GREEN | 76.96 | -17.0 | current_profile_false_positive |
| R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER | 298000 | 효성화학 | failed_rerating | counterexample | R4L15_C17_T05_HYOSUNGCHEM_20210503_FALSE_STAGE2 | 11.37 | -28.37 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
calibration_usable_case_count = 5
representative_trigger_count = 5
new_independent_case_count = 5
new_independent_case_ratio = 1.00
```

The balance is acceptable for shadow calibration. Three positives show what a true C17 spread-to-margin bridge looks like. Two counterexamples show the trap: commodity or proxy price action can look like Stage2/Yellow before the actual margin bridge exists.

## 9. Evidence Source Map

| case_id | evidence family | evidence timing rule | evidence source note |
|---|---|---|---|
| R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE | ECH/caustic soda spread + revision | same-day close | industry spread commentary; stock-web row |
| R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE | tirecord/aramid recovery + operating leverage | same-day close | product cycle commentary; stock-web row |
| R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE | PVC/solar value-chain leverage | same-day close | chemical/PVC/solar commentary; stock-web row |
| R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE | price-only proxy, no margin bridge | same-day close | stock-web price action; evidence gap |
| R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER | PDH spread headline vs overbuild execution risk | same-day close | stock-web row; evidence gap |

No current/live candidate scan was performed.

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry row |
|---:|---|---|---|---|
| 004000 | 롯데정밀화학 | `atlas/ohlcv_tradable_by_symbol_year/004/004000/2021.csv` | `atlas/symbol_profiles/004/004000.json` | 2021-09-01 close 70,500 |
| 120110 | 코오롱인더 | `atlas/ohlcv_tradable_by_symbol_year/120/120110/2021.csv` | `atlas/symbol_profiles/120/120110.json` | 2021-02-02 close 49,100 |
| 009830 | 한화솔루션 | `atlas/ohlcv_tradable_by_symbol_year/009/009830/2020.csv` | `atlas/symbol_profiles/009/009830.json` | 2020-08-03 close 25,850 |
| 161000 | 애경케미칼 | `atlas/ohlcv_tradable_by_symbol_year/161/161000/2023.csv` | `atlas/symbol_profiles/161/161000.json` | 2023-04-11 close 15,710 |
| 298000 | 효성화학 | `atlas/ohlcv_tradable_by_symbol_year/298/298000/2021.csv` | `atlas/symbol_profiles/298/298000.json` | 2021-05-03 close 426,500 |

Representative rows were checked from Stock-Web CSV shards: `004000` shows 2021-09-01 close 70,500 and 2021-09-29 high 101,500; `120110` shows 2021-02-02 close 49,100 and later 2021-09-24 high 114,500; `009830` shows 2020-08-03 close 25,850 and later highs through the 2020 cycle; `161000` shows the April~June 2023 spike; `298000` shows May~July 2021 rebound followed by high MAE. fileciteturn1308file0L51-L68 fileciteturn1309file0L3-L31 fileciteturn1315file0L24-L31 fileciteturn1316file0L63-L69 fileciteturn1313file0L10-L35 fileciteturn1318file0L3-L25 fileciteturn1320file0L7-L15

## 11. Case-by-Case Trigger Grid

| case_id | symbol | company_name | case_type | pos/counter | trigger | MFE90 | MAE90 | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---|
| R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE | 004000 | 롯데정밀화학 | structural_success | positive | R4L15_C17_T01_LOTTEFINE_20210901_STAGE2 | 43.97 | -0.99 | current_profile_correct |
| R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE | 120110 | 코오롱인더 | structural_success | positive | R4L15_C17_T02_KOLONIND_20210202_STAGE2 | 68.84 | -1.63 | current_profile_correct |
| R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE | 009830 | 한화솔루션 | structural_success | positive | R4L15_C17_T03_HANWHA_20200803_STAGE2 | 102.32 | -3.29 | current_profile_correct |
| R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE | 161000 | 애경케미칼 | false_positive_green | counterexample | R4L15_C17_T04_AEKYUNG_20230411_FALSE_GREEN | 76.96 | -17.0 | current_profile_false_positive |
| R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER | 298000 | 효성화학 | failed_rerating | counterexample | R4L15_C17_T05_HYOSUNGCHEM_20210503_FALSE_STAGE2 | 11.37 | -28.37 | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R4L15_C17_T01_LOTTEFINE_20210901_STAGE2 | 004000 | 2021-09-01 | 70500 | 43.97 | 43.97 | 43.97 | -0.99 | -0.99 | -7.38 | 2021-09-29 | 101500 | structural_success_margin_bridge |
| R4L15_C17_T02_KOLONIND_20210202_STAGE2 | 120110 | 2021-02-02 | 49100 | 30.35 | 68.84 | 133.2 | -1.63 | -1.63 | -1.63 | 2021-09-24 | 114500 | structural_success_operating_leverage |
| R4L15_C17_T03_HANWHA_20200803_STAGE2 | 009830 | 2020-08-03 | 25850 | 59.19 | 102.32 | 128.63 | -3.29 | -3.29 | -3.29 | 2021-01-11 | 59100 | structural_success_high_MFE |
| R4L15_C17_T04_AEKYUNG_20230411_FALSE_GREEN | 161000 | 2023-04-11 | 15710 | 43.86 | 76.96 | 76.96 | -17.0 | -17.0 | -42.71 | 2023-06-22 | 27800 | price_moved_without_margin_bridge |
| R4L15_C17_T05_HYOSUNGCHEM_20210503_FALSE_STAGE2 | 298000 | 2021-05-03 | 426500 | 3.52 | 11.37 | 11.37 | -21.1 | -28.37 | -50.76 | 2021-07-16 | 475000 | failed_rerating_high_MAE |


MFE/MAE basis:

```text
MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100
```

The values are computed on Stock-Web tradable rows and are not adjusted close.

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely judgment | actual return path | verdict |
|---|---|---|---|
| R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE | Stage3-Yellow/Green with margin bridge | high MFE, low initial MAE | current_profile_correct |
| R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE | Stage3-Yellow/Green after revision | very large 180D MFE | current_profile_correct |
| R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE | Stage3-Yellow/Green after cross-evidence | high MFE with manageable MAE | current_profile_correct |
| R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE | might over-promote on relative strength | high peak but large later drawdown and weak margin evidence | current_profile_false_positive |
| R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER | might promote headline spread | MFE small, MAE large | current_profile_false_positive |

Axis answers:

```text
stage2_actionable_evidence_bonus: kept, but capped for price-only C17 rows.
yellow_threshold_75: kept; chemical spread headlines can reach Yellow only with margin bridge.
green_threshold_87 / revision_55: strengthened inside C17 by requiring margin bridge + revision.
price_only_blowoff_blocks_positive_stage: strengthened.
full_4b_requires_non_price_evidence: kept.
hard_4c_thesis_break_routes_to_4c: kept, but C17 requires actual margin/revision break, not mere price drawdown.
```

## 14. Stage2 / Yellow / Green Comparison

The C17 pattern is asymmetric:

- Positive rows work when Stage2 already contains **spread evidence**, and Yellow/Green arrives only when that spread has a visible bridge to margin and revision.
- Counterexample rows fail when Stage2 is built from relative strength and commodity/theme headlines, while Stage3 evidence is empty.

`green_lateness_ratio` is therefore meaningful only for the positive rows:

| case_id | Stage2 entry | Green proxy entry | peak | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| LOTTEFINE | 70,500 | about 82,900 | 101,500 | 0.38 | Green somewhat late but acceptable |
| KOLONIND | 49,100 | about 81,100 | 114,500 | 0.49 | Green late but still captures structural upside |
| HANWHA | 25,850 | about 39,950 | 59,100 | 0.42 | Green late but still useful |
| AEKYUNG | 15,710 | n/a | 27,800 | n/a | no confirmed Green trigger |
| HYOSUNGCHEM | 426,500 | n/a | 475,000 | n/a | no confirmed Green trigger |

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | verdict |
|---|---:|---:|---|---|
| LOTTEFINE | 0.92 | 1.00 | valuation_blowoff + positioning + slowdown | good_full_window_4B_timing |
| KOLONIND | 0.78 | 0.88 | valuation_blowoff + revision_slowdown | good_full_window_4B_timing |
| HANWHA | 0.86 | 0.94 | valuation_blowoff + positioning | good_full_window_4B_timing |
| AEKYUNG | 0.97 | 1.00 | price_only + positioning | price-only overlay; not full 4B without non-price evidence |
| HYOSUNGCHEM | 0.43 | 0.43 | margin slowdown + execution risk | spread failed before clean full-cycle 4B |

The local/full split matters. AEKYUNG had a high peak proximity, but without a margin/revision bridge it should block Green and become risk overlay, not become proof of a successful C17 thesis.

## 16. 4C Protection Audit

| case_id | 4C protection label | rationale |
|---|---|---|
| LOTTEFINE | thesis_break_watch_only | later drawdown did not invalidate the original spread bridge until slowdown evidence appeared |
| KOLONIND | thesis_break_watch_only | structural upcycle worked; 4B overlay is enough |
| HANWHA | thesis_break_watch_only | structural rerating worked; 4C not needed |
| AEKYUNG | false_break | price collapse alone should not be labeled hard 4C if original thesis was never valid Green |
| HYOSUNGCHEM | hard_4c_late | overbuild/execution risk eventually broke the spread thesis |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L4_execution_risk_penalty_for_headline_spread
candidate = true
```

Rule proposal:

> In L4 materials/spread sectors, commodity spread headlines should be offset by execution-risk / overbuild-risk when MAE expands before margin bridge and revision appear.

Reason: `298000` demonstrates that a spread headline can be a beautiful signboard on a closed factory: visible from the road, but not yet producing cash flow.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C17_margin_bridge_required_for_Green
candidate = true
```

Canonical rule proposal:

> C17 Green requires at least two of three non-price bridges: margin_bridge_score, revision_score, and financial_visibility. Relative strength alone can support Watch/Stage2 only.

Expected effect: Positive rows remain eligible. AEKYUNG and HYOSUNGCHEM are capped.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | current calibrated profile without C17-specific bridge gate | 5 | 60.69 | -10.26 | 78.83 | -21.15 | 0.4 | mixed; positives pass but two false-positive commodity headlines remain too high |
| P0b_e2r_2_0_baseline_reference | rollback_reference | older profile before post-stock-web guardrails | 5 | 60.69 | -10.26 | 78.83 | -21.15 | 0.6 | worse false-positive handling |
| P1_L4_materials_spread_candidate_profile | sector_specific | L4 spread cycles need margin bridge and revision confirmation before Green | 5 | 71.71 | -1.97 | 101.93 | -4.1 | 0.2 | better separation of real margin bridge vs headline |
| P2_C17_chemical_commodity_margin_bridge_profile | canonical_archetype_specific | C17 positive promotion requires spread + margin bridge + revision; relative-strength alone stays Watch | 5 | 71.71 | -1.97 | 101.93 | -4.1 | 0.0 | best score-return alignment in this loop |
| P3_C17_counterexample_guard_profile | counterexample_guard | cap spread score when MAE expands before any financial visibility | 5 | 44.16 | -22.69 | 44.16 | -46.73 | 0.0 | guards price-only/high-MAE failures |


## 20. Score-Return Alignment Matrix

| case_id | before score/stage | after score/stage | MFE90 | MAE90 | alignment |
|---|---|---|---:|---:|---|
| R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE | 83 / Stage3-Yellow | 88 / Stage3-Green shadow | 43.97 | -0.99 | structural_success_margin_bridge |
| R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE | 81 / Stage3-Yellow | 89 / Stage3-Green shadow | 68.84 | -1.63 | structural_success_operating_leverage |
| R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE | 79 / Stage3-Yellow | 86 / Stage3-Green shadow | 102.32 | -3.29 | structural_success_high_MFE |
| R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE | 76 / Stage3-Yellow false-positive risk | 58 / Stage1/Watch - price-only proxy | 76.96 | -17.0 | price_moved_without_margin_bridge |
| R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER | 72 / Stage2-Actionable false-positive risk | 54 / Stage1/Watch - spread headline only | 11.37 | -28.37 | failed_rerating_high_MAE |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | ALKALI_PVC_PLASTICIZER_TIRECORD_MARGIN_BRIDGE | 3 | 2 | 5 | 2 | 5 | 0 | 5 | 5 | 2 | true | true | C17 now has new margin-bridge positives and price-only/high-MAE counterexamples for loop 15. |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - chemical_spread_false_positive
  - price_only_relative_strength_false_green
  - high_MAE_failed_rerating
new_axis_proposed:
  - C17_margin_bridge_required_for_Green
  - C17_price_only_relative_strength_cap
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
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

Validation scope:

```text
- Historical trigger-level OHLC validation only.
- Price rows from Songdaiki/stock-web tradable_raw shards.
- No stock_agent code inspection.
- No production scoring change.
- No current/live candidate discovery.
- No brokerage or automation work.
```

Non-validation scope:

```text
- No live recommendation.
- No 2026 scan.
- No guarantee of actual production score behavior.
- External evidence notes are research-context summaries, not a fresh live research report.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"spread headline must map to margin_bridge_score and revision_score before Green","reduced false-positive commodity headline rows","R4L15_C17_T01|R4L15_C17_T02|R4L15_C17_T03|R4L15_C17_T04|R4L15_C17_T05",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_price_only_relative_strength_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"price-only spikes are capped at Watch/Yellow unless margin bridge appears","blocked 161000/298000 false-positive promotion","R4L15_C17_T04|R4L15_C17_T05",5,5,2,medium,canonical_shadow_only,"strengthens existing price-only guard inside C17"
shadow_weight,L4_execution_risk_penalty,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"high MAE and overbuild/execution risk should offset commodity spread headline","improved MAE-aware separation","R4L15_C17_T05",5,5,2,low,sector_shadow_only,"candidate only; needs later loops"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"ECH_CAUSTIC_SODA_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L15_C17_T01_LOTTEFINE_20210901_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_margin_bridge","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2021년 하반기 ECH/가성소다 등 염소계 제품 spread 개선과 이익 추정 상향 가능성이 공개 리포트/시장 코멘터리에서 논의되던 구간. 2021-09-01 stock-web close 70,500 이후 2021-09-29 high 101,500."}
{"row_type":"case","case_id":"R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE","symbol":"120110","company_name":"코오롱인더","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"TIRECORD_ARAMID_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L15_C17_T02_KOLONIND_20210202_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_operating_leverage","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2021년 초 산업소재/tirecord/aramid 회복이 단순 가격 반등이 아니라 이익 가시성과 연결되던 구간. 2021-02-02 stock-web close 49,100 이후 2021-09-24 high 114,500."}
{"row_type":"case","case_id":"R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PVC_CAUSTIC_SOLAR_SPREAD_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L15_C17_T03_HANWHA_20200803_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_high_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2020년 하반기 PVC/가성소다 및 태양광 밸류체인 회복이 동반되며 화학 spread가 실적 레버리지로 번역되던 구간. 2020-08-03 close 25,850 이후 2020-09~2021-01에 강한 MFE."}
{"row_type":"case","case_id":"R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE","symbol":"161000","company_name":"애경케미칼","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PLASTICIZER_BATTERY_PROXY_PRICE_ONLY_FALSE_POSITIVE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R4L15_C17_T04_AEKYUNG_20230411_FALSE_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_moved_without_margin_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2023년 4~6월 price tape는 강했지만, C17 관점에서는 실제 commodity spread → margin bridge → revision으로 이어졌다는 확인이 약했다. price-only move를 Green 근거로 쓰면 false-positive risk가 커진다."}
{"row_type":"case","case_id":"R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER","symbol":"298000","company_name":"효성화학","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PDH_PP_SPREAD_OVERBUILD_HIGH_MAE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L15_C17_T05_HYOSUNGCHEM_20210503_FALSE_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2021년 봄 PP/PDH spread headline만으로는 충분하지 않았다. entry 직후 MAE가 커졌고, later path는 overbuild/execution-risk가 margin bridge를 압도하는 반례가 되었다."}
{"row_type":"trigger","trigger_id":"R4L15_C17_T01_LOTTEFINE_20210901_STAGE2","case_id":"R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"ECH_CAUSTIC_SODA_MARGIN_BRIDGE","sector":"정밀화학·염소계","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-09-01","entry_date":"2021-09-01","entry_price":70500,"evidence_available_at_that_date":"2021년 하반기 ECH/가성소다 등 염소계 제품 spread 개선과 이익 추정 상향 가능성이 공개 리포트/시장 코멘터리에서 논의되던 구간. 2021-09-01 stock-web close 70,500 이후 2021-09-29 high 101,500.","evidence_source":"public commodity-spread commentary; company earnings visibility; stock-web 004000 2021 row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004000/2021.csv","profile_path":"atlas/symbol_profiles/004/004000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":43.97,"MFE_90D_pct":43.97,"MFE_180D_pct":43.97,"MFE_1Y_pct":43.97,"MFE_2Y_pct":null,"MAE_30D_pct":-0.99,"MAE_90D_pct":-0.99,"MAE_180D_pct":-7.38,"MAE_1Y_pct":-17.16,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-09-29","peak_price":101500,"drawdown_after_peak_pct":-35.67,"green_lateness_ratio":0.38,"four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_margin_bridge","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L15_C17_T02_KOLONIND_20210202_STAGE2","case_id":"R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE","symbol":"120110","company_name":"코오롱인더","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"TIRECORD_ARAMID_MARGIN_BRIDGE","sector":"산업소재·화학","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-02","entry_date":"2021-02-02","entry_price":49100,"evidence_available_at_that_date":"2021년 초 산업소재/tirecord/aramid 회복이 단순 가격 반등이 아니라 이익 가시성과 연결되던 구간. 2021-02-02 stock-web close 49,100 이후 2021-09-24 high 114,500.","evidence_source":"public product-spread/reopening commentary; company margin visibility; stock-web 120110 2021 row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/120/120110/2021.csv","profile_path":"atlas/symbol_profiles/120/120110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.35,"MFE_90D_pct":68.84,"MFE_180D_pct":133.2,"MFE_1Y_pct":133.2,"MFE_2Y_pct":null,"MAE_30D_pct":-1.63,"MAE_90D_pct":-1.63,"MAE_180D_pct":-1.63,"MAE_1Y_pct":-9.98,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-09-24","peak_price":114500,"drawdown_after_peak_pct":-38.08,"green_lateness_ratio":0.49,"four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_operating_leverage","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L15_C17_T03_HANWHA_20200803_STAGE2","case_id":"R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PVC_CAUSTIC_SOLAR_SPREAD_OPERATING_LEVERAGE","sector":"PVC·태양광·화학","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2020-08-03","entry_date":"2020-08-03","entry_price":25850,"evidence_available_at_that_date":"2020년 하반기 PVC/가성소다 및 태양광 밸류체인 회복이 동반되며 화학 spread가 실적 레버리지로 번역되던 구간. 2020-08-03 close 25,850 이후 2020-09~2021-01에 강한 MFE.","evidence_source":"public chemical/PVC/solar value-chain commentary; stock-web 009830 2020 row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2020.csv","profile_path":"atlas/symbol_profiles/009/009830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":59.19,"MFE_90D_pct":102.32,"MFE_180D_pct":128.63,"MFE_1Y_pct":128.63,"MFE_2Y_pct":null,"MAE_30D_pct":-3.29,"MAE_90D_pct":-3.29,"MAE_180D_pct":-3.29,"MAE_1Y_pct":-3.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-11","peak_price":59100,"drawdown_after_peak_pct":-32.57,"green_lateness_ratio":0.42,"four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_high_MFE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L15_C17_T04_AEKYUNG_20230411_FALSE_GREEN","case_id":"R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE","symbol":"161000","company_name":"애경케미칼","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PLASTICIZER_BATTERY_PROXY_PRICE_ONLY_FALSE_POSITIVE","sector":"가소제·정밀화학","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable false-positive candidate","trigger_date":"2023-04-11","entry_date":"2023-04-11","entry_price":15710,"evidence_available_at_that_date":"2023년 4~6월 price tape는 강했지만, C17 관점에서는 실제 commodity spread → margin bridge → revision으로 이어졌다는 확인이 약했다. price-only move를 Green 근거로 쓰면 false-positive risk가 커진다.","evidence_source":"stock-web 161000 2023 price rows; no verified spread-to-margin bridge in trigger evidence set","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161000/2023.csv","profile_path":"atlas/symbol_profiles/161/161000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":43.86,"MFE_90D_pct":76.96,"MFE_180D_pct":76.96,"MFE_1Y_pct":76.96,"MFE_2Y_pct":null,"MAE_30D_pct":-17.0,"MAE_90D_pct":-17.0,"MAE_180D_pct":-42.71,"MAE_1Y_pct":-48.95,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-22","peak_price":27800,"drawdown_after_peak_pct":-53.96,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_non_price_but_blocks_green","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"false_break","trigger_outcome_label":"price_moved_without_margin_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L15_C17_T05_HYOSUNGCHEM_20210503_FALSE_STAGE2","case_id":"R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER","symbol":"298000","company_name":"효성화학","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PDH_PP_SPREAD_OVERBUILD_HIGH_MAE","sector":"PP·PDH·화학","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable false-positive candidate","trigger_date":"2021-05-03","entry_date":"2021-05-03","entry_price":426500,"evidence_available_at_that_date":"2021년 봄 PP/PDH spread headline만으로는 충분하지 않았다. entry 직후 MAE가 커졌고, later path는 overbuild/execution-risk가 margin bridge를 압도하는 반례가 되었다.","evidence_source":"stock-web 298000 2021 price rows; public commodity spread headline without durable margin conversion","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298000/2021.csv","profile_path":"atlas/symbol_profiles/298/298000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.52,"MFE_90D_pct":11.37,"MFE_180D_pct":11.37,"MFE_1Y_pct":11.37,"MFE_2Y_pct":null,"MAE_30D_pct":-21.1,"MAE_90D_pct":-28.37,"MAE_180D_pct":-50.76,"MAE_1Y_pct":-71.04,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":475000,"drawdown_after_peak_pct":-55.79,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.43,"four_b_full_window_peak_proximity":0.43,"four_b_timing_verdict":"spread_headline_failed_before_full_4B","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk_score"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L15_C17_LOTTEFINE_20210901_ECH_CAUSTIC_POSITIVE","trigger_id":"R4L15_C17_T01_LOTTEFINE_20210901_STAGE2","symbol":"004000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":16,"revision_score":18,"relative_strength_score":14,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":10,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":19,"revision_score":20,"relative_strength_score":14,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":11,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green shadow","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile rewards spread only when it is visible in margin bridge and revision; price-only or headline-only spread is capped and execution risk is raised.","MFE_90D_pct":43.97,"MAE_90D_pct":-0.99,"score_return_alignment_label":"structural_success_margin_bridge","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L15_C17_KOLONIND_20210202_TIRECORD_ARAMID_POSITIVE","trigger_id":"R4L15_C17_T02_KOLONIND_20210202_STAGE2","symbol":"120110","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":15,"revision_score":17,"relative_strength_score":16,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":16,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green shadow","changed_components":["margin_bridge_score","revision_score","relative_strength_score"],"component_delta_explanation":"C17 shadow profile rewards spread only when it is visible in margin bridge and revision; price-only or headline-only spread is capped and execution risk is raised.","MFE_90D_pct":68.84,"MAE_90D_pct":-1.63,"score_return_alignment_label":"structural_success_operating_leverage","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L15_C17_HANWHA_20200803_PVC_SOLAR_SPREAD_POSITIVE","trigger_id":"R4L15_C17_T03_HANWHA_20200803_STAGE2","symbol":"009830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":14,"revision_score":16,"relative_strength_score":18,"customer_quality_score":1,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":17,"revision_score":20,"relative_strength_score":18,"customer_quality_score":1,"policy_or_regulatory_score":4,"valuation_repricing_score":11,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Green shadow","changed_components":["margin_bridge_score","revision_score","relative_strength_score"],"component_delta_explanation":"C17 shadow profile rewards spread only when it is visible in margin bridge and revision; price-only or headline-only spread is capped and execution risk is raised.","MFE_90D_pct":102.32,"MAE_90D_pct":-3.29,"score_return_alignment_label":"structural_success_high_MFE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L15_C17_AEKYUNG_20230411_PLASTICIZER_BATTERY_PROXY_FALSE","trigger_id":"R4L15_C17_T04_AEKYUNG_20230411_FALSE_GREEN","symbol":"161000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":19,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":16,"execution_risk_score":12,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":19,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":10,"execution_risk_score":16,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage1/Watch - price-only proxy","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile rewards spread only when it is visible in margin bridge and revision; price-only or headline-only spread is capped and execution risk is raised.","MFE_90D_pct":76.96,"MAE_90D_pct":-17.0,"score_return_alignment_label":"price_moved_without_margin_bridge","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L15_C17_HYOSUNGCHEM_20210503_PDH_OVERBUILD_COUNTER","trigger_id":"R4L15_C17_T05_HYOSUNGCHEM_20210503_FALSE_STAGE2","symbol":"298000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":11,"execution_risk_score":16,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":3,"revision_score":1,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":20,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54,"stage_label_after":"Stage1/Watch - spread headline only","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C17 shadow profile rewards spread only when it is visible in margin bridge and revision; price-only or headline-only spread is capped and execution risk is raised.","MFE_90D_pct":11.37,"MAE_90D_pct":-28.37,"score_return_alignment_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R4","loop":"15","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","scheduled_round":"R4","scheduled_loop":"15","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":3,"counterexample_count":2,"current_profile_error_count":2,"diversity_score_summary":"5 new C17 symbols/triggers; positive spread-to-margin bridge vs price-only/high-MAE counterexamples","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["chemical_spread_false_positive","price_only_relative_strength_false_green","high_MAE_failed_rerating"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R4
completed_loop = 15
next_round = R5
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Primary price source:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

Source files checked:

```text
- atlas/manifest.json
- atlas/schema.json
- atlas/symbol_profiles/004/004000.json
- atlas/symbol_profiles/120/120110.json
- atlas/symbol_profiles/009/009830.json
- atlas/symbol_profiles/161/161000.json
- atlas/symbol_profiles/298/298000.json
- atlas/ohlcv_tradable_by_symbol_year/004/004000/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/120/120110/2021.csv
- atlas/ohlcv_tradable_by_symbol_year/009/009830/2020.csv
- atlas/ohlcv_tradable_by_symbol_year/161/161000/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/298/298000/2021.csv
```

