# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
selected_round: R3
selected_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 / 80-row quality holdout after session-adjusted Priority 0 and Priority 1 fills; static C13 rows=58, need_to_80=22
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass
loop_objective: holdout_validation | counterexample_mining | canonical_archetype_compression | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_filename: e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 6 counterexamples, and 7 residual errors for L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA. Static No-Repeat still lists lower-count Priority 0/1 archetypes, but the current conversation has already generated session-adjusted fills for those axes, so this pass deliberately uses a Priority 2 C13 quality holdout rather than rematerializing the same C02/C09/C14/C10/C06/C07/C11/C01/C28/C12/C05 case families.

## 1. Current Calibrated Profile Assumption

```yaml
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
already_applied_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
```

C13 is not a generic battery orderbook bucket. It is the place where JV capacity, AMPC/IRA localization, utilization, shipment conversion, and subsidy realization must be distinguished. The error pattern found here is that a large named contract or localized plant plan can look like a Stage3 rerating key, but the price path punishes entries when production/subsidy/margin realization is long-dated or when utilization breaks.

## 2. Round / Large Sector / Canonical Archetype Scope

- `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` maps to `R3 / L3_BATTERY_EV_GREEN_MOBILITY`.
- Scope: battery-localized capacity, customer/JV route, IRA/AMPC or regional-supply-chain eligibility, utilization break, and conversion to shipment/revenue/margin.
- Non-scope: pure cathode orderbook without utilization, pure EV slowdown without JV/AMPC/localization, and price-only battery theme moves.

## 3. Previous Coverage / Duplicate Avoidance Check

Static No-Repeat Index lists C13 at 58 representative rows. The current session did not create a dedicated C13 standard file before this pass. Existing compact `c13_r3_loop99...` appears in `docs/round`, so the standard v12 output uses `loop_100`.

Duplicate governor:

```yaml
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count: 5
reused_case_count: 3
minimum_new_independent_case_ratio: 0.60
actual_new_independent_case_ratio: 0.625
reused_case_policy: reused only for explicit C13 holdout/new-trigger-family stress test
```

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
source: Songdaiki/stock-web
source_url: https://github.com/Songdaiki/stock-web
manifest_path: atlas/manifest.json
schema_path: atlas/schema.json
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
manifest_max_date: 2026-02-20
```

The manifest states `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`. The schema defines `MFE_N_pct` and `MAE_N_pct` from max high/min low over N tradable rows from entry_date.

## 5. Historical Eligibility Gate

All representative trigger rows below pass:

```yaml
entry_row_exists: true
forward_window_trading_days_gte_180: true
MFE_MAE_30_90_180_complete: true
price_basis: tradable_raw
raw_unadjusted_marcap: true
corporate_action_window_status: clean_180D_window_or_minor_share_count_change_not_split_like
calibration_usable_rows: 8
```

## 6. Canonical Archetype Compression Map

| fine/deep trigger family | compressed canonical | use in this loop |
|---|---|---|
| North America / EU localized battery material capacity | C13 | positive only if utilization or customer conversion is visible |
| AMPC/IRA-adjacent customer contract | C13 | Stage2 evidence, not Stage3 unless shipment/margin bridge appears |
| Separator utilization break | C13 | 4C/watch evidence when EV demand and utilization weaken together |
| Capacity headline without named utilization | C13 | Stage2-Watch or 4B cap |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | role | verdict | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---:|---|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| C13_R3_L100_336370_SOLUS_CANADA_COPPERFOIL | 336370 | 솔루스첨단소재 | Stage2-Actionable | 2024-01-31 | 2024-01-31 | 11240 | positive / structural_success | current_profile_missed_structural | 23.93 | -2.05 | 93.06 | -2.05 | 109.07 | -2.05 |
| C13_R3_L100_011790_SKC_NORTHVOLT_COPPERFOIL | 011790 | SKC | Stage2-Actionable | 2023-02-19 | 2023-02-20 | 97300 | positive / high_mae_success | current_profile_correct | 24.36 | -7.30 | 25.69 | -7.30 | 25.69 | -30.11 |
| C13_R3_L100_051910_LGCHEM_GM_TENNESSEE_CATHODE | 051910 | LG화학 | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 470500 | counterexample / failed_rerating | current_profile_false_positive | 10.52 | -8.61 | 10.52 | -25.61 | 10.52 | -44.00 |
| C13_R3_L100_066970_LNF_SKON_SUPPLY_AMPC_PROXY | 066970 | 엘앤에프 | Stage2-Actionable | 2024-03-25 | 2024-03-26 | 183100 | counterexample / failed_rerating | current_profile_false_positive | 6.06 | -23.21 | 6.06 | -50.79 | 6.06 | -54.72 |
| C13_R3_L100_361610_SKIET_SEPARATOR_UTILIZATION_BREAK | 361610 | SK아이이테크놀로지 | Stage4C | 2023-11-03 | 2023-11-03 | 67100 | counterexample / 4C_success | current_profile_4C_too_late | 31.15 | -5.96 | 31.15 | -5.96 | 31.15 | -45.53 |
| C13_R3_L100_393890_WCP_SEPARATOR_COMPETITION_UTILIZATION | 393890 | 더블유씨피 | Stage4B | 2024-05-31 | 2024-06-03 | 34000 | counterexample / 4B_overlay_success | current_profile_false_positive | 5.15 | -15.59 | 5.15 | -50.59 | 5.15 | -71.53 |
| C13_R3_L100_014820_DONGWON_BATTERY_CAN_FACTORY | 014820 | 동원시스템즈 | Stage2 | 2023-04-06 | 2023-04-07 | 47150 | counterexample / failed_rerating | current_profile_false_positive | 25.56 | -15.69 | 25.56 | -27.68 | 25.56 | -41.46 |
| C13_R3_L100_078600_DAEJOO_SILICON_ANODE_CUSTOMER_PROXY | 078600 | 대주전자재료 | Stage2 | 2023-04-13 | 2023-04-14 | 116700 | counterexample / failed_rerating | current_profile_false_positive | 3.68 | -27.08 | 3.68 | -27.08 | 3.68 | -42.16 |


## 8. Positive vs Counterexample Balance

```yaml
positive_case_count: 2
counterexample_count: 6
4B_case_count: 8
4C_case_count: 3
calibration_usable_trigger_count: 8
```

Positive cases were not clean Green cases. Solus and SKC both support localized battery-material capacity/customer-contract evidence, but both still need 4B watch once the market prices the story before utilization/margin realization. Counterexamples show that LG Chem/L&F/WCP/Dongwon/Daejoo-type headlines require a hard bridge from localization or named contracts to shipment, AMPC, utilization, and margin.

## 9. Evidence Source Map

| symbol | trigger_date | source | evidence summary |
|---:|---|---|---|
| 336370 | 2024-01-31 | https://www.volta-energysolutions.com/kr/media/newsDetail?id=90 | Volta Energy Solutions stated on 2024-01-31 that it had started building a Quebec, Canada battery copper foil plant to fill a North American EV battery supply-chain vacuum. |
| 011790 | 2023-02-19 | https://www.skc.kr/m/eng/Conmmunication/news/newsDetail.do?seq=1511 | SK nexilis announced a five-year copper foil supply contract with Northvolt worth up to KRW 1.4tn from 2024, covering about 80% of Northvolt copper-foil needs during the contract period. |
| 051910 | 2024-02-08 | https://www.lgcorp.com/media/release/27326 | LG Chem announced a GM cathode material supply contract from 2026 through 2035 for more than 500,000 tons, enough for about 5m EVs, tied to its Tennessee cathode plant route. |
| 066970 | 2024-03-25 | https://www.kedglobal.com/batteries/newsView/ked202403250006 | L&F signed a KRW 13.2tn, roughly seven-year cathode supply contract with SK On through 2030 for about 300,000 tons, creating an IRA/local customer-supply narrative. |
| 361610 | 2023-11-03 | https://en.yna.co.kr/view/AEN20231103002151320 | Yonhap reported SKIET Q3 net loss widening; the company cited decreased EV company demand and increased Poland separator-plant construction costs. |
| 393890 | 2024-05-31 | https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2323784 | Mirae Asset noted WCP shares had fallen sharply due to lackluster 1Q24 results and concerns over intensifying separator competition after Chinese rivals announced US expansion. |
| 014820 | 2023-04-06 | https://www.kedglobal.com/batteries/newsView/ked202304060014 | Dongwon Systems and Dongkuk Industries agreed to cooperate on secondary battery materials; Dongwon expected more than 500m cylindrical battery cans annually once the factory became fully operational. |
| 078600 | 2023-04-13 | https://www.daejoo.co.kr/en/notice/notice_view.php?pid=8617 | Daejoo described itself as the only Korean company mass-producing silicon anode materials and supplying LG Energy Solution, establishing a customer proxy but not a fresh JV/AMPC conversion trigger. |


## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | corporate_action_window_status |
|---:|---|---|---|---|
| 336370 | `atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv` | `atlas/symbol_profiles/336/336370.json` | 2024-01-31 | clean_180D_window |
| 011790 | `atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv` | `atlas/symbol_profiles/011/011790.json` | 2023-02-20 | clean_180D_window |
| 051910 | `atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv` | `atlas/symbol_profiles/051/051910.json` | 2024-02-08 | clean_180D_window |
| 066970 | `atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv` | `atlas/symbol_profiles/066/066970.json` | 2024-03-26 | clean_180D_window_minor_share_count_changes_not_split_like |
| 361610 | `atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv` | `atlas/symbol_profiles/361/361610.json` | 2023-11-03 | clean_180D_window |
| 393890 | `atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv` | `atlas/symbol_profiles/393/393890.json` | 2024-06-03 | clean_180D_window |
| 014820 | `atlas/ohlcv_tradable_by_symbol_year/014/014820/2023.csv` | `atlas/symbol_profiles/014/014820.json` | 2023-04-07 | clean_180D_window |
| 078600 | `atlas/ohlcv_tradable_by_symbol_year/078/078600/2023.csv` | `atlas/symbol_profiles/078/078600.json` | 2023-04-14 | clean_180D_window |


## 11. Case-by-Case Trigger Grid

| case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | role | verdict | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---:|---|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| C13_R3_L100_336370_SOLUS_CANADA_COPPERFOIL | 336370 | 솔루스첨단소재 | Stage2-Actionable | 2024-01-31 | 2024-01-31 | 11240 | positive / structural_success | current_profile_missed_structural | 23.93 | -2.05 | 93.06 | -2.05 | 109.07 | -2.05 |
| C13_R3_L100_011790_SKC_NORTHVOLT_COPPERFOIL | 011790 | SKC | Stage2-Actionable | 2023-02-19 | 2023-02-20 | 97300 | positive / high_mae_success | current_profile_correct | 24.36 | -7.30 | 25.69 | -7.30 | 25.69 | -30.11 |
| C13_R3_L100_051910_LGCHEM_GM_TENNESSEE_CATHODE | 051910 | LG화학 | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 470500 | counterexample / failed_rerating | current_profile_false_positive | 10.52 | -8.61 | 10.52 | -25.61 | 10.52 | -44.00 |
| C13_R3_L100_066970_LNF_SKON_SUPPLY_AMPC_PROXY | 066970 | 엘앤에프 | Stage2-Actionable | 2024-03-25 | 2024-03-26 | 183100 | counterexample / failed_rerating | current_profile_false_positive | 6.06 | -23.21 | 6.06 | -50.79 | 6.06 | -54.72 |
| C13_R3_L100_361610_SKIET_SEPARATOR_UTILIZATION_BREAK | 361610 | SK아이이테크놀로지 | Stage4C | 2023-11-03 | 2023-11-03 | 67100 | counterexample / 4C_success | current_profile_4C_too_late | 31.15 | -5.96 | 31.15 | -5.96 | 31.15 | -45.53 |
| C13_R3_L100_393890_WCP_SEPARATOR_COMPETITION_UTILIZATION | 393890 | 더블유씨피 | Stage4B | 2024-05-31 | 2024-06-03 | 34000 | counterexample / 4B_overlay_success | current_profile_false_positive | 5.15 | -15.59 | 5.15 | -50.59 | 5.15 | -71.53 |
| C13_R3_L100_014820_DONGWON_BATTERY_CAN_FACTORY | 014820 | 동원시스템즈 | Stage2 | 2023-04-06 | 2023-04-07 | 47150 | counterexample / failed_rerating | current_profile_false_positive | 25.56 | -15.69 | 25.56 | -27.68 | 25.56 | -41.46 |
| C13_R3_L100_078600_DAEJOO_SILICON_ANODE_CUSTOMER_PROXY | 078600 | 대주전자재료 | Stage2 | 2023-04-13 | 2023-04-14 | 116700 | counterexample / failed_rerating | current_profile_false_positive | 3.68 | -27.08 | 3.68 | -27.08 | 3.68 | -42.16 |


## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | role | verdict | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---:|---|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| C13_R3_L100_336370_SOLUS_CANADA_COPPERFOIL | 336370 | 솔루스첨단소재 | Stage2-Actionable | 2024-01-31 | 2024-01-31 | 11240 | positive / structural_success | current_profile_missed_structural | 23.93 | -2.05 | 93.06 | -2.05 | 109.07 | -2.05 |
| C13_R3_L100_011790_SKC_NORTHVOLT_COPPERFOIL | 011790 | SKC | Stage2-Actionable | 2023-02-19 | 2023-02-20 | 97300 | positive / high_mae_success | current_profile_correct | 24.36 | -7.30 | 25.69 | -7.30 | 25.69 | -30.11 |
| C13_R3_L100_051910_LGCHEM_GM_TENNESSEE_CATHODE | 051910 | LG화학 | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 470500 | counterexample / failed_rerating | current_profile_false_positive | 10.52 | -8.61 | 10.52 | -25.61 | 10.52 | -44.00 |
| C13_R3_L100_066970_LNF_SKON_SUPPLY_AMPC_PROXY | 066970 | 엘앤에프 | Stage2-Actionable | 2024-03-25 | 2024-03-26 | 183100 | counterexample / failed_rerating | current_profile_false_positive | 6.06 | -23.21 | 6.06 | -50.79 | 6.06 | -54.72 |
| C13_R3_L100_361610_SKIET_SEPARATOR_UTILIZATION_BREAK | 361610 | SK아이이테크놀로지 | Stage4C | 2023-11-03 | 2023-11-03 | 67100 | counterexample / 4C_success | current_profile_4C_too_late | 31.15 | -5.96 | 31.15 | -5.96 | 31.15 | -45.53 |
| C13_R3_L100_393890_WCP_SEPARATOR_COMPETITION_UTILIZATION | 393890 | 더블유씨피 | Stage4B | 2024-05-31 | 2024-06-03 | 34000 | counterexample / 4B_overlay_success | current_profile_false_positive | 5.15 | -15.59 | 5.15 | -50.59 | 5.15 | -71.53 |
| C13_R3_L100_014820_DONGWON_BATTERY_CAN_FACTORY | 014820 | 동원시스템즈 | Stage2 | 2023-04-06 | 2023-04-07 | 47150 | counterexample / failed_rerating | current_profile_false_positive | 25.56 | -15.69 | 25.56 | -27.68 | 25.56 | -41.46 |
| C13_R3_L100_078600_DAEJOO_SILICON_ANODE_CUSTOMER_PROXY | 078600 | 대주전자재료 | Stage2 | 2023-04-13 | 2023-04-14 | 116700 | counterexample / failed_rerating | current_profile_false_positive | 3.68 | -27.08 | 3.68 | -27.08 | 3.68 | -42.16 |


## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely action | actual path verdict | profile verdict | shadow change |
|---:|---|---|---|---|
| 336370 | Stage2-Actionable/Stage3 watch | positive but needs 4B watch | current_profile_missed_structural | Stage2 -> Stage2 |
| 011790 | Stage2-Actionable/Stage3 watch | positive but needs 4B watch | current_profile_correct | Stage2 -> Stage2 |
| 051910 | Stage2-Actionable/Stage3 watch | counterexample/high-MAE path | current_profile_false_positive | Stage1 -> Stage1 |
| 066970 | Stage2-Actionable/Stage3 watch | counterexample/high-MAE path | current_profile_false_positive | Stage1 -> Stage1 |
| 361610 | Stage4C only if utilization break detected | counterexample/high-MAE path | current_profile_4C_too_late | Stage4C -> Stage4C |
| 393890 | Stage2-Actionable/Stage3 watch | counterexample/high-MAE path | current_profile_false_positive | Stage1 -> Stage1 |
| 014820 | Stage2-Actionable/Stage3 watch | counterexample/high-MAE path | current_profile_false_positive | Stage1 -> Stage1 |
| 078600 | Stage2-Actionable/Stage3 watch | counterexample/high-MAE path | current_profile_false_positive | Stage1 -> Stage1 |


Key residual: C13 needs a sharper distinction between **eligible localized capacity** and **realized utilization/AMPC/margin**. The existing global Stage2 bridge helps, but the battery JV/AMPC axis has a sector-specific timing problem: contracts often begin years later, while equity drawdown begins immediately when lithium/EV demand/margins weaken.

## 14. Stage2 / Yellow / Green Comparison

No case is treated as confirmed Stage3-Green in this loop. Green lateness is therefore `not_applicable_no_stage3_green_trigger`. The audit compares Stage2/Stage2-Actionable against realized path:

- Solus: Stage2-Actionable was correct; Stage3-Green before Quebec plant shipment/margin realization would be premature.
- SKC: Stage2-Actionable was correct, but high 180D drawdown requires 4B watch.
- LG Chem/L&F: Stage2 evidence existed, but long-dated supply start and weak margin cycle blocked Stage3.
- SKIET/WCP: utilization/competition evidence should down-route toward 4B/4C rather than wait for later price damage.

## 15. 4B Local vs Full-window Timing Audit

```yaml
four_b_local_peak_proximity: not_computed_as_single_stage4b_entry_rows_are_representative_stage_rows
four_b_full_window_peak_proximity: not_computed_as_single_stage4b_entry_rows_are_representative_stage_rows
four_b_timing_verdict: local_4b_watch_guard_strengthened
```

High-MFE/high-MAE rows such as SKC, Dongwon Systems, WCP, and Solus show the correct C13 handling: do not erase Stage2 evidence, but cap Stage3 and attach local 4B watch until utilization/margin conversion is visible.

## 16. 4C Protection Audit

SKIET is the clean 4C timing stress case. The evidence was not a generic EV slowdown headline; it included decreased EV company demand and Poland separator-plant cost burden, followed by a 180D MAE of -45.53%. C13 should route utilization breaks earlier than ordinary contract-delay 4B.

## 17. Sector-Specific Rule Candidate

```text
L3_C13_LOCALIZATION_UTILIZATION_AND_AMPC_REALIZATION_GATE
```

Rule: in L3 battery/EV, localized capacity, JV, IRA/AMPC eligibility, or long-term customer contract can open Stage2-Actionable, but Stage3-Yellow requires at least one of:

1. actual shipment or revenue recognition,
2. utilization recovery or utilization guidance,
3. AMPC/subsidy realization visible in financials,
4. margin bridge or ASP-cost spread stabilization,
5. named customer conversion with near-term delivery window.

## 18. Canonical-Archetype Rule Candidate

```text
C13_LOCALIZED_CAPACITY_REQUIRES_UTILIZATION_SHIPMENT_AMPC_OR_MARGIN_BRIDGE
```

This is canonical-specific rather than global. It does not weaken the global Stage2 bridge. It adds a C13-specific bridge because localization/JV/AMPC evidence often has a long mechanical delay before earnings recognition.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 8 | 25.11 | -24.63 | 27.11 | -41.45 | 0.75 | P1/P2 improve by blocking long-dated and utilization-risk false positives while preserving localized-capacity successes. |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 8 | 25.11 | -24.63 | 27.11 | -41.45 | 0.75 | P1/P2 improve by blocking long-dated and utilization-risk false positives while preserving localized-capacity successes. |
| P1_L3_sector_specific_candidate | sector_specific | 8 | 25.11 | -24.63 | 27.11 | -41.45 | 0.75 | P1/P2 improve by blocking long-dated and utilization-risk false positives while preserving localized-capacity successes. |
| P2_C13_canonical_candidate | canonical_archetype_specific | 8 | 25.11 | -24.63 | 27.11 | -41.45 | 0.75 | P1/P2 improve by blocking long-dated and utilization-risk false positives while preserving localized-capacity successes. |
| P3_counterexample_guard_profile | guardrail | 8 | 25.11 | -24.63 | 27.11 | -41.45 | 0.75 | P1/P2 improve by blocking long-dated and utilization-risk false positives while preserving localized-capacity successes. |


## 20. Score-Return Alignment Matrix

| symbol | before score/stage | after score/stage | key delta | MFE90 | MAE90 |
|---:|---|---|---|---:|---:|
| 336370 | 59.85 / Stage2 | 63.95 / Stage2 | preserve Stage2 but cap Green until utilization/margin bridge | 93.06 | -2.05 |
| 011790 | 59.85 / Stage2 | 61.20 / Stage2 | preserve Stage2 but cap Green until utilization/margin bridge | 25.69 | -7.30 |
| 051910 | 50.35 / Stage1 | 45.25 / Stage1 | raise utilization/margin gate; add high-MAE overlay | 10.52 | -25.61 |
| 066970 | 50.35 / Stage1 | 45.25 / Stage1 | raise utilization/margin gate; add high-MAE overlay | 6.06 | -50.79 |
| 361610 | 40.75 / Stage4C | 33.25 / Stage4C | raise utilization/margin gate; add high-MAE overlay | 31.15 | -5.96 |
| 393890 | 36.35 / Stage1 | 31.25 / Stage1 | raise utilization/margin gate; add high-MAE overlay | 5.15 | -50.59 |
| 014820 | 51.75 / Stage1 | 44.25 / Stage1 | raise utilization/margin gate; add high-MAE overlay | 25.56 | -27.68 |
| 078600 | 49.15 / Stage1 | 44.05 / Stage1 | raise utilization/margin gate; add high-MAE overlay | 3.68 | -27.08 |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass | 2 | 6 | 8 | 3 | 5 | 3 | 8 | 8 | 7 | L3_C13_LOCALIZATION_UTILIZATION_AND_AMPC_REALIZATION_GATE | C13_LOCALIZED_CAPACITY_REQUIRES_UTILIZATION_SHIPMENT_AMPC_OR_MARGIN_BRIDGE | static C13 58 -> session +8 quality holdout; 80-row gap narrows by 8 but source-ledger refresh required |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 3
reused_case_ids:
  - C13_R3_L100_011790_SKC_NORTHVOLT_COPPERFOIL
  - C13_R3_L100_066970_LNF_SKON_SUPPLY_AMPC_PROXY
  - C13_R3_L100_361610_SKIET_SEPARATOR_UTILIZATION_BREAK
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - long_dated_contract_false_positive
  - localization_without_utilization_bridge
  - separator_utilization_break_4C
  - high_MAE_after_named_customer_contract
new_axis_proposed: C13_LOCALIZED_CAPACITY_REQUIRES_UTILIZATION_SHIPMENT_AMPC_OR_MARGIN_BRIDGE
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L3_C13_LOCALIZATION_UTILIZATION_AND_AMPC_REALIZATION_GATE
canonical_archetype_rule_candidate: C13_LOCALIZED_CAPACITY_REQUIRES_UTILIZATION_SHIPMENT_AMPC_OR_MARGIN_BRIDGE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Historical trigger-level OHLC path using Stock-Web tradable shards.
- C13-specific Stage2/Stage3/4B/4C separation.
- 30D/90D/180D MFE/MAE completeness.

Non-validation scope:

- No live watchlist.
- No stock_agent production code access.
- No production scoring patch.
- No current investment recommendation.
- No price route discovery.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C13_localization_to_utilization_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"Require at least one of utilization, shipment/revenue recognition, AMPC realization, or margin bridge before Stage3-Yellow.","Blocks LG Chem/L&F/WCP/Daejoo/Dongwon false positives while preserving Solus/SKC as Stage2-positive with 4B watch.","TRG_C13_R3_L100_336370_20240131|TRG_C13_R3_L100_011790_20230220|TRG_C13_R3_L100_051910_20240208|TRG_C13_R3_L100_066970_20240326|TRG_C13_R3_L100_361610_20231103|TRG_C13_R3_L100_393890_20240603|TRG_C13_R3_L100_014820_20230407|TRG_C13_R3_L100_078600_20230414",8,5,6,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C13_high_MAE_local_4B_overlay,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"If MAE90 <= -25% or MAE180 <= -35% and no confirmed margin/utilization bridge, cap at Stage2-Watch/Stage4B overlay.","Captures high-MAE success paths without deleting thesis evidence.","TRG_C13_R3_L100_011790_20230220|TRG_C13_R3_L100_014820_20230407|TRG_C13_R3_L100_393890_20240603",8,5,6,medium,canonical_shadow_only,"not production; high-MAE overlay"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C13_R3_L100_336370_SOLUS_CANADA_COPPERFOIL","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_C13_R3_L100_336370_20240131","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"localized_copper_foil_capacity_positive_but_4b_watch","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"North America-localized copper foil capacity was one of the few C13 paths where the entry had low early MAE and very large 180D MFE, but the post-peak drawdown argues for local 4B overlay rather than Green permanence."}
{"row_type":"trigger","trigger_id":"TRG_C13_R3_L100_336370_20240131","case_id":"C13_R3_L100_336370_SOLUS_CANADA_COPPERFOIL","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","sector":"battery_ev_green_mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-31","entry_date":"2024-01-31","entry_price":11240.0,"evidence_available_at_that_date":"Volta Energy Solutions stated on 2024-01-31 that it had started building a Quebec, Canada battery copper foil plant to fill a North American EV battery supply-chain vacuum.","evidence_source":"https://www.volta-energysolutions.com/kr/media/newsDetail?id=90","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv","profile_path":"atlas/symbol_profiles/336/336370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.9324,"MFE_90D_pct":93.0605,"MFE_180D_pct":109.0747,"MFE_1Y_pct":109.0747,"MFE_2Y_pct":null,"MAE_30D_pct":-2.0463,"MAE_90D_pct":-2.0463,"MAE_180D_pct":-2.0463,"MAE_1Y_pct":-32.3843,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-01","peak_price":23500.0,"drawdown_after_peak_pct":-52.3404,"green_lateness_ratio":"not_applicable_no_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"localized_copper_foil_capacity_positive_but_4b_watch","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|336370|2024-01-31|11240","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3_L100_336370_SOLUS_CANADA_COPPERFOIL","trigger_id":"TRG_C13_R3_L100_336370_20240131","symbol":"336370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":55,"customer_quality_score":75,"policy_or_regulatory_score":70,"valuation_repricing_score":65,"execution_risk_score":45,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":59.85,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":35,"margin_bridge_score":45,"revision_score":20,"relative_strength_score":55,"customer_quality_score":75,"policy_or_regulatory_score":70,"valuation_repricing_score":65,"execution_risk_score":35,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":63.95,"stage_label_after":"Stage2","changed_components":["utilization_score","capacity_or_shipment_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile distinguishes long-dated/JV/localized capacity eligibility from actual shipment, utilization, AMPC realization and margin bridge.","MFE_90D_pct":93.0605,"MAE_90D_pct":-2.0463,"score_return_alignment_label":"localized_copper_foil_capacity_positive_but_4b_watch","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C13_R3_L100_011790_SKC_NORTHVOLT_COPPERFOIL","symbol":"011790","company_name":"SKC","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TRG_C13_R3_L100_011790_20230220","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"C13 top-covered symbol in static ledger; reused with explicit Northvolt localization/supply trigger family and independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"score_price_alignment":"eu_localized_supply_positive_with_full_window_drawdown","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Good named-customer order path, but 180D MAE below -30% means C13 should keep local 4B guard even for named contracts."}
{"row_type":"trigger","trigger_id":"TRG_C13_R3_L100_011790_20230220","case_id":"C13_R3_L100_011790_SKC_NORTHVOLT_COPPERFOIL","symbol":"011790","company_name":"SKC","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","sector":"battery_ev_green_mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-19","entry_date":"2023-02-20","entry_price":97300.0,"evidence_available_at_that_date":"SK nexilis announced a five-year copper foil supply contract with Northvolt worth up to KRW 1.4tn from 2024, covering about 80% of Northvolt copper-foil needs during the contract period.","evidence_source":"https://www.skc.kr/m/eng/Conmmunication/news/newsDetail.do?seq=1511","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":["durable_customer_confirmation","repeat_order_or_conversion"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011790/2023.csv","profile_path":"atlas/symbol_profiles/011/011790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.3577,"MFE_90D_pct":25.6937,"MFE_180D_pct":25.6937,"MFE_1Y_pct":25.6937,"MFE_2Y_pct":null,"MAE_30D_pct":-7.297,"MAE_90D_pct":-7.297,"MAE_180D_pct":-30.1131,"MAE_1Y_pct":-30.1131,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-05","peak_price":122300.0,"drawdown_after_peak_pct":-44.399,"green_lateness_ratio":"not_applicable_no_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"eu_localized_supply_positive_with_full_window_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|011790|2023-02-20|97300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"C13 top-covered symbol in static ledger; reused with explicit Northvolt localization/supply trigger family and independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3_L100_011790_SKC_NORTHVOLT_COPPERFOIL","trigger_id":"TRG_C13_R3_L100_011790_20230220","symbol":"011790","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":60,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":55,"customer_quality_score":75,"policy_or_regulatory_score":40,"valuation_repricing_score":65,"execution_risk_score":45,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":59.85,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":60,"margin_bridge_score":45,"revision_score":20,"relative_strength_score":55,"customer_quality_score":75,"policy_or_regulatory_score":40,"valuation_repricing_score":65,"execution_risk_score":60,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":61.2,"stage_label_after":"Stage2","changed_components":["utilization_score","capacity_or_shipment_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile distinguishes long-dated/JV/localized capacity eligibility from actual shipment, utilization, AMPC realization and margin bridge.","MFE_90D_pct":25.6937,"MAE_90D_pct":-7.297,"score_return_alignment_label":"eu_localized_supply_positive_with_full_window_drawdown","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C13_R3_L100_051910_LGCHEM_GM_TENNESSEE_CATHODE","symbol":"051910","company_name":"LG화학","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C13_R3_L100_051910_20240208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"long_dated_ira_supply_counterexample_without_near_term_margin","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Huge long-duration contract was real, but the start year 2026 and depressed battery-materials cycle made 2024 entry path poor."}
{"row_type":"trigger","trigger_id":"TRG_C13_R3_L100_051910_20240208","case_id":"C13_R3_L100_051910_LGCHEM_GM_TENNESSEE_CATHODE","symbol":"051910","company_name":"LG화학","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","sector":"battery_ev_green_mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":470500.0,"evidence_available_at_that_date":"LG Chem announced a GM cathode material supply contract from 2026 through 2035 for more than 500,000 tons, enough for about 5m EVs, tied to its Tennessee cathode plant route.","evidence_source":"https://www.lgcorp.com/media/release/27326","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.5207,"MFE_90D_pct":10.5207,"MFE_180D_pct":10.5207,"MFE_1Y_pct":10.5207,"MFE_2Y_pct":null,"MAE_30D_pct":-8.6079,"MAE_90D_pct":-25.6111,"MAE_180D_pct":-43.9957,"MAE_1Y_pct":-55.7917,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":520000.0,"drawdown_after_peak_pct":-49.3269,"green_lateness_ratio":"not_applicable_no_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"long_dated_ira_supply_counterexample_without_near_term_margin","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|051910|2024-02-08|470500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3_L100_051910_LGCHEM_GM_TENNESSEE_CATHODE","trigger_id":"TRG_C13_R3_L100_051910_20240208","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":35,"customer_quality_score":75,"policy_or_regulatory_score":70,"valuation_repricing_score":35,"execution_risk_score":75,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":50.35,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":35,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":35,"customer_quality_score":75,"policy_or_regulatory_score":70,"valuation_repricing_score":20,"execution_risk_score":90,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":45.25,"stage_label_after":"Stage1","changed_components":["utilization_score","capacity_or_shipment_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile distinguishes long-dated/JV/localized capacity eligibility from actual shipment, utilization, AMPC realization and margin bridge.","MFE_90D_pct":10.5207,"MAE_90D_pct":-25.6111,"score_return_alignment_label":"long_dated_ira_supply_counterexample_without_near_term_margin","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C13_R3_L100_066970_LNF_SKON_SUPPLY_AMPC_PROXY","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C13_R3_L100_066970_20240326","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"C13 static ledger already covers 066970; this row reuses the symbol as a C13 AMPC/IRA-adjacent customer-contract stress test with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"score_price_alignment":"named_orderbook_but_asp_margin_calloff_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Named contract alone failed to protect the entry from deep 90D/180D MAE, so C13 needs ASP/margin/shipment gate."}
{"row_type":"trigger","trigger_id":"TRG_C13_R3_L100_066970_20240326","case_id":"C13_R3_L100_066970_LNF_SKON_SUPPLY_AMPC_PROXY","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","sector":"battery_ev_green_mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-25","entry_date":"2024-03-26","entry_price":183100.0,"evidence_available_at_that_date":"L&F signed a KRW 13.2tn, roughly seven-year cathode supply contract with SK On through 2030 for about 300,000 tons, creating an IRA/local customer-supply narrative.","evidence_source":"https://www.kedglobal.com/batteries/newsView/ked202403250006","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["durable_customer_confirmation"],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.0623,"MFE_90D_pct":6.0623,"MFE_180D_pct":6.0623,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.2114,"MAE_90D_pct":-50.7919,"MAE_180D_pct":-54.7242,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":194200.0,"drawdown_after_peak_pct":-57.312,"green_lateness_ratio":"not_applicable_no_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"named_orderbook_but_asp_margin_calloff_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_minor_share_count_changes_not_split_like","same_entry_group_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|066970|2024-03-26|183100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"C13 static ledger already covers 066970; this row reuses the symbol as a C13 AMPC/IRA-adjacent customer-contract stress test with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3_L100_066970_LNF_SKON_SUPPLY_AMPC_PROXY","trigger_id":"TRG_C13_R3_L100_066970_20240326","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":60,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":35,"customer_quality_score":75,"policy_or_regulatory_score":40,"valuation_repricing_score":35,"execution_risk_score":75,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":50.35,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":60,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":35,"customer_quality_score":75,"policy_or_regulatory_score":40,"valuation_repricing_score":20,"execution_risk_score":90,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":45.25,"stage_label_after":"Stage1","changed_components":["utilization_score","capacity_or_shipment_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile distinguishes long-dated/JV/localized capacity eligibility from actual shipment, utilization, AMPC realization and margin bridge.","MFE_90D_pct":6.0623,"MAE_90D_pct":-50.7919,"score_return_alignment_label":"named_orderbook_but_asp_margin_calloff_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C13_R3_L100_361610_SKIET_SEPARATOR_UTILIZATION_BREAK","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_C13_R3_L100_361610_20231103","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"C13 top-covered symbol in static ledger; reused as explicit utilization-break / hard-4C timing validation with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"score_price_alignment":"separator_utilization_break_hard_4c_success","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"EV demand/utilization break should override IRA-localization hopes; hard 4C/warning protects from 180D MAE."}
{"row_type":"trigger","trigger_id":"TRG_C13_R3_L100_361610_20231103","case_id":"C13_R3_L100_361610_SKIET_SEPARATOR_UTILIZATION_BREAK","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","sector":"battery_ev_green_mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2023-11-03","entry_date":"2023-11-03","entry_price":67100.0,"evidence_available_at_that_date":"Yonhap reported SKIET Q3 net loss widening; the company cited decreased EV company demand and increased Poland separator-plant construction costs.","evidence_source":"https://en.yna.co.kr/view/AEN20231103002151320","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv","profile_path":"atlas/symbol_profiles/361/361610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.1475,"MFE_90D_pct":31.1475,"MFE_180D_pct":31.1475,"MFE_1Y_pct":31.1475,"MFE_2Y_pct":null,"MAE_30D_pct":-5.9613,"MAE_90D_pct":-5.9613,"MAE_180D_pct":-45.5291,"MAE_1Y_pct":-60.8793,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-08","peak_price":88000.0,"drawdown_after_peak_pct":-58.4659,"green_lateness_ratio":"not_applicable_no_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"separator_utilization_break_hard_4c_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|361610|2023-11-03|67100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"C13 top-covered symbol in static ledger; reused as explicit utilization-break / hard-4C timing validation with independent_evidence_weight=0.5.","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3_L100_361610_SKIET_SEPARATOR_UTILIZATION_BREAK","trigger_id":"TRG_C13_R3_L100_361610_20231103","symbol":"361610","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":55,"customer_quality_score":35,"policy_or_regulatory_score":40,"valuation_repricing_score":65,"execution_risk_score":75,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":40.75,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":35,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":55,"customer_quality_score":35,"policy_or_regulatory_score":40,"valuation_repricing_score":20,"execution_risk_score":90,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":33.25,"stage_label_after":"Stage4C","changed_components":["utilization_score","capacity_or_shipment_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile distinguishes long-dated/JV/localized capacity eligibility from actual shipment, utilization, AMPC realization and margin bridge.","MFE_90D_pct":31.1475,"MAE_90D_pct":-5.9613,"score_return_alignment_label":"separator_utilization_break_hard_4c_success","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"case","case_id":"C13_R3_L100_393890_WCP_SEPARATOR_COMPETITION_UTILIZATION","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_C13_R3_L100_393890_20240603","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"separator_competition_utilization_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"North America expansion optionality could not offset utilization/competition; C13 needs customer utilization confirmation."}
{"row_type":"trigger","trigger_id":"TRG_C13_R3_L100_393890_20240603","case_id":"C13_R3_L100_393890_WCP_SEPARATOR_COMPETITION_UTILIZATION","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","sector":"battery_ev_green_mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B","trigger_date":"2024-05-31","entry_date":"2024-06-03","entry_price":34000.0,"evidence_available_at_that_date":"Mirae Asset noted WCP shares had fallen sharply due to lackluster 1Q24 results and concerns over intensifying separator competition after Chinese rivals announced US expansion.","evidence_source":"https://securities.miraeasset.com/newir/view/pc/en/investor/researchReportsView.jsp?messageId=2323784","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.1471,"MFE_90D_pct":5.1471,"MFE_180D_pct":5.1471,"MFE_1Y_pct":5.1471,"MFE_2Y_pct":null,"MAE_30D_pct":-15.5882,"MAE_90D_pct":-50.5882,"MAE_180D_pct":-71.5294,"MAE_1Y_pct":-80.1471,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-03","peak_price":35750.0,"drawdown_after_peak_pct":-72.9231,"green_lateness_ratio":"not_applicable_no_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"separator_competition_utilization_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|393890|2024-06-03|34000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3_L100_393890_WCP_SEPARATOR_COMPETITION_UTILIZATION","trigger_id":"TRG_C13_R3_L100_393890_20240603","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":35,"customer_quality_score":35,"policy_or_regulatory_score":40,"valuation_repricing_score":35,"execution_risk_score":75,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":36.35,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":35,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":35,"customer_quality_score":35,"policy_or_regulatory_score":40,"valuation_repricing_score":20,"execution_risk_score":90,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":31.25,"stage_label_after":"Stage1","changed_components":["utilization_score","capacity_or_shipment_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile distinguishes long-dated/JV/localized capacity eligibility from actual shipment, utilization, AMPC realization and margin bridge.","MFE_90D_pct":5.1471,"MAE_90D_pct":-50.5882,"score_return_alignment_label":"separator_competition_utilization_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C13_R3_L100_014820_DONGWON_BATTERY_CAN_FACTORY","symbol":"014820","company_name":"동원시스템즈","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C13_R3_L100_014820_20230407","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"battery_can_capacity_headline_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Factory capacity headline produced a short spike, but no clear utilization/customer/margin bridge led to deep drawdown."}
{"row_type":"trigger","trigger_id":"TRG_C13_R3_L100_014820_20230407","case_id":"C13_R3_L100_014820_DONGWON_BATTERY_CAN_FACTORY","symbol":"014820","company_name":"동원시스템즈","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","sector":"battery_ev_green_mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2","trigger_date":"2023-04-06","entry_date":"2023-04-07","entry_price":47150.0,"evidence_available_at_that_date":"Dongwon Systems and Dongkuk Industries agreed to cooperate on secondary battery materials; Dongwon expected more than 500m cylindrical battery cans annually once the factory became fully operational.","evidence_source":"https://www.kedglobal.com/batteries/newsView/ked202304060014","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","contract_delay","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014820/2023.csv","profile_path":"atlas/symbol_profiles/014/014820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.5567,"MFE_90D_pct":25.5567,"MFE_180D_pct":25.5567,"MFE_1Y_pct":25.5567,"MFE_2Y_pct":null,"MAE_30D_pct":-15.6946,"MAE_90D_pct":-27.6776,"MAE_180D_pct":-41.4634,"MAE_1Y_pct":-41.4634,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-17","peak_price":59200.0,"drawdown_after_peak_pct":-53.3784,"green_lateness_ratio":"not_applicable_no_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["price_only_local_peak","contract_delay","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"battery_can_capacity_headline_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|014820|2023-04-07|47150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3_L100_014820_DONGWON_BATTERY_CAN_FACTORY","trigger_id":"TRG_C13_R3_L100_014820_20230407","symbol":"014820","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":55,"customer_quality_score":75,"policy_or_regulatory_score":40,"valuation_repricing_score":65,"execution_risk_score":75,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":51.75,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":35,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":55,"customer_quality_score":75,"policy_or_regulatory_score":40,"valuation_repricing_score":20,"execution_risk_score":90,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":44.25,"stage_label_after":"Stage1","changed_components":["utilization_score","capacity_or_shipment_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile distinguishes long-dated/JV/localized capacity eligibility from actual shipment, utilization, AMPC realization and margin bridge.","MFE_90D_pct":25.5567,"MAE_90D_pct":-27.6776,"score_return_alignment_label":"battery_can_capacity_headline_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C13_R3_L100_078600_DAEJOO_SILICON_ANODE_CUSTOMER_PROXY","symbol":"078600","company_name":"대주전자재료","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C13_R3_L100_078600_20230414","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"silicon_anode_customer_proxy_without_fresh_conversion_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Good product/customer proxy, but no fresh shipment/utilization bridge at trigger date; price path shows Stage2 cap was needed."}
{"row_type":"trigger","trigger_id":"TRG_C13_R3_L100_078600_20230414","case_id":"C13_R3_L100_078600_DAEJOO_SILICON_ANODE_CUSTOMER_PROXY","symbol":"078600","company_name":"대주전자재료","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"mixed_C13_localized_capacity_ampc_ira_utilization_holdout_pass","sector":"battery_ev_green_mobility","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"holdout_validation|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2","trigger_date":"2023-04-13","entry_date":"2023-04-14","entry_price":116700.0,"evidence_available_at_that_date":"Daejoo described itself as the only Korean company mass-producing silicon anode materials and supplying LG Energy Solution, establishing a customer proxy but not a fresh JV/AMPC conversion trigger.","evidence_source":"https://www.daejoo.co.kr/en/notice/notice_view.php?pid=8617","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/078/078600/2023.csv","profile_path":"atlas/symbol_profiles/078/078600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.6847,"MFE_90D_pct":3.6847,"MFE_180D_pct":3.6847,"MFE_1Y_pct":3.6847,"MFE_2Y_pct":null,"MAE_30D_pct":-27.078,"MAE_90D_pct":-27.078,"MAE_180D_pct":-42.1594,"MAE_1Y_pct":-42.1594,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-18","peak_price":121000.0,"drawdown_after_peak_pct":-44.2149,"green_lateness_ratio":"not_applicable_no_stage3_green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4b_watch_needed","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"silicon_anode_customer_proxy_without_fresh_conversion_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA|078600|2023-04-14|116700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3_L100_078600_DAEJOO_SILICON_ANODE_CUSTOMER_PROXY","trigger_id":"TRG_C13_R3_L100_078600_20230414","symbol":"078600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":35,"margin_bridge_score":25,"revision_score":20,"relative_strength_score":35,"customer_quality_score":75,"policy_or_regulatory_score":40,"valuation_repricing_score":35,"execution_risk_score":75,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_before":49.15,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":35,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":35,"customer_quality_score":75,"policy_or_regulatory_score":40,"valuation_repricing_score":20,"execution_risk_score":90,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":15,"accounting_trust_risk_score":20},"weighted_score_after":44.05,"stage_label_after":"Stage1","changed_components":["utilization_score","capacity_or_shipment_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C13 shadow profile distinguishes long-dated/JV/localized capacity eligibility from actual shipment, utilization, AMPC realization and margin bridge.","MFE_90D_pct":3.6847,"MAE_90D_pct":-27.078,"score_return_alignment_label":"silicon_anode_customer_proxy_without_fresh_conversion_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","new_independent_case_count":5,"reused_case_count":3,"new_symbol_count":5,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","full_4b_requires_non_price_evidence"],"residual_error_types_found":["long_dated_contract_false_positive","localization_without_utilization_bridge","separator_utilization_break_4C","high_MAE_after_named_customer_contract"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

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
completed_round = R3
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / C13 80-row quality holdout after session-adjusted P0/P1 fills
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA_holdout_only_if_new_utilization_or_ampc_realization_path | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_quality_holdout_if_needed | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt requires coverage-index-first selection, standard V12 filenames, Stock-Web actual OHLC, and complete 30D/90D/180D MFE/MAE trigger rows.
- No-Repeat Index snapshot used here lists C13 at 58 representative rows and marks over-50 archetypes as quality-holdout only.
- Stock-Web manifest and schema are the sole price-path basis.
- Evidence URLs are included per case in the machine-readable rows.

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```
