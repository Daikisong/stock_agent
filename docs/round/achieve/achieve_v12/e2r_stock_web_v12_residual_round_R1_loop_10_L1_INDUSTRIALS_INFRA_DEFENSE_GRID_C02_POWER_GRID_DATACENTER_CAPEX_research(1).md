# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R1_loop_10_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md

scheduled_round = R1
scheduled_loop = 10
completed_round = R1
completed_loop = 10
next_round = R2
next_loop = 10

round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = GRID_TRANSFORMER_AI_DATACENTER_HVDC_CAPEX

stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

One-line contribution:

```text
This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.
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

This MD does **not** re-prove the global rule that Stage2 is earlier than Green.  
It asks a narrower question: inside C02 grid/datacenter-capex transformer names, does the current calibrated profile still underweight backlog/capacity/customer-quality bridge before formal Green confirmation, and does C02 need a high-MAE / price-only-4B watch guard?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R1
allowed_large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
round_sector_consistency = pass
```

Selected C02 because the R1 grid transformer cluster is a clean place to separate three things that are often tangled:

1. real structural grid/datacenter transformer rerating,
2. high-MAE early Stage2 paths that still worked,
3. price-only local 4B signals that would have exited too early without non-price evidence.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts reviewed:

```text
reports/e2r_calibration/ingest_summary.md
data/e2r/calibration/md_registry.jsonl
```

Observed registry state:

```text
ingest_summary.rounds_covered = R1~R13
ingest_summary.loops_covered = 1~9
R1 historical calibration rows exist through loop 9
corrected v12-style R1 loop 10 was not found in the accessible registry
scheduled_round = R1
scheduled_loop = 10
```

Duplicate avoidance rule used here:

```text
same canonical_archetype_id repetition = allowed
same symbol + same trigger_date + same entry_date + same evidence family = avoided
```

This loop uses three C02 symbols:

```text
267260 HD현대일렉트릭
298040 효성중공업
010120 LS ELECTRIC
```

The LS 4B row reuses the same symbol but uses a different trigger family and is marked as a 4B overlay / counterexample, not as a new representative aggregate case.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Manifest validation:

```text
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
validation_status = usable_for_historical_calibration
```

Caveat:

```text
Raw/unadjusted OHLC.
Corporate actions are not adjusted.
Corporate-action contaminated 180D windows must be blocked.
Zero-volume and invalid OHLC rows are excluded from tradable shards.
```

## 5. Historical Eligibility Gate

| symbol | profile_path | 180D forward window | corporate action in 180D | calibration_usable |
|---|---|---:|---:|---:|
| 267260 | atlas/symbol_profiles/267/267260.json | yes | no 2024 overlap | true |
| 298040 | atlas/symbol_profiles/298/298040.json | yes | none | true |
| 010120 | atlas/symbol_profiles/010/010120.json | yes | no 2024 overlap | true |
| 010120 4B-watch | atlas/symbol_profiles/010/010120.json | yes | no 2024 overlap | true |

Validation scope:

```text
quantitative_stock_web_ohlc_validation = complete_for_30D_90D_180D
evidence_url_validation = partial
exact_original_disclosure_url_enrichment_required = true
production_promotion_allowed_now = false
shadow_weight_only = true
```

The MD is therefore usable for **price-path residual shape** and shadow-rule design, but any coding-agent promotion batch should enrich exact historical evidence URLs before production scoring change.

## 6. Canonical Archetype Compression Map

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_ids =
  - GRID_TRANSFORMER_EXPORT_BACKLOG_DATACENTER_CAPEX
  - GRID_HVDC_TRANSFORMER_CAPACITY_ROUTE
  - GRID_DATACENTER_US_BUSINESS_HIGH_MAE
  - PRICE_ONLY_LOCAL_PEAK_NOT_FULL_4B
```

Compression thesis:

```text
C02 should not be a generic “industrial order” rule.
It is specifically a power-grid / transformer / datacenter-capex bottleneck rule:
  customer/order quality + backlog/delivery visibility + capacity route + margin/revision follow-through.
```

## 7. Case Selection Summary

|case_id|symbol|role|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|profile verdict|
|---|---|---|---|---|---|---|---|---|---|
|267260|267260 HD현대일렉트릭|positive structural_success|2024-01-03|85,800|+219.93%|-5.24%|+336.48%|-5.24%|current_profile_too_late|
|298040|298040 효성중공업|positive structural_success|2024-01-03|167,900|+112.63%|-7.03%|+179.33%|-7.03%|current_profile_too_late|
|010120|010120 LS ELECTRIC|positive high_MAE_success|2024-01-03|73,500|+170.75%|-14.15%|+273.47%|-14.15%|current_profile_too_late|
|010120_4B|010120 LS ELECTRIC|counterexample 4B_too_early|2024-04-12|139,700|+96.49%|-9.66%|+96.49%|-9.66%|current_profile_correct|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
calibration_usable_case_count = 3 representative + 1 overlay
new_independent_case_count = 3
reused_case_count = 1
minimum_new_independent_case_ratio = 3 / 4 = 0.75
minimum_positive_case_count_pass = true
minimum_counterexample_count_pass = true
minimum_calibration_usable_case_count_pass = true
```

Interpretation:

```text
HD현대일렉트릭 and 효성중공업 = clean structural successes.
LS ELECTRIC Stage2 = high-MAE success; good for Stage2 bridge, not automatic Green.
LS ELECTRIC 4B-watch = price-only local 4B counterexample; strengthens non-price 4B requirement.
```

## 9. Evidence Source Map

| symbol | evidence status | evidence fields used | note |
|---|---|---|---|
| 267260 | source_url_pending | customer/order quality, backlog/delivery visibility, relative strength, capacity route | Non-price C02 context is acceptable for shadow research, but exact original URL enrichment is required before production promotion. |
| 298040 | source_url_pending | transformer/HVDC capability, capacity route, policy/grid optionality | Clean OHLC path; evidence URL enrichment required. |
| 010120 | source_url_pending + later public analyst context | U.S. business/datacenter opportunity, grid electrical equipment demand | High-MAE path means this should be a Stage2/Yelow bridge with guard, not loose Green. |
| 010120 4B | price-only stress row | price-only local peak | Not a full 4B because non-price evidence is absent. |

## 10. Price Data Source Map

| symbol | company_name | shard_path | profile_path | entry basis |
|---|---|---|---|---|
| 267260 | HD현대일렉트릭 | atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv | atlas/symbol_profiles/267/267260.json | 2024-01-03 close |
| 298040 | 효성중공업 | atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv | atlas/symbol_profiles/298/298040.json | 2024-01-03 close |
| 010120 | LS ELECTRIC | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json | 2024-01-03 close |
| 010120 | LS ELECTRIC | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv | atlas/symbol_profiles/010/010120.json | 2024-04-12 close |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|dedupe|role|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R1L10_C02_267260_STAGE2A_2024_01_03|267260|Stage2-Actionable|2024-01-03 @ 85800|39.04|219.93|336.48|-5.24|-5.24|-5.24|True|representative|
|R1L10_C02_298040_STAGE2A_2024_01_03|298040|Stage2-Actionable|2024-01-03 @ 167900|14.23|112.63|179.33|-7.03|-7.03|-7.03|True|representative|
|R1L10_C02_010120_STAGE2A_2024_01_03|010120|Stage2-Actionable|2024-01-03 @ 73500|6.12|170.75|273.47|-12.52|-14.15|-14.15|True|representative|
|R1L10_C02_010120_4B_WATCH_2024_04_12|010120|4B-watch|2024-04-12 @ 139700|74.66|96.49|96.49|-7.59|-9.66|-9.66|False|4B_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate triggers

| symbol | entry | peak_date | peak_price | drawdown_after_peak | return shape |
|---|---:|---:|---:|---:|---|
| 267260 | 2024-01-03 @ 85,800 | 2024-07-24 | 374,500 | -39.79% | clean C02 success: low early MAE, very large MFE |
| 298040 | 2024-01-03 @ 167,900 | 2024-05-28 | 469,000 | -50.75% | clean C02 success, but more violent post-peak path |
| 010120 | 2024-01-03 @ 73,500 | 2024-07-24 | 274,500 | -54.03% | high-MAE success: bridge worked, but early risk was large |

### 4B overlay trigger

| symbol | trigger | entry | local_peak_reference | full_peak_reference | verdict |
|---|---|---:|---:|---:|---|
| 010120 | price-only 4B-watch | 2024-04-12 @ 139,700 | 2024-05-29 high 244,000 | 2024-07-24 high 274,500 | price_only_local_4B_too_early |

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| How would current profile judge these cases? | It would likely catch Stage2-Actionable / Yellow but hesitate to give Green before revision/margin confirmation. |
| Did that match MFE/MAE? | Directionally yes for Stage2, but too late for C02 structural Green in HD/Hyosung; LS shows why loosened Green needs a high-MAE guard. |
| Was Stage2 bonus too strong? | Not too strong for C02 when non-price backlog/capacity/customer quality exists. |
| Was Yellow 75 too high/low? | Slightly too high for early C02 if the case already has transformer-capacity bridge. |
| Was Green 87/revision 55 too high/low? | Correct globally; for C02, a narrow shadow bridge can move selected names toward Green-candidate earlier. |
| Was price-only blowoff guard appropriate? | Yes. |
| Was full 4B non-price requirement appropriate? | Yes; LS April price-only local 4B would have been too early. |
| Was hard 4C routing too late/early? | Not enough hard 4C evidence in this loop. |

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2-Actionable works for C02 when:
  - transformer/grid/datacenter demand is not merely theme language,
  - customer/order quality is visible,
  - backlog/delivery or capacity route is visible,
  - price action confirms but does not replace evidence.

Yellow/Green problem:
  - current profile is safe globally,
  - but C02 successes often rerate before full formal revision confirmation,
  - therefore C02 needs a shadow bridge, not a global threshold cut.
```

Green lateness:

```text
HD현대일렉트릭 = current_profile_too_late for Green; Stage2 bridge aligned.
효성중공업 = current_profile_too_late for Green; Stage2 bridge aligned.
LS ELECTRIC = current_profile_too_late but high-MAE guard required.
```

## 15. 4B Local vs Full-window Timing Audit

Formula:

```text
four_b_local_peak_proximity =
(Stage4B_entry_price - Stage2_Actionable_entry_price)
/ (local_peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)

four_b_full_window_peak_proximity =
(Stage4B_entry_price - Stage2_Actionable_entry_price)
/ (full_window_peak_price_after_Stage2_Actionable - Stage2_Actionable_entry_price)
```

LS ELECTRIC price-only 4B-watch row:

```text
Stage2_Actionable_entry_price = 73,500
Stage4B_watch_entry_price = 139,700
local_peak_price_after_Stage2 = 244,000
full_window_peak_price_after_Stage2 = 274,500

four_b_local_peak_proximity = 0.388
four_b_full_window_peak_proximity = 0.329
four_b_timing_verdict = price_only_local_4B_too_early
four_b_evidence_type = price_only
do_not_treat_as_full_4B = true
```

This strengthens the existing rule:

```text
full_4b_requires_non_price_evidence = true
```

## 16. 4C Protection Audit

No hard 4C thesis-break row is promoted in this loop.

```text
four_c_protection_label = not_tested
hard_4c_success_count = 0
hard_4c_late_count = 0
thesis_break_watch_only = true
```

C02 still needs future R1/R13 rows for:

```text
- transformer order cancellation or call-off,
- margin/backlog reversal,
- capex delay,
- accounting/trust break,
- post-peak 4C timing.
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
candidate_axis = L1_grid_capex_order_capacity_bridge
proposal_type = sector_shadow_only
```

Rule candidate:

```text
Inside L1, if the case is grid/datacenter power equipment and has customer/order quality + backlog/delivery visibility + capacity route, then Stage2-Actionable should receive a sector shadow bridge. Do not apply to generic industrial order wins or EPC contracts.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
candidate_axis = c02_grid_datacenter_order_capacity_visibility_bridge_bonus
tested_delta = +1 shadow
```

Canonical rule:

```text
C02 should upweight backlog_visibility_score, customer_quality_score, capacity_or_shipment_score and margin_bridge_score when all are supported by non-price evidence.
```

Guard:

```text
If early MAE exceeds roughly -10% to -15% before confirmed revision/margin follow-through, classify as Stage2/Yelow with high-MAE watch, not Green.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|eligible_trigger_count|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural_count|late_green_count|alignment verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current|Global calibrated profile catches Stage2 bridge but is late for C02 Green.|3|167.77%|-8.81%|263.09%|-8.81%|0/3|2|2|good Stage2, late Green|
|P0b e2r_2_0_baseline_reference|rollback|Earlier baseline would underweight C02 backlog/capacity bridge.|3|167.77%|-8.81%|263.09%|-8.81%|0/3|3|3|too late / underfit|
|P1 sector_specific_candidate_profile|L1|Add L1 grid-capex bridge but keep high-MAE watch.|3|167.77%|-8.81%|263.09%|-8.81%|0/3|1|1|improves missed structural|
|P2 canonical_archetype_candidate_profile|C02|C02 transformer/datacenter order-capacity bridge +1 shadow.|3|167.77%|-8.81%|263.09%|-8.81%|0/3|0|0|best fit, needs source enrichment|
|P3 counterexample_guard_profile|C02 risk|Keep price-only 4B as watch-only unless non-price evidence exists.|1|96.49%|-9.66%|96.49%|-9.66%|0/1|0|0|prevents early full 4B|

## 20. Score-Return Alignment Matrix

| symbol | before score/stage | after shadow score/stage | return alignment | interpretation |
|---|---|---|---|---|
| 267260 | 82 / Stage3-Yellow | 88.5 / Green-candidate-shadow | strong | C02 bridge would reduce Green lateness. |
| 298040 | 77.5 / Stage3-Yellow | 84.0 / stronger Yellow | strong | Do not force Green; capacity/HVDC route improves bridge. |
| 010120 | 73.0 / Stage2-Actionable | 79.0 / Yellow-candidate with high-MAE watch | mixed-positive | Captures structural move but preserves risk guard. |
| 010120 4B | 64 / 4B-watch | 64 / watch-only | protective | Prevents price-only early full 4B. |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L1_INDUSTRIALS_INFRA_DEFENSE_GRID|C02_POWER_GRID_DATACENTER_CAPEX|GRID_TRANSFORMER_AI_DATACENTER_HVDC_CAPEX|3|1|1|0|3|1|4|3|2|True|True|C02 now has clean transformer positives plus a price-only 4B counterexample; still needs exact source URL enrichment and more failed-rerating cases.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids: R1L10_C02_010120_PRICE_ONLY_LOCAL_4B_TOO_EARLY
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 1
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 2
positive_case_count: 3
counterexample_count: 1
current_profile_error_count: 2

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence

residual_error_types_found:
  - current_profile_too_late_for_C02_green
  - high_MAE_success_needs_guard
  - price_only_local_4B_too_early

new_axis_proposed:
  - c02_grid_datacenter_order_capacity_visibility_bridge_bonus_shadow_only

existing_axis_strengthened:
  - full_4b_requires_non_price_evidence

existing_axis_weakened:
  - null

existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

Diversity score summary:

```text
same_archetype_new_symbol_bonus = +12
new_symbol_bonus = +9
counterexample_gap_bonus = +4
residual_error_bonus = +10
same_archetype_new_trigger_family_bonus = +4
repeated_same_symbol_penalty = -5
estimated_diversity_score = +34
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price-basis context
- tradable shard paths for all selected symbols
- symbol profile corporate-action windows
- 30D / 90D / 180D MFE and MAE
- local 4B vs full-window 4B separation for LS ELECTRIC
- duplicate handling: 3 representative rows + 1 overlay row
```

Not validated in this MD:

```text
- exact original disclosure/news URLs for every trigger
- production scoring implementation
- live watchlist or current candidate status
- 1Y / 2Y forward windows
- hard 4C thesis-break rows
```

Therefore:

```text
production_scoring_changed = false
shadow_weight_only = true
exact_source_url_enrichment_required_before_promotion = true
```

## 24. Shadow Weight Calibration

| axis | scope | delta | backtest effect | confidence | proposal |
|---|---|---:|---|---|---|
| c02_grid_datacenter_order_capacity_visibility_bridge_bonus | canonical C02 | +1 shadow | reduces C02 missed structural / late Green | medium-low until URL enrichment | canonical_shadow_only |
| c02_high_mae_stage2_watch_guard | canonical C02 | +1 guard | captures LS-like high-MAE success without loose Green | medium | risk_guard_shadow_only |
| full_4b_requires_non_price_evidence | existing axis | 0 keep | prevents price-only early full 4B | medium | existing_axis_strengthened |

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R1L10_C02_267260_GRID_TRANSFORMER_SUCCESS","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_TRANSFORMER_EXPORT_BACKLOG_DATACENTER_CAPEX","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R1L10_C02_267260_STAGE2A_2024_01_03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2-Actionable / Yellow-era non-price grid transformer visibility aligned with clean 180D MFE >300% and contained early MAE.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Quantitative price validation clean. Exact original event URL should be enriched during batch ingest; non-price evidence summary is transformer/export/backlog/datacenter-grid demand context."}
{"row_type":"case","case_id":"R1L10_C02_298040_GRID_HVDC_SUCCESS","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_HVDC_TRANSFORMER_CAPACITY_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R1L10_C02_298040_STAGE2A_2024_01_03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Power transformer/HVDC capability and grid bottleneck context aligned with clean 180D MFE near 180%.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Clean symbol profile, no corporate-action candidate dates. Original event URL enrichment required before any production promotion."}
{"row_type":"case","case_id":"R1L10_C02_010120_GRID_DATACENTER_HIGH_MAE_SUCCESS","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_DATACENTER_US_BUSINESS_HIGH_MAE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R1L10_C02_010120_STAGE2A_2024_01_03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"The return path supports C02 structural bridge, but early MAE is deeper than HD/Hyosung and needs a high-MAE guard.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Manual shard calculation. High-MAE success should not loosen Green without margin/revision follow-through."}
{"row_type":"case","case_id":"R1L10_C02_010120_PRICE_ONLY_LOCAL_4B_TOO_EARLY","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"PRICE_ONLY_LOCAL_PEAK_NOT_FULL_4B","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"R1L10_C02_010120_4B_WATCH_2024_04_12","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"Same symbol reused for a different trigger family: price-only local 4B watch versus Stage2 entry.","independent_evidence_weight":0.5,"score_price_alignment":"A price-only local overheat flag around April would have arrived too early versus the full-window July peak.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"This row strengthens the existing full_4b_requires_non_price_evidence axis; it is not a positive promotion row."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R1L10_C02_267260_STAGE2A_2024_01_03","case_id":"R1L10_C02_267260_GRID_TRANSFORMER_SUCCESS","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_TRANSFORMER_EXPORT_BACKLOG_DATACENTER_CAPEX","sector":"산업재·수주·인프라·전력망","primary_archetype":"C02 power grid / datacenter capex transformer rerating","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","stage2_actionable_bonus_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":85800,"evidence_available_at_that_date":"Grid transformer/export backlog visibility and AI/datacenter grid bottleneck narrative were publicly knowable by early 2024; exact event URL pending enrichment.","evidence_source":"public_evidence_summary_exact_url_pending; stock-web quantitative validation","stage2_evidence_fields":["customer_or_order_quality","relative_strength","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision_later","margin_bridge_later","financial_visibility_later"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.04,"MFE_90D_pct":219.93,"MFE_180D_pct":336.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.24,"MAE_90D_pct":-5.24,"MAE_180D_pct":-5.24,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":374500,"drawdown_after_peak_pct":-39.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_tested","trigger_outcome_label":"structural_success_clean_mfe","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"267260_2024-01-03_85800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L10_C02_298040_STAGE2A_2024_01_03","case_id":"R1L10_C02_298040_GRID_HVDC_SUCCESS","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_HVDC_TRANSFORMER_CAPACITY_ROUTE","sector":"산업재·수주·인프라·전력망","primary_archetype":"C02 power grid / HVDC transformer capacity route","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","stage2_actionable_bonus_stress_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":167900,"evidence_available_at_that_date":"Power transmission/distribution transformer capability and grid bottleneck context were publicly knowable; exact event URL pending enrichment.","evidence_source":"public_evidence_summary_exact_url_pending; stock-web quantitative validation","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision_later","margin_bridge_later","multiple_public_sources_later"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.23,"MFE_90D_pct":112.63,"MFE_180D_pct":179.33,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.03,"MAE_90D_pct":-7.03,"MAE_180D_pct":-7.03,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":469000,"drawdown_after_peak_pct":-50.75,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_tested","trigger_outcome_label":"structural_success_clean_mfe","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"298040_2024-01-03_167900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L10_C02_010120_STAGE2A_2024_01_03","case_id":"R1L10_C02_010120_GRID_DATACENTER_HIGH_MAE_SUCCESS","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_DATACENTER_US_BUSINESS_HIGH_MAE","sector":"산업재·수주·인프라·전력망","primary_archetype":"C02 power grid / U.S. datacenter electrical equipment opportunity","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","counterexample_mining"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":73500,"evidence_available_at_that_date":"Early-2024 grid/datacenter electrical equipment opportunity; later analyst evidence confirms U.S. business growth but exact early trigger URL is pending enrichment.","evidence_source":"public_evidence_summary_exact_url_pending; later public analyst note for context; stock-web quantitative validation","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision_later","margin_bridge_later"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.12,"MFE_90D_pct":170.75,"MFE_180D_pct":273.47,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.52,"MAE_90D_pct":-14.15,"MAE_180D_pct":-14.15,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":274500,"drawdown_after_peak_pct":-54.03,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_tested","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"010120_2024-01-03_73500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R1L10_C02_010120_4B_WATCH_2024_04_12","case_id":"R1L10_C02_010120_PRICE_ONLY_LOCAL_4B_TOO_EARLY","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"PRICE_ONLY_LOCAL_PEAK_NOT_FULL_4B","sector":"산업재·수주·인프라·전력망","primary_archetype":"C02 price-only local 4B watch","loop_objective":["4B_non_price_requirement_stress_test","counterexample_mining"],"trigger_type":"4B-watch","trigger_date":"2024-04-12","entry_date":"2024-04-12","entry_price":139700,"evidence_available_at_that_date":"Large price acceleration without separate non-price 4B evidence in this MD; used only as price-only local 4B stress test.","evidence_source":"price_only_from_stock_web; no_full_4B_non_price_evidence","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":74.66,"MFE_90D_pct":96.49,"MFE_180D_pct":96.49,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.59,"MAE_90D_pct":-9.66,"MAE_180D_pct":-9.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":274500,"drawdown_after_peak_pct":-54.03,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.388,"four_b_full_window_peak_proximity":0.329,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_tested","trigger_outcome_label":"4B_watch_counterexample_price_only_too_early","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"010120_2024-04-12_139700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"Same symbol as LS Stage2 case but different trigger family: 4B price-only watch.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L10_C02_267260_GRID_TRANSFORMER_SUCCESS","trigger_id":"R1L10_C02_267260_STAGE2A_2024_01_03","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"capacity_or_shipment_score":7,"fcf_conversion_score":5},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow / Stage2-Actionable bridge","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":9,"margin_bridge_score":7,"revision_score":8,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"capacity_or_shipment_score":8,"fcf_conversion_score":6},"weighted_score_after":88.5,"stage_label_after":"Stage3-Green-candidate-shadow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","capacity_or_shipment_score"],"component_delta_explanation":"C02-specific route gives extra weight only when transformer/grid backlog, capacity and customer quality are present together.","MFE_90D_pct":219.93,"MAE_90D_pct":-5.24,"score_return_alignment_label":"shadow_improves_green_lateness","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L10_C02_298040_GRID_HVDC_SUCCESS","trigger_id":"R1L10_C02_298040_STAGE2A_2024_01_03","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"capacity_or_shipment_score":6,"fcf_conversion_score":4},"weighted_score_before":77.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"capacity_or_shipment_score":7,"fcf_conversion_score":5},"weighted_score_after":84.0,"stage_label_after":"Stage3-Yellow-high-confidence-shadow","changed_components":["backlog_visibility_score","margin_bridge_score","capacity_or_shipment_score"],"component_delta_explanation":"HVDC/transformer capacity route supports stronger Yellow but not automatic Green without broader revision/margin confirmation.","MFE_90D_pct":112.63,"MAE_90D_pct":-7.03,"score_return_alignment_label":"shadow_improves_actionable_bridge","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L10_C02_010120_GRID_DATACENTER_HIGH_MAE_SUCCESS","trigger_id":"R1L10_C02_010120_STAGE2A_2024_01_03","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"capacity_or_shipment_score":5,"fcf_conversion_score":4},"weighted_score_before":73.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1,"capacity_or_shipment_score":6,"fcf_conversion_score":4,"high_mae_watch_score":6},"weighted_score_after":79.0,"stage_label_after":"Stage3-Yellow-candidate-with-high-MAE-watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","high_mae_watch_score"],"component_delta_explanation":"C02 bridge captures the later move but adds a high-MAE guard because early drawdown was much deeper than HD/Hyosung.","MFE_90D_pct":170.75,"MAE_90D_pct":-14.15,"score_return_alignment_label":"shadow_improves_missed_structural_but_needs_risk_guard","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R1L10_C02_010120_PRICE_ONLY_LOCAL_4B_TOO_EARLY","trigger_id":"R1L10_C02_010120_4B_WATCH_2024_04_12","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":7},"weighted_score_before":64.0,"stage_label_before":"4B-watch-price-only-local","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":8,"non_price_4b_evidence_score":0},"weighted_score_after":64.0,"stage_label_after":"4B-watch-only-not-full-4B","changed_components":["positioning_overheat_score","non_price_4b_evidence_score"],"component_delta_explanation":"No full-window 4B promotion without non-price evidence; price-only local heat remains a watch overlay.","MFE_90D_pct":96.49,"MAE_90D_pct":-9.66,"score_return_alignment_label":"guard_prevents_early_4B_exit","current_profile_verdict":"current_profile_correct"}
```

### 25.5 shadow_weight rows

```jsonl
{"row_type":"shadow_weight","axis":"c02_grid_datacenter_order_capacity_visibility_bridge_bonus","scope":"canonical_archetype_specific","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","baseline_value":0,"tested_value":1,"delta":"+1","reason":"Transformer/grid/datacenter/HVDC cases show very large 90D/180D MFE when backlog visibility, customer quality and capacity route co-occur.","backtest_effect":"Earlier C02 Stage2-Actionable to Yellow/Green candidate without changing global thresholds.","trigger_ids":"R1L10_C02_267260_STAGE2A_2024_01_03|R1L10_C02_298040_STAGE2A_2024_01_03|R1L10_C02_010120_STAGE2A_2024_01_03","calibration_usable_count":3,"new_independent_case_count":3,"counterexample_count":1,"confidence":"medium_low_until_exact_evidence_urls_enriched","proposal_type":"canonical_shadow_only","notes":"Do not promote production profile directly; exact evidence URLs still need enrichment."}
{"row_type":"shadow_weight","axis":"c02_high_mae_stage2_watch_guard","scope":"canonical_archetype_specific","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","baseline_value":0,"tested_value":1,"delta":"+1_guard","reason":"LS ELECTRIC delivered strong 180D MFE but required tolerating -14% MAE; do not relax Green without margin/revision confirmation.","backtest_effect":"Keeps C02 missed structural candidates alive while preventing automatic Green label.","trigger_ids":"R1L10_C02_010120_STAGE2A_2024_01_03","calibration_usable_count":1,"new_independent_case_count":1,"counterexample_count":1,"confidence":"medium","proposal_type":"risk_guard_shadow_only","notes":"High-MAE success row is positive for Stage2 bridge, negative for loose Green."}
{"row_type":"shadow_weight","axis":"full_4b_requires_non_price_evidence","scope":"existing_axis_strengthened","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","baseline_value":true,"tested_value":true,"delta":"0_keep","reason":"LS price-only April heat had local 4B appearance but full-window peak came later; non-price 4B requirement prevented early full 4B.","backtest_effect":"Strengthens watch-only treatment for price-only local peaks.","trigger_ids":"R1L10_C02_010120_4B_WATCH_2024_04_12","calibration_usable_count":1,"new_independent_case_count":0,"counterexample_count":1,"confidence":"medium","proposal_type":"existing_axis_kept","notes":"No new global delta."}
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"10","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":3,"reused_case_count":1,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":1,"new_trigger_family_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late_for_C02_green","high_MAE_success_needs_guard","price_only_local_4B_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R1L10_C02_SOURCE_URL_ENRICHMENT","symbol":"MULTI","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reason":"exact_original_historical_evidence_urls_pending_for_selected_trigger_dates","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration_until_evidence_url_enriched"}
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
- For this MD specifically, enrich exact original historical evidence URLs before any production promotion; current evidence_source fields are medium-confidence summaries.

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
completed_round = R1
completed_loop = 10
next_round = R2
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web / stock-agent source paths checked:

```text
Songdaiki/stock-web atlas/manifest.json
Songdaiki/stock-web diagnostics/chatgpt_bundle.txt
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv
Songdaiki/stock-web atlas/symbol_profiles/267/267260.json
Songdaiki/stock-web atlas/symbol_profiles/298/298040.json
Songdaiki/stock-web atlas/symbol_profiles/010/010120.json
Songdaiki/stock_agent reports/e2r_calibration/ingest_summary.md
Songdaiki/stock_agent data/e2r/calibration/md_registry.jsonl
```

Research caution:

```text
This MD is not an investment recommendation.
This MD is not a live candidate scan.
This MD does not alter production scoring.
All rows are shadow-only until batch implementation validates exact evidence URLs and duplicate status.
```
