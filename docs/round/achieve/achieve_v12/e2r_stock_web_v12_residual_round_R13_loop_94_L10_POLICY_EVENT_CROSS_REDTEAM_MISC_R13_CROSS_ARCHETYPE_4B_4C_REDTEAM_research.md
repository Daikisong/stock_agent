# E2R Stock-Web v12 Residual Research — R13 / Loop 94

```yaml
scheduled_round: R13
scheduled_loop: 94
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: PF_GOVERNANCE_EDUCATION_POLICY_EXECUTION_BRIDGE_REDTEAM

research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

review_trigger_count: 9
reviewed_original_canonical_count: 3
reviewed_original_canonical_ids:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
reviewed_fine_branch_count: 3
reviewed_fine_branches:
  - SMALL_REGIONAL_CIVIL_BUILDER_POLICY_RELIEF_PF_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_THEME_SPIKE
  - CONTROL_TRANSFER_SALE_PROCESS_ACTIVIST_GOVERNANCE_PREMIUM_CAP_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE
  - EDUCATION_POLICY_ENROLLMENT_CONTENT_REORDER_MARGIN_BRIDGE_VS_EDUCATION_LABEL_SPIKE

new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

positive_control_count: 4
capped_positive_or_bridge_positive_count: 4
local_burst_or_4b_watch_count: 4
watch_yellow_cap_count: 2
stage2_false_positive_or_high_mae_count: 5
hard_4c_candidate_count: 3
accounting_or_listing_trust_caveat_count: 1
corporate_action_caveat_avoided_count: 1
policy_governance_trust_bridge_case_count: 9
construction_pf_case_count: 3
governance_control_case_count: 3
education_policy_service_case_count: 3
calibration_usable_review_count: 9

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 94
next_round: R1
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_94_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 94
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a normal sector-specific expansion round. It is the cross-archetype checkpoint for:

```text
false positive
high MAE
4B too early / too late
4C late
accounting / listing / tradeability trust
price validation
policy label vs company-specific execution bridge
control premium cap
education policy monetization
construction PF trust
```

After this file:

```text
next_round = R1
next_loop = 95
```

---

## 2. Source set reviewed

This R13 review does not add new independent cases. It reviews the nine cases produced in loop94 R10~R12:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 001260 남광토건
  - 010960 삼호개발
  - 001840 이화공영

R11 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - 003920 남양유업
  - 001750 한양증권
  - 003240 태광산업

R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 096240 크레버스
  - 072870 메가스터디
  - 095720 웅진씽크빅
```

No-repeat handling:

```text
row_type = review_case
new_independent_case_count = 0
do_not_count_as_new_case_count = 9
independent_evidence_weight_total = 0.0
```

The original R10/R11/R12 rows remain the usable calibration cases. This R13 file only validates cross-archetype guardrails and links the original cases into a shared failure grammar.

---

## 3. Cross-archetype question

The same structural error appears across three event families:

```text
C30 small/regional/civil builder:
  construction policy or theme salience exists,
  but equity value depends on PF exposure, project cash, receivables, backlog, margin, and trust.

C32 governance/control premium:
  governance salience, control-transfer hope, or sale-process optionality exists,
  but equity value depends on identifiable buyer, transaction price, closing path, minority-holder economics, and corporate-action cutoff.

C31 education policy/service:
  education policy, exam cycle, or edtech salience exists,
  but equity value depends on paid enrollment, renewal, ARPU, retention, cost control, and margin.
```

Shared false-positive mechanism:

```text
external policy / governance / service salience
  -> recognizable sector label becomes hot
  -> price reacts first
  -> model over-promotes label to Stage2-Actionable / Stage3-Green
  -> company-specific economic bridge is missing or stale
  -> shallow MFE, high MAE, Watch cap, local 4B, or hard 4C follows
```

Shared guardrail:

```text
The event rings the bell.
C30 asks whether financing, receivables, and project cash can hold the building.
C32 asks whether the key fits the control gate and whether minority holders can exit at the printed price.
C31 education asks whether the bell puts paid students in seats and margin in the ledger.
```

---

## 4. Reviewed case matrix

| Original canonical | Symbol | Name | Entry | MFE | MAE | R13 verdict |
|---|---:|---|---:|---:|---:|---|
| C30 | 001260 | 남광토건 | 6,950 | +23.0% | -14.4% | capped civil/regional construction positive; PF/cash-flow trust required |
| C30 | 010960 | 삼호개발 | 3,650 | +0.0% | -15.3% | Watch/Yellow cap; civil-construction label without project cash bridge |
| C30 | 001840 | 이화공영 | 3,765 | +6.2% | -38.9% | hard 4C; small construction late spike with row/trust caveat |
| C32 | 003920 | 남양유업 | 620,000 | +16.1% | -25.0% | capped control-transfer positive with 4B and corporate-action cutoff |
| C32 | 001750 | 한양증권 | 16,000 | +21.3% | -23.9% | sale-process local positive; 4B until final buyer/price/closing |
| C32 | 003240 | 태광산업 | 943,000 | +0.7% | -45.9% | hard 4C; asset-rich governance label without executable monetization |
| C31 | 096240 | 크레버스 | 16,550 | +17.5% | -11.1% | premium education capped positive; paid enrollment/margin bridge required |
| C31 | 072870 | 메가스터디 | 10,990 | +5.5% | -3.5% | Watch/Yellow cap; stable education brand without incremental paid demand |
| C31 | 095720 | 웅진씽크빅 | 2,525 | +10.1% | -35.0% | hard 4C; edtech policy label without paid enrollment/margin bridge |

---

## 5. R10 review — construction PF, cash flow, and trust

### 5.1 001260 남광토건

```text
entry_close: 6,950
peak_high: 8,550
MFE: +23.0%
worst_low_after_entry: 5,950
MAE: -14.4%
```

R13 interpretation:

```text
This is the constructive C30 case in the loop94 holdout set.
The move had enough post-trigger MFE to preserve a capped positive.
The drawdown was material but did not reach hard-4C territory.
```

Classification:

```text
positive_control = true
capped_positive = true
local_4b_after_theme_mfe = true
pf_cashflow_trust_bridge_required_for_green = true
```

This is the "construction relief can work" case, but not a Green case. The model still needs project cash, PF exposure reduction, backlog quality, and margin trust.

### 5.2 010960 삼호개발

```text
entry_close: 3,650
peak_high_after_entry: 3,650
MFE: +0.0%
worst_low_after_entry: 3,090
MAE: -15.3%
```

R13 interpretation:

```text
This is the stable civil-construction cap.
The label was relevant, but there was no post-trigger upside.
```

Classification:

```text
watch_yellow_cap = true
actionable_block_without_project_cashflow_bridge = true
```

The lesson is that a calm civil-construction label is not evidence of balance-sheet repair. Controlled MAE alone is not enough to open Actionable if MFE and company bridge are absent.

### 5.3 001840 이화공영

```text
entry_close: 3,765
peak_high_after_entry: 4,000
MFE: +6.2%
worst_low_after_entry: 2,300
MAE: -38.9%
```

R13 interpretation:

```text
This is the hard C30 failure.
The stock behaved like a small-builder policy/theme spike rather than a PF/cash-flow repair event.
```

Classification:

```text
hard_4c_candidate = true
small_builder_late_spike_guard = true
row_presence_or_tradeability_caveat = true
stage2_actionable_block = true
```

The model should not confuse construction theme heat with project-level trust.

---

## 6. R11 review — governance, control premium, sale process, and minority economics

### 6.1 003920 남양유업

```text
entry_close: 620,000
peak_high_before_corporate_action_candidate: 720,000
MFE: +16.1%
worst_low_before_corporate_action_candidate: 465,000
MAE: -25.0%
corporate_action_candidate_cutoff: 2024-11-20
```

R13 interpretation:

```text
This is the constructive C32 control-transfer case, but only with a cap.
Control-transfer premium exists, but the path included large interim MAE.
Post-2024-11-20 rows must be blocked due to corporate-action candidate.
```

Classification:

```text
positive_control = true
local_4b_overlay = true
corporate_action_caveat_avoided = true
control_transfer_cap_required = true
```

The lesson is that C32 positives can be valid even with volatility, but they must be capped by deal economics and corporate-action cutoffs.

### 6.2 001750 한양증권

```text
entry_close: 16,000
peak_high: 19,410
MFE: +21.3%
worst_low_after_entry: 12,180
MAE: -23.9%
```

R13 interpretation:

```text
This is a sale-process local positive.
The trade worked first, but later drawdown proves that final buyer, price, and closing evidence are needed before Green.
```

Classification:

```text
positive_control = true
local_4b_overlay = true
sale_process_price_closing_bridge_required = true
```

The model should hold it as local 4B until final tender/sale price and closing probability are explicit.

### 6.3 003240 태광산업

```text
entry_close: 943,000
peak_high: 950,000
MFE: +0.7%
worst_low_after_entry: 510,000
MAE: -45.9%
```

R13 interpretation:

```text
This is the governance/asset-rich false positive.
The label was strong, but executable monetization was absent.
```

Classification:

```text
hard_4c_candidate = true
asset_rich_governance_label_false_positive = true
green_block_without_tender_sale_or_return_bridge = true
```

The lesson is that governance salience without a buyer, tender, asset sale, buyback, or enforceable shareholder-return mechanism should not be promoted.

---

## 7. R12 review — education policy, paid enrollment, and service margin

### 7.1 096240 크레버스

```text
entry_close: 16,550
peak_high: 19,450
MFE: +17.5%
worst_low_after_entry: 14,720
MAE: -11.1%
```

R13 interpretation:

```text
This is the constructive education-service case.
Premium content and recurring enrollment plausibly worked, but the bridge needs refreshed retention and margin evidence.
```

Classification:

```text
positive_control = true
capped_positive = true
local_4b_after_rerating = true
paid_enrollment_margin_bridge_required = true
```

This is not a blanket education-policy Green. It is a capped positive that needs renewed paid-demand proof.

### 7.2 072870 메가스터디

```text
entry_close: 10,990
peak_high: 11,590
MFE: +5.5%
worst_low_after_entry: 10,600
MAE: -3.5%
```

R13 interpretation:

```text
This is a stable education-brand Watch cap.
MAE was controlled, but MFE was shallow and incremental paid-demand evidence was weak.
```

Classification:

```text
watch_yellow_cap = true
green_block_without_incremental_enrollment = true
```

The lesson is that a stable brand is not the same as policy monetization.

### 7.3 095720 웅진씽크빅

```text
entry_close: 2,525
peak_high: 2,780
MFE: +10.1%
worst_low_after_entry: 1,640
MAE: -35.0%
```

R13 interpretation:

```text
This is the hard education-policy failure.
Children-learning / edtech salience did not become paid enrollment, renewal, ARPU, or margin.
```

Classification:

```text
hard_4c_candidate = true
edtech_label_false_positive = true
paid_enrollment_margin_bridge_missing = true
```

The model must not promote education-policy salience when the economics do not reach paid enrollment and margin.

---

## 8. Cross-archetype guardrail

### Proposed R13 cross-rule

```text
R13_EVENT_LABEL_TO_EXECUTION_BRIDGE_REQUIRED

For policy/event/governance/service archetypes across construction, governance, and education:

  Do not open Stage2-Actionable or Stage3-Green from event salience or sector label alone.

  First classify the event type:
    - C30 balance-sheet / PF / project-cash trust event
    - C32 governance / control-premium / sale-process event
    - C31 education policy / service monetization event

  Then require the matching bridge:
    - C30: PF exposure, project cash, receivables, backlog, funding, cost/margin, tradeability trust
    - C32: buyer, price, tender/sale range, closing path, minority-holder economics, corporate-action cutoff
    - C31 education: paid enrollment, renewal, ARPU, retention, channel cost, teacher/marketing cost, margin

  If MFE is shallow and MAE is large:
    route to hard 4C.

  If MFE is meaningful but execution evidence is not refreshed:
    preserve as capped positive or local 4B rather than Green.

  If MAE is controlled but MFE is shallow:
    cap at Watch/Yellow unless the execution bridge is explicit.

  If corporate-action, row-presence, or tradeability caveat appears:
    apply additional trust cap and block contaminated windows.
```

### Quantitative trigger candidates

```text
hard_4c_event_candidate:
  MFE < +12%
  AND MAE <= -30%
  AND company_specific_execution_bridge_missing == true

watch_cap_event_candidate:
  MFE < +7%
  AND MAE is controlled or moderate
  AND event relevance exists
  AND company-specific economic bridge is weak

capped_positive_event_candidate:
  MFE >= +15%
  AND MAE is not hard-failure
  AND event-company bridge is plausible
  BUT Green bridge is incomplete

local_4b_after_event_mfe:
  MFE >= +15%
  AND later MAE is material
  AND fresh execution evidence is absent

trust_caveat_cap:
  corporate_action_candidate_inside_window == true
  OR row_presence_tradeability_caveat == true
  -> block contaminated rows and cap actionability
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L94_C30_001260","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"001260","name":"남광토건","entry_date":"2024-07-24","entry_price":6950,"mfe_pct":23.0,"mae_pct":-14.4,"r13_verdict":"positive_capped_civil_regional_construction_relief_price_survival_but_pf_cashflow_trust_bridge_required","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L94_C30_010960","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"010960","name":"삼호개발","entry_date":"2024-07-30","entry_price":3650,"mfe_pct":0.0,"mae_pct":-15.3,"r13_verdict":"watch_yellow_cap_civil_construction_infra_label_without_pf_cashflow_repair_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L94_C30_001840","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"001840","name":"이화공영","entry_date":"2024-07-31","entry_price":3765,"mfe_pct":6.2,"mae_pct":-38.9,"r13_verdict":"hard_4c_small_construction_policy_theme_late_spike_without_pf_cashflow_trust_bridge_with_row_presence_caveat","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L94_C32_003920","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"003920","name":"남양유업","entry_date":"2024-02-19","entry_price":620000,"mfe_pct":16.1,"mae_pct":-25.0,"r13_verdict":"positive_capped_control_transfer_premium_with_4b_and_corporate_action_cutoff","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L94_C32_001750","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"001750","name":"한양증권","entry_date":"2024-07-24","entry_price":16000,"mfe_pct":21.3,"mae_pct":-23.9,"r13_verdict":"positive_local_sale_process_control_premium_with_4b_until_final_buyer_price_closing_confirmed","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L94_C32_003240","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"003240","name":"태광산업","entry_date":"2024-02-01","entry_price":943000,"mfe_pct":0.7,"mae_pct":-45.9,"r13_verdict":"hard_4c_activist_governance_asset_rich_label_without_executable_monetization_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L94_C31_096240","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"096240","name":"크레버스","entry_date":"2024-02-01","entry_price":16550,"mfe_pct":17.5,"mae_pct":-11.1,"r13_verdict":"positive_capped_premium_education_content_recurring_enrollment_margin_bridge_with_4b_watch","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L94_C31_072870","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"072870","name":"메가스터디","entry_date":"2024-02-01","entry_price":10990,"mfe_pct":5.5,"mae_pct":-3.5,"r13_verdict":"watch_yellow_cap_stable_education_holding_label_without_incremental_paid_enrollment_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L94_C31_095720","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"095720","name":"웅진씽크빅","entry_date":"2024-02-21","entry_price":2525,"mfe_pct":10.1,"mae_pct":-35.0,"r13_verdict":"hard_4c_children_learning_edtech_policy_label_without_paid_enrollment_margin_bridge","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":9,"reviewed_original_canonical_count":3,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","C31_POLICY_SUBSIDY_LEGISLATION_EVENT"],"reviewed_fine_branch_count":3,"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":4,"capped_positive_or_bridge_positive_count":4,"local_burst_or_4b_watch_count":4,"watch_yellow_cap_count":2,"stage2_false_positive_or_high_mae_count":5,"hard_4c_candidate_count":3,"accounting_or_listing_trust_caveat_count":1,"corporate_action_caveat_avoided_count":1,"policy_governance_trust_bridge_case_count":9,"construction_pf_case_count":3,"governance_control_case_count":3,"education_policy_service_case_count":3,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":94,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_EVENT_LABEL_TO_EXECUTION_BRIDGE_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For policy/event/governance/service archetypes across construction, governance, and education, do not open Stage2-Actionable or Stage3-Green from event salience or sector label alone. Classify the event as C30 balance-sheet/PF/project-cash trust, C32 governance/control-premium/sale-process, or C31 education-policy/service monetization. Require the matching bridge: PF exposure/project cash/receivables/backlog/funding/cost-margin/tradeability trust for C30, buyer/price/tender range/closing path/minority-holder economics/corporate-action cutoff for C32, and paid enrollment/renewal/ARPU/retention/channel cost/teacher-marketing cost/margin for C31 education. Route shallow-MFE/high-MAE cases to hard 4C; keep meaningful-MFE but unrefreshed bridges as capped positive or local 4B; cap low-MAE but shallow-MFE labels at Watch/Yellow unless execution bridge is explicit; apply additional trust caps when corporate-action, row-presence, or tradeability caveats appear.","expected_effect":"Unifies policy/event guardrails so the model stops confusing salience labels with company-specific execution, monetization, control economics, PF repair, or margin conversion.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":94,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"event_label_to_execution_bridge_guard","contribution":"Reviews nine prior loop94 cases without adding new independent evidence weight. Validates a shared event-label-to-execution guard across construction PF trust, governance/control-premium economics, and education policy paid-enrollment monetization.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_94_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_EVENT_LABEL_TO_EXECUTION_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original R10/R11/R12 loop94 files:
   - C30 small/regional/civil-builder PF/cash-flow/trust
   - C32 governance/control premium/tender cap
   - C31 education-policy/service paid enrollment
7. If enough R13 reviews agree, consider implementing a pre-scoring check for policy/event/governance/service archetypes:
   - classify the event type first,
   - identify the true company-level economic or legal bridge,
   - block event-label-only Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep meaningful-MFE but unrefreshed bridges as local 4B or capped positive,
   - cap low-MAE but shallow-MFE labels at Watch/Yellow,
   - apply corporate-action/row-presence/tradeability trust caps.

Expected next schedule:
completed_round = R13
completed_loop = 94
next_round = R1
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 11. Required round-state footer

```text
completed_round = R13
completed_loop = 94
next_round = R1
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
