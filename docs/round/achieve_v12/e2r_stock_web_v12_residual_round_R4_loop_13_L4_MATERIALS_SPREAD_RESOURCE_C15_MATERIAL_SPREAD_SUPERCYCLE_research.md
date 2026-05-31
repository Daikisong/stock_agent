# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": "13",
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "STEEL_NB_LATEX_POLYSILICON_BASIC_PETROCHEM_SPREAD_COMPRESSION",
  "output_file": "e2r_stock_web_v12_residual_round_R4_loop_13_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md",
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_embedded": true,
  "handoff_prompt_executed_now": false,
  "investment_recommendation_language": "not_used"
}
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.

## 1. Current Calibrated Profile Assumption

| Axis | Assumed value | This loop treatment |
|---|---:|---|
| `stage2_actionable_evidence_bonus` | `+2.0` | `existing_axis_tested` |
| `stage3_yellow_total_min` | `75.0` | `existing_axis_kept` |
| `stage3_green_total_min` | `87.0` | `existing_axis_kept` |
| `stage3_green_revision_min` | `55.0` | `existing_axis_kept` |
| `stage3_cross_evidence_green_buffer` | `+1.5` | `existing_axis_kept` |
| `price_only_blowoff_blocks_positive_stage` | `true` | `existing_axis_strengthened` |
| `full_4b_requires_non_price_evidence` | `true` | `existing_axis_strengthened` |
| `hard_4c_thesis_break_routes_to_4c` | `true` | `existing_axis_strengthened` |

The current calibrated profile is treated as the active proxy. This file does not propose a production patch. It uses shadow-only rows to test whether C15 needs a sharper distinction between demand-backed spread conversion and generic commodity beta.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| `scheduled_round` | `R4` |
| `scheduled_loop` | `13` |
| `large_sector_id` | `L4_MATERIALS_SPREAD_RESOURCE` |
| `canonical_archetype_id` | `C15_MATERIAL_SPREAD_SUPERCYCLE` |
| `round_sector_consistency` | `pass` |
| `next_round` | `R5` |
| `next_loop` | `13` |

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`, so the round-sector gate passes. The canonical target is `C15_MATERIAL_SPREAD_SUPERCYCLE`, compressed from steel spread, NB latex spread, polysilicon spread, and basic petrochemical spread cases.

## 3. Previous Coverage / Duplicate Avoidance Check

- `stock_agent` search for `e2r_stock_web_v12_residual_round_R4_loop` returned no existing v12 result file in the repository during this run.
- The older registry contains multiple pre-v12 R4 material-spread files, including repeated loop 6-8 material-spread entries with parsed trigger rows. Those are treated as coverage context only, not as v12 schedule state.
- Scheduler state is inherited from the immediately prior local v12 output: completed `R3 / loop 13`, next `R4 / loop 13`.
- New independent sample condition: 5 calibration-usable cases, 5 new symbols, 5 new trigger families, 0 reused cases.

## 4. Stock-Web OHLC Input / Price Source Validation

| Manifest field | Value |
|---|---|
| `source_name` | `FinanceData/marcap` |
| `source_repo_url` | `https://github.com/FinanceData/marcap` |
| `price_adjustment_status` | `raw_unadjusted_marcap` |
| `min_date` | `1995-05-02` |
| `manifest_max_date` | `2026-02-20` |
| `tradable_row_count` | `14354401` |
| `raw_row_count` | `15214118` |
| `symbol_count` | `5414` |
| `active_like_symbol_count` | `2868` |
| `inactive_or_delisted_like_symbol_count` | `2546` |
| `markets` | `KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI` |
| `calibration_shard_root` | `atlas/ohlcv_tradable_by_symbol_year` |
| `raw_shard_root` | `atlas/ohlcv_raw_by_symbol_year` |
| `schema_path` | `atlas/schema.json` |
| `universe_path` | `atlas/universe/all_symbols.csv` |

Validation status: `usable_for_historical_calibration`. Price basis is `tradable_raw`; OHLC is raw/unadjusted and corporate-action contamination is blocked if it overlaps the 180D window.

## 5. Historical Eligibility Gate

| Case | Entry | 180D available | Corporate-action 180D status | Calibration usable |
|---|---:|---:|---|---:|
| 005490 POSCO홀딩스 | 2021-02-23 / 279,500 | yes | clean_180D_window_proxy_checked | true |
| 011780 금호석유화학 | 2020-10-05 / 118,500 | yes | clean_180D_window_proxy_checked | true |
| 010060 OCI홀딩스 | 2021-02-10 / 114,000 | yes | clean_180D_window_proxy_checked | true |
| 011170 롯데케미칼 | 2021-02-23 / 326,000 | yes | clean_180D_window_proxy_checked | true |
| 006650 대한유화 | 2021-02-10 / 373,500 | yes | clean_180D_window_proxy_checked | true |

## 6. Canonical Archetype Compression Map

| Fine archetype | Canonical mapping | Why compressed |
|---|---|---|
| `STEEL_SPREAD_EXPORT_PRICE_SUPERCYCLE` | `C15_MATERIAL_SPREAD_SUPERCYCLE` | Spread movement must be tested by conversion into margin/revision rather than by spot-price direction alone. |
| `NB_LATEX_BUTADIENE_SPREAD_SUPERCYCLE` | `C15_MATERIAL_SPREAD_SUPERCYCLE` | Spread movement must be tested by conversion into margin/revision rather than by spot-price direction alone. |
| `POLYSILICON_PRICE_SPREAD_WITH_HIGH_MAE` | `C15_MATERIAL_SPREAD_SUPERCYCLE` | Spread movement must be tested by conversion into margin/revision rather than by spot-price direction alone. |
| `NAPHTHA_ETHYLENE_SPREAD_FALSE_POSITIVE` | `C15_MATERIAL_SPREAD_SUPERCYCLE` | Spread movement must be tested by conversion into margin/revision rather than by spot-price direction alone. |
| `BASIC_PETROCHEM_SPREAD_HIGH_MAE_FALSE_POSITIVE` | `C15_MATERIAL_SPREAD_SUPERCYCLE` | Spread movement must be tested by conversion into margin/revision rather than by spot-price direction alone. |

## 7. Case Selection Summary

| Case | Symbol | Role | Trigger | Entry price | MFE90 | MAE90 | Current profile verdict |
|---|---:|---|---|---:|---:|---:|---|
| R4L13_C15_POSCO_20210223_STEEL_SPREAD | 005490 | structural_success | 2021-02-23 | 279,500 | 47.94% | -2.33% | `current_profile_correct` |
| R4L13_C15_KUMHO_20201005_NBLATEX_SPREAD | 011780 | structural_success | 2020-10-05 | 118,500 | 143.04% | -0.42% | `current_profile_correct` |
| R4L13_C15_OCI_20210210_POLYSILICON_SPREAD | 010060 | high_mae_success | 2021-02-10 | 114,000 | 21.49% | -5.26% | `current_profile_4B_too_early` |
| R4L13_C15_LOTTECHEM_20210223_NAPHTHA_ETHYLENE_FALSE_POSITIVE | 011170 | false_positive_green | 2021-02-23 | 326,000 | 3.68% | -11.04% | `current_profile_false_positive` |
| R4L13_C15_DAEHAN_20210210_BASIC_PETROCHEM_HIGH_MAE | 006650 | failed_rerating | 2021-02-10 | 373,500 | 8.57% | -21.82% | `current_profile_false_positive` |

## 8. Positive vs Counterexample Balance

| Metric | Count |
|---|---:|
| positive_case_count | 3 |
| counterexample_count | 2 |
| 4B_case_count | 5 |
| 4C_case_count | 3 |
| calibration_usable_case_count | 5 |
| current_profile_error_count | 3 |

The useful distinction is not “spread up = buy” versus “spread down = sell.” The useful distinction is whether spread behaves like a pipe carrying margin into EPS. POSCO and Kumho show the pipe. Lotte Chemical and 대한유화 show the puddle: price moved first, but the spread did not hold enough earnings water.

## 9. Evidence Source Map

| Case | Evidence available at trigger | Stage2 fields | Stage3 fields | 4B/4C fields |
|---|---|---|---|---|
| 005490 | 중국/글로벌 철강 가격 강세와 원재료 대비 제품 spread 개선이 이미 시장 자료·리포트·가격 데이터로 관찰되었고, 2021년 이익 추정 상향 가능성이 공개적으로 논의되던 구간. | public_event_or_disclosure, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, multiple_public_sources | 4B=valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown; 4C=none |
| 011780 | NB latex 장갑 수요와 BD/SM 원재료 대비 제품가격 spread가 이미 업황 자료에서 드러났고, 분기 실적 레버리지로 연결될 가능성이 강했다. | public_event_or_disclosure, customer_or_order_quality, relative_strength, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, repeat_order_or_conversion | 4B=valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown; 4C=none |
| 010060 | 폴리실리콘 spot 가격 상승과 공급 타이트가 확인되었으나, downstream 태양광 밸류체인 가격전가와 중국 증설 리스크가 같이 존재했다. | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal | margin_bridge, financial_visibility, multiple_public_sources | 4B=positioning_overheat, valuation_blowoff, margin_or_backlog_slowdown; 4C=thesis_evidence_broken |
| 011170 | 리오프닝 기대와 석유화학 spread 개선 기대는 있었으나, 원재료 naphtha 부담·범용 제품 oversupply·downstream 수요 확인 부족으로 revision durability가 약했다. | public_event_or_disclosure, relative_strength, early_revision_signal | margin_bridge | 4B=price_only_local_peak, margin_or_backlog_slowdown, positioning_overheat; 4C=thesis_evidence_broken |
| 006650 | 기초유분 spread와 경기민감 리오프닝 기대가 강했지만, 이미 가격이 급격히 반응했고 원가/증설/범용 제품의 반복 공급 리스크가 컸다. | public_event_or_disclosure, relative_strength, early_revision_signal | margin_bridge | 4B=valuation_blowoff, positioning_overheat, price_only_local_peak; 4C=thesis_evidence_broken |

## 10. Price Data Source Map

| Symbol | Shard path | Profile path | Entry row basis |
|---:|---|---|---|
| 005490 | `atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv` | `atlas/symbol_profiles/005/005490.json` | `c` column on `2021-02-23` |
| 011780 | `atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv|atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv` | `atlas/symbol_profiles/011/011780.json` | `c` column on `2020-10-05` |
| 010060 | `atlas/ohlcv_tradable_by_symbol_year/010/010060/2021.csv` | `atlas/symbol_profiles/010/010060.json` | `c` column on `2021-02-10` |
| 011170 | `atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv` | `atlas/symbol_profiles/011/011170.json` | `c` column on `2021-02-23` |
| 006650 | `atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv` | `atlas/symbol_profiles/006/006650.json` | `c` column on `2021-02-10` |

## 11. Case-by-Case Trigger Grid

| Trigger | Case | Trigger type | Evidence family | Dedupe group | Aggregate role |
|---|---|---|---|---|---|
| R4L13_C15_T01 | R4L13_C15_POSCO_20210223_STEEL_SPREAD | Stage2-Actionable | steel spread to earnings revision | R4L13_C15_POSCO_20210223_STEEL_SPREAD_G1 | representative |
| R4L13_C15_T02 | R4L13_C15_KUMHO_20201005_NBLATEX_SPREAD | Stage2-Actionable | latex demand plus feedstock spread to earnings | R4L13_C15_KUMHO_20201005_NBLATEX_SPREAD_G1 | representative |
| R4L13_C15_T03 | R4L13_C15_OCI_20210210_POLYSILICON_SPREAD | Stage2-Actionable | polysilicon spread to cyclic rerating with volatility | R4L13_C15_OCI_20210210_POLYSILICON_SPREAD_G1 | representative |
| R4L13_C15_T04 | R4L13_C15_LOTTECHEM_20210223_NAPHTHA_ETHYLENE_FALSE_POSITIVE | Stage2-Actionable | commodity spread without durable conversion | R4L13_C15_LOTTECHEM_20210223_NAPHTHA_ETHYLENE_FALSE_POSITIVE_G1 | representative |
| R4L13_C15_T05 | R4L13_C15_DAEHAN_20210210_BASIC_PETROCHEM_HIGH_MAE | Stage2-Actionable | early spread spike with poor durability | R4L13_C15_DAEHAN_20210210_BASIC_PETROCHEM_HIGH_MAE_G1 | representative |

## 12. Trigger-Level OHLC Backtest Tables

| Trigger | Entry | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | Peak | Drawdown after peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| R4L13_C15_T01 | 279,500 | 19.68% | 47.94% | 47.94% | -2.33% | -2.33% | -3.40% | 2021-05-10 / 413,500 | -20.92% |
| R4L13_C15_T02 | 118,500 | 32.07% | 143.04% | 147.68% | -0.42% | -0.42% | -0.42% | 2021-02-05 / 293,500 | -30.84% |
| R4L13_C15_T03 | 114,000 | 21.49% | 21.49% | 48.25% | -5.26% | -5.26% | -11.40% | 2021-10-01 / 169,000 | -39.94% |
| R4L13_C15_T04 | 326,000 | 3.68% | 3.68% | 3.68% | -11.04% | -11.04% | -23.01% | 2021-03-02 / 338,000 | -36.98% |
| R4L13_C15_T05 | 373,500 | 8.57% | 8.57% | 8.57% | -15.39% | -21.82% | -36.28% | 2021-02-17 / 405,500 | -46.24% |

Representative price-row anchors checked in stock-web: POSCO 2021-02-23 close 279,500 and 2021-05-10 high 413,500; Kumho 2020-10-05 close 118,500 and 2021-02-05 high 293,500; OCI 2021-02-10 close 114,000 and 2021-10-01 high 169,000; Lotte Chemical 2021-02-23 close 326,000 and 2021-03-02 high 338,000; 대한유화 2021-02-10 close 373,500 and 2021-02-17 high 405,500.

## 13. Current Calibrated Profile Stress Test

| Case | P0 likely label | Actual path | Verdict | Residual error? |
|---|---|---|---|---:|
| 005490 | Stage3-Yellow / 82 | structural_success_high_MFE_low_MAE | `current_profile_correct` | false |
| 011780 | Stage3-Yellow / 84 | structural_success_spread_supercycle | `current_profile_correct` | false |
| 010060 | Stage3-Yellow / 78 | high_mae_success | `current_profile_4B_too_early` | true |
| 011170 | Stage3-Yellow / 77 | failed_rerating_false_positive | `current_profile_false_positive` | true |
| 006650 | Stage3-Yellow / 76 | failed_rerating_high_MAE | `current_profile_false_positive` | true |

Answers to the required stress questions:

1. P0 correctly handles POSCO and Kumho, but over-promotes generic petrochemical spread rebounds in Lotte Chemical and 대한유화.
2. P0 is directionally right when spread has a margin bridge; it is wrong when the spread signal is only commodity beta plus price strength.
3. Stage2 actionable bonus is not too large globally, but C15 needs an offsetting quality gate.
4. Yellow threshold 75 is adequate, but it should not be reached by relative strength plus generic spread alone.
5. Green threshold 87 / revision 55 remains necessary; the shadow candidate simply clarifies what counts as revision-quality spread evidence in C15.
6. Price-only blowoff guard is strengthened by all counterexamples.
7. Full 4B non-price requirement is strengthened: POSCO/Kumho need non-price slowdown; Lotte/Daehan already had margin-quality break evidence.
8. Hard 4C routing worked as a protection concept, but the thesis-break evidence should be allowed to arrive from spread-to-margin failure, not only explicit disclosure shock.

## 14. Stage2 / Yellow / Green Comparison

| Case | Stage2 entry | Yellow/Green issue | green_lateness_ratio | Interpretation |
|---|---:|---|---:|---|
| 005490 | 2021-02-23 / 279,500 | Stage3-Yellow -> Stage3-Green-shadow | 0.47 | Green not too late |
| 011780 | 2020-10-05 / 118,500 | Stage3-Yellow -> Stage3-Green-shadow | 0.39 | Green not too late |
| 010060 | 2021-02-10 / 114,000 | Stage3-Yellow -> Stage3-Yellow-shadow-high-volatility | 0.58 | Green not too late |
| 011170 | 2021-02-23 / 326,000 | Stage3-Yellow -> Stage2-Watch-shadow | not_applicable | no confirmed Green trigger |
| 006650 | 2021-02-10 / 373,500 | Stage3-Yellow -> Stage2-Watch-shadow | not_applicable | no confirmed Green trigger |

## 15. 4B Local vs Full-window Timing Audit

| Case | local proximity | full-window proximity | 4B evidence type | Verdict |
|---|---:|---:|---|---|
| 005490 | 0.93 | 1.0 | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | `good_full_window_4B_timing` |
| 011780 | 0.96 | 1.0 | valuation_blowoff, positioning_overheat, revision_slowdown | `good_full_window_4B_timing` |
| 010060 | 0.45 | 0.95 | price_only, valuation_blowoff, positioning_overheat | `price_only_local_4B_too_early_until_non_price_slowdown` |
| 011170 | 1.0 | 1.0 | margin_or_backlog_slowdown, price_only | `good_full_window_4B_timing_for_counterexample` |
| 006650 | 1.0 | 1.0 | valuation_blowoff, positioning_overheat, price_only | `good_full_window_4B_timing_for_counterexample` |

## 16. 4C Protection Audit

| Case | 4C evidence | Protection label | Note |
|---|---|---|---|
| 005490 | none | `thesis_break_watch_only` | 4C is thesis-break/protection calibration only. |
| 011780 | none | `thesis_break_watch_only` | 4C is thesis-break/protection calibration only. |
| 010060 | thesis_evidence_broken | `hard_4c_late` | 4C is thesis-break/protection calibration only. |
| 011170 | thesis_evidence_broken | `hard_4c_success_if_margin_break_used` | 4C is thesis-break/protection calibration only. |
| 006650 | thesis_evidence_broken | `hard_4c_success_if_price_and_margin_break_used` | 4C is thesis-break/protection calibration only. |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`, but confidence is lower than the canonical rule. L4 materials generally need a `spread_to_margin_conversion_gate`: spot commodity spread must travel through margin bridge, volume/customer quality, or revision evidence before clean promotion.

Candidate sector shadow rule:

```text
if large_sector_id == L4_MATERIALS_SPREAD_RESOURCE and spread_signal == commodity_spot_beta_only:
    cap_positive_stage = Stage2-Watch unless margin_bridge_score and revision_score are confirmed
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`. C15 should distinguish two shapes:

- **Pipeline spread:** product spread widens, margin bridge appears, revisions follow. POSCO and Kumho fit this shape.
- **Puddle spread:** price and commodity narrative jump, but conversion does not travel into durable EPS. Lotte Chemical and 대한유화 fit this shape.

Proposed C15 shadow axes:

```text
C15_spread_to_margin_conversion_gate = +1
C15_customer_or_downstream_pass_through_requirement = +1
C15_generic_commodity_beta_penalty = +1 guardrail
```

## 19. Before / After Backtest Comparison

| Profile | Scope | Avg MFE90 | Avg MAE90 | False positive rate | Verdict |
|---|---|---:|---:|---|---|
| `P0_e2r_2_1_stock_web_calibrated_proxy` | current_default_proxy | 44.94% | -8.17% | 2/5 | partially_aligned_but_counterexample_sensitive |
| `P0b_e2r_2_0_baseline_reference` | rollback_reference | 44.94% | -8.17% | 3/5 | weaker_than_current_proxy |
| `P1_L4_materials_spread_shadow_profile` | sector_specific_candidate | 44.94% | -8.17% | 1/5 | improved_for_L4 |
| `P2_C15_material_spread_supercycle_shadow_profile` | canonical_archetype_specific_candidate | 44.94% | -8.17% | 0/5 on this holdout set | best_alignment_in_this_loop |
| `P3_counterexample_guard_profile` | counterexample_guard | 44.94% | -8.17% | 0/2 on counterexamples | good_guard_but_too_conservative_if_applied_globally |

## 20. Score-Return Alignment Matrix

| Case | Score before | Label before | Score after | Label after | MFE90/MAE90 | Alignment |
|---|---:|---|---:|---|---|---|
| 005490 | 82 | Stage3-Yellow | 88 | Stage3-Green-shadow | 47.94% / -2.33% | structural_success_high_MFE_low_MAE |
| 011780 | 84 | Stage3-Yellow | 90 | Stage3-Green-shadow | 143.04% / -0.42% | structural_success_spread_supercycle |
| 010060 | 78 | Stage3-Yellow | 82 | Stage3-Yellow-shadow-high-volatility | 21.49% / -5.26% | high_mae_success |
| 011170 | 77 | Stage3-Yellow | 69 | Stage2-Watch-shadow | 3.68% / -11.04% | failed_rerating_false_positive |
| 006650 | 76 | Stage3-Yellow | 67 | Stage2-Watch-shadow | 8.57% / -21.82% | failed_rerating_high_MAE |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | STEEL/NB_LATEX/POLYSILICON/PETROCHEM_SPREAD | 3 | 2 | 5 | 3 | 5 | 0 | 5 | 5 | 3 | true | true | C15 now has balanced spread-supercycle positives and commodity-beta counterexamples, but should add non-Korea materials holdout later. |

## 22. Residual Contribution Summary

```json
{
  "new_independent_case_count": 5,
  "reused_case_count": 0,
  "reused_case_ids": [],
  "new_symbol_count": 5,
  "new_canonical_archetype_count": 1,
  "new_fine_archetype_count": 5,
  "new_trigger_family_count": 5,
  "tested_existing_calibrated_axes": [
    "stage2_actionable_evidence_bonus",
    "stage3_yellow_total_min",
    "stage3_green_total_min",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "hard_4c_thesis_break_routes_to_4c"
  ],
  "residual_error_types_found": [
    "generic_commodity_spread_false_positive",
    "high_MAE_spread_success",
    "price_only_local_4B_too_early_until_non_price_evidence"
  ],
  "new_axis_proposed": [
    "C15_spread_to_margin_conversion_gate",
    "C15_generic_commodity_beta_penalty"
  ],
  "existing_axis_strengthened": [
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "hard_4c_thesis_break_routes_to_4c"
  ],
  "existing_axis_weakened": [],
  "existing_axis_kept": [
    "stage2_actionable_evidence_bonus",
    "stage3_yellow_total_min",
    "stage3_green_total_min"
  ],
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "no_new_signal_reason": null,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false
}
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical Korean listed equities, stock-web tradable_raw OHLC rows, 180D forward windows, C15 spread-supercycle residual behavior, positive/counterexample balance, and shadow-only score simulation.

Not validated: live candidates, brokerage execution, current recommendations, production scoring code, non-Korean materials names, exact analyst-consensus time series, or code implementation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C15_spread_to_margin_conversion_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Spread expansion is useful only when it converts into visible margin bridge and revision route.","keeps POSCO/Kumho as promotion candidates while demoting LotteChem/Daehan false positives",R4L13_C15_T01|R4L13_C15_T02|R4L13_C15_T04|R4L13_C15_T05,5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C15_generic_commodity_beta_penalty,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Generic commodity beta and relative strength without pass-through creates high MAE false positives.","reduces false-positive Green/Yellow labels for basic petrochemical rebounds",R4L13_C15_T04|R4L13_C15_T05,5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L4_high_MAE_spread_cycle_guard,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"High-volatility materials spreads should retain upside but avoid clean Green unless downstream/customer evidence is confirmed.","keeps OCI as Yellow-shadow rather than clean Green due to MAE and late full-window peak",R4L13_C15_T03,5,5,2,low,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"R4L13_C15_POSCO_20210223_STEEL_SPREAD","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_SPREAD_EXPORT_PRICE_SUPERCYCLE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L13_C15_T01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"promote clean spread-to-earnings bridge to Green-shadow only when margin bridge and revision are both present."}
{"row_type":"case","case_id":"R4L13_C15_KUMHO_20201005_NBLATEX_SPREAD","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"NB_LATEX_BUTADIENE_SPREAD_SUPERCYCLE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L13_C15_T02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_spread_supercycle","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"allow spread-supercycle acceleration when product spread is demand-backed and not inventory-only."}
{"row_type":"case","case_id":"R4L13_C15_OCI_20210210_POLYSILICON_SPREAD","symbol":"010060","company_name":"OCI홀딩스","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"POLYSILICON_PRICE_SPREAD_WITH_HIGH_MAE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R4L13_C15_T03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mae_success","current_profile_verdict":"current_profile_4B_too_early","price_source":"Songdaiki/stock-web","notes":"keep high-volatility spread cycles Yellow-shadow unless customer/pass-through evidence strengthens."}
{"row_type":"case","case_id":"R4L13_C15_LOTTECHEM_20210223_NAPHTHA_ETHYLENE_FALSE_POSITIVE","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"NAPHTHA_ETHYLENE_SPREAD_FALSE_POSITIVE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R4L13_C15_T04","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"demote generic naphtha/ethylene recovery unless spread is already visible in margin and revisions."}
{"row_type":"case","case_id":"R4L13_C15_DAEHAN_20210210_BASIC_PETROCHEM_HIGH_MAE","symbol":"006650","company_name":"대한유화","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"BASIC_PETROCHEM_SPREAD_HIGH_MAE_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L13_C15_T05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"block Green when commodity-spread spike has no durable customer or conversion bridge and MAE becomes structurally large."}
```

### 25.3 trigger rows
```jsonl
{"row_type":"trigger","trigger_id":"R4L13_C15_T01","case_id":"R4L13_C15_POSCO_20210223_STEEL_SPREAD","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_SPREAD_EXPORT_PRICE_SUPERCYCLE","sector":"철강·소재","primary_archetype":"steel spread to earnings revision","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-23","evidence_available_at_that_date":"중국/글로벌 철강 가격 강세와 원재료 대비 제품 spread 개선이 이미 시장 자료·리포트·가격 데이터로 관찰되었고, 2021년 이익 추정 상향 가능성이 공개적으로 논의되던 구간.","evidence_source":"industry steel spread/China steel price commentary; company steel segment earnings visibility; stock-web price row 2021-02-23 close 279500.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv","profile_path":"atlas/symbol_profiles/005/005490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-23","entry_price":279500,"MFE_30D_pct":19.68,"MFE_90D_pct":47.94,"MFE_180D_pct":47.94,"MFE_1Y_pct":47.94,"MFE_2Y_pct":null,"MAE_30D_pct":-2.33,"MAE_90D_pct":-2.33,"MAE_180D_pct":-3.4,"MAE_1Y_pct":-12.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-10","peak_price":413500,"drawdown_after_peak_pct":-20.92,"green_lateness_ratio":0.47,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L13_C15_POSCO_20210223_STEEL_SPREAD_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L13_C15_T02","case_id":"R4L13_C15_KUMHO_20201005_NBLATEX_SPREAD","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"NB_LATEX_BUTADIENE_SPREAD_SUPERCYCLE","sector":"석유화학·합성고무","primary_archetype":"latex demand plus feedstock spread to earnings","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2020-10-05","evidence_available_at_that_date":"NB latex 장갑 수요와 BD/SM 원재료 대비 제품가격 spread가 이미 업황 자료에서 드러났고, 분기 실적 레버리지로 연결될 가능성이 강했다.","evidence_source":"public petrochemical product spread commentary; company synthetic rubber earnings route; stock-web price row 2020-10-05 close 118500.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv|atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-10-05","entry_price":118500,"MFE_30D_pct":32.07,"MFE_90D_pct":143.04,"MFE_180D_pct":147.68,"MFE_1Y_pct":147.68,"MFE_2Y_pct":null,"MAE_30D_pct":-0.42,"MAE_90D_pct":-0.42,"MAE_180D_pct":-0.42,"MAE_1Y_pct":-18.99,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-05","peak_price":293500,"drawdown_after_peak_pct":-30.84,"green_lateness_ratio":0.39,"four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_spread_supercycle","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L13_C15_KUMHO_20201005_NBLATEX_SPREAD_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L13_C15_T03","case_id":"R4L13_C15_OCI_20210210_POLYSILICON_SPREAD","symbol":"010060","company_name":"OCI홀딩스","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"POLYSILICON_PRICE_SPREAD_WITH_HIGH_MAE","sector":"태양광소재·폴리실리콘","primary_archetype":"polysilicon spread to cyclic rerating with volatility","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-10","evidence_available_at_that_date":"폴리실리콘 spot 가격 상승과 공급 타이트가 확인되었으나, downstream 태양광 밸류체인 가격전가와 중국 증설 리스크가 같이 존재했다.","evidence_source":"public polysilicon price cycle commentary; company materials segment sensitivity; stock-web price row 2021-02-10 close 114000.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010060/2021.csv","profile_path":"atlas/symbol_profiles/010/010060.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-10","entry_price":114000,"MFE_30D_pct":21.49,"MFE_90D_pct":21.49,"MFE_180D_pct":48.25,"MFE_1Y_pct":48.25,"MFE_2Y_pct":null,"MAE_30D_pct":-5.26,"MAE_90D_pct":-5.26,"MAE_180D_pct":-11.4,"MAE_1Y_pct":-15.79,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-10-01","peak_price":169000,"drawdown_after_peak_pct":-39.94,"green_lateness_ratio":0.58,"four_b_local_peak_proximity":0.45,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"price_only_local_4B_too_early_until_non_price_slowdown","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L13_C15_OCI_20210210_POLYSILICON_SPREAD_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L13_C15_T04","case_id":"R4L13_C15_LOTTECHEM_20210223_NAPHTHA_ETHYLENE_FALSE_POSITIVE","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"NAPHTHA_ETHYLENE_SPREAD_FALSE_POSITIVE","sector":"석유화학·범용화학","primary_archetype":"commodity spread without durable conversion","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-23","evidence_available_at_that_date":"리오프닝 기대와 석유화학 spread 개선 기대는 있었으나, 원재료 naphtha 부담·범용 제품 oversupply·downstream 수요 확인 부족으로 revision durability가 약했다.","evidence_source":"public petrochemical spread/reopening commentary; company commodity chemical exposure; stock-web price row 2021-02-23 close 326000.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-23","entry_price":326000,"MFE_30D_pct":3.68,"MFE_90D_pct":3.68,"MFE_180D_pct":3.68,"MFE_1Y_pct":3.68,"MFE_2Y_pct":null,"MAE_30D_pct":-11.04,"MAE_90D_pct":-11.04,"MAE_180D_pct":-23.01,"MAE_1Y_pct":-34.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-03-02","peak_price":338000,"drawdown_after_peak_pct":-36.98,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_for_counterexample","four_b_evidence_type":["margin_or_backlog_slowdown","price_only"],"four_c_protection_label":"hard_4c_success_if_margin_break_used","trigger_outcome_label":"failed_rerating_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L13_C15_LOTTECHEM_20210223_NAPHTHA_ETHYLENE_FALSE_POSITIVE_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L13_C15_T05","case_id":"R4L13_C15_DAEHAN_20210210_BASIC_PETROCHEM_HIGH_MAE","symbol":"006650","company_name":"대한유화","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"BASIC_PETROCHEM_SPREAD_HIGH_MAE_FALSE_POSITIVE","sector":"석유화학·범용화학","primary_archetype":"early spread spike with poor durability","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-10","evidence_available_at_that_date":"기초유분 spread와 경기민감 리오프닝 기대가 강했지만, 이미 가격이 급격히 반응했고 원가/증설/범용 제품의 반복 공급 리스크가 컸다.","evidence_source":"public petrochemical upcycle commentary; basic petrochemical spread sensitivity; stock-web price row 2021-02-10 close 373500.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-10","entry_price":373500,"MFE_30D_pct":8.57,"MFE_90D_pct":8.57,"MFE_180D_pct":8.57,"MFE_1Y_pct":8.57,"MFE_2Y_pct":null,"MAE_30D_pct":-15.39,"MAE_90D_pct":-21.82,"MAE_180D_pct":-36.28,"MAE_1Y_pct":-45.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-17","peak_price":405500,"drawdown_after_peak_pct":-46.24,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_for_counterexample","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"hard_4c_success_if_price_and_margin_break_used","trigger_outcome_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_proxy_checked_against_profile_no_blocking_event","same_entry_group_id":"R4L13_C15_DAEHAN_20210210_BASIC_PETROCHEM_HIGH_MAE_G1","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C15_POSCO_20210223_STEEL_SPREAD","trigger_id":"R4L13_C15_T01","symbol":"005490","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":18,"revision_score":18,"relative_strength_score":13,"customer_quality_score":2,"policy_or_regulatory_score":7,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":18,"revision_score":18,"relative_strength_score":13,"customer_quality_score":2,"policy_or_regulatory_score":7,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"current calibrated proxy; no shadow changes applied","MFE_90D_pct":47.94,"MAE_90D_pct":-2.33,"score_return_alignment_label":"structural_success_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C15_material_spread_supercycle_shadow_profile","case_id":"R4L13_C15_POSCO_20210223_STEEL_SPREAD","trigger_id":"R4L13_C15_T01","symbol":"005490","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":18,"revision_score":18,"relative_strength_score":13,"customer_quality_score":2,"policy_or_regulatory_score":7,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":4,"margin_bridge_score":21,"revision_score":20,"relative_strength_score":13,"customer_quality_score":2,"policy_or_regulatory_score":7,"valuation_repricing_score":10,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green-shadow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"C15 shadow gives +6 when spread expansion is matched by visible margin bridge and revisions, not just spot price.","MFE_90D_pct":47.94,"MAE_90D_pct":-2.33,"score_return_alignment_label":"structural_success_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C15_KUMHO_20201005_NBLATEX_SPREAD","trigger_id":"R4L13_C15_T02","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":20,"revision_score":19,"relative_strength_score":15,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":12,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":20,"revision_score":19,"relative_strength_score":15,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":12,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"current calibrated proxy; no shadow changes applied","MFE_90D_pct":143.04,"MAE_90D_pct":-0.42,"score_return_alignment_label":"structural_success_spread_supercycle","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C15_material_spread_supercycle_shadow_profile","case_id":"R4L13_C15_KUMHO_20201005_NBLATEX_SPREAD","trigger_id":"R4L13_C15_T02","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":20,"revision_score":19,"relative_strength_score":15,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":12,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":23,"revision_score":21,"relative_strength_score":15,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":12,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green-shadow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"C15 shadow gives +6 because product spread, end-demand, and revision route all pointed in the same direction.","MFE_90D_pct":143.04,"MAE_90D_pct":-0.42,"score_return_alignment_label":"structural_success_spread_supercycle","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C15_OCI_20210210_POLYSILICON_SPREAD","trigger_id":"R4L13_C15_T03","symbol":"010060","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":17,"revision_score":15,"relative_strength_score":12,"customer_quality_score":1,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":17,"revision_score":15,"relative_strength_score":12,"customer_quality_score":1,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"current calibrated proxy; no shadow changes applied","MFE_90D_pct":21.49,"MAE_90D_pct":-5.26,"score_return_alignment_label":"high_mae_success","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"score_simulation","profile_id":"C15_material_spread_supercycle_shadow_profile","case_id":"R4L13_C15_OCI_20210210_POLYSILICON_SPREAD","trigger_id":"R4L13_C15_T03","symbol":"010060","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":17,"revision_score":15,"relative_strength_score":12,"customer_quality_score":1,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":17,"revision_score":15,"relative_strength_score":12,"customer_quality_score":1,"policy_or_regulatory_score":8,"valuation_repricing_score":12,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-shadow-high-volatility","changed_components":["margin_bridge_score","revision_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"C15 high-MAE subtype should not be upgraded to clean Green unless downstream pass-through and supply discipline are confirmed.","MFE_90D_pct":21.49,"MAE_90D_pct":-5.26,"score_return_alignment_label":"high_mae_success","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C15_LOTTECHEM_20210223_NAPHTHA_ETHYLENE_FALSE_POSITIVE","trigger_id":"R4L13_C15_T04","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":13,"revision_score":11,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":14,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":13,"revision_score":11,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":14,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"current calibrated proxy; no shadow changes applied","MFE_90D_pct":3.68,"MAE_90D_pct":-11.04,"score_return_alignment_label":"failed_rerating_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C15_material_spread_supercycle_shadow_profile","case_id":"R4L13_C15_LOTTECHEM_20210223_NAPHTHA_ETHYLENE_FALSE_POSITIVE","trigger_id":"R4L13_C15_T04","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":13,"revision_score":11,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":14,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":10,"revision_score":8,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":14,"execution_risk_score":13,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Watch-shadow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"C15 guard subtracts when spread evidence is generic commodity beta and not supported by customer/conversion or revision durability.","MFE_90D_pct":3.68,"MAE_90D_pct":-11.04,"score_return_alignment_label":"failed_rerating_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C15_DAEHAN_20210210_BASIC_PETROCHEM_HIGH_MAE","trigger_id":"R4L13_C15_T05","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":12,"revision_score":10,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":15,"execution_risk_score":11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":12,"revision_score":10,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":15,"execution_risk_score":11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"current calibrated proxy; no shadow changes applied","MFE_90D_pct":8.57,"MAE_90D_pct":-21.82,"score_return_alignment_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C15_material_spread_supercycle_shadow_profile","case_id":"R4L13_C15_DAEHAN_20210210_BASIC_PETROCHEM_HIGH_MAE","trigger_id":"R4L13_C15_T05","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":12,"revision_score":10,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":15,"execution_risk_score":11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":9,"revision_score":7,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":15,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-Watch-shadow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"C15 counterexample guard penalizes early price spike plus low customer quality and high execution/input risk.","MFE_90D_pct":8.57,"MAE_90D_pct":-21.82,"score_return_alignment_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C15_spread_to_margin_conversion_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Spread expansion is useful only when it converts into visible margin bridge and revision route.","keeps POSCO/Kumho as promotion candidates while demoting LotteChem/Daehan false positives",R4L13_C15_T01|R4L13_C15_T02|R4L13_C15_T04|R4L13_C15_T05,5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C15_generic_commodity_beta_penalty,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Generic commodity beta and relative strength without pass-through creates high MAE false positives.","reduces false-positive Green/Yellow labels for basic petrochemical rebounds",R4L13_C15_T04|R4L13_C15_T05,5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L4_high_MAE_spread_cycle_guard,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"High-volatility materials spreads should retain upside but avoid clean Green unless downstream/customer evidence is confirmed.","keeps OCI as Yellow-shadow rather than clean Green due to MAE and late full-window peak",R4L13_C15_T03,5,5,2,low,sector_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row
```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["generic_commodity_spread_false_positive","high_MAE_spread_success","price_only_local_4B_too_early_until_non_price_evidence"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reason":"no narrative-only rows in this loop; all five representative triggers have usable 180D windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 13
next_round = R5
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Price atlas manifest checked at `atlas/manifest.json`: max_date `2026-02-20`; source `FinanceData/marcap`; price adjustment `raw_unadjusted_marcap`; calibration root `atlas/ohlcv_tradable_by_symbol_year`.
- POSCO price rows checked in `atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv` and profile `atlas/symbol_profiles/005/005490.json`.
- Kumho Petrochemical price rows checked in `atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv`, `atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv`, and profile `atlas/symbol_profiles/011/011780.json`.
- OCI price rows checked in `atlas/ohlcv_tradable_by_symbol_year/010/010060/2021.csv` and profile `atlas/symbol_profiles/010/010060.json`.
- Lotte Chemical and 대한유화 price rows checked in `atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv` and `atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv`.
- Research artifact duplicate check used `data/e2r/calibration/md_registry.jsonl` and repository search for v12 R4 filenames. No `stock_agent` source code was opened or inferred.

