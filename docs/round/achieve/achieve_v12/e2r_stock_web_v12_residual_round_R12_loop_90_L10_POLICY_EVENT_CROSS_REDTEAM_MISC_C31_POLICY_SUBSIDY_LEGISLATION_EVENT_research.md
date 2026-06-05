# E2R Stock-Web v12 Residual Research — R12 / Loop 90

```yaml
scheduled_round: R12
scheduled_loop: 90
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: ECOMMERCE_SETTLEMENT_PROTECTION_PG_ESCROW_REGULATION_BRIDGE_VS_PLATFORM_PAYMENT_DELAY_HEADLINE

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

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 1
delayed_positive_or_relative_resilience_count: 1
counterexample_count: 2
local_burst_but_failed_durability_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 90
next_round: R13
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 90
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy/event or under-covered service/agri branches. This run selects:

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Fine branch:

```text
e-commerce settlement protection / PG escrow regulation / payment-delay policy shock
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rows: 97
symbols: 70
date_range: 2020-01-23~2025-01-17
good/bad S2: 35/25
4B/4C: 5/0
URL pending/proxy: 25/25
top covered symbols:
  013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2)
```

Recent R12 outputs already used:

```text
loop88: value-up policy branch
loop89: medical-school quota / education-service policy branch
```

Selected symbols:

```text
060250 NHN KCP
035600 KG이니시스
377300 카카오페이
```

The selected symbols avoid the C31 top-covered list and avoid the most recent R12 education-service names:

```text
100220, 215200, 095720
```

Hard duplicate key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
060250: same archetype, new symbol, direct PG exposure / merchant-settlement risk branch
035600: same archetype, new symbol, local PG spike without durable regulatory bridge
377300: same archetype, new symbol, wallet/fintech relative-resilience and delayed-positive branch
```

---

## 3. Price-atlas validation

Manifest fields checked:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
active_like_symbol_count: 2,868
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
060250 NHN KCP
  profile: atlas/symbol_profiles/060/060250.json
  first_date: 2002-01-08
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,930
  corporate_action_candidate_dates:
    2005-11-18, 2005-11-29, 2006-02-10, 2007-04-03, 2014-12-16, 2021-12-20
  2024-07 entry~D+180 contamination: none

035600 KG이니시스
  profile: atlas/symbol_profiles/035/035600.json
  first_date: 2002-11-22
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,720
  corporate_action_candidate_dates:
    2003-10-16, 2011-10-21
  2024-07 entry~D+180 contamination: none

377300 카카오페이
  profile: atlas/symbol_profiles/377/377300.json
  first_date: 2021-11-03
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,050
  corporate_action_candidate_dates: none
  2024-07 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-07-26
Qoo10 / TMON / WeMakePrice payment-delay crisis intensifies; vendors cut ties, customers seek refunds, and Korean authorities investigate.

2024-07-29
Korean government prepares financial support for affected small merchants and discusses remedies around delayed marketplace settlements.
```

This is a C31 policy-event branch rather than a pure platform or financial-sector branch because the tradable question is:

```text
merchant-settlement crisis
  -> government support / investigation / future settlement-protection regulation
  -> PG / wallet / platform exposure
  -> who bears settlement, escrow, refund, merchant-credit, and compliance risk?
```

The residual error is that a model may read the crisis as a simple fintech or PG catalyst:

```text
"online payment regulation becomes stricter"
"safe PG/wallet companies gain trust"
"settlement protection policy creates winners"
```

That is too crude.

The correct bridge is:

```text
settlement-delay event
  -> exposure mapping by business model
  -> merchant fund-flow risk
  -> refund / chargeback / working-capital burden
  -> escrow or settlement-period regulation
  -> take-rate / volume / compliance-cost bridge
  -> price path survival
```

A payment-protection headline can be a policy firewall, but every PG/wallet business sits on a different floor of the building.

---

## 5. Case 1 — 060250 NHN KCP

```yaml
case_id: C31_R12L90_060250_2024_07_26
symbol: "060250"
name: "NHN KCP"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: ECOMMERCE_SETTLEMENT_PROTECTION_PG_ESCROW_REGULATION_BRIDGE_VS_PLATFORM_PAYMENT_DELAY_HEADLINE
trigger_date: 2024-07-26
entry_date: 2024-07-26
entry_price_basis: close
entry_price: 9050
classification: hard_4c_candidate_direct_pg_exposure_without_settlement_margin_bridge
calibration_usable: true
```

### Evidence interpretation

NHN KCP is the cleanest direct PG counterexample. A naive model could argue that settlement-protection policy improves trust in established payment processors. The price path says that is not enough.

For a direct PG name, the policy bridge must answer:

```text
does regulation reduce platform credit risk?
does it raise compliance cost?
does it shorten settlement cycles and pressure working capital?
does merchant volume remain intact?
does take-rate improve or compress?
```

Without that bridge, the stock should not be upgraded from a policy headline.

### Price path

Key Stock-Web rows:

```text
2024-07-26: close 9,050
2024-07-29: high 9,140 / close 8,850
2024-07-30: low 8,200 / close 8,270
2024-08-05: low 7,100 / close 7,220
2025-01-23: low 7,100 / close 7,120
2025-02-03: low 6,860 / close 6,960
2025-02-27: high 8,530 / close 8,430
```

Approximate path from entry close:

```text
entry_close: 9,050
180D_peak_high: 9,140
180D_MFE: +1.0%
180D_worst_low: 7,100
180D_MAE: -21.5%
extended_worst_low: 6,860
extended_MAE: -24.2%
```

### Interpretation

This is the hard guardrail case.

```text
Stage2-Watch: allowed as a regulatory-exposure case.
Stage2-Actionable: blocked without company-specific settlement / take-rate / cost bridge.
Stage3-Green: blocked.
Hard 4C candidate: yes.
```

The key lesson: "settlement protection policy" is not automatically positive for direct PG names.

### Stress-test components

```text
raw_component_score_proxy:
  policy_event_relevance: high
  direct_pg_exposure: high
  beneficiary_certainty: low
  settlement_margin_bridge: weak
  price_confirmation: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 6. Case 2 — 035600 KG이니시스

```yaml
case_id: C31_R12L90_035600_2024_07_26
symbol: "035600"
name: "KG이니시스"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: ECOMMERCE_SETTLEMENT_PROTECTION_PG_ESCROW_REGULATION_BRIDGE_VS_PLATFORM_PAYMENT_DELAY_HEADLINE
trigger_date: 2024-07-26
entry_date: 2024-07-26
entry_price_basis: close
entry_price: 10600
classification: local_burst_but_failed_durability_counterexample
calibration_usable: true
```

### Evidence interpretation

KG이니시스 is the local-burst case. A policy/regulatory shock can create a short-term "safe payment processor" bid, but that bid must not be confused with durable Green unless volume, take-rate, cost, and regulatory-compliance bridge appear.

### Price path

Key Stock-Web rows:

```text
2024-07-26: close 10,600
2024-08-01: high 12,120 / close 10,780
2024-08-05: low 9,560 / close 9,620
2024-09-09: low 9,150 / close 9,350
2025-01-22: low 8,680 / close 8,740
2025-04-09: low 7,980 / close 8,090
```

Approximate path from entry close:

```text
entry_close: 10,600
local_peak_high: 12,120
MFE: +14.3%
180D_worst_low: 8,680
180D_MAE: -18.1%
extended_worst_low: 7,980
extended_MAE: -24.7%
```

### Interpretation

This is not a hard 4C inside the 180D window, but it is a clear false-positive guard.

```text
Stage2-Watch: allowed.
Stage2-Actionable: only if the PG has explicit beneficiary economics.
Stage3-Green: blocked.
Local burst: yes, but the burst failed durability.
```

The model should treat the August 1 spike like a flare, not a furnace.

### Stress-test components

```text
raw_component_score_proxy:
  policy_event_relevance: high
  direct_pg_exposure: high
  local_price_confirmation: medium
  durable_price_confirmation: failed
  regulatory_cost_uncertainty: high
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 377300 카카오페이

```yaml
case_id: C31_R12L90_377300_2024_07_26
symbol: "377300"
name: "카카오페이"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: ECOMMERCE_SETTLEMENT_PROTECTION_PG_ESCROW_REGULATION_BRIDGE_VS_PLATFORM_PAYMENT_DELAY_HEADLINE
trigger_date: 2024-07-26
entry_date: 2024-07-26
entry_price_basis: close
entry_price: 26000
classification: delayed_positive_relative_resilience_wallet_platform
calibration_usable: true
```

### Evidence interpretation

카카오페이 is the relative-resilience / delayed-positive case. It is not a clean immediate beneficiary of the TMON / WeMakePrice settlement shock. Instead, it shows that a broad wallet/fintech platform can recover later if the market differentiates it from direct merchant-settlement exposure and if separate fintech/recovery flows appear.

This case should not be used to open immediate Green from the event. It supports a delayed-positive bucket.

### Price path

Key Stock-Web rows:

```text
2024-07-26: close 26,000
2024-08-05: low 21,950 / close 22,600
2024-09-09: low 21,950 / close 22,850
2025-01-15: high 28,800 / close 27,350
2025-02-05: high 33,200 / close 31,950
2025-02-26: high 35,200 / close 34,800
2025-04-09: low 26,350 / close 26,700
```

Approximate path from entry close:

```text
entry_close: 26,000
initial_worst_low: 21,950
initial_MAE: -15.6%
180D_peak_high: 28,800
180D_MFE: +10.8%
extended_peak_high: 35,200
extended_MFE: +35.4%
```

### Interpretation

This is a delayed-positive / relative-resilience case.

```text
Stage2-Watch: allowed after settlement crisis.
Immediate Stage2-Actionable: capped because initial MAE came first.
Delayed Actionable: possible only after the market differentiates wallet/platform trust from direct PG settlement risk.
Stage3-Green: requires separate payment volume / financial service / margin bridge.
```

The case prevents the shadow rule from becoming too blunt: not all payment-related names are pure victims, but the timing and bridge matter.

### Stress-test components

```text
raw_component_score_proxy:
  direct_merchant_settlement_exposure: lower_than_pg
  platform_trust_relevance: medium_high
  initial_price_confirmation: weak
  delayed_price_confirmation: high
  economic_bridge_certainty: medium
  stage3_green_initial_cap: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
delayed_positive_or_relative_resilience_count: 1
counterexample_count: 2
local_burst_but_failed_durability_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C31 grid:

```text
060250 NHN KCP:
  direct PG exposure; settlement-protection policy headline failed the price test.
  Hard 4C candidate.

035600 KG이니시스:
  local spike after the policy shock,
  but no durable Actionable/Green without take-rate / settlement-cost bridge.

377300 카카오페이:
  wallet/platform name; initial drawdown came first,
  but later relative resilience means the model should allow delayed-positive classification after separate confirmation.
```

Shared rule:

```text
C31 payment-settlement policy is not "all payment stocks benefit."
It is "map the fund-flow exposure first, then test whether regulation improves or compresses that specific business model."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R12L90_060250_2024_07_26","scheduled_round":"R12","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"ECOMMERCE_SETTLEMENT_PROTECTION_PG_ESCROW_REGULATION_BRIDGE_VS_PLATFORM_PAYMENT_DELAY_HEADLINE","symbol":"060250","name":"NHN KCP","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":9050,"peak_high_180d":9140,"peak_date_180d":"2024-07-29","worst_low_180d":7100,"worst_low_180d_date":"2024-08-05_or_2025-01-23","extended_worst_low":6860,"extended_worst_low_date":"2025-02-03","mfe_pct_180d":1.0,"mae_pct_180d":-21.5,"extended_mae_pct":-24.2,"classification":"hard_4c_candidate_direct_pg_exposure_without_settlement_margin_bridge","calibration_usable":true,"evidence_family":"direct_pg_merchant_settlement_regulation_risk","residual_error":"settlement_protection_policy_can_overpromote_direct_pg_without_margin_bridge","shadow_rule_candidate":"block_actionable_green_for_direct_pg_without_take_rate_settlement_cost_volume_bridge"}
{"row_type":"case","case_id":"C31_R12L90_035600_2024_07_26","scheduled_round":"R12","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"ECOMMERCE_SETTLEMENT_PROTECTION_PG_ESCROW_REGULATION_BRIDGE_VS_PLATFORM_PAYMENT_DELAY_HEADLINE","symbol":"035600","name":"KG이니시스","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":10600,"local_peak_high":12120,"local_peak_date":"2024-08-01","worst_low_180d":8680,"worst_low_180d_date":"2025-01-22","extended_worst_low":7980,"extended_worst_low_date":"2025-04-09","mfe_pct":14.3,"mae_pct_180d":-18.1,"extended_mae_pct":-24.7,"classification":"local_burst_but_failed_durability_counterexample","calibration_usable":true,"evidence_family":"pg_regulatory_safe_bid_without_durable_take_rate_bridge","residual_error":"local_policy_burst_can_be_mistaken_for_green","shadow_rule_candidate":"cap_local_pg_burst_at_watch_yellow_until_durable_volume_take_rate_bridge_confirms"}
{"row_type":"case","case_id":"C31_R12L90_377300_2024_07_26","scheduled_round":"R12","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"ECOMMERCE_SETTLEMENT_PROTECTION_PG_ESCROW_REGULATION_BRIDGE_VS_PLATFORM_PAYMENT_DELAY_HEADLINE","symbol":"377300","name":"카카오페이","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":26000,"initial_worst_low":21950,"initial_worst_low_date":"2024-08-05_or_2024-09-09","peak_high_180d":28800,"peak_date_180d":"2025-01-15","extended_peak_high":35200,"extended_peak_date":"2025-02-26","initial_mae_pct":-15.6,"mfe_pct_180d":10.8,"extended_mfe_pct":35.4,"classification":"delayed_positive_relative_resilience_wallet_platform","calibration_usable":true,"evidence_family":"wallet_platform_relative_resilience_after_settlement_trust_shock","residual_error":"broad_wallet_platform_can_recover_later_but_not_immediate_green_from_policy_event","shadow_rule_candidate":"allow_delayed_positive_only_after_wallet_platform_price_confirmation_and_separate_volume_margin_bridge"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"ECOMMERCE_SETTLEMENT_PROTECTION_PG_ESCROW_REGULATION_BRIDGE_VS_PLATFORM_PAYMENT_DELAY_HEADLINE","case_count":3,"positive_case_count":1,"delayed_positive_or_relative_resilience_count":1,"counterexample_count":2,"local_burst_but_failed_durability_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":90,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_PAYMENT_SETTLEMENT_EXPOSURE_MAP_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 payment-settlement / e-commerce protection policy events, do not open Stage2-Actionable or Stage3-Green from settlement-protection or merchant-support headlines alone. First classify each company by fund-flow exposure: direct PG, wallet/platform, marketplace, lender, merchant-exposed service provider, or regulatorily insulated platform. Require explicit bridge for volume, take-rate, settlement-cost, refund/chargeback risk, escrow burden, compliance cost, and price survival. Direct PG names with shallow MFE and material MAE should route to false-positive or hard-4C. Wallet/platform names may be delayed positives only after separate price confirmation and margin/volume bridge.","expected_effect":"Reduce false positives from policy headlines that appear positive for payment stocks but actually create settlement, escrow, and compliance-cost ambiguity.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":90,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"payment_settlement_policy_exposure_mapping_guard","contribution":"Adds three C31 payment/e-commerce settlement cases to separate direct PG risk, local policy burst, and delayed wallet/platform resilience.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_PAYMENT_SETTLEMENT_EXPOSURE_MAP_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [ecommerce_settlement, merchant_payment_delay, PG_regulation, escrow_protection]:

  Do not open Stage3-Green from:
    - settlement-protection headline alone
    - merchant-support headline alone
    - regulatory investigation headline alone
    - "safe PG beneficiary" label alone
    - single-day payment-stock spike alone

  First classify business exposure:
    - direct PG / VAN / payment gateway
    - wallet / fintech platform
    - marketplace / seller platform
    - merchant-credit or lender
    - travel / ticketing / voucher service
    - regulatorily insulated platform

  Require at least two of:
    - merchant volume retention
    - take-rate or fee bridge
    - escrow / settlement-cost burden quantified
    - refund / chargeback risk contained
    - compliance-cost bridge
    - balance-sheet / working-capital exposure contained
    - low-MAE post-event price survival
    - delayed price confirmation for wallet/platform names

  If direct PG MFE < 5% and MAE < -20%:
    route to C31 false-positive / hard-4C candidate.

  If local PG MFE > 10% but later MAE < -15%:
    preserve as local burst only; cap below Green.

  If wallet/platform initial MAE appears but later MFE > 30%:
    allow delayed-positive classification only after separate volume/margin bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 payment/e-commerce settlement policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_PAYMENT_SETTLEMENT_EXPOSURE_MAP_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 payment-settlement cases agree, consider implementing a canonical guard that:
   - maps each company by fund-flow exposure before scoring,
   - blocks payment-policy Green without settlement / take-rate / compliance-cost bridge,
   - routes direct-PG shallow-MFE/high-MAE cases to false-positive or hard-4C,
   - allows wallet/platform delayed positives only after separate price and margin confirmation.

Expected next schedule:
completed_round = R12
completed_loop = 90
next_round = R13
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```
