# E2R v12 Residual Research — R1 Loop 90 / L1 / C03

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R1
scheduled_loop: 90
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_BACKLOG_CONTRACT_SCOPE_VS_GEOPOLITICAL_PRICE_ONLY_THEME

current_default_profile_proxy: e2r_2_1_stock_web_calibrated
previous_baseline_reference: e2r_2_0_baseline
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
soft_repeat_symbol_count: 0
positive_case_count: 2
counterexample_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 90
next_round: R2
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Execution boundary

This file is a standalone historical calibration / sector-archetype residual research artifact.

It does **not** perform live stock discovery, portfolio recommendation, brokerage/API work, `stock_agent` code inspection, production scoring patching, or price-route exploration.

The only live data dependency used here is `Songdaiki/stock-web` as the 1D OHLC price atlas.

---

## 2. Scheduler resolution

The previous completed artifact was `R13 / loop 89`, so the v12 round cycle resets to:

```text
R13 loop 89 completed -> R1 loop 90
```

R1 requires:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

This file uses:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

No round-sector violation.

---

## 3. No-Repeat / coverage check

No-Repeat coverage snapshot for R1-relevant archetypes:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE                 25 rows / 14 symbols
C02_POWER_GRID_DATACENTER_CAPEX                 22 rows / 12 symbols
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG             21 rows / 12 symbols
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY           12 rows / 7 symbols
C05_EPC_MEGA_CONTRACT_MARGIN_GAP                 10 rows / 9 symbols
```

C03 is not the shallowest R1 archetype, but it has not been used in the immediately preceding R1 loop sequence, while loop88 used C05 and loop89 used C02. It also has `4B/4C = 0/0` in the coverage snapshot, so it is a useful place to add export-framework 4B/false-positive guardrails.

Top-covered C03 symbols avoided:

```text
079550, 047810, 065450, 005870, 103140, 003570
```

Selected symbols:

```text
012450 Hanwha Aerospace
064350 Hyundai Rotem
010820 Firstec
```

No selected symbol is in the C03 top-covered list. The third case is deliberately a counterexample / bad-expansion guard: it is defense-theme sensitive but lacks a clear export framework/backlog bridge.

Hard duplicate rule used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All three rows use new C03 symbol-trigger-date combinations.

---

## 4. Price atlas validation

Source:

```text
price_atlas_repo = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

Profile checks:

| symbol | name | profile status | corporate-action overlap in entry~D+180? | calibration use |
|---|---|---|---|---|
| 012450 | Hanwha Aerospace | active_like | no; profile candidates are old historical dates | usable |
| 064350 | Hyundai Rotem | active_like | no; profile candidate 2020-08-14 outside window | usable |
| 010820 | Firstec | active_like | no; profile candidates are old historical dates | usable |

All three cases use tradable shard rows only.

---

## 5. Thesis

C03 captures a very specific defense rerating mechanism:

```text
export framework / named customer / executable contract scope / backlog conversion
```

It should not be triggered by a generic defense label alone.

The mechanism is like a factory loading dock. A headline saying “demand is strong” is noise unless a truck has a named destination, a purchase order, a delivery schedule, and margin visibility. C03 should reward the loaded truck, not the rumor of traffic outside the gate.

The residual issue in the current calibrated profile is:

```text
price-only defense/geopolitical bursts can look like Stage2 acceleration,
while named export-contract winners can legitimately deserve Stage2-Actionable or Green.
```

Therefore, C03 needs a sharper split:

```text
named export contract / framework + company scope + backlog bridge -> allow Stage2-Actionable / Yellow / Green
generic defense tension / supplier label / price spike only -> 4B watch or counterexample, not Green
```

---

## 6. Case set

### Case A — 012450 Hanwha Aerospace

```yaml
symbol: "012450"
name: "Hanwha Aerospace"
trigger_date: "2024-07-09"
entry_date: "2024-07-10"
entry_price: 256500
trigger_type: "Stage3-Green-Candidate"
case_direction: positive_with_local_4b_overlay
evidence_family:
  - named export contract
  - Romania K9/K10 order
  - multi-year delivery / backlog conversion
  - defense export scale economics
```

Evidence interpretation:

Hanwha Aerospace had a clean C03-style bridge: named foreign customer, signed contract, explicit equipment package, delivery horizon, and export backlog context. This is not a generic geopolitical defense move; it is a contract-to-backlog conversion event.

Stock-web path:

```text
entry close: 2024-07-10 = 256,500
near-term peak: 2024-07-30 high = 330,000
local panic low: 2024-08-05 low = 247,000
later 180D-region peak: 2025-03-18 high = 781,000
```

Approximate path metrics:

```json
{
  "symbol": "012450",
  "entry_date": "2024-07-10",
  "entry_price": 256500,
  "mfe_30d_pct": 28.7,
  "mae_30d_pct": -3.7,
  "mfe_90d_pct": 54.0,
  "mae_90d_pct": -3.7,
  "mfe_180d_pct": 204.5,
  "mae_180d_pct": -3.7,
  "peak_price_observed": 781000,
  "peak_date_observed": "2025-03-18",
  "max_drawdown_after_peak_pct": "material but not thesis-breaking within early window",
  "calibration_usable": true
}
```

Stage interpretation:

```text
baseline_current_proxy: should allow Stage3-Green only because non-price evidence is unusually clean.
residual guard: once MFE exceeds +50% without fresh estimate/backlog conversion evidence, local 4B watch should activate.
```

---

### Case B — 064350 Hyundai Rotem

```yaml
symbol: "064350"
name: "Hyundai Rotem"
trigger_date: "2024-07-10"
entry_date: "2024-07-10"
entry_price: 41550
trigger_type: "Stage2-Actionable"
case_direction: delayed_positive_with_local_4b_overlay
evidence_family:
  - K2 export framework
  - Poland/Europe defense partnership optionality
  - tank production backlog visibility
  - later contract validation
```

Evidence interpretation:

Hyundai Rotem was not as clean as Hanwha Aerospace at the 2024 trigger point. The core evidence was defense-export framework and follow-on order expectation rather than immediate final-contract conversion. The later K2 contract evidence supports the route ex post, but the 2024 trigger should be treated as Actionable/Yellow rather than instant Green.

Stock-web path:

```text
entry close: 2024-07-10 = 41,550
30D-region peak: 2024-08-14 high = 54,800
panic low: 2024-08-05 low = 41,000
2025 acceleration peak: 2025-03-19 high = 116,800
```

Approximate path metrics:

```json
{
  "symbol": "064350",
  "entry_date": "2024-07-10",
  "entry_price": 41550,
  "mfe_30d_pct": 31.9,
  "mae_30d_pct": -1.3,
  "mfe_90d_pct": 38.4,
  "mae_90d_pct": -1.3,
  "mfe_180d_pct": 181.1,
  "mae_180d_pct": -1.3,
  "peak_price_observed": 116800,
  "peak_date_observed": "2025-03-19",
  "calibration_usable": true
}
```

Stage interpretation:

```text
baseline_current_proxy: Stage2-Actionable or Stage3-Yellow is defensible.
residual guard: delay Green until final order / named customer / production allocation bridge is confirmed.
```

This is a useful C03 positive case, but also a warning: export-framework optionality can be real and profitable while still not satisfying Green at entry.

---

### Case C — 010820 Firstec

```yaml
symbol: "010820"
name: "Firstec"
trigger_date: "2024-01-16"
entry_date: "2024-01-17"
entry_price: 3765
trigger_type: "Stage2-FalsePositive-Candidate"
case_direction: counterexample_hard_4c_candidate
evidence_family:
  - generic defense/geopolitical tension
  - no named export framework
  - no backlog conversion
  - price-only burst
```

Evidence interpretation:

Firstec is included as a C03 bad-expansion guard, not as a positive C03 case. It may react to defense tension and drone/weapon-system narratives, but that is not the same as a named export framework or backlog conversion. The C03 router should not let this kind of signal climb to Green.

Stock-web path:

```text
entry close: 2024-01-17 = 3,765
same-day high: 2024-01-17 = 3,990
later drawdown low: 2024-09-09 low = 2,555
```

Approximate path metrics:

```json
{
  "symbol": "010820",
  "entry_date": "2024-01-17",
  "entry_price": 3765,
  "mfe_30d_pct": 6.0,
  "mae_30d_pct": -15.1,
  "mfe_90d_pct": 6.0,
  "mae_90d_pct": -15.1,
  "mfe_180d_pct": 6.0,
  "mae_180d_pct": -32.1,
  "peak_price_observed": 3990,
  "peak_date_observed": "2024-01-17",
  "calibration_usable": true
}
```

Stage interpretation:

```text
baseline_current_proxy: should be blocked from positive Stage2/Green by price-only blowoff guard.
residual guard: generic defense tension is not a C03 evidence bridge.
```

---

## 7. Score-return alignment

| case | expected calibrated stage | observed path | alignment |
|---|---|---|---|
| Hanwha Aerospace | Stage3-Green allowed, with local 4B after strong MFE | strong 30D/90D/180D MFE, limited early MAE | good |
| Hyundai Rotem | Stage2-Actionable / Yellow first; Green only after stronger contract bridge | strong delayed path, large 2025 acceleration | good if not over-promoted at entry |
| Firstec | blocked / counterexample / hard 4C candidate | shallow MFE and deep MAE | good if price-only guard blocks it |

Residual error found:

```text
C03 needs to separate:
1. contract-grade export backlog conversion
2. framework / negotiation optionality
3. generic defense tension
```

Current global rules already block price-only blowoff in principle, but C03 needs its own evidence ladder so that defense-theme suppliers do not inherit the same score as named export contract winners.

---

## 8. Proposed C03 shadow rule candidate

Do not implement now. Shadow rule only.

```yaml
shadow_rule_id: C03_EXPORT_FRAMEWORK_BACKLOG_CONVERSION_LADDER_V1
scope:
  large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
  canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
rule_type: sector_archetype_specific_stage_gate
production_scoring_changed: false
```

Rule ladder:

```text
C03_GREEN_ALLOWED only if:
  named_foreign_customer == true
  and contract_or_preferred_bidder_scope_is_specific == true
  and product_system_scope_is_named == true
  and backlog_or_delivery_schedule_visibility == true
  and margin_or_revenue_conversion_bridge >= moderate
  and price_only_blowoff == false

C03_YELLOW_ALLOWED if:
  export_framework_or_negotiation_is_specific == true
  and company_is_named_supplier == true
  and likely contract size / production allocation is visible
  but final contract or revenue timing remains pending

C03_BLOCK_POSITIVE_STAGE if:
  evidence is mainly geopolitical tension
  or defense-sector label only
  or price/volume spike without named customer
  or no backlog / order / delivery / margin bridge
```

Suggested component adjustments, shadow only:

```json
{
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "positive_contract_bridge_bonus_candidate": 1.5,
  "named_customer_and_scope_bonus_candidate": 1.0,
  "framework_without_final_contract_green_cap": "Stage3-Yellow",
  "generic_defense_theme_green_block": true,
  "price_only_defense_burst_route": "Stage2-FalsePositive-Candidate_or_4C"
}
```

---

## 9. Machine-readable rows

### 9.1 case rows

```jsonl
{"row_type":"case","scheduled_round":"R1","scheduled_loop":90,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_CONTRACT_SCOPE_VS_GEOPOLITICAL_PRICE_ONLY_THEME","symbol":"012450","name":"Hanwha Aerospace","case_direction":"positive_with_local_4b_overlay","trigger_type":"Stage3-Green-Candidate","trigger_date":"2024-07-09","entry_date":"2024-07-10","entry_price":256500,"calibration_usable":true}
{"row_type":"case","scheduled_round":"R1","scheduled_loop":90,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_CONTRACT_SCOPE_VS_GEOPOLITICAL_PRICE_ONLY_THEME","symbol":"064350","name":"Hyundai Rotem","case_direction":"delayed_positive_with_local_4b_overlay","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-10","entry_date":"2024-07-10","entry_price":41550,"calibration_usable":true}
{"row_type":"case","scheduled_round":"R1","scheduled_loop":90,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_CONTRACT_SCOPE_VS_GEOPOLITICAL_PRICE_ONLY_THEME","symbol":"010820","name":"Firstec","case_direction":"counterexample_hard_4c_candidate","trigger_type":"Stage2-FalsePositive-Candidate","trigger_date":"2024-01-16","entry_date":"2024-01-17","entry_price":3765,"calibration_usable":true}
```

### 9.2 trigger rows

```jsonl
{"row_type":"trigger","symbol":"012450","entry_date":"2024-07-10","entry_price":256500,"mfe_30d_pct":28.7,"mae_30d_pct":-3.7,"mfe_90d_pct":54.0,"mae_90d_pct":-3.7,"mfe_180d_pct":204.5,"mae_180d_pct":-3.7,"peak_price":781000,"peak_date":"2025-03-18","local_4b_watch":true,"hard_4c_candidate":false}
{"row_type":"trigger","symbol":"064350","entry_date":"2024-07-10","entry_price":41550,"mfe_30d_pct":31.9,"mae_30d_pct":-1.3,"mfe_90d_pct":38.4,"mae_90d_pct":-1.3,"mfe_180d_pct":181.1,"mae_180d_pct":-1.3,"peak_price":116800,"peak_date":"2025-03-19","local_4b_watch":true,"hard_4c_candidate":false}
{"row_type":"trigger","symbol":"010820","entry_date":"2024-01-17","entry_price":3765,"mfe_30d_pct":6.0,"mae_30d_pct":-15.1,"mfe_90d_pct":6.0,"mae_90d_pct":-15.1,"mfe_180d_pct":6.0,"mae_180d_pct":-32.1,"peak_price":3990,"peak_date":"2024-01-17","local_4b_watch":false,"hard_4c_candidate":true}
```

### 9.3 score simulation rows

```jsonl
{"row_type":"score_simulation","symbol":"012450","baseline_current_proxy_stage":"Stage3-Green","shadow_rule_stage":"Stage3-Green+local_4B_watch_after_MFE_extension","score_alignment":"pass","reason":"named customer + signed export contract + backlog conversion bridge"}
{"row_type":"score_simulation","symbol":"064350","baseline_current_proxy_stage":"Stage2-Actionable_or_Stage3-Yellow","shadow_rule_stage":"Stage3-Yellow_until_final_contract_bridge","score_alignment":"pass_with_guard","reason":"export framework was real, but final contract evidence lagged the price trigger"}
{"row_type":"score_simulation","symbol":"010820","baseline_current_proxy_stage":"blocked_by_price_only_guard","shadow_rule_stage":"Stage2-FalsePositive-Candidate_or_4C","score_alignment":"pass_if_blocked","reason":"generic defense/geopolitical burst without named export backlog"}
```

### 9.4 aggregate row

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":90,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","case_count":3,"positive_case_count":2,"counterexample_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"residual_contribution_label":"residual_error_found","rule_candidate":"C03_EXPORT_FRAMEWORK_BACKLOG_CONVERSION_LADDER_V1"}
```

### 9.5 shadow weight row

```jsonl
{"row_type":"shadow_weight","rule_id":"C03_EXPORT_FRAMEWORK_BACKLOG_CONVERSION_LADDER_V1","production_scoring_changed":false,"do_not_propose_new_weight_delta":true,"shadow_weight_only":true,"candidate_effect":"separate contract-grade export backlog positives from generic defense-tension false positives"}
```

### 9.6 residual contribution row

```jsonl
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":90,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","contribution":"Adds contract-scope vs price-only defense-theme split; improves C03 4B/4C guard coverage without repeating C02/C05 from prior R1 loops."}
```

---

## 10. Validation scope

Validated:

```text
- R1 / loop90 schedule after R13 / loop89
- R1 -> L1 sector consistency
- C03 coverage and top-covered symbol avoidance
- stock-web manifest basis
- symbol profile presence
- corporate-action candidate non-overlap with entry~D+180 window
- 2024/2025 tradable OHLC rows for the selected triggers
- approximate 30D / 90D / 180D path behavior
```

Not validated in this MD:

```text
- Full exact trading-day indexed 30/90/180 slices by local script
- Analyst consensus revision time series
- OpenDART contract filing text extraction
- Production score implementation
```

Those are intentionally deferred.

---

## 11. Deferred Coding Agent Handoff Prompt

Do not execute in this research session.

```text
You are the deferred coding agent for Songdaiki/stock_agent.

Input artifact:
e2r_stock_web_v12_residual_round_R1_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md

Task:
1. Parse the JSONL rows in sections 9.1~9.6.
2. Add them to the v12 residual research ingestion set as calibration evidence only.
3. Do not modify production scoring directly.
4. Implement no code unless a later batch instruction explicitly asks for it.
5. If implementing later, model the C03_EXPORT_FRAMEWORK_BACKLOG_CONVERSION_LADDER_V1 as a shadow rule candidate:
   - Green requires named customer, contract/preferred-bidder scope, product/system scope, delivery/backlog bridge, and margin/revenue bridge.
   - Framework-only export optionality may permit Stage2-Actionable or Yellow, but should cap Green until final conversion evidence.
   - Generic defense/geopolitical price bursts without named export backlog should be blocked from positive Stage2/Green and routed to false-positive / 4C review.
6. Preserve raw_unadjusted_marcap price-basis caveats and corporate-action contamination rules.
7. Keep production_scoring_changed=false unless a later human-approved patch instruction says otherwise.
```

---

## 12. Final status

```text
completed_round: R1
completed_loop: 90
next_round: R2
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```
