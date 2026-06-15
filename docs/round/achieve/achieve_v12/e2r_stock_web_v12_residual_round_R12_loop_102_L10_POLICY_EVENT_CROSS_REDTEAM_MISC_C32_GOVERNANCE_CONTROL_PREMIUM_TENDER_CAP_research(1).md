# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R12
selected_loop: 102
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: TENDER_CASH_EXIT_PATH_VS_CONTROL_PREMIUM_LABEL_AND_POST_RESOLUTION_CAP
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

`C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` remains one of the thinnest Priority 0 archetypes in the no-repeat index: 3 rows / 3 symbols. The visible top-covered symbols are `000670`, `010130`, and `180640`. This run therefore emphasizes non-visible tender/control cases and uses `010130` only as a reused positive control.

The previous local C32 pass reached loop 101. This run continues as `R12/C32 loop 102`.

---

## 1. Research thesis

C32 is not “governance issue = upside.” It is the narrow bridge:

```text
control premium / tender / governance action
→ legally defined minority cash-exit or executed capital-return path
→ price path validation
→ post-resolution cap and downside guardrail
```

The main split:

1. **Formal tender / cash-exit path**
   - A tender offer or buyback with explicit price and process gives minority holders an actual exit bridge.
   - Stage2 can stay open.
   - But once the offer is resolved, a local 4B watch is required because upside can be capped and post-event drawdown can appear.

2. **Control sale / governance fight without minority cash exit**
   - Control may change, but minority shareholders do not necessarily receive cash.
   - Price can spike from control-premium vocabulary.
   - Without a tender, squeeze-out, appraisal right, passed buyback/cancellation, or binding shareholder-return event, Stage2-Actionable should be blocked.

3. **Activism / NAV-discount / value-up proposal without execution**
   - Governance pressure can be real, but a failed vote or non-binding proposal is not a cash bridge.
   - Treat as Stage2-Watch or false-positive unless execution occurs.

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

Symbol caveats:

```yaml
041510:
  name: 에스엠
  role: formal tender/control contest positive with post-resolution 4B watch
  price_window: stock-web 2023 tradable rows

036560:
  name: KZ정밀 / former 영풍정밀
  role: tender cash-exit path positive with post-offer normalization watch
  price_window: stock-web 2024~2025 tradable rows

040300:
  name: YTN
  role: control sale headline without minority tender counterexample
  price_window: stock-web 2023~2024 tradable rows

028260:
  name: 삼성물산
  role: activism/NAV-discount proposal failed vote counterexample
  price_window: stock-web 2024 tradable rows

011200:
  name: HMM
  role: state asset sale process / failed sale without minority cash-exit counterexample
  price_window: stock-web 2024 tradable rows

010130:
  name: 고려아연
  role: reused tender/control premium positive control
  note: visible-covered in no-repeat index; control only, no new symbol credit
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"FORMAL_TENDER_CASH_EXIT_PATH_POST_RESOLUTION_4B_WATCH","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_close":114700,"price_basis":"tradable_raw","mfe_30d_pct":40.54,"mae_30d_pct":-6.45,"mfe_90d_pct":40.54,"mae_90d_pct":-21.10,"mfe_180d_pct":40.54,"mae_180d_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"case_role":"positive_with_post_resolution_4B_watch","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|041510|Stage2-Actionable|2023-02-10","non_price_bridge":"formal tender/cash path in HYBE-Kakao control contest","score_alignment":"Stage2 valid while cash-exit path exists; post-resolution 4B watch required"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"KOREA_ZINC_BATTLE_AFFILIATE_TENDER_CASH_PATH_WITH_POST_OFFER_CAP","symbol":"036560","name":"KZ정밀","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_close":12180,"price_basis":"tradable_raw","mfe_30d_pct":201.31,"mae_30d_pct":0.00,"mfe_90d_pct":201.31,"mae_90d_pct":0.00,"mfe_180d_pct":201.31,"mae_180d_pct":-11.25,"forward_high_30d":36700,"forward_low_30d":12180,"forward_high_90d":36700,"forward_low_90d":12180,"forward_high_180d":36700,"forward_low_180d":10810,"calibration_usable":true,"case_role":"positive_with_post_tender_4B_watch","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|036560|Stage2-Actionable|2024-09-13","non_price_bridge":"tender offer cash-exit path in Korea Zinc control battle affiliate","score_alignment":"cash path validates Stage2; post-offer normalization requires local 4B"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_SALE_HEADLINE_WITHOUT_MINORITY_TENDER_CASH_EXIT_FALSE_POSITIVE","symbol":"040300","name":"YTN","trigger_type":"Stage2-FalsePositive","entry_date":"2023-10-24","entry_close":7800,"price_basis":"tradable_raw","mfe_30d_pct":23.08,"mae_30d_pct":-30.64,"mfe_90d_pct":23.08,"mae_90d_pct":-30.64,"mfe_180d_pct":23.08,"mae_180d_pct":-49.29,"forward_high_30d":9600,"forward_low_30d":5410,"forward_high_90d":9600,"forward_low_90d":5410,"forward_high_180d":9600,"forward_low_180d":3955,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|040300|Stage2-FalsePositive|2023-10-24","non_price_bridge":"control sale headline without legally defined minority cash-exit path","score_alignment":"spike decayed; block Stage2-Actionable without tender/appraisal/cash-exit bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"NAV_DISCOUNT_ACTIVISM_FAILED_VOTE_NO_EXECUTED_CASH_BRIDGE","symbol":"028260","name":"삼성물산","trigger_type":"Stage2-Watch","entry_date":"2024-03-15","entry_close":154100,"price_basis":"tradable_raw","mfe_30d_pct":7.98,"mae_30d_pct":-10.32,"mfe_90d_pct":7.98,"mae_90d_pct":-14.02,"mfe_180d_pct":7.98,"mae_180d_pct":-15.96,"forward_high_30d":166400,"forward_low_30d":138200,"forward_high_90d":166400,"forward_low_90d":132500,"forward_high_180d":166400,"forward_low_180d":129500,"calibration_usable":true,"case_role":"proposal_execution_counterexample","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|028260|Stage2-Watch|2024-03-15","non_price_bridge":"NAV-discount activism and shareholder-return proposal without passed execution bridge","score_alignment":"watch only; failed vote/non-binding governance pressure blocks Stage2-Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"FAILED_CONTROL_SALE_PROCESS_WITHOUT_MINORITY_CASH_EXIT","symbol":"011200","name":"HMM","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-02","entry_close":20600,"price_basis":"tradable_raw","mfe_30d_pct":4.85,"mae_30d_pct":-8.16,"mfe_90d_pct":4.85,"mae_90d_pct":-27.14,"mfe_180d_pct":4.85,"mae_180d_pct":-27.14,"forward_high_30d":21600,"forward_low_30d":18920,"forward_high_90d":21600,"forward_low_90d":15010,"forward_high_180d":21600,"forward_low_180d":15010,"calibration_usable":true,"case_role":"failed_sale_counterexample","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|011200|Stage2-FalsePositive|2024-01-02","non_price_bridge":"state asset control-sale process without minority tender cash-exit; later failed negotiation","score_alignment":"control-sale vocabulary without public minority cash path should not open C32 Stage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R12","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOSTILE_TENDER_BUYBACK_POSITIVE_CONTROL_VISIBLE_REUSED","symbol":"010130","name":"고려아연","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_close":666000,"price_basis":"tradable_raw","mfe_30d_pct":131.68,"mae_30d_pct":0.00,"mfe_90d_pct":131.68,"mae_90d_pct":0.00,"mfe_180d_pct":131.68,"mae_180d_pct":0.00,"forward_high_30d":1543000,"forward_low_30d":666000,"forward_high_90d":1543000,"forward_low_90d":666000,"forward_high_180d":1543000,"forward_low_180d":666000,"calibration_usable":true,"case_role":"reused_visible_positive_control","novelty_key":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP|010130|Stage2-Actionable|2024-09-13","non_price_bridge":"hostile tender/counter-buyback with explicit cash price mechanics","score_alignment":"control only; validates tender-cash path but no new symbol-credit"}
```

---

## 4. Case analysis

### 4.1 SM Entertainment / 041510 — formal tender path worked, but post-resolution cap mattered

SM validates the positive side of C32. The event was not abstract governance pressure. It had a visible tender/cash-price route. The price path reached +40.54% MFE, validating Stage2.

But by 90D/180D the post-resolution drawdown had reached -21.10%. This proves the second half of the C32 rule: even a valid tender case should enter local 4B watch after tender/control resolution.

```text
route = Stage2-Actionable while tender cash path exists
post_resolution = local 4B watch
```

### 4.2 KZ Precision / 036560 — tender offer cash path produced extreme MFE

KZ Precision is a stronger cash-exit example. Entry at 12,180 and forward high 36,700 gives +201.31% MFE. This is not ordinary governance rumor; the tender path created a real valuation anchor.

But the later low 10,810 shows post-offer normalization risk. The score should not keep extrapolating control-premium MFE after the tender dynamic fades.

```text
route = Stage2-Actionable with post-tender 4B watch
```

### 4.3 YTN / 040300 — control sale without minority tender failed

YTN is a classic C32 false positive. There was a control-sale narrative, but the minority shareholder did not receive a formal tender/cash-exit path. The stock spiked, then 180D MAE reached -49.29%.

```text
route = Stage2-FalsePositive_Block
```

### 4.4 Samsung C&T / 028260 — activism proposal without execution

Samsung C&T tests the capital-return/governance pressure branch. A NAV-discount activism thesis can be real, but the vote/execution bridge matters. Failed proposal and weak MFE mean it remains Watch, not Actionable.

```text
route = Stage2-Watch
block Stage2-Actionable until vote/buyback/cancellation/dividend execution
```

### 4.5 HMM / 011200 — failed sale process without minority cash exit

HMM shows that a state asset sale or control process is not automatically a minority cash exit. When negotiations break, no tender-style price floor remains. Low MFE and deep MAE make this a hard false-positive guardrail row.

```text
route = Stage2-FalsePositive_Block
```

### 4.6 Korea Zinc / 010130 — reused positive control

Korea Zinc is already visible-covered in the no-repeat index, so this row is used only as a control. It validates the tender/counter-buyback mechanics, but should not receive new symbol-diversity credit in this loop.

```text
route = reused positive control
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 5
reused_control_case_count: 1
new_visible_C32_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 3
counterexample_or_cap_count: 3
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 041510 | tender positive + 4B | +40.54 / -6.45 | +40.54 / -21.10 | +40.54 / -21.10 | tender path works, post-resolution cap |
| 036560 | tender positive + post-offer 4B | +201.31 / 0.00 | +201.31 / 0.00 | +201.31 / -11.25 | cash path works, offer fade risk |
| 040300 | control-sale counterexample | +23.08 / -30.64 | +23.08 / -30.64 | +23.08 / -49.29 | no minority tender = false positive |
| 028260 | activism failed-execution watch | +7.98 / -10.32 | +7.98 / -14.02 | +7.98 / -15.96 | proposal/vote failure blocks Actionable |
| 011200 | failed sale counterexample | +4.85 / -8.16 | +4.85 / -27.14 | +4.85 / -27.14 | failed sale process lacks cash exit |
| 010130 | reused control | +131.68 / 0.00 | +131.68 / 0.00 | +131.68 / 0.00 | visible-covered tender control |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"041510","raw_visibility":5,"raw_tender_cash_path":5,"raw_minority_cash_exit":5,"raw_execution_status":4,"raw_post_resolution_cap":3,"raw_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-post-resolution-4B"}
{"row_type":"score_simulation","symbol":"036560","raw_visibility":5,"raw_tender_cash_path":5,"raw_minority_cash_exit":5,"raw_execution_status":4,"raw_post_resolution_cap":4,"raw_validation":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-post-tender-4B"}
{"row_type":"score_simulation","symbol":"040300","raw_visibility":4,"raw_tender_cash_path":0,"raw_minority_cash_exit":0,"raw_execution_status":1,"raw_post_resolution_cap":5,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-control-sale-no-tender"}
{"row_type":"score_simulation","symbol":"028260","raw_visibility":4,"raw_tender_cash_path":0,"raw_minority_cash_exit":1,"raw_execution_status":0,"raw_post_resolution_cap":2,"raw_validation":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-failed-vote-no-cash-bridge"}
{"row_type":"score_simulation","symbol":"011200","raw_visibility":3,"raw_tender_cash_path":0,"raw_minority_cash_exit":0,"raw_execution_status":0,"raw_post_resolution_cap":4,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-failed-sale"}
{"row_type":"score_simulation","symbol":"010130","raw_visibility":5,"raw_tender_cash_path":5,"raw_minority_cash_exit":5,"raw_execution_status":4,"raw_post_resolution_cap":3,"raw_validation":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Reused-positive-control"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C32 can still over-reward three patterns:

```text
governance fight
control sale
NAV discount / activism proposal
```

These are not equivalent to a cash exit. A tender is a bridge with a toll booth and a price. A control-sale headline is just a road sign. An activism proposal is a blueprint. The model should pay for the toll booth, not the sign or the blueprint.

### Rule candidate

```text
C32_TENDER_CASH_EXIT_REQUIREMENT_V102

if C32
and governance_control_premium_headline == true
and formal_tender_buyback_squeezeout_appraisal_or_executed_cash_return == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C32
and formal_tender_or_buyback_cash_exit_path == true
and legally_defined_price_per_share == true:
    keep_stage2_actionable_bonus = true
    if tender_resolution_or_offer_expiry_near == true:
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
and vote_or_board_execution == false:
    stage2_actionable_bonus = 0
    require_executed_buyback_cancellation_dividend_or_tender = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C32_TENDER_CASH_EXIT_REQUIREMENT_V102
existing_axis_strengthened:
  - C32_formal_tender_cash_exit_path_positive_escape_hatch
  - C32_post_tender_resolution_local_4B_watch
  - C32_control_sale_without_minority_cash_exit_stage2_block
  - C32_failed_sale_process_false_positive_block
  - C32_activism_proposal_requires_execution
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C32 loop with prior C32 loop 100~101 and R13 accounting-trust / Stage2 false-positive guardrail files. Extract `C32_TENDER_CASH_EXIT_REQUIREMENT_V102` as a shadow-rule candidate. Preserve formal tender/buyback/appraisal-right/minority cash-exit escape hatches, but block control-sale headlines, failed sales, and non-executed activism proposals from receiving Stage2-Actionable bonus.
```

---

## 10. Next research state

```yaml
completed_round: R12
completed_loop: 102
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```
