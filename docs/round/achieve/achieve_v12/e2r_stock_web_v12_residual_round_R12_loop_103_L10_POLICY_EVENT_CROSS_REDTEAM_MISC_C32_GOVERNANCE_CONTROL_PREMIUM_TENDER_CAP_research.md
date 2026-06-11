# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R12
selected_loop: 103
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: GOVERNANCE_CASH_EXIT_EXECUTION_GATE_VS_CONTROL_SALE_ACTIVISM_AND_POLICY_CROSS_CONTAMINATION
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: cache_miss
  no_repeat_index: cache_miss
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

`C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` remains a thin governance/control-premium archetype. The previous local C32 sector run reached `R12/C32 loop 102`, so this file continues as `R12/C32 loop 103`.

This run is a boundary/refinement pass. It does not try to prove again that tender mechanics can move price. Instead it asks a narrower question:

```text
When does governance/control language create a legally visible cash-exit bridge, and when is it merely control-sale or activism vocabulary?
```

Direct raw GitHub fetch for the prompt/index returned cache miss in this turn. The file therefore uses the established v12 procedure from the current session and reuses current-session stock-web-derived rows already calculated from `Songdaiki/stock-web` tradable 1D OHLC. No production scoring is changed.

---

## 1. Research thesis

C32 is not `governance issue = upside`.

It is the cash-exit bridge:

```text
formal tender / buyback / appraisal / squeeze-out / binding shareholder cash event
→ legally visible price, participation mechanics, execution timing
→ price path validation
→ post-resolution 4B cap
```

The key problem is that the market often uses the same vocabulary for very different events:

```text
formal tender offer
control sale
state asset sale process
activism proposal
NAV discount debate
shareholder-return plan
```

Only the first group has a direct minority cash-exit bridge. The rest need execution before C32 Stage2 can open.

This loop splits six routes:

1. **Formal tender cash-exit path**
   - Stage2 stays open while the cash path is active.
   - Post-resolution or offer expiry requires local 4B.

2. **Control-battle affiliate tender mechanics**
   - Extreme MFE can be valid if the tender anchor is legally visible.
   - Still requires offer-fade / post-tender watch.

3. **Control sale without minority tender**
   - Stage2 false positive unless minority holders receive tender, appraisal, squeeze-out, or executed cash return.

4. **Activism/NAV proposal without vote or board execution**
   - Watch only; no Stage2-Actionable bonus.

5. **Failed state asset sale process**
   - Hard block when the sale fails and no minority cash path exists.

6. **Shareholder-return plan / policy overlap**
   - Real cash intent can belong to C31 or capital-return archetypes.
   - If operating cycle overrides price validation, C32 should not claim control-premium credit.

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
  - e2r_stock_web_v12_residual_round_R12_loop_102_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_8_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_7_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
reason:
  - rows already computed from Songdaiki/stock-web tradable raw 1D OHLC
  - this file turns C32 loop 102 plus R13 cash-bridge checks into a sector-specific C32 refinement
  - exact duplicate C32 keys should be deduped during batch ingest
  - no production scoring changed
```

Symbol caveats:

```yaml
041510:
  name: 에스엠
  role: formal tender/control contest cash path; post-resolution 4B watch

036560:
  name: KZ정밀
  role: control-battle affiliate tender cash path; post-tender watch

040300:
  name: YTN
  role: control-sale headline without minority tender cash exit

028260:
  name: 삼성물산
  role: activism/NAV proposal without passed vote or board execution

011200:
  name: HMM
  role: failed state asset sale process without minority cash exit

010130:
  name: 고려아연
  role: reused visible tender/counter-buyback positive control

005380:
  name: 현대차
  role: shareholder-return policy cash intent, but not C32 control-premium tender case
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"FORMAL_TENDER_CASH_EXIT_PATH_POST_RESOLUTION_4B_WATCH","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_close":114700,"price_basis":"tradable_raw","mfe_30d_pct":40.54,"mae_30d_pct":-6.45,"mfe_90d_pct":40.54,"mae_90d_pct":-21.10,"mfe_180d_pct":40.54,"mae_180d_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"case_role":"formal_tender_positive_with_post_resolution_watch","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|041510|Stage2-Actionable|2023-02-10","non_price_bridge":"formal tender/control contest cash path with visible minority exit mechanics","score_alignment":"keep Stage2 while cash-exit path is active; post-resolution 4B watch required","aggregate_credit_note":"exact key likely present in C32 loop 102; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_BATTLE_AFFILIATE_TENDER_CASH_PATH_WITH_OFFER_FADE_WATCH","symbol":"036560","name":"KZ정밀","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_close":12180,"price_basis":"tradable_raw","mfe_30d_pct":201.31,"mae_30d_pct":0.00,"mfe_90d_pct":201.31,"mae_90d_pct":0.00,"mfe_180d_pct":201.31,"mae_180d_pct":-11.25,"forward_high_30d":36700,"forward_low_30d":12180,"forward_high_90d":36700,"forward_low_90d":12180,"forward_high_180d":36700,"forward_low_180d":10810,"calibration_usable":true,"case_role":"tender_positive_with_post_offer_watch","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|036560|Stage2-Actionable|2024-09-13","non_price_bridge":"tender cash-exit mechanics in control battle affiliate; extreme MFE validates legal price anchor","score_alignment":"Stage2 valid during tender mechanics; local 4B after tender resolution or offer fade","aggregate_credit_note":"exact key likely present in C32 loop 102; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_SALE_HEADLINE_WITHOUT_MINORITY_TENDER_CASH_EXIT_FALSE_POSITIVE","symbol":"040300","name":"YTN","trigger_type":"Stage2-FalsePositive","entry_date":"2023-10-24","entry_close":7800,"price_basis":"tradable_raw","mfe_30d_pct":23.08,"mae_30d_pct":-30.64,"mfe_90d_pct":23.08,"mae_90d_pct":-30.64,"mfe_180d_pct":23.08,"mae_180d_pct":-49.29,"forward_high_30d":9600,"forward_low_30d":5410,"forward_high_90d":9600,"forward_low_90d":5410,"forward_high_180d":9600,"forward_low_180d":3955,"calibration_usable":true,"case_role":"hard_counterexample_no_minority_cash_exit","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|040300|Stage2-FalsePositive|2023-10-24","non_price_bridge":"control-sale headline without public minority tender/appraisal/squeeze-out cash path","score_alignment":"block Stage2-Actionable; control-sale vocabulary is not minority cash exit","aggregate_credit_note":"exact key likely present in C32 loop 102; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"NAV_DISCOUNT_ACTIVISM_PROPOSAL_WITHOUT_EXECUTION_STAGE2_CAP","symbol":"028260","name":"삼성물산","trigger_type":"Stage2-Watch","entry_date":"2024-03-15","entry_close":154100,"price_basis":"tradable_raw","mfe_30d_pct":7.98,"mae_30d_pct":-10.32,"mfe_90d_pct":7.98,"mae_90d_pct":-14.02,"mfe_180d_pct":7.98,"mae_180d_pct":-15.96,"forward_high_30d":166400,"forward_low_30d":138200,"forward_high_90d":166400,"forward_low_90d":132500,"forward_high_180d":166400,"forward_low_180d":129500,"calibration_usable":true,"case_role":"proposal_execution_missing_watch","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|028260|Stage2-Watch|2024-03-15","non_price_bridge":"NAV-discount activism proposal without passed vote, board execution, buyback/cancellation/dividend or tender cash bridge","score_alignment":"Stage2-Watch only; require executed cash bridge before Actionable","aggregate_credit_note":"exact key likely present in C32 loop 102; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"FAILED_STATE_ASSET_SALE_PROCESS_WITHOUT_MINORITY_CASH_EXIT_BLOCK","symbol":"011200","name":"HMM","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-02","entry_close":20600,"price_basis":"tradable_raw","mfe_30d_pct":4.85,"mae_30d_pct":-8.16,"mfe_90d_pct":4.85,"mae_90d_pct":-27.14,"mfe_180d_pct":4.85,"mae_180d_pct":-27.14,"forward_high_30d":21600,"forward_low_30d":18920,"forward_high_90d":21600,"forward_low_90d":15010,"forward_high_180d":21600,"forward_low_180d":15010,"calibration_usable":true,"case_role":"failed_sale_counterexample","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|011200|Stage2-FalsePositive|2024-01-02","non_price_bridge":"state asset sale process failed and did not create public minority cash-exit path","score_alignment":"Stage2-FalsePositive; failed control-sale process is not C32 tender mechanics","aggregate_credit_note":"exact key likely present in C32 loop 102; dedupe if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOSTILE_TENDER_BUYBACK_POSITIVE_CONTROL_VISIBLE_REUSED","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_close":666000,"price_basis":"tradable_raw","mfe_30d_pct":131.68,"mae_30d_pct":0.00,"mfe_90d_pct":131.68,"mae_90d_pct":0.00,"mfe_180d_pct":131.68,"mae_180d_pct":0.00,"forward_high_30d":1543000,"forward_low_30d":666000,"forward_high_90d":1543000,"forward_low_90d":666000,"forward_high_180d":1543000,"forward_low_180d":666000,"calibration_usable":true,"case_role":"reused_visible_positive_control","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|010130|Stage2-Actionable|2024-09-13","non_price_bridge":"hostile tender/counter-buyback cash price mechanics; visible-covered control only","score_alignment":"validates formal tender/buyback cash path; no new symbol credit if already indexed","aggregate_credit_note":"visible-covered positive control; use as control only if duplicate"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"SHAREHOLDER_RETURN_PLAN_REAL_CASH_BUT_NOT_CONTROL_PREMIUM_TENDER_C32_RECLASSIFY","symbol":"005380","name":"현대차","trigger_type":"Stage2-Watch","entry_date":"2024-08-28","entry_close":259000,"price_basis":"tradable_raw","mfe_30d_pct":3.09,"mae_30d_pct":-14.48,"mfe_90d_pct":3.09,"mae_90d_pct":-22.78,"mfe_180d_pct":3.09,"mae_180d_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"case_role":"reclassification_cap","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|005380|Stage2-Watch|2024-08-28","non_price_bridge":"shareholder-return policy cash intent, but not a control-premium tender/appraisal/squeeze-out event; operating cycle overrode price validation","score_alignment":"cap C32 contribution; reclassify to C31/C21 style capital-return policy unless tender/control cash-exit exists"}
```

---

## 4. Case analysis

### 4.1 SM Entertainment / 041510 — formal tender validates C32, then post-resolution 4B

SM is the standard positive. A formal tender cash path gives minority holders a price and mechanism. That is real C32 accounting trust.

```yaml
entry_close: 114700
30d_MFE_MAE: +40.54 / -6.45
90d_MFE_MAE: +40.54 / -21.10
180d_MFE_MAE: +40.54 / -21.10
route: Stage2-Actionable + post-resolution 4B
```

The drawdown after resolution is not a thesis failure; it is the normal C32 post-event cap. The rule must keep Stage2 during tender mechanics and move to 4B after the cash path expires.

---

### 4.2 KZ Precision / 036560 — control-battle affiliate tender validates, but offer fade matters

KZ Precision shows how powerful a visible tender cash anchor can be.

```yaml
entry_close: 12180
30d_MFE_MAE: +201.31 / 0.00
90d_MFE_MAE: +201.31 / 0.00
180d_MFE_MAE: +201.31 / -11.25
route: Stage2-Actionable + post-tender watch
```

This validates the C32 positive escape hatch, while also proving the need for post-offer normalization watch.

---

### 4.3 YTN / 040300 — control sale without tender is a false positive

YTN had control-sale vocabulary but not a minority cash-exit bridge.

```yaml
entry_close: 7800
30d_MFE_MAE: +23.08 / -30.64
90d_MFE_MAE: +23.08 / -30.64
180d_MFE_MAE: +23.08 / -49.29
route: Stage2-FalsePositive
```

A control sale is not automatically a public tender. C32 should block this route unless minority holders receive a legally defined exit.

---

### 4.4 Samsung C&T / 028260 — activism without execution remains Watch

Samsung C&T had a value/NAV/shareholder-return argument, but execution did not pass the bridge test.

```yaml
entry_close: 154100
90d_MFE_MAE: +7.98 / -14.02
180d_MFE_MAE: +7.98 / -15.96
route: Stage2-Watch
```

An activism proposal is a blueprint. C32 needs the building permit: passed vote, board execution, buyback/cancellation, dividend, tender, appraisal or squeeze-out mechanics.

---

### 4.5 HMM / 011200 — failed state asset sale is not minority cash exit

HMM is the sale-process false positive.

```yaml
entry_close: 20600
90d_MFE_MAE: +4.85 / -27.14
180d_MFE_MAE: +4.85 / -27.14
route: Stage2-FalsePositive
```

When the sale process fails and there was no public cash-exit mechanism, C32 must not keep the Stage2 bonus.

---

### 4.6 Korea Zinc / 010130 — reused tender/buyback positive control

Korea Zinc validates tender/counter-buyback mechanics but should not receive new symbol credit if already in the no-repeat index.

```yaml
entry_close: 666000
90d_MFE_MAE: +131.68 / 0.00
route: reused positive control
```

---

### 4.7 Hyundai Motor / 005380 — shareholder-return plan is not C32 tender

Hyundai Motor is a reclassification guard. Shareholder-return cash intent can be real, but it is not control-premium tender mechanics.

```yaml
entry_close: 259000
90d_MFE_MAE: +3.09 / -22.78
180d_MFE_MAE: +3.09 / -32.12
route: reclassify / C32 cap
```

If useful, this row belongs closer to C31/C21 capital-return policy, not C32 control-premium tender.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 1
reused_control_case_count: 6
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_case_count: 3
counterexample_or_cap_count: 4
post_resolution_or_reclassification_watch_count: 4
current_profile_error_count: 4
duplicate_note: exact C32 novelty keys likely already represented in loop 102; use this file as rule-refinement evidence unless batch ingest finds a new key
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 041510 | tender positive + 4B | +40.54 / -6.45 | +40.54 / -21.10 | +40.54 / -21.10 | formal tender cash path validates |
| 036560 | tender positive + 4B | +201.31 / 0.00 | +201.31 / 0.00 | +201.31 / -11.25 | offer anchor works, offer fade watch |
| 040300 | hard counterexample | +23.08 / -30.64 | +23.08 / -30.64 | +23.08 / -49.29 | control sale lacks minority cash exit |
| 028260 | activism watch | +7.98 / -10.32 | +7.98 / -14.02 | +7.98 / -15.96 | proposal needs execution |
| 011200 | hard counterexample | +4.85 / -8.16 | +4.85 / -27.14 | +4.85 / -27.14 | failed sale process has no tender bridge |
| 010130 | visible positive control | +131.68 / 0.00 | +131.68 / 0.00 | +131.68 / 0.00 | tender/buyback mechanics validate |
| 005380 | reclassification cap | +3.09 / -14.48 | +3.09 / -22.78 | +3.09 / -32.12 | shareholder return is not C32 tender |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"041510","raw_tender_cash_exit":5,"raw_legal_visibility":5,"raw_execution_status":4,"raw_minority_participation":5,"raw_post_resolution_cap":3,"raw_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"TenderPositive_PostResolution4B"}
{"row_type":"score_simulation","symbol":"036560","raw_tender_cash_exit":5,"raw_legal_visibility":5,"raw_execution_status":4,"raw_minority_participation":5,"raw_post_resolution_cap":4,"raw_validation":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"TenderPositive_PostOffer4B"}
{"row_type":"score_simulation","symbol":"040300","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":1,"raw_minority_participation":0,"raw_post_resolution_cap":5,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ControlSaleNoTenderBlock"}
{"row_type":"score_simulation","symbol":"028260","raw_tender_cash_exit":0,"raw_legal_visibility":2,"raw_execution_status":0,"raw_minority_participation":1,"raw_post_resolution_cap":2,"raw_validation":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ActivismProposalWatch"}
{"row_type":"score_simulation","symbol":"011200","raw_tender_cash_exit":0,"raw_legal_visibility":1,"raw_execution_status":0,"raw_minority_participation":0,"raw_post_resolution_cap":4,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"FailedSaleBlock"}
{"row_type":"score_simulation","symbol":"010130","raw_tender_cash_exit":5,"raw_legal_visibility":5,"raw_execution_status":4,"raw_minority_participation":5,"raw_post_resolution_cap":3,"raw_validation":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"ReusedTenderPositiveControl"}
{"row_type":"score_simulation","symbol":"005380","raw_tender_cash_exit":0,"raw_legal_visibility":2,"raw_execution_status":2,"raw_minority_participation":1,"raw_post_resolution_cap":3,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyCapitalReturnPolicy"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C32 can over-credit:

```text
governance dispute
control sale
activism proposal
shareholder return plan
```

The correct C32 bridge is narrower:

```text
formal tender / buyback / appraisal / squeeze-out / legally executable cash return
→ minority holder can actually receive cash or a defined price
```

A tender is a checkout counter. A control sale is only a change in store owner. An activism proposal is a shopping list. The model should not pay for the shopping list.

### Rule candidate

```text
C32_GOVERNANCE_CASH_EXIT_EXECUTION_REQUIREMENT_V103

if C32
and governance_control_premium_or_activism_label == true
and formal_tender_buyback_appraisal_squeezeout_or_executed_cash_return == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C32
and formal_tender_buyback_or_cash_exit_path == true
and legally_visible_price_or_mechanics == true:
    keep_stage2_actionable_bonus = true
    if offer_expiry_resolution_or_cash_path_fade == true:
        local_4B_watch = true
```

```text
if C32
and control_sale_headline == true
and minority_cash_exit_path == false
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if C32
and activism_or_NAV_discount_proposal == true
and vote_board_or_buyback_execution == false:
    stage2_actionable_bonus = 0
    require_executed_buyback_cancellation_dividend_tender_or_appraisal = true
```

```text
if shareholder_return_plan == true
and control_premium_or_tender_mechanics == false:
    cap_C32_contribution = true
    require_reclassification_to_C31_or_C21 = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_refinement_from_existing_controls
new_axis_proposed: C32_GOVERNANCE_CASH_EXIT_EXECUTION_REQUIREMENT_V103
existing_axis_strengthened:
  - C32_tender_cash_exit_positive_escape_hatch
  - C32_post_resolution_local_4B_watch
  - C32_control_sale_without_minority_cash_exit_block
  - C32_activism_proposal_requires_execution
  - C32_shareholder_return_plan_reclassification_guard
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C32 loop with C32 loop 102 and adjacent R13 cash-bridge, Stage2 false-positive, high-MAE and 4B/4C guardrail files. Extract `C32_GOVERNANCE_CASH_EXIT_EXECUTION_REQUIREMENT_V103` as a shadow-rule candidate. Preserve formal tender/buyback/appraisal/squeeze-out cash-exit positives, enforce post-resolution local 4B, and block control-sale, activism, failed-sale, and shareholder-return-policy rows unless executed minority cash mechanics are visible.
```

---

## 10. Next research state

```yaml
completed_round: R12
completed_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
