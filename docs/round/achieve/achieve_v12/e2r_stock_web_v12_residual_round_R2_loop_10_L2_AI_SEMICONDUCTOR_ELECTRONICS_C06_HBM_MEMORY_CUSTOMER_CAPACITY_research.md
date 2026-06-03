# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R2_loop_10_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
scheduled_round = R2
scheduled_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
completed_round = R2
completed_loop = 10
next_round = R3
next_loop = 10
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = HBM_CUSTOMER_CAPACITY_QUALIFICATION_SOLDOUT_SPLIT
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **3 new independent cases**, **2 counterexamples**, and **2 current-profile residual/stress errors** for `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS / C06_HBM_MEMORY_CUSTOMER_CAPACITY`.

The research question is not “HBM went up.” The question is whether the C06 archetype needs a sharper split between:

```text
confirmed HBM customer/capacity/sold-out evidence
vs.
customer testing / optionality / placard / expectation without qualification
```

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

Existing applied axes are **tested**, not re-proposed globally.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R2 |
| scheduled_loop | 10 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY |
| fine_archetype_id | HBM_CUSTOMER_CAPACITY_QUALIFICATION_SOLDOUT_SPLIT |
| allowed round-sector pair | pass |
| next round | R3 |
| next loop | 10 |

R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`, so the round-sector gate passes.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show that the calibration corpus already covers all R1~R13 and loops 1~9. R2 loop 1~9 exists in the registry, so the next scheduled R2 run is loop 10.

The previous R2 files are general `ai_semiconductor_electronic_components_research` loops. This MD does not reuse a previous exact file table. It focuses on a narrower C06 split: **HBM customer qualification/capacity proof vs customer-testing optionality**.

Duplicate policy:

| item | status |
|---|---|
| same canonical archetype reused | allowed |
| same symbol reused | allowed only for new trigger family |
| same symbol + same trigger date + same entry date reused | not used |
| new symbols | SK하이닉스, 삼성전자 |
| new trigger families | HBM sold-out capacity, HBM customer-testing optionality, HBM qualification failure, price-only local 4B |

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Stock-web manifest basis:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Profile checks:

| symbol | profile path | latest profile date | corporate action overlap in 2024 trigger→D+180 | calibration window |
|---|---|---:|---|---|
| 000660 | atlas/symbol_profiles/000/000660.json | 2026-02-20 | no, historical candidate dates end in 2003 | clean_180D_window |
| 005930 | atlas/symbol_profiles/005/005930.json | 2026-02-20 | no, historical candidate dates include 2018-05-04 only | clean_180D_window |

## 5. Historical Eligibility Gate

| trigger_id | trigger_date | entry_date | entry_price | 180D available | CA contaminated | calibration_usable |
|---|---:|---:|---:|---|---|---|
| R2L10_C06_000660_20240502_STAGE2A | 2024-05-02 | 2024-05-03 | 173,200 | yes | no | true |
| R2L10_C06_005930_20240320_STAGE2WATCH | 2024-03-20 | 2024-03-21 | 79,300 | yes | no | true |
| R2L10_C06_005930_20240524_4C | 2024-05-24 | 2024-05-24 | 75,900 | yes | no | true |
| R2L10_C06_000660_20240711_4B_LOCAL | 2024-07-11 | 2024-07-11 | 241,000 | yes | no | true, overlay only |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
|---|---|---|
| HBM3E_CUSTOMER_CAPACITY_SOLDOUT_BRIDGE | C06_HBM_MEMORY_CUSTOMER_CAPACITY | Customer capacity and sold-out HBM evidence are the core C06 positive bridge. |
| HBM_CUSTOMER_TESTING_WITHOUT_QUALIFICATION | C06_HBM_MEMORY_CUSTOMER_CAPACITY | Testing/optionality belongs in C06 but should be capped before confirmed qualification. |
| HBM_QUALIFICATION_FAILURE_HEAT_POWER_THESIS_BREAK | C06_HBM_MEMORY_CUSTOMER_CAPACITY | Failed or pending customer qualification is a negative C06 thesis-break route. |
| HBM_PRICE_ONLY_LOCAL_PEAK_NOT_FULL_4B | C06_HBM_MEMORY_CUSTOMER_CAPACITY | Local 4B overlay; does not train positive entry weights. |

## 7. Case Selection Summary

| case_id | symbol | role | reason |
|---|---:|---|---|
| R2L10_C06_000660_HBM3E_SOLDOUT_CAPACITY | 000660 | structural_success | HBM sold-out/capacity evidence aligned with large MFE and acceptable MAE. |
| R2L10_C06_005930_CUSTOMER_TESTING_OPTIONALITY_FALSE_POSITIVE | 005930 | failed_rerating / false_positive_green_risk | Customer testing/expectation rallied, but qualification proof was missing and drawdown later dominated. |
| R2L10_C06_005930_HBM_QUALIFICATION_FAILURE_4C | 005930 | 4C_success | Qualification-failure evidence should route to thesis-break protection. |
| R2L10_C06_000660_PRICE_ONLY_LOCAL_4B_TOO_EARLY | 000660 | 4B_too_early | July 2024 local peak had no non-price break; full-window context makes it too early as full 4B. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 4
representative_trigger_count = 2
new_independent_case_count = 3
reused_case_count = 1
```

The MD is counterexample-heavy by design because C06 already has strong positive memory-cycle examples. The residual contribution is the **qualification/capacity split**, not a global Stage2 relaxation.

## 9. Evidence Source Map

| evidence family | source | interpretation |
|---|---|---|
| SK Hynix HBM sold-out capacity | Reuters 2024-05-02 | Positive C06 bridge: HBM sold out for current year and nearly sold out for next year; customer demand locked before capacity expansion. |
| SK Hynix HBM3E production/supply | Reuters 2024-09-04 | Confirms HBM3E and 12-layer HBM3E production path, supporting customer/capacity visibility. |
| Samsung HBM customer-testing optionality | Investopedia 2024-03-20 | Watch-stage evidence only: Nvidia testing and investor expectation, no firm order. |
| Samsung HBM qualification failure | Reuters 2024-05-24 | Negative C06 break: HBM3/HBM3E not passed Nvidia tests due to reported heat/power issues; Samsung disputed details but acknowledged optimization. |
| Samsung muted HBM3 approval | Reuters 2024-07-23 | HBM3 approval for China H20 was not equivalent to full HBM3E qualification for mainstream high-end AI processors. |

## 10. Price Data Source Map

| symbol | entry trigger | shard | profile |
|---|---|---|---|
| 000660 | 2024-05-02 / 2024-07-11 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | atlas/symbol_profiles/000/000660.json |
| 005930 | 2024-03-20 / 2024-05-24 | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv | atlas/symbol_profiles/005/005930.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | symbol | entry | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| R2L10_C06_000660_20240502_STAGE2A | Stage2-Actionable | 000660 | 2024-05-03 @ 173,200 | 43.48% | -12.47% | 43.48% | -12.47% | current_profile_correct |
| R2L10_C06_005930_20240320_STAGE2WATCH | Stage2-Watch | 005930 | 2024-03-21 @ 79,300 | 11.98% | -6.68% | 11.98% | -37.07% | current_profile_false_positive |
| R2L10_C06_005930_20240524_4C | 4C | 005930 | 2024-05-24 @ 75,900 | 16.99% | -22.40% | 16.99% | -34.26% | current_profile_correct_if_4C_router_receives_exact_qualification_failure |
| R2L10_C06_000660_20240711_4B_LOCAL | 4B-local-price-only | 000660 | 2024-07-11 @ 241,000 | 3.11% | -39.96% | 3.11% | -39.96% | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables

### 000660 SK하이닉스 — HBM sold-out capacity bridge

| metric | value |
|---|---:|
| entry_date | 2024-05-03 |
| entry_price | 173,200 |
| MFE_30D | 35.39% |
| MAE_30D | 0.00% |
| MFE_90D | 43.48% |
| MAE_90D | -12.47% |
| MFE_180D | 43.48% |
| MAE_180D | -12.47% |
| peak_date | 2024-07-11 |
| peak_price | 248,500 |
| drawdown_after_peak | -38.99% |

### 005930 삼성전자 — customer testing without qualification

| metric | value |
|---|---:|
| entry_date | 2024-03-21 |
| entry_price | 79,300 |
| MFE_30D | 8.45% |
| MAE_30D | -5.30% |
| MFE_90D | 11.98% |
| MAE_90D | -6.68% |
| MFE_180D | 11.98% |
| MAE_180D | -37.07% |
| peak_date | 2024-07-11 |
| peak_price | 88,800 |
| drawdown_after_peak | -43.81% |

### 005930 삼성전자 — HBM qualification failure / 4C trigger

| metric | value |
|---|---:|
| entry_date | 2024-05-24 |
| entry_price | 75,900 |
| MFE_30D | 14.76% |
| MAE_30D | -3.16% |
| MFE_90D | 16.99% |
| MAE_90D | -22.40% |
| MFE_180D | 16.99% |
| MAE_180D | -34.26% |
| peak_date | 2024-07-11 |
| peak_price | 88,800 |
| drawdown_after_peak | -43.81% |

### 000660 SK하이닉스 — price-only local 4B

| metric | value |
|---|---:|
| entry_date | 2024-07-11 |
| entry_price | 241,000 |
| local_peak_price | 248,500 |
| MFE_30D | 3.11% |
| MAE_30D | -37.10% |
| MFE_90D | 3.11% |
| MAE_90D | -39.96% |
| four_b_local_peak_proximity | 0.93 |
| four_b_full_window_peak_proximity | 0.13 |
| verdict | price_only_local_4B_too_early |

## 13. Current Calibrated Profile Stress Test

| case | current profile behavior | actual path | verdict |
|---|---|---|---|
| SK Hynix sold-out/capacity | Stage2A/Yellow/Green bridge likely acceptable | strong MFE, drawdown after peak but entry still worked | current_profile_correct |
| Samsung customer testing | Stage2 bonus + relative strength could over-credit customer quality | upside was shallow; later MAE dominated | current_profile_false_positive |
| Samsung qualification failure | hard 4C route should catch if exact evidence is parsed | protected before deep drawdown | current_profile_correct_if_4C_router_receives_exact_qualification_failure |
| SK Hynix local price-only 4B | full 4B blocked without non-price evidence | local peak was not full-window cycle peak | current_profile_correct |

Answers required by prompt:

```text
1. current calibrated profile 판단:
   - SKH sold-out: Stage2A/Yellow/Green bridge acceptable.
   - Samsung testing: too generous if testing is scored as customer quality.
   - Samsung 4C: correct if qualification-failure evidence enters 4C router.
2. MFE/MAE alignment:
   - SKH aligned, Samsung testing not aligned, Samsung 4C protective.
3. Stage2 bonus:
   - useful for SKH sold-out, too high for Samsung testing-only.
4. Yellow threshold 75:
   - acceptable if testing-only is capped; risky if customer_quality is overfilled.
5. Green threshold 87 / revision 55:
   - should stay strict; C06 needs qualification/customer shipment proof.
6. price-only blowoff guard:
   - correct; SKH July local peak should not become full 4B.
7. full 4B non-price requirement:
   - strengthened.
8. hard 4C routing:
   - kept; Samsung qualification failure is exactly the kind of route it should catch.
```

## 14. Stage2 / Yellow / Green Comparison

C06 cannot treat all HBM narratives the same.

| evidence type | recommended max stage before revision/qualification | reason |
|---|---|---|
| Customer testing / Nvidia evaluating / placard / “could order” | Stage2-Watch or Stage3-Yellow cap | It is option value, not durable customer evidence. |
| Sold-out HBM capacity / confirmed HBM shipment / production allocation | Stage2-Actionable to Green bridge | It maps to demand certainty and capacity scarcity. |
| Qualification failure / heat-power issue / customer standard not met | 4C or hard 4C watch | It directly breaks the C06 customer-quality thesis. |

## 15. 4B Local vs Full-window Timing Audit

The SK Hynix July 2024 local peak is a good reason to keep the existing full-4B guardrail.

```text
Stage2_Actionable_entry_price = 173200
Stage4B_local_entry_price = 241000
local_peak_price_after_Stage2 = 248500
conservative_full_window_reference = latest_profile_close 949000, not full peak
four_b_local_peak_proximity = (241000 - 173200) / (248500 - 173200) = 0.93
four_b_full_window_peak_proximity <= (241000 - 173200) / (949000 - 173200) = 0.13
```

Interpretation:

```text
local proximity high + full-window proximity low = price_only_local_4B_too_early
```

This strengthens `full_4b_requires_non_price_evidence` but does not propose a new global 4B rule.

## 16. 4C Protection Audit

Samsung’s May 2024 qualification failure route:

```text
entry_price_after_4C = 75900
90D low = 58900
180D low = 49900
peak_after_watch = 88800
max_drawdown_from_peak_to_180D_low = -43.81%
MAE_90D_after_4C = -22.40%
MAE_180D_after_4C = -34.26%
four_c_protection_label = hard_4c_success_if_taken_as_thesis_break
```

The 4C was not a buy/sell recommendation; it is a thesis-break protection row.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
candidate_axis = L2_customer_capacity_vs_testing_split
status = sector_shadow_only
```

Candidate rule:

```text
In L2 AI/semiconductor, customer evaluation/testing language can support Stage2-Watch,
but customer_quality_score should not be upgraded to Green-level evidence until at least one of:
- qualification pass,
- shipment start,
- sold-out capacity,
- customer-specific volume allocation,
- repeated public financial revision linked to the product.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
candidate_axis = c06_hbm_customer_qualification_required_for_green
status = canonical_shadow_only
```

C06 shadow rule:

```text
if evidence_family == customer_testing_or_evaluation_only:
    cap_stage = Stage2-Watch or Stage3-Yellow
    customer_quality_score_max = low_to_mid
    green_allowed = false

if evidence_family includes sold_out_capacity or confirmed_customer_supply or HBM shipment start:
    allow Stage2A bonus
    allow Green bridge if revision/margin visibility also present

if evidence_family includes qualification_failure or heat/power standard failure:
    route_to = 4C_thesis_break_watch_or_4C
```

## 19. Before / After Backtest Comparison

| profile | selected logic | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 current calibrated proxy | global rules only | 24.15% | -13.85% | 24.15% | -27.60% | mixed |
| P0b rollback baseline | no canonical split | 24.15% | -13.85% | 24.15% | -27.60% | inferior because testing-only may over-score |
| P1 L2 sector candidate | capacity/testing split | 30.24% | -17.44% | 30.24% | -27.19% | better but broad |
| P2 C06 candidate | qualification/capacity required for Green | 24.15% | -13.85% | 24.15% | -27.60% | best explanatory fit |
| P3 counterexample guard | 4C on qualification failure | 16.99% | -22.40% | 16.99% | -34.26% | protective, not positive |

## 20. Score-Return Alignment Matrix

| case | raw score issue | return path | alignment |
|---|---|---|---|
| SKH sold-out | capacity/customer quality deserves boost | +43.48% 90D MFE | aligned |
| Samsung testing | customer_quality overfilled before qualification | -37.07% 180D MAE | residual false positive |
| Samsung 4C | qualification failure should dominate prior optionality | -34.26% 180D MAE after break | aligned as 4C |
| SKH local 4B | price-only local peak lacks thesis break | later full-window price far exceeded local peak | guardrail aligned |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_CUSTOMER_CAPACITY_QUALIFICATION_SOLDOUT_SPLIT | 1 | 2 | 1 | 1 | 3 | 1 | 4 | 2 | 2 | true | true | Need more non-SKH/Samsung C06 holdout rows and exact source URL enrichment. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids: R2L10_C06_000660_PRICE_ONLY_LOCAL_4B_TOO_EARLY
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - customer_testing_without_qualification_false_positive
  - qualification_failure_thesis_break
  - price_only_local_4B_too_early
new_axis_proposed:
  - c06_hbm_customer_capacity_soldout_bridge
  - c06_customer_testing_without_qualification_cap
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
- R2 / L2 round-sector consistency
- C06 canonical archetype mapping
- stock-web manifest max_date = 2026-02-20
- tradable_raw OHLC paths for 000660 and 005930
- 30D / 90D / 180D MFE and MAE for selected triggers
- corporate-action 180D windows clean by profile candidate dates
- positive/counterexample balance
- local vs full-window 4B split
```

Not validated:

```text
- No production scoring patch was made.
- No stock_agent src/e2r code was read.
- No live candidate scan was performed.
- Exact filing/news URL enrichment should still be run before production promotion.
- Foreign HBM peers are narrative-only because they are not in Korean stock-web atlas.
```

## 24. Shadow Weight Calibration

| axis | scope | delta | confidence | proposal_type |
|---|---|---:|---|---|
| c06_hbm_customer_capacity_soldout_bridge | canonical_archetype_specific | +2 to +3 research proxy | medium_low | canonical_shadow_only |
| c06_customer_testing_without_qualification_cap | canonical_archetype_specific | cap to Stage2-Watch/Yellow | medium | canonical_guard_shadow_only |
| full_4b_requires_non_price_evidence | existing global guard | strengthened | high | existing_axis_strengthened |
| hard_4c_thesis_break_routes_to_4c | existing global guard | kept/strengthened | high | existing_axis_strengthened |

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R2L10_C06_000660_HBM3E_SOLDOUT_CAPACITY","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_CUSTOMER_CAPACITY_SOLDOUT_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L10_C06_000660_20240502_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Reuters reported SK Hynix HBM chips sold out for 2024 and almost sold out for 2025; company guided 12-layer HBM3E samples in May and Q3 mass production."}
{"row_type":"case","case_id":"R2L10_C06_005930_CUSTOMER_TESTING_OPTIONALITY_FALSE_POSITIVE","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_TESTING_WITHOUT_QUALIFICATION","case_type":"false_positive_green_risk","positive_or_counterexample":"counterexample","best_trigger":"R2L10_C06_005930_20240320_STAGE2WATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"residual_or_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Reports around Nvidia GTC described Nvidia testing Samsung next-generation HBM and investor expectation of possible future orders; no formal order or qualification was announced."}
{"row_type":"case","case_id":"R2L10_C06_005930_HBM_QUALIFICATION_FAILURE_4C","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_QUALIFICATION_FAILURE_HEAT_POWER_THESIS_BREAK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"R2L10_C06_005930_20240524_4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol as March watch trigger but new trigger family: hard qualification failure / thesis-break timing","independent_evidence_weight":0.5,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct_if_4C_router_receives_exact_qualification_failure","price_source":"Songdaiki/stock-web","notes":"Reuters reported Samsung's HBM3/HBM3E had not passed Nvidia tests due to heat and power issues; Samsung disputed specific claims but said optimization was ongoing."}
{"row_type":"case","case_id":"R2L10_C06_000660_PRICE_ONLY_LOCAL_4B_TOO_EARLY","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PRICE_ONLY_LOCAL_PEAK_NOT_FULL_4B","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"R2L10_C06_000660_20240711_4B_LOCAL","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same symbol reused only for distinct 4B local-vs-full timing audit","independent_evidence_weight":0.25,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Local price peak occurred after strong HBM momentum; no non-price evidence of HBM order cut, qualification break, or margin thesis break was present in this local-peak-only row."}
{"row_type":"trigger","trigger_id":"R2L10_C06_000660_20240502_STAGE2A","case_id":"R2L10_C06_000660_HBM3E_SOLDOUT_CAPACITY","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_CUSTOMER_CAPACITY_SOLDOUT_BRIDGE","sector":"AI·반도체·전자부품","primary_archetype":"HBM memory customer/capacity rerating","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-02","entry_date":"2024-05-03","entry_price":173200,"evidence_available_at_that_date":"Reuters reported SK Hynix HBM chips sold out for 2024 and almost sold out for 2025; company guided 12-layer HBM3E samples in May and Q3 mass production.","evidence_source":"Reuters 2024-05-02 https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-hbm-chips-almost-sold-out-2025-2024-05-02/ ; Reuters 2024-09-04 https://www.reuters.com/technology/sk-hynix-start-mass-producing-hbm3e-12-layer-chips-this-month-2024-09-04/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","durable_customer_confirmation","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.39,"MFE_90D_pct":43.48,"MFE_180D_pct":43.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":0.0,"MAE_90D_pct":-12.47,"MAE_180D_pct":-12.47,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500,"drawdown_after_peak_pct":-38.99,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger_in_trigger_set","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000660_20240503_173200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L10_C06_005930_20240320_STAGE2WATCH","case_id":"R2L10_C06_005930_CUSTOMER_TESTING_OPTIONALITY_FALSE_POSITIVE","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_TESTING_WITHOUT_QUALIFICATION","sector":"AI·반도체·전자부품","primary_archetype":"HBM memory customer/capacity rerating","loop_objective":"counterexample_mining|green_strictness_stress_test|sector_specific_rule_discovery","trigger_type":"Stage2-Watch","trigger_date":"2024-03-20","entry_date":"2024-03-21","entry_price":79300,"evidence_available_at_that_date":"Reports around Nvidia GTC described Nvidia testing Samsung next-generation HBM and investor expectation of possible future orders; no formal order or qualification was announced.","evidence_source":"Investopedia 2024-03-20 https://www.investopedia.com/samsung-stock-jumps-on-reports-nvidia-may-order-next-gen-memory-chips-8611507 ; Reuters 2024-05-24 https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":["qualification_failure","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.45,"MFE_90D_pct":11.98,"MFE_180D_pct":11.98,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.3,"MAE_90D_pct":-6.68,"MAE_180D_pct":-37.07,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":88800,"drawdown_after_peak_pct":-43.81,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only_until_qualification_failure_report","trigger_outcome_label":"false_positive_green_risk","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"005930_20240321_79300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L10_C06_005930_20240524_4C","case_id":"R2L10_C06_005930_HBM_QUALIFICATION_FAILURE_4C","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_QUALIFICATION_FAILURE_HEAT_POWER_THESIS_BREAK","sector":"AI·반도체·전자부품","primary_archetype":"HBM memory customer/capacity rerating","loop_objective":"4C_thesis_break_timing_test|counterexample_mining|current_profile_stress_test","trigger_type":"4C","trigger_date":"2024-05-24","entry_date":"2024-05-24","entry_price":75900,"evidence_available_at_that_date":"Reuters reported Samsung's HBM3/HBM3E had not passed Nvidia tests due to heat and power issues; Samsung disputed specific claims but said optimization was ongoing.","evidence_source":"Reuters 2024-05-24 https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/ ; Reuters 2024-07-23 https://www.reuters.com/technology/nvidia-clears-samsungs-hbm3-chips-use-china-market-processor-sources-say-2024-07-23/","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":["qualification_failure","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.76,"MFE_90D_pct":16.99,"MFE_180D_pct":16.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.16,"MAE_90D_pct":-22.4,"MAE_180D_pct":-34.26,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":88800,"drawdown_after_peak_pct":-43.81,"green_lateness_ratio":"not_applicable:4C_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"explicit_event_cap_before_drawdown","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_if_taken_as_thesis_break","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_correct_if_4C_router_receives_exact_qualification_failure","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"005930_20240524_75900","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":"same symbol as March watch trigger but new trigger family: hard qualification failure / thesis-break timing","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L10_C06_000660_20240711_4B_LOCAL","case_id":"R2L10_C06_000660_PRICE_ONLY_LOCAL_4B_TOO_EARLY","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_PRICE_ONLY_LOCAL_PEAK_NOT_FULL_4B","sector":"AI·반도체·전자부품","primary_archetype":"HBM memory customer/capacity rerating","loop_objective":"4B_non_price_requirement_stress_test|holdout_validation","trigger_type":"4B-local-price-only","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":241000,"evidence_available_at_that_date":"Local price peak occurred after strong HBM momentum; no non-price evidence of HBM order cut, qualification break, or margin thesis break was present in this local-peak-only row.","evidence_source":"Stock-web OHLC local peak only; no non-price 4B evidence used.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.11,"MFE_90D_pct":3.11,"MFE_180D_pct":3.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-37.1,"MAE_90D_pct":-39.96,"MAE_180D_pct":-39.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500,"drawdown_after_peak_pct":-39.96,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.13,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_4C","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"000660_20240711_241000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol reused only for distinct 4B local-vs-full timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L10_C06_000660_HBM3E_SOLDOUT_CAPACITY","trigger_id":"R2L10_C06_000660_20240502_STAGE2A","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow/near-Green","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":8,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":8,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green-shadow","changed_components":["customer_quality_score","backlog_visibility_score","revision_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile requires confirmed HBM qualification/customer capacity; customer-testing-only is capped, sold-out/ship evidence is upgraded, and price-only local 4B is not promoted to full 4B.","MFE_90D_pct":43.48,"MAE_90D_pct":-12.47,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L10_C06_005930_CUSTOMER_TESTING_OPTIONALITY_FALSE_POSITIVE","trigger_id":"R2L10_C06_005930_20240320_STAGE2WATCH","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow-risk/false-Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68.0,"stage_label_after":"Stage2-Watch-capped","changed_components":["customer_quality_score","backlog_visibility_score","revision_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile requires confirmed HBM qualification/customer capacity; customer-testing-only is capped, sold-out/ship evidence is upgraded, and price-only local 4B is not promoted to full 4B.","MFE_90D_pct":11.98,"MAE_90D_pct":-6.68,"score_return_alignment_label":"residual_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L10_C06_005930_HBM_QUALIFICATION_FAILURE_4C","trigger_id":"R2L10_C06_005930_20240524_4C","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58.0,"stage_label_before":"Stage2-Watch/4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":9,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":42.0,"stage_label_after":"4C-thesis-break","changed_components":["customer_quality_score","backlog_visibility_score","revision_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile requires confirmed HBM qualification/customer capacity; customer-testing-only is capped, sold-out/ship evidence is upgraded, and price-only local 4B is not promoted to full 4B.","MFE_90D_pct":16.99,"MAE_90D_pct":-22.4,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct_if_4C_router_receives_exact_qualification_failure"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L10_C06_000660_PRICE_ONLY_LOCAL_4B_TOO_EARLY","trigger_id":"R2L10_C06_000660_20240711_4B_LOCAL","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":8,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":9,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":91.0,"stage_label_before":"Stage3-Green-with-local-4B-risk","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":8,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":9,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90.0,"stage_label_after":"Stage3-Green-price-only-4B-not-full","changed_components":["customer_quality_score","backlog_visibility_score","revision_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile requires confirmed HBM qualification/customer capacity; customer-testing-only is capped, sold-out/ship evidence is upgraded, and price-only local 4B is not promoted to full 4B.","MFE_90D_pct":3.11,"MAE_90D_pct":-39.96,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"shadow_weight","axis":"c06_hbm_customer_capacity_soldout_bridge","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","baseline_value":0,"tested_value":1,"delta":"+2_to_+3_research_proxy","reason":"HBM sold-out / confirmed shipment capacity evidence separated SK Hynix from Samsung customer-testing-only optionality.","backtest_effect":"SK Hynix May 2024 trigger produced +43.48% 90D MFE with -12.47% MAE; Samsung testing-only watch later produced -37.07% 180D MAE.","trigger_ids":"R2L10_C06_000660_20240502_STAGE2A|R2L10_C06_005930_20240320_STAGE2WATCH|R2L10_C06_005930_20240524_4C","calibration_usable_count":3,"new_independent_case_count":3,"counterexample_count":2,"confidence":"medium_low","proposal_type":"canonical_shadow_only","notes":"Do not promote to production until exact evidence URL enrichment confirms trigger-time availability.","shadow_weight":1}
{"row_type":"shadow_weight","axis":"c06_customer_testing_without_qualification_cap","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","baseline_value":0,"tested_value":1,"delta":"cap_to_stage2_watch_or_yellow","reason":"Nvidia testing/placard expectation without qualification behaved like optionality, not durable customer-quality evidence.","backtest_effect":"Samsung March 2024 watch trigger had only +11.98% 180D MFE but -37.07% 180D MAE after qualification failure and memory underperformance.","trigger_ids":"R2L10_C06_005930_20240320_STAGE2WATCH|R2L10_C06_005930_20240524_4C","calibration_usable_count":2,"new_independent_case_count":2,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_guard_shadow_only","notes":"Strengthens existing Green strictness but does not change global threshold.","shadow_weight":1}
{"row_type":"residual_contribution","round":"R2","loop":"10","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":3,"reused_case_count":1,"new_symbol_count":2,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["customer_testing_without_qualification_false_positive","qualification_failure_thesis_break","price_only_local_4B_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R2L10_C06_EXTERNAL_MICRON_HBM3E","symbol":"MU","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","reason":"Foreign ticker not present in Korean stock-web atlas; used only as external industry context, not weight calibration.","price_source":"not_stock_web_korea","usage":"not_weight_calibration"}
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
completed_round = R2
completed_loop = 10
next_round = R3
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Research artifact and price atlas sources checked:

```text
stock_agent allowed artifacts:
- reports/e2r_calibration/ingest_summary.md
- reports/e2r_calibration/applied_scoring_diff.md
- reports/e2r_calibration/calibrated_profile_report.md
- data/e2r/calibration/md_registry.jsonl

stock-web files:
- atlas/manifest.json
- diagnostics/chatgpt_bundle.txt
- atlas/symbol_profiles/000/000660.json
- atlas/symbol_profiles/005/005930.json
- atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005930/2025.csv
```

External historical evidence sources:

```text
- Reuters, 2024-05-02, Nvidia supplier SK Hynix says HBM chips almost sold out for 2025.
- Reuters, 2024-05-24, Samsung's HBM chips failing Nvidia tests due to heat and power consumption woes, sources say.
- Reuters, 2024-07-23, Nvidia clears Samsung's HBM3 chips for use in China-market processor.
- Reuters, 2024-09-04, SK Hynix to start mass producing HBM3E 12-layer chips this month.
- Investopedia, 2024-03-20, Samsung stock jumps on reports Nvidia may order next-gen memory chips.
```
