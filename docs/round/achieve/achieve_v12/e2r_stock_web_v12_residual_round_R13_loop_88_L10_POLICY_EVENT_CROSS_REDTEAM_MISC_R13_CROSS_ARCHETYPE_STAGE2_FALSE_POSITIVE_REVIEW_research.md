# E2R Stock-Web v12 Residual Research — R13 Loop 88 — Stage2 False Positive Cross-Review

```yaml
scheduled_round: R13
scheduled_loop: 88
completed_round: R13
completed_loop: 88
next_round: R1
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
new_independent_case_count: 0
review_trigger_count: 9
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0
```

## 1. R13 scope and scheduler validation

This file intentionally uses **R13** and `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` only. It is not a new C30/C31/C32 sector-positive mining run. The objective is a cross-archetype Stage2 false-positive review of the latest loop 88 policy/event cases.

R13 canonical scope selected:

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```

Reviewed source runs:

```text
R10 loop88 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
R11 loop88 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
R12 loop88 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Round transition:

```text
R12 loop88 completed -> R13 loop88
R13 loop88 completed -> R1 loop89
```

## 2. Stock-Web price source validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

All review rows reuse stock-web-backed 30D/90D/180D paths from the immediately preceding loop88 research MDs. Each row remains `calibration_usable=true` for R13 review, but all rows are marked `do_not_count_as_new_case=true` and `independent_evidence_weight=0.0`.

## 3. No-Repeat handling

R13 rows are cross-review rows. They deliberately reuse source cases from R10/R11/R12 and do **not** create new canonical evidence for C30/C31/C32. The hard duplicate key remains source-level:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

For this R13 file the effective key is review-only and must not be promoted into new sector evidence:

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW + source_case_id + original_canonical_archetype_id + entry_date
```

## 4. Research question

The reviewed loop88 cases all sit near the same failure surface:

```text
broad policy / PF liquidity / governance / value-up headline
    ↓
fast local price response or narrative beta
    ↓
missing company-specific bridge
    ↓
Stage2-Actionable overpromotion risk, local 4B confusion, or hard 4C timing question
```

The test is not whether these themes can move prices. They can. The test is whether E2R should treat them as durable Stage2-Actionable without a company-specific conversion bridge.

## 5. Review case grid

| review_trigger_id | original_canonical | symbol | company | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | R13 verdict | do_not_count_as_new_case |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---:|
| R13L88_STAGE2_FP_REVIEW_001_C30_012630_20240129 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 012630 | HDC | 2024-01-29 | 6880.0 | 28.20 | -1.60 | 78.80 | -1.60 | positive_control_stage2_bridge_survives | true |
| R13L88_STAGE2_FP_REVIEW_002_C30_047040_20240715 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 047040 | Daewoo Engineering & Construction | 2024-07-15 | 4050.0 | 22.60 | -12.50 | 22.60 | -27.40 | stage2_false_positive_local_4b_then_decay | true |
| R13L88_STAGE2_FP_REVIEW_003_C30_021320_20240408 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 021320 | KCC Engineering & Construction | 2024-04-08 | 4515.0 | 27.40 | -6.50 | 27.40 | -13.60 | stage2_false_positive_one_day_local_4b | true |
| R13L88_STAGE2_FP_REVIEW_004_C32_008930_20240115 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 008930 | Hanmi Science | 2024-01-15 | 46350.0 | 21.25 | -34.63 | 21.25 | -44.44 | stage2_false_positive_control_premium_local_4b_high_mae | true |
| R13L88_STAGE2_FP_REVIEW_005_C32_011200_20240207 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 011200 | HMM | 2024-02-07 | 19030.0 | 3.15 | -21.12 | 9.30 | -21.12 | stage2_false_positive_hard_4c_confirmation | true |
| R13L88_STAGE2_FP_REVIEW_006_C32_020560_20240213 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 020560 | Asiana Airlines | 2024-02-13 | 13590.0 | 7.51 | -26.27 | 7.51 | -35.39 | stage2_false_positive_regulatory_clearance_without_holder_route | true |
| R13L88_STAGE2_FP_REVIEW_007_C31_005380_20240227 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 005380 | Hyundai Motor | 2024-02-27 | 238500.0 | 25.60 | -9.20 | 25.60 | -15.30 | positive_control_policy_plus_capital_return_bridge | true |
| R13L88_STAGE2_FP_REVIEW_008_C31_005490_20240227 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 005490 | POSCO Holdings | 2024-02-27 | 427000.0 | 10.30 | -10.90 | 10.30 | -29.00 | stage2_false_positive_low_pbr_policy_beta_high_mae | true |
| R13L88_STAGE2_FP_REVIEW_009_C31_004170_20240227 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 004170 | Shinsegae | 2024-02-27 | 171300.0 | 5.30 | -10.80 | 5.30 | -18.30 | stage2_false_positive_weak_policy_beta | true |

## 6. Mechanism findings

### 6.1 Positive controls: policy plus company-specific bridge survives

The positive controls are `012630 HDC` and `005380 Hyundai Motor`.

HDC shows that a PF/BS repair route can work when the narrative contains company-level survivability and balance-sheet repair bridge rather than pure sector liquidity beta. Hyundai Motor shows the same thing in C31: broad Korea Value-up policy becomes investable only when paired with company-specific capital-return and earnings visibility.

These controls matter because R13 should not convert the guard into a blanket policy/event ban. The correct filter is not `policy_event = reject`; it is:

```text
policy_event + company_specific_bridge = eligible
policy_event_only = watch / holdout / false-positive risk
```

### 6.2 C30: PF liquidity beta without company-specific repair becomes a trap door

`047040 Daewoo E&C` and `021320 KCC E&C` show the same shape. Both achieved local MFE above 20%, but the path did not prove durable Stage2 quality. The local move behaved like steam from a pressure valve: visible, fast, and real, but not proof that the pipe was repaired.

C30 guard interpretation:

```text
Do not promote generic PF support / construction liquidity headlines to Stage2-Actionable
unless the company-specific row has PF exposure reduction, refinancing, cash collection,
margin recovery, or balance-sheet repair bridge.
```

### 6.3 C32: governance/control-premium headlines require holder-economics conversion

`008930 Hanmi Science` produced a local control-premium spike and then a large drawdown. `011200 HMM` is a harder case: once the sale/control-premium path collapsed, the event should not remain a weak positive; it can route toward hard 4C when the original control-premium thesis breaks. `020560 Asiana Airlines` shows that regulatory or merger clearance alone does not automatically equal public-holder upside.

C32 guard interpretation:

```text
binding terms + controlling-share mechanics + tender/minority-holder route + regulatory/court/creditor clearance
must be visible before Stage2-Actionable.
```

### 6.4 C31: Value-up policy needs company-specific action

`005380 Hyundai Motor` is the positive control because broad policy was paired with a company-specific bridge. `005490 POSCO Holdings` and `004170 Shinsegae` show the opposite side: low-PBR or policy beta alone was insufficient.

C31 guard interpretation:

```text
Korea Value-up / low-PBR policy headline alone is not enough.
Require capital efficiency, shareholder return execution, ROE/OP/EPS bridge, or board-level action.
```

## 7. Stage2 false-positive decision rule stress test

The best-performing interpretation across C30/C31/C32 is:

```text
if headline_is_broad_policy_or_governance_event and company_specific_bridge_missing:
    Stage2_Actionable = false
    label = watch_or_holdout

if local_MFE >= 20 and non_price_4B_evidence_missing:
    full_4B = false
    local_4B_watch = true

if original_event_thesis_breaks_non_price:
    hard_4C_watch_or_route = true
```

No global threshold delta is proposed. This R13 file strengthens interpretation of existing axes only.

## 8. Machine-readable JSONL rows

```jsonl
{"trigger_id":"R13L88_STAGE2_FP_REVIEW_001_C30_012630_20240129","source_case_id":"C30_R10_L88_012630_POSITIVE","symbol":"012630","company_name":"HDC","original_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_type":"R13-Review / PositiveControl / CompanySpecificBSRepairBridge","source_trigger_type":"C30_PF_RELIEF_LOW_PBR_PARENT_HOLDING_REPAIR_BRIDGE","trigger_date":"2024-01-26","entry_date":"2024-01-29","entry_price":6880.0,"mfe_30d_pct":28.2,"mae_30d_pct":-1.6,"mfe_90d_pct":28.2,"mae_90d_pct":-1.6,"mfe_180d_pct":78.8,"mae_180d_pct":-1.6,"peak_price":12300.0,"peak_date":"2024-11-28","review_verdict":"positive_control_stage2_bridge_survives","stage2_false_positive_label":"no_false_positive_positive_control","local_4b_watch":false,"hard_4c_watch":false,"review_note":"PF/BS theme had company-specific survivability/repair bridge; R13 uses it as positive control so false-positive guard does not overblock all C30 policy beta.","row_type":"trigger","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":false,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","reuse_reason":"R13 cross-review of R10/R11/R12 loop88 rows; do not count as new sector evidence.","do_not_propose_new_weight_delta":true,"source_proxy_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012630/2024.csv","profile_path":"atlas/symbol_profiles/012/012630.json","same_entry_group_id":"R13L88_012630_2024-01-29_6880"}
{"trigger_id":"R13L88_STAGE2_FP_REVIEW_002_C30_047040_20240715","source_case_id":"C30_R10_L88_047040_COUNTER","symbol":"047040","company_name":"Daewoo Engineering & Construction","original_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_type":"R13-Review / Stage2FalsePositive / PolicyPFSupportNoCompanyBridge","source_trigger_type":"C30_POLICY_SUPPORT_PF_LIQUIDITY_BETA_WITHOUT_COMPANY_BRIDGE","trigger_date":"2024-07-12","entry_date":"2024-07-15","entry_price":4050.0,"mfe_30d_pct":22.6,"mae_30d_pct":-12.5,"mfe_90d_pct":22.6,"mae_90d_pct":-12.5,"mfe_180d_pct":22.6,"mae_180d_pct":-27.4,"peak_price":4965.0,"peak_date":"2024-07-18","review_verdict":"stage2_false_positive_local_4b_then_decay","stage2_false_positive_label":"generic_policy_liquidity_beta_without_company_bridge","local_4b_watch":true,"hard_4c_watch":false,"review_note":"Local +20% move was real, but it was price-led and decayed into high 180D MAE. Label should be local_4b_watch plus Stage2 bridge failure, not Green.","row_type":"trigger","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":false,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","reuse_reason":"R13 cross-review of R10/R11/R12 loop88 rows; do not count as new sector evidence.","do_not_propose_new_weight_delta":true,"source_proxy_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","same_entry_group_id":"R13L88_047040_2024-07-15_4050"}
{"trigger_id":"R13L88_STAGE2_FP_REVIEW_003_C30_021320_20240408","source_case_id":"C30_R10_L88_021320_4B_COUNTER","symbol":"021320","company_name":"KCC Engineering & Construction","original_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","trigger_type":"R13-Review / Stage2FalsePositive / SmallCapConstructionPolicySpike","source_trigger_type":"C30_SMALL_CAP_CONSTRUCTION_POLICY_SPIKE_WITHOUT_DURABLE_BS_REPAIR","trigger_date":"2024-04-05","entry_date":"2024-04-08","entry_price":4515.0,"mfe_30d_pct":27.4,"mae_30d_pct":-4.5,"mfe_90d_pct":27.4,"mae_90d_pct":-6.5,"mfe_180d_pct":27.4,"mae_180d_pct":-13.6,"peak_price":5750.0,"peak_date":"2024-04-08","review_verdict":"stage2_false_positive_one_day_local_4b","stage2_false_positive_label":"thin_liquidity_policy_spike_without_bs_repair","local_4b_watch":true,"hard_4c_watch":false,"review_note":"Peak occurred on entry day; without BS/cash/restructuring bridge the correct classification is price-only spike watch, not durable Stage2-Actionable.","row_type":"trigger","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":false,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","reuse_reason":"R13 cross-review of R10/R11/R12 loop88 rows; do not count as new sector evidence.","do_not_propose_new_weight_delta":true,"source_proxy_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv","profile_path":"atlas/symbol_profiles/021/021320.json","same_entry_group_id":"R13L88_021320_2024-04-08_4515"}
{"trigger_id":"R13L88_STAGE2_FP_REVIEW_004_C32_008930_20240115","source_case_id":"R11L88_C32_008930_FAMILY_GOVERNANCE_CONTROL_PREMIUM","symbol":"008930","company_name":"Hanmi Science","original_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","trigger_type":"R13-Review / Stage2FalsePositive / GovernanceControlPremiumHeadline","source_trigger_type":"family_governance_control_premium_merger_headline","trigger_date":"2024-01-12","entry_date":"2024-01-15","entry_price":46350.0,"mfe_30d_pct":21.25,"mae_30d_pct":-16.5,"mfe_90d_pct":21.25,"mae_90d_pct":-34.63,"mfe_180d_pct":21.25,"mae_180d_pct":-44.44,"peak_price":56200.0,"peak_date":"2024-01-16","review_verdict":"stage2_false_positive_control_premium_local_4b_high_mae","stage2_false_positive_label":"family_governance_headline_without_binding_holder_economics","local_4b_watch":true,"hard_4c_watch":false,"review_note":"Control-premium narrative triggered a violent local peak, then high MAE. C32 needs binding terms and minority-holder economic route before Stage2-Actionable.","row_type":"trigger","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":false,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","reuse_reason":"R13 cross-review of R10/R11/R12 loop88 rows; do not count as new sector evidence.","do_not_propose_new_weight_delta":true,"source_proxy_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv","profile_path":"atlas/symbol_profiles/008/008930.json","same_entry_group_id":"R13L88_008930_2024-01-15_46350"}
{"trigger_id":"R13L88_STAGE2_FP_REVIEW_005_C32_011200_20240207","source_case_id":"R11L88_C32_011200_SALE_COLLAPSE","symbol":"011200","company_name":"HMM","original_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","trigger_type":"R13-Review / Stage2FalsePositive / SaleProcessCollapseHard4C","source_trigger_type":"preferred_bidder_sale_negotiation_collapse","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":19030.0,"mfe_30d_pct":6.15,"mae_30d_pct":-18.23,"mfe_90d_pct":3.15,"mae_90d_pct":-21.12,"mfe_180d_pct":9.3,"mae_180d_pct":-21.12,"peak_price":20200.0,"peak_date":"2024-02-07","review_verdict":"stage2_false_positive_hard_4c_confirmation","stage2_false_positive_label":"sale_process_collapse_should_not_be_positive_control_premium","local_4b_watch":false,"hard_4c_watch":true,"review_note":"Failed sale/negotiation collapse is not merely a weak Stage2; it can route to hard 4C when the control-premium thesis itself breaks.","row_type":"trigger","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":false,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","reuse_reason":"R13 cross-review of R10/R11/R12 loop88 rows; do not count as new sector evidence.","do_not_propose_new_weight_delta":true,"source_proxy_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011200/2024.csv","profile_path":"atlas/symbol_profiles/011/011200.json","same_entry_group_id":"R13L88_011200_2024-02-07_19030"}
{"trigger_id":"R13L88_STAGE2_FP_REVIEW_006_C32_020560_20240213","source_case_id":"R11L88_C32_020560_MERGER_CLEARANCE","symbol":"020560","company_name":"Asiana Airlines","original_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","trigger_type":"R13-Review / Stage2FalsePositive / MergerClearanceWithoutMinorityRerating","source_trigger_type":"merger_regulatory_clearance_without_minority_rerating","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":13590.0,"mfe_30d_pct":7.51,"mae_30d_pct":-22.0,"mfe_90d_pct":7.51,"mae_90d_pct":-26.27,"mfe_180d_pct":7.51,"mae_180d_pct":-35.39,"peak_price":14610.0,"peak_date":"2024-02-14","review_verdict":"stage2_false_positive_regulatory_clearance_without_holder_route","stage2_false_positive_label":"merger_clearance_not_same_as_public_holder_upside","local_4b_watch":false,"hard_4c_watch":false,"review_note":"Regulatory clearance does not automatically create minority-holder upside. R13 keeps C32 bridge requirement around tender mechanics/holder economics.","row_type":"trigger","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":false,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","reuse_reason":"R13 cross-review of R10/R11/R12 loop88 rows; do not count as new sector evidence.","do_not_propose_new_weight_delta":true,"source_proxy_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020560/2024.csv","profile_path":"atlas/symbol_profiles/020/020560.json","same_entry_group_id":"R13L88_020560_2024-02-13_13590"}
{"trigger_id":"R13L88_STAGE2_FP_REVIEW_007_C31_005380_20240227","source_case_id":"R12L88_C31_VALUEUP_005380_2024_02_27","symbol":"005380","company_name":"Hyundai Motor","original_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","trigger_type":"R13-Review / PositiveControl / ValueUpCompanySpecificCapitalReturnBridge","source_trigger_type":"C31_KOREA_VALUE_UP_POLICY_WITH_COMPANY_SPECIFIC_CAPITAL_RETURN_BRIDGE","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":238500.0,"mfe_30d_pct":9.0,"mae_30d_pct":-2.9,"mfe_90d_pct":25.6,"mae_90d_pct":-9.2,"mfe_180d_pct":25.6,"mae_180d_pct":-15.3,"peak_price":299500.0,"peak_date":"2024-06-25","review_verdict":"positive_control_policy_plus_capital_return_bridge","stage2_false_positive_label":"no_false_positive_positive_control","local_4b_watch":true,"hard_4c_watch":false,"review_note":"Value-up policy was broad, but company-specific capital return/earnings bridge made it a usable positive control. Guard must not block policy plus execution bridge.","row_type":"trigger","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":false,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","reuse_reason":"R13 cross-review of R10/R11/R12 loop88 rows; do not count as new sector evidence.","do_not_propose_new_weight_delta":true,"source_proxy_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","same_entry_group_id":"R13L88_005380_2024-02-27_238500"}
{"trigger_id":"R13L88_STAGE2_FP_REVIEW_008_C31_005490_20240227","source_case_id":"R12L88_C31_VALUEUP_005490_2024_02_27","symbol":"005490","company_name":"POSCO Holdings","original_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","trigger_type":"R13-Review / Stage2FalsePositive / ValueUpLowPBRWithoutCapitalReturnBridge","source_trigger_type":"C31_KOREA_VALUE_UP_POLICY_LOW_PBR_BETA_WITHOUT_CAPITAL_RETURN_BRIDGE","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":427000.0,"mfe_30d_pct":10.3,"mae_30d_pct":-2.2,"mfe_90d_pct":10.3,"mae_90d_pct":-10.9,"mfe_180d_pct":10.3,"mae_180d_pct":-29.0,"peak_price":471000.0,"peak_date":"2024-03-05","review_verdict":"stage2_false_positive_low_pbr_policy_beta_high_mae","stage2_false_positive_label":"policy_beta_without_capital_efficiency_or_non_policy_earnings_bridge","local_4b_watch":false,"hard_4c_watch":false,"review_note":"Low-PBR/value-up beta alone did not sustain; C31 needs capital efficiency, shareholder-return execution, or earnings bridge.","row_type":"trigger","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":false,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","reuse_reason":"R13 cross-review of R10/R11/R12 loop88 rows; do not count as new sector evidence.","do_not_propose_new_weight_delta":true,"source_proxy_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv","profile_path":"atlas/symbol_profiles/005/005490.json","same_entry_group_id":"R13L88_005490_2024-02-27_427000"}
{"trigger_id":"R13L88_STAGE2_FP_REVIEW_009_C31_004170_20240227","source_case_id":"R12L88_C31_VALUEUP_004170_2024_02_27","symbol":"004170","company_name":"Shinsegae","original_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","trigger_type":"R13-Review / Stage2FalsePositive / ValueUpRetailLowPBRWeakBeta","source_trigger_type":"C31_KOREA_VALUE_UP_POLICY_LOW_PBR_RETAIL_WITHOUT_CAPITAL_EFFICIENCY_BRIDGE","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":171300.0,"mfe_30d_pct":5.3,"mae_30d_pct":-4.7,"mfe_90d_pct":5.3,"mae_90d_pct":-10.8,"mfe_180d_pct":5.3,"mae_180d_pct":-18.3,"peak_price":180400.0,"peak_date":"2024-04-01","review_verdict":"stage2_false_positive_weak_policy_beta","stage2_false_positive_label":"low_pbr_retail_policy_headline_without_roic_or_return_execution","local_4b_watch":false,"hard_4c_watch":false,"review_note":"Retail low-PBR exposure did not translate into durable rerating without capital-efficiency or return execution bridge.","row_type":"trigger","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"is_new_independent_case":false,"do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"dedupe_for_aggregate":false,"aggregate_group_role":"r13_cross_redteam_only","reuse_reason":"R13 cross-review of R10/R11/R12 loop88 rows; do not count as new sector evidence.","do_not_propose_new_weight_delta":true,"source_proxy_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv","profile_path":"atlas/symbol_profiles/004/004170.json","same_entry_group_id":"R13L88_004170_2024-02-27_171300"}
{"row_type":"score_simulation","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","profile_hypothesis":"A policy/PF/governance/value-up headline is not Stage2-Actionable unless a company-specific bridge exists. Positive controls with bridge remain eligible; headline-only rows become watch/holdout or 4C when thesis breaks.","changed_axes":["existing_axis_kept:stage2_actionable_requires_independent_non_price_bridge","existing_axis_kept:price_only_blowoff_blocks_positive_stage","existing_axis_kept:full_4b_requires_non_price_evidence","existing_axis_kept:hard_4c_thesis_break_routes_to_4c"],"changed_thresholds":{},"eligible_review_trigger_count":9,"positive_control_count":3,"stage2_false_positive_or_high_mae_count":7,"avg_mfe_90d_pct":16.81,"avg_mae_90d_pct":-14.84,"avg_mfe_180d_pct":23.12,"avg_mae_180d_pct":-22.91,"score_return_alignment_verdict":"R13 loop88 confirms the existing bridge requirement. The issue is repeated headline beta overpromotion, not a need for a new global threshold.","production_scoring_changed":false}
{"row_type":"aggregate_metric","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"R13_POLICY_PF_GOVERNANCE_VALUEUP_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW","review_trigger_count":9,"reviewed_original_canonical_count":3,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"],"positive_control_count":3,"stage2_false_positive_or_high_mae_count":7,"local_4b_watch_count":4,"hard_4c_confirmation_count":1,"do_not_count_as_new_case_count":9,"new_independent_case_count":0,"independent_evidence_weight_total":0.0,"avg_mfe_30d_pct":15.3,"avg_mae_30d_pct":-9.46,"avg_mfe_90d_pct":16.81,"avg_mae_90d_pct":-14.84,"avg_mfe_180d_pct":23.12,"avg_mae_180d_pct":-22.91,"metric_verdict":"Holdout validation passed. C30/C31/C32 all show the same mechanism: broad headline beta can produce local MFE, but Stage2-Actionable needs company-specific bridge; hard 4C only when the thesis break is non-price-confirmed."}
{"row_type":"residual_contribution","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","residual_error_type":"policy_pf_governance_valueup_headline_overpromotion_to_stage2_actionable","affected_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"],"supporting_trigger_ids":["R13L88_STAGE2_FP_REVIEW_002_C30_047040_20240715","R13L88_STAGE2_FP_REVIEW_003_C30_021320_20240408","R13L88_STAGE2_FP_REVIEW_004_C32_008930_20240115","R13L88_STAGE2_FP_REVIEW_005_C32_011200_20240207","R13L88_STAGE2_FP_REVIEW_006_C32_020560_20240213","R13L88_STAGE2_FP_REVIEW_008_C31_005490_20240227","R13L88_STAGE2_FP_REVIEW_009_C31_004170_20240227"],"positive_control_trigger_ids":["R13L88_STAGE2_FP_REVIEW_001_C30_012630_20240129","R13L88_STAGE2_FP_REVIEW_004_C32_008930_20240115","R13L88_STAGE2_FP_REVIEW_007_C31_005380_20240227"],"new_axis_proposed":null,"existing_axis_strengthened":"stage2_actionable_requires_company_specific_non_price_bridge","existing_axis_kept":"price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c","promotion_recommendation":"holdout_validation_passed_no_patch","reason":"R13 rows are review-only and source_proxy_pending; they validate current guard direction but do not add independent evidence weight."}
{"row_type":"shadow_weight","schema_version":"v12","scheduled_round":"R13","scheduled_loop":88,"rule_scope":"R13_cross_archetype_redteam_only","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","shadow_rule_candidate":"Across C30/C31/C32, do not let policy/PF/governance/value-up headlines alone open Stage2-Actionable. Require company-specific bridge. Price-only local MFE becomes local_4b_watch; hard 4C requires explicit thesis break.","shadow_delta":0,"do_not_propose_new_weight_delta":true,"production_scoring_changed":false,"rollback_condition":"If future R13 rows show multiple company-specific bridge positives being overblocked, relax only the sector-specific bridge wording, not global thresholds."}
```

## 9. Aggregate summary

```yaml
review_trigger_count: 9
reviewed_original_canonical_count: 3
reviewed_original_canonical_ids:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
positive_control_count: 3
stage2_false_positive_or_high_mae_count: 7
local_4b_watch_count: 4
hard_4c_confirmation_count: 1
do_not_count_as_new_case_count: 9
new_independent_case_count: 0
independent_evidence_weight_total: 0.0
avg_mfe_90d_pct: 16.81
avg_mae_90d_pct: -14.84
avg_mfe_180d_pct: 23.12
avg_mae_180d_pct: -22.91
```

## 10. Residual contribution summary

```text
contribution_label = holdout_validation_passed
residual_error_type = policy_pf_governance_valueup_headline_overpromotion_to_stage2_actionable
new_axis_proposed = null
existing_axis_strengthened = stage2_actionable_requires_company_specific_non_price_bridge
existing_axis_kept = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
do_not_propose_new_weight_delta = true
production_scoring_changed = false
```

This R13 result does not propose a new patch. It says the existing guard family is directionally right: broad headline beta must pass through a company-specific bridge before Stage2-Actionable. Local price spikes should stay as `local_4b_watch`, and hard 4C should require a non-price thesis break.

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Later coding agent task:
1. Ingest this R13 loop88 Markdown as review-only cross-archetype validation.
2. Parse rows with canonical_archetype_id=R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW.
3. Ensure all trigger rows with do_not_count_as_new_case=true and independent_evidence_weight=0.0 are excluded from new sector evidence counts.
4. Use residual_contribution only as guardrail validation for existing Stage2 bridge requirements.
5. Do not create a production scoring patch from this file alone.
6. If batch aggregation finds repeated R13 Stage2 false positives across C30/C31/C32, consider only scope-specific wording in documentation/reporting, not global threshold movement.
```

## 12. Final round state

```text
completed_round = R13
completed_loop = 88
next_round = R1
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```
