# E2R Stock-Web v12 Residual Research — R13 / Loop 197 / Stage2 False Positive Taxonomy
```text
research_file = e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
selected_round = R13
selected_loop = 197
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 over-covered R13 taxonomy cleanup / direct URL quality check
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id = R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```
## 1. Execution Boundary
This is not a live scan, not a stock_agent code patch, and not a production scoring change. The only output is this standalone historical calibration Markdown file. The research objective is R13 cross-archetype Stage2 false-positive taxonomy repair: identify which single-variable headlines should remain Stage2 watch only, and which direct conversion bridges protect true Stage2-Actionable cases.
## 2. Source / Price Atlas Validation
```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
missing_required_mfe_mae_count = 0
```
The selected trigger rows use actual stock-web 1D OHLC rows. Where local stock-web CSV shards were available in this session, 30/90/180D MFE/MAE were recomputed from those shards; all rows retain the stock-web shard path and profile path for later batch validation.
## 3. No-Repeat / Coverage Selection
NO-REPEAT INDEX was used only as the duplicate ledger. The cumulative ledger says the corpus is no longer in 30/50/80-row fill mode; the next useful R13 work is direct URL/proxy quality and false-positive taxonomy. This loop therefore avoids the already-completed R13 high-MAE and 4B/4C boundary files from this session and creates the first local R13 `STAGE2_FALSE_POSITIVE_REVIEW` file with a new R13 duplicate key family.
```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
new_r13_duplicate_keys = 9
reused_source_sector_case_count = 9
new_independent_case_count_for_R13_scope = 9
source_proxy_only_count = 0
evidence_url_pending_count = 0
new_independent_ratio = 1.00
```
## 4. Case Selection
| # | source canonical | symbol | company | trigger | entry | taxonomy | 180D MFE / MAE | role |
|---:|---|---:|---|---|---|---|---:|---|
| 1 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 006400 | Samsung SDI | Stage2 | 2023-04-26 | long_lead_JV_or_capex_without_utilization | 5.97 / -47.72 | counterexample |
| 2 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 096770 | SK Innovation | Stage2 | 2023-07-28 | loss_narrowing_without_positive_unit_economics | 19.79 / -45.86 | counterexample |
| 3 | C15_MATERIAL_SPREAD_SUPERCYCLE | 004020 | Hyundai Steel | Stage2 | 2021-04-27 | commodity_profit_swing_without_forward_spread_duration | 11.11 / -34.66 | counterexample |
| 4 | C15_MATERIAL_SPREAD_SUPERCYCLE | 010950 | S-Oil | Stage2-Actionable | 2022-07-28 | inventory_gain_or_windfall_without_persistence | 18.84 / -17.63 | counterexample |
| 5 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 319660 | PSK | Stage2 | 2024-04-25 | customer_capex_beta_without_supplier_order_conversion | 29.90 / -48.34 | counterexample |
| 6 | C15_MATERIAL_SPREAD_SUPERCYCLE | 103140 | Poongsan | Stage2-Actionable | 2024-05-16 | commodity_price_headline_without_company_volume_margin_bridge | 0.91 / -40.30 | counterexample |
| 7 | C02_POWER_GRID_DATACENTER_CAPEX | 298040 | Hyosung Heavy Industries | Stage2-Actionable | 2025-04-29 | positive_control_direct_backlog_margin_revenue_bridge | 377.50 / -6.35 | positive_control |
| 8 | C02_POWER_GRID_DATACENTER_CAPEX | 010120 | LS ELECTRIC | Stage2-Actionable | 2025-04-22 | positive_control_direct_us_grid_order_backlog | 220.97 / -0.41 | positive_control |
| 9 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 003670 | POSCO Future M | Stage2-Actionable | 2023-06-02 | positive_control_direct_customer_capacity_but_green_block_needed | 85.56 / -38.10 | positive_control_high_mae |
## 5. Actual 1D OHLC / MFE-MAE Table
| symbol | entry_date | entry_price | o | h | l | c | v | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | drawdown after peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 006400 | 2023-04-26 | 703000.00 | 707000.00 | 721000.00 | 701000.00 | 703000.00 | 220437 | 5.97 / -6.83 | 5.97 / -17.07 | 5.97 / -47.72 | 2023-06-12 @ 745000.00 | -50.67 |
| 096770 | 2023-07-28 | 189500.00 | 182500.00 | 191700.00 | 182200.00 | 189500.00 | 1384523 | 19.79 / -10.77 | 19.79 / -36.62 | 19.79 / -45.86 | 2023-08-01 @ 227000.00 | -54.80 |
| 004020 | 2021-04-27 | 56700.00 | 52600.00 | 57000.00 | 52400.00 | 56700.00 | 5322376 | 11.11 / -10.76 | 11.11 / -20.19 | 11.11 / -34.66 | 2021-05-11 @ 63000.00 | -41.19 |
| 010950 | 2022-07-28 | 91300.00 | 93600.00 | 93800.00 | 90500.00 | 91300.00 | 538463 | 18.84 / -7.12 | 18.84 / -15.12 | 18.84 / -17.63 | 2022-08-30 @ 108500.00 | -30.69 |
| 319660 | 2024-04-25 | 30100.00 | 29900.00 | 30900.00 | 29850.00 | 30100.00 | 242835 | 14.45 / -8.64 | 29.90 / -24.58 | 29.90 / -48.34 | 2024-07-11 @ 39100.00 | -60.23 |
| 103140 | 2024-05-16 | 77300.00 | 78000.00 | 78000.00 | 74400.00 | 77300.00 | 562357 | 0.91 / -28.07 | 0.91 / -39.20 | 0.91 / -40.30 | 2024-05-16 @ 78000.00 | -40.83 |
| 298040 | 2025-04-29 | 520000.00 | 492000.00 | 522000.00 | 487000.00 | 520000.00 | 92036 | 49.04 / -6.35 | 160.77 / -6.35 | 377.50 / -6.35 | 2025-11-04 @ 2483000.00 | -30.29 |
| 010120 | 2025-04-22 | 172600.00 | 173700.00 | 179400.00 | 171900.00 | 172600.00 | 340505 | 54.84 / -0.41 | 93.51 / -0.41 | 220.97 / -0.41 | 2026-01-14 @ 554000.00 | -10.20 |
| 003670 | 2023-06-02 | 374000.00 | 361500.00 | 381500.00 | 358500.00 | 374000.00 | 1467089 | 12.30 / -7.89 | 85.56 / -16.18 | 85.56 / -38.10 | 2023-07-26 @ 694000.00 | -66.64 |
## 6. Stage2 False-Positive Taxonomy
The repeated error is not simply that Stage2 is early. Stage2 is supposed to be early. The error is **single-variable elevation**: the model sees one shiny object and mistakes it for a bridge. A Stage2 headline becomes false-positive-prone when it has only one of the following and lacks a second conversion proof.
| taxonomy | false-positive mechanism | required second bridge before Actionable/Yellow | representative rows |
|---|---|---|---|
| long_lead_JV_or_capex_without_utilization | announced capacity is temporally far from eligible volume | utilization, customer call-off, shipment schedule, ex-subsidy margin | 006400, 096770 |
| commodity_profit_swing_without_forward_spread_duration | earnings spike arrives after spread/stock peak | forward spread duration, cost pass-through, order/sell-through visibility | 004020, 010950, 103140 |
| customer_capex_beta_without_supplier_order_conversion | customer capex is mapped to supplier revenue too quickly | supplier order, backlog, revenue conversion, customer allocation | 319660 |
| direct_backlog_margin_revenue_bridge | positive control, not a false positive | company-specific order/backlog + margin/revenue recognition | 298040, 010120 |
| direct_customer_capacity_high_MAE | positive but volatile; blocks Green, not Stage2 | customer/capacity evidence + timeboxed risk control | 003670 |
## 7. Current Calibrated Profile Stress Test
| profile | scope | eligible | selected | avg 90D MFE/MAE | avg 180D MFE/MAE | false positive rate | missed structural | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 9 | 9 | 47.37 / -19.52 | 85.62 / -31.04 | 0.667 | 2 | mixed; false-positive cluster visible |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 9 | 9 | 47.37 / -19.52 | 85.62 / -31.04 | 0.75 | 1 | worse false-positive profile |
| P1_R13_stage2_single_variable_headline_guard | cross_archetype_guard | 9 | 3 | 113.28 / -7.65 | 228.01 / -14.95 | 0.0 | 0 | best alignment but must not block high-MAE true winners |
| P2_canonical_bridge_taxonomy_profile | canonical_archetype_specific | 9 | 5 | 78.73 / -11.78 | 148.57 / -20.37 | 0.2 | 0 | preferred R13 taxonomy, no immediate production delta |
| P3_counterexample_guard_profile | guardrail_only | 9 | 3 | 113.28 / -7.65 | 228.01 / -14.95 | 0.0 | 1 | safe but possibly too conservative for early structural high-MAE winners |
### Applied-axis audit
```text
existing_axis_tested:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

existing_axis_strengthened:
- stage2_actionable_evidence_bonus should require second-bridge evidence in R13 taxonomy labels
- price_only_blowoff_blocks_positive_stage remains useful for commodity/capex beta entries

existing_axis_weakened:
- none

existing_axis_kept:
- Green strictness remains intact; high-MAE true winners should be Green-blocked rather than Stage2-blocked

new_axis_proposed: false
```
## 8. Case Notes
### 1. 006400 Samsung SDI — long_lead_JV_or_capex_without_utilization
- Source canonical: `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` / source file: `e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md`.
- Evidence URL: https://www.samsungsdi.com/sdi-now/sdi-news/3162.html?idx=3162&pageIndex=2&pagesize=15
- Evidence summary: Samsung SDI and GM announced a prospective US battery-cell JV with over $3B investment and more than 30GWh annual capacity, but mass production was only targeted for 2026, so the trigger lacked near-term utilization and margin conversion.
- Price result: 30D `5.97/-6.83`, 90D `5.97/-17.07`, 180D `5.97/-47.72`.
- Stress-test verdict: `current_profile_false_positive`. Long-lead JV capacity was treated like current utilization. The price path had only +5.97% 180D MFE and -47.72% 180D MAE.
### 2. 096770 SK Innovation — loss_narrowing_without_positive_unit_economics
- Source canonical: `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` / source file: `e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md`.
- Evidence URL: https://en.yna.co.kr/view/AEN20230728002051320
- Evidence summary: SK Innovation swung to red in Q2 2023 on falling oil prices; the battery loss-narrowing interpretation was insufficient as a utilization conversion proof.
- Price result: 30D `19.79/-10.77`, 90D `19.79/-36.62`, 180D `19.79/-45.86`.
- Stress-test verdict: `current_profile_false_positive`. Loss narrowing was not the same as positive unit economics. 180D MFE stayed below 20% while MAE reached -45.86%.
### 3. 004020 Hyundai Steel — commodity_profit_swing_without_forward_spread_duration
- Source canonical: `C15_MATERIAL_SPREAD_SUPERCYCLE` / source file: `e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md`.
- Evidence URL: https://en.yna.co.kr/view/AEN20210427007052320
- Evidence summary: Hyundai Steel swung to profit in Q1 2021 on robust demand and steel price strength, but the entry was already late in the spread/stock cycle.
- Price result: 30D `11.11/-10.76`, 90D `11.11/-20.19`, 180D `11.11/-34.66`.
- Stress-test verdict: `current_profile_false_positive`. A profit swing from price/spread expansion did not carry forward duration evidence. 180D MFE was +11.11% while 180D MAE was -34.66%.
### 4. 010950 S-Oil — inventory_gain_or_windfall_without_persistence
- Source canonical: `C15_MATERIAL_SPREAD_SUPERCYCLE` / source file: `e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md`.
- Evidence URL: https://en.yna.co.kr/view/AEN20220728002252320
- Evidence summary: S-Oil Q2 2022 profit was driven by widened refining margins and inventory gains; the windfall was real but did not prove full-window spread persistence.
- Price result: 30D `18.84/-7.12`, 90D `18.84/-15.12`, 180D `18.84/-17.63`.
- Stress-test verdict: `current_profile_too_early`. This was not a zero signal, but Stage2-Actionable/Yellow over-promotion would be false. 180D MFE was +18.84%; drawdown after peak reached -30.69%.
### 5. 319660 PSK — customer_capex_beta_without_supplier_order_conversion
- Source canonical: `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` / source file: `e2r_stock_web_v12_residual_round_R2_loop_192_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md`.
- Evidence URL: https://www.pskinc.com/ir/financial_summary.php ; https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/
- Evidence summary: SK Hynix recovery/capex evidence was strong at customer level, while PSK supplier-level order conversion was not yet directly proven; PSK official financial summary is used as direct company context.
- Price result: 30D `14.45/-8.64`, 90D `29.90/-24.58`, 180D `29.90/-48.34`.
- Stress-test verdict: `current_profile_false_positive`. Customer capex beta was not supplier order conversion. 90D MFE was good at +29.90%, but 180D MAE was -48.34%.
### 6. 103140 Poongsan — commodity_price_headline_without_company_volume_margin_bridge
- Source canonical: `C15_MATERIAL_SPREAD_SUPERCYCLE` / source file: `e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md`.
- Evidence URL: https://v.daum.net/v/fXzID0JqJ6?f=p ; https://poongsan.co.kr/en/ir/financial/information
- Evidence summary: Copper-price and defense optimism created a plausible Stage2 story, but the entry lacked direct forward volume/margin bridge strong enough to justify Actionable promotion.
- Price result: 30D `0.91/-28.07`, 90D `0.91/-39.20`, 180D `0.91/-40.30`.
- Stress-test verdict: `current_profile_false_positive`. Entry was essentially the local peak. 180D MFE was only +0.91%, while 30D/90D/180D MAE reached -28.07%/-39.20%/-40.30%.
### 7. 298040 Hyosung Heavy Industries — positive_control_direct_backlog_margin_revenue_bridge
- Source canonical: `C02_POWER_GRID_DATACENTER_CAPEX` / source file: `e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md`.
- Evidence URL: https://securities.miraeasset.com/bbs/download/2135886.pdf?attachmentId=2135886
- Evidence summary: 1Q25 coverage showed heavy-industry backlog, new orders, high-value project revenue recognition, and improving overseas margins.
- Price result: 30D `49.04/-6.35`, 90D `160.77/-6.35`, 180D `377.50/-6.35`.
- Stress-test verdict: `current_profile_missed_structural`. Positive control: this is what a non-false Stage2-Actionable looks like. 180D MFE was +377.50% with only -6.35% MAE.
### 8. 010120 LS ELECTRIC — positive_control_direct_us_grid_order_backlog
- Source canonical: `C02_POWER_GRID_DATACENTER_CAPEX` / source file: `e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md`.
- Evidence URL: https://www.ls-electric.com/ko/company/data/25_1Q_Results.pdf
- Evidence summary: LS ELECTRIC 1Q25 result material showed HVTR/SWGR order/backlog reacceleration and US/grid-related visibility.
- Price result: 30D `54.84/-0.41`, 90D `93.51/-0.41`, 180D `220.97/-0.41`.
- Stress-test verdict: `current_profile_correct`. Positive control: direct order/backlog visibility separated this from generic grid beta. 180D MFE was +220.97% and 180D MAE was only -0.41%.
### 9. 003670 POSCO Future M — positive_control_direct_customer_capacity_but_green_block_needed
- Source canonical: `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` / source file: `e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md`.
- Evidence URL: https://www.poscofuturem.com/en/pr/view.do?num=695 ; https://news.gm.com/home.detail.html/Pages/news/us/en/2023/jun/0602-posco.html
- Evidence summary: POSCO Future M and GM expanded an integrated CAM/precursor complex tied to the Ultium battery supply chain, providing direct customer/capacity evidence.
- Price result: 30D `12.30/-7.89`, 90D `85.56/-16.18`, 180D `85.56/-38.10`.
- Stress-test verdict: `current_profile_missed_structural_if_capacity_not_mapped_but_green_block_correct`. Positive control with risk: high MAE does not make initial Stage2 false when direct customer/capacity evidence is real; it should block Green, not the initial Stage2.
## 9. Score Component Breakdown
### 006400 Samsung SDI
```json
{
  "symbol": "006400",
  "component_breakdown_required": true,
  "raw_component_scores_before": {
    "contract_score": 58,
    "backlog_visibility_score": 54,
    "margin_bridge_score": 30,
    "revision_score": 38,
    "relative_strength_score": 58,
    "customer_quality_score": 72,
    "policy_or_regulatory_score": 78,
    "valuation_repricing_score": 55,
    "execution_risk_score": 50,
    "legal_or_contract_risk_score": 12,
    "dilution_cb_risk_score": 10,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_before": 59.1,
  "stage_label_before": "Stage2 watch only",
  "raw_component_scores_after": {
    "contract_score": 46,
    "backlog_visibility_score": 42,
    "margin_bridge_score": 18,
    "revision_score": 26,
    "relative_strength_score": 58,
    "customer_quality_score": 60,
    "policy_or_regulatory_score": 78,
    "valuation_repricing_score": 43,
    "execution_risk_score": 68,
    "legal_or_contract_risk_score": 12,
    "dilution_cb_risk_score": 10,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_after": 50.7,
  "stage_label_after": "Stage1/Stage2 watch only",
  "component_delta_explanation": "Long-lead JV capacity was treated like current utilization. The price path had only +5.97% 180D MFE and -47.72% 180D MAE."
}
```
### 096770 SK Innovation
```json
{
  "symbol": "096770",
  "component_breakdown_required": true,
  "raw_component_scores_before": {
    "contract_score": 30,
    "backlog_visibility_score": 40,
    "margin_bridge_score": 42,
    "revision_score": 58,
    "relative_strength_score": 52,
    "customer_quality_score": 48,
    "policy_or_regulatory_score": 58,
    "valuation_repricing_score": 52,
    "execution_risk_score": 64,
    "legal_or_contract_risk_score": 12,
    "dilution_cb_risk_score": 15,
    "accounting_trust_risk_score": 12
  },
  "weighted_score_before": 51.5,
  "stage_label_before": "Stage1/Stage2 watch only",
  "raw_component_scores_after": {
    "contract_score": 18,
    "backlog_visibility_score": 28,
    "margin_bridge_score": 30,
    "revision_score": 46,
    "relative_strength_score": 52,
    "customer_quality_score": 36,
    "policy_or_regulatory_score": 58,
    "valuation_repricing_score": 40,
    "execution_risk_score": 82,
    "legal_or_contract_risk_score": 12,
    "dilution_cb_risk_score": 15,
    "accounting_trust_risk_score": 12
  },
  "weighted_score_after": 43.2,
  "stage_label_after": "Stage1/Stage2 watch only",
  "component_delta_explanation": "Loss narrowing was not the same as positive unit economics. 180D MFE stayed below 20% while MAE reached -45.86%."
}
```
### 004020 Hyundai Steel
```json
{
  "symbol": "004020",
  "component_breakdown_required": true,
  "raw_component_scores_before": {
    "contract_score": 28,
    "backlog_visibility_score": 36,
    "margin_bridge_score": 68,
    "revision_score": 64,
    "relative_strength_score": 70,
    "customer_quality_score": 32,
    "policy_or_regulatory_score": 30,
    "valuation_repricing_score": 66,
    "execution_risk_score": 58,
    "legal_or_contract_risk_score": 8,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_before": 53.8,
  "stage_label_before": "Stage1/Stage2 watch only",
  "raw_component_scores_after": {
    "contract_score": 16,
    "backlog_visibility_score": 24,
    "margin_bridge_score": 56,
    "revision_score": 52,
    "relative_strength_score": 70,
    "customer_quality_score": 20,
    "policy_or_regulatory_score": 30,
    "valuation_repricing_score": 54,
    "execution_risk_score": 76,
    "legal_or_contract_risk_score": 8,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_after": 45.5,
  "stage_label_after": "Stage1/Stage2 watch only",
  "component_delta_explanation": "A profit swing from price/spread expansion did not carry forward duration evidence. 180D MFE was +11.11% while 180D MAE was -34.66%."
}
```
### 010950 S-Oil
```json
{
  "symbol": "010950",
  "component_breakdown_required": true,
  "raw_component_scores_before": {
    "contract_score": 28,
    "backlog_visibility_score": 36,
    "margin_bridge_score": 68,
    "revision_score": 64,
    "relative_strength_score": 70,
    "customer_quality_score": 32,
    "policy_or_regulatory_score": 30,
    "valuation_repricing_score": 66,
    "execution_risk_score": 58,
    "legal_or_contract_risk_score": 8,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_before": 53.8,
  "stage_label_before": "Stage1/Stage2 watch only",
  "raw_component_scores_after": {
    "contract_score": 16,
    "backlog_visibility_score": 24,
    "margin_bridge_score": 56,
    "revision_score": 52,
    "relative_strength_score": 70,
    "customer_quality_score": 20,
    "policy_or_regulatory_score": 30,
    "valuation_repricing_score": 54,
    "execution_risk_score": 76,
    "legal_or_contract_risk_score": 8,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_after": 45.5,
  "stage_label_after": "Stage1/Stage2 watch only",
  "component_delta_explanation": "This was not a zero signal, but Stage2-Actionable/Yellow over-promotion would be false. 180D MFE was +18.84%; drawdown after peak reached -30.69%."
}
```
### 319660 PSK
```json
{
  "symbol": "319660",
  "component_breakdown_required": true,
  "raw_component_scores_before": {
    "contract_score": 58,
    "backlog_visibility_score": 54,
    "margin_bridge_score": 30,
    "revision_score": 38,
    "relative_strength_score": 58,
    "customer_quality_score": 72,
    "policy_or_regulatory_score": 78,
    "valuation_repricing_score": 55,
    "execution_risk_score": 50,
    "legal_or_contract_risk_score": 12,
    "dilution_cb_risk_score": 10,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_before": 59.1,
  "stage_label_before": "Stage2 watch only",
  "raw_component_scores_after": {
    "contract_score": 46,
    "backlog_visibility_score": 42,
    "margin_bridge_score": 18,
    "revision_score": 26,
    "relative_strength_score": 58,
    "customer_quality_score": 60,
    "policy_or_regulatory_score": 78,
    "valuation_repricing_score": 43,
    "execution_risk_score": 68,
    "legal_or_contract_risk_score": 12,
    "dilution_cb_risk_score": 10,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_after": 50.7,
  "stage_label_after": "Stage1/Stage2 watch only",
  "component_delta_explanation": "Customer capex beta was not supplier order conversion. 90D MFE was good at +29.90%, but 180D MAE was -48.34%."
}
```
### 103140 Poongsan
```json
{
  "symbol": "103140",
  "component_breakdown_required": true,
  "raw_component_scores_before": {
    "contract_score": 28,
    "backlog_visibility_score": 36,
    "margin_bridge_score": 68,
    "revision_score": 64,
    "relative_strength_score": 70,
    "customer_quality_score": 32,
    "policy_or_regulatory_score": 30,
    "valuation_repricing_score": 66,
    "execution_risk_score": 58,
    "legal_or_contract_risk_score": 8,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_before": 53.8,
  "stage_label_before": "Stage1/Stage2 watch only",
  "raw_component_scores_after": {
    "contract_score": 16,
    "backlog_visibility_score": 24,
    "margin_bridge_score": 56,
    "revision_score": 52,
    "relative_strength_score": 70,
    "customer_quality_score": 20,
    "policy_or_regulatory_score": 30,
    "valuation_repricing_score": 54,
    "execution_risk_score": 76,
    "legal_or_contract_risk_score": 8,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 10
  },
  "weighted_score_after": 45.5,
  "stage_label_after": "Stage1/Stage2 watch only",
  "component_delta_explanation": "Entry was essentially the local peak. 180D MFE was only +0.91%, while 30D/90D/180D MAE reached -28.07%/-39.20%/-40.30%."
}
```
### 298040 Hyosung Heavy Industries
```json
{
  "symbol": "298040",
  "component_breakdown_required": true,
  "raw_component_scores_before": {
    "contract_score": 78,
    "backlog_visibility_score": 81,
    "margin_bridge_score": 74,
    "revision_score": 76,
    "relative_strength_score": 74,
    "customer_quality_score": 86,
    "policy_or_regulatory_score": 65,
    "valuation_repricing_score": 66,
    "execution_risk_score": 25,
    "legal_or_contract_risk_score": 10,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_before": 77.0,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 78,
    "backlog_visibility_score": 86,
    "margin_bridge_score": 82,
    "revision_score": 76,
    "relative_strength_score": 74,
    "customer_quality_score": 86,
    "policy_or_regulatory_score": 65,
    "valuation_repricing_score": 66,
    "execution_risk_score": 25,
    "legal_or_contract_risk_score": 10,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_after": 78.3,
  "stage_label_after": "Stage2-Actionable",
  "component_delta_explanation": "Positive control: this is what a non-false Stage2-Actionable looks like. 180D MFE was +377.50% with only -6.35% MAE."
}
```
### 010120 LS ELECTRIC
```json
{
  "symbol": "010120",
  "component_breakdown_required": true,
  "raw_component_scores_before": {
    "contract_score": 78,
    "backlog_visibility_score": 81,
    "margin_bridge_score": 74,
    "revision_score": 76,
    "relative_strength_score": 74,
    "customer_quality_score": 86,
    "policy_or_regulatory_score": 65,
    "valuation_repricing_score": 66,
    "execution_risk_score": 25,
    "legal_or_contract_risk_score": 10,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_before": 77.0,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 78,
    "backlog_visibility_score": 86,
    "margin_bridge_score": 82,
    "revision_score": 76,
    "relative_strength_score": 74,
    "customer_quality_score": 86,
    "policy_or_regulatory_score": 65,
    "valuation_repricing_score": 66,
    "execution_risk_score": 25,
    "legal_or_contract_risk_score": 10,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_after": 78.3,
  "stage_label_after": "Stage2-Actionable",
  "component_delta_explanation": "Positive control: direct order/backlog visibility separated this from generic grid beta. 180D MFE was +220.97% and 180D MAE was only -0.41%."
}
```
### 003670 POSCO Future M
```json
{
  "symbol": "003670",
  "component_breakdown_required": true,
  "raw_component_scores_before": {
    "contract_score": 78,
    "backlog_visibility_score": 81,
    "margin_bridge_score": 54,
    "revision_score": 58,
    "relative_strength_score": 74,
    "customer_quality_score": 86,
    "policy_or_regulatory_score": 65,
    "valuation_repricing_score": 76,
    "execution_risk_score": 42,
    "legal_or_contract_risk_score": 10,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_before": 73.3,
  "stage_label_before": "Stage2-Actionable",
  "raw_component_scores_after": {
    "contract_score": 78,
    "backlog_visibility_score": 86,
    "margin_bridge_score": 62,
    "revision_score": 58,
    "relative_strength_score": 74,
    "customer_quality_score": 86,
    "policy_or_regulatory_score": 65,
    "valuation_repricing_score": 76,
    "execution_risk_score": 42,
    "legal_or_contract_risk_score": 10,
    "dilution_cb_risk_score": 5,
    "accounting_trust_risk_score": 8
  },
  "weighted_score_after": 74.7,
  "stage_label_after": "Stage2-Actionable",
  "component_delta_explanation": "Positive control with risk: high MAE does not make initial Stage2 false when direct customer/capacity evidence is real; it should block Green, not the initial Stage2."
}
```
## 10. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY | 3 | 6 | 0 | 0 | 9 | 9 source-sector seeds | 9 | 9 | 8 | no_new_sector_rule | R13_STAGE2_SINGLE_VARIABLE_HEADLINE_TAXONOMY | false-positive taxonomy expanded; no immediate weight delta |
## 11. Residual Contribution Summary
```text
new_independent_case_count: 9
reused_case_count: 9 source-sector seeds, 0 duplicate R13 false-positive keys
reused_case_ids: source sector rows from C02, C10, C13, C15
new_symbol_count: 9
new_canonical_archetype_count: 1 R13 scope
new_fine_archetype_count: 1
new_trigger_family_count: 9
positive_case_count: 3
counterexample_count: 6
current_profile_error_count: 8
diversity_score_summary: high; 9 symbols, 4 source canonicals, 5 failure/positive-control taxonomies
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, green_strictness, price_only_blowoff_blocks_positive_stage
residual_error_types_found: single_variable_stage2_headline, long_lead_JV_without_utilization, commodity_spread_peak_chase, customer_capex_beta_without_supplier_order, windfall_without_persistence
new_axis_proposed: false
existing_axis_strengthened: Stage2-Actionable second-bridge requirement as R13 taxonomy label
existing_axis_weakened: none
existing_axis_kept: Green strictness and price-only/4B non-price guardrails
sector_specific_rule_candidate: none
canonical_archetype_rule_candidate: R13_STAGE2_SINGLE_VARIABLE_HEADLINE_TAXONOMY
no_new_signal_reason: R13 taxonomy cleanup; no immediate production weight delta
loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true
```
This loop adds 9 new R13-scope independent cases, 6 counterexamples, and 8 residual errors for R13/CROSS_STAGE2_FALSE_POSITIVE_REVIEW.
## 12. Machine-readable JSONL rows
```jsonl
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","case_id":"R13_S2FP_197_01_006400_LONG_LEAD_JV","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_case_id":"C13_R3L190_006400_GM_JV_2023_LONG_LEAD_FALSE_POSITIVE","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"006400","company_name":"Samsung SDI","best_trigger":"R13_S2FP_197_T01","case_type":"long_lead_JV_or_capex_without_utilization","positive_or_counterexample":"counterexample","score_price_alignment":"stage2_false_positive_long_lead_jv_low_mfe_deep_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"new R13 Stage2 false-positive taxonomy row built from validated sector-case source and recomputed stock-web local shard where available","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","trigger_id":"R13_S2FP_197_T01","case_id":"R13_S2FP_197_01_006400_LONG_LEAD_JV","symbol":"006400","company_name":"Samsung SDI","market":"KOSPI","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_case_id":"C13_R3L190_006400_GM_JV_2023_LONG_LEAD_FALSE_POSITIVE","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","source_fine_archetype_id":"GM_SDI_JV_HEADLINE_WITHOUT_NEAR_TERM_UTILIZATION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_stage2_false_positive_review","loop_objective":"residual_false_positive_mining; stage2_actionable_bonus_stress_test; canonical_archetype_compression; holdout_validation","trigger_type":"Stage2","trigger_date":"2023-04-25","evidence_available_at_that_date":"Samsung SDI and GM announced a prospective US battery-cell JV with over $3B investment and more than 30GWh annual capacity, but mass production was only targeted for 2026, so the trigger lacked near-term utilization and margin conversion.","evidence_source":"https://www.samsungsdi.com/sdi-now/sdi-news/3162.html?idx=3162&pageIndex=2&pagesize=15","stage2_evidence_fields":["policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv; atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-26","entry_price":703000.0,"actual_1d_ohlc_row":{"o":707000.0,"h":721000.0,"l":701000.0,"c":703000.0,"v":220437,"a":155850026000.0,"mc":48341464590000.0,"s":68764530.0,"m":"KOSPI","d":"2023-04-26"},"MFE_30D_pct":5.97,"MFE_90D_pct":5.97,"MFE_180D_pct":5.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.83,"MAE_90D_pct":-17.07,"MAE_180D_pct":-47.72,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-12","peak_price":745000.0,"trough_date":"2024-01-18","drawdown_after_peak_pct":-50.67,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_full_window_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_timing_verdict":"stage2_false_positive_review_not_full_4B","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable_stage2_false_positive_review","trigger_outcome_label":"stage2_false_positive_long_lead_jv_low_mfe_deep_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|006400|Stage2|2023-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative_R13_taxonomy_row","is_new_independent_case":true,"reuse_reason":"source sector row reused only as evidence seed; new R13 false-positive taxonomy row and fresh duplicate key","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","profile_id":"R13_stage2_false_positive_taxonomy_shadow","case_id":"R13_S2FP_197_01_006400_LONG_LEAD_JV","trigger_id":"R13_S2FP_197_T01","symbol":"006400","raw_component_scores_before":{"contract_score":58,"backlog_visibility_score":54,"margin_bridge_score":30,"revision_score":38,"relative_strength_score":58,"customer_quality_score":72,"policy_or_regulatory_score":78,"valuation_repricing_score":55,"execution_risk_score":50,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8},"weighted_score_before":59.1,"stage_label_before":"Stage2 watch only","raw_component_scores_after":{"contract_score":46,"backlog_visibility_score":42,"margin_bridge_score":18,"revision_score":26,"relative_strength_score":58,"customer_quality_score":60,"policy_or_regulatory_score":78,"valuation_repricing_score":43,"execution_risk_score":68,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8},"weighted_score_after":50.7,"stage_label_after":"Stage1/Stage2 watch only","component_delta_explanation":"Long-lead JV capacity was treated like current utilization. The price path had only +5.97% 180D MFE and -47.72% 180D MAE.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","case_id":"R13_S2FP_197_02_096770_LOSS_NARROWING","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_case_id":"C13_R3L190_096770_SKON_Q2_2023_LOSS_NARROW_STAGE2_FAIL","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"096770","company_name":"SK Innovation","best_trigger":"R13_S2FP_197_T02","case_type":"loss_narrowing_without_positive_unit_economics","positive_or_counterexample":"counterexample","score_price_alignment":"stage2_false_positive_loss_narrowing_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"new R13 Stage2 false-positive taxonomy row built from validated sector-case source and recomputed stock-web local shard where available","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","trigger_id":"R13_S2FP_197_T02","case_id":"R13_S2FP_197_02_096770_LOSS_NARROWING","symbol":"096770","company_name":"SK Innovation","market":"KOSPI","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_case_id":"C13_R3L190_096770_SKON_Q2_2023_LOSS_NARROW_STAGE2_FAIL","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","source_fine_archetype_id":"SKON_LOSS_NARROWING_WITHOUT_MARGIN_CONVERSION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_stage2_false_positive_review","loop_objective":"residual_false_positive_mining; stage2_actionable_bonus_stress_test; canonical_archetype_compression; holdout_validation","trigger_type":"Stage2","trigger_date":"2023-07-28","evidence_available_at_that_date":"SK Innovation swung to red in Q2 2023 on falling oil prices; the battery loss-narrowing interpretation was insufficient as a utilization conversion proof.","evidence_source":"https://en.yna.co.kr/view/AEN20230728002051320","stage2_evidence_fields":["early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv; atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv","profile_path":"atlas/symbol_profiles/096/096770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-28","entry_price":189500.0,"actual_1d_ohlc_row":{"o":182500.0,"h":191700.0,"l":182200.0,"c":189500.0,"v":1384523,"a":259538370400.0,"mc":17522224378000.0,"s":92465564.0,"m":"KOSPI","d":"2023-07-28"},"MFE_30D_pct":19.79,"MFE_90D_pct":19.79,"MFE_180D_pct":19.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.77,"MAE_90D_pct":-36.62,"MAE_180D_pct":-45.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-01","peak_price":227000.0,"trough_date":"2024-04-16","drawdown_after_peak_pct":-54.8,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_full_window_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_timing_verdict":"stage2_false_positive_review_not_full_4B","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable_stage2_false_positive_review","trigger_outcome_label":"stage2_false_positive_loss_narrowing_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|096770|Stage2|2023-07-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative_R13_taxonomy_row","is_new_independent_case":true,"reuse_reason":"source sector row reused only as evidence seed; new R13 false-positive taxonomy row and fresh duplicate key","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","profile_id":"R13_stage2_false_positive_taxonomy_shadow","case_id":"R13_S2FP_197_02_096770_LOSS_NARROWING","trigger_id":"R13_S2FP_197_T02","symbol":"096770","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":40,"margin_bridge_score":42,"revision_score":58,"relative_strength_score":52,"customer_quality_score":48,"policy_or_regulatory_score":58,"valuation_repricing_score":52,"execution_risk_score":64,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_before":51.5,"stage_label_before":"Stage1/Stage2 watch only","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":28,"margin_bridge_score":30,"revision_score":46,"relative_strength_score":52,"customer_quality_score":36,"policy_or_regulatory_score":58,"valuation_repricing_score":40,"execution_risk_score":82,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":15,"accounting_trust_risk_score":12},"weighted_score_after":43.2,"stage_label_after":"Stage1/Stage2 watch only","component_delta_explanation":"Loss narrowing was not the same as positive unit economics. 180D MFE stayed below 20% while MAE reached -45.86%.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","case_id":"R13_S2FP_197_03_004020_STEEL_SPREAD_PEAK","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_case_id":"C15_192_02_HYUNDAI_STEEL_1Q21_LATE_STEEL_CHASE","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"004020","company_name":"Hyundai Steel","best_trigger":"R13_S2FP_197_T03","case_type":"commodity_profit_swing_without_forward_spread_duration","positive_or_counterexample":"counterexample","score_price_alignment":"stage2_false_positive_late_steel_spread_chase","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"new R13 Stage2 false-positive taxonomy row built from validated sector-case source and recomputed stock-web local shard where available","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","trigger_id":"R13_S2FP_197_T03","case_id":"R13_S2FP_197_03_004020_STEEL_SPREAD_PEAK","symbol":"004020","company_name":"Hyundai Steel","market":"KOSPI","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_case_id":"C15_192_02_HYUNDAI_STEEL_1Q21_LATE_STEEL_CHASE","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","source_fine_archetype_id":"STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_stage2_false_positive_review","loop_objective":"residual_false_positive_mining; stage2_actionable_bonus_stress_test; canonical_archetype_compression; holdout_validation","trigger_type":"Stage2","trigger_date":"2021-04-27","evidence_available_at_that_date":"Hyundai Steel swung to profit in Q1 2021 on robust demand and steel price strength, but the entry was already late in the spread/stock cycle.","evidence_source":"https://en.yna.co.kr/view/AEN20210427007052320","stage2_evidence_fields":["bottleneck_pricing","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv; atlas/ohlcv_tradable_by_symbol_year/004/004020/2022.csv","profile_path":"atlas/symbol_profiles/004/004020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-04-27","entry_price":56700.0,"actual_1d_ohlc_row":{"o":52600.0,"h":57000.0,"l":52400.0,"c":56700.0,"v":5322376,"a":293326474700.0,"mc":7566376009500.0,"s":133445785.0,"m":"KOSPI","d":"2021-04-27"},"MFE_30D_pct":11.11,"MFE_90D_pct":11.11,"MFE_180D_pct":11.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.76,"MAE_90D_pct":-20.19,"MAE_180D_pct":-34.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-11","peak_price":63000.0,"trough_date":"2021-12-01","drawdown_after_peak_pct":-41.19,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_full_window_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_timing_verdict":"stage2_false_positive_review_not_full_4B","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable_stage2_false_positive_review","trigger_outcome_label":"stage2_false_positive_late_steel_spread_chase","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|004020|Stage2|2021-04-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative_R13_taxonomy_row","is_new_independent_case":true,"reuse_reason":"source sector row reused only as evidence seed; new R13 false-positive taxonomy row and fresh duplicate key","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","profile_id":"R13_stage2_false_positive_taxonomy_shadow","case_id":"R13_S2FP_197_03_004020_STEEL_SPREAD_PEAK","trigger_id":"R13_S2FP_197_T03","symbol":"004020","raw_component_scores_before":{"contract_score":28,"backlog_visibility_score":36,"margin_bridge_score":68,"revision_score":64,"relative_strength_score":70,"customer_quality_score":32,"policy_or_regulatory_score":30,"valuation_repricing_score":66,"execution_risk_score":58,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":53.8,"stage_label_before":"Stage1/Stage2 watch only","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":24,"margin_bridge_score":56,"revision_score":52,"relative_strength_score":70,"customer_quality_score":20,"policy_or_regulatory_score":30,"valuation_repricing_score":54,"execution_risk_score":76,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_after":45.5,"stage_label_after":"Stage1/Stage2 watch only","component_delta_explanation":"A profit swing from price/spread expansion did not carry forward duration evidence. 180D MFE was +11.11% while 180D MAE was -34.66%.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","case_id":"R13_S2FP_197_04_010950_REFINING_INVENTORY_WIND","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_case_id":"C15_192_06_SOIL_Q2_2022_REFINING_MARGIN_LATE","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"010950","company_name":"S-Oil","best_trigger":"R13_S2FP_197_T04","case_type":"inventory_gain_or_windfall_without_persistence","positive_or_counterexample":"counterexample","score_price_alignment":"stage2_actionable_windfall_needs_green_blocker","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"new R13 Stage2 false-positive taxonomy row built from validated sector-case source and recomputed stock-web local shard where available","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","trigger_id":"R13_S2FP_197_T04","case_id":"R13_S2FP_197_04_010950_REFINING_INVENTORY_WIND","symbol":"010950","company_name":"S-Oil","market":"KOSPI","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_192_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_case_id":"C15_192_06_SOIL_Q2_2022_REFINING_MARGIN_LATE","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","source_fine_archetype_id":"STEEL_COPPER_REFINING_SPREAD_REVERSAL_INVENTORY_CYCLE","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_stage2_false_positive_review","loop_objective":"residual_false_positive_mining; stage2_actionable_bonus_stress_test; canonical_archetype_compression; holdout_validation","trigger_type":"Stage2-Actionable","trigger_date":"2022-07-28","evidence_available_at_that_date":"S-Oil Q2 2022 profit was driven by widened refining margins and inventory gains; the windfall was real but did not prove full-window spread persistence.","evidence_source":"https://en.yna.co.kr/view/AEN20220728002252320","stage2_evidence_fields":["bottleneck_pricing","margin_bridge"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010950/2022.csv; atlas/ohlcv_tradable_by_symbol_year/010/010950/2023.csv","profile_path":"atlas/symbol_profiles/010/010950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-07-28","entry_price":91300.0,"actual_1d_ohlc_row":{"o":93600.0,"h":93800.0,"l":90500.0,"c":91300.0,"v":538463,"a":49183815300.0,"mc":10278808909600.0,"s":112582792.0,"m":"KOSPI","d":"2022-07-28"},"MFE_30D_pct":18.84,"MFE_90D_pct":18.84,"MFE_180D_pct":18.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.12,"MAE_90D_pct":-15.12,"MAE_180D_pct":-17.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-30","peak_price":108500.0,"trough_date":"2023-03-27","drawdown_after_peak_pct":-30.69,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_full_window_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_timing_verdict":"stage2_false_positive_review_not_full_4B","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable_stage2_false_positive_review","trigger_outcome_label":"stage2_actionable_windfall_needs_green_blocker","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|010950|Stage2-Actionable|2022-07-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative_R13_taxonomy_row","is_new_independent_case":true,"reuse_reason":"source sector row reused only as evidence seed; new R13 false-positive taxonomy row and fresh duplicate key","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","profile_id":"R13_stage2_false_positive_taxonomy_shadow","case_id":"R13_S2FP_197_04_010950_REFINING_INVENTORY_WIND","trigger_id":"R13_S2FP_197_T04","symbol":"010950","raw_component_scores_before":{"contract_score":28,"backlog_visibility_score":36,"margin_bridge_score":68,"revision_score":64,"relative_strength_score":70,"customer_quality_score":32,"policy_or_regulatory_score":30,"valuation_repricing_score":66,"execution_risk_score":58,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":53.8,"stage_label_before":"Stage1/Stage2 watch only","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":24,"margin_bridge_score":56,"revision_score":52,"relative_strength_score":70,"customer_quality_score":20,"policy_or_regulatory_score":30,"valuation_repricing_score":54,"execution_risk_score":76,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_after":45.5,"stage_label_after":"Stage1/Stage2 watch only","component_delta_explanation":"This was not a zero signal, but Stage2-Actionable/Yellow over-promotion would be false. 180D MFE was +18.84%; drawdown after peak reached -30.69%.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","case_id":"R13_S2FP_197_05_319660_CUSTOMER_CAPEX_BETA","source_research_file":"e2r_stock_web_v12_residual_round_R2_loop_192_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md","source_case_id":"C10_319660_20240424_STAGE2_FALSE","source_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","source_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"319660","company_name":"PSK","best_trigger":"R13_S2FP_197_T05","case_type":"customer_capex_beta_without_supplier_order_conversion","positive_or_counterexample":"counterexample","score_price_alignment":"stage2_false_positive_memory_customer_capex_beta","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"new R13 Stage2 false-positive taxonomy row built from validated sector-case source and recomputed stock-web local shard where available","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","trigger_id":"R13_S2FP_197_T05","case_id":"R13_S2FP_197_05_319660_CUSTOMER_CAPEX_BETA","symbol":"319660","company_name":"PSK","market":"KOSDAQ GLOBAL","source_research_file":"e2r_stock_web_v12_residual_round_R2_loop_192_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md","source_case_id":"C10_319660_20240424_STAGE2_FALSE","source_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","source_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","source_fine_archetype_id":"MEMORY_CAPEX_ORDER_CONVERSION_AND_FALSE_POSITIVE_GATE","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_stage2_false_positive_review","loop_objective":"residual_false_positive_mining; stage2_actionable_bonus_stress_test; canonical_archetype_compression; holdout_validation","trigger_type":"Stage2","trigger_date":"2024-04-24","evidence_available_at_that_date":"SK Hynix recovery/capex evidence was strong at customer level, while PSK supplier-level order conversion was not yet directly proven; PSK official financial summary is used as direct company context.","evidence_source":"https://www.pskinc.com/ir/financial_summary.php ; https://www.reuters.com/technology/sk-hynix-q1-profit-beats-expectations-ai-boom-2024-04-24/","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv; atlas/ohlcv_tradable_by_symbol_year/319/319660/2025.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":30100.0,"actual_1d_ohlc_row":{"o":29900.0,"h":30900.0,"l":29850.0,"c":30100.0,"v":242835,"a":7357587550.0,"mc":871898091400.0,"s":28966714.0,"m":"KOSDAQ GLOBAL","d":"2024-04-25"},"MFE_30D_pct":14.45,"MFE_90D_pct":29.9,"MFE_180D_pct":29.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.64,"MAE_90D_pct":-24.58,"MAE_180D_pct":-48.34,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":39100.0,"trough_date":"2024-12-02","drawdown_after_peak_pct":-60.23,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_full_window_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_timing_verdict":"stage2_false_positive_review_not_full_4B","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable_stage2_false_positive_review","trigger_outcome_label":"stage2_false_positive_memory_customer_capex_beta","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|319660|Stage2|2024-04-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative_R13_taxonomy_row","is_new_independent_case":true,"reuse_reason":"source sector row reused only as evidence seed; new R13 false-positive taxonomy row and fresh duplicate key","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","profile_id":"R13_stage2_false_positive_taxonomy_shadow","case_id":"R13_S2FP_197_05_319660_CUSTOMER_CAPEX_BETA","trigger_id":"R13_S2FP_197_T05","symbol":"319660","raw_component_scores_before":{"contract_score":58,"backlog_visibility_score":54,"margin_bridge_score":30,"revision_score":38,"relative_strength_score":58,"customer_quality_score":72,"policy_or_regulatory_score":78,"valuation_repricing_score":55,"execution_risk_score":50,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8},"weighted_score_before":59.1,"stage_label_before":"Stage2 watch only","raw_component_scores_after":{"contract_score":46,"backlog_visibility_score":42,"margin_bridge_score":18,"revision_score":26,"relative_strength_score":58,"customer_quality_score":60,"policy_or_regulatory_score":78,"valuation_repricing_score":43,"execution_risk_score":68,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":10,"accounting_trust_risk_score":8},"weighted_score_after":50.7,"stage_label_after":"Stage1/Stage2 watch only","component_delta_explanation":"Customer capex beta was not supplier order conversion. 90D MFE was good at +29.90%, but 180D MAE was -48.34%.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","case_id":"R13_S2FP_197_06_103140_COPPER_HEADLINE","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_case_id":"C15-103140-20240514-STAGE2A","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"103140","company_name":"Poongsan","best_trigger":"R13_S2FP_197_T06","case_type":"commodity_price_headline_without_company_volume_margin_bridge","positive_or_counterexample":"counterexample","score_price_alignment":"stage2_actionable_false_positive_copper_headline_no_bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"new R13 Stage2 false-positive taxonomy row built from validated sector-case source and recomputed stock-web local shard where available","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","trigger_id":"R13_S2FP_197_T06","case_id":"R13_S2FP_197_06_103140_COPPER_HEADLINE","symbol":"103140","company_name":"Poongsan","market":"KOSPI","source_research_file":"e2r_stock_web_v12_residual_round_R4_loop_191_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md","source_case_id":"C15-103140-20240514-STAGE2A","source_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","source_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","source_fine_archetype_id":"COPPER_PRICE_THESIS_WITH_VOLUME_COST_OFFSET","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_stage2_false_positive_review","loop_objective":"residual_false_positive_mining; stage2_actionable_bonus_stress_test; canonical_archetype_compression; holdout_validation","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-14","evidence_available_at_that_date":"Copper-price and defense optimism created a plausible Stage2 story, but the entry lacked direct forward volume/margin bridge strong enough to justify Actionable promotion.","evidence_source":"https://v.daum.net/v/fXzID0JqJ6?f=p ; https://poongsan.co.kr/en/ir/financial/information","stage2_evidence_fields":["bottleneck_pricing","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv; atlas/ohlcv_tradable_by_symbol_year/103/103140/2025.csv","profile_path":"atlas/symbol_profiles/103/103140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":77300.0,"actual_1d_ohlc_row":{"o":78000.0,"h":78000.0,"l":74400.0,"c":77300.0,"v":562357,"a":42846430300.0,"mc":2166276689400.0,"s":28024278.0,"m":"KOSPI","d":"2024-05-16"},"MFE_30D_pct":0.91,"MFE_90D_pct":0.91,"MFE_180D_pct":0.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.07,"MAE_90D_pct":-39.2,"MAE_180D_pct":-40.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":78000.0,"trough_date":"2024-12-09","drawdown_after_peak_pct":-40.83,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_full_window_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_timing_verdict":"stage2_false_positive_review_not_full_4B","four_b_evidence_type":["valuation_blowoff","price_only_local_peak"],"four_c_protection_label":"not_applicable_stage2_false_positive_review","trigger_outcome_label":"stage2_actionable_false_positive_copper_headline_no_bridge","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|103140|Stage2-Actionable|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative_R13_taxonomy_row","is_new_independent_case":true,"reuse_reason":"source sector row reused only as evidence seed; new R13 false-positive taxonomy row and fresh duplicate key","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","profile_id":"R13_stage2_false_positive_taxonomy_shadow","case_id":"R13_S2FP_197_06_103140_COPPER_HEADLINE","trigger_id":"R13_S2FP_197_T06","symbol":"103140","raw_component_scores_before":{"contract_score":28,"backlog_visibility_score":36,"margin_bridge_score":68,"revision_score":64,"relative_strength_score":70,"customer_quality_score":32,"policy_or_regulatory_score":30,"valuation_repricing_score":66,"execution_risk_score":58,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":53.8,"stage_label_before":"Stage1/Stage2 watch only","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":24,"margin_bridge_score":56,"revision_score":52,"relative_strength_score":70,"customer_quality_score":20,"policy_or_regulatory_score":30,"valuation_repricing_score":54,"execution_risk_score":76,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_after":45.5,"stage_label_after":"Stage1/Stage2 watch only","component_delta_explanation":"Entry was essentially the local peak. 180D MFE was only +0.91%, while 30D/90D/180D MAE reached -28.07%/-39.20%/-40.30%.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","case_id":"R13_S2FP_197_07_298040_TRUE_BACKLOG_MARGIN","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_case_id":"C02_R1L193_298040_20250429_STAGE2A","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"298040","company_name":"Hyosung Heavy Industries","best_trigger":"R13_S2FP_197_T07","case_type":"positive_control_direct_backlog_margin_revenue_bridge","positive_or_counterexample":"positive","score_price_alignment":"true_stage2_actionable_when_order_backlog_margin_bridge_is_direct","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"new R13 Stage2 false-positive taxonomy row built from validated sector-case source and recomputed stock-web local shard where available","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","trigger_id":"R13_S2FP_197_T07","case_id":"R13_S2FP_197_07_298040_TRUE_BACKLOG_MARGIN","symbol":"298040","company_name":"Hyosung Heavy Industries","market":"KOSPI","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_case_id":"C02_R1L193_298040_20250429_STAGE2A","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","source_fine_archetype_id":"GRID_DATACENTER_HIGH_VALUE_TRANSFORMER_BACKLOG_MARGIN_BRIDGE","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_stage2_false_positive_review","loop_objective":"residual_false_positive_mining; stage2_actionable_bonus_stress_test; canonical_archetype_compression; holdout_validation","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-29","evidence_available_at_that_date":"1Q25 coverage showed heavy-industry backlog, new orders, high-value project revenue recognition, and improving overseas margins.","evidence_source":"https://securities.miraeasset.com/bbs/download/2135886.pdf?attachmentId=2135886","stage2_evidence_fields":["backlog_or_delivery_visibility","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv; atlas/ohlcv_tradable_by_symbol_year/298/298040/2026.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-04-29","entry_price":520000.0,"actual_1d_ohlc_row":{"o":492000.0,"h":522000.0,"l":487000.0,"c":520000.0,"v":92036,"a":47150316250.0,"mc":4848764960000.0,"s":9324548.0,"m":"KOSPI","d":"2025-04-29"},"MFE_30D_pct":49.04,"MFE_90D_pct":160.77,"MFE_180D_pct":377.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.35,"MAE_90D_pct":-6.35,"MAE_180D_pct":-6.35,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-11-04","peak_price":2483000.0,"trough_date":"2025-12-26","drawdown_after_peak_pct":-30.29,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_full_window_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_timing_verdict":"stage2_false_positive_review_not_full_4B","four_b_evidence_type":["none"],"four_c_protection_label":"not_applicable_stage2_false_positive_review","trigger_outcome_label":"true_stage2_actionable_when_order_backlog_margin_bridge_is_direct","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|298040|Stage2-Actionable|2025-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative_R13_taxonomy_row","is_new_independent_case":true,"reuse_reason":"source sector row reused only as evidence seed; new R13 false-positive taxonomy row and fresh duplicate key","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","profile_id":"R13_stage2_false_positive_taxonomy_shadow","case_id":"R13_S2FP_197_07_298040_TRUE_BACKLOG_MARGIN","trigger_id":"R13_S2FP_197_T07","symbol":"298040","raw_component_scores_before":{"contract_score":78,"backlog_visibility_score":81,"margin_bridge_score":74,"revision_score":76,"relative_strength_score":74,"customer_quality_score":86,"policy_or_regulatory_score":65,"valuation_repricing_score":66,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":77.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":78,"backlog_visibility_score":86,"margin_bridge_score":82,"revision_score":76,"relative_strength_score":74,"customer_quality_score":86,"policy_or_regulatory_score":65,"valuation_repricing_score":66,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":78.3,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"Positive control: this is what a non-false Stage2-Actionable looks like. 180D MFE was +377.50% with only -6.35% MAE.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","case_id":"R13_S2FP_197_08_010120_TRUE_ORDER_BACKLOG","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_case_id":"C02_R1L193_010120_20250422_STAGE2A","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"010120","company_name":"LS ELECTRIC","best_trigger":"R13_S2FP_197_T08","case_type":"positive_control_direct_us_grid_order_backlog","positive_or_counterexample":"positive","score_price_alignment":"true_stage2_actionable_us_grid_order_backlog_reacceleration","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"new R13 Stage2 false-positive taxonomy row built from validated sector-case source and recomputed stock-web local shard where available","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","trigger_id":"R13_S2FP_197_T08","case_id":"R13_S2FP_197_08_010120_TRUE_ORDER_BACKLOG","symbol":"010120","company_name":"LS ELECTRIC","market":"KOSPI","source_research_file":"e2r_stock_web_v12_residual_round_R1_loop_193_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","source_case_id":"C02_R1L193_010120_20250422_STAGE2A","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","source_fine_archetype_id":"GRID_DATACENTER_US_ORDER_BACKLOG_REACCELERATION","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_stage2_false_positive_review","loop_objective":"residual_false_positive_mining; stage2_actionable_bonus_stress_test; canonical_archetype_compression; holdout_validation","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-22","evidence_available_at_that_date":"LS ELECTRIC 1Q25 result material showed HVTR/SWGR order/backlog reacceleration and US/grid-related visibility.","evidence_source":"https://www.ls-electric.com/ko/company/data/25_1Q_Results.pdf","stage2_evidence_fields":["backlog_or_delivery_visibility","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv; atlas/ohlcv_tradable_by_symbol_year/010/010120/2026.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-04-22","entry_price":172600.0,"actual_1d_ohlc_row":{"o":173700.0,"h":179400.0,"l":171900.0,"c":172600.0,"v":340505,"a":59789951000.0,"mc":5178000000000.0,"s":30000000.0,"m":"KOSPI","d":"2025-04-22"},"MFE_30D_pct":54.84,"MFE_90D_pct":93.51,"MFE_180D_pct":220.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.41,"MAE_90D_pct":-0.41,"MAE_180D_pct":-0.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-01-14","peak_price":554000.0,"trough_date":"2026-01-14","drawdown_after_peak_pct":-10.2,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_full_window_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_timing_verdict":"stage2_false_positive_review_not_full_4B","four_b_evidence_type":["none"],"four_c_protection_label":"not_applicable_stage2_false_positive_review","trigger_outcome_label":"true_stage2_actionable_us_grid_order_backlog_reacceleration","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|010120|Stage2-Actionable|2025-04-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative_R13_taxonomy_row","is_new_independent_case":true,"reuse_reason":"source sector row reused only as evidence seed; new R13 false-positive taxonomy row and fresh duplicate key","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","profile_id":"R13_stage2_false_positive_taxonomy_shadow","case_id":"R13_S2FP_197_08_010120_TRUE_ORDER_BACKLOG","trigger_id":"R13_S2FP_197_T08","symbol":"010120","raw_component_scores_before":{"contract_score":78,"backlog_visibility_score":81,"margin_bridge_score":74,"revision_score":76,"relative_strength_score":74,"customer_quality_score":86,"policy_or_regulatory_score":65,"valuation_repricing_score":66,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":77.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":78,"backlog_visibility_score":86,"margin_bridge_score":82,"revision_score":76,"relative_strength_score":74,"customer_quality_score":86,"policy_or_regulatory_score":65,"valuation_repricing_score":66,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":78.3,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"Positive control: direct order/backlog visibility separated this from generic grid beta. 180D MFE was +220.97% and 180D MAE was only -0.41%.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","case_id":"R13_S2FP_197_09_003670_TRUE_JV_HIGH_MAE","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_case_id":"C13_R3L190_003670_POSCO_GM_ULTIUM_CAM_EXPANSION","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"003670","company_name":"POSCO Future M","best_trigger":"R13_S2FP_197_T09","case_type":"positive_control_direct_customer_capacity_but_green_block_needed","positive_or_counterexample":"positive","score_price_alignment":"true_stage2_actionable_with_high_mae_not_green","current_profile_verdict":"current_profile_missed_structural_if_capacity_not_mapped_but_green_block_correct","price_source":"Songdaiki/stock-web","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"new R13 Stage2 false-positive taxonomy row built from validated sector-case source and recomputed stock-web local shard where available","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"do_not_propose_new_weight_delta":true}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","trigger_id":"R13_S2FP_197_T09","case_id":"R13_S2FP_197_09_003670_TRUE_JV_HIGH_MAE","symbol":"003670","company_name":"POSCO Future M","market":"KOSPI","source_research_file":"e2r_stock_web_v12_residual_round_R3_loop_190_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md","source_case_id":"C13_R3L190_003670_POSCO_GM_ULTIUM_CAM_EXPANSION","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","source_fine_archetype_id":"GM_POSCO_ULTIUM_CAM_JV_CAPACITY_BRIDGE","sector":"cross_archetype_redteam_misc","primary_archetype":"R13_stage2_false_positive_review","loop_objective":"residual_false_positive_mining; stage2_actionable_bonus_stress_test; canonical_archetype_compression; holdout_validation","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-02","evidence_available_at_that_date":"POSCO Future M and GM expanded an integrated CAM/precursor complex tied to the Ultium battery supply chain, providing direct customer/capacity evidence.","evidence_source":"https://www.poscofuturem.com/en/pr/view.do?num=695 ; https://news.gm.com/home.detail.html/Pages/news/us/en/2023/jun/0602-posco.html","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","policy_or_regulatory_optionality"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv; atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-02","entry_price":374000.0,"actual_1d_ohlc_row":{"o":361500.0,"h":381500.0,"l":358500.0,"c":374000.0,"v":1467089,"a":546474921500.0,"mc":28971244280000.0,"s":77463220.0,"m":"KOSPI","d":"2023-06-02"},"MFE_30D_pct":12.3,"MFE_90D_pct":85.56,"MFE_180D_pct":85.56,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.89,"MAE_90D_pct":-16.18,"MAE_180D_pct":-38.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000.0,"trough_date":"2023-11-01","drawdown_after_peak_pct":-66.64,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_full_window_peak_proximity":"not_applicable_stage2_false_positive_review","four_b_timing_verdict":"stage2_false_positive_review_not_full_4B","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable_stage2_false_positive_review","trigger_outcome_label":"true_stage2_actionable_with_high_mae_not_green","current_profile_verdict":"current_profile_missed_structural_if_capacity_not_mapped_but_green_block_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|003670|Stage2-Actionable|2023-06-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative_R13_taxonomy_row","is_new_independent_case":true,"reuse_reason":"source sector row reused only as evidence seed; new R13 false-positive taxonomy row and fresh duplicate key","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"do_not_propose_new_weight_delta":true}
{"row_type":"score_simulation","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","profile_id":"R13_stage2_false_positive_taxonomy_shadow","case_id":"R13_S2FP_197_09_003670_TRUE_JV_HIGH_MAE","trigger_id":"R13_S2FP_197_T09","symbol":"003670","raw_component_scores_before":{"contract_score":78,"backlog_visibility_score":81,"margin_bridge_score":54,"revision_score":58,"relative_strength_score":74,"customer_quality_score":86,"policy_or_regulatory_score":65,"valuation_repricing_score":76,"execution_risk_score":42,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":73.3,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":78,"backlog_visibility_score":86,"margin_bridge_score":62,"revision_score":58,"relative_strength_score":74,"customer_quality_score":86,"policy_or_regulatory_score":65,"valuation_repricing_score":76,"execution_risk_score":42,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":74.7,"stage_label_after":"Stage2-Actionable","component_delta_explanation":"Positive control with risk: high MAE does not make initial Stage2 false when direct customer/capacity evidence is real; it should block Green, not the initial Stage2.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"aggregate","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_STAGE2_FALSE_POSITIVE_SINGLE_VARIABLE_HEADLINE_TAXONOMY","new_independent_case_count":9,"reused_source_sector_case_count":9,"new_symbol_count":9,"same_archetype_new_trigger_family_count":9,"positive_case_count":3,"counterexample_count":6,"current_profile_error_count":8,"calibration_usable_trigger_count":9,"avg_MFE_90D_pct":47.37,"avg_MAE_90D_pct":-19.52,"avg_MFE_180D_pct":85.62,"avg_MAE_180D_pct":-31.04,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_weight","research_file":"e2r_stock_web_v12_residual_round_R13_loop_197_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md","round":"R13","loop":197,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","axis":"R13_STAGE2_SINGLE_VARIABLE_HEADLINE_TAXONOMY","old_weight":"not_applicable_R13_guard","new_weight":"not_applicable_R13_guard","delta":0,"evidence_summary":"R13 taxonomy strengthens bridge requirement but does not request immediate profile weight delta.","representative_trigger_ids":["R13_S2FP_197_T01","R13_S2FP_197_T02","R13_S2FP_197_T03","R13_S2FP_197_T04","R13_S2FP_197_T05","R13_S2FP_197_T06","R13_S2FP_197_T07","R13_S2FP_197_T08","R13_S2FP_197_T09"],"usable_trigger_count":9,"positive_count":3,"counterexample_count":6,"application_status":"hold_for_batch_taxonomy_review","production_scoring_changed":false,"shadow_weight_only":true}
```
## 13. Deferred Coding Agent Handoff Prompt
```text
Do not execute this handoff during the research run. Later, in a separate coding-agent batch, parse this MD together with other v12 results. Treat `R13_STAGE2_SINGLE_VARIABLE_HEADLINE_TAXONOMY` as a taxonomy/QA candidate, not as an immediate production weight delta. Validate that the trigger rows have complete MFE_30D_pct/MFE_90D_pct/MFE_180D_pct and MAE_30D_pct/MAE_90D_pct/MAE_180D_pct. If promotion is considered, implement only as a non-production diagnostic label or canonical bridge-quality check: Stage2-Actionable requires at least two independent bridges when the first evidence is a single-variable headline. Do not loosen Stage3-Green. Preserve high-MAE true-winner handling by blocking Green rather than blocking initial Stage2 where direct customer/order/capacity evidence exists.
```
## 14. Next Research State
```text
completed_round = R13
completed_loop = 197
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 R13 false-positive taxonomy cleanup
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = [
  R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION,
  C05_EPC_MEGA_CONTRACT_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR,
  C01_ORDER_BACKLOG_MARGIN_BRIDGE_FCF_COUNTEREXAMPLE_REPAIR,
  C13_BATTERY_JV_UTILIZATION_AMPC_IRA_OFFSET_QUALITY_REPAIR,
  C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_CONVERSION_REPAIR
]
```
