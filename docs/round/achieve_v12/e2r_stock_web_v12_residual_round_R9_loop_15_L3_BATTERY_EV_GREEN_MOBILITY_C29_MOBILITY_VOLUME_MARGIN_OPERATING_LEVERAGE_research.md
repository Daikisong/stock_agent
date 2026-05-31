# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
scheduled_round: R9
scheduled_loop: 15
completed_round: R9
completed_loop: 15
next_round: R10
next_loop: 15
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
stock_web_price_atlas_access_required: true
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **3** new independent cases, **1** counterexample, and **3** residual errors for **R9 / L3_BATTERY_EV_GREEN_MOBILITY / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE**.

## 1. Current Calibrated Profile Assumption

Current proxy profile is treated as `e2r_2_1_stock_web_calibrated_proxy`.

Applied global axes assumed in force:

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

This MD does **not** re-prove those global rules. It tests where C29 mobility volume/mix leverage still needs a canonical-archetype shadow rule.

## 2. Round / Large Sector / Canonical Archetype Scope

- `scheduled_round = R9`
- `scheduled_loop = 15`
- R9 is interpreted as mobility / transport nature. The allowed large-sector pair used here is `L3_BATTERY_EV_GREEN_MOBILITY`.
- Canonical archetype: `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE`
- Fine archetype: `AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM`

The selected C29 question:

> When does mobility volume/mix evidence deserve early Actionable credit, and when does a mega-customer rumor only create a 4B/4C risk overlay?

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were treated as duplicate-avoidance references only. No `src/e2r` code was opened.

Selection notes:

- Previous generated local MD ended at `R8 / loop 15`; this execution follows `next_round = R9`.
- Available registry samples showed older `e2r_stock_web_historical_calibration_round_*` files, not a completed v12 `R9 loop 15 C29` residual MD.
- Same canonical archetype repetition is allowed, but same symbol + same trigger + same entry is not repeated from prior v12 output.

Diversity decision:

```text
new_independent_case_count = 3
new_symbol_count = 2
new_trigger_family_count = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 3
diversity_score_summary = "new C29 auto-EV volume/mix bridge + mega-customer rumor redteam"
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

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
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Validation row:

```json
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All representative trigger rows pass the 180-trading-day historical eligibility gate:

| case_id | symbol | entry_date | forward window | corporate action 180D | calibration_usable |
|---|---:|---:|---:|---|---|
| R9L15_C29_005380_EGMP_VOLUME_MIX_20201202 | 005380 | 2020-12-02 | >=180D | clean | true |
| R9L15_C29_000270_Q3_VOLUME_MIX_20201026 | 000270 | 2020-10-26 | >=180D | clean | true |
| R9L15_C29_000270_APPLE_RUMOR_FALSE_GREEN_20210203 | 000270 | 2021-02-03 | >=180D | clean | true |

Profile checks:

- `005380` has old corporate-action candidates only in 1998-1999; the 2020-12 to 2021-08 window is clean.
- `000270` has old corporate-action candidates only in 1999; the 2020-10 to 2021-10 window is clean.
- Both symbols have `price_adjustment_status = raw_unadjusted_marcap`.

## 6. Canonical Archetype Compression Map

```text
fine_archetype: AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
```

Compression logic:

- EV platform / dedicated platform / volume recovery / model mix improvement all compress into C29.
- Rumor-driven mega-customer headlines are not C29 positives unless converted into contract / production / delivery / margin evidence.
- Price-only local peaks in C29 are treated as 4B overlays, not full Stage4B exits, unless non-price overheat or explicit event-cap evidence exists.

## 7. Case Selection Summary

| case_id | symbol | role | trigger family | new independent | reason |
|---|---:|---|---|---|---|
| R9L15_C29_005380_EGMP_VOLUME_MIX_20201202 | 005380 | structural_success | EV platform volume/mix route | true | EV platform disclosure mapped to volume/mix operating leverage. |
| R9L15_C29_000270_Q3_VOLUME_MIX_20201026 | 000270 | structural_success | Q3 margin/volume mix recovery | true | Earnings visibility preceded major rerating. |
| R9L15_C29_000270_APPLE_RUMOR_FALSE_GREEN_20210203 | 000270 | false_positive_green | unconfirmed mega-customer rumor | true | Strong price reaction without binding customer/order/margin evidence. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 3
```

Balance verdict: pass.

The useful split is not “EV car good / rumor bad.” It is more mechanical:

- **Positive C29** = volume or platform path plus earnings / margin visibility.
- **Counterexample C29** = customer-like rumor without contract, production allocation, delivery visibility, or margin bridge.
- **4B/4C overlay** = price or event risk can protect the cycle, but cannot promote Stage2/Stage3.

## 9. Evidence Source Map

| trigger | evidence family | evidence available at trigger date | use in score |
|---|---|---|---|
| T001 | public EV platform | E-GMP dedicated platform disclosed on 2020-12-02 | positive Stage2/Yellow, not immediate Green |
| T002 | price-only overheat | local peak after E-GMP and Apple-related excitement | 4B overlay only |
| T003 | volume/mix earnings | Q3 2020 volume/mix recovery and financial visibility | positive Stage2/Yellow |
| T004 | unconfirmed customer rumor | Apple-car rumor / speculative customer expectation | counterexample; cap customer_quality |
| T005 | explicit thesis break | Hyundai/Kia no longer in talks with Apple | 4C thesis-break route |

## 10. Price Data Source Map

| symbol | shard path | profile path | entry rows checked |
|---:|---|---|---|
| 005380 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2020.csv; 2021.csv | atlas/symbol_profiles/005/005380.json | 2020-12-02, 2021-01-11 |
| 000270 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2020.csv; 2021.csv | atlas/symbol_profiles/000/000270.json | 2020-10-26, 2021-02-03, 2021-02-08 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case | type | entry | price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | peak | current verdict | aggregate |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| R9L15_T001 | 005380 현대차 | Stage2-Actionable | 2020-12-02 | 182,500 | 58.36 | 58.36 | 58.36 | -0.55 | -0.55 | 2021-01-11 289,000 | current_profile_too_late | representative |
| R9L15_T002 | 005380 현대차 | 4B-overlay-price-only | 2021-01-11 | 267,500 | 8.04 | 8.04 | 8.04 | -14.39 | -20.75 | 2021-01-11 289,000 | current_profile_correct | 4B_overlay_only |
| R9L15_T003 | 000270 기아 | Stage2-Actionable | 2020-10-26 | 47,950 | 38.89 | 112.72 | 112.72 | -5.32 | -5.32 | 2021-02-03 102,000 | current_profile_too_late | representative |
| R9L15_T004 | 000270 기아 | Stage2-rumor-redteam | 2021-02-03 | 97,700 | 4.4 | 4.4 | 4.4 | -23.95 | -23.95 | 2021-02-03 102,000 | current_profile_false_positive | representative |
| R9L15_T005 | 000270 기아 | 4C-thesis-break | 2021-02-08 | 86,300 | 2.67 | 8.57 | 8.57 | -13.9 | -13.9 | 2021-06-24 93,700 | current_profile_4C_too_late | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate rows

| trigger | entry | entry_price | max_high_30D | min_low_30D | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T001 Hyundai E-GMP | 2020-12-02 | 182,500 | 289,000 | 181,500 | 58.36 | -0.55 | 58.36 | -0.55 | 58.36 | -0.55 |
| T003 Kia Q3 mix | 2020-10-26 | 47,950 | 66,600 | 45,400 | 38.89 | -5.32 | 112.72 | -5.32 | 112.72 | -5.32 |
| T004 Kia Apple rumor | 2021-02-03 | 97,700 | 102,000 | 74,300 | 4.40 | -23.95 | 4.40 | -23.95 | 4.40 | -23.95 |

### Overlay rows

| trigger | role | entry | entry_price | max_high_90D | min_low_90D | MFE90 | MAE90 | purpose |
|---|---|---:|---:|---:|---:|---:|---:|---|
| T002 | 4B price-only overlay | 2021-01-11 | 267,500 | 289,000 | 212,000 | 8.04 | -20.75 | test price-only local peak guard |
| T005 | 4C thesis break | 2021-02-08 | 86,300 | 93,700 | 74,300 | 8.57 | -13.90 | test explicit denial / thesis-break routing |

## 13. Current Calibrated Profile Stress Test

### Case conclusions

| case | current profile likely label | actual price path | verdict |
|---|---|---|---|
| Hyundai E-GMP | may wait for confirmed delivery/revision before Green | +58.36% MFE with <1% early MAE | current_profile_too_late |
| Kia Q3 volume/mix | may be Yellow but Green only later | +112.72% MFE before full confirmation | current_profile_too_late |
| Kia Apple rumor | may over-score relative strength + customer-like rumor | +4.40% MFE / -23.95% MAE | current_profile_false_positive |
| Kia Apple denial 4C | may wait for price damage | explicit denial already breaks thesis | current_profile_4C_too_late |

Answers to required stress-test questions:

1. The current calibrated profile is directionally correct on price-only blowoff and non-price 4B requirements, but C29 needs a sharper distinction between **conversion bridge** and **customer rumor**.
2. MFE/MAE alignment supports early Actionable credit for confirmed volume/mix evidence.
3. Stage2 bonus is insufficient for Hyundai/Kia volume/mix positives when evidence is public and clean.
4. Yellow threshold 75 is mostly right, but C29 should allow earlier Actionable when margin bridge and volume route coexist.
5. Green threshold 87 and revision 55 should not be weakened globally; C29 Green should require conversion evidence.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is appropriate.
8. Hard 4C should route faster when the thesis is explicitly denied.

## 14. Stage2 / Yellow / Green Comparison

C29 Green should not simply be earlier. The point is to separate two corridors:

```text
Corridor A: Stage2/Yellow should be earlier when volume/mix + margin bridge are visible.
Corridor B: Green should stay strict unless conversion bridge exists.
```

For Hyundai and Kia Q3, Stage2/Yellow captured large MFE before a fully confirmed Green. For the Apple-rumor case, a looser Green would have been wrong.

`green_lateness_ratio` is `not_applicable` because no clean confirmed Green trigger was selected. The residual is not a generic Green-lateness proof; it is a C29-specific conversion bridge requirement.

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| T002 Hyundai price-only peak | 0.798 | 0.798 | price_only, positioning_overheat | price-only local 4B; do not treat as full 4B |
| T004 Kia Apple rumor peak | 0.920 | 0.920 | valuation_blowoff, positioning_overheat, explicit_event_cap | good 4B risk overlay, but not positive Stage3 evidence |

C29-specific audit finding:

> A mobility name can approach full-window peak on a customer rumor, but the same row should be a 4B risk overlay, not a Stage3-Green promotion.

## 16. 4C Protection Audit

Kia Apple denial row:

```text
prior_peak_price = 102000
4C_entry_price = 86300
post_4C_min_low_90D = 74300
max_drawdown_after_peak_from_prior_stage = (74300 / 102000 - 1) = -27.16%
MAE_90D_after_4C = (74300 / 86300 - 1) = -13.90%
four_c_protection_score ≈ 0.488
four_c_protection_label = hard_4c_success
```

This supports keeping `hard_4c_thesis_break_routes_to_4c`, and for C29 suggests that explicit customer-denial rows should not wait for additional price confirmation.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = sample is concentrated in Korean auto/EV mobility names, not broad enough for whole L3 mobility/transport.
```

No broad sector rule is proposed.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

Candidate shadow rules:

1. `C29_volume_mix_bridge_actionable_bonus = +2 shadow`
   - Applies when public event/disclosure plus financial or margin visibility gives a plausible operating leverage route.
   - Does not promote directly to Green.

2. `C29_conversion_bridge_required_for_green = true`
   - Green requires at least one of: confirmed shipment/delivery, repeat order, production allocation, margin bridge, or hard revision.
   - Relative strength and broad EV narrative cannot substitute.

3. `C29_unconfirmed_mega_customer_rumor_caps_customer_quality_score = 0`
   - Mega-customer rumor cannot score as customer quality unless named counterparty + binding agreement / production allocation / delivery route exists.

4. `C29_explicit_customer_denial_routes_to_4C = true`
   - When the entire thesis is a specific customer partnership and the company denies talks, route to 4C watch/4C depending on event clarity.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | false_positive_rate | missed_structural | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 3 | 58.49 | -9.94 | 0.33 | 2 | mixed; strong positives but rumor false-positive remains |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 3 | 58.49 | -9.94 | 0.33 | 2 | worse; rumor customer-quality misclassification larger |
| P1_sector_specific_candidate_profile | sector_specific | 3 | 58.49 | -9.94 | 0.33 | 1 | improves positive timing but still needs C29 rumor guard |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 3 | 58.49 | -9.94 | 0.0 | 0 | best balance; positives remain Actionable, rumor blocked |
| P3_counterexample_guard_profile | counterexample_guard | 1 | 4.4 | -23.95 | 0.0 | 0 | blocks the residual false-positive |

## 20. Score-Return Alignment Matrix

| trigger | current score issue | return evidence | proposed alignment |
|---|---|---|---|
| T001 | too slow on public platform + volume/mix | +58.36% MFE, almost no early MAE | add Actionable credit, keep Green strict |
| T003 | too slow on Q3 volume/mix margin recovery | +112.72% MFE | add Actionable credit, watch later rumor overextension |
| T004 | over-scores customer-like rumor | +4.40% MFE / -23.95% MAE | cap customer_quality; treat as 4B risk |
| T005 | 4C may arrive late if waiting for price | explicit denial precedes drawdown | route thesis-break faster |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM | 2 | 1 | 2 | 1 | 3 | 0 | 5 | 3 | 3 | false | true | C29 still needs non-Korea holdout and non-auto transport sample, but the core auto EV/mix false-positive guard is now covered. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_symbol_count: 2
same_archetype_new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late_for_C29_volume_mix_bridge
  - current_profile_false_positive_on_unconfirmed_mega_customer_rumor
  - current_profile_4C_too_late_after_explicit_denial
new_axis_proposed:
  - C29_volume_mix_bridge_actionable_bonus
  - C29_conversion_bridge_required_for_green
  - C29_unconfirmed_mega_customer_rumor_caps_customer_quality_score
  - C29_explicit_customer_denial_routes_to_4C
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual stock-web tradable OHLC rows for selected entry dates and observed forward windows.
- Manifest max-date based forward-window availability.
- Corporate-action windows via symbol profiles.
- Trigger-level MFE/MAE/peak/drawdown values for the selected historical rows.
- Positive/counterexample balance for C29.

Not validated:

- No live watchlist.
- No 2026 current candidate scan.
- No `stock_agent/src` code inspection.
- No production scoring patch.
- No brokerage or automated trading route.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_volume_mix_bridge_actionable_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,+2,+2,"public volume/mix + margin bridge moved before confirmed Green","improves Hyundai/Kia positive timing without weakening Green","R9L15_T001|R9L15_T003",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_conversion_bridge_required_for_green,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,false,true,+1,"rumor-only customer narratives fail MFE/MAE alignment","blocks Kia Apple false-positive","R9L15_T004",1,1,1,medium,canonical_shadow_only,"not production; do not weaken global Green"
shadow_weight,C29_unconfirmed_mega_customer_rumor_caps_customer_quality_score,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,none,0,-1,"unconfirmed customer rumor has poor return alignment","reduces false positive rate from 0.33 to 0.0 in this set","R9L15_T004",1,1,1,medium,counterexample_guard,"not production; risk guard"
shadow_weight,C29_explicit_customer_denial_routes_to_4C,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,false,true,+1,"specific customer thesis breaks when company denies talks","earlier 4C protection label","R9L15_T005",1,0,1,medium,canonical_shadow_only,"4C overlay, not entry promotion"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L15_C29_005380_EGMP_VOLUME_MIX_20201202","symbol":"005380","company_name":"현대차","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L15_T001","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"E-GMP 전용 EV 플랫폼 공개는 단순 가격 모멘텀이 아니라, 차종 확장과 플랫폼 공용화로 volume/mix operating leverage를 설명하는 public event였다."}
{"row_type":"case","case_id":"R9L15_C29_000270_Q3_VOLUME_MIX_20201026","symbol":"000270","company_name":"기아","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L15_T003","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2020년 하반기 volume/mix 회복과 전동화 내러티브가 operating leverage로 연결된 케이스. 다만 후속 Apple-car rumor가 peak를 과장했으므로 4B overlay를 별도 분리한다."}
{"row_type":"case","case_id":"R9L15_C29_000270_APPLE_RUMOR_FALSE_GREEN_20210203","symbol":"000270","company_name":"기아","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R9L15_T004","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false-positive risk exposed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"특정 대형 고객/Apple car rumor는 customer_quality처럼 보였지만 확정 계약·마진 bridge·capacity conversion이 없었다. current profile이 단순 price+rumor를 Green에 가깝게 밀면 false positive다."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R9L15_T001","case_id":"R9L15_C29_005380_EGMP_VOLUME_MIX_20201202","symbol":"005380","company_name":"현대차","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM","sector":"mobility_auto_ev","primary_archetype":"EV platform volume/mix operating leverage","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-12-02","evidence_available_at_that_date":"Hyundai Motor Group E-GMP dedicated EV platform 공개. EV lineup 확장과 platform commonization이 volume/mix path를 설명.","evidence_source":"Hyundai Motor Group E-GMP public release / public news on 2020-12-02","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2020.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-12-02","entry_price":182500,"MFE_30D_pct":58.36,"MFE_90D_pct":58.36,"MFE_180D_pct":58.36,"MFE_1Y_pct":58.36,"MFE_2Y_pct":58.36,"MAE_30D_pct":-0.55,"MAE_90D_pct":-0.55,"MAE_180D_pct":-0.55,"MAE_1Y_pct":-0.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-11","peak_price":289000,"drawdown_after_peak_pct":-26.64,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_005380_20201202_182500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L15_T002","case_id":"R9L15_C29_005380_EGMP_VOLUME_MIX_20201202","symbol":"005380","company_name":"현대차","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM","sector":"mobility_auto_ev","primary_archetype":"price-only local peak after EV platform rerating","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay-price-only","trigger_date":"2021-01-11","evidence_available_at_that_date":"주가가 E-GMP/Apple-car 기대를 흡수하며 local peak에 접근했지만, 이 row는 non-price 4B evidence가 아니라 price-only local peak audit이다.","evidence_source":"stock-web OHLC row; no independent non-price 4B evidence used","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2021.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-11","entry_price":267500,"MFE_30D_pct":8.04,"MFE_90D_pct":8.04,"MFE_180D_pct":8.04,"MFE_1Y_pct":8.04,"MFE_2Y_pct":8.04,"MAE_30D_pct":-14.39,"MAE_90D_pct":-20.75,"MAE_180D_pct":-20.75,"MAE_1Y_pct":-26.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-11","peak_price":289000,"drawdown_after_peak_pct":-26.64,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.798,"four_b_full_window_peak_proximity":0.798,"four_b_timing_verdict":"price_only_local_4B_too_early_for_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success_price_only_not_full_exit","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_005380_20210111_267500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay; not representative entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R9L15_T003","case_id":"R9L15_C29_000270_Q3_VOLUME_MIX_20201026","symbol":"000270","company_name":"기아","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM","sector":"mobility_auto","primary_archetype":"volume/mix operating leverage","loop_objective":"coverage_gap_fill|yellow_threshold_stress_test|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2020-10-26","evidence_available_at_that_date":"Q3 2020 volume/mix recovery and earnings visibility became visible; entry uses same-day tradable close.","evidence_source":"Kia Q3 2020 earnings / public financial visibility; stock-web 2020 row","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2020.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-10-26","entry_price":47950,"MFE_30D_pct":38.89,"MFE_90D_pct":112.72,"MFE_180D_pct":112.72,"MFE_1Y_pct":112.72,"MFE_2Y_pct":112.72,"MAE_30D_pct":-5.32,"MAE_90D_pct":-5.32,"MAE_180D_pct":-5.32,"MAE_1Y_pct":-5.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-03","peak_price":102000,"drawdown_after_peak_pct":-27.16,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_with_later_rumor_overextension","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_000270_20201026_47950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L15_T004","case_id":"R9L15_C29_000270_APPLE_RUMOR_FALSE_GREEN_20210203","symbol":"000270","company_name":"기아","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM","sector":"mobility_auto","primary_archetype":"unconfirmed mega-customer rumor redteam","loop_objective":"residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-rumor-redteam","trigger_date":"2021-02-03","evidence_available_at_that_date":"Apple-car 관련 보도/기대가 가격에 반영됐지만 specific signed customer, order, margin bridge, committed capacity가 없었다.","evidence_source":"Reuters/CNBC-type Apple car rumor public reports; stock-web 2021 row","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2021.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-03","entry_price":97700,"MFE_30D_pct":4.4,"MFE_90D_pct":4.4,"MFE_180D_pct":4.4,"MFE_1Y_pct":4.4,"MFE_2Y_pct":4.4,"MAE_30D_pct":-23.95,"MAE_90D_pct":-23.95,"MAE_180D_pct":-23.95,"MAE_1Y_pct":-23.95,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-03","peak_price":102000,"drawdown_after_peak_pct":-27.16,"green_lateness_ratio":"not_applicable:false_positive_rumor","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_full_window_4B_timing_if_treated_as_risk_overlay_not_positive_stage","four_b_evidence_type":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only_before_2021_02_08","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_000270_20210203_97700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L15_T005","case_id":"R9L15_C29_000270_APPLE_RUMOR_FALSE_GREEN_20210203","symbol":"000270","company_name":"기아","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EV_VOLUME_MIX_OPERATING_LEVERAGE_AND_RUMOR_REDTEAM","sector":"mobility_auto","primary_archetype":"explicit thesis break after rumor","loop_objective":"4C_thesis_break_timing_test|counterexample_mining","trigger_type":"4C-thesis-break","trigger_date":"2021-02-08","evidence_available_at_that_date":"Hyundai/Kia가 Apple과 자율주행차 개발 협의 중이 아니라고 밝힌 뒤, rumor-driven thesis가 깨졌다.","evidence_source":"Reuters 2021-02-08 / public disclosure; stock-web 2021 row","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken","contract_cancelled"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2021.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-08","entry_price":86300,"MFE_30D_pct":2.67,"MFE_90D_pct":8.57,"MFE_180D_pct":8.57,"MFE_1Y_pct":8.57,"MFE_2Y_pct":8.57,"MAE_30D_pct":-13.9,"MAE_90D_pct":-13.9,"MAE_180D_pct":-13.9,"MAE_1Y_pct":-13.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-24","peak_price":93700,"drawdown_after_peak_pct":-20.7,"green_lateness_ratio":"not_applicable:4C_overlay","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_000270_20210208_86300","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same false-positive case; explicit thesis-break overlay only","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L15_C29_005380_EGMP_VOLUME_MIX_20201202","trigger_id":"R9L15_T001","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":10,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-Actionable","changed_components":["margin_bridge_score","revision_score"],"component_delta_explanation":"EV platform public event needs volume/mix bridge credit but no immediate Green without confirmed deliveries.","MFE_90D_pct":58.36,"MAE_90D_pct":-0.55,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L15_C29_000270_Q3_VOLUME_MIX_20201026","trigger_id":"R9L15_T003","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":12,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":12,"revision_score":12,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow-Actionable","changed_components":["margin_bridge_score"],"component_delta_explanation":"Volume/mix operating leverage deserves earlier Yellow/Actionable, not late Green.","MFE_90D_pct":112.72,"MAE_90D_pct":-5.32,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L15_C29_000270_APPLE_RUMOR_FALSE_GREEN_20210203","trigger_id":"R9L15_T004","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":14,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":0,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow-risky","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":15,"execution_risk_score":0,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-Risk/4B-watch","changed_components":["customer_quality_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"Rumor must not score as confirmed customer quality; risk overlay should dominate.","MFE_90D_pct":4.4,"MAE_90D_pct":-23.95,"score_return_alignment_label":"current_profile_false_positive_risk","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L15_C29_000270_APPLE_RUMOR_FALSE_GREEN_20210203","trigger_id":"R9L15_T005","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":0,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":0,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":48,"stage_label_after":"4C-thesis-break","changed_components":["legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"Explicit denial routes the rumor case to 4C, not just 4B watch.","MFE_90D_pct":8.57,"MAE_90D_pct":-13.9,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4C_too_late"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late_for_volume_mix","current_profile_false_positive_on_unconfirmed_mega_customer_rumor","current_profile_4C_too_late_after_explicit_denial"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.6 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"all selected cases have sufficient 180D forward windows; no narrative-only row needed","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R9
completed_loop = 15
next_round = R10
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files directly checked:

- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/symbol_profiles/005/005380.json`
- `atlas/symbol_profiles/000/000270.json`
- `atlas/ohlcv_tradable_by_symbol_year/005/005380/2020.csv`
- `atlas/ohlcv_tradable_by_symbol_year/005/005380/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/000/000270/2020.csv`
- `atlas/ohlcv_tradable_by_symbol_year/000/000270/2021.csv`

Historical public evidence notes:

- Hyundai Motor Group E-GMP public release / public news, 2020-12-02.
- Kia Q3 2020 earnings / volume-mix financial visibility, 2020-10-26.
- Kia / Hyundai Apple-car rumor and denial sequence, 2021-01-20 to 2021-02-08.

No live candidate discovery, no stock recommendation, no `stock_agent` code inspection, and no production scoring change were performed.

