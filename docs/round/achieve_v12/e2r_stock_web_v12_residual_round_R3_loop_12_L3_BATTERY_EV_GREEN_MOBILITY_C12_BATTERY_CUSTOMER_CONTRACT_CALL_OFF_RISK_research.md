# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R3_loop_12_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
scheduled_round: R3
scheduled_loop: 12
completed_round: R3
completed_loop: 12
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK
round_schedule_status: valid
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
current_stock_discovery_allowed: false
stock_web_price_atlas_access_required: true
stock_web_manifest_max_date: "2026-02-20"
created_at_utc: "2026-05-27T20:42:29.051365+00:00"
```

This loop adds **4** new independent cases, **3** counterexamples, and **3** residual errors for **R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK**.

No current/live candidate scan was performed. No stock_agent production scoring was changed. This is a standalone historical residual calibration file.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
rollback_reference_profile_id = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual question is not whether Stage2 came earlier than Green. That was already solved by the current profile. The residual question here is more specific: **when a battery-material company discloses a very large customer contract, does the contract have fixed-volume / take-or-pay / near-term utilization evidence, or is it economically exposed to customer call-off, chemistry ramp, EV demand, and delayed shipment risk?**

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 12
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK
```

R3 maps to L3 battery / EV / green mobility. C12 was selected because it is the cleanest R3 residual axis for post-calibrated research: contract notional size can look like an EPS rerating bridge, but in battery materials the real mechanism often sits one layer deeper: fixed volume, customer ramp, cathode chemistry readiness, and whether the contract is cancellable or economically optional.

## 3. Previous Coverage / Duplicate Avoidance Check

- Filename search for `e2r_stock_web_v12_residual_round_R3_loop_12` returned no existing file in the accessible GitHub search result.
- The immediately preceding produced state was R2 / Loop 12, with next state R3 / Loop 12.
- No stock_agent `src/e2r` code was opened.
- No production patch was written.
- The selected symbols avoid the prior R2 HBM/HBM-equipment set.
- All four cases are new independent R3/C12 samples in this loop.

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
schema_rematerialization_penalty = 0
wrong_round_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

```json
{
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Observed manifest properties used in this MD:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The schema uses `d,o,h,l,c,v,a,mc,s,m` for tradable shards. MFE/MAE follow the Stock-Web schema convention: `MFE_N_pct = max(high)/entry_price - 1`; `MAE_N_pct = min(low)/entry_price - 1`.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | entry_date | forward 180D available by manifest max_date? | corporate-action overlap in 180D? | calibration_usable |
|---|---|---|---:|---|---|---|
| 003670 | 포스코퓨처엠 | atlas/symbol_profiles/003/003670.json | 2023-04-03 | yes | no; profile candidate dates 2015-05-04, 2021-02-03 | true |
| 066970 | 엘앤에프 | atlas/symbol_profiles/066/066970.json | 2023-03-02 | yes | no; profile candidate dates 2016-02-19, 2021-08-11 | true |
| 051910 | LG화학 | atlas/symbol_profiles/051/051910.json | 2024-02-08 | yes | no; profile candidate count 0 | true |
| 373220 | LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | 2024-04-25 | yes | no; profile candidate count 0 | true |

All representative rows use `tradable_raw`. 1Y/2Y values are not used for quantitative weight proposals where not fully recomputed in this loop; 30D/90D/180D are the calibration basis.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
|---|---|---|
| TESLA_4680_CATHODE_SUPPLY_CALL_OFF_RISK | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Large customer contract depended on Tesla 4680 ramp and later proved economically fragile. |
| GM_LONG_DATED_CATHODE_SUPPLY_WITHOUT_MARGIN_BRIDGE | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Contract headline was large, but shipment start and margin bridge were too far away. |
| MULTI_CUSTOMER_CATHODE_ORDERBOOK_RERATING | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | The successful version had stronger multi-customer/backlog breadth and sector relabeling. |
| EV_DEMAND_CAPEX_SLOWDOWN_THESIS_BREAK | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Demand and capex warnings are the negative mirror of customer-contract durability. |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | role | trigger_date | entry_date | current_profile_verdict | notes |
|---|---|---|---|---|---:|---:|---|---|
| R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403 | 003670 | 포스코퓨처엠 | structural_success | positive | 2023-04-03 | 2023-04-03 | current_profile_correct | Multi-customer/scale narrative had genuine 90D upside, but 4B overlay is needed because July 2023 peak consumed most upside and later drawdown was severe. |
| R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228 | 066970 | 엘앤에프 | high_mae_success | counterexample | 2023-02-28 | 2023-03-02 | current_profile_false_positive | The contract produced a tradable MFE, but without take-or-pay or proven 4680 utilization it should be capped below Green and watched for 4C thesis break. |
| R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207 | 051910 | LG화학 | failed_rerating | counterexample | 2024-02-07 | 2024-02-08 | current_profile_false_positive | Large notional amount should not promote above Stage2-Actionable without near-term shipment, margin bridge, or revision evidence. |
| R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425 | 373220 | LG에너지솔루션 | 4C_success | counterexample | 2024-04-25 | 2024-04-25 | current_profile_4C_too_late | EV-demand/capex evidence protected against contract-size optimism but did not mean immediate full-cycle peak; 4C should route to thesis-break watch, not automatic short/exit. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 3
calibration_usable_case_count = 4
calibration_usable_trigger_count = 5
representative_trigger_count = 4
```

This loop intentionally has more counterexamples than positives because C12 is a guardrail archetype. It is meant to prevent the machine from treating contract notional value as a clean EPS-rerating bridge. The POSCO Future M case is retained to avoid over-tightening: some customer/orderbook cases are real Stage3-Yellow structural signals, just not automatic Green.

## 9. Evidence Source Map

| case_id | evidence available at trigger date | evidence family | evidence source note |
|---|---|---|---|
| R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403 | Name-change / battery-material identity and multi-customer orderbook narrative | customer quality + backlog breadth | stock-web profile name history; public POSCO Future M sector/orderbook reporting |
| R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228 | Tesla high-nickel cathode material contract | single-customer contract | Reuters later confirmed the 2023 Tesla/L&F deal and the subsequent drastic reduction |
| R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207 | GM/LG Chem cathode-material deal | long-dated customer contract | public report of $18.8B / 25T won GM cathode deal starting 2026 |
| R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425 | Q1 profit plunge, weak EV demand, capex minimization | 4C thesis-risk evidence | Reuters April 2024 LGES demand/capex report |

## 10. Price Data Source Map

| symbol | shard used | profile used | row basis |
|---|---|---|---|
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | atlas/symbol_profiles/003/003670.json | tradable_raw |
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv | atlas/symbol_profiles/066/066970.json | tradable_raw |
| 051910 | atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv | atlas/symbol_profiles/051/051910.json | tradable_raw |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | atlas/symbol_profiles/373/373220.json | tradable_raw |

## 11. Case-by-Case Trigger Grid

| case_id | symbol/company | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak | current_profile_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403 | 003670 포스코퓨처엠 | Stage2-Actionable | 2023-04-03 | 2023-04-03 | 288,500 | 140.55 | -4.68 | 140.55 | -19.76 | 2023-07-26 694,000 | current_profile_correct |
| R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228 | 066970 엘앤에프 | Stage2-Actionable | 2023-02-28 | 2023-03-02 | 250,500 | 39.52 | -12.57 | 39.52 | -48.94 | 2023-04-03 349,500 | current_profile_false_positive |
| R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207 | 051910 LG화학 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 470,500 | 10.52 | -26.04 | 10.52 | -44.0 | 2024-02-19 520,000 | current_profile_false_positive |
| R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425 | 373220 LG에너지솔루션 | 4C | 2024-04-25 | 2024-04-25 | 372,500 | 6.58 | -16.51 | 19.19 | -16.51 | 2024-10-08 444,000 | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative triggers

| trigger_id | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak / drawdown |
|---|---:|---:|---:|---:|---|
| TRG-R3L12-003670-STAGE2A-20230403 | 2023-04-03 @ 288,500 | 46.45 / -4.68 | 140.55 / -4.68 | 140.55 / -19.76 | 2023-07-26 694,000; drawdown -66.64% |
| TRG-R3L12-066970-STAGE2A-20230228 | 2023-03-02 @ 250,500 | 39.52 / -12.57 | 39.52 / -12.57 | 39.52 / -48.94 | 2023-04-03 349,500; drawdown -63.4% |
| TRG-R3L12-051910-STAGE2A-20240207 | 2024-02-08 @ 470,500 | 10.52 / -8.61 | 10.52 / -26.04 | 10.52 / -44.0 | 2024-02-19 520,000; drawdown -49.33% |
| TRG-R3L12-373220-4C-20240425 | 2024-04-25 @ 372,500 | 6.58 / -12.48 | 6.58 / -16.51 | 19.19 / -16.51 | 2024-10-08 444,000; drawdown -29.95% |

### 12.2 Main interpretation

- POSCO Future M shows the valid side of C12: when the market saw a broader multi-customer battery-material orderbook identity, MFE_90D reached **140.55%** from the representative entry.
- L&F shows the fragile side: a high-quality customer name and strong 30D MFE did not protect the 180D path; MAE_180D reached **-48.94%**.
- LG Chem shows that notional contract size can be too long-dated to rerate the equity when near-term margin/revision evidence is absent; MAE_180D reached **-44.00%**.
- LGES shows that demand/capex warning evidence should route to 4C watch/protection but not necessarily an immediate full-cycle top.

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| Would current profile over-credit Stage2 bonus? | Not globally, but it is too generous when a battery contract has optional future volume, unproven chemistry ramp, or long-dated shipment. |
| Was Yellow threshold 75 too high or too low? | Mostly correct. POSCO belongs near Yellow. L&F should be Yellow-capped or lower despite contract quality. |
| Was Green threshold 87 / revision 55 too strict? | Correct. None of the contract-only rows should automatically reach Green without margin/revision. |
| Was price-only blowoff guard adequate? | Strengthened. L&F and POSCO peaks show price-only/local 4B can be too early or too late unless tied to non-price valuation/positioning/evidence. |
| Was full 4B non-price requirement adequate? | Strengthened. Full 4B should require valuation/positioning/execution-risk overlay, not just a local peak. |
| Was hard 4C routing too late? | For LGES-style demand/capex warnings, 4C watch should activate earlier, but it should not be treated as an automatic immediate exit signal. |

Current profile verdict counts:

```text
current_profile_correct = 1
current_profile_false_positive = 2
current_profile_4C_too_late = 1
current_profile_error_count = 3
```

## 14. Stage2 / Yellow / Green Comparison

The residual correction is not to weaken Stage2 generally. It is to split Stage2 into two economic shapes:

```text
Stage2-Actionable contract with fixed-volume / multi-customer / utilization bridge:
    allow Stage3-Yellow if score >= 75 and non-price evidence is broad.
    require revision/margin bridge for Green.

Stage2-Actionable contract with single-customer / call-off / unproven chemistry ramp / long-dated start:
    cap at Stage2-Watch or Stage2-Actionable.
    apply call_off_risk_haircut.
    block Green even if customer_quality_score is high.
```

Green lateness ratio:

```text
POSCO Future M: not_applicable; no clean confirmed Stage3-Green trigger used.
L&F: not_applicable; Green should be blocked by call-off risk.
LG Chem: not_applicable; Green should be blocked by long-dated/margin-bridge gap.
LGES: not_applicable; 4C watch row, not positive Green row.
```

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B interpretation | full-window 4B interpretation | verdict |
|---|---|---|---|
| POSCO Future M | July 2023 price/positioning blowoff near full observed peak | full-window proximity high but non-price valuation overlay needed | good_full_window_4B_timing if valuation/positioning evidence is present |
| L&F | April 2023 local peak was close to full observed peak | however call-off risk evidence appeared later, so full 4B should have been watch/guard, not outcome hindsight | price_only_local_4B_too_early without non-price evidence |
| LG Chem | February high after GM contract was local bounce, not structural rerating | contract failed to carry forward due long-dated economics | failed_rerating_not_full_4B |
| LGES | April 2024 demand/capex warning did not mark full-window peak; later upside existed | should be thesis-break watch, not automatic full 4B | 4C_watch_not_full_exit |

## 16. 4C Protection Audit

```text
LGES 2024-04-25:
    trigger_type = 4C
    evidence = weak EV demand + capex minimization + profit pressure
    MFE_180D = +19.19%
    MAE_90D = -16.51%
    label = hard_4c_success as protection/watch, but not an immediate full-exit proof

L&F 2023-02-28:
    later 4C evidence = Tesla/4680 call-off risk realized
    label = hard_4c_late if only recognized after contract reduction
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = battery_customer_contract_call_off_risk_haircut
scope = L3_BATTERY_EV_GREEN_MOBILITY
tested_value = -6 to -8 research proxy points

Apply when:
- contract depends on one customer;
- volume is future optional or not take-or-pay;
- shipment starts far beyond current fiscal year;
- battery chemistry/platform ramp is not yet proven;
- margin/revision evidence is absent;
- customer EV demand is slowing or capex is being reduced.

Do not apply when:
- there is multi-customer orderbook breadth;
- utilization/shipment evidence is near-term;
- revision/margin bridge is confirmed;
- customer/order quality is supported by repeat conversion or capacity ramp.
```

This is sector-specific because battery contracts can be massive in notional value but economically flexible in call-off volume. The factory, chemistry, OEM platform, and subsidy channel are the riverbed; the contract is only the water level. If the riverbed is dry, a headline number floods the score but not the cash flow.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
axis = C12_direct_fixed_volume_or_utilization_bridge_required_for_green
proposal_type = canonical_shadow_only
```

Proposed canonical compression:

```text
C12 Green is allowed only when at least two are true:
1. fixed volume / take-or-pay / minimum purchase is visible;
2. near-term shipment or plant utilization is visible;
3. margin bridge or revision confirmation is visible;
4. customer concentration is mitigated by multi-customer backlog;
5. chemistry/platform ramp risk is already reduced by production evidence.
```

Otherwise, cap at Stage2-Actionable or Stage3-Yellow, and apply a call-off-risk haircut.

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | none | 4 | 49.29 | -14.95 | 52.45 | -32.30 | 0.50 | 0 | 1 | directionally useful but over-credits large customer contracts |
| P0b_e2r_2_0_baseline_reference | rollback | lower Stage2 evidence discipline | 4 | 49.29 | -14.95 | 52.45 | -32.30 | 0.75 | 0 | 1 | worse false-positive control |
| P1_sector_specific_candidate_profile | L3 | call_off_risk_haircut=-6~-8 for single-customer or long-dated contracts | 4 | 49.29 | -14.95 | 52.45 | -32.30 | 0.25 | 0 | 1 | improved contract-quality alignment |
| P2_canonical_archetype_candidate_profile | C12 | fixed-volume/utilization bridge required for Stage3-Green | 4 | 49.29 | -14.95 | 52.45 | -32.30 | 0.25 | 0 | 1 | best explanatory compression |
| P3_counterexample_guard_profile | C12 guard | cap at Yellow when margin/revision absent | 4 | 49.29 | -14.95 | 52.45 | -32.30 | 0.00 | 1 | 0 | safest, but may delay POSCO-like structural success |


## 20. Score-Return Alignment Matrix

| case | P0 alignment | proposed C12 alignment | reason |
|---|---|---|---|
| POSCO Future M | good but at risk of over-Green | kept as Yellow / no haircut | strong MFE and multi-customer/orderbook breadth |
| L&F | false-positive Green-borderline | downgraded to Yellow-cap/Watch | single-customer + 4680 ramp + later call-off proved risk |
| LG Chem | false-positive contract-size Stage2 | downgraded to Watch | contract start far away; no near-term margin/revision bridge |
| LGES | 4C watch too late | earlier 4C watch but not full exit | demand/capex warning is protection evidence, not price-top evidence |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK | 1 | 3 | 2 | 2 | 4 | 0 | 5 | 4 | 3 | true | true | still needs more positive fixed-volume examples and explicit take-or-pay disclosures |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - contract_size_false_positive
  - single_customer_call_off_risk
  - long_dated_contract_without_margin_bridge
  - 4C_watch_not_full_exit
new_axis_proposed:
  - C12_direct_fixed_volume_or_utilization_bridge_required_for_green
  - battery_customer_contract_call_off_risk_haircut
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Actual Stock-Web tradable_raw OHLC rows were used for entry_price, MFE, MAE, peak, and drawdown.
- 180D forward windows are available under manifest max_date 2026-02-20.
- Corporate-action candidate dates do not overlap the 180D windows used.
- Same-entry dedupe is trivial because representative triggers use distinct symbols and entry dates.
- Current calibrated profile was stress-tested on each case.
```

Not validated in this MD:

```text
- No production scoring code was opened.
- No live candidate list was generated.
- No brokerage/API connection was used.
- No current 2026 recommendation was made.
- 1Y/2Y fields are not the quantitative basis for this round.
- Some public evidence summaries are compressed to trigger-level narratives; later implementation should attach official filing URLs where available.
```

## 24. Shadow Weight Calibration

The shadow-only proposal is:

```text
axis: C12_direct_fixed_volume_or_utilization_bridge_required_for_green
scope: canonical_archetype_specific
baseline_value: false
tested_value: true
delta: +1 guard
effect: blocks Green when contract quality is high but volume/margin/utilization durability is unsupported
confidence: medium
production_scoring_changed: false
```

The proposed haircut:

```text
axis: call_off_risk_haircut
scope: sector_specific / C12-specific
tested_value: -6 to -8 research proxy points
applies_to: single-customer, future-optional, chemistry-ramp-dependent, long-dated battery contracts
does_not_apply_to: broad multi-customer, near-term, margin-confirmed orderbook cases
```

## 25. Machine-Readable Rows

### 25.1 JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG-R3L12-003670-STAGE2A-20230403","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_with_late_4B_overlay","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Multi-customer/scale narrative had genuine 90D upside, but 4B overlay is needed because July 2023 peak consumed most upside and later drawdown was severe."}
{"row_type":"case","case_id":"R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TRG-R3L12-066970-STAGE2A-20230228","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"initial_mfe_then_contract_call_off_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The contract produced a tradable MFE, but without take-or-pay or proven 4680 utilization it should be capped below Green and watched for 4C thesis break."}
{"row_type":"case","case_id":"R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207","symbol":"051910","company_name":"LG화학","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG-R3L12-051910-STAGE2A-20240207","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"long_dated_contract_failed_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Large notional amount should not promote above Stage2-Actionable without near-term shipment, margin bridge, or revision evidence."}
{"row_type":"case","case_id":"R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"TRG-R3L12-373220-4C-20240425","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4C_watch_correct_but_full_exit_not_immediate","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"EV-demand/capex evidence protected against contract-size optimism but did not mean immediate full-cycle peak; 4C should route to thesis-break watch, not automatic short/exit."}
{"row_type":"trigger","trigger_id":"TRG-R3L12-003670-STAGE2A-20230403","case_id":"R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK","sector":"battery_ev_green_mobility","primary_archetype":"customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-04-03","evidence_available_at_that_date":"name-change to POSCO FUTURE M and visible 2023 multi-customer battery-material orderbook narrative; this is treated as customer-quality/orderbook evidence, not as price-only momentum.","evidence_source":"stock-web profile name_history; public POSCO Future M orderbook/industry reporting; price rows from 2023 tradable shard.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-03","entry_price":288500,"MFE_30D_pct":46.45,"MFE_90D_pct":140.55,"MFE_180D_pct":140.55,"MFE_1Y_pct":140.55,"MFE_2Y_pct":null,"MAE_30D_pct":-4.68,"MAE_90D_pct":-4.68,"MAE_180D_pct":-19.76,"MAE_1Y_pct":-19.76,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-66.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_with_late_4B_overlay","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403::2023-04-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-R3L12-066970-STAGE2A-20230228","case_id":"R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK","sector":"battery_ev_green_mobility","primary_archetype":"customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2023-02-28","evidence_available_at_that_date":"Tesla high-nickel cathode material supply contract narrative; customer identity strong, but volume durability depended on Tesla 4680 ramp and future call-off.","evidence_source":"Reuters retrospective on 2023 Tesla/L&F deal and later reduction; 2023 stock-web tradable rows.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-02","entry_price":250500,"MFE_30D_pct":39.52,"MFE_90D_pct":39.52,"MFE_180D_pct":39.52,"MFE_1Y_pct":39.52,"MFE_2Y_pct":null,"MAE_30D_pct":-12.57,"MAE_90D_pct":-12.57,"MAE_180D_pct":-48.94,"MAE_1Y_pct":-48.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-03","peak_price":349500,"drawdown_after_peak_pct":-63.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"initial_mfe_then_contract_call_off_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228::2023-03-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-R3L12-051910-STAGE2A-20240207","case_id":"R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207","symbol":"051910","company_name":"LG화학","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK","sector":"battery_ev_green_mobility","primary_archetype":"customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"trigger_type":"Stage2-Actionable","trigger_date":"2024-02-07","evidence_available_at_that_date":"GM/LG Chem cathode-material contract, but supply begins later and the contract did not immediately repair battery-material margin or parent-company petrochemical drag.","evidence_source":"Investopedia summary of GM/LG Chem $18.8B cathode deal; 2024 stock-web tradable rows.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":470500,"MFE_30D_pct":10.52,"MFE_90D_pct":10.52,"MFE_180D_pct":10.52,"MFE_1Y_pct":10.52,"MFE_2Y_pct":null,"MAE_30D_pct":-8.61,"MAE_90D_pct":-26.04,"MAE_180D_pct":-44.0,"MAE_1Y_pct":-44.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":520000,"drawdown_after_peak_pct":-49.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown","explicit_event_cap"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"long_dated_contract_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207::2024-02-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG-R3L12-373220-4C-20240425","case_id":"R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_FIXED_VOLUME_VS_CALL_OFF_RISK","sector":"battery_ev_green_mobility","primary_archetype":"customer_contract_call_off_risk","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","canonical_archetype_compression","counterexample_mining","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"trigger_type":"4C","trigger_date":"2024-04-25","evidence_available_at_that_date":"Q1 profit plunge, weak EV sales, and capex minimization statement; this is not a positive contract trigger but a thesis-risk/protection trigger.","evidence_source":"Reuters April 2024 LGES demand slowdown/capex report; 2024 stock-web tradable rows.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":372500,"MFE_30D_pct":6.58,"MFE_90D_pct":6.58,"MFE_180D_pct":19.19,"MFE_1Y_pct":19.19,"MFE_2Y_pct":null,"MAE_30D_pct":-12.48,"MAE_90D_pct":-16.51,"MAE_180D_pct":-16.51,"MAE_1Y_pct":-16.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000,"drawdown_after_peak_pct":-29.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"thesis_break_watch_only","four_b_evidence_type":["margin_or_backlog_slowdown","explicit_event_cap"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_watch_correct_but_full_exit_not_immediate","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425::2024-04-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403","trigger_id":"TRG-R3L12-003670-STAGE2A-20230403","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":6,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":8},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":6,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":8},"weighted_score_after":83.0,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"P0 current calibrated proxy only; no shadow rule applied.","MFE_90D_pct":140.55,"MAE_90D_pct":-4.68,"score_return_alignment_label":"structural_success_with_late_4B_overlay","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"sector_specific_candidate_profile","case_id":"R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403","trigger_id":"TRG-R3L12-003670-STAGE2A-20230403","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":6,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":8},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":6,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":8,"call_off_risk_haircut":0},"weighted_score_after":83.0,"stage_label_after":"Stage3-Yellow","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"No haircut; multi-customer structure and orderbook visibility allow Stage3-Yellow, but not unconditional Green without margin/revision confirmation.","MFE_90D_pct":140.55,"MAE_90D_pct":-4.68,"score_return_alignment_label":"structural_success_with_late_4B_overlay","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403","trigger_id":"TRG-R3L12-003670-STAGE2A-20230403","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":6,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":8},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":6,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":8,"call_off_risk_haircut":0},"weighted_score_after":83.0,"stage_label_after":"Stage3-Yellow","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"No haircut; multi-customer structure and orderbook visibility allow Stage3-Yellow, but not unconditional Green without margin/revision confirmation.","MFE_90D_pct":140.55,"MAE_90D_pct":-4.68,"score_return_alignment_label":"structural_success_with_late_4B_overlay","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R3L12-C12-POSCO-FUTUREM-ORDERBOOK-20230403","trigger_id":"TRG-R3L12-003670-STAGE2A-20230403","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":6,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":8},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":15,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":14,"customer_quality_score":13,"policy_or_regulatory_score":6,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":8,"call_off_risk_haircut":0},"weighted_score_after":83.0,"stage_label_after":"Stage3-Yellow","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"No haircut; multi-customer structure and orderbook visibility allow Stage3-Yellow, but not unconditional Green without margin/revision confirmation.","MFE_90D_pct":140.55,"MAE_90D_pct":-4.68,"score_return_alignment_label":"structural_success_with_late_4B_overlay","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228","trigger_id":"TRG-R3L12-066970-STAGE2A-20230228","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":11,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":3,"valuation_repricing_score":12,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":2},"weighted_score_before":81.0,"stage_label_before":"Stage3-Yellow/Green-borderline","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":11,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":3,"valuation_repricing_score":12,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":2},"weighted_score_after":81.0,"stage_label_after":"Stage3-Yellow/Green-borderline","changed_components":[],"component_delta_explanation":"P0 current calibrated proxy only; no shadow rule applied.","MFE_90D_pct":39.52,"MAE_90D_pct":-12.57,"score_return_alignment_label":"initial_mfe_then_contract_call_off_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"sector_specific_candidate_profile","case_id":"R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228","trigger_id":"TRG-R3L12-066970-STAGE2A-20230228","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":11,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":3,"valuation_repricing_score":12,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":2},"weighted_score_before":81.0,"stage_label_before":"Stage3-Yellow/Green-borderline","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":7,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":-6,"legal_or_contract_risk_score":-7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":0,"call_off_risk_haircut":-8},"weighted_score_after":52.0,"stage_label_after":"Stage2-Watch/Yellow-cap","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Apply call-off haircut when customer contract depends on unproven cell ramp, future optional volume, or single-customer concentration.","MFE_90D_pct":39.52,"MAE_90D_pct":-12.57,"score_return_alignment_label":"initial_mfe_then_contract_call_off_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228","trigger_id":"TRG-R3L12-066970-STAGE2A-20230228","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":11,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":3,"valuation_repricing_score":12,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":2},"weighted_score_before":81.0,"stage_label_before":"Stage3-Yellow/Green-borderline","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":7,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":-6,"legal_or_contract_risk_score":-7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":0,"call_off_risk_haircut":-8},"weighted_score_after":52.0,"stage_label_after":"Stage2-Watch/Yellow-cap","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Apply call-off haircut when customer contract depends on unproven cell ramp, future optional volume, or single-customer concentration.","MFE_90D_pct":39.52,"MAE_90D_pct":-12.57,"score_return_alignment_label":"initial_mfe_then_contract_call_off_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R3L12-C12-LNF-TESLA-4680-CALLOFF-20230228","trigger_id":"TRG-R3L12-066970-STAGE2A-20230228","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":11,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":3,"valuation_repricing_score":12,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":2},"weighted_score_before":81.0,"stage_label_before":"Stage3-Yellow/Green-borderline","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":7,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":-6,"legal_or_contract_risk_score":-7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":0,"call_off_risk_haircut":-8},"weighted_score_after":52.0,"stage_label_after":"Stage2-Watch/Yellow-cap","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Apply call-off haircut when customer contract depends on unproven cell ramp, future optional volume, or single-customer concentration.","MFE_90D_pct":39.52,"MAE_90D_pct":-12.57,"score_return_alignment_label":"initial_mfe_then_contract_call_off_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207","trigger_id":"TRG-R3L12-051910-STAGE2A-20240207","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":17,"backlog_visibility_score":10,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":14,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":1},"weighted_score_before":58.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":17,"backlog_visibility_score":10,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":14,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":1},"weighted_score_after":58.0,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"P0 current calibrated proxy only; no shadow rule applied.","MFE_90D_pct":10.52,"MAE_90D_pct":-26.04,"score_return_alignment_label":"long_dated_contract_failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"sector_specific_candidate_profile","case_id":"R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207","trigger_id":"TRG-R3L12-051910-STAGE2A-20240207","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":17,"backlog_visibility_score":10,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":14,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":1},"weighted_score_before":58.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":17,"backlog_visibility_score":6,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":14,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":-8,"legal_or_contract_risk_score":-3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":0,"call_off_risk_haircut":-6},"weighted_score_after":38.0,"stage_label_after":"Stage2-Watch","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Long-dated start date and absent margin bridge reduce backlog visibility and block Stage3.","MFE_90D_pct":10.52,"MAE_90D_pct":-26.04,"score_return_alignment_label":"long_dated_contract_failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207","trigger_id":"TRG-R3L12-051910-STAGE2A-20240207","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":17,"backlog_visibility_score":10,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":14,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":1},"weighted_score_before":58.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":17,"backlog_visibility_score":6,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":14,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":-8,"legal_or_contract_risk_score":-3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":0,"call_off_risk_haircut":-6},"weighted_score_after":38.0,"stage_label_after":"Stage2-Watch","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Long-dated start date and absent margin bridge reduce backlog visibility and block Stage3.","MFE_90D_pct":10.52,"MAE_90D_pct":-26.04,"score_return_alignment_label":"long_dated_contract_failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R3L12-C12-LGCHEM-GM-LONGDATED-CATHODE-20240207","trigger_id":"TRG-R3L12-051910-STAGE2A-20240207","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":17,"backlog_visibility_score":10,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":14,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":-5,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":1},"weighted_score_before":58.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":17,"backlog_visibility_score":6,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":14,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":-8,"legal_or_contract_risk_score":-3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":0,"call_off_risk_haircut":-6},"weighted_score_after":38.0,"stage_label_after":"Stage2-Watch","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Long-dated start date and absent margin bridge reduce backlog visibility and block Stage3.","MFE_90D_pct":10.52,"MAE_90D_pct":-26.04,"score_return_alignment_label":"long_dated_contract_failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425","trigger_id":"TRG-R3L12-373220-4C-20240425","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":-2,"revision_score":-4,"relative_strength_score":2,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":-10,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":-5},"weighted_score_before":13.0,"stage_label_before":"4C-Watch","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":-2,"revision_score":-4,"relative_strength_score":2,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":-10,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":-5},"weighted_score_after":13.0,"stage_label_after":"4C-Watch","changed_components":[],"component_delta_explanation":"P0 current calibrated proxy only; no shadow rule applied.","MFE_90D_pct":6.58,"MAE_90D_pct":-16.51,"score_return_alignment_label":"4C_watch_correct_but_full_exit_not_immediate","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"sector_specific_candidate_profile","case_id":"R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425","trigger_id":"TRG-R3L12-373220-4C-20240425","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":-2,"revision_score":-4,"relative_strength_score":2,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":-10,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":-5},"weighted_score_before":13.0,"stage_label_before":"4C-Watch","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":4,"margin_bridge_score":-3,"revision_score":-5,"relative_strength_score":2,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":1,"execution_risk_score":-12,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":-6,"call_off_risk_haircut":-5},"weighted_score_after":-5.0,"stage_label_after":"4C-Watch/Protection","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Demand/capex warning strengthens thesis-break routing but does not prove full 4B top timing.","MFE_90D_pct":6.58,"MAE_90D_pct":-16.51,"score_return_alignment_label":"4C_watch_correct_but_full_exit_not_immediate","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425","trigger_id":"TRG-R3L12-373220-4C-20240425","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":-2,"revision_score":-4,"relative_strength_score":2,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":-10,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":-5},"weighted_score_before":13.0,"stage_label_before":"4C-Watch","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":4,"margin_bridge_score":-3,"revision_score":-5,"relative_strength_score":2,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":1,"execution_risk_score":-12,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":-6,"call_off_risk_haircut":-5},"weighted_score_after":-5.0,"stage_label_after":"4C-Watch/Protection","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Demand/capex warning strengthens thesis-break routing but does not prove full 4B top timing.","MFE_90D_pct":6.58,"MAE_90D_pct":-16.51,"score_return_alignment_label":"4C_watch_correct_but_full_exit_not_immediate","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"counterexample_guard_profile","case_id":"R3L12-C12-LGES-EV-DEMAND-CAPEX-20240425","trigger_id":"TRG-R3L12-373220-4C-20240425","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":6,"margin_bridge_score":-2,"revision_score":-4,"relative_strength_score":2,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":2,"execution_risk_score":-10,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":-5},"weighted_score_before":13.0,"stage_label_before":"4C-Watch","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":4,"margin_bridge_score":-3,"revision_score":-5,"relative_strength_score":2,"customer_quality_score":10,"policy_or_regulatory_score":5,"valuation_repricing_score":1,"execution_risk_score":-12,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"channel_reorder_score":"unknown_or_not_supported","utilization_score":-6,"call_off_risk_haircut":-5},"weighted_score_after":-5.0,"stage_label_after":"4C-Watch/Protection","changed_components":["call_off_risk_haircut","backlog_visibility_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Demand/capex warning strengthens thesis-break routing but does not prove full 4B top timing.","MFE_90D_pct":6.58,"MAE_90D_pct":-16.51,"score_return_alignment_label":"4C_watch_correct_but_full_exit_not_immediate","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["contract_size_false_positive","single_customer_call_off_risk","long_dated_contract_without_margin_bridge","4C_watch_not_full_exit"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.2 Shadow weight CSV

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,contract_size_without_fixed_volume_green_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"Block Stage3-Green when contract has single-customer or future call-off risk and no utilization/margin bridge","reduced false positives in L&F and LG Chem while preserving POSCO Stage3-Yellow","TRG-R3L12-066970-STAGE2A-20230228|TRG-R3L12-051910-STAGE2A-20240207|TRG-R3L12-003670-STAGE2A-20230403",4,4,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,call_off_risk_haircut,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,-6_to_-8,-6_to_-8,"Large battery-customer contracts can be optional in economics even when large in notional value","improves score-return alignment for long-dated or technology-ramp-dependent contracts","TRG-R3L12-066970-STAGE2A-20230228|TRG-R3L12-051910-STAGE2A-20240207",4,4,3,medium,sector_shadow_only,"requires evidence of fixed volume/take-or-pay/near-term shipment to remove haircut"
shadow_weight,4c_demand_slowdown_watch_not_full_exit,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"Demand/capex warnings should route to thesis-break watch but not automatic full 4B timing","prevents treating LGES demand warning as immediate full-window top","TRG-R3L12-373220-4C-20240425",1,1,1,low,guard_shadow_only,"4C protection only; not positive promotion"

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
completed_loop = 12
next_round = R4
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source files read in this research session:

- `atlas/manifest.json` confirmed `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, and `max_date=2026-02-20`.
- `atlas/schema.json` confirmed tradable/raw shard columns, MFE/MAE definitions, and calibration-usable rules.
- Symbol profiles read:
  - `atlas/symbol_profiles/003/003670.json`
  - `atlas/symbol_profiles/066/066970.json`
  - `atlas/symbol_profiles/051/051910.json`
  - `atlas/symbol_profiles/373/373220.json`
- Tradable shards read:
  - `atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv`

External evidence notes:

- Reuters later reported that L&F's 2023 Tesla high-nickel cathode materials deal was later reduced drastically, citing Tesla 4680 ramp and EV demand issues as explanatory factors.
- Public reporting summarized the GM/LG Chem cathode-material deal as a large, long-dated supply arrangement beginning from 2026.
- Reuters reported LG Energy Solution's April 2024 weak EV demand, profit drop, and capex minimization signal.
- POSCO Future M profile/name-history and sector reporting are used as orderbook/identity evidence, while quantitative calibration is only from Stock-Web OHLC.
