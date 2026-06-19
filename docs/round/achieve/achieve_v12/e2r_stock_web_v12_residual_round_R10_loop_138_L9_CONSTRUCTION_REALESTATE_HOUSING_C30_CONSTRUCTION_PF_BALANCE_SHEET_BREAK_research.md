# E2R Stock-Web v12 Residual Research — R10/L9/C30 Construction PF Balance-Sheet Break

```yaml
artifact_type: stock_web_v12_sector_archetype_residual_calibration_md
created_at_kst: 2026-06-16
selected_round: R10
selected_loop: 138
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C30 PF/liquidity and construction-trust hard 4C vs builder-beta decay/reopen split
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE
loop_objective:
  - canonical_archetype_rule_candidate
  - quality_repair_holdout_validation
  - hard_4c_transition_timing_test
  - decay_reopen_after_cleanup_rule
  - source_proxy_quality_repair
  - complete_30_90_180_MFE_MAE
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
```

## 0. Execution guardrails

This file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as the execution prompt. It does not run live discovery, does not patch `stock_agent`, and does not propose production scoring changes. The No-Repeat Index is used only as a duplicate-avoidance and coverage-quality ledger.

Stock-Web basis used here:

```yaml
primary_price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
required_forward_windows: [30D, 90D, 180D]
MFE_definition: max(high from entry_date through N tradable rows) / entry_close - 1
MAE_definition: min(low from entry_date through N tradable rows) / entry_close - 1
```

## 1. Coverage and duplicate-avoidance rationale

The latest No-Repeat Index shows that all C01~C32 scopes are above the minimum row floor. C30 is therefore not selected as a quantity-fill. It is selected as a quality repair loop because construction/PF events are easy to overgeneralize: the same sector label can hide a PF liquidity break, a construction-quality trust break, or an ordinary builder beta that can reopen after cleanup.

```yaml
selected_scope: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
no_repeat_index_snapshot_for_C30:
  representative_rows: 369
  unique_symbols: 51
  positives: 36
  counterexamples: 66
  stage4B: 48
  stage4C: 31
  current_shadow_weights_EPS_Vis_Bott_Mis_Val_Cap_Info: [18, 12, 8, 12, 10, 10, 30]
reason_for_selection:
  - C29 was the immediately preceding run; C30 is the next uncovered late-round construction/real-estate axis in this cluster.
  - C30 has many rows, but the useful work is finer taxonomy: PF-liquidity hard 4C, construction-quality hard 4C, and decay/reopen after cleanup.
  - C30 false positives often begin as backlog/low-PBR/government-support narratives without company-level balance-sheet repair.
```

Loop number rule:

```yaml
existing_standard_C30_root_max_loop_observed: 137
selected_loop_rule: max(existing loop for R10/C30) + 1
selected_loop: 138
```

Important novelty note:

```yaml
hard_duplicate_policy: canonical_archetype_id + symbol + trigger_type + trigger_date + entry_date + evidence_family
this_loop_type: quality_repair_holdout_validation
prior_c30_price_path_reference_used: true
new_symbol_discovery_count: 0
new_rule_language_count: 1
new_taxonomy_split_count: 3
calibration_usable_trigger_count: 8
representative_trigger_candidate_count: 8
aggregate_note: if exact R10_loop_137 rows are already present, batch dedupe should retain one representative price row and use this loop for source-quality / rule-language repair, not as a duplicate quantity expansion.
```

## 2. Non-price evidence stack

C30 should not treat every construction headline as the same animal.

1. **PF/liquidity break** — failed refinancing, PF guarantee stress, debt-workout application, or a broken financing chain. Taeyoung E&C is the clean non-price anchor: the FSC described refinancing difficulty for real-estate PF loans/ABS, many PF development sites, and large financial-sector exposure. That path is a hard 4C rule anchor, although Taeyoung's own price window should be blocked if restructuring/corporate-action contamination overlaps the forward path.
2. **Construction-quality trust break** — fatal/repeated accident, rebuild obligation, regulatory suspension, license/brand impairment, or orderbook trust damage. HDC Hyundai Development and GS E&C show that this is company-specific thesis damage, not merely sector beta.
3. **Ordinary builder beta with balance-sheet bridge** — weak housing/PF sentiment can coexist with cash, cost-rate discipline, order selectivity, and later profit normalization. Hyundai E&C, DL E&C, and Daewoo E&C show that hard 4C should not be immortal after cleanup.

Government liquidity support is not itself Stage2 evidence. It is sector weather. E2R should require company-level bridge: refinancing access, cost-to-complete visibility, balance-sheet repair, profitable backlog, or executed cleanup.

## 3. Price validation scope

The price path table uses Stock-Web `tradable_raw` basis. Every usable trigger row below includes all six required fields:

```text
MFE_30D_pct / MAE_30D_pct / MFE_90D_pct / MAE_90D_pct / MFE_180D_pct / MAE_180D_pct
```

Because the current execution environment could not directly re-download every raw Stock-Web shard, this loop uses the already published R10 loop 137 C30 Stock-Web path table as the price-validated holdout reference and focuses this file on taxonomy compression, source-quality repair, and guardrail wording. The generated rows are marked as `prior_c30_holdout_reference=true` so a later batch deduper can avoid counting exact duplicated price rows twice.

## 4. Trigger path table

| symbol | company | trigger_type | entry_date | entry_price | MFE/MAE 30D | MFE/MAE 90D | MFE/MAE 180D | class | evidence family |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 294870 | HDC Hyundai Development | Stage4C | 2022-01-17 | 18,750 | 5.6 / -28.0 | 5.6 / -29.87 | 5.6 / -45.33 | protection_positive_4c | construction_quality_trust_break_fatal_accident_management_accountability |
| 294870 | HDC Hyundai Development | Stage4C | 2022-03-30 | 15,700 | 11.78 / -11.78 | 11.78 / -33.44 | 11.78 / -37.77 | protection_positive_4c | quality_trust_break_rebuild_license_brand_risk |
| 006360 | GS Engineering & Construction | Stage4C | 2023-05-09 | 21,550 | 2.78 / -4.64 | 2.78 / -37.96 | 2.78 / -41.21 | protection_positive_4c | apartment_collapse_rebuild_cost_trust_break |
| 006360 | GS Engineering & Construction | Stage4B | 2024-02-01 | 15,690 | 3.44 / -6.05 | 6.56 / -10.52 | 38.62 / -10.52 | decay_reopen_watch | cleanup_after_quality_break_but_margin_trust_not_fully_repaired |
| 000720 | Hyundai Engineering & Construction | Stage2-Actionable | 2025-01-23 | 29,700 | 26.43 / -2.53 | 149.16 / -2.53 | 186.53 / -2.53 | positive_reopen | balance_sheet_backlog_order_selectivity_profitability_reopen |
| 375500 | DL E&C | Stage2-Actionable | 2024-10-31 | 30,900 | 12.62 / -5.18 | 51.94 / -5.18 | 93.2 / -5.18 | positive_reopen | cost_base_reset_financial_quality_stage2_reopen |
| 375500 | DL E&C | Stage2-Actionable | 2025-02-06 | 35,150 | 33.57 / -11.66 | 59.89 / -11.66 | 69.84 / -11.66 | positive_but_4b_watch | reopen_after_cleanup_with_front_loaded_price_move |
| 047040 | Daewoo Engineering & Construction | Stage2-Actionable | 2025-02-06 | 3,360 | 11.9 / -4.76 | 43.01 / -12.5 | 43.01 / -12.5 | positive_reopen | ordinary_builder_beta_requires_cost_order_financial_bridge |


## 5. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","symbol":"294870","company":"HDC Hyundai Development","company_kr":"HDC현대산업개발","trigger_type":"Stage4C","trigger_date":"2022-01-17","entry_date":"2022-01-17","entry_price":18750,"MFE_30D_pct":5.6,"MAE_30D_pct":-28.0,"MFE_90D_pct":5.6,"MAE_90D_pct":-29.87,"MFE_180D_pct":5.6,"MAE_180D_pct":-45.33,"case_class":"protection_positive_4c","evidence_family":"construction_quality_trust_break_fatal_accident_management_accountability","evidence_summary":"Fatal/repeated construction-quality trust break and management accountability after the Gwangju apartment collapse; backlog alone was not investable evidence.","source_urls":["https://www.reuters.com/world/asia-pacific/skorea-builder-hdcs-chairman-steps-down-after-apartment-complex-collapse-2022-01-17/"],"calibration_usable":true,"prior_c30_holdout_reference":true,"aggregate_group_role":"quality_repair_holdout_row","round":"R10","loop":138,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","symbol":"294870","company":"HDC Hyundai Development","company_kr":"HDC현대산업개발","trigger_type":"Stage4C","trigger_date":"2022-03-30","entry_date":"2022-03-30","entry_price":15700,"MFE_30D_pct":11.78,"MAE_30D_pct":-11.78,"MFE_90D_pct":11.78,"MAE_90D_pct":-33.44,"MFE_180D_pct":11.78,"MAE_180D_pct":-37.77,"case_class":"protection_positive_4c","evidence_family":"quality_trust_break_rebuild_license_brand_risk","evidence_summary":"The trust break persisted after the first shock; price rebound did not repair the construction-quality thesis.","source_urls":["https://www.reuters.com/world/asia-pacific/skorea-builder-hdcs-chairman-steps-down-after-apartment-complex-collapse-2022-01-17/"],"calibration_usable":true,"prior_c30_holdout_reference":true,"aggregate_group_role":"quality_repair_holdout_row","round":"R10","loop":138,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","symbol":"006360","company":"GS Engineering & Construction","company_kr":"GS건설","trigger_type":"Stage4C","trigger_date":"2023-05-09","entry_date":"2023-05-09","entry_price":21550,"MFE_30D_pct":2.78,"MAE_30D_pct":-4.64,"MFE_90D_pct":2.78,"MAE_90D_pct":-37.96,"MFE_180D_pct":2.78,"MAE_180D_pct":-41.21,"case_class":"protection_positive_4c","evidence_family":"apartment_collapse_rebuild_cost_trust_break","evidence_summary":"Geomdan apartment collapse/rebuild obligation converted a construction quality event into a company-specific trust and cost-to-complete break.","source_urls":["https://en.yna.co.kr/view/AEN20230827002451320"],"calibration_usable":true,"prior_c30_holdout_reference":true,"aggregate_group_role":"quality_repair_holdout_row","round":"R10","loop":138,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","symbol":"006360","company":"GS Engineering & Construction","company_kr":"GS건설","trigger_type":"Stage4B","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":15690,"MFE_30D_pct":3.44,"MAE_30D_pct":-6.05,"MFE_90D_pct":6.56,"MAE_90D_pct":-10.52,"MFE_180D_pct":38.62,"MAE_180D_pct":-10.52,"case_class":"decay_reopen_watch","evidence_family":"cleanup_after_quality_break_but_margin_trust_not_fully_repaired","evidence_summary":"After the first hard 4C, partial normalization can reopen Stage2 watch, but old trust-break scars require 4B overlay until margin/trust repair is visible.","source_urls":["https://en.yna.co.kr/view/AEN20230827002451320"],"calibration_usable":true,"prior_c30_holdout_reference":true,"aggregate_group_role":"quality_repair_holdout_row","round":"R10","loop":138,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","symbol":"000720","company":"Hyundai Engineering & Construction","company_kr":"현대건설","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-23","entry_date":"2025-01-23","entry_price":29700,"MFE_30D_pct":26.43,"MAE_30D_pct":-2.53,"MFE_90D_pct":149.16,"MAE_90D_pct":-2.53,"MFE_180D_pct":186.53,"MAE_180D_pct":-2.53,"case_class":"positive_reopen","evidence_family":"balance_sheet_backlog_order_selectivity_profitability_reopen","evidence_summary":"Strong builder beta becomes actionable only when balance sheet, order selectivity, and profit normalization are visible rather than only low-PBR sentiment.","source_urls":["https://en.hdec.kr/en/invest/finance_01.aspx"],"calibration_usable":true,"prior_c30_holdout_reference":true,"aggregate_group_role":"quality_repair_holdout_row","round":"R10","loop":138,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","symbol":"375500","company":"DL E&C","company_kr":"DL이앤씨","trigger_type":"Stage2-Actionable","trigger_date":"2024-10-31","entry_date":"2024-10-31","entry_price":30900,"MFE_30D_pct":12.62,"MAE_30D_pct":-5.18,"MFE_90D_pct":51.94,"MAE_90D_pct":-5.18,"MFE_180D_pct":93.2,"MAE_180D_pct":-5.18,"case_class":"positive_reopen","evidence_family":"cost_base_reset_financial_quality_stage2_reopen","evidence_summary":"After sector fear, cost-base reset and financial-quality evidence can reopen the builder from 4B watch to Stage2-Actionable.","source_urls":["https://www.dlenc.co.kr/eng/ir/financialPerformance.do"],"calibration_usable":true,"prior_c30_holdout_reference":true,"aggregate_group_role":"quality_repair_holdout_row","round":"R10","loop":138,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","symbol":"375500","company":"DL E&C","company_kr":"DL이앤씨","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-06","entry_date":"2025-02-06","entry_price":35150,"MFE_30D_pct":33.57,"MAE_30D_pct":-11.66,"MFE_90D_pct":59.89,"MAE_90D_pct":-11.66,"MFE_180D_pct":69.84,"MAE_180D_pct":-11.66,"case_class":"positive_but_4b_watch","evidence_family":"reopen_after_cleanup_with_front_loaded_price_move","evidence_summary":"Reopen remains valid, but a fast front-loaded move should carry local 4B/profit-lock overlay even when PF thesis is repaired.","source_urls":["https://www.dlenc.co.kr/eng/ir/financialPerformance.do"],"calibration_usable":true,"prior_c30_holdout_reference":true,"aggregate_group_role":"quality_repair_holdout_row","round":"R10","loop":138,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","symbol":"047040","company":"Daewoo Engineering & Construction","company_kr":"대우건설","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-06","entry_date":"2025-02-06","entry_price":3360,"MFE_30D_pct":11.9,"MAE_30D_pct":-4.76,"MFE_90D_pct":43.01,"MAE_90D_pct":-12.5,"MFE_180D_pct":43.01,"MAE_180D_pct":-12.5,"case_class":"positive_reopen","evidence_family":"ordinary_builder_beta_requires_cost_order_financial_bridge","evidence_summary":"Ordinary builder rerating is usable when backed by cost/order/financial bridge; backlog or low PBR alone should stay capped at Stage2 watch.","source_urls":["https://www.daewooenc.com/eng/ir/financialInfo"],"calibration_usable":true,"prior_c30_holdout_reference":true,"aggregate_group_role":"quality_repair_holdout_row","round":"R10","loop":138,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","required_mfe_mae_complete":true,"production_scoring_changed":false,"shadow_weight_only":true}
```

## 6. Score simulation and raw component breakdown

Component order: `EPS/FCF`, `visibility`, `bottleneck/pricing`, `market_mispricing`, `valuation_rerating`, `capital_allocation`, `information_confidence`.

```jsonl
{"symbol":"294870","trigger_type":"Stage4C","stage_before":"Stage2/Watch false-positive risk","stage_after_shadow":"Stage4C","eps_fcf":4,"visibility":4,"bottleneck_pricing":2,"market_mispricing":5,"valuation_rerating":2,"capital_allocation":0,"information_confidence":34,"raw_total_proxy":51,"decision":"route_to_4C_quality_trust_break"}
{"symbol":"006360","trigger_type":"Stage4C","stage_before":"Stage2 false-positive risk","stage_after_shadow":"Stage4C","eps_fcf":3,"visibility":5,"bottleneck_pricing":2,"market_mispricing":4,"valuation_rerating":1,"capital_allocation":1,"information_confidence":35,"raw_total_proxy":51,"decision":"route_to_4C_rebuild_cost_trust_break"}
{"symbol":"000720","trigger_type":"Stage2-Actionable","stage_before":"Stage2","stage_after_shadow":"Stage2-Actionable","eps_fcf":15,"visibility":13,"bottleneck_pricing":6,"market_mispricing":11,"valuation_rerating":9,"capital_allocation":11,"information_confidence":22,"raw_total_proxy":87,"decision":"allow_reopen_with_bridge"}
{"symbol":"375500","trigger_type":"Stage2-Actionable","stage_before":"Stage2","stage_after_shadow":"Stage2-Actionable + local 4B watch","eps_fcf":14,"visibility":13,"bottleneck_pricing":5,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":11,"information_confidence":24,"raw_total_proxy":85,"decision":"allow_reopen_but_cap_green_until_drawdown_confirmation"}
```

Interpretation:

- C30 hard 4C should not need price confirmation when the non-price evidence is a confirmed PF/liquidity break or construction-quality trust break.
- C30 reopen should not be based on low PBR, backlog, or government support alone.
- Stage2-Actionable can reopen only after balance-sheet quality, cost-rate discipline, profit normalization, order selectivity, or explicit cleanup evidence appears.
- Stage3-Yellow/Green remains capped if the move is front-loaded and the bridge is still only sector beta.

## 7. Residual diagnosis

C30 is a trapdoor archetype. The floorboard looks identical from above: construction, housing, PF, backlog, low valuation. Under the board, however, there are three different mechanisms.

**PF/liquidity break** is the broken water pipe. It can flood the whole house quickly: debt workout, failed refinancing, PF guarantees, self-performed project exposure, and weak lender confidence. These belong to hard 4C unless the price window itself is contaminated and must be narrative-only.

**Construction-quality trust break** is the cracked foundation. Even if the backlog remains, customers, regulators, and counterparties now question whether that backlog can become trusted earnings. HDC and GS E&C show that this deserves hard 4C when fatal/repeated accidents, rebuild obligations, or license/brand impairment are confirmed.

**Ordinary builder beta with cleanup bridge** is different. A builder can look ugly while the sector is cold, but if cash, cost-base reset, order discipline, and profit normalization return, hard 4C should decay and the name can reopen to Stage2-Actionable.

## 8. Proposed shadow rule candidate

```yaml
new_axis_proposed: C30_PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE
canonical_archetype_rule_candidate: C30_PF_LIQUIDITY_TRUST_BREAK_DECAY_REOPEN_GATE
rule_body:
  - If a builder has confirmed PF liquidity stress, debt-workout application, high PF guarantees, failed refinancing, or restructuring evidence, route to Stage4C unless the price window is corporate-action/restructuring contaminated.
  - If a builder has fatal/repeated construction-quality accidents, rebuild obligations, regulatory suspension, license impairment, or brand/orderbook trust break, route to hard 4C even when backlog remains.
  - Government liquidity support, low PBR, large backlog, or generic sector rebound is not Stage2-Actionable evidence by itself.
  - Stage2-Actionable may reopen only after at least two of the following are visible: cost-base reset, profit normalization, cash/refinancing capacity, PF exposure reduction, order selectivity, balance-sheet repair, or trustworthy cost-to-complete visibility.
  - After reopen, keep local 4B watch if the price move is front-loaded or 90D/180D drawdown risk remains high.
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
existing_axis_weakened: null
production_scoring_changed: false
shadow_weight_only: true
```

Suggested shadow weight delta for C30 only:

```yaml
before_EPS_Vis_Bott_Mis_Val_Cap_Info: [18, 12, 8, 12, 10, 10, 30]
after_EPS_Vis_Bott_Mis_Val_Cap_Info:  [16, 14, 7, 10, 8, 12, 33]
delta:                              [-2, +2, -1, -2, -2, +2, +3]
rationale:
  - reduce valuation/low-PBR and generic mispricing credit
  - increase visibility for explicit cleanup/reopen evidence
  - increase capital allocation / balance-sheet quality weight
  - increase information confidence because C30 decisions hinge on verified PF, regulatory, accident, and restructuring evidence
```

## 9. Residual contribution summary

```yaml
loop_contribution_label: C30_pf_liquidity_trust_break_decay_reopen_quality_repair
sector_specific_rule_candidate: L9 construction/real-estate should not promote from backlog, low PBR, or government liquidity support alone; it must separate PF/liquidity hard 4C from ordinary builder-beta reopen.
canonical_archetype_rule_candidate: C30 requires a hard 4C gate for confirmed PF/liquidity or construction-quality trust break and a decay/reopen gate after cleanup evidence.
positive_case_count: 4
counterexample_or_protection_count: 4
stage4b_case_count: 2
stage4c_case_count: 3
current_profile_error_count: 5
source_proxy_only_count: 0
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
```

## 10. Narrative-only blocked anchors

```jsonl
{"row_type":"narrative_only","symbol":"009410","company":"Taeyoung E&C","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"PF workout/restructuring anchor; useful for hard 4C rule language, but price path can be contaminated by restructuring/corporate-action events and should not be aggregate weight input.","evidence_family":"pf_liquidity_debt_workout","source_urls":["https://www.fsc.go.kr/eng/pr010101/81565"],"calibration_usable":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"narrative_only","symbol":"034300","company":"Shinsegae E&C","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"restructuring/delisting-like path anchor; keep as narrative guardrail, not calibration row.","evidence_family":"restructuring_balance_sheet_break","calibration_usable":false,"production_scoring_changed":false,"shadow_weight_only":true}
```

## 11. Batch Ingest Self-Audit

```yaml
required_filename_regex_pass: true
filename_round_matches_metadata_round: true
filename_loop_matches_metadata_loop: true
round_sector_consistency: pass
standard_canonical_archetype_id: true
large_sector_id_valid: true
trigger_type_canonical_labels_only: true
complete_30_90_180_mfe_mae_in_every_trigger_row: true
price_source_stock_web: true
production_scoring_changed: false
shadow_weight_only: true
hard_duplicate_risk_flagged: true
hard_duplicate_risk_note: Exact price paths overlap with prior C30 loop 137 holdout references; use later batch dedupe to avoid quantity double-counting and retain this file for taxonomy/rule-quality repair.
```

## 12. Deferred Coding Agent Handoff Prompt

```text
Deferred Coding Agent Handoff — do not execute during research run.

Read this MD together with existing C30 representative rows. Implement no production change directly from a single MD. If multiple C30 loops agree, add or refine a C30-specific shadow rule:

1. Confirmed PF/liquidity break, debt workout, failed refinancing, high PF guarantees, or restructuring evidence routes to hard 4C unless the price window is corporate-action/restructuring contaminated.
2. Fatal/repeated construction-quality trust break, rebuild obligation, regulatory suspension, license/brand impairment, or orderbook trust damage routes to hard 4C even if backlog remains.
3. Reopen from 4C/4B to Stage2-Actionable requires at least two company-level bridge items: cost-base reset, profit normalization, cash/refinancing capacity, PF exposure reduction, order selectivity, balance-sheet repair, or cost-to-complete visibility.
4. Do not promote from low PBR, backlog, government support, or sector beta alone.
5. Preserve local 4B overlay for front-loaded recoveries with high MAE risk.
```

## 13. Next research state

```yaml
completed_round: R10
completed_loop: 138
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C30 PF/liquidity and construction-trust hard 4C vs builder-beta decay/reopen split
next_recommended_archetypes:
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
