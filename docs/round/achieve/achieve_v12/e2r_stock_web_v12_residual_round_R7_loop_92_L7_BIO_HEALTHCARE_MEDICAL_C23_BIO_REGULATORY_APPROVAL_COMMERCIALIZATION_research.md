# E2R Stock-Web v12 Residual Research — R7 / Loop 92

```yaml
scheduled_round: R7
scheduled_loop: 92
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_COMPETITOR_APPROVAL_AND_LITIGATION_BETA

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
positive_case_count: 2
counterexample_count: 1
delayed_positive_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 0
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 92
next_round: R8
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_92_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 92
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 hard gate requires:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

Recent R7 branch usage already covered:

```text
loop89: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop90: C24_BIO_TRIAL_DATA_EVENT_RISK
loop91: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

This run returns to C23, but uses a different fine branch:

```text
botulinum-toxin US approval / commercialization bridge
vs competitor-approval and litigation beta
```

The goal is not to repeat generic biotech approval or trial-data event risk. The goal is to separate:

```text
regulatory approval -> launch / distribution / reimbursement or channel economics -> sales and margin
```

from:

```text
approval headline, competitor readthrough, or litigation sentiment only.
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
rows: 26
symbols: 14
date_range: 2022-06-29~2024-08-21
good/bad S2: 8/5
4B/4C: 0/2
URL pending/proxy: 0/0
top covered symbols:
  UNKNOWN_SYMBOL(6), 028300(4), 000100(2), 039200(2), 195940(2), 003850(1)
```

Selected symbols:

```text
145020 휴젤
069620 대웅제약
086900 메디톡스
```

They avoid the C23 top-covered symbols and avoid the recent R7 C24/C25 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
145020: same archetype, new symbol, botulinum-toxin US approval / commercialization positive with 4B watch
069620: same archetype, new symbol, existing US toxin commercialization / delayed positive bridge
086900: same archetype, new symbol, competitor-approval/litigation beta with delayed recovery and immediate-green block
```

---

## 3. Price-atlas validation

Manifest fields checked from stock-web:

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
inactive_or_delisted_like_symbol_count: 2,546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
145020 휴젤
  profile: atlas/symbol_profiles/145/145020.json
  first_date: 2015-12-24
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,489
  corporate_action_candidate_dates:
    2017-07-31, 2020-07-08, 2020-07-31
  2024 entry~D+180 contamination: none

069620 대웅제약
  profile: atlas/symbol_profiles/069/069620.json
  first_date: 2002-11-01
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,751
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

086900 메디톡스
  profile: atlas/symbol_profiles/086/086900.json
  first_date: 2009-01-16
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,215
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-03-04
US regulatory/commercialization readthrough around Korean botulinum-toxin assets, led by Letybo / letibotulinumtoxinA approval and US launch-path expectations.
```

This is C23 because the investment question is not simply "a medical aesthetics stock went up." The C23 question is:

```text
regulatory approval
  -> commercial launch path
  -> distributor / doctor-channel access
  -> procedure adoption
  -> price and reimbursement / cash-pay positioning
  -> revenue and margin conversion
  -> post-approval price survival
```

The model can over-score:

```text
FDA approval headline
botulinum toxin label
medical aesthetics label
competitor readthrough
litigation settlement hope
one-day approval spike
```

The bridge must be stricter:

```text
approval or regulatory clearance
  -> launch timing
  -> channel economics
  -> share capture
  -> gross margin / OP conversion
  -> legal or competitive overhang check
  -> price survival after the initial approval move
```

A regulatory approval is the key to a door. C23 asks whether the company can walk through the door, stock the shelves, and collect margin.

---

## 5. Case 1 — 145020 휴젤

```yaml
case_id: C23_R7L92_145020_2024_03_04
symbol: "145020"
name: "휴젤"
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_COMPETITOR_APPROVAL_AND_LITIGATION_BETA
trigger_date: 2024-03-04
entry_date: 2024-03-04
entry_price_basis: close
entry_price: 202500
classification: positive_with_local_4b_us_approval_commercialization_bridge
calibration_usable: true
```

### Evidence interpretation

휴젤 is the direct regulatory/commercialization positive.

The useful C23 read is:

```text
botulinum-toxin US approval / launch path
  -> addressable US aesthetic channel
  -> distributor / physician adoption
  -> revenue and margin bridge
  -> later price confirmation
```

The price path did not move in a straight line. It pulled back first, then rerated strongly. That means the model should allow Actionable when launch-channel and commercialization bridge are explicit, but it should attach local 4B after the extended move.

### Price path

Key Stock-Web rows:

```text
2024-03-04: high 219,000 / close 202,500
2024-03-21: low 172,300 / close 177,900
2024-04-29: high 223,000 / close 221,000
2024-07-24: high 251,000 / close 246,500
2024-08-19: high 294,500 / close 286,500
2024-10-17: high 301,000 / close 293,000
2024-11-04: high 289,000 / close 287,500
```

Approximate path from entry close:

```text
entry_close: 202,500
peak_high: 301,000
MFE: +48.6%
worst_low: 172,300
MAE: -14.9%
```

### Interpretation

This is a C23 positive with 4B watch:

```text
Stage2-Actionable: valid if approval-to-launch commercialization bridge is explicit.
Stage3-Green: possible only with channel uptake / revenue / margin evidence.
Local 4B: attach after +45%~50% MFE unless a fresh revision bridge appears.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  regulatory_approval_relevance: high
  direct_commercialization_bridge: high
  channel_launch_visibility: medium_high
  margin_bridge: medium
  early_pullback_penalty: medium
  price_confirmation: high
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 069620 대웅제약

```yaml
case_id: C23_R7L92_069620_2024_03_04
symbol: "069620"
name: "대웅제약"
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_COMPETITOR_APPROVAL_AND_LITIGATION_BETA
trigger_date: 2024-03-04
entry_date: 2024-03-04
entry_price_basis: close
entry_price: 113200
classification: positive_delayed_existing_toxin_commercialization_bridge
calibration_usable: true
```

### Evidence interpretation

대웅제약 is the existing commercialization / delayed positive.

It was not the direct new-approval beneficiary in the same way as 휴젤. But the stock later behaved like the market differentiated existing toxin commercialization economics, US/international sales capability, and legal/competitive risk.

The key is timing: C23 should not open immediate Green from a competitor approval headline. It can, however, allow delayed-positive classification after price and commercialization evidence confirm.

### Price path

Key Stock-Web rows:

```text
2024-03-04: close 113,200
2024-03-19: high 124,500 / close 123,600
2024-03-25: high 127,600 / close 126,900
2024-05-30: low 103,100 / close 103,100
2024-07-24: high 131,600 / close 128,800
2024-08-23: high 150,000 / close 146,200
2024-10-15: high 164,400 / close 160,400
```

Approximate path from entry close:

```text
entry_close: 113,200
peak_high: 164,400
MFE: +45.2%
worst_low: 103,100
MAE: -8.9%
```

### Interpretation

This is a delayed C23 positive:

```text
Stage2-Watch: valid immediately from toxin commercialization readthrough.
Stage2-Actionable: allowed only after price confirms and commercialization bridge is explicit.
Stage3-Green: requires sales, margin, and legal/competitive-risk evidence.
Local 4B: monitor after +40%~45% MFE.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  direct_new_approval_relevance: medium
  existing_commercialization_bridge: medium_high
  legal_competitive_overhang: medium
  price_confirmation: high_after_delay
  drawdown_penalty: low_to_medium
  delayed_positive: yes
```

---

## 7. Case 3 — 086900 메디톡스

```yaml
case_id: C23_R7L92_086900_2024_03_04
symbol: "086900"
name: "메디톡스"
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_COMPETITOR_APPROVAL_AND_LITIGATION_BETA
trigger_date: 2024-03-04
entry_date: 2024-03-04
entry_price_basis: close
entry_price: 152600
classification: delayed_recovery_but_immediate_green_block_competitor_approval_litigation_beta
calibration_usable: true
```

### Evidence interpretation

메디톡스 is the guardrail case.

It is a real botulinum-toxin company, but the trigger is not a clean company-specific approval-to-commercialization bridge. The immediate path after the March trigger fell first and did not support instant Green. Later in August it recovered strongly, which means the case should not be treated as a permanent negative. It is a timing and bridge guardrail.

The model must distinguish:

```text
direct regulatory approval and launch path
```

from:

```text
competitor approval readthrough / litigation beta / later sentiment recovery.
```

### Price path

Key Stock-Web rows:

```text
2024-03-04: close 152,600
2024-03-07: low 143,100 / close 147,500
2024-04-17: low 128,000 / close 128,100
2024-05-28: high 150,000 / close 141,100
2024-08-05: low 149,100 / close 152,100
2024-08-21: high 217,500 / close 214,500
2024-08-22: high 218,000 / close 213,500
2024-10-22: low 164,800 / close 170,500
```

Approximate path from entry close:

```text
entry_close: 152,600
initial_worst_low: 128,000
initial_MAE: -16.1%
later_peak_high: 218,000
later_MFE: +42.9%
```

### Interpretation

This is a delayed-positive / immediate-green-block case:

```text
Stage2-Watch: allowed from toxin-sector relevance.
Immediate Stage2-Actionable: blocked without company-specific approval/commercialization bridge.
Delayed Actionable: possible only after separate price confirmation and legal/commercial bridge.
Stage3-Green: blocked from competitor approval readthrough alone.
Hard 4C: no because later MFE was strong; classify as timing/bridge guardrail.
```

### Stress-test components

```text
raw_component_score_proxy:
  toxin_sector_relevance: high
  direct_company_approval_bridge: weak_at_trigger
  litigation_or_competitive_beta: high
  initial_price_confirmation: weak
  later_price_confirmation: high
  delayed_positive: yes
  immediate_green_block: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
delayed_positive_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 0
calibration_usable_trigger_count: 3
```

The three-case C23 grid:

```text
145020 휴젤:
  direct approval/commercialization positive;
  early pullback then strong MFE, local 4B after extended move.

069620 대웅제약:
  existing toxin commercialization delayed-positive;
  not direct approval beneficiary, but price and commercialization bridge later confirmed.

086900 메디톡스:
  sector relevance but no immediate company-specific approval bridge;
  initial drawdown first, later recovery means delayed classification only.
```

Shared rule:

```text
C23 is not "regulatory approval headline exists."
C23 is "approval converts into company-specific launch, channel adoption, sales, and margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C23_R7L92_145020_2024_03_04","scheduled_round":"R7","scheduled_loop":92,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_COMPETITOR_APPROVAL_AND_LITIGATION_BETA","symbol":"145020","name":"휴젤","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":202500,"peak_high":301000,"peak_date":"2024-10-17","worst_low":172300,"worst_low_date":"2024-03-21","mfe_pct":48.6,"mae_pct":-14.9,"classification":"positive_with_local_4b_us_approval_commercialization_bridge","calibration_usable":true,"evidence_family":"botulinum_toxin_us_approval_launch_channel_margin_bridge","residual_error":"positive_entry_but_approval_rerating_needs_4b_after_large_mfe_without_fresh_revenue_bridge","shadow_rule_candidate":"allow_actionable_when_approval_to_launch_channel_margin_bridge_confirms; attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C23_R7L92_069620_2024_03_04","scheduled_round":"R7","scheduled_loop":92,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_COMPETITOR_APPROVAL_AND_LITIGATION_BETA","symbol":"069620","name":"대웅제약","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":113200,"peak_high":164400,"peak_date":"2024-10-15","worst_low":103100,"worst_low_date":"2024-05-30","mfe_pct":45.2,"mae_pct":-8.9,"classification":"positive_delayed_existing_toxin_commercialization_bridge","calibration_usable":true,"evidence_family":"existing_toxin_commercialization_sales_margin_legal_risk_bridge","residual_error":"competitor_approval_readthrough_needs_delayed_price_and_commercialization_confirmation","shadow_rule_candidate":"allow_delayed_positive_when_existing_commercialization_bridge_and_price_survival_confirm"}
{"row_type":"case","case_id":"C23_R7L92_086900_2024_03_04","scheduled_round":"R7","scheduled_loop":92,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_COMPETITOR_APPROVAL_AND_LITIGATION_BETA","symbol":"086900","name":"메디톡스","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":152600,"initial_worst_low":128000,"initial_worst_low_date":"2024-04-17","later_peak_high":218000,"later_peak_date":"2024-08-22","initial_mae_pct":-16.1,"later_mfe_pct":42.9,"classification":"delayed_recovery_but_immediate_green_block_competitor_approval_litigation_beta","calibration_usable":true,"evidence_family":"toxin_sector_competitor_approval_litigation_beta_without_direct_approval_bridge_at_trigger","residual_error":"sector_or_competitor_approval_readthrough_can_fail_immediate_green_but_recover_later","shadow_rule_candidate":"block_immediate_green_without_company_specific_approval_commercialization_bridge; allow_delayed_positive_after_separate_price_confirmation"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":92,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_TOXIN_US_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_COMPETITOR_APPROVAL_AND_LITIGATION_BETA","case_count":3,"positive_case_count":2,"counterexample_count":1,"delayed_positive_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":0,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":92,"canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","rule_id":"C23_APPROVAL_TO_COMMERCIAL_LAUNCH_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C23, do not open Stage2-Actionable or Stage3-Green from regulatory approval, toxin label, competitor readthrough, or litigation sentiment alone. Require company-specific approval or clearance, launch timing, channel/distributor access, adoption or prescription/procedure uptake, revenue conversion, margin/OP bridge, legal/competitive overhang check, and post-trigger price survival. Direct approval beneficiaries may be Actionable when launch and margin bridge are explicit. Competitor-readthrough or litigation-beta names should cap at Watch or delayed-positive until separate price confirmation appears. Large MFE after approval should attach local 4B unless fresh sales or margin revision appears.","expected_effect":"Preserve direct approval/commercialization positives while reducing competitor-readthrough and litigation-beta false positives in bio/toxin names.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":92,"canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","residual_type":"bio_regulatory_approval_to_commercial_launch_guard","contribution":"Adds one direct toxin-approval positive, one existing-commercialization delayed positive, and one competitor/litigation-beta timing guardrail case to calibrate C23 launch-channel-margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C23_APPROVAL_TO_COMMERCIAL_LAUNCH_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION:

  Do not open Stage3-Green from:
    - regulatory approval headline alone
    - FDA / overseas approval label alone
    - toxin / drug / biologic label alone
    - competitor approval readthrough alone
    - litigation settlement or sentiment alone
    - one-day approval spike alone

  Require at least two of:
    - company-specific approval or clearance
    - launch timing and distributor/channel plan
    - adoption / prescription / procedure uptake
    - revenue conversion
    - gross margin or OP bridge
    - legal / competitive overhang check
    - low-MAE post-trigger price survival
    - fresh sales or revision evidence after approval

  If direct approval beneficiary has MFE > 40%:
    preserve positive classification but attach local 4B unless fresh commercial-sales evidence appears.

  If non-beneficiary sector peer falls first and recovers later:
    classify as delayed-positive only after separate price confirmation.

  If competitor-readthrough name lacks direct approval/commercial bridge:
    cap at Watch/Yellow and block immediate Green.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_92_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C23 bio regulatory approval/commercialization cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C23_APPROVAL_TO_COMMERCIAL_LAUNCH_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C23 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C23 cases agree, consider implementing a canonical guard that:
   - blocks approval-headline Green without launch/channel/revenue/margin bridge,
   - preserves direct approval positives only with price survival and commercialization evidence,
   - attaches local 4B after large approval rerating,
   - caps competitor-readthrough or litigation-beta names at Watch/Delayed-positive until separate confirmation.

Expected next schedule:
completed_round = R7
completed_loop = 92
next_round = R8
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R7
completed_loop = 92
next_round = R8
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
