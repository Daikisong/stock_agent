# E2R Stock-Web V12 Residual Research — R13 Loop 89 Cross-Archetype Stage2 False-Positive Review

```yaml
artifact_type: e2r_stock_web_v12_residual_research
scheduled_round: R13
scheduled_loop: 89
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: R13_PF_NUCLEAR_EDUCATION_POLICY_STAGE2_FALSE_POSITIVE_BRIDGE_REVIEW

review_only: true
new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

review_trigger_count: 9
reviewed_original_canonical_count: 3
reviewed_original_canonical_ids:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT

positive_control_count: 2
stage2_false_positive_or_high_mae_count: 7
local_4b_watch_count: 4
hard_4c_candidate_count: 2

loop_contribution_label: holdout_validation_passed
residual_type: cross_archetype_policy_headline_false_positive_guard
do_not_propose_new_weight_delta: true
production_scoring_change_allowed: false

completed_round: R13
completed_loop: 89
next_round: R1
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 0. Execution boundary

This file follows the v12 round scheduler as a **review-only R13** artifact.

R13 is not a normal single-sector discovery round. It is a cross-archetype checkpoint for false positives, high-MAE cases, 4B/4C routes, accounting trust, price validation, and rule hygiene.

The reviewed source cases are the immediately preceding loop-89 outputs:

1. `R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`
2. `R11 / C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY`
3. `R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT`

No new case should be added to the No-Repeat ledger from this file. The nine rows below are **holdout review rows** over already-generated loop-89 case material.

---

## 1. Price data basis

```yaml
price_atlas_repo: Songdaiki/stock-web
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
default_price_basis: tradable_raw
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
tradable_row_count: 14354401
corporate_action_rule: contaminated windows blocked by default
```

All reviewed rows use 1D tradable OHLCV rows from stock-web. Corporate-action candidate windows were checked at profile level in the original round files. The reviewed 2024~2025 windows below are not using raw/untradable rows for calibration.

---

## 2. R13 thesis

Across C30, C04, and C31, the failure mode is structurally similar:

> A broad policy/event headline opens the gate, the first price candle shouts, but the bridge to company-specific economics is missing.

This is a classic E2R residual: the market initially treats the headline as if it were a signed contract, cash collection, utilization recovery, or recurring revenue. But the actual rerating only survives when a firm-level conversion bridge appears.

For this R13 checkpoint, the invariant is:

```text
Broad policy headline is not enough.

Require at least one company-specific conversion bridge before Stage2-Actionable,
and require multiple durable bridges before Stage3-Green.
```

Applicable bridge families:

```text
C30 PF / construction:
  refinancing
  PF exposure reduction
  cash collection
  impaired-project ringfence
  order backlog to margin bridge
  balance-sheet repair

C04 nuclear:
  named scope
  final contract / binding terms
  legal or antitrust clearance
  service or engineering revenue timing
  backlog-to-revenue bridge
  vendor-specific margin bridge

C31 education policy:
  product fit
  actual enrollment / seat conversion
  paid course conversion
  ARPU / retention
  revenue / OP / EPS bridge
```

---

## 3. Reviewed trigger table

| original canonical | symbol | name | trigger date | entry date | entry price | observed path | R13 route |
|---|---:|---|---:|---:|---:|---|---|
| C30 | 000720 | 현대건설 | 2025-01-22 | 2025-01-22 | 28,450 | 2025-02-18 high 37,550; 2025-07-01 high 83,900 | positive control + local 4B watch |
| C30 | 003070 | 코오롱글로벌 | 2024-06-26 | 2024-06-26 | 13,630 | 2024-06-27 high 15,200; 2024-08-05 low 8,500 | high-MAE false positive |
| C30 | 002780 | 진흥기업 | 2024-06-26 | 2024-06-26 | 884 | 2024-06-26 high 1,009; 2024-08-05 low 797 | shallow false positive |
| C04 | 052690 | 한전기술 | 2024-07-18 | 2024-07-18 | 82,000 | same-day high 98,100; 2024-08-05 low 61,600; 2025-04-09 low 49,800 | local 4B then high-MAE false positive |
| C04 | 051600 | 한전KPS | 2024-07-18 | 2024-07-18 | 38,900 | 2025-01-24 high 48,100 | positive control |
| C04 | 105840 | 우진 | 2024-07-18 | 2024-07-18 | 9,300 | same-day high 10,950; 2024-08-05 low 7,120; 2025-04-09 low 6,000 | hard 4C candidate |
| C31 | 100220 | 비상교육 | 2024-02-06 | 2024-02-06 | 5,060 | 2024-02-21 high 8,420; 2024-08-05 low 3,990 | price-positive but Green-blocked / local 4B |
| C31 | 215200 | 메가스터디교육 | 2024-02-06 | 2024-02-06 | 63,100 | 2024-02-08 high 68,900; 2024-09-23 low 42,450 | high-MAE false positive |
| C31 | 095720 | 웅진씽크빅 | 2024-02-06 | 2024-02-06 | 2,475 | 2024-02-21 high 2,780; 2024-09-09 low 1,640 | hard 4C candidate |

---

## 4. Case-level review

### 4.1 C30 — Construction PF / balance-sheet break

#### 000720 현대건설 — positive control with local 4B watch

```yaml
symbol: "000720"
name: "현대건설"
original_canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
entry_date: 2025-01-22
entry_price: 28450
r13_route: positive_control_with_local_4b_watch
calibration_usable: true
```

Price path:

```text
2025-01-22 close: 28,450
2025-02-18 high: 37,550
2025-07-01 high: 83,900
```

R13 interpretation:

현대건설은 PF sector liquidity headline만으로 설명하기보다, later company-specific re-rating evidence가 붙은 positive control로 남기는 편이 맞다. 다만 price path가 매우 빠르게 커졌기 때문에 4B proximity guard는 필요하다. Stage3-Green은 policy beta가 아니라 company-specific order/margin/cash-collection bridge가 붙을 때만 허용한다.

R13 rule implication:

```text
C30 Green route:
  policy_support_headline + company_specific_backlog_or_margin_bridge + balance_sheet_repair_visibility
```

#### 003070 코오롱글로벌 — short MFE, deep MAE

```yaml
symbol: "003070"
name: "코오롱글로벌"
original_canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
entry_date: 2024-06-26
entry_price: 13630
r13_route: stage2_false_positive_high_mae
calibration_usable: true
```

Price path:

```text
2024-06-26 close: 13,630
2024-06-27 high: 15,200
2024-08-05 low: 8,500
```

R13 interpretation:

코오롱글로벌은 policy/liquidity headline이 초기 반등을 만들 수 있지만, 회사별 PF exposure repair와 cash collection bridge가 없으면 Stage2-Actionable을 오래 열 수 없다는 검문 사례다. A single relief candle is not a balance-sheet repair.

R13 rule implication:

```text
If C30 trigger is mostly sector liquidity / policy relief:
  cap at Watch or Stage2-FalsePositive-Candidate
  unless issuer-specific PF reduction/refinancing/cash collection is verified
```

#### 002780 진흥기업 — shallow price-only beta

```yaml
symbol: "002780"
name: "진흥기업"
original_canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
entry_date: 2024-06-26
entry_price: 884
r13_route: shallow_mfe_false_positive_candidate
calibration_usable: true
```

Price path:

```text
2024-06-26 close: 884
2024-06-26 high: 1,009
2024-08-05 low: 797
```

R13 interpretation:

진흥기업은 small-cap construction beta가 policy liquidity headline에 따라 튈 수 있음을 보여준다. 그러나 MFE가 sustained rerating으로 이어지지 않고 MAE도 남았다. The signal is a spark, not a furnace.

R13 rule implication:

```text
Small-cap construction beta without firm-specific repair evidence:
  never Stage3-Green
  only narrative-only / local 4B watch / false-positive calibration row
```

---

### 4.2 C04 — Nuclear policy / project legal delay

#### 052690 한전기술 — project headline without final-contract bridge

```yaml
symbol: "052690"
name: "한전기술"
original_canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
entry_date: 2024-07-18
entry_price: 82000
r13_route: local_4b_then_high_mae_false_positive
calibration_usable: true
```

Price path:

```text
2024-07-18 close: 82,000
2024-07-18 high: 98,100
2024-08-05 low: 61,600
2025-04-09 low: 49,800
```

R13 interpretation:

한전기술은 nuclear export headline의 strongest first-order receiver처럼 보였지만, final contract / legal clearance / revenue timing bridge가 붙기 전에는 Stage3-Green까지 올리면 안 된다. Project headline이 실제 매출로 내려오기 전까지는 마치 설계도 위의 고층건물이다. 그림은 크지만 아직 현금흐름이 아니다.

R13 rule implication:

```text
C04 preferred_bidder_event:
  block Green if final_contract_status != signed_or_legally_clear
  downgrade to 4B-watch if same-day or 5D spike outruns contract evidence
```

#### 051600 한전KPS — service bridge positive control

```yaml
symbol: "051600"
name: "한전KPS"
original_canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
entry_date: 2024-07-18
entry_price: 38900
r13_route: positive_control
calibration_usable: true
```

Price path:

```text
2024-07-18 close: 38,900
2025-01-24 high: 48,100
```

R13 interpretation:

한전KPS is the useful positive control because the service/maintenance angle is less dependent on one explosive EPC-like project headline. It supports a more conservative positive route: nuclear policy + recurring service economics + less severe headline blowoff.

R13 rule implication:

```text
C04 service/maintenance route can remain Stage2-Actionable:
  if recurring service bridge or O&M visibility is present
  and if initial spike remains below 4B blowoff threshold
```

#### 105840 우진 — instrument-theme hard 4C candidate

```yaml
symbol: "105840"
name: "우진"
original_canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
entry_date: 2024-07-18
entry_price: 9300
r13_route: hard_4c_candidate
calibration_usable: true
```

Price path:

```text
2024-07-18 close: 9,300
2024-07-18 high: 10,950
2024-08-05 low: 7,120
2025-04-09 low: 6,000
```

R13 interpretation:

우진은 "원전 부품/계측기 theme receiver"가 preferred-bidder headline에 반응할 수 있지만, named scope and revenue bridge 없이 지속 rerating으로 연결되지 않는 경우다.

R13 rule implication:

```text
Nuclear component/instrument names:
  require named scope / order / revenue bridge
  otherwise C04 headline exposure routes to 4C-candidate after failed MFE persistence
```

---

### 4.3 C31 — Policy / subsidy / legislation event: medical-school quota education branch

#### 100220 비상교육 — price-positive, Green-blocked

```yaml
symbol: "100220"
name: "비상교육"
original_canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
entry_date: 2024-02-06
entry_price: 5060
r13_route: price_positive_but_green_blocked_local_4b
calibration_usable: true
```

Price path:

```text
2024-02-06 close: 5,060
2024-02-21 high: 8,420
2024-08-05 low: 3,990
```

R13 interpretation:

비상교육은 policy theme의 raw reflexivity를 잘 보여준다. 의대 정원 확대 headline은 교육주 묶음을 움직였지만, 제품 fit, 실제 수강 전환, revenue bridge 없이 Stage3-Green으로 가면 안 된다. 테마는 문을 열었지만, 매출이 방에 들어오지는 않았다.

R13 rule implication:

```text
C31 education policy:
  initial theme spike can be positive price evidence
  but Green requires enrollment/ARPU/paid-course conversion evidence
```

#### 215200 메가스터디교육 — policy mismatch counterexample

```yaml
symbol: "215200"
name: "메가스터디교육"
original_canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
entry_date: 2024-02-06
entry_price: 63100
r13_route: high_mae_false_positive
calibration_usable: true
```

Price path:

```text
2024-02-06 close: 63,100
2024-02-08 high: 68,900
2024-09-23 low: 42,450
```

R13 interpretation:

메가스터디교육은 "교육 대장주"라는 label이 policy beta를 받을 수 있지만, 의대 정원 확대가 곧바로 해당 상장사의 paid-course growth와 OP bridge를 의미하지는 않는다는 반례다.

R13 rule implication:

```text
Large incumbent education platform:
  policy headline alone is insufficient
  require product-specific conversion bridge before Stage2-Actionable
```

#### 095720 웅진씽크빅 — hard 4C candidate

```yaml
symbol: "095720"
name: "웅진씽크빅"
original_canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
entry_date: 2024-02-06
entry_price: 2475
r13_route: hard_4c_candidate
calibration_usable: true
```

Price path:

```text
2024-02-06 close: 2,475
2024-02-21 high: 2,780
2024-09-09 low: 1,640
```

R13 interpretation:

웅진씽크빅은 generic education label이 정책 이벤트와 맞물려도, product fit and revenue conversion이 없으면 durable rerating이 아니라 liquidity fade로 끝날 수 있음을 보여준다.

R13 rule implication:

```text
Generic education label + policy headline:
  if no product fit / paid conversion / OP bridge
  route to C31 4C-candidate or false-positive row
```

---

## 5. Cross-archetype residual rule candidate

### 5.1 New shared guard candidate

```yaml
rule_candidate_id: V12_R13_POLICY_HEADLINE_TO_FIRM_BRIDGE_GUARD
scope:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
trigger_family:
  - policy_headline
  - preferred_bidder
  - sector_liquidity_support
  - subsidy_or_quota_event
  - legal_or_regulatory_event
action:
  - prevent Stage3-Green from headline-only evidence
  - require firm-specific bridge for Stage2-Actionable
  - route price-only spike to local 4B watch
  - route failed bridge + high-MAE path to 4C candidate
production_change: false
handoff_only: true
```

### 5.2 Proposed scoring behavior for later coding agent

```python
def policy_headline_to_firm_bridge_guard(case):
    if case.canonical_archetype_id not in {
        "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
        "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
        "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
    }:
        return None

    headline_only = case.has_policy_or_event_headline and not case.has_company_specific_bridge

    if headline_only:
        case.block_stage3_green = True
        case.stage2_actionable_cap_reason = "policy_headline_without_firm_specific_bridge"

        if case.price_spike_5d_or_30d and not case.non_price_confirmation:
            case.add_overlay("local_4b_watch")

        if case.high_mae_or_failed_mfe_persistence:
            case.route = "Stage2-FalsePositive-Candidate_or_4C"

    return case
```

### 5.3 Archetype-specific bridge requirements

```yaml
C30_required_bridge_any_of:
  - PF_exposure_reduction
  - refinancing_success
  - cash_collection
  - impaired_project_ringfence
  - margin_or_order_conversion
  - balance_sheet_repair_visibility

C04_required_bridge_any_of:
  - final_contract_signed
  - legal_clearance
  - named_project_scope
  - order_or_service_revenue_timing
  - backlog_to_revenue_bridge

C31_required_bridge_any_of:
  - product_fit_to_policy
  - actual_enrollment_or_paid_user_conversion
  - ARPU_or_retention_improvement
  - revenue_OP_EPS_bridge
```

---

## 6. Machine-readable rows

```jsonl
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":89,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","C31_POLICY_SUBSIDY_LEGISLATION_EVENT"],"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":2,"stage2_false_positive_or_high_mae_count":7,"local_4b_watch_count":4,"hard_4c_candidate_count":2,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"review_case","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"000720","name":"현대건설","trigger_date":"2025-01-22","entry_date":"2025-01-22","entry_price":28450,"r13_route":"positive_control_with_local_4b_watch","stage3_green_allowed_only_if":"company_specific_order_margin_cash_collection_bridge","calibration_usable":true}
{"row_type":"review_case","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"003070","name":"코오롱글로벌","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":13630,"r13_route":"stage2_false_positive_high_mae","stage3_green_allowed":false,"calibration_usable":true}
{"row_type":"review_case","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002780","name":"진흥기업","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":884,"r13_route":"shallow_mfe_false_positive_candidate","stage3_green_allowed":false,"calibration_usable":true}
{"row_type":"review_case","original_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"052690","name":"한전기술","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":82000,"r13_route":"local_4b_then_high_mae_false_positive","stage3_green_allowed":false,"calibration_usable":true}
{"row_type":"review_case","original_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"051600","name":"한전KPS","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":38900,"r13_route":"positive_control","stage3_green_allowed_only_if":"service_or_OandM_revenue_bridge","calibration_usable":true}
{"row_type":"review_case","original_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"105840","name":"우진","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":9300,"r13_route":"hard_4c_candidate","stage3_green_allowed":false,"calibration_usable":true}
{"row_type":"review_case","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"100220","name":"비상교육","trigger_date":"2024-02-06","entry_date":"2024-02-06","entry_price":5060,"r13_route":"price_positive_but_green_blocked_local_4b","stage3_green_allowed":false,"calibration_usable":true}
{"row_type":"review_case","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"215200","name":"메가스터디교육","trigger_date":"2024-02-06","entry_date":"2024-02-06","entry_price":63100,"r13_route":"high_mae_false_positive","stage3_green_allowed":false,"calibration_usable":true}
{"row_type":"review_case","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"095720","name":"웅진씽크빅","trigger_date":"2024-02-06","entry_date":"2024-02-06","entry_price":2475,"r13_route":"hard_4c_candidate","stage3_green_allowed":false,"calibration_usable":true}
{"row_type":"shadow_rule_candidate","rule_candidate_id":"V12_R13_POLICY_HEADLINE_TO_FIRM_BRIDGE_GUARD","scope":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","C31_POLICY_SUBSIDY_LEGISLATION_EVENT"],"action":"block_stage3_green_on_policy_headline_without_firm_specific_bridge; cap_stage2_actionable; route_price_only_spike_to_local_4b_watch; route_failed_bridge_high_mae_to_4c_candidate","production_change":false,"do_not_propose_new_weight_delta":true}
```

---

## 7. Deferred Coding Agent Handoff Prompt

```text
Implement a non-production shadow guard candidate named:

V12_R13_POLICY_HEADLINE_TO_FIRM_BRIDGE_GUARD

Scope:
- C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
- C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
- C31_POLICY_SUBSIDY_LEGISLATION_EVENT

Behavior:
1. Detect policy/event headline-only evidence:
   - PF support / liquidity headline
   - preferred bidder / nuclear export headline
   - quota / subsidy / education policy headline
   - legal/regulatory event headline

2. If no company-specific conversion bridge exists:
   - block Stage3-Green
   - cap Stage2-Actionable or route to Watch
   - add local_4b_watch if price spike is large and non-price evidence is thin
   - route to 4C candidate if high MAE or failed MFE persistence is confirmed

3. Bridge requirements:
   C30:
   - PF exposure reduction
   - refinancing success
   - cash collection
   - impaired project ringfence
   - margin/order conversion
   C04:
   - final contract / binding terms
   - legal clearance
   - named scope
   - order/service revenue timing
   C31:
   - product fit
   - enrollment / paid user conversion
   - ARPU / retention
   - revenue / OP / EPS bridge

4. Keep this as shadow output only.
5. Do not change production scoring weights automatically.
6. Add tests using the nine R13 loop89 review rows:
   - 000720 positive control
   - 003070 false positive
   - 002780 shallow false positive
   - 052690 local 4B + high-MAE false positive
   - 051600 positive control
   - 105840 hard 4C candidate
   - 100220 price-positive but Green-blocked
   - 215200 high-MAE false positive
   - 095720 hard 4C candidate
```

---

## 8. Final status

```yaml
completed_round: R13
completed_loop: 89
next_round: R1
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
artifact_status: complete
```
