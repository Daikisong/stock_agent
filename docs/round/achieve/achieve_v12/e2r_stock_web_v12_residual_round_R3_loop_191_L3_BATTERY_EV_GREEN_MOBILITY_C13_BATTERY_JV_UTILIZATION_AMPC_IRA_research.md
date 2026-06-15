# E2R Stock-Web V12 Residual Research — R3 Loop 191 — C13 Battery JV Utilization AMPC IRA

```yaml
selected_round: R3
selected_loop: 191
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: mixed_c13_us_jv_ampc_ira_utilization_parent_proxy_leaf_set
research_session: post_calibrated_sector_archetype_residual_research
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_patch_allowed: false
live_candidate_mode: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
output_filename: e2r_stock_web_v12_residual_round_R3_loop_191_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
```

## 1. Selection rationale

This pass continues after loop 190. The original No-Repeat Index lists **C13_BATTERY_JV_UTILIZATION_AMPC_IRA** as a 58-row Priority 2 quality-repair zone. The session already cleared P0/P1 and produced one dedicated C13 pass at loop 161, but that pass was concentrated in LG Energy Solution and Samsung SDI quarterly AMPC/utilization headlines. This loop therefore adds a second C13 pass focused on a different fine leaf: **U.S. JV/capex/IRA localization headlines versus actual utilization, ex-credit profit, ramp timing, and listed-entity value capture**.

The guiding question is simple: a battery JV is a factory blueprint, but E2R should not treat every blueprint as running current through the machine. C13 should ask whether the plant/JV/AMPC bridge has already reached **utilization, ex-AMPC operating profit, revenue timing, or customer call-off visibility**.

## 2. Stock-Web validation scope

```text
primary_price_source = Songdaiki/stock-web
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
entry_price_rule = close price on entry_date
mfe_mae_rule = max(high) / min(low) over next 30/90/180 tradable rows after entry_date
manifest_max_date = 2026-02-20
```

Profile caveat summary:

- 373220 LG에너지솔루션: corporate_action_candidate_count = 0.
- 051910 LG화학: corporate_action_candidate_count = 0.
- 096770 SK이노베이션: profile has a corporate-action candidate at 2024-11-20, but the 2023 entry windows used here complete their D+180 windows before that candidate; the regular 180D rows are retained.
- 006400 삼성SDI and 003670 POSCO퓨처엠: no 2023 trigger window contamination was detected in the downloaded tradable rows used for this pass.

## 3. Novelty and no-repeat check

Hard duplicate key rule used:

```text
canonical_archetype_id + ticker + trigger_type + entry_date
```

This loop avoids the prior C13 loop 161 trigger families:

- LG Energy Solution Q1/Q2/Q3 2024 AMPC/utilization and Q1 2025 reset entries.
- Samsung SDI Q2 2024, StarPlus DOE loan, and Q1 2025 loss/JV/yield entries.

New or distinct trigger families in this loop:

- LGES Arizona standalone complex and Toyota 20GWh supply.
- LG Chem Tennessee cathode/IRA compliance as parent/material proxy boundary.
- SK Innovation BlueOval SK DOE conditional loan and SK On loss-narrowing productivity case.
- Samsung SDI second StarPlus JV 2027 ramp and Q3 2023 auto-battery revenue/margin case.
- POSCO Future M/GM Ultium CAM expansion and binding supply as IRA chain positive with 4B exit risk.

## 4. Case inventory

| case_id | ticker | company | trigger_date | trigger_type | classification | fine_archetype_id |
|---|---:|---|---:|---|---|---|
| C13-L191-001 | 373220 | LG에너지솔루션 | 2023-03-24 | Stage2-Watch | counterexample | C13_US_STANDALONE_CAPEX_IRA_LONG_DATED_RAMP |
| C13-L191-002 | 373220 | LG에너지솔루션 | 2023-10-04 | Stage2-Watch | counterexample | C13_NAMED_CUSTOMER_CONTRACT_BUT_2025_RAMP_DELAY |
| C13-L191-003 | 051910 | LG화학 | 2023-12-20 | Stage4B-Watch | counterexample | C13_PARENT_CATHODE_PLANT_IRA_BRIDGE_BUT_PARENT_SPREAD_DRAG |
| C13-L191-004 | 096770 | SK이노베이션 | 2023-06-23 | Stage2-Actionable | positive_with_4b_exit_guard | C13_BLUEOVAL_SK_DOE_CONDITIONAL_LOAN_LOCALIZATION |
| C13-L191-005 | 096770 | SK이노베이션 | 2023-07-28 | Stage4B-Watch | counterexample | C13_LOSS_NARROWING_PRODUCTIVITY_BUT_NOT_PROFIT_CONVERSION |
| C13-L191-006 | 006400 | 삼성SDI | 2023-07-24 | Stage2-Watch | counterexample | C13_STARPLUS_SECOND_JV_LONG_DATED_STARTUP |
| C13-L191-007 | 006400 | 삼성SDI | 2023-10-26 | Stage2-Actionable | positive_with_high_mae_guard | C13_AUTO_BATTERY_REVENUE_MARGIN_WITH_EV_TAPE_GUARD |
| C13-L191-008 | 003670 | POSCO퓨처엠 | 2023-06-02 | Stage2-Actionable | positive_with_4b_exit_guard | C13_ULTIUM_CAM_JV_BINDING_SUPPLY_IRA_CHAIN |

## 5. Price-path table

| case_id | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C13-L191-001 | 2023-03-27 | 574,000 | 6.79 | -4.53 | 8.01 | -7.67 | 8.01 | -34.58 |
| C13-L191-002 | 2023-10-05 | 467,500 | 7.17 | -19.68 | 7.17 | -22.57 | 7.17 | -31.02 |
| C13-L191-003 | 2023-12-20 | 504,000 | 0.0 | -23.91 | 3.17 | -27.38 | 3.17 | -47.72 |
| C13-L191-004 | 2023-06-23 | 182,600 | 25.68 | -13.58 | 25.68 | -34.23 | 25.68 | -41.13 |
| C13-L191-005 | 2023-07-28 | 189,500 | 19.79 | -12.08 | 19.79 | -36.62 | 19.79 | -45.86 |
| C13-L191-006 | 2023-07-25 | 712,000 | 3.23 | -18.12 | 3.23 | -41.43 | 3.23 | -51.97 |
| C13-L191-007 | 2023-10-27 | 452,000 | 15.49 | -7.74 | 15.49 | -24.34 | 15.49 | -24.34 |
| C13-L191-008 | 2023-06-05 | 380,000 | 21.05 | -9.34 | 82.63 | -17.5 | 82.63 | -39.08 |

## 6. Case notes

### C13-L191-001 — LG Energy Solution Arizona complex

Reuters reported that LG Energy Solution resumed its stalled Arizona project with a roughly USD 5.6bn investment to qualify for IRA incentives. The evidence was real and strategic, but the price path shows only modest upside and a deep 180D drawdown. This is a capex/localization bridge, not yet a utilization or ex-AMPC earnings bridge. It should remain Stage2-Watch unless construction progress is paired with customer call-off and profit conversion.

### C13-L191-002 — LG Energy Solution Toyota supply

The Toyota agreement had a clear named customer and 20GWh annual capacity from 2025, produced at LGES Michigan. The problem is timing. A 2025 supply start did not protect a 2023 entry from sector derating. C13 should separate named-customer quality from near-term utilization.

### C13-L191-003 — LG Chem Tennessee cathode plant

LG Chem's Tennessee cathode plant explicitly supports IRA-compliant North American supply. However, LG Chem as the listed entity still carried chemical spread, capex, and parent-proxy drag. This is a useful C13 boundary: parent/material proxy exposure needs listed-entity conversion, not just IRA vocabulary.

### C13-L191-004 — SK Innovation / BlueOval SK DOE conditional loan

The BlueOval SK DOE conditional loan was a hard policy-financing/JV localization bridge. It created a strong short-term MFE, but the 90D/180D MAE shows why C13 positives still need 4B exit discipline when the listed parent still carries battery losses, refining volatility, or funding burden.

### C13-L191-005 — SK Innovation Q2 loss narrowing

SK On narrowed losses and cited productivity/new-factory improvements. That was a better signal than generic EV optimism, but still not the same as ex-credit profit conversion. The path became a high-MAE row, so the rule should require confirmed profitable utilization before Actionable escalation.

### C13-L191-006 — Samsung SDI second StarPlus JV

The second U.S. StarPlus JV was real but long-dated: initial production was planned for 2027. The stock path punished the timing gap. This is the cleanest warning in the set: long-dated JV capacity should not be granted full near-term Stage2-Actionable credit.

### C13-L191-007 — Samsung SDI Q3 2023

Samsung SDI's Q3 2023 report linked record revenue to automotive battery sales and margin. This was not merely capex language; it had realized revenue/margin content. The MFE was not explosive, but the row deserves a staged positive with high-MAE guard.

### C13-L191-008 — POSCO Future M / Ultium CAM

The GM/POSCO Future M expansion was a powerful IRA/North America chain case: JV expansion plus binding CAM supply. The path delivered very large MFE, but then a severe drawdown. This should be a positive C13-like supply-chain bridge with explicit 4B exit guard, not a forever-Green unlock.

## 7. Current calibrated profile stress test

Observed residual errors:

1. **Long-dated JV over-credit** — planned 2027 capacity or 2025 supply start can be scored too much like present utilization.
2. **AMPC/IRA optical-profit error** — policy credit and tax language can hide ex-credit operating losses or delayed ramp.
3. **Parent/material proxy gap** — parent-listed equities and material suppliers should not inherit full C13 weight unless the listed entity captures cash flow.
4. **MFE/MAE asymmetry** — some C13 rows produce very good early MFE and later severe MAE, so successful positives need explicit 4B exit or staged-entry instructions.

## 8. Shadow rule candidate

```text
rule_id = C13_JV_UTILIZATION_AMPC_EX_CREDIT_AND_RAMP_TIMING_GATE_V2
scope = canonical_archetype_id:C13_BATTERY_JV_UTILIZATION_AMPC_IRA
production_scoring_changed = false
shadow_weight_only = true
```

Proposed rule:

```text
C13 Stage2-Actionable should require at least one support bridge and one conversion bridge.

support_bridge examples:
- named JV or named OEM customer
- binding financing/DOE/IRA/AMPC support
- announced or operating U.S./FTA-localized capacity
- customer plant-linked supply chain placement

conversion_bridge examples:
- actual utilization improvement
- ex-AMPC operating profit or clear path to it
- revenue recognition window within the forward price window
- shipment/call-off visibility
- margin/revision bridge at the listed entity level

If support_bridge exists but conversion_bridge is absent:
- cap at Stage2-Watch
- attach high-MAE guard if MAE90 <= -20
- do not permit Stage3-Green

If MFE90 >= 20 and MAE90 <= -30:
- label positive_with_4B_exit_guard, not clean positive
```

## 9. Machine-readable rows

```jsonl
{"row_type": "trigger", "case_id": "C13-L191-001", "ticker": "373220", "company_name": "LG에너지솔루션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_US_STANDALONE_CAPEX_IRA_LONG_DATED_RAMP", "trigger_date": "2023-03-24", "entry_date": "2023-03-27", "entry_price": 574000, "trigger_type": "Stage2-Watch", "classification": "counterexample", "evidence_family": "Arizona standalone battery complex / IRA capex", "evidence_url": "https://www.reuters.com/technology/south-koreas-lges-resume-arizona-battery-factory-plan-with-56-bln-investment-2023-03-24/", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 6.79, "MAE_30D_pct": -4.53, "MFE_90D_pct": 8.01, "MAE_90D_pct": -7.67, "MFE_180D_pct": 8.01, "MAE_180D_pct": -34.58, "peak_180D_date": "2023-07-26", "trough_180D_date": "2023-11-01", "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Watch|2023-03-27", "current_profile_error": "current profile could over-credit binding capex as immediate Stage2-Actionable without utilization timing."}
{"row_type": "trigger", "case_id": "C13-L191-002", "ticker": "373220", "company_name": "LG에너지솔루션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_NAMED_CUSTOMER_CONTRACT_BUT_2025_RAMP_DELAY", "trigger_date": "2023-10-04", "entry_date": "2023-10-05", "entry_price": 467500, "trigger_type": "Stage2-Watch", "classification": "counterexample", "evidence_family": "Toyota 20GWh supply / Michigan dedicated line", "evidence_url": "https://news.lgensol.com/company-news/press-releases/2177/", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 7.17, "MAE_30D_pct": -19.68, "MFE_90D_pct": 7.17, "MAE_90D_pct": -22.57, "MFE_180D_pct": 7.17, "MAE_180D_pct": -31.02, "peak_180D_date": "2023-10-12", "trough_180D_date": "2024-06-28", "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Watch|2023-10-05", "current_profile_error": "customer contract vocabulary should not override ramp timing and sector tape."}
{"row_type": "trigger", "case_id": "C13-L191-003", "ticker": "051910", "company_name": "LG화학", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_PARENT_CATHODE_PLANT_IRA_BRIDGE_BUT_PARENT_SPREAD_DRAG", "trigger_date": "2023-12-20", "entry_date": "2023-12-20", "entry_price": 504000, "trigger_type": "Stage4B-Watch", "classification": "counterexample", "evidence_family": "Tennessee cathode plant / IRA compliance", "evidence_url": "https://www.lgcorp.com/media/release/27138", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 0.0, "MAE_30D_pct": -23.91, "MFE_90D_pct": 3.17, "MAE_90D_pct": -27.38, "MFE_180D_pct": 3.17, "MAE_180D_pct": -47.72, "peak_180D_date": "2024-02-19", "trough_180D_date": "2024-08-05", "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|051910|Stage4B-Watch|2023-12-20", "current_profile_error": "C13 parent/material proxy should require listed-entity earnings bridge, not plant headline alone."}
{"row_type": "trigger", "case_id": "C13-L191-004", "ticker": "096770", "company_name": "SK이노베이션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_BLUEOVAL_SK_DOE_CONDITIONAL_LOAN_LOCALIZATION", "trigger_date": "2023-06-23", "entry_date": "2023-06-23", "entry_price": 182600, "trigger_type": "Stage2-Actionable", "classification": "positive_with_4b_exit_guard", "evidence_family": "BlueOval SK DOE conditional loan / Ford-SK On JV", "evidence_url": "https://askinno.com/global/archives/14766", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 25.68, "MAE_30D_pct": -13.58, "MFE_90D_pct": 25.68, "MAE_90D_pct": -34.23, "MFE_180D_pct": 25.68, "MAE_180D_pct": -41.13, "peak_180D_date": "2023-07-26", "trough_180D_date": "2024-01-23", "calibration_usable": true, "corporate_action_window_status": "clean_180D_window_profile_has_2024-11-20_candidate_outside_180D", "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|096770|Stage2-Actionable|2023-06-23", "current_profile_error": "good bridge was recognized, but MAE asymmetry means staged entry/exit guard should be attached."}
{"row_type": "trigger", "case_id": "C13-L191-005", "ticker": "096770", "company_name": "SK이노베이션", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_LOSS_NARROWING_PRODUCTIVITY_BUT_NOT_PROFIT_CONVERSION", "trigger_date": "2023-07-28", "entry_date": "2023-07-28", "entry_price": 189500, "trigger_type": "Stage4B-Watch", "classification": "counterexample", "evidence_family": "SK On Q2 loss narrowing / new factories productivity", "evidence_url": "https://en.yna.co.kr/view/AEN20230728002051320", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 19.79, "MAE_30D_pct": -12.08, "MFE_90D_pct": 19.79, "MAE_90D_pct": -36.62, "MFE_180D_pct": 19.79, "MAE_180D_pct": -45.86, "peak_180D_date": "2023-08-01", "trough_180D_date": "2024-04-16", "calibration_usable": true, "corporate_action_window_status": "clean_180D_window_profile_has_2024-11-20_candidate_outside_180D", "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|096770|Stage4B-Watch|2023-07-28", "current_profile_error": "loss narrowing should stay watch until ex-credit operating profit or utilization conversion is visible."}
{"row_type": "trigger", "case_id": "C13-L191-006", "ticker": "006400", "company_name": "삼성SDI", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_STARPLUS_SECOND_JV_LONG_DATED_STARTUP", "trigger_date": "2023-07-24", "entry_date": "2023-07-25", "entry_price": 712000, "trigger_type": "Stage2-Watch", "classification": "counterexample", "evidence_family": "Stellantis-Samsung SDI second U.S. JV / 2027 SOP", "evidence_url": "https://www.stellantis.com/en/news/press-releases/2023/july/stellantis-samsung-sdi-announce-plans-to-build-second-starplus-energy-gigafactory-in-the-united-states", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 3.23, "MAE_30D_pct": -18.12, "MFE_90D_pct": 3.23, "MAE_90D_pct": -41.43, "MFE_180D_pct": 3.23, "MAE_180D_pct": -51.97, "peak_180D_date": "2023-07-26", "trough_180D_date": "2024-01-26", "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage2-Watch|2023-07-25", "current_profile_error": "long-dated JV capacity should not receive full near-term Stage2-Actionable credit."}
{"row_type": "trigger", "case_id": "C13-L191-007", "ticker": "006400", "company_name": "삼성SDI", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_AUTO_BATTERY_REVENUE_MARGIN_WITH_EV_TAPE_GUARD", "trigger_date": "2023-10-26", "entry_date": "2023-10-27", "entry_price": 452000, "trigger_type": "Stage2-Actionable", "classification": "positive_with_high_mae_guard", "evidence_family": "Q3 record revenue / automotive battery sales and margin", "evidence_url": "https://news.samsungsdi.com/global/articleView?seq=33", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 15.49, "MAE_30D_pct": -7.74, "MFE_90D_pct": 15.49, "MAE_90D_pct": -24.34, "MFE_180D_pct": 15.49, "MAE_180D_pct": -24.34, "peak_180D_date": "2023-11-06", "trough_180D_date": "2024-01-26", "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage2-Actionable|2023-10-27", "current_profile_error": "needs positive recognition but position-size/high-MAE guard is still necessary."}
{"row_type": "trigger", "case_id": "C13-L191-008", "ticker": "003670", "company_name": "POSCO퓨처엠", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "C13_ULTIUM_CAM_JV_BINDING_SUPPLY_IRA_CHAIN", "trigger_date": "2023-06-02", "entry_date": "2023-06-05", "entry_price": 380000, "trigger_type": "Stage2-Actionable", "classification": "positive_with_4b_exit_guard", "evidence_family": "GM-POSCO Future M Ultium CAM expansion / binding CAM supply", "evidence_url": "https://www.poscofuturem.com/en/pr/view.do?num=695", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 21.05, "MAE_30D_pct": -9.34, "MFE_90D_pct": 82.63, "MAE_90D_pct": -17.5, "MFE_180D_pct": 82.63, "MAE_180D_pct": -39.08, "peak_180D_date": "2023-07-26", "trough_180D_date": "2023-11-01", "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "dedupe_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|003670|Stage2-Actionable|2023-06-05", "current_profile_error": "current profile may catch the positive but can miss event-cap/exit after parabolic MFE."}
{"row_type": "score_simulation", "case_id": "C13-L191-001", "ticker": "373220", "profile_proxy": "e2r_2_2_rolling_calibrated_shadow", "raw_component_score_breakdown": {"eps_fcf": 8, "visibility": 10, "bottleneck": 11, "mispricing": 8, "valuation": 6, "capital": 5, "info": 12}, "shadow_total_score": 60, "expected_stage_after_rule": "Stage2-Watch", "score_return_alignment": "mixed"}
{"row_type": "score_simulation", "case_id": "C13-L191-002", "ticker": "373220", "profile_proxy": "e2r_2_2_rolling_calibrated_shadow", "raw_component_score_breakdown": {"eps_fcf": 8, "visibility": 10, "bottleneck": 11, "mispricing": 8, "valuation": 6, "capital": 5, "info": 12}, "shadow_total_score": 60, "expected_stage_after_rule": "Stage2-Watch", "score_return_alignment": "aligned"}
{"row_type": "score_simulation", "case_id": "C13-L191-003", "ticker": "051910", "profile_proxy": "e2r_2_2_rolling_calibrated_shadow", "raw_component_score_breakdown": {"eps_fcf": 8, "visibility": 10, "bottleneck": 11, "mispricing": 8, "valuation": 6, "capital": 5, "info": 12}, "shadow_total_score": 60, "expected_stage_after_rule": "Stage4B-Watch", "score_return_alignment": "aligned"}
{"row_type": "score_simulation", "case_id": "C13-L191-004", "ticker": "096770", "profile_proxy": "e2r_2_2_rolling_calibrated_shadow", "raw_component_score_breakdown": {"eps_fcf": 16, "visibility": 18, "bottleneck": 14, "mispricing": 10, "valuation": 5, "capital": 6, "info": 10}, "shadow_total_score": 79, "expected_stage_after_rule": "Stage2-Actionable", "score_return_alignment": "aligned"}
{"row_type": "score_simulation", "case_id": "C13-L191-005", "ticker": "096770", "profile_proxy": "e2r_2_2_rolling_calibrated_shadow", "raw_component_score_breakdown": {"eps_fcf": 8, "visibility": 10, "bottleneck": 11, "mispricing": 8, "valuation": 6, "capital": 5, "info": 16}, "shadow_total_score": 64, "expected_stage_after_rule": "Stage4B-Watch", "score_return_alignment": "aligned"}
{"row_type": "score_simulation", "case_id": "C13-L191-006", "ticker": "006400", "profile_proxy": "e2r_2_2_rolling_calibrated_shadow", "raw_component_score_breakdown": {"eps_fcf": 8, "visibility": 10, "bottleneck": 11, "mispricing": 8, "valuation": 6, "capital": 5, "info": 16}, "shadow_total_score": 64, "expected_stage_after_rule": "Stage2-Watch", "score_return_alignment": "aligned"}
{"row_type": "score_simulation", "case_id": "C13-L191-007", "ticker": "006400", "profile_proxy": "e2r_2_2_rolling_calibrated_shadow", "raw_component_score_breakdown": {"eps_fcf": 16, "visibility": 18, "bottleneck": 14, "mispricing": 10, "valuation": 5, "capital": 6, "info": 10}, "shadow_total_score": 79, "expected_stage_after_rule": "Stage2-Actionable", "score_return_alignment": "aligned"}
{"row_type": "score_simulation", "case_id": "C13-L191-008", "ticker": "003670", "profile_proxy": "e2r_2_2_rolling_calibrated_shadow", "raw_component_score_breakdown": {"eps_fcf": 16, "visibility": 18, "bottleneck": 14, "mispricing": 10, "valuation": 5, "capital": 6, "info": 10}, "shadow_total_score": 79, "expected_stage_after_rule": "Stage2-Actionable", "score_return_alignment": "aligned"}
{"row_type": "aggregate", "selected_round": "R3", "selected_loop": 191, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "usable_trigger_row_count": 8, "positive_case_count": 3, "counterexample_count": 5, "stage4b_watch_or_overlay_count": 4, "high_mae_90_count": 6, "mfe90_ge_20_count": 2, "avg_MFE_90D_pct": 20.65, "avg_MAE_90D_pct": -26.47, "current_profile_error_count": 7, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "shadow_weight", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "rule_candidate": "C13_JV_UTILIZATION_AMPC_EX_CREDIT_AND_RAMP_TIMING_GATE_V2", "proposed_scope": "archetype_specific_stage2_required_bridge_and_4b_exit_guard", "do_not_apply_now": true, "evidence_basis_case_ids": ["C13-L191-001", "C13-L191-002", "C13-L191-003", "C13-L191-004", "C13-L191-005", "C13-L191-006", "C13-L191-007", "C13-L191-008"]}
{"row_type": "residual_contribution", "residual_error_found": ["long_dated_jv_capacity_overcredit", "AMPC_or_IRA_headline_without_ex_credit_profit_conversion", "parent_proxy_or_material_proxy_listed_entity_gap", "good_MFE_but_high_MAE_exit_timing"], "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_requires_confirmed_thesis_break"], "existing_axis_weakened": ["hard_4c_should_not_fire_on_capex_delay_or_long_dated_jv_language_alone"]}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working in stock_agent after the research session has ended.
Do not treat this Markdown as an instruction to patch production scoring blindly.
First ingest this file with the existing v12 calibration parser.
Validate filename, metadata, trigger rows, MFE/MAE completeness, evidence URLs, duplicate keys, and corporate-action contamination.
If accepted, consider adding a C13-scoped shadow rule candidate named C13_JV_UTILIZATION_AMPC_EX_CREDIT_AND_RAMP_TIMING_GATE_V2.
The intended behavior is to cap capex-only or long-dated JV headlines at Stage2-Watch unless utilization/ex-AMPC profit/revenue timing/call-off conversion is present.
Positive rows with high MFE and high MAE should be tagged with 4B exit guard rather than clean Green unlock.
Do not modify production scoring unless the batch promotion decision says apply_next_patch.
```

## 11. Residual contribution summary

```text
new_independent_case_count = 8
usable_trigger_row_count = 8
representative_trigger_count = 8
positive_case_count = 3
counterexample_count = 5
current_profile_error_count = 7
high_mae_90_count = 6
MFE90_ge_20_count = 2
avg_MFE_90D_pct = 20.65
avg_MAE_90D_pct = -26.47
```

## 12. Next research state

```text
completed_round = R3
completed_loop = 191
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes = C15_MATERIAL_SPREAD_SUPERCYCLE|C16_STRATEGIC_RESOURCE_POLICY_SUPPLY|C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG|C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
