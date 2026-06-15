# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 8
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: GOVERNANCE_TENDER_POLICY_CASHFLOW_ACCOUNTING_TRUST_VS_CONTROL_SALE_AND_POLICY_LABEL
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

R13 is a cross-archetype checkpoint, not a new sector-specific discovery round. This loop compares recent `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` and `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` evidence through one ledger question:

```text
Did the event create a legally or economically traceable cash bridge for listed minority shareholders?
```

The previous local `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` run reached loop 7. This continuation is `loop 8`.

---

## 1. Research thesis

Accounting trust is not the same as market excitement.

```text
tender / buyback / legally defined price / signed contract / shareholder cash return
→ traceable cash bridge
→ Stage2 can survive

control sale headline / activism proposal / exploration headline / broad policy label
→ attention without cash bridge
→ Stage2 should be capped or blocked
```

The mechanism is like a ledger. A headline is an invoice request. Stage2 requires that the invoice can be matched to a payer, price, recipient, timing, and cash path.

This loop splits seven routes:

1. **Tender cash-exit path** — accounting trust validated, but post-resolution 4B watch needed.
2. **Tender affiliate cash path** — extreme MFE validates tender mechanics, but post-offer normalization needs watch.
3. **Control sale without minority cash exit** — hard counterexample.
4. **Activism proposal without vote/execution** — Stage2 cap.
5. **Failed state asset sale without minority cash path** — hard counterexample.
6. **Signed state-linked export contract** — direct revenue bridge validates C31/C32-style event.
7. **Shareholder-return plan overwhelmed by core cycle** — cash intent is real, but accounting trust is insufficient without operating confirmation.

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

Validation basis:

```yaml
price_rows_reused_from_current_session:
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP loop 102
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT loop 101
  - R13_STAGE2_FALSE_POSITIVE_POLICY_TO_CASHFLOW_GATE_V7
reason:
  - individual stock-web shard fetch for new symbols returned intermittent cache miss in this turn
  - prior session rows were already computed from stock-web 30D/90D/180D windows
  - no production scoring changed
```

Symbol caveats:

```yaml
041510:
  name: 에스엠
  source_archetype: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  role: formal tender/control contest cash path

036560:
  name: KZ정밀
  source_archetype: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  role: tender cash-exit path in control battle affiliate

040300:
  name: YTN
  source_archetype: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  role: control sale headline without minority tender cash exit

028260:
  name: 삼성물산
  source_archetype: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  role: activism/NAV-discount proposal without passed execution

011200:
  name: HMM
  source_archetype: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  role: failed control-sale process without minority cash exit

064350:
  name: 현대로템
  source_archetype: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  role: state-linked signed export contract / direct revenue bridge

005380:
  name: 현대차
  source_archetype: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  role: shareholder-return policy with core cycle override
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"FORMAL_TENDER_CASH_EXIT_ACCOUNTING_TRUST_VALIDATED_POST_RESOLUTION_4B","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_close":114700,"price_basis":"tradable_raw","mfe_30d_pct":40.54,"mae_30d_pct":-6.45,"mfe_90d_pct":40.54,"mae_90d_pct":-21.10,"mfe_180d_pct":40.54,"mae_180d_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"case_role":"accounting_trust_validated_with_post_resolution_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|041510|Stage2-Actionable|2023-02-10","accounting_bridge":"formal tender/control contest cash path with legally visible minority exit price","route":"KeepStage2_PostResolution4B"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CONTROL_BATTLE_AFFILIATE_TENDER_CASH_PATH_VALIDATED_WITH_OFFER_FADE_WATCH","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"036560","name":"KZ정밀","trigger_type":"Stage2-Actionable","entry_date":"2024-09-13","entry_close":12180,"price_basis":"tradable_raw","mfe_30d_pct":201.31,"mae_30d_pct":0.00,"mfe_90d_pct":201.31,"mae_90d_pct":0.00,"mfe_180d_pct":201.31,"mae_180d_pct":-11.25,"forward_high_30d":36700,"forward_low_30d":12180,"forward_high_90d":36700,"forward_low_90d":12180,"forward_high_180d":36700,"forward_low_180d":10810,"calibration_usable":true,"case_role":"accounting_trust_validated_with_post_tender_watch","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|036560|Stage2-Actionable|2024-09-13","accounting_bridge":"tender offer cash-exit mechanics in Korea Zinc control battle affiliate","route":"KeepStage2_PostTender4B"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"CONTROL_SALE_HEADLINE_NO_MINORITY_CASH_EXIT_ACCOUNTING_TRUST_BLOCK","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"040300","name":"YTN","trigger_type":"Stage2-FalsePositive","entry_date":"2023-10-24","entry_close":7800,"price_basis":"tradable_raw","mfe_30d_pct":23.08,"mae_30d_pct":-30.64,"mfe_90d_pct":23.08,"mae_90d_pct":-30.64,"mfe_180d_pct":23.08,"mae_180d_pct":-49.29,"forward_high_30d":9600,"forward_low_30d":5410,"forward_high_90d":9600,"forward_low_90d":5410,"forward_high_180d":9600,"forward_low_180d":3955,"calibration_usable":true,"case_role":"accounting_trust_not_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|040300|Stage2-FalsePositive|2023-10-24","accounting_bridge":"control sale headline without minority tender or legally defined cash-exit path","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"ACTIVISM_PROPOSAL_WITHOUT_EXECUTION_ACCOUNTING_TRUST_CAP","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"028260","name":"삼성물산","trigger_type":"Stage2-Watch","entry_date":"2024-03-15","entry_close":154100,"price_basis":"tradable_raw","mfe_30d_pct":7.98,"mae_30d_pct":-10.32,"mfe_90d_pct":7.98,"mae_90d_pct":-14.02,"mfe_180d_pct":7.98,"mae_180d_pct":-15.96,"forward_high_30d":166400,"forward_low_30d":138200,"forward_high_90d":166400,"forward_low_90d":132500,"forward_high_180d":166400,"forward_low_180d":129500,"calibration_usable":true,"case_role":"watch_execution_missing","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|028260|Stage2-Watch|2024-03-15","accounting_bridge":"NAV-discount activism proposal without passed vote or executed shareholder-return bridge","route":"Stage2Cap_UntilExecution"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"FAILED_STATE_ASSET_SALE_NO_MINORITY_CASH_EXIT_BLOCK","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"011200","name":"HMM","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-02","entry_close":20600,"price_basis":"tradable_raw","mfe_30d_pct":4.85,"mae_30d_pct":-8.16,"mfe_90d_pct":4.85,"mae_90d_pct":-27.14,"mfe_180d_pct":4.85,"mae_180d_pct":-27.14,"forward_high_30d":21600,"forward_low_30d":18920,"forward_high_90d":21600,"forward_low_90d":15010,"forward_high_180d":21600,"forward_low_180d":15010,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|011200|Stage2-FalsePositive|2024-01-02","accounting_bridge":"state asset sale process failed without tender or minority cash-exit path","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"STATE_LINKED_SIGNED_EXPORT_CONTRACT_ACCOUNTING_TRUST_VALIDATED","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"064350","name":"현대로템","trigger_type":"Stage2-Actionable","entry_date":"2025-02-26","entry_close":85600,"price_basis":"tradable_raw","mfe_30d_pct":36.45,"mae_30d_pct":-8.64,"mfe_90d_pct":157.59,"mae_90d_pct":-8.64,"mfe_180d_pct":157.59,"mae_180d_pct":-8.64,"forward_high_30d":116800,"forward_low_30d":78200,"forward_high_90d":220500,"forward_low_90d":78200,"forward_high_180d":220500,"forward_low_180d":78200,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|064350|Stage2-Actionable|2025-02-26","accounting_bridge":"signed state-linked export order with direct revenue path","route":"KeepStage2_DirectRevenueBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"SHAREHOLDER_RETURN_PLAN_REAL_CASH_BUT_CYCLE_OVERRIDES_ACCOUNTING_TRUST","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"005380","name":"현대차","trigger_type":"Stage2-Watch","entry_date":"2024-08-28","entry_close":259000,"price_basis":"tradable_raw","mfe_30d_pct":3.09,"mae_30d_pct":-14.48,"mfe_90d_pct":3.09,"mae_90d_pct":-22.78,"mfe_180d_pct":3.09,"mae_180d_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"case_role":"cash_intent_but_price_validation_failed","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005380|Stage2-Watch|2024-08-28","accounting_bridge":"shareholder-return plan is real, but auto volume/mix/margin cycle overrode price validation","route":"Stage2Cap_CycleOverridesCashReturn"}
```

---

## 4. Case analysis

### 4.1 SM Entertainment / 041510 — tender accounting trust validated, then capped

SM is a clean example of a formal cash-exit path. Accounting trust exists because minority holders had a visible tender/cash mechanism. But the 90D/180D drawdown shows why post-resolution 4B is mandatory.

```text
route = KeepStage2_PostResolution4B
```

### 4.2 KZ Precision / 036560 — tender cash mechanics validated

The KZ Precision case is an extreme example: the tender anchor created +201.31% MFE. This is a valid accounting bridge, not mere governance vocabulary. The later -11.25% 180D MAE still makes post-tender watch necessary.

```text
route = KeepStage2_PostTender4B
```

### 4.3 YTN / 040300 — control sale without cash exit fails

YTN had the language of control premium, but not the mechanics of minority cash exit. Accounting trust fails.

```text
route = Stage2FalsePositiveBlock
```

### 4.4 Samsung C&T / 028260 — activism proposal without execution

An activism proposal can point at value, but until it passes vote/board execution and becomes buyback/cancellation/dividend/tender cash, accounting trust remains incomplete.

```text
route = Stage2Cap_UntilExecution
```

### 4.5 HMM / 011200 — failed sale process is not a shareholder cash path

A state asset sale process can be a control event without being a minority shareholder cash event. Once sale negotiations fail, the bridge disappears.

```text
route = Stage2FalsePositiveBlock
```

### 4.6 Hyundai Rotem / 064350 — signed export order is accounting-trust positive

Rotem is the non-governance positive control. A signed state-linked export order creates a direct revenue path, so Stage2 survives.

```text
route = KeepStage2_DirectRevenueBridge
```

### 4.7 Hyundai Motor / 005380 — cash-return intent but price validation failed

Hyundai Motor shows that real shareholder-return intent is not always enough. If the operating cycle dominates, accounting trust is not sufficient for Stage2-Actionable.

```text
route = Stage2Cap_CycleOverridesCashReturn
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 7
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
accounting_trust_validated_count: 3
post_resolution_4B_count: 2
stage2_cap_count: 2
stage2_false_positive_count: 2
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | accounting lesson |
|---|---:|---:|---:|---:|---|
| 041510 | C32 | tender valid + 4B | +40.54 / -21.10 | +40.54 / -21.10 | tender cash path exists, post-resolution cap |
| 036560 | C32 | tender valid + 4B | +201.31 / 0.00 | +201.31 / -11.25 | tender anchor validates, offer fade watch |
| 040300 | C32 | hard block | +23.08 / -30.64 | +23.08 / -49.29 | control sale lacks minority cash exit |
| 028260 | C32 | Stage2 cap | +7.98 / -14.02 | +7.98 / -15.96 | proposal without execution lacks cash bridge |
| 011200 | C32 | hard block | +4.85 / -27.14 | +4.85 / -27.14 | failed sale is not cash exit |
| 064350 | C31 | direct revenue bridge | +157.59 / -8.64 | +157.59 / -8.64 | signed export order validates |
| 005380 | C31 | Stage2 cap | +3.09 / -22.78 | +3.09 / -32.12 | cash-return plan overruled by cycle |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"041510","raw_cash_bridge":5,"raw_legal_visibility":5,"raw_execution_status":4,"raw_price_validation":4,"raw_post_resolution_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PostResolution4B"}
{"row_type":"score_simulation","symbol":"036560","raw_cash_bridge":5,"raw_legal_visibility":5,"raw_execution_status":4,"raw_price_validation":5,"raw_post_resolution_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PostTender4B"}
{"row_type":"score_simulation","symbol":"040300","raw_cash_bridge":0,"raw_legal_visibility":1,"raw_execution_status":1,"raw_price_validation":0,"raw_post_resolution_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"028260","raw_cash_bridge":1,"raw_legal_visibility":2,"raw_execution_status":0,"raw_price_validation":1,"raw_post_resolution_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_UntilExecution"}
{"row_type":"score_simulation","symbol":"011200","raw_cash_bridge":0,"raw_legal_visibility":1,"raw_execution_status":0,"raw_price_validation":0,"raw_post_resolution_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"064350","raw_cash_bridge":5,"raw_legal_visibility":4,"raw_execution_status":5,"raw_price_validation":5,"raw_post_resolution_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_DirectRevenueBridge"}
{"row_type":"score_simulation","symbol":"005380","raw_cash_bridge":3,"raw_legal_visibility":3,"raw_execution_status":2,"raw_price_validation":0,"raw_post_resolution_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_CycleOverridesCashReturn"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The current profile can still confuse these three:

```text
formal cash bridge
control/governance headline
cash intention without price validation
```

The first should keep Stage2. The second should be blocked. The third should be capped until operating or execution evidence confirms.

### Rule candidate

```text
R13_ACCOUNTING_TRUST_CASH_BRIDGE_GATE_V8

if formal_tender_buyback_cash_exit_signed_contract_or_binding_cash_transfer == true
and legally_visible_price_or_revenue_path == true
and MFE_90D_pct >= +20:
    accounting_trust_validated = true
    keep_stage2_actionable_bonus = true
```

```text
if control_sale_governance_or_policy_headline == true
and minority_cash_exit_or_direct_revenue_bridge == false:
    accounting_trust_validated = false
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if formal_cash_path_resolved_or_expiring == true:
    local_4B_watch = true
    block_stage3_green_without_fresh_cash_bridge = true
```

```text
if shareholder_return_plan == true
and operating_cycle_or_margin_risk_overrides == true
and MFE_90D_pct < +10:
    stage2_actionable_bonus = 0
    route = Stage2Cap_CycleOverridesCashReturn
```

```text
if activism_or_NAV_discount_proposal == true
and vote_board_or_buyback_execution == false:
    stage2_actionable_bonus = 0
    route = Stage2Cap_UntilExecution
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_accounting_trust_cash_bridge_candidate
new_axis_proposed: R13_ACCOUNTING_TRUST_CASH_BRIDGE_GATE_V8
existing_axis_strengthened:
  - formal_tender_buyback_contract_cash_bridge_keep_stage2
  - control_sale_without_minority_cash_exit_block
  - post_resolution_cash_path_local_4B
  - activism_proposal_without_execution_stage2_cap
  - shareholder_return_plan_cycle_override_cap
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 loop with C32 loop 102, C31 loop 101, and adjacent R13 accounting-trust / Stage2 false-positive files. Extract `R13_ACCOUNTING_TRUST_CASH_BRIDGE_GATE_V8` as a cross-archetype shadow rule. Preserve formal tender/buyback/cash-exit and signed contract escape hatches; block control-sale headlines, failed sales, and activism proposals without executed cash bridge.
```

---

## 10. Next research state

```yaml
completed_round: R13
completed_loop: 8
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```
