# E2R Stock-Web v12 Residual Research — R11 loop 89

```yaml
artifact_type: e2r_stock_web_v12_residual_research
scheduled_round: R11
scheduled_loop: 89
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_EVENT_TO_CONTRACT_EXECUTION_BRIDGE
round_schedule_status: valid
round_sector_consistency: pass
current_default_profile_proxy: e2r_2_1_stock_web_calibrated
previous_baseline_reference: e2r_2_0_baseline
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
do_not_propose_new_weight_delta: true
completed_round: R11
completed_loop: 89
next_round: R12
next_loop: 89
```

## 0. Execution note

This run follows the v12 round scheduler after the completed `R10 / loop 89` artifact.  
Therefore the valid next artifact is `R11 / loop 89`.

R11 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or a policy-defense-linked L1 path. This artifact uses the L10 policy-event route and focuses on `C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY`.

The research objective is not to recommend current nuclear stocks. It is to test whether a nuclear policy/project headline should be treated as Stage2-Actionable or Stage3-ready before the project has a company-specific conversion bridge.

---

## 1. Why this archetype / gap

`C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` is under-covered relative to the heavily repeated C30/C31/C32 policy-event cluster.

Current No-Repeat coverage snapshot used for this run:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rows: 12
symbols: 7
date range: 2022-03-10 ~ 2025-01-17
positive/counterexample: 5/3
4B/4C: 1/0
top repeated symbols:
  011700(4), 083650(3), 006910(1), 034020(1), 042370(1), 046120(1)
```

This run avoids the top repeated combinations and uses three new C04 symbols:

```text
052690 한전기술
051600 한전KPS
105840 우진
```

All three are exposed to the same broad policy headline, but they should not be scored the same way.  
A nuclear export headline is the spark. The scoring question is whether the spark reaches fuel: contract scope, project participation, order timing, execution margin, recurring service revenue, or instrument shipment.

---

## 2. Source and price-data controls

Stock-Web basis:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
symbol_count: 5,414
active_like_symbol_count: 2,868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
```

Profile checks:

| symbol | name | profile caveat | CA overlap with entry~D+180? | calibration use |
|---|---:|---|---:|---|
| 052690 | 한전기술 | no major raw discontinuity; no CA candidate | no | usable |
| 051600 | 한전KPS | no major raw discontinuity; no CA candidate | no | usable |
| 105840 | 우진 | old 2012 CA candidates only | no | usable |

Trigger event:

```text
trigger_event: Czech government selected Korea Hydro & Nuclear Power as preferred bidder for two Dukovany nuclear reactors.
trigger_date: 2024-07-17
entry_rule: next tradable session / first full market reaction close
entry_date: 2024-07-18
```

Reuters reported that South Korea's KHNP was selected by the Czech government as preferred bidder on 2024-07-17, with contract details still to be finalized and substantial stock gains among Korean nuclear-related names. Reuters later reported the appeal / anti-monopoly watchdog process in October 2024, confirming the legal-delay aspect of the archetype.

---

## 3. Case path summary

### 3.1 052690 한전기술 — counterexample with same-day price-only 4B overlay

```yaml
case_id: C04_052690_2024-07-18_CZECH_NUCLEAR_PREFERRED_BIDDER_PROJECT_SCOPE_DELAY
symbol: "052690"
name: "한전기술"
trigger_type: Stage2-FalsePositive-Candidate
entry_date: 2024-07-18
entry_price: 82000
entry_basis: close
same_day_event_high: 98100
same_day_event_high_vs_entry: 19.63%
post_close_30d_mfe_high: 83200
post_close_30d_mfe_pct: 1.46%
post_close_30d_mae_low: 61600
post_close_30d_mae_pct: -24.88%
post_close_180d_mfe_high: 83200
post_close_180d_mfe_pct: 1.46%
post_close_180d_mae_low: 49800
post_close_180d_mae_pct: -39.27%
classification: counterexample
local_4b_overlay: true
hard_4c_candidate: false
calibration_usable: true
```

Interpretation:

한전기술 is the cleanest “headline-to-engineering-scope” stress test.  
The same-day candle proves that the headline was recognized by the market: 2024-07-18 traded from 80,700 to 98,100 and closed at 82,000. But after a close-based entry, the forward path did not validate Stage2-Actionable quality. The stock quickly fell to 61,600 on 2024-08-05 and later to 49,800 on 2025-04-09.

The signal therefore looks like a policy-event 4B burst, not a clean C04 Green. The missing bridge is direct engineering scope, signed terms, timing of recognized revenue, and margin/EPS visibility.

### 3.2 051600 한전KPS — positive control, but delayed and bridge-dependent

```yaml
case_id: C04_051600_2024-07-18_CZECH_NUCLEAR_PREFERRED_BIDDER_SERVICE_RECURRING_BRIDGE
symbol: "051600"
name: "한전KPS"
trigger_type: Stage2-Actionable
entry_date: 2024-07-18
entry_price: 38900
entry_basis: close
same_day_event_high: 47450
same_day_event_high_vs_entry: 21.98%
post_close_30d_mfe_high: 43500
post_close_30d_mfe_pct: 11.83%
post_close_30d_mae_low: 35850
post_close_30d_mae_pct: -7.84%
post_close_180d_mfe_high: 48100
post_close_180d_mfe_pct: 23.65%
post_close_180d_mae_low: 35850
post_close_180d_mae_pct: -7.84%
classification: positive
local_4b_overlay: false
hard_4c_candidate: false
calibration_usable: true
```

Interpretation:

한전KPS behaves differently from the pure engineering/project-scope names.  
After the same Czech event, the stock absorbed the volatility better: 2024-08-05 low was 35,850 versus a 38,900 entry, then the path recovered to 48,100 by 2025-01-24.

This is not a pure headline score. The better fit is “nuclear policy event plus service/maintenance cash-flow bridge.” For this case, Stage2-Actionable is defensible, but Stage3-Green still needs evidence of recurring service scope, backlog/order conversion, and margin/EPS carry rather than a one-day Czech-project beta.

### 3.3 105840 우진 — hard-4C candidate / instrument-theme false positive

```yaml
case_id: C04_105840_2024-07-18_CZECH_NUCLEAR_PREFERRED_BIDDER_INSTRUMENT_THEME_FADE
symbol: "105840"
name: "우진"
trigger_type: Stage2-FalsePositive-Candidate
entry_date: 2024-07-18
entry_price: 9300
entry_basis: close
same_day_event_high: 10950
same_day_event_high_vs_entry: 17.74%
post_close_30d_mfe_high: 9320
post_close_30d_mfe_pct: 0.22%
post_close_30d_mae_low: 7120
post_close_30d_mae_pct: -23.44%
post_close_180d_mfe_high: 9320
post_close_180d_mfe_pct: 0.22%
post_close_180d_mae_low: 6000
post_close_180d_mae_pct: -35.48%
classification: counterexample
local_4b_overlay: true
hard_4c_candidate: true
calibration_usable: true
```

Interpretation:

우진 is the guardrail case.  
The stock was clearly pulled into the nuclear policy basket on the event day, but after the close-based entry it produced almost no usable forward MFE and a large drawdown. The pattern says “nuclear instrument theme” is too remote unless the evidence shows named instrument orders, delivery timing, or revenue conversion.

This should not be scored as Stage2-Actionable merely because the headline is large and nuclear-related. It belongs in Watch / 4B burst / possible 4C fade unless non-price evidence appears.

---

## 4. Residual error

### Residual error found

The calibrated profile already blocks price-only blowoff, but C04 still has a more specific residual:

```text
A nuclear policy/project headline can produce the same first-day price burst across engineering, service, component, and instrument names.
But the correct E2R classification depends on where the economic bridge sits:
  - direct EPC / design / engineering scope
  - recurring O&M / service exposure
  - named component/instrument order
  - signed contract timing
  - legal challenge / final-contract delay risk
  - OP/EPS bridge
```

Without this bridge, the model can over-promote C04 cases because the headline appears “big enough.”

### Mechanism

The Czech tender headline is like hearing that a city will build a new airport.  
The architect, the runway contractor, the security company, the maintenance vendor, and a supplier of small sensors can all trade up on the announcement. But only some of them actually receive the work, and not necessarily on the same timeline. The first candle is not the contract.

---

## 5. Shadow rule candidate

```yaml
shadow_rule_candidate:
  id: C04_NUCLEAR_PROJECT_POLICY_EVENT_TO_CONTRACT_SCOPE_BRIDGE_GUARD
  scope: canonical_archetype_specific
  applies_to:
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  rule_type: stage_promotion_guard
  do_not_apply_to_production_now: true
  rationale: >
    Nuclear policy / export project headlines create large first-day sector moves,
    but forward returns diverge by direct contract scope and legal/final-contract timing.
  guard:
    if:
      - evidence_family in ["nuclear_policy_headline", "preferred_bidder", "MOU", "government_export_goal"]
      - direct_company_scope_missing == true
    then:
      - max_stage: Stage2-Watch
      - block_stage3_green: true
      - require_non_price_bridge_for_stage2_actionable: true
  positive_bridge_terms:
    - signed_contract_or_binding_scope
    - direct_project_scope_to_company
    - backlog_or_order_conversion
    - O&M_or_recurring_service_revenue
    - named_component_or_instrument_order
    - legal_appeal_cleared_or_contract_finalized
    - margin_or_EPS_revision_visibility
  negative_guard_terms:
    - preferred_bidder_only
    - final_contract_not_signed
    - legal_appeal_pending
    - generic_nuclear_theme
    - same_day_gap_only
    - no company-specific revenue bridge
  evidence_from_cases:
    positive:
      - 051600
    counterexamples:
      - 052690
      - 105840
```

---

## 6. Machine-readable rows

### 6.1 trigger rows

```jsonl
{"row_type":"trigger","scheduled_round":"R11","scheduled_loop":89,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_EVENT_TO_CONTRACT_EXECUTION_BRIDGE","symbol":"052690","name":"한전기술","trigger_date":"2024-07-17","entry_date":"2024-07-18","entry_price":82000,"trigger_type":"Stage2-FalsePositive-Candidate","classification":"counterexample","local_4b_overlay":true,"hard_4c_candidate":false,"calibration_usable":true,"same_archetype_new_symbol":true}
{"row_type":"trigger","scheduled_round":"R11","scheduled_loop":89,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_EVENT_TO_CONTRACT_EXECUTION_BRIDGE","symbol":"051600","name":"한전KPS","trigger_date":"2024-07-17","entry_date":"2024-07-18","entry_price":38900,"trigger_type":"Stage2-Actionable","classification":"positive","local_4b_overlay":false,"hard_4c_candidate":false,"calibration_usable":true,"same_archetype_new_symbol":true}
{"row_type":"trigger","scheduled_round":"R11","scheduled_loop":89,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_NUCLEAR_PREFERRED_BIDDER_POLICY_EVENT_TO_CONTRACT_EXECUTION_BRIDGE","symbol":"105840","name":"우진","trigger_date":"2024-07-17","entry_date":"2024-07-18","entry_price":9300,"trigger_type":"Stage2-FalsePositive-Candidate","classification":"counterexample","local_4b_overlay":true,"hard_4c_candidate":true,"calibration_usable":true,"same_archetype_new_symbol":true}
```

### 6.2 price-path rows

```jsonl
{"row_type":"price_path","symbol":"052690","entry_date":"2024-07-18","entry_price":82000,"same_day_event_high":98100,"same_day_event_high_pct":19.63,"mfe_30d_high":83200,"mfe_30d_pct":1.46,"mae_30d_low":61600,"mae_30d_pct":-24.88,"mfe_180d_high":83200,"mfe_180d_pct":1.46,"mae_180d_low":49800,"mae_180d_pct":-39.27}
{"row_type":"price_path","symbol":"051600","entry_date":"2024-07-18","entry_price":38900,"same_day_event_high":47450,"same_day_event_high_pct":21.98,"mfe_30d_high":43500,"mfe_30d_pct":11.83,"mae_30d_low":35850,"mae_30d_pct":-7.84,"mfe_180d_high":48100,"mfe_180d_pct":23.65,"mae_180d_low":35850,"mae_180d_pct":-7.84}
{"row_type":"price_path","symbol":"105840","entry_date":"2024-07-18","entry_price":9300,"same_day_event_high":10950,"same_day_event_high_pct":17.74,"mfe_30d_high":9320,"mfe_30d_pct":0.22,"mae_30d_low":7120,"mae_30d_pct":-23.44,"mfe_180d_high":9320,"mfe_180d_pct":0.22,"mae_180d_low":6000,"mae_180d_pct":-35.48}
```

### 6.3 aggregate row

```json
{
  "row_type": "aggregate",
  "scheduled_round": "R11",
  "scheduled_loop": 89,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "new_independent_case_count": 3,
  "same_archetype_new_symbol_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "local_4b_overlay_case_count": 2,
  "hard_4c_candidate_count": 1,
  "calibration_usable_trigger_count": 3,
  "residual_error_found": true,
  "rule_candidate": "C04_NUCLEAR_PROJECT_POLICY_EVENT_TO_CONTRACT_SCOPE_BRIDGE_GUARD",
  "do_not_propose_new_weight_delta": true,
  "next_round": "R12",
  "next_loop": 89
}
```

---

## 7. Deferred Coding Agent Handoff Prompt

```text
Goal:
  Add a C04-specific shadow validation rule, not production scoring, to distinguish
  nuclear policy/project headline beta from company-specific contract conversion.

Inputs:
  - canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - new cases:
      052690 / 2024-07-18 / counterexample / local 4B overlay
      051600 / 2024-07-18 / positive control
      105840 / 2024-07-18 / hard 4C candidate

Implementation sketch:
  1. Add a shadow-only feature group:
       nuclear_project_scope_bridge_score
       legal_delay_or_final_contract_risk_flag
       same_day_policy_blowoff_flag
  2. For C04:
       if preferred_bidder/MOU/government headline exists but direct company scope is missing:
           block Stage3-Green
           cap at Stage2-Watch unless a non-price bridge is present
  3. Positive bridge terms:
       signed contract, direct project scope, O&M/service revenue, named component order,
       backlog conversion, legal appeal cleared, OP/EPS revision
  4. Negative terms:
       preferred bidder only, legal appeal pending, final contract not signed,
       generic nuclear theme, same-day gap only
  5. Run only as shadow profile validation.
  6. Do not change production weights until batch review across R11/R12/R13 confirms.
```

---

## 8. Final scheduler state

```text
completed_round: R11
completed_loop: 89
next_round: R12
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
```
