# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R13
selected_loop: 148
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — R13 4B/4C cross-archetype RedTeam after C01~C32 coverage sweep; 4B-watch vs hard-4C escalation timing, price/proxy-only false positives, and thesis-break confirmation
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE
loop_objective: 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; holdout_validation; counterexample_mining; residual_false_positive_mining
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patched: false
live_candidate_mode: false
auto_trading_allowed: false
```

This loop adds 8 new R13 cross-scope independent cases, 6 counterexamples, and 7 residual errors for R13/L10/R13_CROSS_ARCHETYPE_4B_4C_REDTEAM.

## 1. Current Calibrated Profile Assumption

- baseline_current_proxy: `e2r_2_1_stock_web_calibrated_proxy`
- prior baseline reference: `e2r_2_0_baseline_reference`
- already-applied global axes are treated as existing controls, not re-proposed: Stage2 actionable evidence bonus, Yellow/Green thresholds, price-only blowoff block, full 4B non-price requirement, hard 4C thesis-break routing.
- This file proposes only a R13 cross-scope shadow rule candidate. Production scoring remains unchanged.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R13 |
| selected_loop | 148 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM |
| fine_archetype_id | CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE |
| scope_reason | R13 is a cross-archetype checkpoint, not a sector-specific positive research round. |
| invalid_round_sector_pair | false |

## 3. Previous Coverage / Duplicate Avoidance Check

- `V12_Research_No_Repeat_Index.md` reports cumulative `--include-archive` ingest with 2081 v12 result MDs, 11200 representative rows, 36 covered canonical scopes, and all representative rows having complete required MFE/MAE fields.
- The GitHub root listing shows R13 4B/4C RedTeam files up to loop 147. Therefore this output uses R13 loop 148.
- Recent local outputs in this session swept C01~C32 and one R13 high-MAE guardrail. This file does not create another sector-specific Cxx MD; it re-tests 4B/4C escalation across sectors.
- The selected rows deliberately use different underlying archetypes, symbols, trigger families, and failure modes. They are R13 cross-scope holdout references, not schema rematerialization.

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| validation_status | usable_for_historical_calibration |

All selected trigger rows retain the 30D/90D/180D MFE and MAE fields from prior Stock-Web-backed sector rows. Each row uses `clean_180D_window` and has at least 180 forward tradable rows under the manifest max date.

## 5. Historical Eligibility Gate

| gate | status |
|---|---|
| trigger_date is historical | pass |
| entry_date exists in Stock-Web tradable shard | pass |
| forward_window_trading_days >= 180 | pass |
| required MFE/MAE 30D/90D/180D present | pass |
| corporate_action_window_status | clean_180D_window for every trigger |
| current/live candidate discovery | not performed |

## 6. Canonical Archetype Compression Map

| R13 bucket | underlying archetypes compressed | purpose |
|---|---|---|
| 4B watch | C16, C07, C02 | Separate reversible overheat / price-only theme from hard thesis break. |
| Hard 4C | C12, C17, C30, C27, C28 | Confirm when company-specific evidence break, margin/cash break, trust break, or monetization/retention bridge failure appears. |
| Cross-scope rule | C02/C07/C12/C16/C17/C27/C28/C30 | Require non-price escalation evidence before a row upgrades from watch to hard 4C. |

## 7. Case Selection Summary

| case_id | symbol | company | underlying | trigger | entry | MFE90 | MAE90 | role |
|---|---:|---|---|---|---:|---:|---:|---|
| R13_4B4C_C16_005490_POSCO_RESOURCE_VALUE_DAY_LOCAL_4B | 005490 | POSCO홀딩스 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | Stage4B | 2023-07-12 | 82.99 | -6.71 | 4B_overlay_success |
| R13_4B4C_C07_042700_HANMI_TCBONDER_ORDER_LATE_BLOWOFF | 042700 | 한미반도체 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | Stage4B | 2024-06-07 | 25.13 | -41.77 | 4B_overlay_success |
| R13_4B4C_C02_006340_DAEWON_PRICE_ONLY_GRID_THEME | 006340 | 대원전선 | C02_POWER_GRID_DATACENTER_CAPEX | Stage4B | 2024-06-27 | 9.77 | -41.38 | false_positive_green |
| R13_4B4C_C12_066970_LNF_INVENTORY_VALUATION_LOSS_TRUE_4C | 066970 | 엘앤에프 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Stage4C | 2024-05-10 | 15.46 | -45.92 | 4C_success |
| R13_4B4C_C17_011170_LOTTECHEM_LOSS_SPREAD_BREAK_TRUE_4C | 011170 | 롯데케미칼 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Stage4C | 2024-02-08 | 3.41 | -28.66 | 4C_success |
| R13_4B4C_C30_294870_HDC_CONSTRUCTION_TRUST_BREAK_TRUE_4C | 294870 | HDC현대산업개발 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage4C | 2022-01-17 | 5.60 | -29.87 | 4C_success |
| R13_4B4C_C27_253450_STUDIO_DRAGON_HIT_WITHOUT_MONETIZATION | 253450 | 스튜디오드래곤 | C27_CONTENT_IP_GLOBAL_MONETIZATION | Stage4C | 2023-03-13 | 2.89 | -36.12 | false_positive_green |
| R13_4B4C_C28_263860_GENIANS_REVENUE_MILESTONE_NO_RETENTION | 263860 | 지니언스 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Stage4C | 2024-02-26 | 5.30 | -32.54 | false_positive_green |

## 8. Positive vs Counterexample Balance

| bucket | count | interpretation |
|---|---:|---|
| 4B / watch-positive rows | 2 | 4B is useful as a watch overlay, but hard 4C would overkill or be premature. |
| counterexample / protection rows | 6 | Weak bridge or explicit break rows where positive scoring must be capped or routed to 4C. |
| Stage4B rows | 3 | Local/full-window overheat and price/proxy-only false-positive tests. |
| Stage4C rows | 5 | Thesis break / margin break / trust break / monetization failure tests. |
| avg 90D MFE / MAE | 18.82 / -32.87 | Deep average MAE validates that this is a guardrail rather than positive-promotion research. |

## 9. Evidence Source Map

| case_id | evidence_family | evidence_source | source_proxy_only |
|---|---|---|---:|
| R13_4B4C_C16_005490_POSCO_RESOURCE_VALUE_DAY_LOCAL_4B | resource_policy_capacity_target_local_blowoff_without_immediate_cashflow | https://www.asiae.co.kr/en/article/2023071114413620672 | true |
| R13_4B4C_C07_042700_HANMI_TCBONDER_ORDER_LATE_BLOWOFF | real_hbm_equipment_order_but_late_valuation_positioning_overheat | https://www.kedglobal.com/korean-chipmakers/newsView/ked202406070008 | false |
| R13_4B4C_C02_006340_DAEWON_PRICE_ONLY_GRID_THEME | price_only_transformer_expectation_without_order_margin_bridge | https://securities.miraeasset.com/bbs/download/2129191.pdf?attachmentId=2129191 | true |
| R13_4B4C_C12_066970_LNF_INVENTORY_VALUATION_LOSS_TRUE_4C | inventory_valuation_loss_customer_demand_break_margin_damage | https://www.asiae.co.kr/en/article/2024050915570493698 | true |
| R13_4B4C_C17_011170_LOTTECHEM_LOSS_SPREAD_BREAK_TRUE_4C | company_level_operating_loss_spread_cost_break | https://www.lottechem.com/en/media/news/list.do | false |
| R13_4B4C_C30_294870_HDC_CONSTRUCTION_TRUST_BREAK_TRUE_4C | construction_quality_trust_break_fatal_accident_management_accountability | https://en.yna.co.kr/ | true |
| R13_4B4C_C27_253450_STUDIO_DRAGON_HIT_WITHOUT_MONETIZATION | global_hit_drama_without_listed_company_monetization_or_margin_bridge | https://en.yna.co.kr/view/AEN20230313003200315 | true |
| R13_4B4C_C28_263860_GENIANS_REVENUE_MILESTONE_NO_RETENTION | official_revenue_milestone_without_forward_contract_retention_confirmation | https://www.genians.co.kr/ | true |

## 10. Price Data Source Map

| symbol | entry_year | shard | profile | corporate_action_window_status |
|---:|---:|---|---|---|
| 005490 | 2023 | `atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv` | `atlas/symbol_profiles/005/005490.json` | clean_180D_window |
| 042700 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv` | `atlas/symbol_profiles/042/042700.json` | clean_180D_window |
| 006340 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv` | `atlas/symbol_profiles/006/006340.json` | clean_180D_window |
| 066970 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv` | `atlas/symbol_profiles/066/066970.json` | clean_180D_window |
| 011170 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv` | `atlas/symbol_profiles/011/011170.json` | clean_180D_window |
| 294870 | 2022 | `atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv` | `atlas/symbol_profiles/294/294870.json` | clean_180D_window |
| 253450 | 2023 | `atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv` | `atlas/symbol_profiles/253/253450.json` | clean_180D_window |
| 263860 | 2024 | `atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv` | `atlas/symbol_profiles/263/263860.json` | clean_180D_window |

## 11. Case-by-Case Trigger Grid

### R13_4B4C_C16_005490_POSCO_RESOURCE_VALUE_DAY_LOCAL_4B

- **Underlying archetype:** `C16_STRATEGIC_RESOURCE_POLICY_SUPPLY`
- **Trigger:** `Stage4B` on `2023-07-11`, entry `2023-07-12` at `417500.0`.
- **Evidence family:** resource_policy_capacity_target_local_blowoff_without_immediate_cashflow.
- **Stage2 fields:** policy_or_regulatory_optionality, resource_capacity_target, strategic_supply_chain_vocabulary.
- **Stage3 fields:** not_yet_cashflow_conversion, not_yet_margin_bridge.
- **4B fields:** valuation_blowoff, positioning_overheat, future_capacity_target_without_current_margin_bridge.
- **4C fields:** none.
- **Interpretation:** local_4b_watch_success_not_hard_4c / current_profile_4B_too_late_if_policy_resource_blowoff_waits_for_full_window_peak.

### R13_4B4C_C07_042700_HANMI_TCBONDER_ORDER_LATE_BLOWOFF

- **Underlying archetype:** `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`
- **Trigger:** `Stage4B` on `2024-06-07`, entry `2024-06-07` at `156800.0`.
- **Evidence family:** real_hbm_equipment_order_but_late_valuation_positioning_overheat.
- **Stage2 fields:** customer_or_order_quality, named_equipment, relative_strength.
- **Stage3 fields:** order_quality_supported, but_forward_revision_bridge_limited.
- **4B fields:** valuation_blowoff, positioning_overheat, late_entry_after_parabolic_rs.
- **4C fields:** none.
- **Interpretation:** real_order_needs_4b_overlay_not_positive_promotion / current_profile_false_positive_if_order_quality_overrides_blowoff_location.

### R13_4B4C_C02_006340_DAEWON_PRICE_ONLY_GRID_THEME

- **Underlying archetype:** `C02_POWER_GRID_DATACENTER_CAPEX`
- **Trigger:** `Stage4B` on `2024-06-26`, entry `2024-06-27` at `4350.0`.
- **Evidence family:** price_only_transformer_expectation_without_order_margin_bridge.
- **Stage2 fields:** relative_strength_only, sector_theme_proxy.
- **Stage3 fields:** none.
- **4B fields:** price_only_local_peak, valuation_blowoff, source_proxy_only.
- **4C fields:** positive_stage_evidence_absent_but_thesis_break_not_direct.
- **Interpretation:** price_only_4b_watch_blocks_stage2_false_positive / current_profile_false_positive_if_price_only_theme_given_actionable_bonus.

### R13_4B4C_C12_066970_LNF_INVENTORY_VALUATION_LOSS_TRUE_4C

- **Underlying archetype:** `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`
- **Trigger:** `Stage4C` on `2024-05-09`, entry `2024-05-10` at `153300.0`.
- **Evidence family:** inventory_valuation_loss_customer_demand_break_margin_damage.
- **Stage2 fields:** existing_customer_contract_vocabulary.
- **Stage3 fields:** not_supported_after_inventory_loss.
- **4B fields:** demand_slowdown, margin_or_backlog_slowdown.
- **4C fields:** inventory_valuation_loss, operating_loss_or_margin_break, customer_calloff_or_order_cut_risk.
- **Interpretation:** hard_4c_success_after_margin_inventory_break / current_profile_correct_only_if_hard_4c_routes_inventory_loss_to_thesis_break.

### R13_4B4C_C17_011170_LOTTECHEM_LOSS_SPREAD_BREAK_TRUE_4C

- **Underlying archetype:** `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`
- **Trigger:** `Stage4C` on `2024-02-08`, entry `2024-02-08` at `134700.0`.
- **Evidence family:** company_level_operating_loss_spread_cost_break.
- **Stage2 fields:** generic_spread_cycle_vocab_not_sufficient.
- **Stage3 fields:** none.
- **4B fields:** spread_pressure, earnings_miss.
- **4C fields:** sustained_operating_loss, company_level_margin_break, demand_and_spread_break.
- **Interpretation:** hard_4c_success_company_specific_loss / current_profile_correct_if_company_specific_loss_overrides_commodity_mean_reversion.

### R13_4B4C_C30_294870_HDC_CONSTRUCTION_TRUST_BREAK_TRUE_4C

- **Underlying archetype:** `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`
- **Trigger:** `Stage4C` on `2022-01-17`, entry `2022-01-17` at `18750.0`.
- **Evidence family:** construction_quality_trust_break_fatal_accident_management_accountability.
- **Stage2 fields:** construction_beta_not_sufficient.
- **Stage3 fields:** none.
- **4B fields:** accounting_or_trust_break_watch, legal_or_regulatory_block.
- **4C fields:** accounting_or_trust_break, forced_liquidation_or_crash_risk, thesis_evidence_broken.
- **Interpretation:** hard_4c_success_quality_trust_break / current_profile_too_late_if_balance_sheet_guard_waits_for_financial_statement_confirmation.

### R13_4B4C_C27_253450_STUDIO_DRAGON_HIT_WITHOUT_MONETIZATION

- **Underlying archetype:** `C27_CONTENT_IP_GLOBAL_MONETIZATION`
- **Trigger:** `Stage4C` on `2023-03-13`, entry `2023-03-13` at `76000.0`.
- **Evidence family:** global_hit_drama_without_listed_company_monetization_or_margin_bridge.
- **Stage2 fields:** global_hit_visibility, content_ip_popularity.
- **Stage3 fields:** revenue_share_or_margin_bridge_missing.
- **4B fields:** event_premium, valuation_blowoff.
- **4C fields:** monetization_bridge_absent, earnings_conversion_failure.
- **Interpretation:** hard_4c_when_hit_without_listed_company_economics / current_profile_false_positive_if_global_hit_counts_as_recurring_monetization.

### R13_4B4C_C28_263860_GENIANS_REVENUE_MILESTONE_NO_RETENTION

- **Underlying archetype:** `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION`
- **Trigger:** `Stage4C` on `2024-02-26`, entry `2024-02-26` at `13030.0`.
- **Evidence family:** official_revenue_milestone_without_forward_contract_retention_confirmation.
- **Stage2 fields:** software_security_revenue_milestone.
- **Stage3 fields:** ARR_or_retention_bridge_missing.
- **4B fields:** theme_premium, contract_retention_uncertainty.
- **4C fields:** forward_confirmation_absent, revenue_retention_bridge_failure.
- **Interpretation:** 4c_or_strict_cap_for_revenue_milestone_without_retention / current_profile_false_positive_if_revenue_milestone_counts_as_recurring_contract_visibility.

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R13L148_4B4C_T01_C16_005490_20230712 | 005490 | Stage4B | 2023-07-12 | 417500.0 | 82.99 | -6.71 | 82.99 | -6.71 | 82.99 | -7.31 | 2023-07-26 | 764000.0 | -49.35 |
| R13L148_4B4C_T02_C07_042700_20240607 | 042700 | Stage4B | 2024-06-07 | 156800.0 | 25.13 | -5.23 | 25.13 | -41.77 | 25.13 | -55.74 | 2024-06-14 | 196200.0 | -64.63 |
| R13L148_4B4C_T03_C02_006340_20240627 | 006340 | Stage4B | 2024-06-27 | 4350.0 | 9.7701 | -39.3103 | 9.7701 | -41.3793 | 9.7701 | -49.3103 | 2024-06-28 | 4775.0 | -53.822 |
| R13L148_4B4C_T04_C12_066970_20240510 | 066970 | Stage4C | 2024-05-10 | 153300.0 | 15.4599 | -4.6967 | 15.4599 | -45.923 | 15.4599 | -49.9674 | 2024-06-13 | 177000.0 | -56.67 |
| R13L148_4B4C_T05_C17_011170_20240208 | 011170 | Stage4C | 2024-02-08 | 134700.0 | 3.41 | -13.29 | 3.41 | -28.66 | 3.41 | -43.21 | 2024-02-19 | 139300.0 | -45.08 |
| R13L148_4B4C_T06_C30_294870_20220117 | 294870 | Stage4C | 2022-01-17 | 18750.0 | 5.6 | -28.0 | 5.6 | -29.87 | 5.6 | -45.33 | unknown_from_reused_sector_row | 19800.0 | -45.33 |
| R13L148_4B4C_T07_C27_253450_20230313 | 253450 | Stage4C | 2023-03-13 | 76000.0 | 2.89 | -11.58 | 2.89 | -36.12 | 2.89 | -39.47 | unknown_from_reused_sector_row | 78196.4 | -39.47 |
| R13L148_4B4C_T08_C28_263860_20240226 | 263860 | Stage4C | 2024-02-26 | 13030.0 | 5.3 | -11.13 | 5.3 | -32.54 | 5.3 | -36.22 | unknown_from_reused_sector_row | 13720.59 | -36.22 |

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| How would current profile judge these? | Many price/theme or broad-evidence rows still look Stage2/Yellow unless the existing guardrail catches them. |
| Did that match MFE/MAE? | Not consistently. Average 90D MAE is deep, and several rows have low MFE with large MAE. |
| Was Stage2 actionable bonus too much? | Too much for price/proxy-only rows and milestone-without-retention rows. |
| Was Yellow threshold too strict or loose? | Loose for C02/C27/C28 proxy rows, mostly adequate for C07 order-quality rows only if 4B overlay fires. |
| Was Green threshold too strict or loose? | Green remains appropriately strict; the residual problem is earlier Stage2/Yellow permissiveness and late 4B/4C escalation. |
| Price-only blowoff guard? | Correct but needs cross-scope reinforcement for sector-proxy rows where price is not the only weak input. |
| Full 4B non-price requirement? | Correct; R13 adds a timing split between reversible 4B watch and hard 4C escalation. |
| Hard 4C routing? | Correct when explicit company-specific thesis break exists, but should not fire from generic sector weakness alone. |

## 14. Stage2 / Yellow / Green Comparison

- Stage2/Yellow can still be too permissive when it accepts broad sector vocabulary, relative strength, or a single revenue milestone as if it were recurring evidence.
- Stage3-Green is not loosened. The R13 result supports keeping Green strict while improving earlier negative overlays.
- Green lateness ratio is `not_applicable_cross_4b4c_review` because this file tests negative overlays rather than positive Green timing.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local/full verdict | path lesson |
|---:|---|---|---|
| 005490 | valuation_blowoff + future capacity target | local watch, not hard 4C | A policy/resource value-day blowoff can have strong MFE before later drawdown; hard 4C is too severe without broken project evidence. |
| 042700 | real order + late positioning | good 4B timing | A real customer/order row can still need 4B if valuation location captures most near-term upside. |
| 006340 | price-only local peak | good price-only 4B block | Price/proxy-only theme should be blocked from Stage2/Yellow promotion and watched as 4B, not upgraded. |

## 16. 4C Protection Audit

| symbol | thesis-break evidence | MFE90 | MAE90 | protection label |
|---:|---|---:|---:|---|
| 066970 | inventory_valuation_loss, operating_loss_or_margin_break, customer_calloff_or_order_cut_risk | 15.46 | -45.92 | hard_4c_success_after_margin_inventory_break |
| 011170 | sustained_operating_loss, company_level_margin_break, demand_and_spread_break | 3.41 | -28.66 | hard_4c_success_company_specific_loss |
| 294870 | accounting_or_trust_break, forced_liquidation_or_crash_risk, thesis_evidence_broken | 5.60 | -29.87 | hard_4c_success_quality_trust_break |
| 253450 | monetization_bridge_absent, earnings_conversion_failure | 2.89 | -36.12 | hard_4c_when_hit_without_listed_company_economics |
| 263860 | forward_confirmation_absent, revenue_retention_bridge_failure | 5.30 | -32.54 | 4c_or_strict_cap_for_revenue_milestone_without_retention |

## 17. Sector-Specific Rule Candidate

No sector-specific production rule is proposed because R13 is cross-archetype. The sector lesson is that 4B and 4C evidence vocabularies must be interpreted within the underlying sector: order quality in HBM, inventory loss in battery, spread loss in chemicals, trust break in construction, monetization bridge in content, and retention bridge in software.

## 18. Canonical-Archetype Rule Candidate

**R13_4B_4C_NONPRICE_ESCALATION_GATE**:

- Keep reversible overheat, valuation blowoff, local peak, legal delay, and sector proxy weakness at `Stage4B` unless a company-specific thesis break is explicit.
- Escalate to `Stage4C` only when at least two hard-break fields are present: order/customer cancellation, confirmed qualification/regulatory failure, sustained operating/margin loss, trust/accounting break, commercialization/retention bridge failure, or forced liquidity/crash evidence.
- Do not let price-only or proxy-only rows promote Stage2/Yellow. Their role is negative-overlay calibration, not positive evidence.

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | changed_axes | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline proxy treats many rows as Stage2/Yellow unless existing generic guardrail fires | none | 8 | 18.82 | -32.87 | 18.82 | -40.82 | 0.750 | mixed; false-positive residual remains |
| P0b_e2r_2_0_baseline_reference | older baseline overweights theme and relative strength | none | 8 | 18.82 | -32.87 | 18.82 | -40.82 | 0.875 | poor; price/theme entries exposed to deep MAE |
| P1_cross_4b_nonprice_watch_profile | force 4B when overheat has non-price risk or price-only proxy | local_4b_watch_guard + cross_nonprice_escalation | 8 | 18.82 | -32.87 | 18.82 | -40.82 | 0.375 | better; 4B contains blowoff rows without killing all theses |
| P2_cross_4c_thesis_break_profile | hard 4C only with explicit company-specific break | hard_4c_confirmation + thesis_break_evidence_count | 8 | 18.82 | -32.87 | 18.82 | -40.82 | 0.250 | best balance; hard 4C rows have low MFE and deep MAE |
| P3_counterexample_guard_profile | blocks price/proxy-only positive promotions and escalates confirmed break | stage2_required_bridge + source_quality_gate | 8 | 18.82 | -32.87 | 18.82 | -40.82 | 0.125 | best guard; reduces false positives but keeps POSCO/Hanmi as watch rather than hard 4C |

## 20. Score-Return Alignment Matrix

| symbol | before_score | before_stage | after_score | after_stage | MFE90 | MAE90 | alignment |
|---:|---:|---|---:|---|---:|---:|---|
| 005490 | 74 | Stage2-Actionable | 59 | Stage4B | 82.99 | -6.71 | local_4b_watch_success_not_hard_4c |
| 042700 | 74 | Stage2-Actionable | 63 | Stage4B | 25.13 | -41.77 | real_order_needs_4b_overlay_not_positive_promotion |
| 006340 | 69 | Stage2-Actionable | 59 | Stage4B | 9.77 | -41.38 | price_only_4b_watch_blocks_stage2_false_positive |
| 066970 | 64 | Stage2 | 38 | Stage4C | 15.46 | -45.92 | hard_4c_success_after_margin_inventory_break |
| 011170 | 58 | Stage2 | 38 | Stage4C | 3.41 | -28.66 | hard_4c_success_company_specific_loss |
| 294870 | 58 | Stage2 | 38 | Stage4C | 5.60 | -29.87 | hard_4c_success_quality_trust_break |
| 253450 | 64 | Stage2 | 45 | Stage4C | 2.89 | -36.12 | hard_4c_when_hit_without_listed_company_economics |
| 263860 | 64 | Stage2 | 45 | Stage4C | 5.30 | -32.54 | 4c_or_strict_cap_for_revenue_milestone_without_retention |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE | 2 | 6 | 3 | 5 | 8 | 0 | 8 | 8 | 7 | no_sector_rule_R13_only | R13_4B_4C_NONPRICE_ESCALATION_GATE | improves cross-archetype 4B/4C timing and hard-4C split |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
underlying_sector_holdout_reference_count: 8
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, stage2_required_bridge]
residual_error_types_found: [price_proxy_positive_false_positive, real_order_late_valuation_blowoff, sector_proxy_4B_needed, company_specific_thesis_break_4C, monetization_bridge_failure, contract_retention_failure]
new_axis_proposed: R13_4B_4C_NONPRICE_ESCALATION_GATE
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_confirmation, stage2_required_bridge, drawdown_aware_confirmation]
existing_axis_weakened: []
existing_axis_kept: [stage3_green_total_min, stage3_green_revision_min]
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: R13_4B_4C_NONPRICE_ESCALATION_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

- Validation scope: historical Stock-Web OHLC path, 30D/90D/180D MFE/MAE, stage-overlay label comparison, R13 cross-archetype guardrail stress test.
- Non-validation scope: live candidate discovery, investment recommendation, production profile patch, brokerage execution, stock_agent source code review.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,R13_4B_4C_NONPRICE_ESCALATION_GATE,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"Require non-price escalation evidence to separate reversible 4B watch from hard 4C thesis break","Reduces Stage2/Yellow false positives while preserving 4B watch rows that should not be killed","R13L148_4B4C_T01_C16_005490_20230712|R13L148_4B4C_T02_C07_042700_20240607|R13L148_4B4C_T03_C02_006340_20240627|R13L148_4B4C_T04_C12_066970_20240510|R13L148_4B4C_T05_C17_011170_20240208|R13L148_4B4C_T06_C30_294870_20220117|R13L148_4B4C_T07_C27_253450_20230313|R13L148_4B4C_T08_C28_263860_20240226",8,8,6,medium,r13_shadow_only,"not production; post-calibrated residual"
shadow_weight,R13_PRICE_PROXY_BLOCK_BEFORE_4B_OR_4C,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"Price-only or source-proxy theme rows cannot promote positive stage and should become watch/protection rows","Contains Dae Won Cable, Studio Dragon, and Genians false-positive rows","R13L148_4B4C_T01_C16_005490_20230712|R13L148_4B4C_T03_C02_006340_20240627|R13L148_4B4C_T04_C12_066970_20240510|R13L148_4B4C_T06_C30_294870_20220117|R13L148_4B4C_T07_C27_253450_20230313|R13L148_4B4C_T08_C28_263860_20240226",6,6,6,medium,r13_shadow_only,"source quality gate"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13_4B4C_C16_005490_POSCO_RESOURCE_VALUE_DAY_LOCAL_4B","symbol":"005490","company_name":"POSCO홀딩스","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"local_4b_watch_success_not_hard_4c","current_profile_verdict":"current_profile_4B_too_late_if_policy_resource_blowoff_waits_for_full_window_peak","price_source":"Songdaiki/stock-web","notes":"R13 cross-scope holdout from R4 / C16_STRATEGIC_RESOURCE_POLICY_SUPPLY; source file e2r_stock_web_v12_residual_round_R4_loop_105_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md"}
{"row_type":"case","case_id":"R13_4B4C_C07_042700_HANMI_TCBONDER_ORDER_LATE_BLOWOFF","symbol":"042700","company_name":"한미반도체","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"real_order_needs_4b_overlay_not_positive_promotion","current_profile_verdict":"current_profile_false_positive_if_order_quality_overrides_blowoff_location","price_source":"Songdaiki/stock-web","notes":"R13 cross-scope holdout from R2 / C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH; source file e2r_stock_web_v12_residual_round_R2_loop_128_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md"}
{"row_type":"case","case_id":"R13_4B4C_C02_006340_DAEWON_PRICE_ONLY_GRID_THEME","symbol":"006340","company_name":"대원전선","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_only_4b_watch_blocks_stage2_false_positive","current_profile_verdict":"current_profile_false_positive_if_price_only_theme_given_actionable_bonus","price_source":"Songdaiki/stock-web","notes":"R13 cross-scope holdout from R1 / C02_POWER_GRID_DATACENTER_CAPEX; source file e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"case","case_id":"R13_4B4C_C12_066970_LNF_INVENTORY_VALUATION_LOSS_TRUE_4C","symbol":"066970","company_name":"엘앤에프","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_success_after_margin_inventory_break","current_profile_verdict":"current_profile_correct_only_if_hard_4c_routes_inventory_loss_to_thesis_break","price_source":"Songdaiki/stock-web","notes":"R13 cross-scope holdout from R3 / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK; source file e2r_stock_web_v12_residual_round_R3_loop_126_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"case","case_id":"R13_4B4C_C17_011170_LOTTECHEM_LOSS_SPREAD_BREAK_TRUE_4C","symbol":"011170","company_name":"롯데케미칼","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_success_company_specific_loss","current_profile_verdict":"current_profile_correct_if_company_specific_loss_overrides_commodity_mean_reversion","price_source":"Songdaiki/stock-web","notes":"R13 cross-scope holdout from R4 / C17_CHEMICAL_COMMODITY_MARGIN_SPREAD; source file e2r_stock_web_v12_residual_round_R4_loop_106_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md"}
{"row_type":"case","case_id":"R13_4B4C_C30_294870_HDC_CONSTRUCTION_TRUST_BREAK_TRUE_4C","symbol":"294870","company_name":"HDC현대산업개발","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_success_quality_trust_break","current_profile_verdict":"current_profile_too_late_if_balance_sheet_guard_waits_for_financial_statement_confirmation","price_source":"Songdaiki/stock-web","notes":"R13 cross-scope holdout from R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK; source file e2r_stock_web_v12_residual_round_R10_loop_138_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"case","case_id":"R13_4B4C_C27_253450_STUDIO_DRAGON_HIT_WITHOUT_MONETIZATION","symbol":"253450","company_name":"스튜디오드래곤","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"hard_4c_when_hit_without_listed_company_economics","current_profile_verdict":"current_profile_false_positive_if_global_hit_counts_as_recurring_monetization","price_source":"Songdaiki/stock-web","notes":"R13 cross-scope holdout from R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION; source file e2r_stock_web_v12_residual_round_R8_loop_142_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"case","case_id":"R13_4B4C_C28_263860_GENIANS_REVENUE_MILESTONE_NO_RETENTION","symbol":"263860","company_name":"지니언스","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4c_or_strict_cap_for_revenue_milestone_without_retention","current_profile_verdict":"current_profile_false_positive_if_revenue_milestone_counts_as_recurring_contract_visibility","price_source":"Songdaiki/stock-web","notes":"R13 cross-scope holdout from R8 / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION; source file e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"trigger","trigger_id":"R13L148_4B4C_T01_C16_005490_20230712","case_id":"R13_4B4C_C16_005490_POSCO_RESOURCE_VALUE_DAY_LOCAL_4B","symbol":"005490","company_name":"POSCO홀딩스","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","source_round":"R4","loop_objective":"4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; holdout_validation; counterexample_mining","trigger_type":"Stage4B","trigger_date":"2023-07-11","entry_date":"2023-07-12","entry_price":417500.0,"evidence_available_at_that_date":true,"evidence_source":"Asia Business Daily article on POSCO Future Materials lithium/nickel/battery-material targets and 2030 value day; prior C16 row treated this as policy-resource blowoff watch.","evidence_url":"https://www.asiae.co.kr/en/article/2023071114413620672","stage2_evidence_fields":["policy_or_regulatory_optionality","resource_capacity_target","strategic_supply_chain_vocabulary"],"stage3_evidence_fields":["not_yet_cashflow_conversion","not_yet_margin_bridge"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","future_capacity_target_without_current_margin_bridge"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv","profile_path":"atlas/symbol_profiles/005/005490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":82.99,"MFE_90D_pct":82.99,"MFE_180D_pct":82.99,"MAE_30D_pct":-6.71,"MAE_90D_pct":-6.71,"MAE_180D_pct":-7.31,"peak_date":"2023-07-26","peak_price":764000.0,"drawdown_after_peak_pct":-49.35,"green_lateness_ratio":"not_applicable_cross_4b4c_review","four_b_local_peak_proximity":0.55,"four_b_full_window_peak_proximity":0.55,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["valuation_blowoff","positioning_overheat","future_capacity_target_without_current_margin_bridge"],"four_c_protection_label":"not_4c","trigger_outcome_label":"local_4b_watch_success_not_hard_4c","current_profile_verdict":"current_profile_4B_too_late_if_policy_resource_blowoff_waits_for_full_window_peak","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|005490|2023-07-12","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false,"underlying_sector_source_file":"e2r_stock_web_v12_residual_round_R4_loop_105_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md"}
{"row_type":"trigger","trigger_id":"R13L148_4B4C_T02_C07_042700_20240607","case_id":"R13_4B4C_C07_042700_HANMI_TCBONDER_ORDER_LATE_BLOWOFF","symbol":"042700","company_name":"한미반도체","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","source_round":"R2","loop_objective":"4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; holdout_validation; counterexample_mining","trigger_type":"Stage4B","trigger_date":"2024-06-07","entry_date":"2024-06-07","entry_price":156800.0,"evidence_available_at_that_date":true,"evidence_source":"KED Global report on Hanmi Semiconductor Dual TC Bonder Griffin order / SK hynix HBM supply-chain context; prior C07 row classified non-price 4B because order was real but price location was late.","evidence_url":"https://www.kedglobal.com/korean-chipmakers/newsView/ked202406070008","stage2_evidence_fields":["customer_or_order_quality","named_equipment","relative_strength"],"stage3_evidence_fields":["order_quality_supported","but_forward_revision_bridge_limited"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","late_entry_after_parabolic_rs"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.13,"MFE_90D_pct":25.13,"MFE_180D_pct":25.13,"MAE_30D_pct":-5.23,"MAE_90D_pct":-41.77,"MAE_180D_pct":-55.74,"peak_date":"2024-06-14","peak_price":196200.0,"drawdown_after_peak_pct":-64.63,"green_lateness_ratio":"not_applicable_cross_4b4c_review","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.65,"four_b_timing_verdict":"good_full_window_4b_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","late_entry_after_parabolic_rs"],"four_c_protection_label":"not_4c","trigger_outcome_label":"real_order_needs_4b_overlay_not_positive_promotion","current_profile_verdict":"current_profile_false_positive_if_order_quality_overrides_blowoff_location","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|042700|2024-06-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"underlying_sector_source_file":"e2r_stock_web_v12_residual_round_R2_loop_128_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md"}
{"row_type":"trigger","trigger_id":"R13L148_4B4C_T03_C02_006340_20240627","case_id":"R13_4B4C_C02_006340_DAEWON_PRICE_ONLY_GRID_THEME","symbol":"006340","company_name":"대원전선","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","source_round":"R1","loop_objective":"4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; holdout_validation; counterexample_mining","trigger_type":"Stage4B","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":4350.0,"evidence_available_at_that_date":true,"evidence_source":"Mirae Asset transformer/grid theme notes used as sector proxy in prior C02 row; no symbol-level order/backlog/margin bridge for Dae Won Cable at trigger.","evidence_url":"https://securities.miraeasset.com/bbs/download/2129191.pdf?attachmentId=2129191","stage2_evidence_fields":["relative_strength_only","sector_theme_proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","source_proxy_only"],"stage4c_evidence_fields":["positive_stage_evidence_absent_but_thesis_break_not_direct"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv","profile_path":"atlas/symbol_profiles/006/006340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.7701,"MFE_90D_pct":9.7701,"MFE_180D_pct":9.7701,"MAE_30D_pct":-39.3103,"MAE_90D_pct":-41.3793,"MAE_180D_pct":-49.3103,"peak_date":"2024-06-28","peak_price":4775.0,"drawdown_after_peak_pct":-53.822,"green_lateness_ratio":"not_applicable_cross_4b4c_review","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"good_full_window_4b_timing","four_b_evidence_type":["price_only_local_peak","valuation_blowoff","source_proxy_only"],"four_c_protection_label":"not_4c","trigger_outcome_label":"price_only_4b_watch_blocks_stage2_false_positive","current_profile_verdict":"current_profile_false_positive_if_price_only_theme_given_actionable_bonus","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006340|2024-06-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false,"underlying_sector_source_file":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","trigger_id":"R13L148_4B4C_T04_C12_066970_20240510","case_id":"R13_4B4C_C12_066970_LNF_INVENTORY_VALUATION_LOSS_TRUE_4C","symbol":"066970","company_name":"엘앤에프","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_round":"R3","loop_objective":"4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; holdout_validation; counterexample_mining","trigger_type":"Stage4C","trigger_date":"2024-05-09","entry_date":"2024-05-10","entry_price":153300.0,"evidence_available_at_that_date":true,"evidence_source":"Asia Business Daily article on L&F Q1 results; prior C12 row linked inventory valuation loss and weak battery customer demand to true 4C protection.","evidence_url":"https://www.asiae.co.kr/en/article/2024050915570493698","stage2_evidence_fields":["existing_customer_contract_vocabulary"],"stage3_evidence_fields":["not_supported_after_inventory_loss"],"stage4b_evidence_fields":["demand_slowdown","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["inventory_valuation_loss","operating_loss_or_margin_break","customer_calloff_or_order_cut_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.4599,"MFE_90D_pct":15.4599,"MFE_180D_pct":15.4599,"MAE_30D_pct":-4.6967,"MAE_90D_pct":-45.923,"MAE_180D_pct":-49.9674,"peak_date":"2024-06-13","peak_price":177000.0,"drawdown_after_peak_pct":-56.67,"green_lateness_ratio":"not_applicable_cross_4b4c_review","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage4c","four_b_evidence_type":["demand_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_after_margin_inventory_break","trigger_outcome_label":"hard_4c_success_after_margin_inventory_break","current_profile_verdict":"current_profile_correct_only_if_hard_4c_routes_inventory_loss_to_thesis_break","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|066970|2024-05-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false,"underlying_sector_source_file":"e2r_stock_web_v12_residual_round_R3_loop_126_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"trigger","trigger_id":"R13L148_4B4C_T05_C17_011170_20240208","case_id":"R13_4B4C_C17_011170_LOTTECHEM_LOSS_SPREAD_BREAK_TRUE_4C","symbol":"011170","company_name":"롯데케미칼","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","source_round":"R4","loop_objective":"4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; holdout_validation; counterexample_mining","trigger_type":"Stage4C","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":134700.0,"evidence_available_at_that_date":true,"evidence_source":"Lotte Chemical official 2023 business-performance release; prior C17 row cited consolidated operating loss, basic-materials spread weakness, and reduced demand.","evidence_url":"https://www.lottechem.com/en/media/news/list.do","stage2_evidence_fields":["generic_spread_cycle_vocab_not_sufficient"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["spread_pressure","earnings_miss"],"stage4c_evidence_fields":["sustained_operating_loss","company_level_margin_break","demand_and_spread_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.41,"MFE_90D_pct":3.41,"MFE_180D_pct":3.41,"MAE_30D_pct":-13.29,"MAE_90D_pct":-28.66,"MAE_180D_pct":-43.21,"peak_date":"2024-02-19","peak_price":139300.0,"drawdown_after_peak_pct":-45.08,"green_lateness_ratio":"not_applicable_cross_4b4c_review","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage4c","four_b_evidence_type":["spread_pressure","earnings_miss"],"four_c_protection_label":"hard_4c_success_company_specific_loss","trigger_outcome_label":"hard_4c_success_company_specific_loss","current_profile_verdict":"current_profile_correct_if_company_specific_loss_overrides_commodity_mean_reversion","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|011170|2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"underlying_sector_source_file":"e2r_stock_web_v12_residual_round_R4_loop_106_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md"}
{"row_type":"trigger","trigger_id":"R13L148_4B4C_T06_C30_294870_20220117","case_id":"R13_4B4C_C30_294870_HDC_CONSTRUCTION_TRUST_BREAK_TRUE_4C","symbol":"294870","company_name":"HDC현대산업개발","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_round":"R10","loop_objective":"4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; holdout_validation; counterexample_mining","trigger_type":"Stage4C","trigger_date":"2022-01-17","entry_date":"2022-01-17","entry_price":18750.0,"evidence_available_at_that_date":true,"evidence_source":"Prior C30 row: construction-quality and trust break after fatal accident / accountability event, not merely PF beta.","evidence_url":"https://en.yna.co.kr/","stage2_evidence_fields":["construction_beta_not_sufficient"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["accounting_or_trust_break_watch","legal_or_regulatory_block"],"stage4c_evidence_fields":["accounting_or_trust_break","forced_liquidation_or_crash_risk","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2022.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.6,"MFE_90D_pct":5.6,"MFE_180D_pct":5.6,"MAE_30D_pct":-28.0,"MAE_90D_pct":-29.87,"MAE_180D_pct":-45.33,"peak_date":"unknown_from_reused_sector_row","peak_price":19800.0,"drawdown_after_peak_pct":-45.33,"green_lateness_ratio":"not_applicable_cross_4b4c_review","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage4c","four_b_evidence_type":["accounting_or_trust_break_watch","legal_or_regulatory_block"],"four_c_protection_label":"hard_4c_success_quality_trust_break","trigger_outcome_label":"hard_4c_success_quality_trust_break","current_profile_verdict":"current_profile_too_late_if_balance_sheet_guard_waits_for_financial_statement_confirmation","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|294870|2022-01-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false,"underlying_sector_source_file":"e2r_stock_web_v12_residual_round_R10_loop_138_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"trigger","trigger_id":"R13L148_4B4C_T07_C27_253450_20230313","case_id":"R13_4B4C_C27_253450_STUDIO_DRAGON_HIT_WITHOUT_MONETIZATION","symbol":"253450","company_name":"스튜디오드래곤","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_round":"R8","loop_objective":"4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; holdout_validation; counterexample_mining","trigger_type":"Stage4C","trigger_date":"2023-03-13","entry_date":"2023-03-13","entry_price":76000.0,"evidence_available_at_that_date":true,"evidence_source":"Yonhap/industry coverage of The Glory global hit used in prior C27 row; R13 checks whether IP popularity alone should escalate to 4B/4C protection.","evidence_url":"https://en.yna.co.kr/view/AEN20230313003200315","stage2_evidence_fields":["global_hit_visibility","content_ip_popularity"],"stage3_evidence_fields":["revenue_share_or_margin_bridge_missing"],"stage4b_evidence_fields":["event_premium","valuation_blowoff"],"stage4c_evidence_fields":["monetization_bridge_absent","earnings_conversion_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv","profile_path":"atlas/symbol_profiles/253/253450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.89,"MFE_90D_pct":2.89,"MFE_180D_pct":2.89,"MAE_30D_pct":-11.58,"MAE_90D_pct":-36.12,"MAE_180D_pct":-39.47,"peak_date":"unknown_from_reused_sector_row","peak_price":78196.4,"drawdown_after_peak_pct":-39.47,"green_lateness_ratio":"not_applicable_cross_4b4c_review","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage4c","four_b_evidence_type":["event_premium","valuation_blowoff"],"four_c_protection_label":"hard_4c_when_hit_without_listed_company_economics","trigger_outcome_label":"hard_4c_when_hit_without_listed_company_economics","current_profile_verdict":"current_profile_false_positive_if_global_hit_counts_as_recurring_monetization","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|253450|2023-03-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false,"underlying_sector_source_file":"e2r_stock_web_v12_residual_round_R8_loop_142_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"trigger","trigger_id":"R13L148_4B4C_T08_C28_263860_20240226","case_id":"R13_4B4C_C28_263860_GENIANS_REVENUE_MILESTONE_NO_RETENTION","symbol":"263860","company_name":"지니언스","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"CROSS_ARCHETYPE_4B_WATCH_VS_HARD_4C_ESCALATION_GATE","underlying_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","source_round":"R8","loop_objective":"4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; holdout_validation; counterexample_mining","trigger_type":"Stage4C","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":13030.0,"evidence_available_at_that_date":true,"evidence_source":"Prior C28 row: revenue milestone / security-software vocabulary without fresh ARR, renewal, managed-service or contract-retention bridge.","evidence_url":"https://www.genians.co.kr/","stage2_evidence_fields":["software_security_revenue_milestone"],"stage3_evidence_fields":["ARR_or_retention_bridge_missing"],"stage4b_evidence_fields":["theme_premium","contract_retention_uncertainty"],"stage4c_evidence_fields":["forward_confirmation_absent","revenue_retention_bridge_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv","profile_path":"atlas/symbol_profiles/263/263860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.3,"MFE_90D_pct":5.3,"MFE_180D_pct":5.3,"MAE_30D_pct":-11.13,"MAE_90D_pct":-32.54,"MAE_180D_pct":-36.22,"peak_date":"unknown_from_reused_sector_row","peak_price":13720.59,"drawdown_after_peak_pct":-36.22,"green_lateness_ratio":"not_applicable_cross_4b4c_review","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage4c","four_b_evidence_type":["theme_premium","contract_retention_uncertainty"],"four_c_protection_label":"4c_or_strict_cap_for_revenue_milestone_without_retention","trigger_outcome_label":"4c_or_strict_cap_for_revenue_milestone_without_retention","current_profile_verdict":"current_profile_false_positive_if_revenue_milestone_counts_as_recurring_contract_visibility","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|263860|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false,"underlying_sector_source_file":"e2r_stock_web_v12_residual_round_R8_loop_143_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_4B4C_C16_005490_POSCO_RESOURCE_VALUE_DAY_LOCAL_4B","trigger_id":"R13L148_4B4C_T01_C16_005490_20230712","symbol":"005490","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","underlying_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":90,"customer_quality_score":35,"policy_or_regulatory_score":80,"valuation_repricing_score":95,"execution_risk_score":45,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":80,"valuation_repricing_score":100,"execution_risk_score":55,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":59,"stage_label_after":"Stage4B","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"R13 cross-scope shadow profile separates reversible 4B watch from hard 4C thesis break using non-price escalation evidence and forward MFE/MAE asymmetry.","MFE_90D_pct":82.99,"MAE_90D_pct":-6.71,"score_return_alignment_label":"local_4b_watch_success_not_hard_4c","current_profile_verdict":"current_profile_4B_too_late_if_policy_resource_blowoff_waits_for_full_window_peak"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_4B4C_C07_042700_HANMI_TCBONDER_ORDER_LATE_BLOWOFF","trigger_id":"R13L148_4B4C_T02_C07_042700_20240607","symbol":"042700","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","underlying_canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":95,"customer_quality_score":65,"policy_or_regulatory_score":35,"valuation_repricing_score":92,"execution_risk_score":55,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":85,"customer_quality_score":65,"policy_or_regulatory_score":35,"valuation_repricing_score":97,"execution_risk_score":65,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":63,"stage_label_after":"Stage4B","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"R13 cross-scope shadow profile separates reversible 4B watch from hard 4C thesis break using non-price escalation evidence and forward MFE/MAE asymmetry.","MFE_90D_pct":25.13,"MAE_90D_pct":-41.77,"score_return_alignment_label":"real_order_needs_4b_overlay_not_positive_promotion","current_profile_verdict":"current_profile_false_positive_if_order_quality_overrides_blowoff_location"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_4B4C_C02_006340_DAEWON_PRICE_ONLY_GRID_THEME","trigger_id":"R13L148_4B4C_T03_C02_006340_20240627","symbol":"006340","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","underlying_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":90,"customer_quality_score":10,"policy_or_regulatory_score":35,"valuation_repricing_score":88,"execution_risk_score":70,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":25,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":80,"customer_quality_score":10,"policy_or_regulatory_score":35,"valuation_repricing_score":93,"execution_risk_score":80,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":59,"stage_label_after":"Stage4B","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"R13 cross-scope shadow profile separates reversible 4B watch from hard 4C thesis break using non-price escalation evidence and forward MFE/MAE asymmetry.","MFE_90D_pct":9.7701,"MAE_90D_pct":-41.3793,"score_return_alignment_label":"price_only_4b_watch_blocks_stage2_false_positive","current_profile_verdict":"current_profile_false_positive_if_price_only_theme_given_actionable_bonus"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_4B4C_C12_066970_LNF_INVENTORY_VALUATION_LOSS_TRUE_4C","trigger_id":"R13L148_4B4C_T04_C12_066970_20240510","symbol":"066970","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","underlying_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":15,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":45,"customer_quality_score":30,"policy_or_regulatory_score":20,"valuation_repricing_score":50,"execution_risk_score":90,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":10,"accounting_trust_risk_score":45},"weighted_score_before":64,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":15,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":45,"customer_quality_score":30,"policy_or_regulatory_score":20,"valuation_repricing_score":40,"execution_risk_score":100,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":10,"accounting_trust_risk_score":53},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"R13 cross-scope shadow profile separates reversible 4B watch from hard 4C thesis break using non-price escalation evidence and forward MFE/MAE asymmetry.","MFE_90D_pct":15.4599,"MAE_90D_pct":-45.923,"score_return_alignment_label":"hard_4c_success_after_margin_inventory_break","current_profile_verdict":"current_profile_correct_only_if_hard_4c_routes_inventory_loss_to_thesis_break"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_4B4C_C17_011170_LOTTECHEM_LOSS_SPREAD_BREAK_TRUE_4C","trigger_id":"R13L148_4B4C_T05_C17_011170_20240208","symbol":"011170","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","underlying_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":45,"customer_quality_score":20,"policy_or_regulatory_score":20,"valuation_repricing_score":50,"execution_risk_score":85,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":10,"accounting_trust_risk_score":20},"weighted_score_before":58,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":45,"customer_quality_score":20,"policy_or_regulatory_score":20,"valuation_repricing_score":40,"execution_risk_score":95,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":10,"accounting_trust_risk_score":28},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"R13 cross-scope shadow profile separates reversible 4B watch from hard 4C thesis break using non-price escalation evidence and forward MFE/MAE asymmetry.","MFE_90D_pct":3.41,"MAE_90D_pct":-28.66,"score_return_alignment_label":"hard_4c_success_company_specific_loss","current_profile_verdict":"current_profile_correct_if_company_specific_loss_overrides_commodity_mean_reversion"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_4B4C_C30_294870_HDC_CONSTRUCTION_TRUST_BREAK_TRUE_4C","trigger_id":"R13L148_4B4C_T06_C30_294870_20220117","symbol":"294870","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","underlying_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":45,"customer_quality_score":20,"policy_or_regulatory_score":20,"valuation_repricing_score":50,"execution_risk_score":85,"legal_or_contract_risk_score":90,"dilution_cb_risk_score":10,"accounting_trust_risk_score":90},"weighted_score_before":58,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":10,"revision_score":15,"relative_strength_score":45,"customer_quality_score":20,"policy_or_regulatory_score":20,"valuation_repricing_score":40,"execution_risk_score":95,"legal_or_contract_risk_score":100,"dilution_cb_risk_score":10,"accounting_trust_risk_score":98},"weighted_score_after":38,"stage_label_after":"Stage4C","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"R13 cross-scope shadow profile separates reversible 4B watch from hard 4C thesis break using non-price escalation evidence and forward MFE/MAE asymmetry.","MFE_90D_pct":5.6,"MAE_90D_pct":-29.87,"score_return_alignment_label":"hard_4c_success_quality_trust_break","current_profile_verdict":"current_profile_too_late_if_balance_sheet_guard_waits_for_financial_statement_confirmation"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_4B4C_C27_253450_STUDIO_DRAGON_HIT_WITHOUT_MONETIZATION","trigger_id":"R13L148_4B4C_T07_C27_253450_20230313","symbol":"253450","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","underlying_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":5,"revision_score":15,"relative_strength_score":65,"customer_quality_score":15,"policy_or_regulatory_score":20,"valuation_repricing_score":50,"execution_risk_score":70,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":10,"accounting_trust_risk_score":45},"weighted_score_before":64,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":5,"revision_score":15,"relative_strength_score":65,"customer_quality_score":15,"policy_or_regulatory_score":20,"valuation_repricing_score":40,"execution_risk_score":80,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":10,"accounting_trust_risk_score":53},"weighted_score_after":45,"stage_label_after":"Stage4C","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"R13 cross-scope shadow profile separates reversible 4B watch from hard 4C thesis break using non-price escalation evidence and forward MFE/MAE asymmetry.","MFE_90D_pct":2.89,"MAE_90D_pct":-36.12,"score_return_alignment_label":"hard_4c_when_hit_without_listed_company_economics","current_profile_verdict":"current_profile_false_positive_if_global_hit_counts_as_recurring_monetization"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13_4B4C_C28_263860_GENIANS_REVENUE_MILESTONE_NO_RETENTION","trigger_id":"R13L148_4B4C_T08_C28_263860_20240226","symbol":"263860","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","underlying_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":15,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":45,"customer_quality_score":25,"policy_or_regulatory_score":20,"valuation_repricing_score":50,"execution_risk_score":65,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":10,"accounting_trust_risk_score":45},"weighted_score_before":64,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":15,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":45,"customer_quality_score":25,"policy_or_regulatory_score":20,"valuation_repricing_score":40,"execution_risk_score":75,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":10,"accounting_trust_risk_score":53},"weighted_score_after":45,"stage_label_after":"Stage4C","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"R13 cross-scope shadow profile separates reversible 4B watch from hard 4C thesis break using non-price escalation evidence and forward MFE/MAE asymmetry.","MFE_90D_pct":5.3,"MAE_90D_pct":-32.54,"score_return_alignment_label":"4c_or_strict_cap_for_revenue_milestone_without_retention","current_profile_verdict":"current_profile_false_positive_if_revenue_milestone_counts_as_recurring_contract_visibility"}
{"row_type":"residual_contribution","round":"R13","loop":148,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":8,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_confirmation","stage2_required_bridge"],"residual_error_types_found":["price_proxy_positive_false_positive","real_order_late_valuation_blowoff","company_specific_thesis_break_4C","monetization_bridge_failure","contract_retention_failure"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 8
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
1. Use only calibration_usable=true rows for quantitative calibration.
2. Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
3. Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
4. Do not apply global deltas unless multiple large_sector_id values support the same direction.
5. Prefer sector_specific or canonical_archetype_specific shadow profiles.
6. Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
7. 4B rows are overlay/risk calibration only.
8. 4C rows are thesis-break/protection calibration only.
9. price-only rows cannot promote Stage2/Stage3.
10. If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
11. Production scoring must not change unless the user explicitly asks for another promotion batch.

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

## 27. Next Round State

```yaml
completed_round: R13
completed_loop: 148
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — R13 4B/4C cross-archetype RedTeam
next_recommended_archetypes: [R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C31_POLICY_SUBSIDY_LEGISLATION_EVENT]
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Underlying sector rows are cited by source file name in each machine-readable case row. These are holdout references for R13 cross-scope timing; production scoring remains unchanged.
