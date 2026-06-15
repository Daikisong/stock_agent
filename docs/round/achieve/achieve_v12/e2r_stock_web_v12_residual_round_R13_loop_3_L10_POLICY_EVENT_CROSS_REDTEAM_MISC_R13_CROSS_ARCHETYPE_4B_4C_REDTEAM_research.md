# E2R Stock-Web v12 Residual Research — R13 Cross-Archetype 4B/4C RedTeam

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R13
selected_loop: 3
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: CROSS_ARCHETYPE_4B_TOO_EARLY_VS_HARD_4C_LATE_PRICE_PATH_REDTEAM

output_filename: e2r_stock_web_v12_residual_round_R13_loop_3_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_patch_allowed: false
```

---

## 1. Selection rationale

`R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` is selected because the latest no-repeat index still shows all R13 cross-archetype scopes as empty in the committed research registry, while the current local run has already filled:

- `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` as local R13 loop 1.
- `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` as local R13 loop 2.

This run therefore fills the next R13 gap:

```text
selected_canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
selected_round = R13
selected_loop = 3
```

R13 is not a new sector-positive mining pass. It is a cross-archetype checkpoint: compare cases where 4B would have been too early, cases where hard 4C would have been too late, and cases where a drawdown alone must not be confused with a thesis break.

---

## 2. Price source validation

Stock-web manifest snapshot used for this run:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year"
}
```

Validation notes:

```text
- All entry/high/low rows in this MD are from Songdaiki/stock-web calibration shards.
- Price basis is tradable_raw.
- Forward windows are bounded by manifest max_date, not current date.
- No production scoring change is proposed here.
- All rule suggestions are shadow/diagnostic-only.
```

---

## 3. Cross-archetype question

The red-team question:

```text
When should E2R treat a drawdown as local 4B watch,
and when should it escalate to hard 4C thesis break?
```

The key mechanism is simple:

```text
4B = price went too far or evidence needs refresh, but the thesis bridge is not yet broken.
4C = the thesis bridge itself failed: no revenue/margin/cash conversion, no contract-to-delivery bridge,
     no partner economics, or no refreshed evidence after a deep negative path.
```

So price is a symptom. Evidence is the organ. A falling price can be a fever; it becomes 4C only when the underlying bridge has cracked.

---

## 4. Case set

| case_id | symbol | name | origin canonical | red-team role | entry_date | entry_price | core lesson |
|---|---:|---|---|---|---:|---:|---|
| R13_4B_4C_001 | 079550 | LIG넥스원 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 4B too early / not hard 4C | 2024-09-19 | 206500 | signed export/backlog can survive interim drawdown |
| R13_4B_4C_002 | 326030 | SK바이오팜 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 4B too early positive-control | 2024-08-12 | 98800 | commercial revenue bridge can justify holding through valuation fear |
| R13_4B_4C_003 | 051910 | LG화학 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | hard 4C late | 2024-05-20 | 391500 | low MFE + deep MAE + no segment margin bridge should break thesis |
| R13_4B_4C_004 | 170900 | 동아에스티 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | hard 4C late | 2024-10-11 | 76400 | approval label without listed-company economics should break after failed follow-through |

---

## 5. Price-path calculations

### 5.1 R13_4B_4C_001 — 079550 / LIG넥스원 / C03

Non-price context: LIG Nex1 had a named government export contract path. Reuters reported a $2.8B Iraq missile-system export order and prior M-SAM export visibility.

Entry and stock-web path:

```text
entry_date = 2024-09-19
entry_price = 206500

30D high = 259500
30D low  = 205500
90D high = 271500
90D low  = 168800
180D high = 324500
180D low  = 168800

MFE_30D_pct = +25.67
MAE_30D_pct = -0.48
MFE_90D_pct = +31.48
MAE_90D_pct = -18.26
MFE_180D_pct = +57.14
MAE_180D_pct = -18.26
```

Red-team interpretation:

```text
This is not a hard 4C case.
The interim drawdown after a large MFE should be local 4B/watch unless contract/backlog evidence breaks.
If a mechanical 4C fired on the drawdown alone, it would miss the later 180D high.
```

---

### 5.2 R13_4B_4C_002 — 326030 / SK바이오팜 / C23

Non-price context: this is treated as a commercialized-drug positive-control. It is not a mere binary approval label case.

Entry and stock-web path:

```text
entry_date = 2024-08-12
entry_price = 98800

30D high = 119500
30D low  = 93000
90D high = 130000
90D low  = 93000
180D high = 130000
180D low  = 93000

MFE_30D_pct = +20.95
MAE_30D_pct = -5.87
MFE_90D_pct = +31.58
MAE_90D_pct = -5.87
MFE_180D_pct = +31.58
MAE_180D_pct = -5.87
```

Red-team interpretation:

```text
This is a 4B-too-early control.
A valuation or post-run cooling rule should not cap the case unless the commercial bridge deteriorates.
The price path has good MFE/MAE alignment and does not behave like a failed Stage2/Stage3.
```

---

### 5.3 R13_4B_4C_003 — 051910 / LG화학 / C17

Non-price context: Korean petrochemical firms were using cheaper LPG as feedstock in a low-margin, oversupplied environment. That is not enough to make a company-specific rerating bridge. LG Chem also has segment-mix dilution from battery/petrochemical exposure.

Entry and stock-web path:

```text
entry_date = 2024-05-20
entry_price = 391500

30D high = 406500
30D low  = 350000
90D high = 406500
90D low  = 263500
180D high = 406500
180D low  = 208000

MFE_30D_pct = +3.83
MAE_30D_pct = -10.60
MFE_90D_pct = +3.83
MAE_90D_pct = -32.69
MFE_180D_pct = +3.83
MAE_180D_pct = -46.87
```

Red-team interpretation:

```text
This is hard-4C-late evidence.
It has low MFE and deep MAE.
If there is no refreshed segment margin/revision/cash bridge, remaining in 4B/watch is too forgiving.
```

---

### 5.4 R13_4B_4C_004 — 170900 / 동아에스티 / C23

Non-price context: Imuldosa/ustekinumab-srlf approval is a regulatory label, but C23 needs commercialization economics. If partner economics, royalty timing, reimbursement/launch economics, and listed-company cash bridge are not visible, approval alone should not keep the case alive.

Entry and stock-web path:

```text
entry_date = 2024-10-11
entry_price = 76400

30D high = 80700
30D low  = 73100
90D high = 80700
90D low  = 51100
180D high = 80700
180D low  = 40900

MFE_30D_pct = +5.63
MAE_30D_pct = -4.32
MFE_90D_pct = +5.63
MAE_90D_pct = -33.12
MFE_180D_pct = +5.63
MAE_180D_pct = -46.47
```

Red-team interpretation:

```text
This is hard-4C-late evidence.
The approval label did not convert into a company-level price/economics bridge.
By 90D, low MFE + deep MAE should force a hard thesis-break review.
```

---

## 6. JSONL trigger rows

```jsonl
{"row_type":"trigger","case_id":"R13_4B_4C_001","symbol":"079550","name":"LIG넥스원","selected_round":"R13","selected_loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","origin_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"CROSS_ARCHETYPE_4B_TOO_EARLY_VS_HARD_4C_LATE_PRICE_PATH_REDTEAM","trigger_type":"4B","trigger_date":"2024-09-19","entry_date":"2024-09-19","entry_price":206500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":25.67,"MAE_30D_pct":-0.48,"MFE_90D_pct":31.48,"MAE_90D_pct":-18.26,"MFE_180D_pct":57.14,"MAE_180D_pct":-18.26,"profile_verdict_current":"would_risk_local_4B_or_4C_if_price_only","profile_verdict_candidate":"local_4B_watch_only_not_hard_4C_without_export_backlog_break","classification":"positive_control_4B_too_early","calibration_usable":true}
{"row_type":"trigger","case_id":"R13_4B_4C_002","symbol":"326030","name":"SK바이오팜","selected_round":"R13","selected_loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","origin_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CROSS_ARCHETYPE_4B_TOO_EARLY_VS_HARD_4C_LATE_PRICE_PATH_REDTEAM","trigger_type":"4B","trigger_date":"2024-08-12","entry_date":"2024-08-12","entry_price":98800,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":20.95,"MAE_30D_pct":-5.87,"MFE_90D_pct":31.58,"MAE_90D_pct":-5.87,"MFE_180D_pct":31.58,"MAE_180D_pct":-5.87,"profile_verdict_current":"could_overcap_if_valuation_only_4B","profile_verdict_candidate":"do_not_4B_without_commercial_bridge_break","classification":"positive_control_4B_too_early","calibration_usable":true}
{"row_type":"trigger","case_id":"R13_4B_4C_003","symbol":"051910","name":"LG화학","selected_round":"R13","selected_loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","origin_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CROSS_ARCHETYPE_4B_TOO_EARLY_VS_HARD_4C_LATE_PRICE_PATH_REDTEAM","trigger_type":"4C","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":391500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.83,"MAE_30D_pct":-10.60,"MFE_90D_pct":3.83,"MAE_90D_pct":-32.69,"MFE_180D_pct":3.83,"MAE_180D_pct":-46.87,"profile_verdict_current":"would_be_too_lenient_if_only_4B_watch","profile_verdict_candidate":"hard_4C_after_low_MFE_high_MAE_without_segment_margin_bridge","classification":"counterexample_4C_late","calibration_usable":true}
{"row_type":"trigger","case_id":"R13_4B_4C_004","symbol":"170900","name":"동아에스티","selected_round":"R13","selected_loop":3,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","origin_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CROSS_ARCHETYPE_4B_TOO_EARLY_VS_HARD_4C_LATE_PRICE_PATH_REDTEAM","trigger_type":"4C","trigger_date":"2024-10-11","entry_date":"2024-10-11","entry_price":76400,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.63,"MAE_30D_pct":-4.32,"MFE_90D_pct":5.63,"MAE_90D_pct":-33.12,"MFE_180D_pct":5.63,"MAE_180D_pct":-46.47,"profile_verdict_current":"approval_label_may_keep_watch_too_long","profile_verdict_candidate":"hard_4C_after_failed_follow_through_without_partner_economics","classification":"counterexample_4C_late","calibration_usable":true}
```

---

## 7. Score-return alignment

| case_id | return shape | current-profile risk | candidate diagnostic |
|---|---|---|---|
| R13_4B_4C_001 | high MFE, moderate later MAE, later recovery | price-only 4C would be too harsh | local 4B watch only unless export bridge breaks |
| R13_4B_4C_002 | high MFE, low MAE | valuation-only 4B would be too early | keep positive until commercial bridge deteriorates |
| R13_4B_4C_003 | low MFE, deep MAE | 4B/watch too lenient | hard 4C once no margin/cash bridge is refreshed |
| R13_4B_4C_004 | low MFE, deep MAE | approval-label watch too lenient | hard 4C once no partner economics/cash bridge is refreshed |

---

## 8. Shadow rule candidate

### 8.1 Proposed cross-archetype 4B/4C routing rule

```text
if MFE_90D_pct >= +25
and MAE_90D_pct > -25
and non_price_bridge_still_intact == true:
    route = local_4B_watch_only
    block_hard_4C = true
```

```text
if MFE_90D_pct < +10
and MAE_90D_pct <= -25
and refreshed_non_price_bridge == false:
    route = hard_4C_thesis_break_review
```

```text
if MFE_180D_pct >= +25
and later_new_high_after_interim_drawdown == true
and thesis_bridge_unbroken == true:
    classify_prior_price_only_4B_or_4C_as_too_early
```

### 8.2 Cross-archetype escape hatch

```text
if signed_contract_or_commercial_revenue_bridge == true
and drawdown_is_not_accompanied_by_evidence_break:
    do_not_fire_hard_4C_from_price_path_alone
```

### 8.3 Cross-archetype hard-break escalation

```text
if approval_label_or_commodity_label_or_policy_label == true
and no company_specific_revenue_margin_cash_bridge
and MFE_90D_pct < +10
and MAE_90D_pct <= -25:
    force_hard_4C_review
```

---

## 9. Residual contribution summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4

positive_control_count: 2
counterexample_count: 2
current_profile_error_count: 2

loop_contribution_label: cross_archetype_4b_4c_redteam_guardrail_candidate
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true

new_axis_proposed: R13_CROSS_ARCHETYPE_4B_TOO_EARLY_VS_HARD_4C_LATE_ROUTE
existing_axis_strengthened:
  - hard_4c_requires_thesis_break_not_price_only
  - local_4b_watch_allowed_for_high_mfe_intact_bridge
  - low_mfe_high_mae_forces_hard_4c_review_without_bridge_refresh
existing_axis_weakened: null
do_not_propose_new_weight_delta: false
```

---

## 10. Validation scope

```text
valid_for:
- historical calibration
- cross-archetype red-team
- 4B/4C route stress test
- shadow rule candidate planning

not_valid_for:
- live trading
- current candidate discovery
- production scoring patch
- broker execution
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for stock_agent E2R calibration.

Input artifact:
e2r_stock_web_v12_residual_round_R13_loop_3_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Do not treat this MD as a production patch. Parse the JSONL rows and evaluate only as shadow calibration evidence.

Potential candidate axis:
R13_CROSS_ARCHETYPE_4B_TOO_EARLY_VS_HARD_4C_LATE_ROUTE

Candidate logic to test in shadow only:
1. If MFE_90D_pct >= +25, MAE_90D_pct > -25, and non-price thesis bridge remains intact,
   hard 4C should be blocked and local 4B watch should be preferred.
2. If MFE_90D_pct < +10, MAE_90D_pct <= -25, and no refreshed non-price bridge exists,
   hard 4C review should be forced.
3. If later new high occurs after interim drawdown and thesis bridge remained intact,
   prior price-only 4B/4C should be marked too early.

Do not patch production scoring until this axis is validated against larger R13 cross-archetype evidence.
```

---

## 12. Next research state

```text
completed_round = R13
completed_loop = 3
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

