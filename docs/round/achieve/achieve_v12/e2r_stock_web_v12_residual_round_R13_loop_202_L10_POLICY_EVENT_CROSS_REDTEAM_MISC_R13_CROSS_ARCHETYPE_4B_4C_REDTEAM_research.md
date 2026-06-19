# E2R Stock-Web v12 Residual Research — R13 / 4B·4C Offset Quality Refresh

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
output_file = e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Execution scope

This standalone Markdown file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as the execution procedure. It does not open or patch `stock_agent` source code, does not perform live discovery, does not recommend current stocks, and does not change production scoring.

The No-Repeat Index is used only as a duplicate-prevention ledger and quality-gap guide. The current cumulative corpus is beyond the old 30/50/80-row filling phase, so this run is a **R13 cross-archetype boundary audit**, not a new sector-positive hunting run.

## 2. Selection Metadata

```text
selected_round = R13
selected_loop = 202
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 R13 quality refresh / 4B-4C offset-quality cleanup
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id = R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS
standard_v12_filename = e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

### Why R13 / 4B·4C was selected

The latest ledger shows all C01~C32 archetypes above 80 representative rows, while R13 cross-archetype scopes are now quality-control surfaces. The useful residual is no longer “add more rows.” It is to compress recent C05/C13/C02/C16 holdouts into a reusable 4B/4C boundary:

```text
R13 question:
  - When is ugly non-price evidence hard 4C?
  - When is it only local 4B/watch because offset quality is real?
  - When does a damaged thesis reopen to Stage2-Actionable?
  - When should theme/profile exposure stay capped even when the market later rallies?
```

Hard duplicate key used in this R13 file:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Visible/local R13 4B/4C duplicates intentionally avoided:

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|095610|Stage4B|2024-04-25
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|166090|Stage4B|2024-06-26
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|373220|Stage4B|2024-07-26
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006400|Stage4C|2024-10-31
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006400|Stage4C|2025-04-28
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|010950|Stage4C|2023-04-25
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|096770|Stage4C|2023-02-07
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|375500|Stage4C|2025-02-07
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|010120|Stage4B|2024-07-25
```

## 3. Stock-Web Price Atlas Validation

```text
price_atlas_repo = Songdaiki/stock-web
manifest = atlas/manifest.json
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14,354,401
raw_row_count = 15,214,118
symbol_count = 5,414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_schema = d,o,h,l,c,v,a,mc,s,m
```

MFE/MAE method:

```text
entry_price = actual stock-web tradable close on entry_date
MFE_N = max(high from entry row through N-th forward tradable row) / entry_close - 1
MAE_N = min(low from entry row through N-th forward tradable row) / entry_close - 1
```

All selected usable rows have complete 30D/90D/180D forward windows before manifest max date and are treated as clean 180D calibration windows in their source-sector MDs.

## 4. Batch Coverage / Novelty Summary

```text
source_sector_case_reused_count = 12
new_independent_case_count_for_r13_scope = 12
new_independent_trigger_count_for_r13_scope = 12
unique_symbol_count = 10
unique_source_canonical_count = 4

stage2_actionable_count = 3
stage4b_count = 6
stage4c_count = 3

positive_or_reopen_control_count = 3
offset_quality_watch_count = 4
hard_4c_positive_control_count = 3
proxy_theme_or_profile_cap_count = 2

source_proxy_only_count = 2
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
missing_entry_price_count = 0
missing_actual_entry_ohlcv_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0

current_profile_error_count = 9
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
ready_for_batch_ingest = true
```

## 5. Evidence Map

| # | symbol | company | source canonical | evidence family | evidence summary | source URL |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `006360` | GS E&C | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | construction_quality_admission_missing_rebar | Issuer-confirmed construction-quality failure at Geomdan apartment parking-lot collapse; missing rebar / faulty construction is direct non-price thesis-break evidence. | https://www.koreatimes.co.kr/business/companies/20230509/gs-ec-admits-to-faulty-construction-of-apartment-underground-parking-lot-in-incheon |
| 2 | `006360` | GS E&C | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | ceo_change_brand_repair_after_quality_failure | Management reset after the quality scandal is non-price offset/watch evidence; it should split later repair state from the original hard 4C event. | https://www.koreatimes.co.kr/business/companies/20231020/gs-ec-replaces-ceo-with-owners-son |
| 3 | `294870` | HDC Hyundai Development | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | business_suspension_license_risk | Business suspension and license risk after fatal construction collapse are direct operating-permission damage; hard 4C should override order headlines. | https://koreajoongangdaily.joins.com/2022/03/30/business/industry/HDC-Building-collapse-Gwangju/20220330162503613.html |
| 4 | `294870` | HDC Hyundai Development | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | credit_rating_financial_improvement_recovery | Credit-rating / financial-improvement recognition reopens a damaged construction thesis, but high MAE keeps Yellow/Green blocked until cash conversion is visible. | https://biz.chosun.com/en/en-realestate/2025/05/26/4XWZSHVIIND6HO5MXQE5SYR43E/ |
| 5 | `373220` | LG Energy Solution | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | ex_AMPC_loss_lower_utilization_capex_cut_with_ESS_offset | FY2024/Q4 loss and AMPC dependence were ugly, but ESS/new-chemistry/order-processing offsets argue for 4B/watch before hard 4C. | https://www.lgcorp.com/media/release/28617 |
| 6 | `006400` | Samsung SDI | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | battery_loss_customer_inventory_ESS_JV_offset | Battery operating loss and customer inventory adjustment fit hard-break language, but ESS record revenue and U.S. JV progress mean weak-offset quality must be proven before hard 4C is final. | https://www.businesskorea.co.kr/news/articleView.html?idxno=234435 |
| 7 | `020150` | LOTTE Energy Materials | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | copper_foil_customer_inventory_adjustment_utilization_recovery_guidance | Shipment reduction and customer inventory adjustment were negative, but stated utilization recovery and North America OEM/JV route make this reversible 4B/watch. | https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=138 |
| 8 | `003670` | POSCO Future M | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | q1_profit_reopen_cathode_materials_turnaround | Q1 2025 revenue/profit rebound is a direct reopen bridge after a weak battery-material year, but high MAE keeps Yellow/Green capped. | https://www.poscofuturem.com/en/pr/list.do?m=04&topic=18&y=2025 |
| 9 | `024840` | KBI Metal | C02_POWER_GRID_DATACENTER_CAPEX | copper_wire_power_grid_theme_no_company_order_bridge | Copper-wire/power-line theme exposure without customer-specific grid order/backlog bridge; this is local 4B/proxy-theme overextension. | https://www.asiae.co.kr/en/article/2024041910590184215 |
| 10 | `267260` | HD Hyundai Electric | C02_POWER_GRID_DATACENTER_CAPEX | orders_backlog_sales_operating_profit_margin_bridge | Orders, backlog, sales, operating profit and North-America profitability form a direct grid equipment bridge; this should not be penalized like proxy-theme 4B rows. | https://en.yna.co.kr/view/AEN20250422006151320 |
| 11 | `047400` | Union Materials | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | rare_earth_export_control_ferrite_magnet_proxy | Ferrite magnet / rare-earth substitute theme is real product exposure, but the as-of evidence lacks customer pull, shipment, ASP, margin, or offtake bridge. | https://www.mk.co.kr/en/stock/11290565 |
| 12 | `005490` | POSCO Holdings | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | lithium_hydroxide_capacity_long_lead_resource_bridge | Lithium hydroxide facility opening is company-specific strategic-resource capacity, but near-term offtake/margin/cashflow conversion was not visible at entry. | https://www.pls.com/news-stories/posco-pilbara-minerals-jv-opens-south-korean-lithium-hydroxide-facility/ |

## 6. Actual Entry OHLCV Rows

| symbol | company | entry_date | o | h | l | c | v | a | mc | s | m | tradable shard |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `006360` | GS E&C | 2023-05-09 | 21,600 | 21,800 | 21,250 | 21,550 | 655,556 | 14,149,448,900 | 1,844,281,109,500 | 85,581,490 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv` |
| `006360` | GS E&C | 2023-10-20 | 13,260 | 13,470 | 12,930 | 13,370 | 562,200 | 7,416,786,850 | 1,144,224,521,300 | 85,581,490 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv` |
| `294870` | HDC Hyundai Development | 2022-03-30 | 15,200 | 17,550 | 15,150 | 15,700 | 6,306,714 | 101,820,639,850 | 1,034,745,081,000 | 65,907,330 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv` |
| `294870` | HDC Hyundai Development | 2025-05-26 | 25,750 | 25,800 | 23,250 | 23,550 | 570,339 | 13,748,928,425 | 1,552,117,621,500 | 65,907,330 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/294/294870/2025.csv` |
| `373220` | LG Energy Solution | 2025-01-31 | 353,500 | 356,500 | 346,500 | 352,000 | 147,908 | 51,977,272,500 | 82,368,000,000,000 | 234,000,000 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv` |
| `006400` | Samsung SDI | 2025-01-24 | 233,000 | 234,500 | 225,000 | 226,500 | 475,862 | 108,036,156,000 | 15,575,166,045,000 | 68,764,530 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv` |
| `020150` | LOTTE Energy Materials | 2025-05-09 | 22,800 | 22,800 | 22,000 | 22,000 | 71,322 | 1,581,745,725 | 1,152,040,186,000 | 52,365,463 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv` |
| `003670` | POSCO Future M | 2025-04-24 | 134,500 | 135,500 | 130,100 | 130,200 | 283,955 | 37,523,019,200 | 10,085,711,244,000 | 77,463,220 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/003/003670/2025.csv` |
| `024840` | KBI Metal | 2024-05-21 | 4,155 | 4,745 | 3,960 | 4,040 | 60,066,232 | 261,732,979,995 | 138,532,323,160 | 34,290,179 | KOSDAQ | `atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv` |
| `267260` | HD Hyundai Electric | 2025-04-22 | 329,000 | 333,500 | 300,000 | 301,000 | 706,084 | 221,732,415,500 | 10,850,187,635,000 | 36,047,135 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv` |
| `047400` | Union Materials | 2025-04-14 | 2,205 | 2,350 | 2,110 | 2,125 | 4,236,395 | 9,378,719,018 | 89,250,000,000 | 42,000,000 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/047/047400/2025.csv` |
| `005490` | POSCO Holdings | 2023-11-29 | 480,000 | 485,500 | 474,000 | 483,000 | 537,203 | 257,440,359,000 | 40,847,904,090,000 | 84,571,230 | KOSPI | `atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv` |

## 7. Forward Price Path Results

| # | symbol | company | source C | trigger | entry_date | entry c | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak | trough | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `006360` | GS E&C | C05 | Stage4C | 2023-05-09 | 21,550 | 2.78 / -4.64 | 2.78 / -37.96 | 2.78 / -41.21 | 2023-05-24 | 2023-10-10 | direct_quality_failure_hard_4c_positive_control |
| 2 | `006360` | GS E&C | C05 | Stage4B | 2023-10-20 | 13,370 | 30.14 / -4.41 | 30.14 / -4.41 | 30.14 / -4.41 | 2023-11-23 | 2023-10-24 | management_reset_offset_watch |
| 3 | `294870` | HDC Hyundai Development | C05 | Stage4C | 2022-03-30 | 15,700 | 11.78 / -11.78 | 11.78 / -33.44 | 11.78 / -37.77 | 2022-03-30 | 2022-10-27 | operating_permission_hard_4c_positive_control |
| 4 | `294870` | HDC Hyundai Development | C05 | Stage2-Actionable | 2025-05-26 | 23,550 | 18.26 / -8.07 | 18.26 / -18.17 | 18.26 / -22.93 | 2025-06-12 | 2025-11-07 | credit_recovery_reopen_control_with_mae_cap |
| 5 | `373220` | LG Energy Solution | C13 | Stage4B | 2025-01-31 | 352,000 | 9.80 / -7.67 | 9.80 / -24.43 | 44.89 / -24.43 | 2025-10-28 | 2025-05-23 | ugly_quarter_but_offset_quality_watch |
| 6 | `006400` | Samsung SDI | C13 | Stage4C | 2025-01-24 | 226,500 | 9.71 / -16.42 | 9.71 / -30.38 | 34.44 / -30.38 | 2025-10-27 | 2025-05-22 | hard_4c_with_nontrivial_offset_stress |
| 7 | `020150` | LOTTE Energy Materials | C13 | Stage4B | 2025-05-09 | 22,000 | 7.05 / -11.55 | 28.41 / -11.55 | 102.95 / -11.55 | 2025-11-25 | 2025-05-22 | inventory_adjustment_with_utilization_recovery_offset |
| 8 | `003670` | POSCO Future M | C13 | Stage2-Actionable | 2025-04-24 | 130,200 | 4.07 / -24.35 | 26.65 / -24.35 | 99.69 / -24.35 | 2025-10-27 | 2025-05-27 | direct_profit_reopen_high_mae_cap |
| 9 | `024840` | KBI Metal | C02 | Stage4B | 2024-05-21 | 4,040 | 17.45 / -36.14 | 17.45 / -46.16 | 17.45 / -58.74 | 2024-05-21 | 2025-01-03 | proxy_theme_overextension_counterexample |
| 10 | `267260` | HD Hyundai Electric | C02 | Stage2-Actionable | 2025-04-22 | 301,000 | 34.39 / -3.16 | 72.76 / -3.16 | 224.25 / -3.16 | 2025-11-04 | 2025-04-22 | direct_order_backlog_margin_positive_control |
| 11 | `047400` | Union Materials | C16 | Stage4B | 2025-04-14 | 2,125 | 10.59 / -25.88 | 10.59 / -27.53 | 26.12 / -40.24 | 2025-10-14 | 2025-12-26 | rare_earth_product_proxy_no_customer_pull |
| 12 | `005490` | POSCO Holdings | C16 | Stage4B | 2023-11-29 | 483,000 | 5.18 / -9.32 | 5.18 / -21.22 | 5.18 / -36.02 | 2023-12-27 | 2024-08-05 | long_lead_lithium_capacity_without_near_term_cashflow |

## 8. Residual Diagnosis

### 8.1 Hard 4C positive-control rows

`006360` on 2023-05-09 and `294870` on 2022-03-30 are direct C05 trust-break rows. The evidence is not “bad price action.” It is issuer/regulator-confirmed operating damage. The 180D paths then validate that hard 4C was protective.

`006400` on 2025-01-24 is deliberately kept as a stress row: the battery-loss language was severe, but the later path shows that ESS/JV offset quality mattered. This row teaches the opposite side of the same rule: a hard 4C label requires **weak or absent offset quality**, not just an ugly quarter.

### 8.2 Stage4B / watch rows with real offset quality

`006360` on 2023-10-20, `373220` on 2025-01-31, and `020150` on 2025-05-09 show why R13 should not let hard 4C become a one-way trapdoor. Management reset, ESS/non-EV offset, utilization recovery, customer inventory normalization, or North America OEM/JV routing can move a damaged thesis into local 4B/watch.

The mechanism is like a cracked pipe with a shutoff valve. The crack is real, so the system cannot run at full pressure. But once the valve is closed and the pressure is isolated, calling the whole building condemned is also wrong.

### 8.3 Stage2-Actionable reopen controls

`294870`, `003670`, and `267260` show that reopen is legitimate when the second bridge is direct: credit/financial improvement, profit rebound, order/backlog/margin conversion. R13 should not punish these rows just because their source archetype had prior 4B/4C stress.

However, Stage2-Actionable reopen is not Green. High MAE, absent FCF, or incomplete cash conversion still blocks Stage3-Green.

### 8.4 Proxy/theme/profile rows stay capped

`024840`, `047400`, and `005490` are useful because their themes are plausible but not sufficiently issuer-level. Copper-wire exposure, ferrite magnet exposure, and long-lead lithium capacity can all be real. They still do not equal customer pull, offtake, shipment, margin, or cashflow conversion. The correct R13 action is local 4B/watch or Stage2 cap, not Yellow/Green.

## 9. Current Calibrated Profile Stress Test

| symbol | trigger | score before | score after | delta | profile error / repair target |
| --- | --- | --- | --- | --- | --- |
| `006360` | Stage4C | 50 | 42 | -8 | hard_4c_too_late_if_waiting_for_formal_suspension |
| `006360` | Stage4B | 44 | 55 | 11 | overhard_4c_if_offset_quality_is_ignored |
| `294870` | Stage4C | 52 | 39 | -13 | hard_4c_should_not_wait_for_price_confirmation |
| `294870` | Stage2-Actionable | 58 | 72 | 14 | reopen_allowed_but_green_blocked_by_cashflow_gap |
| `373220` | Stage4B | 49 | 61 | 12 | hard_4c_false_positive_if_offset_quality_ignored |
| `006400` | Stage4C | 43 | 55 | 12 | overhard_4c_if_recovery_offset_is_ignored |
| `020150` | Stage4B | 52 | 66 | 14 | missed_reversible_4b_to_reopen_path |
| `003670` | Stage2-Actionable | 65 | 76 | 11 | actionable_reopen_missed_but_green_blocked_by_early_mae |
| `024840` | Stage4B | 66 | 45 | -21 | profile_or_theme_false_positive_if_not_routed_to_4b |
| `267260` | Stage2-Actionable | 70 | 82 | 12 | too_strict_if_direct_order_backlog_bridge_is_treated_like_theme_beta |
| `047400` | Stage4B | 67 | 48 | -19 | strategic_resource_theme_false_positive_without_issuer_bridge |
| `005490` | Stage4B | 64 | 49 | -15 | long_lead_capacity_false_positive_if_cashflow_bridge_missing |

Interpretation:

```text
preferred_rule_shape = R13_4B4C_OFFSET_QUALITY_AND_REOPEN_GATE_V2

hard_4c_when:
  - direct operating permission / quality / license / trust break is confirmed
  - utilization or margin thesis break is issuer-level and offset quality is weak
  - customer/order/backlog or cash-conversion damage is not merely price-implied

stage4b_watch_when:
  - ugly quarter exists but ESS / JV / customer / management / credit / utilization offset is visible
  - thesis is damaged but not irreversibly broken
  - evidence is profile/theme exposure after price extension

stage2_actionable_reopen_when:
  - damaged thesis has direct second bridge:
      credit improvement
      actual profit rebound
      utilization recovery
      order/backlog-to-revenue conversion
      margin/cash bridge

green_blocker_when:
  - 180D MAE <= -20% and cash/FCF bridge is absent
  - source row is proxy-theme/profile-only
  - offset is only narrative and not tied to issuer-level economics
```

## 10. Residual Contribution Summary

```text
rule_candidate = R13_4B4C_OFFSET_QUALITY_AND_REOPEN_GATE_V2
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

Residual contribution:

1. Hard 4C should be triggered by confirmed non-price thesis break, not by price drawdown alone.
2. Hard 4C should be delayed or softened when explicit offset quality is visible.
3. Stage4B/watch is the correct middle state for damaged-but-repairable theses.
4. Reopen to Stage2-Actionable is allowed only with a direct second bridge.
5. Profile/theme exposure can remain capped even if the later price path is strong.
6. Stage3-Green strictness should remain unchanged.

## 11. Shadow Rule Candidate

```yaml
shadow_rule_candidate:
  id: R13_4B4C_OFFSET_QUALITY_AND_REOPEN_GATE_V2
  scope:
    round: R13
    large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
    canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  production_scoring_changed: false
  shadow_weight_only: true
  do_not_propose_new_weight_delta: true
  hard_4c_positive_controls:
    - issuer_confirmed_quality_or_license_break
    - regulator_confirmed_operating_permission_damage
    - margin_or_utilization_thesis_break_with_weak_offset
  route_to_stage4b_watch:
    - management_reset_after_break
    - ESS_or_non_EV_or_JV_offset_after_battery_loss
    - customer_inventory_adjustment_with_utilization_recovery
    - proxy_theme_or_profile_exposure_after_extension
  route_to_stage2_actionable_reopen:
    - credit_or_financial_improvement_after_trust_break
    - direct_profit_reopen_after_materials_downcycle
    - order_backlog_sales_margin_bridge_after_grid_equipment_pull
  green_blockers:
    - 180d_MAE_below_minus_20_without_FCF_or_cash_bridge
    - proxy_theme_only
    - long_lead_capacity_without_near_term_cashflow
    - offset_quality_not_issuer_level
```

## 12. Machine-Readable JSONL Trigger Rows

```jsonl
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_01_006360_2023-05-09_Stage4C","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","source_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4C|2023-05-09","symbol":"006360","company":"GS E&C","market":"KOSPI","trigger_type":"Stage4C","trigger_date":"2023-05-09","entry_date":"2023-05-09","entry_price":21550.0,"actual_1d_ohlcv":{"d":"2023-05-09","o":21600.0,"h":21800.0,"l":21250.0,"c":21550.0,"v":655556,"a":14149448900.0,"mc":1844281109500.0,"s":85581490,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":2.78,"mae_30d_pct":-4.64,"mfe_90d_pct":2.78,"mae_90d_pct":-37.96,"mfe_180d_pct":2.78,"mae_180d_pct":-41.21,"peak_180d_date":"2023-05-24","peak_180d_price":22150.0,"trough_180d_date":"2023-10-10","drawdown_after_peak_pct":-42.8},"evidence_family":"construction_quality_admission_missing_rebar","evidence_summary":"Issuer-confirmed construction-quality failure at Geomdan apartment parking-lot collapse; missing rebar / faulty construction is direct non-price thesis-break evidence.","evidence_url":"https://www.koreatimes.co.kr/business/companies/20230509/gs-ec-admits-to-faulty-construction-of-apartment-underground-parking-lot-in-incheon","case_role":"direct_quality_failure_hard_4c_positive_control","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":50,"weighted_score_after":42,"current_profile_error":"hard_4c_too_late_if_waiting_for_formal_suspension","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006360|Stage4C|2023-05-09","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006360|Stage4C|2023-05-09"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_02_006360_2023-10-20_Stage4B","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","source_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4B|2023-10-20","symbol":"006360","company":"GS E&C","market":"KOSPI","trigger_type":"Stage4B","trigger_date":"2023-10-20","entry_date":"2023-10-20","entry_price":13370.0,"actual_1d_ohlcv":{"d":"2023-10-20","o":13260.0,"h":13470.0,"l":12930.0,"c":13370.0,"v":562200,"a":7416786850.0,"mc":1144224521300.0,"s":85581490,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","profile_path":"atlas/symbol_profiles/006/006360.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":30.14,"mae_30d_pct":-4.41,"mfe_90d_pct":30.14,"mae_90d_pct":-4.41,"mfe_180d_pct":30.14,"mae_180d_pct":-4.41,"peak_180d_date":"2023-11-23","peak_180d_price":17400.0,"trough_180d_date":"2023-10-24","drawdown_after_peak_pct":-26.55},"evidence_family":"ceo_change_brand_repair_after_quality_failure","evidence_summary":"Management reset after the quality scandal is non-price offset/watch evidence; it should split later repair state from the original hard 4C event.","evidence_url":"https://www.koreatimes.co.kr/business/companies/20231020/gs-ec-replaces-ceo-with-owners-son","case_role":"management_reset_offset_watch","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":44,"weighted_score_after":55,"current_profile_error":"overhard_4c_if_offset_quality_is_ignored","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006360|Stage4B|2023-10-20","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006360|Stage4B|2023-10-20"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_03_294870_2022-03-30_Stage4C","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","source_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage4C|2022-03-30","symbol":"294870","company":"HDC Hyundai Development","market":"KOSPI","trigger_type":"Stage4C","trigger_date":"2022-03-30","entry_date":"2022-03-30","entry_price":15700.0,"actual_1d_ohlcv":{"d":"2022-03-30","o":15200.0,"h":17550.0,"l":15150.0,"c":15700.0,"v":6306714,"a":101820639850.0,"mc":1034745081000.0,"s":65907330,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":11.78,"mae_30d_pct":-11.78,"mfe_90d_pct":11.78,"mae_90d_pct":-33.44,"mfe_180d_pct":11.78,"mae_180d_pct":-37.77,"peak_180d_date":"2022-03-30","peak_180d_price":17550.0,"trough_180d_date":"2022-10-27","drawdown_after_peak_pct":-44.33},"evidence_family":"business_suspension_license_risk","evidence_summary":"Business suspension and license risk after fatal construction collapse are direct operating-permission damage; hard 4C should override order headlines.","evidence_url":"https://koreajoongangdaily.joins.com/2022/03/30/business/industry/HDC-Building-collapse-Gwangju/20220330162503613.html","case_role":"operating_permission_hard_4c_positive_control","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":52,"weighted_score_after":39,"current_profile_error":"hard_4c_should_not_wait_for_price_confirmation","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|294870|Stage4C|2022-03-30","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|294870|Stage4C|2022-03-30"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_04_294870_2025-05-26_Stage2_Actionable","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_205_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","source_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|294870|Stage2-Actionable|2025-05-26","symbol":"294870","company":"HDC Hyundai Development","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_date":"2025-05-26","entry_date":"2025-05-26","entry_price":23550.0,"actual_1d_ohlcv":{"d":"2025-05-26","o":25750.0,"h":25800.0,"l":23250.0,"c":23550.0,"v":570339,"a":13748928425.0,"mc":1552117621500.0,"s":65907330,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2025.csv","profile_path":"atlas/symbol_profiles/294/294870.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":18.26,"mae_30d_pct":-8.07,"mfe_90d_pct":18.26,"mae_90d_pct":-18.17,"mfe_180d_pct":18.26,"mae_180d_pct":-22.93,"peak_180d_date":"2025-06-12","peak_180d_price":27850.0,"trough_180d_date":"2025-11-07","drawdown_after_peak_pct":-34.83},"evidence_family":"credit_rating_financial_improvement_recovery","evidence_summary":"Credit-rating / financial-improvement recognition reopens a damaged construction thesis, but high MAE keeps Yellow/Green blocked until cash conversion is visible.","evidence_url":"https://biz.chosun.com/en/en-realestate/2025/05/26/4XWZSHVIIND6HO5MXQE5SYR43E/","case_role":"credit_recovery_reopen_control_with_mae_cap","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":58,"weighted_score_after":72,"current_profile_error":"reopen_allowed_but_green_blocked_by_cashflow_gap","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|294870|Stage2-Actionable|2025-05-26","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|294870|Stage2-Actionable|2025-05-26"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_05_373220_2025-01-31_Stage4B","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_203_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage4B|2025-01-31","symbol":"373220","company":"LG Energy Solution","market":"KOSPI","trigger_type":"Stage4B","trigger_date":"2025-01-31","entry_date":"2025-01-31","entry_price":352000.0,"actual_1d_ohlcv":{"d":"2025-01-31","o":353500.0,"h":356500.0,"l":346500.0,"c":352000.0,"v":147908,"a":51977272500.0,"mc":82368000000000.0,"s":234000000,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv","profile_path":"atlas/symbol_profiles/373/373220.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":9.8,"mae_30d_pct":-7.67,"mfe_90d_pct":9.8,"mae_90d_pct":-24.43,"mfe_180d_pct":44.89,"mae_180d_pct":-24.43,"peak_180d_date":"2025-10-28","peak_180d_price":510000.0,"trough_180d_date":"2025-05-23","drawdown_after_peak_pct":-17.25},"evidence_family":"ex_AMPC_loss_lower_utilization_capex_cut_with_ESS_offset","evidence_summary":"FY2024/Q4 loss and AMPC dependence were ugly, but ESS/new-chemistry/order-processing offsets argue for 4B/watch before hard 4C.","evidence_url":"https://www.lgcorp.com/media/release/28617","case_role":"ugly_quarter_but_offset_quality_watch","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":49,"weighted_score_after":61,"current_profile_error":"hard_4c_false_positive_if_offset_quality_ignored","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|373220|Stage4B|2025-01-31","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|373220|Stage4B|2025-01-31"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_06_006400_2025-01-24_Stage4C","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_203_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage4C|2025-01-24","symbol":"006400","company":"Samsung SDI","market":"KOSPI","trigger_type":"Stage4C","trigger_date":"2025-01-24","entry_date":"2025-01-24","entry_price":226500.0,"actual_1d_ohlcv":{"d":"2025-01-24","o":233000.0,"h":234500.0,"l":225000.0,"c":226500.0,"v":475862,"a":108036156000.0,"mc":15575166045000.0,"s":68764530,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv","profile_path":"atlas/symbol_profiles/006/006400.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":9.71,"mae_30d_pct":-16.42,"mfe_90d_pct":9.71,"mae_90d_pct":-30.38,"mfe_180d_pct":34.44,"mae_180d_pct":-30.38,"peak_180d_date":"2025-10-27","peak_180d_price":304500.0,"trough_180d_date":"2025-05-22","drawdown_after_peak_pct":-10.18},"evidence_family":"battery_loss_customer_inventory_ESS_JV_offset","evidence_summary":"Battery operating loss and customer inventory adjustment fit hard-break language, but ESS record revenue and U.S. JV progress mean weak-offset quality must be proven before hard 4C is final.","evidence_url":"https://www.businesskorea.co.kr/news/articleView.html?idxno=234435","case_role":"hard_4c_with_nontrivial_offset_stress","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":43,"weighted_score_after":55,"current_profile_error":"overhard_4c_if_recovery_offset_is_ignored","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006400|Stage4C|2025-01-24","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006400|Stage4C|2025-01-24"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_07_020150_2025-05-09_Stage4B","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_203_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|020150|Stage4B|2025-05-09","symbol":"020150","company":"LOTTE Energy Materials","market":"KOSPI","trigger_type":"Stage4B","trigger_date":"2025-05-09","entry_date":"2025-05-09","entry_price":22000.0,"actual_1d_ohlcv":{"d":"2025-05-09","o":22800.0,"h":22800.0,"l":22000.0,"c":22000.0,"v":71322,"a":1581745725.0,"mc":1152040186000.0,"s":52365463,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv","profile_path":"atlas/symbol_profiles/020/020150.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":7.05,"mae_30d_pct":-11.55,"mfe_90d_pct":28.41,"mae_90d_pct":-11.55,"mfe_180d_pct":102.95,"mae_180d_pct":-11.55,"peak_180d_date":"2025-11-25","peak_180d_price":44650.0,"trough_180d_date":"2025-05-22","drawdown_after_peak_pct":-13.1},"evidence_family":"copper_foil_customer_inventory_adjustment_utilization_recovery_guidance","evidence_summary":"Shipment reduction and customer inventory adjustment were negative, but stated utilization recovery and North America OEM/JV route make this reversible 4B/watch.","evidence_url":"https://www.lotteenergymaterials.com/en/pr/promotion_detail.do?seq=138","case_role":"inventory_adjustment_with_utilization_recovery_offset","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":52,"weighted_score_after":66,"current_profile_error":"missed_reversible_4b_to_reopen_path","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|020150|Stage4B|2025-05-09","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|020150|Stage4B|2025-05-09"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_08_003670_2025-04-24_Stage2_Actionable","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_203_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_duplicate_key":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|003670|Stage2-Actionable|2025-04-24","symbol":"003670","company":"POSCO Future M","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-24","entry_date":"2025-04-24","entry_price":130200.0,"actual_1d_ohlcv":{"d":"2025-04-24","o":134500.0,"h":135500.0,"l":130100.0,"c":130200.0,"v":283955,"a":37523019200.0,"mc":10085711244000.0,"s":77463220,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2025.csv","profile_path":"atlas/symbol_profiles/003/003670.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":4.07,"mae_30d_pct":-24.35,"mfe_90d_pct":26.65,"mae_90d_pct":-24.35,"mfe_180d_pct":99.69,"mae_180d_pct":-24.35,"peak_180d_date":"2025-10-27","peak_180d_price":260000.0,"trough_180d_date":"2025-05-27","drawdown_after_peak_pct":-19.0},"evidence_family":"q1_profit_reopen_cathode_materials_turnaround","evidence_summary":"Q1 2025 revenue/profit rebound is a direct reopen bridge after a weak battery-material year, but high MAE keeps Yellow/Green capped.","evidence_url":"https://www.poscofuturem.com/en/pr/list.do?m=04&topic=18&y=2025","case_role":"direct_profit_reopen_high_mae_cap","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":65,"weighted_score_after":76,"current_profile_error":"actionable_reopen_missed_but_green_blocked_by_early_mae","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|003670|Stage2-Actionable|2025-04-24","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|003670|Stage2-Actionable|2025-04-24"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_09_024840_2024-05-21_Stage4B","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_duplicate_key":"C02_POWER_GRID_DATACENTER_CAPEX|024840|Stage4B|2024-05-21","symbol":"024840","company":"KBI Metal","market":"KOSDAQ","trigger_type":"Stage4B","trigger_date":"2024-05-21","entry_date":"2024-05-21","entry_price":4040.0,"actual_1d_ohlcv":{"d":"2024-05-21","o":4155.0,"h":4745.0,"l":3960.0,"c":4040.0,"v":60066232,"a":261732979995.0,"mc":138532323160.0,"s":34290179,"m":"KOSDAQ"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/024/024840/2024.csv","profile_path":"atlas/symbol_profiles/024/024840.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":17.45,"mae_30d_pct":-36.14,"mfe_90d_pct":17.45,"mae_90d_pct":-46.16,"mfe_180d_pct":17.45,"mae_180d_pct":-58.74,"peak_180d_date":"2024-05-21","peak_180d_price":4745.0,"trough_180d_date":"2025-01-03","drawdown_after_peak_pct":-64.87},"evidence_family":"copper_wire_power_grid_theme_no_company_order_bridge","evidence_summary":"Copper-wire/power-line theme exposure without customer-specific grid order/backlog bridge; this is local 4B/proxy-theme overextension.","evidence_url":"https://www.asiae.co.kr/en/article/2024041910590184215","case_role":"proxy_theme_overextension_counterexample","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":66,"weighted_score_after":45,"current_profile_error":"profile_or_theme_false_positive_if_not_routed_to_4b","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|024840|Stage4B|2024-05-21","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|024840|Stage4B|2024-05-21"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_10_267260_2025-04-22_Stage2_Actionable","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_204_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_duplicate_key":"C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage2-Actionable|2025-04-22","symbol":"267260","company":"HD Hyundai Electric","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-22","entry_date":"2025-04-22","entry_price":301000.0,"actual_1d_ohlcv":{"d":"2025-04-22","o":329000.0,"h":333500.0,"l":300000.0,"c":301000.0,"v":706084,"a":221732415500.0,"mc":10850187635000.0,"s":36047135,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv","profile_path":"atlas/symbol_profiles/267/267260.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":34.39,"mae_30d_pct":-3.16,"mfe_90d_pct":72.76,"mae_90d_pct":-3.16,"mfe_180d_pct":224.25,"mae_180d_pct":-3.16,"peak_180d_date":"2025-11-04","peak_180d_price":976000.0,"trough_180d_date":"2025-04-22","drawdown_after_peak_pct":-24.59},"evidence_family":"orders_backlog_sales_operating_profit_margin_bridge","evidence_summary":"Orders, backlog, sales, operating profit and North-America profitability form a direct grid equipment bridge; this should not be penalized like proxy-theme 4B rows.","evidence_url":"https://en.yna.co.kr/view/AEN20250422006151320","case_role":"direct_order_backlog_margin_positive_control","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":70,"weighted_score_after":82,"current_profile_error":"too_strict_if_direct_order_backlog_bridge_is_treated_like_theme_beta","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|267260|Stage2-Actionable|2025-04-22","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|267260|Stage2-Actionable|2025-04-22"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_11_047400_2025-04-14_Stage4B","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_205_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md","source_duplicate_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|047400|Stage4B|2025-04-14","symbol":"047400","company":"Union Materials","market":"KOSPI","trigger_type":"Stage4B","trigger_date":"2025-04-14","entry_date":"2025-04-14","entry_price":2125.0,"actual_1d_ohlcv":{"d":"2025-04-14","o":2205.0,"h":2350.0,"l":2110.0,"c":2125.0,"v":4236395,"a":9378719018.0,"mc":89250000000.0,"s":42000000,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047400/2025.csv","profile_path":"atlas/symbol_profiles/047/047400.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":10.59,"mae_30d_pct":-25.88,"mfe_90d_pct":10.59,"mae_90d_pct":-27.53,"mfe_180d_pct":26.12,"mae_180d_pct":-40.24,"peak_180d_date":"2025-10-14","peak_180d_price":2680.0,"trough_180d_date":"2025-12-26","drawdown_after_peak_pct":-51.87},"evidence_family":"rare_earth_export_control_ferrite_magnet_proxy","evidence_summary":"Ferrite magnet / rare-earth substitute theme is real product exposure, but the as-of evidence lacks customer pull, shipment, ASP, margin, or offtake bridge.","evidence_url":"https://www.mk.co.kr/en/stock/11290565","case_role":"rare_earth_product_proxy_no_customer_pull","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":67,"weighted_score_after":48,"current_profile_error":"strategic_resource_theme_false_positive_without_issuer_bridge","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|047400|Stage4B|2025-04-14","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|047400|Stage4B|2025-04-14"}
{"schema_version":"e2r_v12_trigger_row_v1","row_type":"trigger","source_row_type":"r13_cross_case","row_id":"R13_L202_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_12_005490_2023-11-29_Stage4B","research_file":"e2r_stock_web_v12_residual_round_R13_loop_202_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md","selected_round":"R13","selected_loop":202,"round":"R13","loop":202,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"R13_4B_4C_OFFSET_QUALITY_REFRESH_FROM_RECENT_HOLDOUTS","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_205_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md","source_duplicate_key":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|005490|Stage4B|2023-11-29","symbol":"005490","company":"POSCO Holdings","market":"KOSPI","trigger_type":"Stage4B","trigger_date":"2023-11-29","entry_date":"2023-11-29","entry_price":483000.0,"actual_1d_ohlcv":{"d":"2023-11-29","o":480000.0,"h":485500.0,"l":474000.0,"c":483000.0,"v":537203,"a":257440359000.0,"mc":40847904090000.0,"s":84571230,"m":"KOSPI"},"price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv","profile_path":"atlas/symbol_profiles/005/005490.json","corporate_action_contamination_180D":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"mfe_mae":{"method":"entry close vs max high / min low over inclusive N-tradable-row windows","mfe_30d_pct":5.18,"mae_30d_pct":-9.32,"mfe_90d_pct":5.18,"mae_90d_pct":-21.22,"mfe_180d_pct":5.18,"mae_180d_pct":-36.02,"peak_180d_date":"2023-12-27","peak_180d_price":508000.0,"trough_180d_date":"2024-08-05","drawdown_after_peak_pct":-39.17},"evidence_family":"lithium_hydroxide_capacity_long_lead_resource_bridge","evidence_summary":"Lithium hydroxide facility opening is company-specific strategic-resource capacity, but near-term offtake/margin/cashflow conversion was not visible at entry.","evidence_url":"https://www.pls.com/news-stories/posco-pilbara-minerals-jv-opens-south-korean-lithium-hydroxide-facility/","case_role":"long_lead_lithium_capacity_without_near_term_cashflow","score_simulation":{"current_profile_proxy":"e2r_2_2_rolling_calibrated","weighted_score_before":64,"weighted_score_after":49,"current_profile_error":"long_lead_capacity_false_positive_if_cashflow_bridge_missing","production_scoring_changed":false,"shadow_weight_only":true,"stage3_green_blocked":true},"residual_contribution":{"label":"R13_4B4C_offset_quality_refresh","representative_for_aggregate":true,"new_independent_trigger_for_r13_scope":true,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"shadow_weight_only":true},"duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|005490|Stage4B|2023-11-29","hard_duplicate_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|005490|Stage4B|2023-11-29"}
```

## 13. Batch Ingest Self-Audit

```text
standard_v12_filename = pass
filename_regex_pass = true
metadata_round_matches_filename = true
metadata_loop_matches_filename = true
round_sector_consistency = pass
R13_large_sector_L10_only = pass

must_use_actual_stock_web_1D_OHLC = pass
entry_price_present_all_rows = true
actual_1d_ohlcv_present_all_rows = true
mfe_mae_30_90_180_present_all_rows = true
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0

stock_agent_code_accessed = false
stock_agent_code_patched = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false

new_independent_ratio_for_r13_scope = 1.00
source_proxy_only_count = 2
evidence_url_pending_count = 0
ready_for_batch_ingest = true
```

## 14. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research session. It is a later batch-implementation handoff only.

```text
Read this MD as a v12 R13 cross-archetype residual calibration artifact.
Do not infer a production patch from any single row.
If batch evidence supports it, consider a cross-archetype guardrail named:
R13_4B4C_OFFSET_QUALITY_AND_REOPEN_GATE_V2

Scope:
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM only
- Use as validation logic / review summary first
- Do not loosen Stage3-Green
- Do not change production scoring unless the aggregate v12 calibration pipeline promotes the same axis

Implementation idea:
- hard 4C requires confirmed non-price thesis break plus weak offset quality
- Stage4B/watch absorbs damaged but repairable evidence packets
- Stage2-Actionable reopen requires direct second bridge
- proxy/theme/profile rows stay capped without issuer-level conversion
```

## 15. Next Research State

```text
completed_round = R13
completed_loop = 202
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 R13 quality refresh / 4B-4C offset-quality cleanup
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

next_recommended_archetypes:
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
