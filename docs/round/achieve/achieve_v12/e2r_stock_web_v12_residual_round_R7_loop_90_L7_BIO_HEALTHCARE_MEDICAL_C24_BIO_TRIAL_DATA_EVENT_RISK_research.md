# E2R Stock-Web v12 Residual Research — R7 / Loop 90

```yaml
scheduled_round: R7
scheduled_loop: 90
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_BINARY_TRIAL_REGULATORY_EVENT_TO_ECONOMIC_BRIDGE_VS_HEADLINE_AND_PRICE_SPIKE

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
watch_positive_with_initial_mae_count: 1
counterexample_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 90
next_round: R8
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_90_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

Under the v12 round scheduler:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 90
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 hard gate allows ordinary bio / healthcare / medical research. Recent R7 work already covered:

```text
loop88: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop89: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

This file therefore uses:

```text
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK
rows: 30
symbols: 20
date_range: 2022-01-12~2024-08-26
good/bad S2: 13/9
4B/4C: 0/2
URL pending/proxy: 10/10
top covered symbols:
  298380(3), 323990(3), 007390(2), 087010(2), 141080(2), 226950(2)
```

Selected symbols:

```text
196170 알테오젠
028300 HLB
039200 오스코텍
```

The selected symbols are not in the C24 top-covered list. They also avoid the most recent R7 loop89 C23 exact scenario set.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
196170: same archetype, new symbol, new trial/readthrough family
028300: same archetype, new symbol, binary FDA-decision risk family
039200: same archetype, new symbol, approval-readthrough sell-the-news family
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
196170 알테오젠
  profile: atlas/symbol_profiles/196/196170.json
  first_date: 2014-12-12
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,745
  corporate_action_candidate_dates:
    2017-12-07, 2017-12-28, 2020-07-23, 2020-08-13, 2021-04-12
  2024-11 entry~D+180 contamination: none

028300 HLB
  profile: atlas/symbol_profiles/028/028300.json
  first_date: 1996-09-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,065
  corporate_action_candidate_dates include past events through 2021-04-01
  2024-05 entry~D+180 contamination: none

039200 오스코텍
  profile: atlas/symbol_profiles/039/039200.json
  first_date: 2007-01-17
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,708
  corporate_action_candidate_dates:
    2009-12-29, 2010-01-26, 2012-11-16, 2022-11-30
  2024-08 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

C24 is not about a routine bio headline. It is about event convexity:

```text
trial data
regulatory decision
readthrough from partner data
approval / non-approval
label / route-of-administration / formulation result
```

The failure mode is that the model may read:

```text
"positive trial result"
"FDA approval"
"regulatory event"
"partner readthrough"
"binary decision upcoming"
```

as if the event automatically supports Stage3-Green.

For C24, the correct bridge is narrower:

```text
trial result or regulatory event
  -> clinical probability / regulatory clarity
  -> economic ownership
  -> royalty / milestone / sales conversion
  -> financing runway and dilution risk
  -> price path not dominated by binary gap risk
```

A good result can still be a sell-the-news event. A negative decision can invalidate a previously strong setup in a single trading day. A readthrough can still work, but only if the economic bridge is clear enough and the price path survives the event.

---

## 5. Case 1 — 196170 알테오젠

```yaml
case_id: C24_R7L90_196170_2024_11_20
symbol: "196170"
name: "알테오젠"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_BINARY_TRIAL_REGULATORY_EVENT_TO_ECONOMIC_BRIDGE_VS_HEADLINE_AND_PRICE_SPIKE
trigger_date: 2024-11-19
entry_date: 2024-11-20
entry_price_basis: close
entry_price: 350500
classification: watch_positive_with_initial_mae
calibration_usable: true
```

### Evidence interpretation

The event frame is the readthrough from Merck's subcutaneous Keytruda trial data. This is not a simple domestic biotech headline. It ties a global blockbuster's formulation strategy to a Korean platform/enzyme economics readthrough.

But the case is not a clean zero-drawdown Green. The price path had a sharp initial shakeout before later making a new high.

### Price path

Key Stock-Web rows:

```text
2024-11-19: close 376,000
2024-11-20: close 350,500
2024-11-21: low 279,000 / close 346,500
2024-11-29: low 279,000 / close 280,000
2024-12-20: low 274,000 / close 277,000
2025-01-24: high 364,000 / close 362,000
2025-02-17: high 403,500 / close 398,500
2025-03-18: high 459,500 / close 443,500
```

Approximate path from 2024-11-20 close:

```text
entry_close: 350,500
peak_high: 459,500
MFE: +31.1%
worst_low: 274,000
MAE: -21.8%
```

### Interpretation

This is a useful positive-with-watch case.

```text
Stage2-Actionable: allowed if economic bridge is explicit.
Stage3-Green: only after post-event recovery confirms the bridge.
Local 4B/4C guard: needed because initial MAE was large.
```

The case says C24 should not reject every volatile bio event. It should demand that the event has a real economic path and that price confirmation reappears after the first drawdown.

### Stress-test components

```text
raw_component_score_proxy:
  partner_trial_readthrough_quality: high
  economic_ownership_bridge: medium_high
  binary_event_risk: high
  initial_mae_penalty: high
  post_event_recovery_confirmation: high
  financing/dilution_risk_proxy: medium
  stage3_green_initial_cap: yes
  delayed_green_possible: yes
```

---

## 6. Case 2 — 028300 HLB

```yaml
case_id: C24_R7L90_028300_2024_05_16
symbol: "028300"
name: "HLB"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_BINARY_TRIAL_REGULATORY_EVENT_TO_ECONOMIC_BRIDGE_VS_HEADLINE_AND_PRICE_SPIKE
trigger_date: 2024-05-16
entry_date: 2024-05-16
entry_price_basis: close
entry_price: 95800
classification: hard_4c_candidate_binary_fda_decision_risk
calibration_usable: true
```

### Evidence interpretation

This case models the dangerous pre-event setup: a binary FDA/regulatory outcome is near, and the market may already price optimistic approval/trial interpretation into the stock.

The residual error:

```text
model sees late-stage / regulatory catalyst
  -> over-promotes to Stage3-Green before the decision
  -> decision shock creates instant MAE
```

The price path is the clean evidence here. The event turned into a cliff.

### Price path

Key Stock-Web rows:

```text
2024-05-16: close 95,800
2024-05-17: open/high/low/close 67,100
2024-05-20: low 47,000 / close 47,000
2024-05-21: low 45,150 / close 48,500
2024-06-25: high 73,800 / close 72,800
2024-07-05: high 94,400 / close 93,100
2024-09-23: high 97,600 / close 91,200
2024-10-25: low 63,000 / close 65,300
```

Approximate path from 2024-05-16 close:

```text
entry_close: 95,800
post_entry_peak_high: 97,600
MFE: +1.9%
worst_low: 45,150
MAE: -52.9%
```

### Interpretation

This is a hard C24 guardrail case.

```text
Stage2-Watch: possible before binary decision.
Stage2-Actionable: only if risk-adjusted catalyst score accounts for binary downside.
Stage3-Green: blocked before decision clarity.
Hard 4C candidate: yes.
```

The later rebound does not rescue the entry-quality label. The useful calibration point is the gap risk and the depth of the immediate forward MAE.

### Stress-test components

```text
raw_component_score_proxy:
  late_stage_or_regulatory_catalyst: high
  binary_event_risk: extreme
  pre-decision_price_expectation: high
  economic_bridge_uncertainty: high
  immediate_mae_penalty: extreme
  4c_guard_required: yes
```

---

## 7. Case 3 — 039200 오스코텍

```yaml
case_id: C24_R7L90_039200_2024_08_21
symbol: "039200"
name: "오스코텍"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_BINARY_TRIAL_REGULATORY_EVENT_TO_ECONOMIC_BRIDGE_VS_HEADLINE_AND_PRICE_SPIKE
trigger_date: 2024-08-20
entry_date: 2024-08-21
entry_price_basis: close
entry_price: 36900
classification: counterexample_sell_the_news_approval_readthrough_without_near_term_economic_bridge
calibration_usable: true
```

### Evidence interpretation

The event frame is FDA approval of J&J's Rybrevant + lazertinib combination. The approval was real and clinically important. For a Korean bio readthrough name, however, the investability question is not simply whether the drug was approved.

The required C24 bridge is:

```text
approval
  -> economic ownership / royalty or milestone visibility
  -> launch timing
  -> probability of recurring revenue
  -> valuation support after the headline
```

This path did not behave like a durable Green from the immediate event.

### Price path

Key Stock-Web rows:

```text
2024-08-20: close 41,450
2024-08-21: high 45,850 / low 36,350 / close 36,900
2024-08-28: high 43,200 / close 41,350
2024-09-06: low 32,850 / close 33,900
2024-09-27: low 32,700 / close 32,850
2025-01-07: low 23,950 / close 24,000
2025-02-05: high 30,700 / close 30,250
```

Approximate path from 2024-08-21 close:

```text
entry_close: 36,900
peak_high: 43,200
MFE: +17.1%
worst_low: 23,950
MAE: -35.1%
```

### Interpretation

This is the approval-readthrough counterexample.

```text
Stage2-Watch: allowed.
Stage2-Actionable: only if economic/royalty bridge is explicit.
Stage3-Green: blocked by sell-the-news and high-MAE path.
Hard 4C: not as clean as HLB, but a strong C24 false-positive guard.
```

The event was clinically real, but the stock path says the market did not sustain a C24 Green without a stronger economic conversion bridge.

### Stress-test components

```text
raw_component_score_proxy:
  approval_headline_quality: high
  trial/regulatory_event_reality: high
  economic_ownership_bridge: medium_or_unclear
  post_headline_price_confirmation: weak
  mae_penalty: high
  green_block: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
hard_4c_candidate_count: 1
watch_positive_with_initial_mae_count: 1
```

The three-case C24 grid:

```text
196170 알테오젠:
  real partner trial/readthrough plus later recovery can become positive,
  but initial MAE means Green should be delayed until post-event confirmation.

028300 HLB:
  pre-binary regulatory optimism can be catastrophic.
  This is the hard 4C guardrail.

039200 오스코텍:
  approval can be real but still sell-the-news without direct economic conversion.
  Watch/Yellow is safer than immediate Green.
```

The shared rule is simple:

```text
C24 is not "event happened = Green."
C24 is "event + economic ownership + conversion bridge + post-event price survival = possible Green."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C24_R7L90_196170_2024_11_20","scheduled_round":"R7","scheduled_loop":90,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_BINARY_TRIAL_REGULATORY_EVENT_TO_ECONOMIC_BRIDGE_VS_HEADLINE_AND_PRICE_SPIKE","symbol":"196170","name":"알테오젠","trigger_date":"2024-11-19","entry_date":"2024-11-20","entry_price":350500,"peak_high":459500,"peak_date":"2025-03-18","worst_low":274000,"worst_low_date":"2024-12-20","mfe_pct":31.1,"mae_pct":-21.8,"classification":"watch_positive_with_initial_mae","calibration_usable":true,"evidence_family":"partner_trial_readthrough_subcutaneous_formulation_economic_bridge","residual_error":"positive_event_can_require_delayed_green_after_initial_mae","shadow_rule_candidate":"delay_green_until_post_event_recovery_confirms_economic_bridge"}
{"row_type":"case","case_id":"C24_R7L90_028300_2024_05_16","scheduled_round":"R7","scheduled_loop":90,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_BINARY_TRIAL_REGULATORY_EVENT_TO_ECONOMIC_BRIDGE_VS_HEADLINE_AND_PRICE_SPIKE","symbol":"028300","name":"HLB","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800,"peak_high":97600,"peak_date":"2024-09-23","worst_low":45150,"worst_low_date":"2024-05-21","mfe_pct":1.9,"mae_pct":-52.9,"classification":"hard_4c_candidate_binary_fda_decision_risk","calibration_usable":true,"evidence_family":"binary_fda_decision_risk_pre_event_expectation","residual_error":"pre_decision_bio_optimism_can_be_catastrophic_if_promoted_to_green","shadow_rule_candidate":"block_green_before_binary_regulatory_decision_unless_downside_risk_adjusted"}
{"row_type":"case","case_id":"C24_R7L90_039200_2024_08_21","scheduled_round":"R7","scheduled_loop":90,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_BINARY_TRIAL_REGULATORY_EVENT_TO_ECONOMIC_BRIDGE_VS_HEADLINE_AND_PRICE_SPIKE","symbol":"039200","name":"오스코텍","trigger_date":"2024-08-20","entry_date":"2024-08-21","entry_price":36900,"peak_high":43200,"peak_date":"2024-08-28","worst_low":23950,"worst_low_date":"2025-01-07","mfe_pct":17.1,"mae_pct":-35.1,"classification":"counterexample_sell_the_news_approval_readthrough_without_near_term_economic_bridge","calibration_usable":true,"evidence_family":"approval_readthrough_without_direct_economic_conversion_bridge","residual_error":"real_approval_headline_can_overpromote_bio_readthrough_name","shadow_rule_candidate":"cap_approval_readthrough_at_watch_or_yellow_without_royalty_sales_conversion_bridge"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":90,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_BINARY_TRIAL_REGULATORY_EVENT_TO_ECONOMIC_BRIDGE_VS_HEADLINE_AND_PRICE_SPIKE","case_count":3,"positive_case_count":1,"watch_positive_with_initial_mae_count":1,"counterexample_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":90,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","rule_id":"C24_BINARY_EVENT_ECONOMIC_BRIDGE_AND_POST_EVENT_SURVIVAL_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C24, do not open Stage3-Green from trial/regulatory/binary event headlines alone. Require economic ownership, milestone/royalty/sales conversion bridge, financing runway, and post-event price survival. Before binary regulatory decision, cap at Watch/Yellow unless downside-adjusted evidence is overwhelming. After approval/readthrough, block Green if MFE is shallow and MAE is large.","expected_effect":"Reduce bio event false positives and hard-4C cases while preserving delayed positives when real partner data readthrough converts into sustained recovery.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":90,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","residual_type":"bio_binary_event_false_positive_guard","contribution":"Adds one delayed positive and two counterexamples to separate real trial/regulatory events from investable economic conversion and price survival.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C24_BINARY_EVENT_ECONOMIC_BRIDGE_AND_POST_EVENT_SURVIVAL_REQUIRED

IF canonical_archetype_id == C24_BIO_TRIAL_DATA_EVENT_RISK:

  Do not open Stage3-Green from:
    - trial data headline alone
    - FDA/EMA/regulatory decision date alone
    - partner approval/readthrough alone
    - near-binary event expectation alone
    - single-day price spike alone

  Require:
    - economic ownership / royalty / milestone / sales bridge
    - label or population clarity
    - financing runway / dilution risk check
    - post-event price survival
    - no immediate high-MAE failure

  If entry is before a binary regulatory decision:
    cap at Stage2-Watch or Stage2-Yellow.
    require explicit downside-risk adjustment.

  If the event is approved but MFE < 20% and MAE < -30%:
    classify as sell-the-news counterexample or C24 false-positive guard.

  If the event initially draws down but later recovers with MFE > 30%:
    allow delayed-positive classification, not immediate Green.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_90_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C24 bio event-risk cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C24_BINARY_EVENT_ECONOMIC_BRIDGE_AND_POST_EVENT_SURVIVAL_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C24 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C24 cases agree, consider implementing a canonical guard that:
   - caps pre-binary regulatory-event setups at Watch/Yellow,
   - requires economic ownership and conversion bridge before Green,
   - routes shallow-MFE/high-MAE post-approval cases to false-positive or hard-4C,
   - allows delayed positive only after post-event recovery confirms the bridge.

Expected next schedule:
completed_round = R7
completed_loop = 90
next_round = R8
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```
