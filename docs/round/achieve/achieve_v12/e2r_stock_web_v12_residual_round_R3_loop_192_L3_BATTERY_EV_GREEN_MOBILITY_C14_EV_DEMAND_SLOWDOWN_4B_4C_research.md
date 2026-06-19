# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_mode: post_calibrated_sector_archetype_residual_research_v12
source_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selection_mode: coverage_index_first_with_no_repeat_index_as_duplicate_ledger
selected_round: R3
selected_loop: 192
selected_priority_bucket: Priority_2_quality_reinforcement_4B_4C_boundary_after_C05_C01_C13_C15_C10
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: EV_DEMAND_SLOWDOWN_REVERSIBLE_VS_IRREVERSIBLE_4C
research_file: e2r_stock_web_v12_residual_round_R3_loop_192_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds **6 new independent cases, 3 counterexamples, and 3 residual errors** for L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C. The No-Repeat index is used only as a duplicate ledger and coverage reference, not as a production scoring source.

## 1. Current Calibrated Profile Assumption

```yaml
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
active_runtime_profile_context: e2r_2_2 rolling calibration assumed but not modified
existing_axis_tested:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
new_axis_proposed: false
```

The loop is not re-proving the global Stage2/Green rules. It tests a narrower C14 residual: **EV slowdown/loss language can be either irreversible thesis break or reversible 4B watch depending on customer/ESS/new-model/recovery offsets**.

## 2. Round / Large Sector / Canonical Archetype Scope

```yaml
selected_round: R3
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: EV_DEMAND_SLOWDOWN_REVERSIBLE_VS_IRREVERSIBLE_4C
loop_objective:
  - 4C_thesis_break_timing_test
  - 4B_non_price_requirement_stress_test
  - counterexample_mining
  - sector_specific_rule_discovery
```

C14 belongs to R3 / L3. The selected scope is therefore round-sector consistent.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for selection:

```yaml
canonical_rows_before: 251
canonical_symbols_before: 56
positives_counter_before: 48 / 77
4B_4C_before: 88 / 82
source_proxy_only_total_corpus: 3611
evidence_url_pending_total_corpus: 3888
missing_required_mfe_mae_total_corpus: 3755
```

Local previous outputs deliberately avoided:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
C01_ORDER_BACKLOG_MARGIN_BRIDGE
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
C15_MATERIAL_SPREAD_SUPERCYCLE
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

Hard duplicate key policy:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

| Novelty field | Result |
|---|---:|
| new_independent_case_count | 6 |
| reused_case_count | 0 |
| same_archetype_new_symbol_count | 3 |
| same_archetype_new_trigger_family_count | 6 |
| hard duplicate key reused | 0 |
| new_independent_ratio | 1.00 |

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
primary_price_source: Songdaiki/stock-web
price_data_repo: https://github.com/Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
schema_columns: d,o,h,l,c,v,a,mc,s,m
```

Stock-Web manifest confirms raw/unadjusted marcap OHLC, max date 2026-02-20, calibration shard root `atlas/ohlcv_tradable_by_symbol_year`, and corporate-action windows blocked by default. Schema confirms the MFE/MAE calculation as max high / min low from the entry row through N tradable rows.

## 5. Historical Eligibility Gate

| Symbol | Company | Corporate action candidate dates in profile | Selected entry windows |
|---|---|---|---|
| 373220 | LG Energy Solution | none observed | clean_180D_window |
| 006400 | Samsung SDI | 1996-01-03, 1998-11-03, 2014-07-15 | clean_180D_window for 2024/2025 entries |
| 003670 | POSCO Future M | 2015-05-04, 2021-02-03 | clean_180D_window for 2024 entry |

All trigger rows have entry_date, entry_price, clean 180D windows, and all six required 30/90/180D MFE/MAE fields.

## 6. Canonical Archetype Compression Map

| Fine archetype | Canonical compression | Residual purpose |
|---|---|---|
| EV_DEMAND_SLOWDOWN_UTILIZATION_ADJUSTMENT_4B | C14_EV_DEMAND_SLOWDOWN_4B_4C | local 4B watch when utilization/AMPC pressure exists but offset remains |
| EV_DEMAND_SLOWDOWN_WITH_SHIPMENT_ESS_OFFSET_FALSE_4C | C14_EV_DEMAND_SLOWDOWN_4B_4C | false hard-4C guard when shipment/ESS offset is explicit |
| EV_DEMAND_SLOWDOWN_BATTERY_UNIT_EARNINGS_COLLAPSE_HARD_4C | C14_EV_DEMAND_SLOWDOWN_4B_4C | correct hard 4C when earnings collapse confirms thesis break |
| EV_DEMAND_SLOWDOWN_Q1_TROUGH_WITH_CUSTOMER_RECOVERY_FALSE_4C | C14_EV_DEMAND_SLOWDOWN_4B_4C | loss headline with recovery offset should not auto-route to hard 4C |
| EV_DEMAND_CHASM_LITHIUM_NICKEL_PRICE_INVENTORY_4B | C14_EV_DEMAND_SLOWDOWN_4B_4C | inventory/spread shock as local 4B before full 4C |
| EV_DEMAND_SLOWDOWN_WITH_ESS_STRATEGIC_OFFSET_4B | C14_EV_DEMAND_SLOWDOWN_4B_4C | Q-loss/chasm as 4B watch when ESS/non-EV offset exists |

## 7. Case Selection Summary

|Case ID|Symbol|Company|Trigger|Trigger Date|Entry Date|Entry Close|30D MFE/MAE|90D MFE/MAE|180D MFE/MAE|Role|Profile Verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|C14_373220_20240425_Q1_UTILIZATION_STAGE4B|373220|LG Energy Solution|Stage4B|2024-04-25|2024-04-26|372,000|6.72/-12.37|12.63/-16.4|19.35/-16.4|4B_overlay_success|current_profile_correct|
|C14_373220_20240725_Q2_SHIPMENT_ESS_OFFSET_FALSE_4C|373220|LG Energy Solution|Stage4B|2024-07-25|2024-07-26|325,000|28.92/-4.31|36.62/-4.31|36.62/-4.46|4C_too_early|current_profile_false_positive|
|C14_006400_20241030_Q3_HARD_4C_SUCCESS|006400|Samsung SDI|Stage4C|2024-10-30|2024-10-31|327,000|4.28/-27.98|4.28/-42.87|4.28/-51.77|4C_success|current_profile_correct|
|C14_006400_20250425_Q1_TROUGH_FALSE_HARD_4C|006400|Samsung SDI|Stage4C|2025-04-25|2025-04-28|184,200|2.93/-14.39|27.04/-14.39|109.28/-14.39|4C_too_early|current_profile_false_positive|
|C14_003670_20240123_RESULTS_EV_CHASM_4B|003670|POSCO Future M|Stage4B|2024-01-23|2024-01-24|261,000|28.93/-7.85|30.65/-7.85|30.65/-25.1|4B_overlay_success_with_local_rally_then_decay|current_profile_correct|
|C14_373220_20250109_Q4_LOSS_ESS_OFFSET_STAGE4B|373220|LG Energy Solution|Stage4B|2025-01-09|2025-01-10|348,500|10.9/-5.6|10.9/-23.67|15.64/-23.67|4B_watch_recovery_offset|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 3
counterexample_count: 3
4B_case_count: 4
4C_case_count: 2
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
current_profile_error_count: 3
```

Positive / guardrail successes:

- LGES 2024 Q1: local 4B watch, not hard 4C.
- Samsung SDI 2024 Q3: correct hard 4C after battery-unit collapse.
- POSCO Future M 2023 results: inventory/spread damage as local 4B before full decay.

Counterexamples / residual errors:

- LGES 2024 Q2: slowdown headline had shipment/ESS offset; hard 4C would be false.
- Samsung SDI 2025 Q1: loss headline had demand-recovery and project offset; hard 4C would be false.
- LGES 2025 Q4 preliminary: EV chasm and Q-loss existed, but ESS/non-EV offset kept it at volatile 4B watch.

## 9. Evidence Source Map

|Case ID|Source Key|Evidence Summary|Source URLs|source_proxy_only|evidence_url_pending|
|---|---|---|---|---|---|
|C14_373220_20240425_Q1_UTILIZATION_STAGE4B|LGES_Q1_2024|Q1 2024 release reported revenue/profit pressure, utilization adjustment caused by EV demand slowdown, and operating loss excluding IRA tax credit; the same release also included JV/customer and cost-efficiency offsets, so it is a local 4B watch, not hard 4C.|https://www.lgcorp.com/media/release/27605|0|0|
|C14_373220_20240725_Q2_SHIPMENT_ESS_OFFSET_FALSE_4C|LGES_Q2_2024|Q2 release still cited EV demand slowdown, ASP pressure, and utilization adjustment, but also disclosed sequential revenue improvement from new EV model shipments, ESS grid batteries, Renault LFP agreement, Indonesia JV shipment, and Arizona ESS order.|https://news.lgensol.com/company-news/press-releases/3096/|0|0|
|C14_006400_20241030_Q3_HARD_4C_SUCCESS|Samsung_SDI_Q3_2024|Q3 2024 release showed sharp revenue/operating-profit decline, battery business profit down 85% YoY and 69% QoQ, European EV slowdown and lower cylindrical utilization, with limited near-term recovery language.|https://www.samsungsdi.com/sdi-now/sdi-news/4082.html|0|0|
|C14_006400_20250425_Q1_TROUGH_FALSE_HARD_4C|Samsung_SDI_Q1_2025|Q1 2025 loss and battery operating loss were severe, but official outlook said Q2 earnings should improve upon demand recovery and major OEM inventory adjustments were expected to finalize; Yonhap also tied the loss to EV slowdown and inventory adjustments.|https://www.samsungsdi.com/sdi-now/sdi-news/4344.html<br>https://en.yna.co.kr/view/AEN20250425006751320|0|0|
|C14_003670_20240123_RESULTS_EV_CHASM_4B|POSCO_FutureM_2023|Yonhap reported 2023 net profit plunge and operating-profit decline from lower material prices and inventory valuation pressure; POSCO Future M remained a cathode/anode supplier to major battery customers, so this is spread/inventory quality damage rather than customer cancellation.|https://en.yna.co.kr/view/AEN20240123007500320|0|0|
|C14_373220_20250109_Q4_LOSS_ESS_OFFSET_STAGE4B|Yonhap_LGES_Q4_2024|Q4 2024 preliminary loss and EV chasm were real, but coverage also described temporary slowdown, ESS/non-EV expansion and line conversion. This is a volatile 4B watch, not automatic hard 4C without order or utilization follow-through.|https://en.yna.co.kr/view/AEN20250109002953320<br>https://koreajoongangdaily.joins.com/news/2025-01-09/business/industry/LG-Energy-Solution-posts-Q4-loss-amid-weak-EV-demand/2218019|0|0|

## 10. Price Data Source Map

|Symbol|Entry Date|Open|High|Low|Close|Volume|Stock-Web shard|Corporate action window|
|---|---|---|---|---|---|---|---|---|
|373220|2024-04-26|373,000|375,000|367,500|372,000|143701|atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv|clean_180D_window|
|373220|2024-07-26|332,000|334,000|322,500|325,000|165067|atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv|clean_180D_window|
|006400|2024-10-31|334,500|341,000|327,000|327,000|378994|atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv|clean_180D_window|
|006400|2025-04-28|184,500|189,600|183,500|184,200|327979|atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv|clean_180D_window|
|003670|2024-01-24|265,000|268,500|257,000|261,000|443127|atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv|clean_180D_window|
|373220|2025-01-10|356,000|357,500|348,000|348,500|280639|atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv|clean_180D_window|

## 11. Case-by-Case Trigger Grid

### 11.1 LG Energy Solution 2024 Q1 — Stage4B, not Hard 4C

Q1 evidence showed demand weakening, utilization adjustment, ex-IRA operating loss and ASP pressure. However, the same release included JV shipment/capacity and supply-chain/cost-efficiency offsets. Price path after the 2024-04-26 entry produced 180D MFE/MAE of 19.35 / -16.4, validating local 4B watch rather than hard 4C.

### 11.2 LG Energy Solution 2024 Q2 — False Hard 4C Stress

Q2 evidence still carried slowdown and ASP pressure, but also new EV-model shipments, ESS grid batteries, Renault LFP agreement, Indonesia JV shipment and Arizona ESS order. The price path had 180D MFE/MAE of 36.62 / -4.46. This is the cleanest false-hard-4C row in the batch.

### 11.3 Samsung SDI 2024 Q3 — Correct Hard 4C

Q3 battery business operating profit collapsed and the company cited European EV slowdown and lower utilization. After 2024-10-31, 180D MFE/MAE was 4.28 / -51.77. Hard 4C was appropriate because slowdown translated into realized battery-unit earnings damage with weak near-term offsets.

### 11.4 Samsung SDI 2025 Q1 — Loss Headline but False Hard 4C

Q1 loss was severe, but the release and coverage described demand recovery, major-customer inventory adjustment completion and new battery/customer routes. After 2025-04-28, 180D MFE/MAE was 109.28 / -14.39. This is a hard-4C reversibility guardrail, not a positive Stage2 row.

### 11.5 POSCO Future M 2023 Results — Local 4B before Full Decay

Material price and inventory-value pressure damaged earnings quality. The first 90D still produced 30.65 MFE with only -7.85 MAE, while 180D widened to -25.1 MAE. This supports local 4B, not immediate hard 4C without customer/orderbook break confirmation.

### 11.6 LG Energy Solution 2025 Q4 Preliminary Loss — Volatile 4B Watch

Q4 loss and EV chasm were real, but ESS/non-EV expansion and line conversion were explicit. The row produced 180D MFE/MAE of 15.64 / -23.67. It remains a 4B watch with risk, not clean hard 4C.

## 12. Trigger-Level OHLC Backtest Tables

|Trigger ID|Entry Price|MFE 30D|MAE 30D|MFE 90D|MAE 90D|MFE 180D|MAE 180D|Peak Date|Peak Price|Drawdown after Peak|
|---|---|---|---|---|---|---|---|---|---|---|
|C14_373220_20240425_STAGE4B_EV_DEMAND_UTILIZATION_AMPC|372,000|6.72|-12.37|12.63|-16.40|19.35|-16.40|2024-10-08|444,000|-23.31|
|C14_373220_20240725_STAGE4B_SLOWDOWN_WITH_ESS_SHIPMENT_OFFSET|325,000|28.92|-4.31|36.62|-4.31|36.62|-4.46|2024-10-08|444,000|-30.07|
|C14_006400_20241030_STAGE4C_EV_SLOWDOWN_BATTERY_UNIT_COLLAPSE|327,000|4.28|-27.98|4.28|-42.87|4.28|-51.77|2024-10-31|341,000|-53.75|
|C14_006400_20250425_STAGE4C_LOSS_WITH_RECOVERY_OFFSET_FALSE_BREAK|184,200|2.93|-14.39|27.04|-14.39|109.28|-14.39|2026-01-22|385,500|-15.56|
|C14_003670_20240123_STAGE4B_MATERIAL_PRICE_EV_CHASM_INVENTORY|261,000|28.93|-7.85|30.65|-7.85|30.65|-25.10|2024-03-13|341,000|-42.67|
|C14_373220_20250109_STAGE4B_Q4_LOSS_ESS_OFFSET|348,500|10.90|-5.60|10.90|-23.67|15.64|-23.67|2025-07-31|403,000|-16.50|

## 13. Current Calibrated Profile Stress Test

|Case ID|Trigger|Score Before|Stage Before|Score After|Stage After|Profile Verdict|Alignment|
|---|---|---|---|---|---|---|---|
|C14_373220_20240425_Q1_UTILIZATION_STAGE4B|Stage4B|72|Stage3-Yellow|58|Stage4B|current_profile_correct|4B watch aligned; hard 4C would have been too severe|
|C14_373220_20240725_Q2_SHIPMENT_ESS_OFFSET_FALSE_4C|Stage4B|51|Stage4C|61|Stage4B|current_profile_false_positive|hard 4C would be false; offset evidence plus 180D path supports 4B-only|
|C14_006400_20241030_Q3_HARD_4C_SUCCESS|Stage4C|50|Stage4B|34|Stage4C|current_profile_correct|hard 4C aligned; 180D MFE only 4.28% versus MAE -51.77%|
|C14_006400_20250425_Q1_TROUGH_FALSE_HARD_4C|Stage4C|36|Stage4C|55|Stage4B|current_profile_false_positive|hard 4C too severe; 180D MFE 109.28% after trough-like entry|
|C14_003670_20240123_RESULTS_EV_CHASM_4B|Stage4B|64|Stage3-Yellow|50|Stage4B|current_profile_correct|4B watch aligned; 90D bounce followed by 180D decay, not immediate hard 4C|
|C14_373220_20250109_Q4_LOSS_ESS_OFFSET_STAGE4B|Stage4B|40|Stage4C|53|Stage4B|current_profile_false_positive|hard 4C too severe; local 4B watch still needed because MAE180 reached -23.67%|

Interpretation:

- The current profile is correct when slowdown is backed by irreversible realized deterioration: Samsung SDI Q3 2024.
- The current profile is too harsh when the same evidence set includes credible offset: LGES Q2 2024, Samsung SDI Q1 2025, LGES Q4 2024 preliminary.
- Existing hard 4C routing should be kept, but the C14-specific hard 4C confirmer needs an **offset check**.

## 14. Stage2 / Yellow / Green Comparison

This loop does not promote any Stage3-Green row. All selected triggers are Stage4B/Stage4C timing rows. Green lateness is therefore marked `not_applicable_no_stage3_green_trigger` in the trigger JSONL. The point is not to loosen Green; it is to keep reversible downturn rows from being over-routed to hard 4C.

## 15. 4B Local vs Full-window Timing Audit

| Case | 4B / 4C timing verdict | Local vs full-window read |
|---|---|---|
| LGES Q1 2024 | local_4b_watch_only_non_price_evidence_present | Non-price utilization/AMPC weakness existed, but 180D upside blocked hard 4C. |
| LGES Q2 2024 | local_4b_watch_with_offset_visible | Slowdown was real, offset was stronger; hard 4C false. |
| Samsung SDI Q3 2024 | hard_4c_row_after_non_price_thesis_break | Realized battery-unit collapse confirmed thesis break. |
| Samsung SDI Q1 2025 | hard_4c_stress_but_recovery_offset_visible | Severe loss, but explicit recovery guide made hard 4C premature. |
| POSCO Future M 2023 | local_4b_watch_then_full_window_decay | Inventory/spread issue gave 4B watch; first 90D still bounced. |
| LGES Q4 2024 | local_4b_watch_with_ess_offset_visible | Q-loss and EV chasm with ESS offset; not clean 4C. |

## 16. 4C Protection Audit

```yaml
hard_4c_success:
  - C14_006400_20241030_Q3_HARD_4C_SUCCESS
false_break_or_overhard_4c_risk:
  - C14_373220_20240725_Q2_SHIPMENT_ESS_OFFSET_FALSE_4C
  - C14_006400_20250425_Q1_TROUGH_FALSE_HARD_4C
  - C14_373220_20250109_Q4_LOSS_ESS_OFFSET_STAGE4B
thesis_break_watch_only:
  - C14_373220_20240425_Q1_UTILIZATION_STAGE4B
  - C14_003670_20240123_RESULTS_EV_CHASM_4B
```

## 17. Sector-Specific Rule Candidate

```yaml
sector_specific_rule_candidate: L3_C14_EV_SLOWDOWN_REVERSIBLE_4B_GATE
rule_scope: sector_specific
rule_text: >
  In L3 battery/EV names, EV demand slowdown or quarterly-loss evidence should first route to local 4B watch when the evidence set also contains credible offsets such as ESS/non-EV growth, new model shipments, customer recovery guide, IRA/AMPC eligible-volume stabilization, or line-conversion plan. Hard 4C requires realized earnings collapse plus no offset, repeated utilization break, or customer/order cut confirmation.
confidence: medium
production_scoring_changed: false
```

## 18. Canonical-Archetype Rule Candidate

```yaml
canonical_archetype_rule_candidate: C14_HARD_4C_UTILIZATION_IRREVERSIBILITY_GATE
rule_scope: canonical_archetype_specific
rule_text: >
  For C14, hard 4C is confirmed when at least two of the following are present: battery-unit earnings collapse, utilization decline without recovery guide, customer call-off/order cancellation, ASP/spread deterioration with no offset, or repeated management downgrade. If explicit recovery/ESS/customer/new-model offset exists, cap at Stage4B watch until follow-through confirms irreversibility.
confidence: medium
production_scoring_changed: false
```

## 19. Before / After Backtest Comparison

|Profile|Profile ID|Hypothesis|Changed axes|Eligible triggers|Avg MFE90|Avg MAE90|Avg MFE180|Avg MAE180|Verdict|
|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|current calibrated proxy|can over-route slowdown/loss headlines to hard 4C when offset evidence exists|6|20.35|-18.25|35.97|-22.63|3/6 residual errors: false hard-4C risk in reversible slowdown rows|
|P0b|e2r_2_0_baseline_reference|rollback reference|would under-separate 4B watch from hard 4C and treat slowdown mostly as generic risk|6|20.35|-18.25|35.97|-22.63|less precise timing; weaker hard-4C confirmation|
|P1|L3 sector candidate|EV slowdown offset gate|requires realized earnings collapse plus no offset before hard 4C|6|20.35|-18.25|35.97|-22.63|keeps 4B watch but prevents false hard 4C|
|P2|C14 canonical candidate|reversible vs irreversible 4C split|customer/ESS/new-model/recovery offsets block hard 4C; repeated utilization/customer break confirms|6|20.35|-18.25|35.97|-22.63|best explanatory split for SDI Q3 vs SDI Q1/LGES Q2|
|P3|counterexample guard profile|overhard-4C guard|downgrades single-quarter loss/slowdown with explicit offset to local 4B watch|3|24.85|-14.12|53.85|-14.17|best protection against false hard 4C, but still preserves 4B watch|

## 20. Score-Return Alignment Matrix

| Alignment class | Cases | Read |
|---|---:|---|
| score_return_aligned_4B_watch | 2 | LGES Q1 and POSCO Future M support non-price 4B watch without automatic hard 4C. |
| score_return_aligned_hard_4C | 1 | Samsung SDI Q3 validates hard 4C after realized earnings collapse. |
| residual_false_hard_4C | 3 | LGES Q2, Samsung SDI Q1 2025 and LGES Q4 2024 show offset evidence can reverse the path. |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L3_BATTERY_EV_GREEN_MOBILITY|C14_EV_DEMAND_SLOWDOWN_4B_4C|EV_DEMAND_SLOWDOWN_REVERSIBLE_VS_IRREVERSIBLE_4C|3|3|4|2|6|0|6|6|3|L3_C14_EV_SLOWDOWN_REVERSIBLE_4B_GATE|C14_HARD_4C_UTILIZATION_IRREVERSIBILITY_GATE|quality reinforcement: false-hard-4C reversible-vs-irreversible split|

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 6
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - false_hard_4c_from_reversible_slowdown
  - local_4b_vs_hard_4c_boundary
  - earnings_loss_with_recovery_offset
new_axis_proposed: false
existing_axis_strengthened:
  - hard_4c_requires_irreversible_demand_or_customer_break
  - stage4b_local_watch_non_price_gate
existing_axis_weakened:
  - hard_4c_from_slowdown_word_alone
  - hard_4c_from_single_quarter_loss_when_recovery_offset_is_explicit
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L3_C14_EV_SLOWDOWN_REVERSIBLE_4B_GATE
canonical_archetype_rule_candidate: C14_HARD_4C_UTILIZATION_IRREVERSIBILITY_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Historical trigger-level evidence available at trigger date.
- Actual Stock-Web 1D tradable OHLC rows.
- 30D/90D/180D MFE and MAE for every trigger.
- 4B local watch vs hard 4C distinction.
- Sector/canonical shadow rules only.

Non-validation scope:

- No live candidate search.
- No current stock recommendation.
- No production scoring change.
- No stock_agent source-code patch.
- No brokerage/API/trading action.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,hard_4c_requires_irreversible_ev_slowdown,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Block hard 4C when slowdown/loss evidence includes ESS/new-model/customer recovery offset","reduces 3 false-hard-4C rows while retaining SDI 2024 hard-4C success","C14_373220_20240725_STAGE4B_SLOWDOWN_WITH_ESS_SHIPMENT_OFFSET|C14_006400_20241030_STAGE4C_EV_SLOWDOWN_BATTERY_UNIT_COLLAPSE|C14_006400_20250425_STAGE4C_LOSS_WITH_RECOVERY_OFFSET_FALSE_BREAK",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,local_4b_watch_for_ev_slowdown_with_offset,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Keep non-price EV slowdown evidence as 4B watch when offset exists","preserves risk overlay without suppressing reversible trough rows","C14_373220_20240425_STAGE4B_EV_DEMAND_UTILIZATION_AMPC|C14_373220_20250109_STAGE4B_Q4_LOSS_ESS_OFFSET",6,6,3,medium,sector_shadow_only,"not production; batch confirmation required"
```

## 25. Machine-Readable Rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_373220_20240425_Q1_UTILIZATION_STAGE4B", "case_type": "4B_overlay_success", "company_name": "LG Energy Solution", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_UTILIZATION_ADJUSTMENT_4B", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "notes": "Q1 2024 release reported revenue/profit pressure, utilization adjustment caused by EV demand slowdown, and operating loss excluding IRA tax credit; the same release also included JV/customer and cost-efficiency offsets, so it is a local 4B watch, not hard 4C.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "4B watch aligned; hard 4C would have been too severe", "symbol": "373220"}
{"MAE_180D_pct": -16.4, "MAE_1Y_pct": -17.74, "MAE_2Y_pct": null, "MAE_30D_pct": -12.37, "MAE_90D_pct": -16.4, "MFE_180D_pct": 19.35, "MFE_1Y_pct": 19.35, "MFE_2Y_pct": null, "MFE_30D_pct": 6.72, "MFE_90D_pct": 12.63, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_373220_20240425_Q1_UTILIZATION_STAGE4B", "company_name": "LG Energy Solution", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -23.31, "entry_date": "2024-04-26", "entry_price": 372000.0, "evidence_available_at_that_date": "Q1 2024 release reported revenue/profit pressure, utilization adjustment caused by EV demand slowdown, and operating loss excluding IRA tax credit; the same release also included JV/customer and cost-efficiency offsets, so it is a local 4B watch, not hard 4C.", "evidence_source": "https://www.lgcorp.com/media/release/27605", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_UTILIZATION_ADJUSTMENT_4B", "forward_window_trading_days": 440, "four_b_evidence_type": "margin_or_backlog_slowdown|explicit_event_cap", "four_b_full_window_peak_proximity": "not_promoted_to_full_4b_without_non_price_followthrough", "four_b_local_peak_proximity": "watch_case_no_prior_stage2_pair", "four_b_timing_verdict": "local_4b_watch_only_non_price_evidence_present", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|sector_specific_rule_discovery", "peak_date": "2024-10-08", "peak_price": 444000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "primary_archetype": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "profile_path": "atlas/symbol_profiles/373/373220.json", "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|373220|Stage4B|2024-04-26", "sector": "battery_ev_green_mobility", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "373220", "trigger_date": "2024-04-25", "trigger_id": "C14_373220_20240425_STAGE4B_EV_DEMAND_UTILIZATION_AMPC", "trigger_outcome_label": "utilization_adjustment_and_ampc_dependency_local_4b_not_hard_4c", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -16.4, "MFE_90D_pct": 12.63, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_373220_20240425_Q1_UTILIZATION_STAGE4B", "changed_components": ["execution_risk_score", "margin_bridge_score", "customer_quality_score", "policy_or_regulatory_score"], "component_delta_explanation": "utilization slowdown, ex-IRA loss and ASP pressure lower margin/revision visibility; JV and supply-chain offsets block hard 4C.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 30, "contract_score": 35, "customer_quality_score": 45, "dilution_cb_risk_score": 0, "execution_risk_score": 70, "legal_or_contract_risk_score": 5, "margin_bridge_score": 25, "policy_or_regulatory_score": 55, "relative_strength_score": 45, "revision_score": 25, "valuation_repricing_score": 42}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 30, "contract_score": 35, "customer_quality_score": 45, "dilution_cb_risk_score": 0, "execution_risk_score": 55, "legal_or_contract_risk_score": 5, "margin_bridge_score": 25, "policy_or_regulatory_score": 55, "relative_strength_score": 45, "revision_score": 25, "valuation_repricing_score": 42}, "row_type": "score_simulation", "score_return_alignment_label": "4B watch aligned; hard 4C would have been too severe", "stage_label_after": "Stage4B", "stage_label_before": "Stage3-Yellow", "symbol": "373220", "trigger_id": "C14_373220_20240425_STAGE4B_EV_DEMAND_UTILIZATION_AMPC", "weighted_score_after": 58, "weighted_score_before": 72}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_373220_20240725_Q2_SHIPMENT_ESS_OFFSET_FALSE_4C", "case_type": "4C_false_break_guardrail", "company_name": "LG Energy Solution", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_WITH_SHIPMENT_ESS_OFFSET_FALSE_4C", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "notes": "Q2 release still cited EV demand slowdown, ASP pressure, and utilization adjustment, but also disclosed sequential revenue improvement from new EV model shipments, ESS grid batteries, Renault LFP agreement, Indonesia JV shipment, and Arizona ESS order.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard 4C would be false; offset evidence plus 180D path supports 4B-only", "symbol": "373220"}
{"MAE_180D_pct": -4.46, "MAE_1Y_pct": -18.15, "MAE_2Y_pct": null, "MAE_30D_pct": -4.31, "MAE_90D_pct": -4.31, "MFE_180D_pct": 36.62, "MFE_1Y_pct": 36.62, "MFE_2Y_pct": null, "MFE_30D_pct": 28.92, "MFE_90D_pct": 36.62, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_373220_20240725_Q2_SHIPMENT_ESS_OFFSET_FALSE_4C", "company_name": "LG Energy Solution", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.07, "entry_date": "2024-07-26", "entry_price": 325000.0, "evidence_available_at_that_date": "Q2 release still cited EV demand slowdown, ASP pressure, and utilization adjustment, but also disclosed sequential revenue improvement from new EV model shipments, ESS grid batteries, Renault LFP agreement, Indonesia JV shipment, and Arizona ESS order.", "evidence_source": "https://news.lgensol.com/company-news/press-releases/3096/", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_WITH_SHIPMENT_ESS_OFFSET_FALSE_4C", "forward_window_trading_days": 379, "four_b_evidence_type": "margin_or_backlog_slowdown|explicit_event_cap", "four_b_full_window_peak_proximity": "not_promoted_to_full_4b_without_non_price_followthrough", "four_b_local_peak_proximity": "watch_case_no_prior_stage2_pair", "four_b_timing_verdict": "local_4b_watch_with_offset_visible", "four_c_protection_label": "false_break", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|sector_specific_rule_discovery", "peak_date": "2024-10-08", "peak_price": 444000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv", "primary_archetype": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "profile_path": "atlas/symbol_profiles/373/373220.json", "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|373220|Stage4B|2024-07-26", "sector": "battery_ev_green_mobility", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "373220", "trigger_date": "2024-07-25", "trigger_id": "C14_373220_20240725_STAGE4B_SLOWDOWN_WITH_ESS_SHIPMENT_OFFSET", "trigger_outcome_label": "ev_slowdown_headline_offset_by_new_model_shipments_and_ess_false_hard_4c", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -4.31, "MFE_90D_pct": 36.62, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_373220_20240725_Q2_SHIPMENT_ESS_OFFSET_FALSE_4C", "changed_components": ["execution_risk_score", "margin_bridge_score", "customer_quality_score", "policy_or_regulatory_score"], "component_delta_explanation": "add offset-quality bonus from shipments/ESS agreement and block hard 4C unless deterioration follow-through appears.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 30, "contract_score": 30, "customer_quality_score": 45, "dilution_cb_risk_score": 0, "execution_risk_score": 70, "legal_or_contract_risk_score": 5, "margin_bridge_score": 20, "policy_or_regulatory_score": 55, "relative_strength_score": 42, "revision_score": 20, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 30, "contract_score": 30, "customer_quality_score": 45, "dilution_cb_risk_score": 0, "execution_risk_score": 65, "legal_or_contract_risk_score": 5, "margin_bridge_score": 20, "policy_or_regulatory_score": 55, "relative_strength_score": 42, "revision_score": 20, "valuation_repricing_score": 45}, "row_type": "score_simulation", "score_return_alignment_label": "hard 4C would be false; offset evidence plus 180D path supports 4B-only", "stage_label_after": "Stage4B", "stage_label_before": "Stage4C", "symbol": "373220", "trigger_id": "C14_373220_20240725_STAGE4B_SLOWDOWN_WITH_ESS_SHIPMENT_OFFSET", "weighted_score_after": 61, "weighted_score_before": 51}
{"best_trigger": "Stage4C", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_006400_20241030_Q3_HARD_4C_SUCCESS", "case_type": "4C_success", "company_name": "Samsung SDI", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_BATTERY_UNIT_EARNINGS_COLLAPSE_HARD_4C", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "notes": "Q3 2024 release showed sharp revenue/operating-profit decline, battery business profit down 85% YoY and 69% QoQ, European EV slowdown and lower cylindrical utilization, with limited near-term recovery language.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard 4C aligned; 180D MFE only 4.28% versus MAE -51.77%", "symbol": "006400"}
{"MAE_180D_pct": -51.77, "MAE_1Y_pct": -51.77, "MAE_2Y_pct": null, "MAE_30D_pct": -27.98, "MAE_90D_pct": -42.87, "MFE_180D_pct": 4.28, "MFE_1Y_pct": 8.41, "MFE_2Y_pct": null, "MFE_30D_pct": 4.28, "MFE_90D_pct": 4.28, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_006400_20241030_Q3_HARD_4C_SUCCESS", "company_name": "Samsung SDI", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -53.75, "entry_date": "2024-10-31", "entry_price": 327000.0, "evidence_available_at_that_date": "Q3 2024 release showed sharp revenue/operating-profit decline, battery business profit down 85% YoY and 69% QoQ, European EV slowdown and lower cylindrical utilization, with limited near-term recovery language.", "evidence_source": "https://www.samsungsdi.com/sdi-now/sdi-news/4082.html", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_BATTERY_UNIT_EARNINGS_COLLAPSE_HARD_4C", "forward_window_trading_days": 317, "four_b_evidence_type": "margin_or_backlog_slowdown|explicit_event_cap", "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "hard_4c_row_after_non_price_thesis_break", "four_c_protection_label": "hard_4c_success", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|sector_specific_rule_discovery", "peak_date": "2024-10-31", "peak_price": 341000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv", "primary_archetype": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "profile_path": "atlas/symbol_profiles/006/006400.json", "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|006400|Stage4C|2024-10-31", "sector": "battery_ev_green_mobility", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken", "call_off_or_order_cut"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "006400", "trigger_date": "2024-10-30", "trigger_id": "C14_006400_20241030_STAGE4C_EV_SLOWDOWN_BATTERY_UNIT_COLLAPSE", "trigger_outcome_label": "ev_slowdown_plus_battery_unit_earnings_collapse_hard_4c_success", "trigger_type": "Stage4C"}
{"MAE_90D_pct": -42.87, "MFE_90D_pct": 4.28, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_006400_20241030_Q3_HARD_4C_SUCCESS", "changed_components": ["execution_risk_score", "margin_bridge_score", "customer_quality_score", "policy_or_regulatory_score"], "component_delta_explanation": "realized battery-unit collapse and lower utilization convert slowdown from 4B watch to hard 4C.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 15, "customer_quality_score": 25, "dilution_cb_risk_score": 0, "execution_risk_score": 90, "legal_or_contract_risk_score": 10, "margin_bridge_score": 4, "policy_or_regulatory_score": 25, "relative_strength_score": 35, "revision_score": 15, "valuation_repricing_score": 32}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 20, "contract_score": 15, "customer_quality_score": 25, "dilution_cb_risk_score": 0, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "margin_bridge_score": 12, "policy_or_regulatory_score": 25, "relative_strength_score": 35, "revision_score": 15, "valuation_repricing_score": 32}, "row_type": "score_simulation", "score_return_alignment_label": "hard 4C aligned; 180D MFE only 4.28% versus MAE -51.77%", "stage_label_after": "Stage4C", "stage_label_before": "Stage4B", "symbol": "006400", "trigger_id": "C14_006400_20241030_STAGE4C_EV_SLOWDOWN_BATTERY_UNIT_COLLAPSE", "weighted_score_after": 34, "weighted_score_before": 50}
{"best_trigger": "Stage4C", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_006400_20250425_Q1_TROUGH_FALSE_HARD_4C", "case_type": "4C_false_break_guardrail", "company_name": "Samsung SDI", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_Q1_TROUGH_WITH_CUSTOMER_RECOVERY_FALSE_4C", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "notes": "Q1 2025 loss and battery operating loss were severe, but official outlook said Q2 earnings should improve upon demand recovery and major OEM inventory adjustments were expected to finalize; Yonhap also tied the loss to EV slowdown and inventory adjustments.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard 4C too severe; 180D MFE 109.28% after trough-like entry", "symbol": "006400"}
{"MAE_180D_pct": -14.39, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "MAE_30D_pct": -14.39, "MAE_90D_pct": -14.39, "MFE_180D_pct": 109.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 2.93, "MFE_90D_pct": 27.04, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_006400_20250425_Q1_TROUGH_FALSE_HARD_4C", "company_name": "Samsung SDI", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -15.56, "entry_date": "2025-04-28", "entry_price": 184200.0, "evidence_available_at_that_date": "Q1 2025 loss and battery operating loss were severe, but official outlook said Q2 earnings should improve upon demand recovery and major OEM inventory adjustments were expected to finalize; Yonhap also tied the loss to EV slowdown and inventory adjustments.", "evidence_source": "https://www.samsungsdi.com/sdi-now/sdi-news/4344.html + https://en.yna.co.kr/view/AEN20250425006751320", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_Q1_TROUGH_WITH_CUSTOMER_RECOVERY_FALSE_4C", "forward_window_trading_days": 198, "four_b_evidence_type": "margin_or_backlog_slowdown|explicit_event_cap", "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "hard_4c_stress_but_recovery_offset_visible", "four_c_protection_label": "false_break", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|sector_specific_rule_discovery", "peak_date": "2026-01-22", "peak_price": 385500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv", "primary_archetype": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "profile_path": "atlas/symbol_profiles/006/006400.json", "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|006400|Stage4C|2025-04-28", "sector": "battery_ev_green_mobility", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stock_web_manifest_max_date": "2026-02-20", "symbol": "006400", "trigger_date": "2025-04-25", "trigger_id": "C14_006400_20250425_STAGE4C_LOSS_WITH_RECOVERY_OFFSET_FALSE_BREAK", "trigger_outcome_label": "q1_loss_with_demand_recovery_offset_false_hard_4c_timing", "trigger_type": "Stage4C"}
{"MAE_90D_pct": -14.39, "MFE_90D_pct": 27.04, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_006400_20250425_Q1_TROUGH_FALSE_HARD_4C", "changed_components": ["execution_risk_score", "margin_bridge_score", "customer_quality_score", "policy_or_regulatory_score"], "component_delta_explanation": "loss headline remains a 4B warning, but explicit recovery/46-series/new-project offset blocks hard 4C until follow-through confirms.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 15, "contract_score": 12, "customer_quality_score": 20, "dilution_cb_risk_score": 0, "execution_risk_score": 88, "legal_or_contract_risk_score": 10, "margin_bridge_score": 8, "policy_or_regulatory_score": 35, "relative_strength_score": 20, "revision_score": 10, "valuation_repricing_score": 28}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 15, "contract_score": 12, "customer_quality_score": 20, "dilution_cb_risk_score": 0, "execution_risk_score": 88, "legal_or_contract_risk_score": 10, "margin_bridge_score": 8, "policy_or_regulatory_score": 35, "relative_strength_score": 20, "revision_score": 10, "valuation_repricing_score": 28}, "row_type": "score_simulation", "score_return_alignment_label": "hard 4C too severe; 180D MFE 109.28% after trough-like entry", "stage_label_after": "Stage4B", "stage_label_before": "Stage4C", "symbol": "006400", "trigger_id": "C14_006400_20250425_STAGE4C_LOSS_WITH_RECOVERY_OFFSET_FALSE_BREAK", "weighted_score_after": 55, "weighted_score_before": 36}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_003670_20240123_RESULTS_EV_CHASM_4B", "case_type": "4B_overlay_success", "company_name": "POSCO Future M", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "EV_DEMAND_CHASM_LITHIUM_NICKEL_PRICE_INVENTORY_4B", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "notes": "Yonhap reported 2023 net profit plunge and operating-profit decline from lower material prices and inventory valuation pressure; POSCO Future M remained a cathode/anode supplier to major battery customers, so this is spread/inventory quality damage rather than customer cancellation.", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "4B watch aligned; 90D bounce followed by 180D decay, not immediate hard 4C", "symbol": "003670"}
{"MAE_180D_pct": -25.1, "MAE_1Y_pct": null, "MAE_2Y_pct": null, "MAE_30D_pct": -7.85, "MAE_90D_pct": -7.85, "MFE_180D_pct": 30.65, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 28.93, "MFE_90D_pct": 30.65, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_003670_20240123_RESULTS_EV_CHASM_4B", "company_name": "POSCO Future M", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.67, "entry_date": "2024-01-24", "entry_price": 261000.0, "evidence_available_at_that_date": "Yonhap reported 2023 net profit plunge and operating-profit decline from lower material prices and inventory valuation pressure; POSCO Future M remained a cathode/anode supplier to major battery customers, so this is spread/inventory quality damage rather than customer cancellation.", "evidence_source": "https://en.yna.co.kr/view/AEN20240123007500320", "fine_archetype_id": "EV_DEMAND_CHASM_LITHIUM_NICKEL_PRICE_INVENTORY_4B", "forward_window_trading_days": 228, "four_b_evidence_type": "margin_or_backlog_slowdown|explicit_event_cap", "four_b_full_window_peak_proximity": "not_promoted_to_full_4b_without_non_price_followthrough", "four_b_local_peak_proximity": "watch_case_no_prior_stage2_pair", "four_b_timing_verdict": "local_4b_watch_then_full_window_decay", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|sector_specific_rule_discovery", "peak_date": "2024-03-13", "peak_price": 341000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv", "primary_archetype": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "profile_path": "atlas/symbol_profiles/003/003670.json", "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|003670|Stage4B|2024-01-24", "sector": "battery_ev_green_mobility", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "003670", "trigger_date": "2024-01-23", "trigger_id": "C14_003670_20240123_STAGE4B_MATERIAL_PRICE_EV_CHASM_INVENTORY", "trigger_outcome_label": "material_price_inventory_loss_ev_chasm_local_4b_before_full_decay", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -7.85, "MFE_90D_pct": 30.65, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_003670_20240123_RESULTS_EV_CHASM_4B", "changed_components": ["execution_risk_score", "margin_bridge_score", "customer_quality_score", "policy_or_regulatory_score"], "component_delta_explanation": "inventory/spread loss blocks positive stage; lack of customer cancellation keeps it at local 4B rather than hard 4C.", "current_profile_verdict": "current_profile_correct", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 25, "contract_score": 35, "customer_quality_score": 55, "dilution_cb_risk_score": 0, "execution_risk_score": 70, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 35, "relative_strength_score": 40, "revision_score": 20, "valuation_repricing_score": 45}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 25, "contract_score": 35, "customer_quality_score": 55, "dilution_cb_risk_score": 0, "execution_risk_score": 65, "legal_or_contract_risk_score": 5, "margin_bridge_score": 18, "policy_or_regulatory_score": 35, "relative_strength_score": 40, "revision_score": 20, "valuation_repricing_score": 45}, "row_type": "score_simulation", "score_return_alignment_label": "4B watch aligned; 90D bounce followed by 180D decay, not immediate hard 4C", "stage_label_after": "Stage4B", "stage_label_before": "Stage3-Yellow", "symbol": "003670", "trigger_id": "C14_003670_20240123_STAGE4B_MATERIAL_PRICE_EV_CHASM_INVENTORY", "weighted_score_after": 50, "weighted_score_before": 64}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_373220_20250109_Q4_LOSS_ESS_OFFSET_STAGE4B", "case_type": "4C_false_break_guardrail", "company_name": "LG Energy Solution", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_WITH_ESS_STRATEGIC_OFFSET_4B", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "notes": "Q4 2024 preliminary loss and EV chasm were real, but coverage also described temporary slowdown, ESS/non-EV expansion and line conversion. This is a volatile 4B watch, not automatic hard 4C without order or utilization follow-through.", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R3", "row_type": "case", "score_price_alignment": "hard 4C too severe; local 4B watch still needed because MAE180 reached -23.67%", "symbol": "373220"}
{"MAE_180D_pct": -23.67, "MAE_1Y_pct": -23.67, "MAE_2Y_pct": null, "MAE_30D_pct": -5.6, "MAE_90D_pct": -23.67, "MFE_180D_pct": 15.64, "MFE_1Y_pct": 51.22, "MFE_2Y_pct": null, "MFE_30D_pct": 10.9, "MFE_90D_pct": 10.9, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_373220_20250109_Q4_LOSS_ESS_OFFSET_STAGE4B", "company_name": "LG Energy Solution", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -16.5, "entry_date": "2025-01-10", "entry_price": 348500.0, "evidence_available_at_that_date": "Q4 2024 preliminary loss and EV chasm were real, but coverage also described temporary slowdown, ESS/non-EV expansion and line conversion. This is a volatile 4B watch, not automatic hard 4C without order or utilization follow-through.", "evidence_source": "https://en.yna.co.kr/view/AEN20250109002953320 + https://koreajoongangdaily.joins.com/news/2025-01-09/business/industry/LG-Energy-Solution-posts-Q4-loss-amid-weak-EV-demand/2218019", "fine_archetype_id": "EV_DEMAND_SLOWDOWN_WITH_ESS_STRATEGIC_OFFSET_4B", "forward_window_trading_days": 269, "four_b_evidence_type": "margin_or_backlog_slowdown|explicit_event_cap", "four_b_full_window_peak_proximity": "not_promoted_to_full_4b_without_non_price_followthrough", "four_b_local_peak_proximity": "watch_case_no_prior_stage2_pair", "four_b_timing_verdict": "local_4b_watch_with_ess_offset_visible", "four_c_protection_label": "false_break", "green_lateness_ratio": "not_applicable_no_stage3_green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "loop_objective": "4C_thesis_break_timing_test|4B_non_price_requirement_stress_test|counterexample_mining|sector_specific_rule_discovery", "peak_date": "2025-07-31", "peak_price": 403000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv", "primary_archetype": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "profile_path": "atlas/symbol_profiles/373/373220.json", "reuse_reason": null, "round": "R3", "row_type": "trigger", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C|373220|Stage4B|2025-01-10", "sector": "battery_ev_green_mobility", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "explicit_event_cap"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "373220", "trigger_date": "2025-01-09", "trigger_id": "C14_373220_20250109_STAGE4B_Q4_LOSS_ESS_OFFSET", "trigger_outcome_label": "q4_loss_and_ev_chasm_with_ess_offset_not_clean_hard_4c", "trigger_type": "Stage4B"}
{"MAE_90D_pct": -23.67, "MFE_90D_pct": 10.9, "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "case_id": "C14_373220_20250109_Q4_LOSS_ESS_OFFSET_STAGE4B", "changed_components": ["execution_risk_score", "margin_bridge_score", "customer_quality_score", "policy_or_regulatory_score"], "component_delta_explanation": "temporary slowdown and ESS conversion offset weaken hard 4C while preserving 4B risk overlay.", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow", "raw_component_scores_after": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 18, "contract_score": 15, "customer_quality_score": 25, "dilution_cb_risk_score": 0, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "margin_bridge_score": 10, "policy_or_regulatory_score": 40, "relative_strength_score": 30, "revision_score": 12, "valuation_repricing_score": 35}, "raw_component_scores_before": {"accounting_trust_risk_score": 5, "backlog_visibility_score": 18, "contract_score": 15, "customer_quality_score": 25, "dilution_cb_risk_score": 0, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "margin_bridge_score": 10, "policy_or_regulatory_score": 40, "relative_strength_score": 30, "revision_score": 12, "valuation_repricing_score": 35}, "row_type": "score_simulation", "score_return_alignment_label": "hard 4C too severe; local 4B watch still needed because MAE180 reached -23.67%", "stage_label_after": "Stage4B", "stage_label_before": "Stage4C", "symbol": "373220", "trigger_id": "C14_373220_20250109_STAGE4B_Q4_LOSS_ESS_OFFSET", "weighted_score_after": 53, "weighted_score_before": 40}
{"canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "do_not_propose_new_weight_delta": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "loop": "192", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 6, "new_symbol_count": 3, "new_trigger_family_count": 6, "residual_error_types_found": ["false_hard_4c_from_reversible_slowdown", "local_4b_vs_hard_4c_boundary", "earnings_loss_with_recovery_offset"], "reused_case_count": 0, "round": "R3", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["hard_4c_thesis_break_routes_to_4c", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"]}
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

```yaml
completed_round: R3
completed_loop: 192
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority_2_quality_reinforcement_4B_4C_boundary_after_C05_C01_C13_C15_C10
next_recommended_archetypes:
  - C02_POWER_GRID_DATACENTER_CAPEX
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C14_EV_DEMAND_SLOWDOWN_4B_4C_OFFSET_HOLDOUT
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-Repeat Index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Daikisong/stock-web/refs/heads/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Daikisong/stock-web/refs/heads/main/atlas/schema.json
- LG Energy Solution Q1 2024: https://www.lgcorp.com/media/release/27605
- LG Energy Solution Q2 2024: https://news.lgensol.com/company-news/press-releases/3096/
- Samsung SDI Q3 2024: https://www.samsungsdi.com/sdi-now/sdi-news/4082.html
- Samsung SDI Q1 2025: https://www.samsungsdi.com/sdi-now/sdi-news/4344.html
- Yonhap Samsung SDI Q1 2025: https://en.yna.co.kr/view/AEN20250425006751320
- POSCO Future M 2023 result coverage: https://en.yna.co.kr/view/AEN20240123007500320
- Yonhap LGES Q4 2024 preliminary: https://en.yna.co.kr/view/AEN20250109002953320
