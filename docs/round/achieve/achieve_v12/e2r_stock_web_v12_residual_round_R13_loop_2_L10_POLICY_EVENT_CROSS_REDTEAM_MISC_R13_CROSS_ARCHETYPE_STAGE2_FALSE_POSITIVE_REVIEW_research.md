# E2R Stock-Web v12 Residual Research — R13 Cross-Archetype Stage2 False-Positive Review

```text
schema_family = v12_sector_archetype_residual
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R13_loop_2_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md

selected_round = R13
selected_loop = 2
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id = CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_WITH_POSITIVE_CONTROL
loop_objective = cross_archetype_false_positive_review | stage2_actionable_bonus_stress_test | low_MFE_high_MAE_guardrail | positive_control_contrast

production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
handoff_prompt_executed_now = false
```

---

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still shows all R13 cross-archetype scopes at zero rows in the repository baseline. The previous local R13 pass filled `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` at loop 1, so this pass uses the next R13 scope: `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW`.

This is not a new sector-positive search. The purpose is to compare Stage2-looking signals across different canonical archetypes and isolate cases where the historical price path says: “the label was present, but the business bridge was not ready.”

R13 special-scope rules applied:

```text
selected_round = R13
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
no individual sector naming in output filename
no production patch
no stock_agent source code access
```

---

## 2. Price source validation

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

All selected cases use post-corporate-action-safe windows for the specific trigger interval used here. No forward price is created beyond `stock_web_manifest_max_date`.

---

## 3. Cross-case thesis

The repeated failure pattern is:

```text
Stage2-looking label exists
but company-specific bridge is missing or too indirect
and forward path shows either:
  - MFE_90D < +10% with MAE_90D <= -25%, or
  - MFE_180D < +10% with MAE_180D <= -30%, or
  - early MFE is not large enough to pay for the downside path
```

This is different from the prior high-MAE R13 pass. The prior pass focused on “large MFE but also deep MAE.” This pass focuses on **Stage2 false positives where upside never became meaningful enough**, or where a label was confused for a business bridge.

---

## 4. Case table

| case_id | source canonical | symbol | name | trigger label | verdict | failure / control mechanism |
|---|---:|---:|---|---|---|---|
| R13_FP_LGCHEM_C17_20240520 | C17 | 051910 | LG화학 | Stage2 | false_positive | petrochemical feedstock/substitution headline without segment-level margin/revision bridge |
| R13_FP_DONGAST_C23_20241011 | C23 | 170900 | 동아에스티 | Stage2 | false_positive | biosimilar approval label without direct listed-company revenue/royalty timing bridge |
| R13_FP_HYOSUNGCHEM_C17_20240520 | C17 | 298000 | 효성화학 | Stage2 | false_positive | chemical/PP spread label with balance-sheet/cash drag and low forward MFE |
| R13_PC_SKBIOPHARM_C23_20240812 | C23 | 326030 | SK바이오팜 | Stage2 | positive_control | commercialization/sales bridge with low early MAE and aligned forward MFE |

---

## 5. Historical price-path metrics

Metrics are calculated from actual 1D stock-web OHLC rows. Values are percent from entry close.

| case_id | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | path verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R13_FP_LGCHEM_C17_20240520 | 2024-05-20 | 391500 | 3.83 | -14.05 | 3.83 | -32.69 | 3.83 | -46.87 | low-MFE / high-MAE false positive |
| R13_FP_DONGAST_C23_20241011 | 2024-10-11 | 76400 | 5.63 | -20.16 | 5.63 | -36.32 | 5.63 | -46.47 | approval-label false positive |
| R13_FP_HYOSUNGCHEM_C17_20240520 | 2024-05-20 | 71000 | 9.01 | -16.20 | 9.01 | -22.39 | 9.01 | -60.35 | spread-label high-MAE false positive |
| R13_PC_SKBIOPHARM_C23_20240812 | 2024-08-12 | 98800 | 20.95 | -5.87 | 31.58 | -5.87 | 31.58 | -5.87 | positive control |

Interpretation:

- `LG화학` and `동아에스티` are the cleanest Stage2 false-positive guards: MFE never reached +10% but 90D/180D MAE was large.
- `효성화학` is a slightly different false positive: MFE was near +9%, but not enough to compensate for balance-sheet/path damage.
- `SK바이오팜` is the positive-control anchor: MFE/MAE alignment shows why the rule should not simply block all biotech or approval-linked Stage2 cases.

---

## 6. Trigger rows JSONL

```jsonl
{"schema_family":"v12_sector_archetype_residual","selected_round":"R13","selected_loop":2,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_WITH_POSITIVE_CONTROL","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","case_id":"R13_FP_LGCHEM_C17_20240520","symbol":"051910","company_name":"LG화학","trigger_type":"Stage2","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":391500,"MFE_30D_pct":3.83,"MAE_30D_pct":-14.05,"MFE_90D_pct":3.83,"MAE_90D_pct":-32.69,"MFE_180D_pct":3.83,"MAE_180D_pct":-46.87,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_family":"petrochemical_feedstock_substitution_headline_without_segment_margin_revision_bridge","profile_verdict_current":"Stage2_actionable_too_permissive","profile_verdict_proposed":"Stage2_false_positive_block","calibration_usable":true,"row_role":"counterexample","residual_type":"low_mfe_high_mae_false_positive"}
{"schema_family":"v12_sector_archetype_residual","selected_round":"R13","selected_loop":2,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_WITH_POSITIVE_CONTROL","source_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","case_id":"R13_FP_DONGAST_C23_20241011","symbol":"170900","company_name":"동아에스티","trigger_type":"Stage2","trigger_date":"2024-10-11","entry_date":"2024-10-11","entry_price":76400,"MFE_30D_pct":5.63,"MAE_30D_pct":-20.16,"MFE_90D_pct":5.63,"MAE_90D_pct":-36.32,"MFE_180D_pct":5.63,"MAE_180D_pct":-46.47,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_family":"biosimilar_approval_label_without_direct_revenue_royalty_timing_bridge","profile_verdict_current":"Stage2_actionable_too_permissive","profile_verdict_proposed":"Stage2_false_positive_block","calibration_usable":true,"row_role":"counterexample","residual_type":"approval_label_low_mfe_high_mae_false_positive"}
{"schema_family":"v12_sector_archetype_residual","selected_round":"R13","selected_loop":2,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_WITH_POSITIVE_CONTROL","source_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","case_id":"R13_FP_HYOSUNGCHEM_C17_20240520","symbol":"298000","company_name":"효성화학","trigger_type":"Stage2","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":71000,"MFE_30D_pct":9.01,"MAE_30D_pct":-16.20,"MFE_90D_pct":9.01,"MAE_90D_pct":-22.39,"MFE_180D_pct":9.01,"MAE_180D_pct":-60.35,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_family":"chemical_spread_label_without_cash_balance_sheet_repair","profile_verdict_current":"Stage2_actionable_too_permissive","profile_verdict_proposed":"Stage2_false_positive_block_or_positive_contribution_cap","calibration_usable":true,"row_role":"counterexample","residual_type":"low_forward_mfe_extreme_mae_false_positive"}
{"schema_family":"v12_sector_archetype_residual","selected_round":"R13","selected_loop":2,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_WITH_POSITIVE_CONTROL","source_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","case_id":"R13_PC_SKBIOPHARM_C23_20240812","symbol":"326030","company_name":"SK바이오팜","trigger_type":"Stage2","trigger_date":"2024-08-12","entry_date":"2024-08-12","entry_price":98800,"MFE_30D_pct":20.95,"MAE_30D_pct":-5.87,"MFE_90D_pct":31.58,"MAE_90D_pct":-5.87,"MFE_180D_pct":31.58,"MAE_180D_pct":-5.87,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","evidence_family":"approved_drug_commercialization_sales_bridge","profile_verdict_current":"Stage2_actionable_supported","profile_verdict_proposed":"positive_control_keep_stage2_possible","calibration_usable":true,"row_role":"positive_control","residual_type":"stage2_true_positive_control"}
```

---

## 7. Current calibrated profile stress test

### 7.1 Failure mode

If Stage2 scoring gives too much credit to:

```text
sector label + policy/regulatory/industry headline + one-day price reaction
```

without requiring a company-specific bridge, three distinct source archetypes can be misclassified:

```text
C17 chemical / commodity spread:
  - LG화학
  - 효성화학

C23 bio regulatory approval:
  - 동아에스티
```

The common problem is not sector-specific. It is a cross-archetype Stage2 compression problem.

### 7.2 Positive-control contrast

`SK바이오팜` should not be blocked by a simple “bio label” penalty. The positive-control row shows:

```text
MFE_30D >= +20%
MAE_30D > -10%
MFE_90D >= +30%
MAE_90D > -10%
```

So the shadow rule should be conditional, not blanket.

---

## 8. Proposed shadow guardrail

```text
rule_id = R13_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_GUARD
scope = cross_archetype
production_scoring_changed = false
shadow_weight_only = true
```

### 8.1 Hard false-positive block

```text
if trigger_type == Stage2
and MFE_90D_pct < +10
and MAE_90D_pct <= -25
and no company_specific_revenue_margin_cash_bridge:
    profile_verdict_proposed = Stage2_FalsePositive_Block
```

### 8.2 Positive contribution cap

```text
if trigger_type == Stage2
and MFE_180D_pct < +10
and MAE_180D_pct <= -30
and evidence_family is label_or_indirect_bridge:
    positive_contribution_cap = 0
    local_4B_watch = true
```

### 8.3 Positive-control escape hatch

```text
if MFE_30D_pct >= +15
and MAE_30D_pct > -10
and company_specific_revenue_margin_cash_bridge == true:
    do_not_apply_false_positive_block
```

This escape hatch is necessary to avoid over-penalizing true Stage2 cases that already have a clean price/evidence alignment.

---

## 9. Raw component score breakdown — shadow-only

| component | LG화학 | 동아에스티 | 효성화학 | SK바이오팜 |
|---|---:|---:|---:|---:|
| label / headline score | 14 | 18 | 14 | 16 |
| company-specific cash bridge | 2 | 3 | 1 | 18 |
| margin / revenue revision bridge | 2 | 2 | 1 | 17 |
| balance-sheet / dilution risk adjustment | -8 | -3 | -12 | 0 |
| price-path alignment | -18 | -20 | -22 | 16 |
| high-MAE penalty | -16 | -16 | -22 | 0 |
| proposed net shadow contribution | -24 | -16 | -40 | 67 |

The exact production score is not changed. This table is a shadow diagnostic for later batch calibration review.

---

## 10. 4B local vs full-window proximity

| case_id | local 4B watch | full-window 4C candidate | reason |
|---|---:|---:|---|
| R13_FP_LGCHEM_C17_20240520 | yes | no | low MFE plus large MAE; not an accounting break, but Stage2 should be blocked |
| R13_FP_DONGAST_C23_20241011 | yes | no | approval label did not convert to listed-company economics |
| R13_FP_HYOSUNGCHEM_C17_20240520 | yes | possible if balance-sheet stress persists | MAE extreme and MFE insufficient |
| R13_PC_SKBIOPHARM_C23_20240812 | no | no | positive-control path alignment |

---

## 11. Residual contribution summary

```text
new_independent_case_count = 4
reused_case_count = 0
same_cross_scope_new_source_archetype_count = 2
same_cross_scope_new_trigger_family_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4

positive_control_count = 1
counterexample_count = 3
current_profile_error_count = 3

sector_specific_rule_candidate = false
canonical_archetype_rule_candidate = false
cross_archetype_rule_candidate = true

loop_contribution_label = cross_archetype_stage2_false_positive_guardrail_candidate

new_axis_proposed = R13_STAGE2_FALSE_POSITIVE_LOW_MFE_HIGH_MAE_GUARD
existing_axis_strengthened = stage2_required_non_price_bridge; high_MAE_guard; price_path_alignment_check
existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

---

## 12. Deferred Coding Agent Handoff Prompt

Do not execute this in the research session.

```text
You are the deferred coding agent for stock_agent E2R calibration.

Input artifact:
- e2r_stock_web_v12_residual_round_R13_loop_2_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md

Task:
1. Parse the JSONL trigger rows.
2. Validate complete MFE/MAE fields.
3. Deduplicate by symbol + trigger_type + entry_date + source_canonical_archetype_id + evidence_family.
4. Treat the proposed rule as shadow-only unless multiple R13 runs confirm it.
5. Do not lower Stage3-Green thresholds.
6. Do not convert this single MD into a production patch.
7. Aggregate this with R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL and future R13 cross-checkpoints.
8. Candidate guardrail to test:
   - Stage2 low-MFE/high-MAE false-positive block
   - positive-control escape hatch when MFE_30D >= +15%, MAE_30D > -10%, and company-specific bridge exists.
```

---

## 13. Required next research state

```text
completed_round = R13
completed_loop = 2
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```
