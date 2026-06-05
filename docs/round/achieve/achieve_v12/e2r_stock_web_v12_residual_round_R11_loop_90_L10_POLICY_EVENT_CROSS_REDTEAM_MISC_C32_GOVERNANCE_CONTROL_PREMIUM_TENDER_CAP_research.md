# E2R Stock-Web v12 Residual Research — R11 / Loop 90

```yaml
scheduled_round: R11
scheduled_loop: 90
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: DOOSAN_RESTRUCTURING_MINORITIZED_SUBSIDIARY_MERGER_RATIO_GOVERNANCE_CAP_VS_CONTROL_PREMIUM_HEADLINE

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
same_archetype_new_symbol_count: 2
soft_repeat_symbol_count: 1
positive_or_local_burst_count: 1
counterexample_count: 3
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 90
next_round: R12
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_90_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 90
```

R11 may use:

```text
L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

for policy / governance / event research. This file uses:

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

The fine branch is the 2024 Doosan restructuring controversy:

```text
control-family / holdco restructuring
  -> listed subsidiary exchange or merger ratio
  -> minority-shareholder value transfer risk
  -> governance cap on Stage2/Stage3 scoring
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rows: 41
symbols: 22
date_range: 2020-02-12~2024-10-31
good/bad S2: 16/12
4B/4C: 3/0
URL pending/proxy: 8/8
top covered symbols:
  010130(4), 036560(4), 000150(3), 041510(3), 241560(3), 000990(2)
```

Selected symbols:

```text
454910 두산로보틱스
034020 두산에너빌리티
241560 두산밥캣
```

Novelty classification:

```text
454910: same archetype, new symbol, parent-favored robotics valuation leg
034020: same archetype, new symbol, intermediate holdco / source-of-transfer leg
241560: soft repeat symbol, but new loop/fine-branch/date/failure-mode
```

Hard duplicate key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

The repeated symbol `241560` is not treated as a hard duplicate because this file uses a distinct trigger date and the Doosan restructuring minority-shareholder transfer branch. It is still marked as a soft repeat.

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
454910 두산로보틱스
  profile: atlas/symbol_profiles/454/454910.json
  first_date: 2023-10-05
  last_date: 2026-02-20
  tradable_ohlcv rows: 578
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

034020 두산에너빌리티
  profile: atlas/symbol_profiles/034/034020.json
  first_date: 2000-10-25
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,245
  corporate_action_candidate_dates:
    2019-05-29, 2020-02-18, 2020-12-24
  2024 entry~D+180 contamination: none

241560 두산밥캣
  profile: atlas/symbol_profiles/241/241560.json
  first_date: 2016-11-18
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,269
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-07-11 / 2024-07-12
Doosan restructuring proposal involving Doosan Bobcat, Doosan Robotics, and group control economics.
```

The public controversy centered on the exchange-ratio / valuation problem:

```text
valuable cash-generating Bobcat
  -> routed into a high-multiple Robotics structure
  -> minority holders could see economic interest diluted
  -> controlling-family/holding-company economics may improve
  -> affected stocks may move in opposite directions
```

This is exactly where C32 needs a guard.

C32 is not:

```text
"governance event = automatic control-premium buy"
```

C32 is:

```text
governance event
  -> who receives control premium?
  -> who bears dilution?
  -> does minority value improve or transfer away?
  -> does tender / exchange / merger ratio create a price floor or cap?
  -> does the price path survive after the governance burst?
```

---

## 5. Case 1 — 454910 두산로보틱스

```yaml
case_id: C32_R11L90_454910_2024_07_11
symbol: "454910"
name: "두산로보틱스"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: DOOSAN_RESTRUCTURING_MINORITIZED_SUBSIDIARY_MERGER_RATIO_GOVERNANCE_CAP_VS_CONTROL_PREMIUM_HEADLINE
trigger_date: 2024-07-11
entry_date: 2024-07-11
entry_price_basis: close
entry_price: 85300
classification: local_burst_but_high_mae_governance_beneficiary_leg
calibration_usable: true
```

### Evidence interpretation

두산로보틱스 is the apparent beneficiary leg. In a governance restructuring where a high-multiple listed robotics platform absorbs or receives economic exposure to a cash-generating industrial subsidiary, the market can initially price the robotics leg as the favored vehicle.

This is not a clean Green. The price path shows a powerful one-day burst followed by a violent reversal.

### Price path

Key Stock-Web rows:

```text
2024-07-11: close 85,300
2024-07-12: high 109,300 / close 105,700
2024-07-18: close 81,700
2024-08-05: low 53,900 / close 59,300
2024-08-29: high 73,600 / close 69,300
2024-09-30: close 63,700
```

Approximate path from entry close:

```text
entry_close: 85,300
peak_high: 109,300
MFE: +28.1%
worst_low: 53,900
MAE: -36.8%
```

### Interpretation

This is a local burst, not a durable Green.

```text
Stage2-Watch: allowed.
Stage2-Actionable: only for very short-term event trading.
Stage3-Green: blocked.
4B/4C: local 4B required after the spike; high-MAE guard applies after reversal.
```

The C32 model must not equate "favored control vehicle" with "durable minority-shareholder rerating."

### Stress-test components

```text
raw_component_score_proxy:
  apparent_control_beneficiary: high
  valuation_ratio_advantage: high
  minority_value_certainty: low
  price_spike_confirmation: high
  post_spike_survival: failed
  drawdown_penalty: high
  green_block: yes
```

---

## 6. Case 2 — 034020 두산에너빌리티

```yaml
case_id: C32_R11L90_034020_2024_07_11
symbol: "034020"
name: "두산에너빌리티"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: DOOSAN_RESTRUCTURING_MINORITIZED_SUBSIDIARY_MERGER_RATIO_GOVERNANCE_CAP_VS_CONTROL_PREMIUM_HEADLINE
trigger_date: 2024-07-11
entry_date: 2024-07-11
entry_price_basis: close
entry_price: 21850
classification: counterexample_intermediate_holding_leg_without_clean_value_transfer_bridge
calibration_usable: true
```

### Evidence interpretation

두산에너빌리티 is the intermediate leg. The group-level restructuring may appear to simplify ownership or crystallize value, but the equity path depends on what the listed holder gives up, receives, and how minority value is treated.

The event produced noise, but not a clean C32 positive.

### Price path

Key Stock-Web rows:

```text
2024-07-11: close 21,850
2024-07-12: high 21,700 / close 20,900
2024-07-18: high 25,000 / close 21,000
2024-08-05: low 15,150 / close 15,860
2024-09-13: high 18,670 / close 18,160
```

Approximate path from entry close:

```text
entry_close: 21,850
peak_high: 25,000
MFE: +14.4%
worst_low: 15,150
MAE: -30.7%
```

### Interpretation

This is a C32 false-positive / high-MAE case.

```text
Stage2-Watch: possible.
Stage2-Actionable: blocked unless value-transfer bridge is clearly positive to this class of shareholders.
Stage3-Green: blocked by weak MFE / large MAE.
Hard 4C candidate: yes.
```

The lesson is that a control-driven restructuring can create a trading burst in one leg while destroying certainty in another.

### Stress-test components

```text
raw_component_score_proxy:
  group_restructuring_relevance: high
  direct_control_premium_capture: unclear
  valuation_ratio_fairness: contested
  price_confirmation: weak
  drawdown_penalty: high
  green_block: yes
```

---

## 7. Case 3 — 241560 두산밥캣

```yaml
case_id: C32_R11L90_241560_2024_07_11
symbol: "241560"
name: "두산밥캣"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: DOOSAN_RESTRUCTURING_MINORITIZED_SUBSIDIARY_MERGER_RATIO_GOVERNANCE_CAP_VS_CONTROL_PREMIUM_HEADLINE
trigger_date: 2024-07-11
entry_date: 2024-07-11
entry_price_basis: close
entry_price: 52000
classification: hard_4c_candidate_minoritized_subsidiary_value_transfer_risk
calibration_usable: true
soft_repeat_symbol: true
```

### Evidence interpretation

두산밥캣 is the minority-shareholder risk leg. The controversy is clearest here: if a valuable operating subsidiary is effectively moved into a structure where its valuation is set by a statutory or market-price ratio rather than intrinsic value, minority shareholders may face value-transfer risk.

The price path was decisive. The stock did not behave like a control-premium beneficiary.

### Price path

Key Stock-Web rows:

```text
2024-07-11: close 52,000
2024-07-12: high 59,500 / close 54,600
2024-07-25: low 41,150 / close 44,150
2024-08-05: low 33,350 / close 34,250
2024-08-27: high 43,950 / close 43,750
2024-09-30: close 40,600
```

Approximate path from entry close:

```text
entry_close: 52,000
peak_high: 59,500
MFE: +14.4%
worst_low: 33,350
MAE: -35.9%
```

### Interpretation

This is the core hard-4C case for the file.

```text
Stage2-Watch: allowed when governance event first appears.
Stage2-Actionable: blocked for the minority-risk leg unless exchange terms protect intrinsic value.
Stage3-Green: blocked.
Hard 4C: yes.
```

C32 should distinguish between:

```text
control premium to controller / favored vehicle
```

and:

```text
control discount or value-transfer risk to minority holders.
```

### Stress-test components

```text
raw_component_score_proxy:
  minority_value_transfer_risk: high
  merger_ratio_contestation: high
  intrinsic_value_discount_risk: high
  price_confirmation: failed after one-day spike
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_or_local_burst_count: 1
counterexample_count: 3
hard_4c_candidate_count: 2
soft_repeat_symbol_count: 1
calibration_usable_trigger_count: 3
```

The three-case Doosan C32 grid:

```text
454910 두산로보틱스:
  apparent favored vehicle; local event burst;
  but high MAE means not Green.

034020 두산에너빌리티:
  intermediate holding leg;
  weak MFE and large MAE without clear value-transfer benefit.

241560 두산밥캣:
  minority-risk operating subsidiary;
  hard 4C candidate due to value-transfer / merger-ratio risk.
```

Shared rule:

```text
C32 is not "governance restructuring happened."
C32 is "which shareholder class captures the control premium, and which class absorbs the discount?"
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C32_R11L90_454910_2024_07_11","scheduled_round":"R11","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"DOOSAN_RESTRUCTURING_MINORITIZED_SUBSIDIARY_MERGER_RATIO_GOVERNANCE_CAP_VS_CONTROL_PREMIUM_HEADLINE","symbol":"454910","name":"두산로보틱스","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":85300,"peak_high":109300,"peak_date":"2024-07-12","worst_low":53900,"worst_low_date":"2024-08-05","mfe_pct":28.1,"mae_pct":-36.8,"classification":"local_burst_but_high_mae_governance_beneficiary_leg","calibration_usable":true,"evidence_family":"apparent_control_favored_vehicle_but_no_durable_minority_rerating","residual_error":"favored_governance_vehicle_can_spike_then_fail_without_minority_value_bridge","shadow_rule_candidate":"cap_green_after_governance_burst_until_post_event_price_survival_confirms"}
{"row_type":"case","case_id":"C32_R11L90_034020_2024_07_11","scheduled_round":"R11","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"DOOSAN_RESTRUCTURING_MINORITIZED_SUBSIDIARY_MERGER_RATIO_GOVERNANCE_CAP_VS_CONTROL_PREMIUM_HEADLINE","symbol":"034020","name":"두산에너빌리티","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":21850,"peak_high":25000,"peak_date":"2024-07-18","worst_low":15150,"worst_low_date":"2024-08-05","mfe_pct":14.4,"mae_pct":-30.7,"classification":"counterexample_intermediate_holding_leg_without_clean_value_transfer_bridge","calibration_usable":true,"evidence_family":"group_restructuring_intermediate_leg_without_direct_minority_value_capture","residual_error":"group_restructuring_relevance_can_overpromote_intermediate_leg","shadow_rule_candidate":"block_actionable_green_when_value_transfer_bridge_to_this_share_class_is_unclear"}
{"row_type":"case","case_id":"C32_R11L90_241560_2024_07_11","scheduled_round":"R11","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"DOOSAN_RESTRUCTURING_MINORITIZED_SUBSIDIARY_MERGER_RATIO_GOVERNANCE_CAP_VS_CONTROL_PREMIUM_HEADLINE","symbol":"241560","name":"두산밥캣","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":52000,"peak_high":59500,"peak_date":"2024-07-12","worst_low":33350,"worst_low_date":"2024-08-05","mfe_pct":14.4,"mae_pct":-35.9,"classification":"hard_4c_candidate_minoritized_subsidiary_value_transfer_risk","calibration_usable":true,"soft_repeat_symbol":true,"evidence_family":"minority_operating_subsidiary_merger_ratio_value_transfer_risk","residual_error":"control_restructuring_can_harm_minority_leg_even_if_group_control_economics_improve","shadow_rule_candidate":"route_minority_risk_leg_to_false_positive_or_hard_4c_if_mfe_shallow_mae_large"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"DOOSAN_RESTRUCTURING_MINORITIZED_SUBSIDIARY_MERGER_RATIO_GOVERNANCE_CAP_VS_CONTROL_PREMIUM_HEADLINE","case_count":3,"positive_or_local_burst_count":1,"counterexample_count":3,"hard_4c_candidate_count":2,"soft_repeat_symbol_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":90,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule_id":"C32_SHARE_CLASS_VALUE_TRANSFER_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C32 governance, restructuring, tender, or control-premium events, do not open Stage2-Actionable or Stage3-Green from the existence of a governance event alone. Identify the shareholder class and listed vehicle. Require evidence that the specific share class captures control premium or intrinsic value uplift. If the event creates merger-ratio, dilution, minority squeeze, or value-transfer risk, cap at Watch/Yellow or route to hard-4C when MFE is shallow and MAE is large.","expected_effect":"Reduce governance-event false positives by separating control-premium beneficiary legs from minority-value-transfer risk legs.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":90,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"governance_share_class_value_transfer_guard","contribution":"Adds Doosan restructuring governance cases to separate apparent control-beneficiary burst from minority-shareholder value-transfer risk.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C32_SHARE_CLASS_VALUE_TRANSFER_BRIDGE_REQUIRED

IF canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:

  Do not open Stage3-Green from:
    - governance restructuring headline alone
    - tender offer headline alone
    - control battle headline alone
    - merger / spin-off / exchange ratio headline alone
    - controller or holdco benefit alone

  First classify the listed vehicle as:
    - control-premium beneficiary
    - favored holding vehicle
    - intermediate transfer leg
    - minority-risk operating subsidiary
    - tender-floor beneficiary
    - tender-cap / post-tender discount leg

  Require:
    - explicit tender floor or exchange-ratio protection,
    - intrinsic-value uplift to this specific share class,
    - no minority value transfer,
    - low-MAE post-event price survival,
    - and no immediate governance backlash.

  If MFE < 20% and MAE < -30%:
    route to C32 false-positive / hard-4C candidate.

  If MFE > 20% but post-event MAE > -30%:
    preserve as local burst only, not Green.

  If the share class is a minority-risk subsidiary:
    cap at Watch/Yellow unless the terms are clearly accretive to that class.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C32 governance/control-premium cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C32_SHARE_CLASS_VALUE_TRANSFER_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C32 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. Handle 241560 as a soft repeat, not a hard duplicate, because it uses a different fine branch and trigger date/failure mode.
8. If enough C32 cases agree, consider implementing a canonical guard that:
   - identifies the relevant share class before scoring,
   - blocks governance-event Green without share-class-specific value capture,
   - routes minority-risk merger-ratio cases to false-positive or hard-4C,
   - preserves local burst classification for favored vehicles but requires price survival before Green.

Expected next schedule:
completed_round = R11
completed_loop = 90
next_round = R12
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```
