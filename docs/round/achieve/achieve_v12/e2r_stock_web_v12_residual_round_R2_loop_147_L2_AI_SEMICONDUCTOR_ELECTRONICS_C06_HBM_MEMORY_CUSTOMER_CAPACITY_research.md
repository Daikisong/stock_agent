# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| selected_round | `R2` |
| selected_loop | `147` |
| selection_basis | `docs/core/V12_Research_No_Repeat_Index.md` |
| selected_priority_bucket | `Priority 0` |
| round_schedule_status | `coverage_index_selected_not_sequential` |
| round_sector_consistency | `pass` |
| large_sector_id | `L2_AI_SEMICONDUCTOR_ELECTRONICS` |
| canonical_archetype_id | `C06_HBM_MEMORY_CUSTOMER_CAPACITY` |
| fine_archetype_id | `mixed_c06_hbm_named_customer_booked_capacity_vs_ai_substrate_boundary_leaf_set` |
| loop_objective | `coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery` |
| price_source | `Songdaiki/stock-web` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| stock_web_manifest_max_date | `2026-02-20` |


This loop adds 7 new independent cases, 5 counterexamples, and 5 residual errors for L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

## 1. Current Calibrated Profile Assumption

- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated_proxy`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- code_patch_written: `false`

The current profile already blocks generic price-only blowoff and requires non-price evidence for full 4B. This loop does not re-prove that global rule. It stress-tests a narrower C06 boundary: whether HBM customer/CAPA language should absorb generic AI substrate, FC-BGA, and MLB beneficiaries.

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R2`
- large_sector_id: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical_archetype_id: `C06_HBM_MEMORY_CUSTOMER_CAPACITY`
- scope consistency: `pass`

C06 is defined here as HBM memory customer qualification, named customer shipment, booked/sold-out HBM capacity, HBM mix/ASP/revision bridge, or direct memory-supplier capacity evidence. It is not a generic bucket for every AI component or substrate company.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index baseline: C06 has 17 representative rows and remains Priority 0. In this session, C06 was already extended by loop129 and loop139, but session-aware coverage was still roughly 28 rows. This loop therefore uses C06 again but avoids the prior trigger set:

- prior C06 loop129: SK hynix 2024-01/04/07; Samsung Electronics 2024-05/07.
- prior C06 loop139: SK hynix 2023-10, 2024-10, 2025-01; Samsung Electronics 2023-10, 2024-10, 2025-01.
- this loop: SK hynix 2024-03 HBM3E production, SK hynix 2024-09 12-layer production, Samsung 2024-02 product sampling, Samsung 2024-08 partial qualification/no-deal, Samsung Electro-Mechanics AI FC-BGA boundary, Daeduck FC-BGA boundary, Isu Petasys AI MLB boundary.

Hard duplicate status: `none`. Reused symbols are used only with new trigger family / new cycle phase and are assigned independent_evidence_weight 0.5 where applicable.

## 4. Stock-Web OHLC Input / Price Source Validation

- primary_price_source: `Songdaiki/stock-web`
- manifest_path: `atlas/manifest.json`
- schema_path: `atlas/schema.json`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- raw_shard_root: `atlas/ohlcv_raw_by_symbol_year`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- stock_web_manifest_max_date: `2026-02-20`
- entry rule used: event timing unknown or after-market-safe assumption → next stock-web tradable date close.

## 5. Historical Eligibility Gate

All representative trigger rows pass:

- trigger_date is historical.
- entry_date exists in stock-web tradable shard.
- at least 180 forward trading rows are available.
- MFE_30D_pct / MFE_90D_pct / MFE_180D_pct and MAE_30D_pct / MAE_90D_pct / MAE_180D_pct are complete.
- corporate-action-contaminated 180D window: `false` for all rows.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | compressed canonical | interpretation |
|---|---|---|
| HBM3E_NVIDIA_NAMED_CUSTOMER_BOOKED_CAPACITY | C06 | Direct named-customer HBM memory shipment/capacity evidence |
| HBM3E_12_LAYER_CUSTOMER_SUPPLY_CAPACITY | C06 | Direct HBM memory capacity/product supply milestone |
| HBM3E_12H_PRODUCT_SAMPLING_WITHOUT_NAMED_CUSTOMER_QUALIFICATION | C06 boundary | Product development/sampling alone is not actionable C06 |
| HBM3E_PARTIAL_QUALIFICATION_NO_SUPPLY_DEAL | C06 boundary | Partial qualification without signed supply deal is not enough |
| AI_SERVER_FCBGA_BOUNDARY_NOT_HBM_MEMORY_CUSTOMER_CAPACITY | C06 boundary | AI substrate is related but lacks HBM memory customer/CAPA bridge |
| DATACENTER_COWOS_FCBGA_BOUNDARY_LOCAL_4B | C06 boundary / 4B | CoWoS/FC-BGA vocabulary must not be compressed into HBM memory capacity automatically |
| AI_ACCELERATOR_MLB_BOUNDARY_NOT_HBM_MEMORY_CAPACITY | C06 boundary / 4B | AI accelerator PCB customer names are not HBM memory capacity evidence |

## 7. Case Selection Summary

| case_id | symbol | name | trigger_date | trigger_type | role | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| C06_L147_000660_20240319_HBM3E_NVIDIA_SHIPMENT | 000660 | SK하이닉스 | 2024-03-19 | Stage2-Actionable | positive / structural_success | 2024-03-20 | 156500 | 22.3 | -1.53 | 58.79 | -1.53 | 58.79 | -7.54 | current_profile_correct |
| C06_L147_000660_20240926_12LAYER_HBM3E | 000660 | SK하이닉스 | 2024-09-26 | Stage2-Actionable | positive / structural_success | 2024-09-27 | 183800 | 12.08 | -8.0 | 23.5 | -14.25 | 62.4 | -14.25 | current_profile_correct |
| C06_L147_005930_20240227_12H_HBM3E_SAMPLING | 005930 | 삼성전자 | 2024-02-27 | Stage2 | counterexample / failed_rerating | 2024-02-28 | 73200 | 17.49 | -2.05 | 21.04 | -2.05 | 21.31 | -31.83 | current_profile_false_positive |
| C06_L147_005930_20240807_PARTIAL_HBM3E_QUALIFICATION_REPORT | 005930 | 삼성전자 | 2024-08-07 | Stage2 | counterexample / failed_rerating | 2024-08-08 | 73400 | 9.26 | -15.26 | 9.26 | -32.02 | 9.26 | -32.02 | current_profile_false_positive |
| C06_L147_009150_20240826_AI_FCBGA_BOUNDARY | 009150 | 삼성전기 | 2024-08-26 | Stage2 | counterexample / false_positive_green | 2024-08-27 | 143900 | 1.39 | -12.44 | 1.39 | -26.69 | 4.1 | -26.69 | current_profile_false_positive |
| C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B | 353200 | 대덕전자 | 2024-06-26 | Stage4B | counterexample / 4B_too_early | 2024-06-27 | 21150 | 18.91 | -17.26 | 18.91 | -26.48 | 18.91 | -39.15 | current_profile_false_positive |
| C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B | 007660 | 이수페타시스 | 2024-06-18 | Stage4B | counterexample / 4B_overlay_success | 2024-06-19 | 54600 | 9.34 | -24.45 | 9.34 | -43.41 | 9.34 | -61.54 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

- positive_case_count: 2
- counterexample_count: 5
- 4B_watch_or_overlay_count: 6
- 4C_case_count: 0
- current_profile_error_count: 5

The positive side is deliberately narrow: direct SK hynix HBM3E production, named Nvidia/customer supply, and capacity booking. The counterexample side draws a fence around the moat: product sampling, partial qualification without a deal, generic AI FC-BGA, data-center CoWoS substrate, and AI-accelerator MLB should not be promoted as C06 unless they carry a memory customer qualification or booked HBM capacity bridge.

## 9. Evidence Source Map

| symbol | trigger_date | evidence source | evidence summary |
|---:|---|---|---|
| 000660 | 2024-03-19 | https://www.reuters.com/technology/nvidia-supplier-sk-hynix-begins-mass-production-next-generation-memory-chip-2024-03-19/ | HBM3E mass production began and first shipments were directed to Nvidia; 2024 HBM capacity was effectively booked. |
| 000660 | 2024-09-26 | https://en.yna.co.kr/view/AEN20240926002700320 | World-first 12-layer HBM3E mass production and customer supply plan including Nvidia within the year. |
| 005930 | 2024-02-27 | https://news.samsungsemiconductor.com/global/samsung-develops-industry-first-36gb-hbm3e-12h-dram/ | Industry-first 36GB 12-stack HBM3E development and sampling narrative, but no named Nvidia qualification or booked capacity bridge at trigger date. |
| 005930 | 2024-08-07 | https://www.reuters.com/technology/artificial-intelligence/samsungs-8-layer-hbm3e-chips-clear-nvidias-tests-use-sources-say-2024-08-06/ | Reuters reported 8-layer HBM3E cleared Nvidia tests but also noted no supply deal yet; 12-layer qualification remained a separate issue. |
| 009150 | 2024-08-26 | https://m.samsungsem.com/global/newsroom/news/view.do?id=8382 | High-performance FC-BGA roadmap for servers, AI, automotive, and networks; not a named HBM memory customer/capacity contract. |
| 353200 | 2024-06-26 | https://iconnect007.com/article/141298/daeduck-electronics-developed-large-body-fcbga-substrate-for-data-centers/141295/pcb | Large-body FC-BGA substrate for data-center/HPC/CoWoS packaging; C06 should not treat this as HBM memory maker customer-capacity unless memory customer bridge exists. |
| 007660 | 2024-06-18 | https://view.asiae.co.kr/en/article/2024061809204023846 | AI/cloud MLB beneficiary narrative with Nvidia, Google, and Microsoft customer exposure; important AI substrate path but not HBM memory customer/CAPA evidence. |


## 10. Price Data Source Map

| symbol | entry_date | shard | profile | corporate_action_window_status |
|---:|---|---|---|---|
| 000660 | 2024-03-20 | `atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv` | `atlas/symbol_profiles/000/000660.json` | clean_180D_window |
| 000660 | 2024-09-27 | `atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv` | `atlas/symbol_profiles/000/000660.json` | clean_180D_window |
| 005930 | 2024-02-28 | `atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv` | `atlas/symbol_profiles/005/005930.json` | clean_180D_window |
| 005930 | 2024-08-08 | `atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv` | `atlas/symbol_profiles/005/005930.json` | clean_180D_window |
| 009150 | 2024-08-27 | `atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv` | `atlas/symbol_profiles/009/009150.json` | clean_180D_window |
| 353200 | 2024-06-27 | `atlas/ohlcv_tradable_by_symbol_year/353/353200/2024.csv` | `atlas/symbol_profiles/353/353200.json` | clean_180D_window |
| 007660 | 2024-06-19 | `atlas/ohlcv_tradable_by_symbol_year/007/007660/2024.csv` | `atlas/symbol_profiles/007/007660.json` | clean_180D_window |


## 11. Case-by-Case Trigger Grid

1. **SK hynix 2024-03-19**: the C06 engine is firing on all cylinders. Named Nvidia shipment and booked HBM capacity make Stage2-Actionable justified. 90D path confirms it with MFE_90D_pct 58.79 and MAE_90D_pct -1.53.
2. **SK hynix 2024-09-26**: 12-layer HBM3E mass production is still valid C06, but below-entry closes inside 30/90D mean staged-entry or MAE guard is useful.
3. **Samsung Electronics 2024-02-27**: product leadership and sampling created near-term MFE, but the 180D drawdown shows why product sampling must not equal customer-qualified capacity.
4. **Samsung Electronics 2024-08-07**: partial qualification report without signed supply deal failed the price path; C06 needs a contract/customer bridge, not a rumor-shaped bridge.
5. **Samsung Electro-Mechanics 2024-08-26**: AI FC-BGA is structurally related to AI servers, but not HBM memory-maker customer capacity. Current profile can over-promote this if C06 scope is too wide.
6. **Daeduck Electronics 2024-06-26**: data-center/CoWoS FC-BGA product evidence had local MFE but collapsed into MAE_180D_pct -39.15; treat as boundary 4B/high-MAE guard.
7. **Isu Petasys 2024-06-18**: Nvidia/Google/Microsoft customer vocabulary in AI MLB is powerful, but if compressed into C06 HBM memory capacity, it becomes a severe high-MAE false positive.

## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | name | trigger_date | trigger_type | role | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| C06_L147_000660_20240319_HBM3E_NVIDIA_SHIPMENT | 000660 | SK하이닉스 | 2024-03-19 | Stage2-Actionable | positive / structural_success | 2024-03-20 | 156500 | 22.3 | -1.53 | 58.79 | -1.53 | 58.79 | -7.54 | current_profile_correct |
| C06_L147_000660_20240926_12LAYER_HBM3E | 000660 | SK하이닉스 | 2024-09-26 | Stage2-Actionable | positive / structural_success | 2024-09-27 | 183800 | 12.08 | -8.0 | 23.5 | -14.25 | 62.4 | -14.25 | current_profile_correct |
| C06_L147_005930_20240227_12H_HBM3E_SAMPLING | 005930 | 삼성전자 | 2024-02-27 | Stage2 | counterexample / failed_rerating | 2024-02-28 | 73200 | 17.49 | -2.05 | 21.04 | -2.05 | 21.31 | -31.83 | current_profile_false_positive |
| C06_L147_005930_20240807_PARTIAL_HBM3E_QUALIFICATION_REPORT | 005930 | 삼성전자 | 2024-08-07 | Stage2 | counterexample / failed_rerating | 2024-08-08 | 73400 | 9.26 | -15.26 | 9.26 | -32.02 | 9.26 | -32.02 | current_profile_false_positive |
| C06_L147_009150_20240826_AI_FCBGA_BOUNDARY | 009150 | 삼성전기 | 2024-08-26 | Stage2 | counterexample / false_positive_green | 2024-08-27 | 143900 | 1.39 | -12.44 | 1.39 | -26.69 | 4.1 | -26.69 | current_profile_false_positive |
| C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B | 353200 | 대덕전자 | 2024-06-26 | Stage4B | counterexample / 4B_too_early | 2024-06-27 | 21150 | 18.91 | -17.26 | 18.91 | -26.48 | 18.91 | -39.15 | current_profile_false_positive |
| C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B | 007660 | 이수페타시스 | 2024-06-18 | Stage4B | counterexample / 4B_overlay_success | 2024-06-19 | 54600 | 9.34 | -24.45 | 9.34 | -43.41 | 9.34 | -61.54 | current_profile_false_positive |


MFE/MAE formula used:

```text
MFE_N_pct = (max high from entry_date through N trading rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading rows / entry_price - 1) * 100
entry_price = entry_date close from stock-web tradable shard
```

## 13. Current Calibrated Profile Stress Test

| case_id | likely P0 behavior | actual path | verdict |
|---|---|---|---|
| C06_L147_000660_20240319_HBM3E_NVIDIA_SHIPMENT | Stage2-Actionable / possible Yellow | strong 90D MFE, shallow MAE | current_profile_correct |
| C06_L147_000660_20240926_12LAYER_HBM3E | Stage2-Actionable | strong 180D MFE but with early MAE | current_profile_correct with staged-entry guard |
| C06_L147_005930_20240227_12H_HBM3E_SAMPLING | Stage2-Actionable if product-development vocabulary is over-weighted | initial MFE but 180D drawdown | current_profile_false_positive |
| C06_L147_005930_20240807_PARTIAL_HBM3E_QUALIFICATION_REPORT | Stage2-Actionable if qualification headline is accepted without supply deal | low MFE, high MAE | current_profile_false_positive |
| C06_L147_009150_20240826_AI_FCBGA_BOUNDARY | Stage2 if AI substrate is compressed into C06 | low MFE, material MAE | current_profile_false_positive |
| C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B | Stage2/Watch if CoWoS/AI package substrate leaks into C06 | local MFE, high MAE | current_profile_false_positive |
| C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B | Stage2-Actionable if customer vocabulary is over-weighted | severe 90D/180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is created in this MD. That is intentional. C06 should let direct named-customer HBM memory capacity enter Stage2-Actionable early, while reserving Yellow/Green for confirmed mix, ASP, revision, and customer shipment conversion. Product sampling and partial qualification should remain Stage2-Watch until a supply deal or durable customer qualification is observed.

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence type | local peak proximity | full-window proximity | timing verdict |
|---|---|---:|---:|---|
| C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B | price_only_local_peak, positioning_overheat, valuation_blowoff | 1.00 | 1.00 | local_4b_boundary_guard_high_mae |
| C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B | positioning_overheat, price_only_local_peak, valuation_blowoff | 1.00 | 1.00 | local_4b_boundary_guard_high_mae |

These are not full thesis-break 4C rows. They are boundary/overheat rows showing that a C06 classifier should not let adjacent AI substrate vocabulary pretend to be HBM memory customer capacity.

## 16. 4C Protection Audit

No hard Stage4C trigger is proposed. Samsung's Feb/Aug cases are qualification-gap watches rather than confirmed permanent thesis breaks. The correct protection is to block Actionable/Green until named customer qualification and supply economics are confirmed, not to force an immediate 4C on every delay headline.

## 17. Sector-Specific Rule Candidate

`L2_HBM_CUSTOMER_QUALIFICATION_BOUNDARY_GATE_V3`

For L2 AI/semiconductor electronics, separate three layers:

1. **Core C06**: named HBM customer, booked/sold-out HBM capacity, HBM mix/ASP/revision, shipment to AI accelerator customer.
2. **Watch C06**: product development, sampling, partial qualification, no supply deal, no revenue conversion.
3. **Boundary non-C06 / 4B watch**: generic AI server FC-BGA, CoWoS substrate, MLB, PCB, memory substrate recovery unless tied to HBM memory-maker qualification/capacity.

## 18. Canonical-Archetype Rule Candidate

`C06_NAMED_CUSTOMER_BOOKED_CAPACITY_AND_AI_SUBSTRATE_BOUNDARY_GATE_V3`

Shadow rule:

```text
if canonical_archetype_id == C06:
    require one of:
      - named HBM customer qualification or shipment
      - booked/sold-out HBM capacity
      - HBM mix/ASP/revision bridge in reported results
      - explicit supply deal or customer delivery timing
    if only product sampling / partial qualification / generic AI substrate / FC-BGA / MLB:
      cap at Stage2-Watch or route to boundary 4B/high-MAE guard
```

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | eligible trigger count | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | Treats broad HBM/AI capacity vocabulary as potentially actionable once Stage2 bonus applies | 7 | 20.32 | -20.92 | 26.3 | -30.43 | 0.71 | too many C06 boundary false positives |
| P0b e2r_2_0_baseline_reference | Slower and less bridge-sensitive baseline | 7 | 20.32 | -20.92 | 26.3 | -30.43 | 0.71 | misses early SK Hynix HBM3E but still lets narrative rows leak |
| P1 sector_specific_candidate_profile | Require semiconductor AI evidence plus delivery/customer/margin bridge | 4 | 23.22 | -18.61 | 27.19 | -21.18 | 0.50 | better but still not enough for generic substrate boundary |
| P2 canonical_archetype_candidate_profile | Require named HBM customer qualification or booked/sold-out HBM memory capacity; boundary AI substrate rows fail | 2 | 41.14 | -7.89 | 60.6 | -10.9 | 0.00 | best score-return alignment |
| P3 counterexample_guard_profile | Add high-MAE guard for sampling-only, no-supply-deal, and generic AI substrate vocabulary | 7 | 20.32 | -20.92 | 26.3 | -30.43 | 0.14 | keeps SK Hynix positives, blocks most boundary false positives |


## 20. Score-Return Alignment Matrix

| bucket | cases | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | interpretation |
|---|---:|---:|---:|---:|---:|---|
| Core C06 named-customer positives | 2 | 41.14 | -7.89 | 60.6 | -10.9 | strong alignment |
| Boundary / qualification-gap counterexamples | 5 | 11.99 | -26.13 | 12.58 | -38.25 | false-positive guard needed |
| All rows | 7 | 20.32 | -20.92 | 26.3 | -30.43 | mixed until boundary guard is applied |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | mixed_c06_hbm_named_customer_booked_capacity_vs_ai_substrate_boundary_leaf_set | 2 | 5 | 6 | 0 | 7 | 0 | 7 | 7 | 5 | L2_HBM_CUSTOMER_QUALIFICATION_BOUNDARY_GATE_V3 | C06_NAMED_CUSTOMER_BOOKED_CAPACITY_AND_AI_SUBSTRATE_BOUNDARY_GATE_V3 | index baseline 17→24; session-aware after loop129+139+147 ≈ 35 |


## 22. Residual Contribution Summary

new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
residual_error_types_found: product_sampling_without_named_customer|partial_qualification_without_supply_deal|generic_ai_substrate_boundary_false_positive|high_mae_after_ai_component_theme
new_axis_proposed: c06_named_customer_booked_capacity_and_ai_substrate_boundary_gate_v3
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus|stage3_green_thresholds
sector_specific_rule_candidate: L2_HBM_CUSTOMER_QUALIFICATION_BOUNDARY_GATE_V3
canonical_archetype_rule_candidate: C06_NAMED_CUSTOMER_BOOKED_CAPACITY_AND_AI_SUBSTRATE_BOUNDARY_GATE_V3
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- stock-web OHLC path only.
- 30D/90D/180D MFE/MAE based on tradable_raw close entry.
- historical trigger evidence available at or near trigger date.
- C06 taxonomy boundary between direct HBM memory capacity and adjacent AI substrate beneficiaries.

Non-validation scope:

- no live watchlist.
- no current valuation target.
- no production scoring change.
- no brokerage/API action.
- no claim that boundary stocks are bad businesses; only that they should not be scored as direct C06 HBM memory customer capacity without bridge evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,customer_quality_named_hbm_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Require named HBM customer qualification/shipment or booked HBM capacity before Stage2-Actionable", "Selects SK hynix positives and blocks Samsung sampling/partial qual plus substrate boundary false positives", "C06_L147_000660_20240319_HBM3E_NVIDIA_SHIPMENT_Stage2-Actionable|C06_L147_000660_20240926_12LAYER_HBM3E_Stage2-Actionable",7,7,5,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,ai_substrate_boundary_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Do not compress FC-BGA/CoWoS/MLB/PCB into C06 unless HBM memory customer capacity bridge exists", "Reduces high-MAE boundary false positives in 009150/353200/007660", "C06_L147_009150_20240826_AI_FCBGA_BOUNDARY_Stage2|C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B_Stage4B|C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B_Stage4B",7,7,5,medium,canonical_shadow_only,"not production; boundary guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C06_L147_000660_20240319_HBM3E_NVIDIA_SHIPMENT","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_NVIDIA_NAMED_CUSTOMER_BOOKED_CAPACITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same core memory symbol as prior C06 loops but new trigger family: HBM3E mass production and named Nvidia shipment, not quarterly result or qualification headline","independent_evidence_weight":0.5,"score_price_alignment":"hbm3e_mass_production_nvidia_shipment_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HBM3E mass production began and first shipments were directed to Nvidia; 2024 HBM capacity was effectively booked."}
{"row_type":"trigger","trigger_id":"C06_L147_000660_20240319_HBM3E_NVIDIA_SHIPMENT_Stage2-Actionable","case_id":"C06_L147_000660_20240319_HBM3E_NVIDIA_SHIPMENT","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_NVIDIA_NAMED_CUSTOMER_BOOKED_CAPACITY","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-19","evidence_available_at_that_date":"HBM3E mass production began and first shipments were directed to Nvidia; 2024 HBM capacity was effectively booked.","evidence_source":"https://www.reuters.com/technology/nvidia-supplier-sk-hynix-begins-mass-production-next-generation-memory-chip-2024-03-19/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["durable_customer_confirmation","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-20","entry_price":156500.0,"MFE_30D_pct":22.3,"MFE_90D_pct":58.79,"MFE_180D_pct":58.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.53,"MAE_90D_pct":-1.53,"MAE_180D_pct":-7.54,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-11","peak_price":248500.0,"drawdown_after_peak_pct":-41.77,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_confirmed_stage3_green_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm3e_mass_production_nvidia_shipment_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage2-Actionable|2024-03-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same core memory symbol as prior C06 loops but new trigger family: HBM3E mass production and named Nvidia shipment, not quarterly result or qualification headline","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C06_CUSTOMER_BOOKED_CAPACITY_AND_BOUNDARY_GUARD_V3","case_id":"C06_L147_000660_20240319_HBM3E_NVIDIA_SHIPMENT","trigger_id":"C06_L147_000660_20240319_HBM3E_NVIDIA_SHIPMENT_Stage2-Actionable","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":5,"revision_score":7,"relative_strength_score":7,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":9,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":7,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score","contract_score"],"component_delta_explanation":"Promote only named-customer/booked-capacity HBM memory rows; demote product sampling, partial qualification, and generic AI substrate boundary rows.","MFE_90D_pct":58.79,"MAE_90D_pct":-1.53,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C06_L147_000660_20240926_12LAYER_HBM3E","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_12_LAYER_CUSTOMER_SUPPLY_CAPACITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same core memory symbol as prior C06 loops but new trigger family: 12-layer HBM3E capacity/customer supply milestone","independent_evidence_weight":0.5,"score_price_alignment":"twelve_layer_hbm3e_customer_supply_positive_with_staged_entry_guard","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"World-first 12-layer HBM3E mass production and customer supply plan including Nvidia within the year."}
{"row_type":"trigger","trigger_id":"C06_L147_000660_20240926_12LAYER_HBM3E_Stage2-Actionable","case_id":"C06_L147_000660_20240926_12LAYER_HBM3E","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_12_LAYER_CUSTOMER_SUPPLY_CAPACITY","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-26","evidence_available_at_that_date":"World-first 12-layer HBM3E mass production and customer supply plan including Nvidia within the year.","evidence_source":"https://en.yna.co.kr/view/AEN20240926002700320","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":["durable_customer_confirmation","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-27","entry_price":183800.0,"MFE_30D_pct":12.08,"MFE_90D_pct":23.5,"MFE_180D_pct":62.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.0,"MAE_90D_pct":-14.25,"MAE_180D_pct":-14.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-26","peak_price":298500.0,"drawdown_after_peak_pct":-5.86,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_confirmed_stage3_green_trigger","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"twelve_layer_hbm3e_customer_supply_positive_with_staged_entry_guard","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage2-Actionable|2024-09-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same core memory symbol as prior C06 loops but new trigger family: 12-layer HBM3E capacity/customer supply milestone","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C06_CUSTOMER_BOOKED_CAPACITY_AND_BOUNDARY_GUARD_V3","case_id":"C06_L147_000660_20240926_12LAYER_HBM3E","trigger_id":"C06_L147_000660_20240926_12LAYER_HBM3E_Stage2-Actionable","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":5,"revision_score":7,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":9,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":8,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score","contract_score"],"component_delta_explanation":"Promote only named-customer/booked-capacity HBM memory rows; demote product sampling, partial qualification, and generic AI substrate boundary rows.","MFE_90D_pct":23.5,"MAE_90D_pct":-14.25,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C06_L147_005930_20240227_12H_HBM3E_SAMPLING","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_12H_PRODUCT_SAMPLING_WITHOUT_NAMED_CUSTOMER_QUALIFICATION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same core memory symbol as prior C06 loops but new trigger family: product-development/sampling before customer qualification","independent_evidence_weight":0.5,"score_price_alignment":"product_development_sampling_not_enough_for_actionable_c06","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Industry-first 36GB 12-stack HBM3E development and sampling narrative, but no named Nvidia qualification or booked capacity bridge at trigger date."}
{"row_type":"trigger","trigger_id":"C06_L147_005930_20240227_12H_HBM3E_SAMPLING_Stage2","case_id":"C06_L147_005930_20240227_12H_HBM3E_SAMPLING","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_12H_PRODUCT_SAMPLING_WITHOUT_NAMED_CUSTOMER_QUALIFICATION","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-02-27","evidence_available_at_that_date":"Industry-first 36GB 12-stack HBM3E development and sampling narrative, but no named Nvidia qualification or booked capacity bridge at trigger date.","evidence_source":"https://news.samsungsemiconductor.com/global/samsung-develops-industry-first-36gb-hbm3e-12h-dram/","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["qualification_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-28","entry_price":73200.0,"MFE_30D_pct":17.49,"MFE_90D_pct":21.04,"MFE_180D_pct":21.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.05,"MAE_90D_pct":-2.05,"MAE_180D_pct":-31.83,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":88800.0,"drawdown_after_peak_pct":-43.81,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_confirmed_stage3_green_trigger","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"false_break_or_watch_only","trigger_outcome_label":"product_development_sampling_not_enough_for_actionable_c06","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage2|2024-02-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same core memory symbol as prior C06 loops but new trigger family: product-development/sampling before customer qualification","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C06_CUSTOMER_BOOKED_CAPACITY_AND_BOUNDARY_GUARD_V3","case_id":"C06_L147_005930_20240227_12H_HBM3E_SAMPLING","trigger_id":"C06_L147_005930_20240227_12H_HBM3E_SAMPLING_Stage2","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":3,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score","contract_score"],"component_delta_explanation":"Promote only named-customer/booked-capacity HBM memory rows; demote product sampling, partial qualification, and generic AI substrate boundary rows.","MFE_90D_pct":21.04,"MAE_90D_pct":-2.05,"score_return_alignment_label":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C06_L147_005930_20240807_PARTIAL_HBM3E_QUALIFICATION_REPORT","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_PARTIAL_QUALIFICATION_NO_SUPPLY_DEAL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same core memory symbol as prior C06 loops but new trigger date/family: partial qualification report with no signed supply deal","independent_evidence_weight":0.5,"score_price_alignment":"reported_partial_qualification_without_signed_supply_deal_failed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Reuters reported 8-layer HBM3E cleared Nvidia tests but also noted no supply deal yet; 12-layer qualification remained a separate issue."}
{"row_type":"trigger","trigger_id":"C06_L147_005930_20240807_PARTIAL_HBM3E_QUALIFICATION_REPORT_Stage2","case_id":"C06_L147_005930_20240807_PARTIAL_HBM3E_QUALIFICATION_REPORT","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM3E_PARTIAL_QUALIFICATION_NO_SUPPLY_DEAL","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-08-07","evidence_available_at_that_date":"Reuters reported 8-layer HBM3E cleared Nvidia tests but also noted no supply deal yet; 12-layer qualification remained a separate issue.","evidence_source":"https://www.reuters.com/technology/artificial-intelligence/samsungs-8-layer-hbm3e-chips-clear-nvidias-tests-use-sources-say-2024-08-06/","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","contract_delay"],"stage4c_evidence_fields":["qualification_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-08","entry_price":73400.0,"MFE_30D_pct":9.26,"MFE_90D_pct":9.26,"MFE_180D_pct":9.26,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.26,"MAE_90D_pct":-32.02,"MAE_180D_pct":-32.02,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-16","peak_price":80200.0,"drawdown_after_peak_pct":-37.78,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_confirmed_stage3_green_trigger","four_b_evidence_type":["positioning_overheat","contract_delay"],"four_c_protection_label":"false_break_or_watch_only","trigger_outcome_label":"reported_partial_qualification_without_signed_supply_deal_failed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage2|2024-08-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same core memory symbol as prior C06 loops but new trigger date/family: partial qualification report with no signed supply deal","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C06_CUSTOMER_BOOKED_CAPACITY_AND_BOUNDARY_GUARD_V3","case_id":"C06_L147_005930_20240807_PARTIAL_HBM3E_QUALIFICATION_REPORT","trigger_id":"C06_L147_005930_20240807_PARTIAL_HBM3E_QUALIFICATION_REPORT_Stage2","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"Stage2","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score","contract_score"],"component_delta_explanation":"Promote only named-customer/booked-capacity HBM memory rows; demote product sampling, partial qualification, and generic AI substrate boundary rows.","MFE_90D_pct":9.26,"MAE_90D_pct":-32.02,"score_return_alignment_label":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C06_L147_009150_20240826_AI_FCBGA_BOUNDARY","symbol":"009150","company_name":"삼성전기","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_SERVER_FCBGA_BOUNDARY_NOT_HBM_MEMORY_CUSTOMER_CAPACITY","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ai_fc_bga_market_growth_not_hbm_customer_capacity","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"High-performance FC-BGA roadmap for servers, AI, automotive, and networks; not a named HBM memory customer/capacity contract."}
{"row_type":"trigger","trigger_id":"C06_L147_009150_20240826_AI_FCBGA_BOUNDARY_Stage2","case_id":"C06_L147_009150_20240826_AI_FCBGA_BOUNDARY","symbol":"009150","company_name":"삼성전기","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_SERVER_FCBGA_BOUNDARY_NOT_HBM_MEMORY_CUSTOMER_CAPACITY","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-08-26","evidence_available_at_that_date":"High-performance FC-BGA roadmap for servers, AI, automotive, and networks; not a named HBM memory customer/capacity contract.","evidence_source":"https://m.samsungsem.com/global/newsroom/news/view.do?id=8382","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv","profile_path":"atlas/symbol_profiles/009/009150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-27","entry_price":143900.0,"MFE_30D_pct":1.39,"MFE_90D_pct":1.39,"MFE_180D_pct":4.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.44,"MAE_90D_pct":-26.69,"MAE_180D_pct":-26.69,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-17","peak_price":149800.0,"drawdown_after_peak_pct":-27.37,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_no_confirmed_stage3_green_trigger","four_b_evidence_type":["positioning_overheat","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ai_fc_bga_market_growth_not_hbm_customer_capacity","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|009150|Stage2|2024-08-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C06_CUSTOMER_BOOKED_CAPACITY_AND_BOUNDARY_GUARD_V3","case_id":"C06_L147_009150_20240826_AI_FCBGA_BOUNDARY","trigger_id":"C06_L147_009150_20240826_AI_FCBGA_BOUNDARY_Stage2","symbol":"009150","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage1","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score","contract_score"],"component_delta_explanation":"Promote only named-customer/booked-capacity HBM memory rows; demote product sampling, partial qualification, and generic AI substrate boundary rows.","MFE_90D_pct":1.39,"MAE_90D_pct":-26.69,"score_return_alignment_label":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B","symbol":"353200","company_name":"대덕전자","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"DATACENTER_COWOS_FCBGA_BOUNDARY_LOCAL_4B","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"datacenter_fc_bga_cowos_boundary_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Large-body FC-BGA substrate for data-center/HPC/CoWoS packaging; C06 should not treat this as HBM memory maker customer-capacity unless memory customer bridge exists."}
{"row_type":"trigger","trigger_id":"C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B_Stage4B","case_id":"C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B","symbol":"353200","company_name":"대덕전자","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"DATACENTER_COWOS_FCBGA_BOUNDARY_LOCAL_4B","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-06-26","evidence_available_at_that_date":"Large-body FC-BGA substrate for data-center/HPC/CoWoS packaging; C06 should not treat this as HBM memory maker customer-capacity unless memory customer bridge exists.","evidence_source":"https://iconnect007.com/article/141298/daeduck-electronics-developed-large-body-fcbga-substrate-for-data-centers/141295/pcb","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/353/353200/2024.csv","profile_path":"atlas/symbol_profiles/353/353200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-27","entry_price":21150.0,"MFE_30D_pct":18.91,"MFE_90D_pct":18.91,"MFE_180D_pct":18.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.26,"MAE_90D_pct":-26.48,"MAE_180D_pct":-39.15,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":25150.0,"drawdown_after_peak_pct":-48.83,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4b_boundary_guard_high_mae","four_b_evidence_type":["price_only_local_peak","positioning_overheat","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"datacenter_fc_bga_cowos_boundary_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|353200|Stage4B|2024-06-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C06_CUSTOMER_BOOKED_CAPACITY_AND_BOUNDARY_GUARD_V3","case_id":"C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B","trigger_id":"C06_L147_353200_20240626_DATACENTER_FCBGA_BOUNDARY_4B_Stage4B","symbol":"353200","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage4B","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score","contract_score"],"component_delta_explanation":"Promote only named-customer/booked-capacity HBM memory rows; demote product sampling, partial qualification, and generic AI substrate boundary rows.","MFE_90D_pct":18.91,"MAE_90D_pct":-26.48,"score_return_alignment_label":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B","symbol":"007660","company_name":"이수페타시스","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_ACCELERATOR_MLB_BOUNDARY_NOT_HBM_MEMORY_CAPACITY","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"ai_mlb_customer_vocabulary_not_hbm_memory_capacity_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"AI/cloud MLB beneficiary narrative with Nvidia, Google, and Microsoft customer exposure; important AI substrate path but not HBM memory customer/CAPA evidence."}
{"row_type":"trigger","trigger_id":"C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B_Stage4B","case_id":"C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B","symbol":"007660","company_name":"이수페타시스","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_ACCELERATOR_MLB_BOUNDARY_NOT_HBM_MEMORY_CAPACITY","sector":"AI_SEMICONDUCTOR_ELECTRONICS","primary_archetype":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-06-18","evidence_available_at_that_date":"AI/cloud MLB beneficiary narrative with Nvidia, Google, and Microsoft customer exposure; important AI substrate path but not HBM memory customer/CAPA evidence.","evidence_source":"https://view.asiae.co.kr/en/article/2024061809204023846","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007660/2024.csv","profile_path":"atlas/symbol_profiles/007/007660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-19","entry_price":54600.0,"MFE_30D_pct":9.34,"MFE_90D_pct":9.34,"MFE_180D_pct":9.34,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.45,"MAE_90D_pct":-43.41,"MAE_180D_pct":-61.54,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-03","peak_price":59700.0,"drawdown_after_peak_pct":-64.82,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4b_boundary_guard_high_mae","four_b_evidence_type":["positioning_overheat","price_only_local_peak","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ai_mlb_customer_vocabulary_not_hbm_memory_capacity_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY|007660|Stage4B|2024-06-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"C06_CUSTOMER_BOOKED_CAPACITY_AND_BOUNDARY_GUARD_V3","case_id":"C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B","trigger_id":"C06_L147_007660_20240618_AI_MLB_BOUNDARY_4B_Stage4B","symbol":"007660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage4B","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score","contract_score"],"component_delta_explanation":"Promote only named-customer/booked-capacity HBM memory rows; demote product sampling, partial qualification, and generic AI substrate boundary rows.","MFE_90D_pct":9.34,"MAE_90D_pct":-43.41,"score_return_alignment_label":"counterexample_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"147","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["product_sampling_without_named_customer","partial_qualification_without_supply_deal","generic_ai_substrate_boundary_false_positive","high_mae_after_ai_component_theme"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

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

completed_round = R2
completed_loop = 147
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING|C06_HBM_MEMORY_CUSTOMER_CAPACITY|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- stock-web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Evidence sources are listed per case in Section 9 and machine-readable trigger rows.

## Batch Ingest Self-Audit

expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
