# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R7
selected_loop: 138
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: APPROVAL_TO_COMMERCIAL_REVENUE_PROFIT_BRIDGE_VS_APPROVAL_LABEL_WITHOUT_LISTED_COMPANY_ECONOMICS
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` remains a Priority 0 archetype in the no-repeat index: 12 representative rows, still 18 rows short of the 30-row minimum. The visible covered set is concentrated in `195940`, `145020`, `000100`, `009420`, `067630`, and `068270`, so this run uses less-covered current-session C23 rows and converts the recent R13 accounting-trust guardrail into a sector-specific C23 rule candidate.

The previous local C23 sector pass reached loop 137. This run continues as `R7/C23 loop 138`.

Direct stock-web file fetch for uncached shards was unstable in recent turns, so this MD uses stock-web-derived rows already computed in the current v12 session. The rows contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable 1D OHLC. No production scoring is changed.

---

## 1. Research thesis

C23 is not `approval headline = successful bio trigger`. It is the bridge:

```text
regulatory approval / label expansion / commercialization event
→ launch, prescriptions, reimbursement, royalty, partner economics, sales cadence, margin or profit
→ price path validation
```

This loop separates three routes:

1. **Approved commercial drug with visible revenue/profit bridge**
   - Approval has already become prescriptions, sales, or profit contribution.
   - Stage2 can remain open and can approach Stage3-Yellow when price confirms with controlled MAE.

2. **FDA approval to launch bridge**
   - The approval itself is real.
   - Stage2 may open, but Green must wait for launch revenue cadence, channel uptake, reimbursement, and margin evidence.

3. **Approval label without listed-company economics**
   - The regulatory event may be real, but the listed company may not yet capture launch economics.
   - If partner economics, royalty timing, reimbursement, or direct sales bridge is unclear and price rejects the event, Stage2 must be blocked.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - e2r_stock_web_v12_residual_round_R13_loop_9_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_8_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_6_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current run formalizes the sector-specific C23 rule after R13 gate checks
  - duplicate keys should be treated as reused controls if already present in C23 loop 137
  - no production scoring changed
```

Symbol caveats:

```yaml
326030:
  name: SK바이오팜
  role: approved commercialized drug revenue/profit bridge
  calibration_usable: true

006280:
  name: 녹십자
  role: FDA approval to US launch bridge
  calibration_usable: true

170900:
  name: 동아에스티
  role: biosimilar approval label without visible listed-company economics
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R7","loop":138,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"APPROVED_DRUG_COMMERCIAL_REVENUE_PROFIT_BRIDGE_POSITIVE_CONTROL","symbol":"326030","name":"SK바이오팜","trigger_type":"Stage2-Actionable","entry_date":"2024-08-12","entry_close":98800,"price_basis":"tradable_raw","mfe_30d_pct":20.95,"mae_30d_pct":-5.87,"mfe_90d_pct":31.58,"mae_90d_pct":-5.87,"mfe_180d_pct":31.58,"mae_180d_pct":-5.87,"forward_high_30d":119500,"forward_low_30d":93000,"forward_high_90d":130000,"forward_low_90d":93000,"forward_high_180d":130000,"forward_low_180d":93000,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|326030|Stage2-Actionable|2024-08-12","non_price_bridge":"approved-drug commercialization with visible sales/profit bridge","score_alignment":"keep Stage2-Actionable; allow Stage3-Yellow path when revenue/profit bridge remains refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R7","loop":138,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"FDA_APPROVAL_TO_US_LAUNCH_BRIDGE_LOCAL_4B_UNTIL_REVENUE_CADENCE","symbol":"006280","name":"녹십자","trigger_type":"Stage2-Actionable","entry_date":"2024-07-09","entry_close":124900,"price_basis":"tradable_raw","mfe_30d_pct":33.71,"mae_30d_pct":-4.56,"mfe_90d_pct":45.56,"mae_90d_pct":-4.56,"mfe_180d_pct":45.56,"mae_180d_pct":-10.49,"forward_high_30d":167000,"forward_low_30d":119200,"forward_high_90d":181800,"forward_low_90d":119200,"forward_high_180d":181800,"forward_low_180d":111800,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|006280|Stage2-Actionable|2024-07-09","non_price_bridge":"FDA approval and US launch path, but launch revenue cadence still needed","score_alignment":"Stage2 opens; block Stage3-Green until quarterly launch revenue, channel uptake and margin evidence confirm"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R7","loop":138,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOSIMILAR_APPROVAL_LABEL_WITHOUT_LISTED_COMPANY_ECONOMICS_FALSE_POSITIVE","symbol":"170900","name":"동아에스티","trigger_type":"Stage2-FalsePositive","entry_date":"2024-10-11","entry_close":76400,"price_basis":"tradable_raw","mfe_30d_pct":5.63,"mae_30d_pct":-20.16,"mfe_90d_pct":5.63,"mae_90d_pct":-36.32,"mfe_180d_pct":5.63,"mae_180d_pct":-46.47,"forward_high_30d":80700,"forward_low_30d":61000,"forward_high_90d":80700,"forward_low_90d":48650,"forward_high_180d":80700,"forward_low_180d":40900,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|170900|Stage2-FalsePositive|2024-10-11","non_price_bridge":"biosimilar approval label without visible direct sales, royalty, launch timing or listed-company margin bridge","score_alignment":"block Stage2-Actionable; require listed-company economics before reopen"}
```

---

## 4. Case analysis

### 4.1 SK Biopharm / 326030 — approval has already become commercial economics

SK Biopharm is the C23 positive-control. The important point is not merely that a drug is approved. The bridge is that commercialization is already visible enough to be traced into sales and profit expectations.

```yaml
entry_date: 2024-08-12
entry_close: 98800
30d_high: 119500
30d_low: 93000
90d_high: 130000
90d_low: 93000
180d_high: 130000
180d_low: 93000
mfe_90d_pct: 31.58
mae_90d_pct: -5.87
```

Interpretation:

```text
classification = Stage2-Actionable positive-control
```

The model should preserve Stage2 when the approval-to-revenue bridge is already visible and the price path confirms with shallow MAE.

---

### 4.2 Green Cross / 006280 — approval-to-launch is valid, but not yet Green

Green Cross is the correct positive-with-4B case. FDA approval is a strong bridge, but C23 should not treat approval itself as the final cash bridge before launch revenue cadence appears.

```yaml
entry_date: 2024-07-09
entry_close: 124900
30d_high: 167000
30d_low: 119200
90d_high: 181800
90d_low: 119200
180d_high: 181800
180d_low: 111800
mfe_90d_pct: 45.56
mae_180d_pct: -10.49
```

Interpretation:

```text
classification = Stage2-Actionable with local_4B_watch
```

Approval is the passport. Commercialization is the paycheck. C23 Stage3-Green should wait for launch revenue, reimbursement/channel uptake, and margin confirmation.

---

### 4.3 Dong-A ST / 170900 — approval label failed as accounting bridge

Dong-A ST is the hard counterexample. The approval-related label did not translate into visible listed-company economics inside the validation window.

```yaml
entry_date: 2024-10-11
entry_close: 76400
30d_high: 80700
30d_low: 61000
90d_high: 80700
90d_low: 48650
180d_high: 80700
180d_low: 40900
mfe_90d_pct: 5.63
mae_90d_pct: -36.32
```

Interpretation:

```text
classification = Stage2-FalsePositive
```

This is the guardrail. A regulatory event can be real, but Stage2 must ask whether the listed company captures economics through launch, royalty, reimbursement, market access, or margin.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
local_4B_watch_count: 1
current_profile_error_count: 2
duplicate_note: if C23 loop 137 already contains any identical novelty_key, treat that row as reused control rather than new aggregate credit
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 326030 | positive-control | +20.95 / -5.87 | +31.58 / -5.87 | +31.58 / -5.87 | commercialized-drug bridge validates Stage2 |
| 006280 | positive + 4B | +33.71 / -4.56 | +45.56 / -4.56 | +45.56 / -10.49 | approval-to-launch bridge needs revenue cadence |
| 170900 | hard counterexample | +5.63 / -20.16 | +5.63 / -36.32 | +5.63 / -46.47 | approval label without listed-company economics fails |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"326030","raw_regulatory_event":3,"raw_commercial_revenue_bridge":5,"raw_reimbursement_market_access":3,"raw_royalty_or_direct_sales":4,"raw_margin_profit_bridge":4,"raw_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"006280","raw_regulatory_event":5,"raw_commercial_revenue_bridge":3,"raw_reimbursement_market_access":3,"raw_royalty_or_direct_sales":3,"raw_margin_profit_bridge":2,"raw_validation":4,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-local-4B-watch"}
{"row_type":"score_simulation","symbol":"170900","raw_regulatory_event":4,"raw_commercial_revenue_bridge":1,"raw_reimbursement_market_access":1,"raw_royalty_or_direct_sales":1,"raw_margin_profit_bridge":1,"raw_validation":0,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-approval-label"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C23 can over-credit:

```text
approval headline
+ biosimilar/new-drug label
+ short-window attention
```

That is too broad. The accounting bridge should be explicit:

```text
approval -> launch -> reimbursement / market access -> prescription or order -> revenue / royalty -> margin/profit
```

Without the later links, approval is a key that has not yet opened the register.

### Rule candidate

```text
C23_APPROVAL_TO_COMMERCIAL_ECONOMICS_REQUIREMENT_V138

if C23
and regulatory_approval_or_label_expansion == true
and listed_company_launch_revenue_reimbursement_royalty_or_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C23
and approved_drug_commercialization_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C23
and FDA_approval_to_launch_bridge == true
and MFE_30D_pct >= +30
and quarterly_launch_revenue_cadence == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C23
and approval_label_only == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
    require_new_evidence_family_before_reopen = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C23_APPROVAL_TO_COMMERCIAL_ECONOMICS_REQUIREMENT_V138
existing_axis_strengthened:
  - C23_approval_label_not_enough_without_commercial_bridge
  - C23_commercialized_drug_positive_escape_hatch
  - C23_FDA_approval_launch_bridge_local_4B_until_revenue_cadence
  - C23_biosimilar_partner_economics_delay_stage2_block
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C23 loop with C23 loop 137 and adjacent R13 bio/device accounting-trust, Stage2 false-positive and high-MAE guardrail files. Extract `C23_APPROVAL_TO_COMMERCIAL_ECONOMICS_REQUIREMENT_V138` as a shadow-rule candidate. Preserve commercialized-drug and FDA-approval-to-launch escape hatches, but block approval-label-only cases without listed-company revenue, reimbursement, royalty, launch cadence, margin or profit bridge.
```

---

## 10. Next research state

```yaml
completed_round: R7
completed_loop: 138
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_battery_and_grid_policy_controls
```
