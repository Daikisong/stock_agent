# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R4
scheduled_loop: 10
completed_round: R4
completed_loop: 10
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_SPREAD_PRICE_TO_MARGIN_REVERSAL_GUARD
sector: 소재·스프레드·전략자원
primary_archetype: chemical / commodity spread cycle, margin bridge, reversal risk
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - sector_specific_rule_discovery
  - green_strictness_stress_test
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
output_file: e2r_stock_web_v12_residual_round_R4_loop_10_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
round_schedule_status: valid
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.
```

## 1. Current Calibrated Profile Assumption

This research uses the post-calibrated proxy baseline:

```text
P0  = e2r_2_1_stock_web_calibrated_proxy
P0b = e2r_2_0_baseline_reference
```

Already-applied global axes are treated as active and are not re-proposed globally:

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

This loop stress-tests whether chemical/commodity spread cases need a stricter C17-local split between:

1. spread expansion that is actually converted into margin / EPS / cash flow, and
2. spot-price or inventory-cycle enthusiasm that produces high MAE or failed rerating.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 10
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = CHEMICAL_SPREAD_PRICE_TO_MARGIN_REVERSAL_GUARD
```

R4 consistency gate:

```text
R4 -> L4_MATERIALS_SPREAD_RESOURCE = pass
canonical scope -> C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = pass
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed calibration artifact checked:

```text
reports/e2r_calibration/by_round/R4.md
```

The existing R4 calibration report already contains representative trigger coverage across Stage2-Actionable, Stage3-Yellow, Stage3-Green, Stage4B, Stage4C and earliest awareness rows. This MD therefore avoids repeating the global lessons that Stage2 is earlier than Green or that price-only blowoff must be blocked. The new contribution is C17-local: chemical spread conversion versus reversal guard.

Duplicate avoidance rule used:

```text
same canonical_archetype_id is allowed
same symbol + same trigger_date + same entry_date + same evidence family is duplicate-low-value
new symbol / new trigger family / new failure mode inside C17 is high value
```

Selected case set:

| case_id | symbol | company_name | novelty status | role |
|---|---:|---|---|---|
| R4L10-C17-KUMHO-2020 | 011780 | 금호석유화학 | new independent C17 case | structural_success + 4B overlay |
| R4L10-C17-HYOSUNG-2020 | 298020 | 효성티앤씨 | new independent C17 case | structural_success + late 4B overlay |
| R4L10-C17-LOTTECHEM-2021 | 011170 | 롯데케미칼 | new independent C17 case | false_positive / failed_rerating |
| R4L10-C17-OCI-2021 | 010060 | OCI / OCI홀딩스 | new independent C17 case | high_mae_success / spread whipsaw counterexample |
| R4L10-C17-KUMHO-4B-2021 | 011780 | 금호석유화학 | reused symbol, new trigger family | 4B_overlay_only |

## 4. Stock-Web OHLC Input / Price Source Validation

Price atlas validation:

```json
{
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Schema check:

```text
tradable shard columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_usable requires entry row, positive OHLCV, 180 forward tradable rows, and no 180D corporate-action contamination.
```

## 5. Historical Eligibility Gate

| symbol | profile_path | entry windows checked | corporate_action_window_status | forward window | calibration_usable |
|---:|---|---|---|---:|---|
| 011780 | atlas/symbol_profiles/011/011780.json | 2020-11-16 to 2021-08 area | clean_180D_window; profile corporate action date 2001-01-16 only | >=180D | true |
| 298020 | atlas/symbol_profiles/298/298020.json | 2020-12-17 to 2021-09 area | clean_180D_window; profile has no corporate-action candidate dates | >=180D | true |
| 011170 | atlas/symbol_profiles/011/011170.json | 2021-02-23 to 2021-11 area | clean_180D_window for 2021; profile corporate action candidate 2023-02-13 outside window | >=180D | true |
| 010060 | atlas/symbol_profiles/010/010060.json | 2021-02-15 to 2021-11 area | clean_180D_window for 2021; 2023 split candidates outside window | >=180D | true |

## 6. Canonical Archetype Compression Map

```text
fine_archetype: NB_LATEX_SYNTHETIC_RUBBER_SUPERCYCLE
  -> canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

fine_archetype: SPANDEX_SUPPLY_SHORTAGE_MARGIN_SPIKE
  -> canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

fine_archetype: ETHYLENE_NAPHTHA_REOPENING_SPREAD_FALSE_START
  -> canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD

fine_archetype: POLYSILICON_PRICE_UP_CASHFLOW_WITH_REVERSAL_RISK
  -> canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

Compression rule:

```text
Do not split each chemical product into separate production weights. Use C17 as the runtime canonical ID and let supplemental component fields encode the actual spread/product route.
```

## 7. Case Selection Summary

| case_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | case role | positive/counterexample |
|---|---:|---|---|---|---|---:|---|---|
| R4L10-C17-KUMHO-2020 | 011780 | 금호석유화학 | Stage2-Actionable | 2020-11-16 | 2020-11-16 | 138000 | structural_success | positive |
| R4L10-C17-HYOSUNG-2020 | 298020 | 효성티앤씨 | Stage2-Actionable | 2020-12-17 | 2020-12-17 | 206000 | structural_success | positive |
| R4L10-C17-LOTTECHEM-2021 | 011170 | 롯데케미칼 | Stage2-Actionable | 2021-02-23 | 2021-02-23 | 326000 | false_positive_green | counterexample |
| R4L10-C17-OCI-2021 | 010060 | OCI / OCI홀딩스 | Stage2-Actionable | 2021-02-15 | 2021-02-15 | 119000 | high_mae_success | counterexample |
| R4L10-C17-KUMHO-4B-2021 | 011780 | 금호석유화학 | Stage4B | 2021-05-06 | 2021-05-06 | 296000 | 4B_overlay_success | reused overlay |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
calibration_usable_trigger_count = 5
new_independent_case_count = 4
reused_case_count = 1
new_independent_case_ratio = 4 / 4 = 1.00
```

Interpretation:

- C17 should not reward commodity price language alone.
- C17 works best when product spread improvement is visibly crossing into margin bridge / EPS revision / cash conversion.
- Green should be delayed or blocked when the only evidence is spot-price spread or reopening beta without company-specific margin confirmation.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | stage2 evidence | stage3 evidence | 4B / 4C evidence |
|---|---|---|---|---|
| R4L10-C17-KUMHO-2020 | Public chemical spread / latex margin cycle was visible before the stock’s January 2021 acceleration. | NB latex / synthetic rubber spread, relative strength, early revision expectation | confirmed earnings revision, margin bridge, multiple public sources | valuation_blowoff / margin peak watch around 2021-05 |
| R4L10-C17-HYOSUNG-2020 | Spandex tightness and capacity shortage were visible before the 2021 parabolic rerating. | product spread, supply shortage, relative strength | confirmed margin bridge, EPS revision, low near-term execution risk | valuation_blowoff / positioning overheat after 2021-Q2/Q3 peak zone |
| R4L10-C17-LOTTECHEM-2021 | Reopening / petrochemical spread narrative was visible but less company-specific and less durable. | public spread narrative, relative strength | weak margin bridge, limited durable revision | margin/backlog slowdown, price failure |
| R4L10-C17-OCI-2021 | Polysilicon price recovery was visible but cyclicality and whipsaw risk remained high. | product price recovery, policy/solar demand optionality | partial revision support, uncertain durability | high MAE and reversal guard required |

## 10. Price Data Source Map

| symbol | company_name | tradable shard(s) used | profile path | notes |
|---:|---|---|---|---|
| 011780 | 금호석유화학 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv; 2021.csv | atlas/symbol_profiles/011/011780.json | clean 2020-2021 calibration window |
| 298020 | 효성티앤씨 | atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv; 2021.csv | atlas/symbol_profiles/298/298020.json | no corporate-action candidate in profile |
| 011170 | 롯데케미칼 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv | atlas/symbol_profiles/011/011170.json | 2021 window clean; 2023 candidate outside window |
| 010060 | OCI / OCI홀딩스 | atlas/ohlcv_tradable_by_symbol_year/010/010060/2021.csv | atlas/symbol_profiles/010/010060.json | 2021 window clean; 2023 split candidates outside window |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | entry | stage2 fields | stage3 fields | 4B fields | current_profile_verdict |
|---|---|---|---|---|---|---|---|
| R4L10-C17-KUMHO-S2A-20201116 | R4L10-C17-KUMHO-2020 | Stage2-Actionable | 2020-11-16 @ 138000 | relative_strength; product_spread; early_revision_signal | margin_bridge later confirmed | none at entry | current_profile_correct |
| R4L10-C17-HYOSUNG-S2A-20201217 | R4L10-C17-HYOSUNG-2020 | Stage2-Actionable | 2020-12-17 @ 206000 | supply_shortage; product_spread; relative_strength | margin_bridge; confirmed_revision | none at entry | current_profile_correct |
| R4L10-C17-LOTTECHEM-S2A-20210223 | R4L10-C17-LOTTECHEM-2021 | Stage2-Actionable | 2021-02-23 @ 326000 | reopening_spread; relative_strength | weak / not durable | margin_slowdown later | current_profile_false_positive |
| R4L10-C17-OCI-S2A-20210215 | R4L10-C17-OCI-2021 | Stage2-Actionable | 2021-02-15 @ 119000 | product_price_recovery; policy_optional | partial revision | high_mae / cyclicality | current_profile_too_early |
| R4L10-C17-KUMHO-4B-20210506 | R4L10-C17-KUMHO-2020 | Stage4B | 2021-05-06 @ 296000 | not applicable | margin already confirmed | valuation_blowoff; margin_peak_watch | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger table

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R4L10-C17-KUMHO-S2A-20201116 | 2020-11-16 | 138000 | 11.96 | -5.07 | 112.68 | -5.07 | 116.30 | -5.07 | 2021-05-06 | 298500 | -32.16 | strong structural rerating then 4B zone |
| R4L10-C17-HYOSUNG-S2A-20201217 | 2020-12-17 | 206000 | 61.41 | -4.85 | 293.20 | -4.85 | 367.48 | -4.85 | 2021-07-16 | 963000 | -22.64 | explosive structural spread cycle |
| R4L10-C17-LOTTECHEM-S2A-20210223 | 2021-02-23 | 326000 | 3.68 | -8.59 | 3.68 | -23.31 | 3.68 | -23.31 | 2021-03-02 | 338000 | -26.92 | spread false start / high MAE |
| R4L10-C17-OCI-S2A-20210215 | 2021-02-15 | 119000 | 16.39 | -9.24 | 23.53 | -9.24 | 23.53 | -9.24 | 2021-04-23 | 147000 | -23.47 | positive but high whipsaw, needs guard |

### 4B overlay table

| trigger_id | entry_date | entry_price | prior_stage2_entry_price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | timing verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| R4L10-C17-KUMHO-4B-20210506 | 2021-05-06 | 296000 | 138000 | 298500 | 298500 | 0.98 | 0.98 | valuation_blowoff; margin_peak_watch; positioning_overheat | good_full_window_4B_timing |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely stage | actual path | profile verdict | why |
|---|---|---|---|---|
| KUMHO-2020 | Stage2-Actionable -> Green after confirmation | MFE180 +116.30, low MAE | current_profile_correct | spread had company-specific margin bridge and later revision confirmation |
| HYOSUNG-2020 | Stage2-Actionable -> Green after confirmation | MFE180 +367.48, low MAE | current_profile_correct | shortage + spread + margin bridge aligned |
| LOTTECHEM-2021 | Stage2-Actionable or Yellow if generic spread score overweights cycle | MFE180 +3.68, MAE180 -23.31 | current_profile_false_positive | reopening spread did not convert into durable company-specific rerating |
| OCI-2021 | Stage2-Actionable | MFE90 +23.53 but MAE path non-trivial | current_profile_too_early | positive price path existed, but high cyclicality and policy/commodity beta should lower Green confidence |

Answers to required stress-test questions:

1. Stage2 bonus was useful for KUMHO/HYOSUNG but too generous for LOTTECHEM if product-spread narrative lacked margin/EPS confirmation.
2. Yellow threshold 75 is acceptable if C17 confidence is capped without margin bridge.
3. Green threshold 87 and revision 55 are directionally correct; C17 needs a local product-spread-to-margin bridge before Green.
4. price-only blowoff guard is appropriate and should be kept.
5. full 4B non-price requirement is appropriate; C17 local 4B works when valuation blowoff is paired with margin peak or revision slowdown.
6. Hard 4C routing is not newly tested here because no clean hard thesis-break row was included.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3 proxy entry | peak price | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| KUMHO-2020 | 138000 | 220500 | 298500 | 0.514 | Green confirmation captured later but still meaningful upside |
| HYOSUNG-2020 | 206000 | 389000 | 963000 | 0.242 | Green not very late because spread + margin evidence persisted |
| LOTTECHEM-2021 | 326000 | not confirmed | 338000 | not_applicable | no confirmed Stage3 Green trigger |
| OCI-2021 | 119000 | 134500 | 147000 | 0.554 | confirmation came late relative to small available upside |

C17 conclusion:

```text
Green should require margin bridge or confirmed revision. Product spread alone can be Stage2 watch/actionable, but not Green.
```

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| KUMHO-2020 | valuation_blowoff + margin peak watch | 0.98 | 0.98 | good_full_window_4B_timing |
| HYOSUNG-2020 | valuation blowoff emerged after extreme spread conversion, but the first local peaks were not enough alone | 0.80 proxy | 0.80 proxy | price-only local peaks should remain watch-only until non-price evidence appears |
| LOTTECHEM-2021 | price failure + margin weakness | not full 4B | not full 4B | better as false-positive guard than 4B success |
| OCI-2021 | whipsaw / cyclicality | not full 4B | not full 4B | use as C17 volatility guard |

## 16. 4C Protection Audit

No clean hard 4C row is promoted from this MD. C17 4C candidate signals that should be tested in future R4 loops:

```text
- product price collapse confirmed by third-party index
- company guidance / revision cut
- inventory loss or negative spread evidence
- structural demand impairment rather than temporary destocking
```

## 17. Sector-Specific Rule Candidate

```yaml
rule_id: L4_C17_SPREAD_TO_MARGIN_BRIDGE_GATE
rule_scope: sector_specific
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
proposal_type: sector_shadow_only
rule_text: >
  In L4/C17, product spread or commodity price improvement may produce Stage2-Actionable,
  but Stage3-Green should require at least one of: confirmed company margin bridge,
  durable EPS revision, cash-flow conversion, or evidence of supply discipline.
  Generic spread/reopening narrative without company-specific conversion should be capped at Yellow/watch.
backtest_effect: >
  Preserves KUMHO/HYOSUNG positive entries while reducing LOTTECHEM-style false positive Green risk.
confidence: medium
production_scoring_changed: false
```

## 18. Canonical-Archetype Rule Candidate

```yaml
rule_id: C17_COMMODITY_SPREAD_REVERSAL_GUARD
rule_scope: canonical_archetype_specific
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
proposal_type: archetype_shadow_only
changed_components:
  - margin_bridge_score +2 only if product spread is shown in realized margin or confirmed revision
  - execution_risk_score +2 when inventory/reversal/overcapacity risk is visible
  - valuation_repricing_score capped if spread evidence is price-only
  - Stage3 Green block when revision_score < 55 and margin_bridge_score is weak
reason: >
  Chemical spread cycles rerate rapidly when spread converts into earnings, but can also produce
  false starts when investors extrapolate commodity spot prices without company-specific margin conversion.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected entries | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | late_green_count | alignment verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 4 | 108.52 | -10.99 | 0.25 | 0 | 2 | good but C17 false-positive residual remains |
| P0b_e2r_2_0_baseline_reference | rollback reference | 4 | 108.52 | -10.99 | 0.50 | 1 | 1 | overweights price/spread headline |
| P1_L4_sector_specific_candidate | sector shadow | 4 | 108.52 | -10.99 | 0.25 | 0 | 1 | improves Green discipline without killing Stage2 |
| P2_C17_archetype_candidate | canonical shadow | 4 | 108.52 | -10.99 | 0.00 to 0.25 | 0 | 1 | best explanatory compression |
| P3_C17_counterexample_guard_profile | guard shadow | 4 | 108.52 | -10.99 | 0.00 | 0 | 2 | safest but may delay positive spread cycles |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| KUMHO-S2A-20201116 | 78 | Stage2-Actionable | 82 | Stage3-Yellow / pre-Green | 112.68 | -5.07 | strong alignment |
| HYOSUNG-S2A-20201217 | 81 | Stage3-Yellow | 88 | Stage3-Green | 293.20 | -4.85 | strong alignment |
| LOTTECHEM-S2A-20210223 | 76 | Stage3-Yellow risk | 67 | Stage2-watch | 3.68 | -23.31 | improved false-positive control |
| OCI-S2A-20210215 | 75 | Stage3-Yellow risk | 72 | Stage2-Actionable | 23.53 | -9.24 | improved cyclicality guard |

Raw component proxy scores:

```json
{
  "KUMHO-S2A-20201116": {
    "before": {"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":15,"revision_score":14,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18},
    "after":  {"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":15,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":20}
  },
  "HYOSUNG-S2A-20201217": {
    "before": {"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":15,"relative_strength_score":14,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":20},
    "after":  {"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":17,"relative_strength_score":14,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":22}
  },
  "LOTTECHEM-S2A-20210223": {
    "before": {"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":15,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18},
    "after":  {"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":11,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":14}
  },
  "OCI-S2A-20210215": {
    "before": {"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":9,"relative_strength_score":12,"customer_quality_score":2,"policy_or_regulatory_score":5,"valuation_repricing_score":11,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18},
    "after":  {"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":11,"customer_quality_score":2,"policy_or_regulatory_score":5,"valuation_repricing_score":8,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":16}
  }
}
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHEMICAL_SPREAD_PRICE_TO_MARGIN_REVERSAL_GUARD | 2 | 2 | 1 | 0 | 4 | 1 | 5 | 4 | 2 | true | true | C17 now has balanced positive/counterexample sample; needs future hard 4C rows |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids:
  - R4L10-C17-KUMHO-4B-2021
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_too_early
new_axis_proposed: null
existing_axis_strengthened:
  - C17-specific margin_bridge gate for Stage3-Green
  - C17 price-only spread cap at Stage2/watch
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- R4/L4/C17 round-sector-archetype consistency
- stock-web manifest/schema price basis
- symbol profile caveat and corporate-action window status
- actual tradable_raw entry prices from stock-web CSV shards
- trigger-level MFE/MAE proxy calculations for 30D/90D/180D windows
- local vs full-window 4B split for one reused overlay row
```

Not validated:

```text
- No live candidate scan
- No production score change
- No src/e2r code inspection
- No broker/API connection
- No current investment recommendation
- No hard 4C production rule promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,margin_bridge_required_for_green,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,false,true,+1,"C17 spread headlines split sharply by realized margin bridge","Preserves KUMHO/HYOSUNG while reducing LOTTECHEM false positive",R4L10-C17-KUMHO-S2A-20201116|R4L10-C17-HYOSUNG-S2A-20201217|R4L10-C17-LOTTECHEM-S2A-20210223|R4L10-C17-OCI-S2A-20210215,4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_only_spread_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,none,cap_at_stage2_watch,+1,"Commodity price/spread alone produced whipsaw and false positives","Improves MAE discipline in LOTTECHEM/OCI-style cases",R4L10-C17-LOTTECHEM-S2A-20210223|R4L10-C17-OCI-S2A-20210215,2,2,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,non_price_4b_for_spread_peak,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,true,true,0,"Already applied full 4B non-price rule is kept; C17 uses margin peak/valuation overheat as overlay evidence","KUMHO 4B overlay aligns with full-window peak",R4L10-C17-KUMHO-4B-20210506,1,0,0,medium,axis_stress_test,"kept, not new global delta"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R4L10-C17-KUMHO-2020","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NB_LATEX_SYNTHETIC_RUBBER_SUPERCYCLE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L10-C17-KUMHO-S2A-20201116","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Spread expansion translated into margin/EPS rerating; later 4B overlay useful."}
{"row_type":"case","case_id":"R4L10-C17-HYOSUNG-2020","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPANDEX_SUPPLY_SHORTAGE_MARGIN_SPIKE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L10-C17-HYOSUNG-S2A-20201217","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"very_strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Spread/shortage converted into extreme margin rerating."}
{"row_type":"case","case_id":"R4L10-C17-LOTTECHEM-2021","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"ETHYLENE_NAPHTHA_REOPENING_SPREAD_FALSE_START","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R4L10-C17-LOTTECHEM-S2A-20210223","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_failed_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Generic spread/reopening narrative had poor MFE and high MAE."}
{"row_type":"case","case_id":"R4L10-C17-OCI-2021","symbol":"010060","company_name":"OCI / OCI홀딩스","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"POLYSILICON_PRICE_UP_CASHFLOW_WITH_REVERSAL_RISK","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R4L10-C17-OCI-S2A-20210215","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_whipsaw_guard_needed","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Polysilicon price recovery worked, but C17 needs cyclicality/MAE guard before Green."}
{"row_type":"trigger","trigger_id":"R4L10-C17-KUMHO-S2A-20201116","case_id":"R4L10-C17-KUMHO-2020","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NB_LATEX_SYNTHETIC_RUBBER_SUPERCYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical spread to margin bridge","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2020-11-16","evidence_available_at_that_date":"NB latex/synthetic rubber spread and relative strength visible; margin bridge not yet fully confirmed","evidence_source":"historical public spread/revision proxy; stock-web price validation","stage2_evidence_fields":["relative_strength","early_revision_signal","asp_or_spread_score"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-11-16","entry_price":138000,"MFE_30D_pct":11.96,"MFE_90D_pct":112.68,"MFE_180D_pct":116.30,"MFE_1Y_pct":116.30,"MFE_2Y_pct":116.30,"MAE_30D_pct":-5.07,"MAE_90D_pct":-5.07,"MAE_180D_pct":-5.07,"MAE_1Y_pct":-5.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-06","peak_price":298500,"drawdown_after_peak_pct":-32.16,"green_lateness_ratio":0.514,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_tested","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L10-C17-KUMHO-20201116-138000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L10-C17-HYOSUNG-S2A-20201217","case_id":"R4L10-C17-HYOSUNG-2020","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPANDEX_SUPPLY_SHORTAGE_MARGIN_SPIKE","sector":"소재·스프레드·전략자원","primary_archetype":"spandex spread supercycle","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2020-12-17","evidence_available_at_that_date":"spandex shortage and spread expansion visible before confirmed earnings rerating","evidence_source":"historical public spread/revision proxy; stock-web price validation","stage2_evidence_fields":["relative_strength","asp_or_spread_score","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-12-17","entry_price":206000,"MFE_30D_pct":61.41,"MFE_90D_pct":293.20,"MFE_180D_pct":367.48,"MFE_1Y_pct":367.48,"MFE_2Y_pct":367.48,"MAE_30D_pct":-4.85,"MAE_90D_pct":-4.85,"MAE_180D_pct":-4.85,"MAE_1Y_pct":-4.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-22.64,"green_lateness_ratio":0.242,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_tested","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L10-C17-HYOSUNG-20201217-206000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L10-C17-LOTTECHEM-S2A-20210223","case_id":"R4L10-C17-LOTTECHEM-2021","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"ETHYLENE_NAPHTHA_REOPENING_SPREAD_FALSE_START","sector":"소재·스프레드·전략자원","primary_archetype":"generic petrochemical spread false start","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-23","evidence_available_at_that_date":"spread/reopening narrative and relative strength visible but margin conversion not durable","evidence_source":"historical public spread/revision proxy; stock-web price validation","stage2_evidence_fields":["relative_strength","asp_or_spread_score"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-23","entry_price":326000,"MFE_30D_pct":3.68,"MFE_90D_pct":3.68,"MFE_180D_pct":3.68,"MFE_1Y_pct":3.68,"MFE_2Y_pct":3.68,"MAE_30D_pct":-8.59,"MAE_90D_pct":-23.31,"MAE_180D_pct":-23.31,"MAE_1Y_pct":-23.31,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-03-02","peak_price":338000,"drawdown_after_peak_pct":-26.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_tested","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L10-C17-LOTTECHEM-20210223-326000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L10-C17-OCI-S2A-20210215","case_id":"R4L10-C17-OCI-2021","symbol":"010060","company_name":"OCI / OCI홀딩스","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"POLYSILICON_PRICE_UP_CASHFLOW_WITH_REVERSAL_RISK","sector":"소재·스프레드·전략자원","primary_archetype":"polysilicon spread recovery with reversal risk","loop_objective":"counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-15","evidence_available_at_that_date":"polysilicon price recovery and solar demand optionality visible; durability not yet proven","evidence_source":"historical public spread/revision proxy; stock-web price validation","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","asp_or_spread_score"],"stage3_evidence_fields":["partial_revision"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010060/2021.csv","profile_path":"atlas/symbol_profiles/010/010060.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-15","entry_price":119000,"MFE_30D_pct":16.39,"MFE_90D_pct":23.53,"MFE_180D_pct":23.53,"MFE_1Y_pct":23.53,"MFE_2Y_pct":23.53,"MAE_30D_pct":-9.24,"MAE_90D_pct":-9.24,"MAE_180D_pct":-9.24,"MAE_1Y_pct":-9.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-04-23","peak_price":147000,"drawdown_after_peak_pct":-23.47,"green_lateness_ratio":0.554,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_tested","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L10-C17-OCI-20210215-119000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L10-C17-KUMHO-4B-20210506","case_id":"R4L10-C17-KUMHO-2020","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NB_LATEX_SYNTHETIC_RUBBER_SUPERCYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical spread peak 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2021-05-06","evidence_available_at_that_date":"valuation/margin peak watch after confirmed spread rerating","evidence_source":"historical public valuation/revision proxy; stock-web price validation","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-06","entry_price":296000,"MFE_30D_pct":0.84,"MFE_90D_pct":0.84,"MFE_180D_pct":0.84,"MFE_1Y_pct":0.84,"MFE_2Y_pct":0.84,"MAE_30D_pct":-31.59,"MAE_90D_pct":-31.59,"MAE_180D_pct":-31.59,"MAE_1Y_pct":-31.59,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-06","peak_price":298500,"drawdown_after_peak_pct":-32.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L10-C17-KUMHO-20210506-296000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol reused for different 4B timing family after Stage2 success","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L10-C17-LOTTECHEM-2021","trigger_id":"R4L10-C17-LOTTECHEM-S2A-20210223","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":15,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":11,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":14},"weighted_score_after":67,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 spread-only enthusiasm is capped without durable margin bridge.","MFE_90D_pct":3.68,"MAE_90D_pct":-23.31,"score_return_alignment_label":"improved_false_positive_control","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":4,"reused_case_count":1,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_false_positive","current_profile_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R4
completed_loop = 10
next_round = R5
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Price atlas / manifest / schema:

- Songdaiki/stock-web `atlas/manifest.json`: source_name FinanceData/marcap, max_date 2026-02-20, price_adjustment_status raw_unadjusted_marcap, calibration_shard_root atlas/ohlcv_tradable_by_symbol_year.
- Songdaiki/stock-web `atlas/schema.json`: tradable shard columns and MFE/MAE formula.
- Stock-web symbol profiles checked: 011780, 298020, 011170, 010060.
- Stock-web tradable OHLC shards checked: 011780/2020.csv, 011780/2021.csv, 298020/2020.csv, 298020/2021.csv, 011170/2021.csv, 010060/2021.csv.
- Allowed stock_agent artifact checked: reports/e2r_calibration/by_round/R4.md.

This MD is historical calibration research only. It is not an investment recommendation, not a live scan, and not a production scoring patch.

