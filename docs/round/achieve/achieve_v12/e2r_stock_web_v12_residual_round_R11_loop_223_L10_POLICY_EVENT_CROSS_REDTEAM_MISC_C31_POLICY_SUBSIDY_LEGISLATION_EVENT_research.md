# E2R v12 Residual Research — R11 / L10 / C31 Policy Subsidy Legislation Event

```yaml
research_session: post_calibrated_sector_archetype_residual_research_v12
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R11_loop_223_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
selected_round: R11
selected_loop: 223
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: C31_POLICY_TARIFF_SUBSIDY_TO_CASHFLOW_EXECUTION_GATE_V1
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality reinforcement / direct cashflow execution repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection / No-Repeat Audit

The main prompt requires coverage-index-first selection, not sequential R1~R13 cycling. `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` maps to `R11 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`. The No-Repeat Index shows all C01~C32 archetypes are above 80 representative rows, so this run is not row-count filling. It is a quality-repair run focused on direct evidence that policy, subsidy, tariff, or legislation events actually travel into earnings, receivables, cashflow, order intake, or capex economics.

No-repeat rule applied:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

This batch avoids the recently repeated C05/C10/C13/C15/C16/C18~C32 and R13 review sets in the current session. It also avoids using policy headlines as generic sector positives; each row is tested for second bridge quality.

## 2. Stock-Web Price Source Validation

```yaml
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_columns: d,o,h,l,c,v,a,mc,s,m
corporate_action_contamination_rule: block D~D+180 if candidate date overlaps
```

All usable rows below use entry close from the Stock-Web tradable shard. 30D/90D/180D MFE and MAE are measured from entry close to max high / min low in the corresponding forward tradable-row window.

## 3. Loop Objective

```text
loop_objective:
- residual_false_positive_mining
- stage2_actionable_bonus_stress_test
- 4B_non_price_requirement_stress_test
- sector_specific_rule_discovery
- canonical_archetype_compression
```

Core question:

> In C31, when does a policy/tariff/subsidy/legislation headline become an actionable E2R bridge, and when is it only a policy option that should be capped at Stage2 or Stage4B/watch?

Policy events are like a door being unlocked. E2R should not score the unlocked door as revenue until someone actually walks through it: tariff approval must reduce losses or receivables, subsidy must appear in OP or cash receipt, a bidding regime must convert to order volume, and an export-policy win must convert to contracts or recognized revenue.

## 4. Trigger Table

| # | symbol | name | source event family | trigger_type | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | calibration_usable | case_role |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| 1 | 015760 | KEPCO | regulated electricity tariff hike, still-lossy utility | Stage2 | 2023-05-16 | 18,680 | 6.10 / -2.94 | 8.62 / -13.70 | 30.09 / -13.70 | true | tariff headline with incomplete cashflow bridge |
| 2 | 015760 | KEPCO | industrial tariff hike + Q3 return to profit | Stage2-Actionable | 2023-11-09 | 17,190 | 14.89 / -2.56 | 53.87 / -2.56 | 54.74 / -10.41 | true | tariff-to-earnings positive control |
| 3 | 036460 | Korea Gas Corp. | city-gas tariff increase and receivable-recovery option | Stage2-Actionable | 2024-07-05 | 47,050 | 3.72 / -18.81 | 19.66 / -24.76 | 19.66 / -27.52 | true | tariff bridge with receivables drag |
| 4 | 112610 | CS Wind | IRA/AMPC tax-credit margin support, policy-risk offset | Stage4B | 2024-11-08 | 46,750 | 13.58 / -17.22 | 13.58 / -25.88 | 26.20 / -31.76 | true | subsidy support but policy/contract volatility watch |
| 5 | 009830 | Hanwha Solutions | IRA AMPC support vs solar oversupply/loss | Stage4B | 2024-02-22 | 29,300 | 12.97 / -9.56 | 20.82 / -21.50 | 20.82 / -31.40 | true | subsidy headline without durable margin bridge |
| 6 | 336260 | Doosan Fuel Cell | CHPS hydrogen bidding market order share | Stage2-Actionable | 2023-12-07 | 21,600 | 9.03 / -4.17 | 34.26 / -7.87 | 55.09 / -17.59 | true | policy bidding system to order-volume bridge |
| 7 | 052690 | KEPCO Engineering & Construction | Czech nuclear preferred bidder / export-policy win | Stage2 | 2024-07-18 | 82,000 | 19.63 / -24.88 | 19.63 / -24.88 | 19.63 / -32.68 | true | policy-export option but final-contract bridge pending |

## 5. Evidence Notes

### 5.1 KEPCO — tariff approval is not enough; earnings conversion matters

South Korea raised electricity and city-gas prices in May 2023 while KEPCO was still carrying very large losses. This is a valid C31 policy event, but the first row remains Stage2 because the approved increase was not yet sufficient to repair the balance sheet. The later November 2023 row is stronger: industrial electricity rates were increased and KEPCO returned to quarterly operating profit, turning policy permission into an observable earnings bridge.

### 5.2 KOGAS — tariff bridge must be tested against receivables

The 2024 household gas tariff increase is a direct policy bridge for Korea Gas Corp. The row is Stage2-Actionable because the tariff mechanism is explicit, but it should not be Yellow/Green while receivables and cost-pass-through lag remain unresolved. C31 should distinguish tariff-setting authority from actual receivable liquidation.

### 5.3 CS Wind — AMPC/direct pay is a real bridge, but policy durability matters

CS Wind's own IR material describes AMPC/tax credit mechanics and direct pay effects on sales and operating margin. That makes the subsidy bridge non-price and issuer-relevant. However, late-2024 evidence also carried contract/policy volatility. The row is therefore Stage4B/watch rather than hard 4C or Green.

### 5.4 Hanwha Solutions — subsidy does not automatically repair oversupply

IRA/AMPC can be a real cash/economic item for U.S. solar manufacturing, but Hanwha Solutions' 2024 solar route shows why C31 needs a subsidy-to-margin gate. If module pricing, inventory, utilization, or global oversupply overwhelms the credit, the policy event stays Stage4B/watch.

### 5.5 Doosan Fuel Cell — bidding regime can be Actionable when order share is quantified

CHPS separated hydrogen power generation support from the existing RPS framework and created a bidding market. Doosan Fuel Cell disclosed winning 110.42 MW of general hydrogen bids in 2023, equal to 63% of the total volume. This row qualifies as Stage2-Actionable because the policy framework produced quantified order volume.

### 5.6 KEPCO E&C — policy export win is Stage2 until contract/revenue conversion

The Czech preferred-bidder event is a major policy/export catalyst and fits C31 as a policy-legislation event. However, final contract terms, project timing, and issuer-level revenue/margin conversion were still pending at the trigger. Therefore the row is capped at Stage2 despite the strong immediate price response.

## 6. Score Simulation / Current Profile Stress

| symbol | trigger_type | current profile likely behavior | residual diagnosis | preferred cap |
|---|---|---|---|---|
| 015760 2023-05-16 | Stage2 | may over-credit tariff headline | approved tariff was partial; balance-sheet repair not visible yet | Stage2 cap |
| 015760 2023-11-09 | Stage2-Actionable | appropriate or slightly late | tariff + Q3 profit gives second bridge | Actionable allowed |
| 036460 2024-07-05 | Stage2-Actionable | may over-credit receivable recovery | gas tariff helps, but receivables drag blocks Yellow/Green | Actionable cap |
| 112610 2024-11-08 | Stage4B | may treat subsidy as structural Green | AMPC valid, but policy/contract volatility requires watch | 4B/watch |
| 009830 2024-02-22 | Stage4B | may over-credit IRA/AMPC | solar oversupply and losses overwhelm subsidy headline | 4B/watch |
| 336260 2023-12-07 | Stage2-Actionable | may be too conservative if order share ignored | CHPS bid share creates quantifiable bridge | Actionable allowed |
| 052690 2024-07-18 | Stage2 | may over-credit export policy win | preferred bidder is not yet final contract / revenue | Stage2 cap |

Raw component stress direction:

```text
C31 base profile tendency: high information_confidence / capital_allocation / visibility on policy events
residual error: policy permission is often scored like cashflow execution
needed correction: second_bridge_required before Actionable/Yellow/Green
```

## 7. Proposed Shadow Rule Candidate

```yaml
sector_rule_candidate: L10_POLICY_EVENT_TO_CASHFLOW_EXECUTION_GATE_V1
canonical_rule_candidate: C31_POLICY_TARIFF_SUBSIDY_EXECUTION_SECOND_BRIDGE_GATE_V1
production_scoring_changed: false
shadow_weight_only: true
```

Rule wording:

```text
In C31, policy / subsidy / tariff / legislation / preferred-bidder events create at most Stage2 unless there is a direct execution bridge.

Stage2-Actionable requires at least one of:
- approved tariff linked to observable OP / receivables / debt repair
- subsidy or AMPC recognized in operating profit, sales, cash receipt, or transferable credit
- bidding/legislation framework converted into quantified order volume or contract award
- final contract, budget allocation, tariff formula, or reimbursement/cash mechanism
- issuer-level revenue, margin, working-capital, or cashflow conversion

Stage3-Yellow / Stage3-Green requires repeated execution evidence across at least two evidence families.

Stage4B/watch applies when:
- policy exists but execution is delayed or incomplete
- subsidy is real but offset by oversupply, utilization decline, or contract volatility
- preferred-bidder / policy win is not yet final contract or revenue
- receivables or regulated-price lag remain unresolved

Hard 4C requires policy reversal, subsidy cancellation, failed final contract, tariff freeze with balance-sheet stress, or confirmed weak offset quality.
```

## 8. Residual Contribution Summary

```yaml
new_independent_case_count: 7
new_independent_trigger_count: 7
unique_symbol_count: 6
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 3
counterexample_or_guardrail_count: 4
stage2_count: 2
stage2_actionable_count: 3
stage4b_count: 2
stage4c_count: 0
source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
current_profile_error_count: 5
production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```

Interpretation:

- C31 should not be treated as a generic policy-news bucket.
- Policy permission is the switch; cashflow execution is the current.
- The profile should reward tariff/subsidy/order frameworks only when a second bridge is visible.
- Strong MFE after a policy catalyst should not loosen Green when the issuer-level execution bridge is missing.

## 9. Machine-Readable JSONL Rows

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R11_loop_223_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","round":"R11","loop":223,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TARIFF_SUBSIDY_TO_CASHFLOW_EXECUTION_GATE_V1","symbol":"015760","name":"KEPCO","trigger_type":"Stage2","trigger_date":"2023-05-15","entry_date":"2023-05-16","entry_price":18680.0,"actual_entry_ohlcv":{"d":"2023-05-16","o":19120.0,"h":19230.0,"l":18650.0,"c":18680.0,"v":1844472.0,"m":"KOSPI"},"mfe_30d_pct":6.10,"mae_30d_pct":-2.94,"mfe_90d_pct":8.62,"mae_90d_pct":-13.70,"mfe_180d_pct":30.09,"mae_180d_pct":-13.70,"calibration_usable":true,"case_role":"tariff_headline_incomplete_cashflow_bridge","source_url":"https://www.reuters.com/markets/asia/south-korea-lifts-power-prices-by-53-delayed-move-2023-05-15/","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","production_scoring_changed":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R11_loop_223_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","round":"R11","loop":223,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TARIFF_SUBSIDY_TO_CASHFLOW_EXECUTION_GATE_V1","symbol":"015760","name":"KEPCO","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-08","entry_date":"2023-11-09","entry_price":17190.0,"actual_entry_ohlcv":{"d":"2023-11-09","o":17900.0,"h":17990.0,"l":17150.0,"c":17190.0,"v":2290944.0,"m":"KOSPI"},"mfe_30d_pct":14.89,"mae_30d_pct":-2.56,"mfe_90d_pct":53.87,"mae_90d_pct":-2.56,"mfe_180d_pct":54.74,"mae_180d_pct":-10.41,"calibration_usable":true,"case_role":"tariff_to_earnings_positive_control","source_url":"https://www.reuters.com/business/energy/kepco-hike-industrial-electricity-price-sell-assets-debt-hits-154-bln-2023-11-08/","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","production_scoring_changed":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R11_loop_223_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","round":"R11","loop":223,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TARIFF_SUBSIDY_TO_CASHFLOW_EXECUTION_GATE_V1","symbol":"036460","name":"Korea Gas Corp.","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-05","entry_date":"2024-07-05","entry_price":47050.0,"actual_entry_ohlcv":{"d":"2024-07-05","o":45050.0,"h":47750.0,"l":45000.0,"c":47050.0,"v":5418517.0,"m":"KOSPI"},"mfe_30d_pct":3.72,"mae_30d_pct":-18.81,"mfe_90d_pct":19.66,"mae_90d_pct":-24.76,"mfe_180d_pct":19.66,"mae_180d_pct":-27.52,"calibration_usable":true,"case_role":"tariff_bridge_with_receivables_drag","source_url":"https://www.koreatimes.co.kr/southkorea/society/20240705/kogas-to-raise-gas-price-for-households-by-68-from-august","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","production_scoring_changed":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R11_loop_223_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","round":"R11","loop":223,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TARIFF_SUBSIDY_TO_CASHFLOW_EXECUTION_GATE_V1","symbol":"112610","name":"CS Wind","trigger_type":"Stage4B","trigger_date":"2024-11-08","entry_date":"2024-11-08","entry_price":46750.0,"actual_entry_ohlcv":{"d":"2024-11-08","o":52400.0,"h":53100.0,"l":46650.0,"c":46750.0,"v":2485865.0,"m":"KOSPI"},"mfe_30d_pct":13.58,"mae_30d_pct":-17.22,"mfe_90d_pct":13.58,"mae_90d_pct":-25.88,"mfe_180d_pct":26.20,"mae_180d_pct":-31.76,"calibration_usable":true,"case_role":"subsidy_support_but_policy_contract_volatility_watch","source_url":"https://www.cswind.com/en/board/board.download/?n=455&seq=1&t=common","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","production_scoring_changed":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R11_loop_223_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","round":"R11","loop":223,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TARIFF_SUBSIDY_TO_CASHFLOW_EXECUTION_GATE_V1","symbol":"009830","name":"Hanwha Solutions","trigger_type":"Stage4B","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":29300.0,"actual_entry_ohlcv":{"d":"2024-02-22","o":32950.0,"h":33100.0,"l":28900.0,"c":29300.0,"v":4885784.0,"m":"KOSPI"},"mfe_30d_pct":12.97,"mae_30d_pct":-9.56,"mfe_90d_pct":20.82,"mae_90d_pct":-21.50,"mfe_180d_pct":20.82,"mae_180d_pct":-31.40,"calibration_usable":true,"case_role":"IRA_AMPC_headline_without_durable_margin_bridge","source_url":"https://www.hanwhasolutions.com/file/board/388","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","production_scoring_changed":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R11_loop_223_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","round":"R11","loop":223,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TARIFF_SUBSIDY_TO_CASHFLOW_EXECUTION_GATE_V1","symbol":"336260","name":"Doosan Fuel Cell","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-07","entry_date":"2023-12-07","entry_price":21600.0,"actual_entry_ohlcv":{"d":"2023-12-07","o":21950.0,"h":22150.0,"l":21500.0,"c":21600.0,"v":249375.0,"m":"KOSPI"},"mfe_30d_pct":9.03,"mae_30d_pct":-4.17,"mfe_90d_pct":34.26,"mae_90d_pct":-7.87,"mfe_180d_pct":55.09,"mae_180d_pct":-17.59,"calibration_usable":true,"case_role":"CHPS_policy_bidding_to_quantified_order_volume","source_url":"https://www.doosanfuelcell.com/en/media-center/medi-0101_view/?id=141","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","production_scoring_changed":false}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R11_loop_223_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md","round":"R11","loop":223,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_POLICY_TARIFF_SUBSIDY_TO_CASHFLOW_EXECUTION_GATE_V1","symbol":"052690","name":"KEPCO Engineering & Construction","trigger_type":"Stage2","trigger_date":"2024-07-17","entry_date":"2024-07-18","entry_price":82000.0,"actual_entry_ohlcv":{"d":"2024-07-18","o":95000.0,"h":98100.0,"l":80700.0,"c":82000.0,"v":5851892.0,"m":"KOSPI"},"mfe_30d_pct":19.63,"mae_30d_pct":-24.88,"mfe_90d_pct":19.63,"mae_90d_pct":-24.88,"mfe_180d_pct":19.63,"mae_180d_pct":-32.68,"calibration_usable":true,"case_role":"preferred_bidder_policy_export_without_final_contract_revenue","source_url":"https://www.reuters.com/business/energy/south-koreas-winning-bid-czech-nuclear-power-project-2024-07-17/","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","production_scoring_changed":false}
```

## 10. Batch Ingest Self-Audit

```yaml
standard_v12_filename: pass
filename_round_matches_metadata: pass
filename_loop_matches_metadata: pass
round_sector_consistency: pass
canonical_archetype_valid: pass
actual_stock_web_1d_ohlcv_used: pass
entry_price_present_for_all_usable_rows: pass
mfe_mae_30_90_180_present_for_all_usable_rows: pass
same_entry_deduped_for_aggregate: pass
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
source_proxy_only_count: 0
evidence_url_pending_count: 0
production_scoring_changed: false
handoff_prompt_executed_now: false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

When batch-applying v12 residual research, parse this MD as one standard v12 result file.
Scope: C31_POLICY_SUBSIDY_LEGISLATION_EVENT / L10_POLICY_EVENT_CROSS_REDTEAM_MISC.
Candidate rule: C31_POLICY_TARIFF_SUBSIDY_EXECUTION_SECOND_BRIDGE_GATE_V1.
Patch type: shadow rule candidate only.
Do not loosen Stage3-Green.
Do not add price-path information to runtime scoring.
Only consider a scoped rule requiring direct execution bridge before Actionable/Yellow/Green:
  tariff -> OP / receivable / debt repair,
  subsidy/AMPC -> OP / sales / cash / transferable credit,
  bidding/legislation -> quantified order or contract,
  export-policy win -> final contract / revenue / margin conversion.
```

## 12. Next Research State

```yaml
completed_round: R11
completed_loop: 223
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality reinforcement / direct cashflow execution repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_CASHFLOW_EXECUTION_DIRECT_ROW_REPAIR
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
