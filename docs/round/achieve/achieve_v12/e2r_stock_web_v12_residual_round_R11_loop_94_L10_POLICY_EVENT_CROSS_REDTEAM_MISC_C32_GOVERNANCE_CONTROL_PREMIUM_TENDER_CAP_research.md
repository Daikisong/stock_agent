# E2R Stock-Web v12 Residual Research — R11 / Loop 94

```yaml
scheduled_round: R11
scheduled_loop: 94
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_TRANSFER_SALE_PROCESS_ACTIVIST_GOVERNANCE_PREMIUM_CAP_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE

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
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
corporate_action_caveat_avoided_count: 1
control_transfer_or_sale_process_case_count: 2
activist_governance_label_case_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 94
next_round: R12
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_94_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 94
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R11 can use L10 policy/event/cross-redteam miscellaneous. This file uses:

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

The selected fine branch is:

```text
control transfer / sale process / activist governance
control-premium cap and price-survival bridge
vs governance-label spike
```

This deliberately avoids the previous R11 loop93 Korea Value-up / holding-company C31 branch and the previous R11 loop92 public tender / delisting cap branch. It also avoids the C32 top-covered symbols.

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
003920 남양유업
001750 한양증권
003240 태광산업
```

They avoid the C32 top-covered list and avoid recent R11/R12 policy names:

```text
loop91 avoid: 000660, 005930, 000990
loop92 avoid: 003410, 115390, 119860
loop93 avoid: 402340, 001040, 034730
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
003920: same archetype, new symbol, control-transfer premium positive with 4B and later corporate-action caveat avoided
001750: same archetype, new symbol, sale-process / financial-control premium local-positive with 4B watch
003240: same archetype, new symbol, activist/governance label hard-4C without executable monetization bridge
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
003920 남양유업
  profile: atlas/symbol_profiles/003/003920.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,437
  non_tradable_zero_volume rows: 328
  corporate_action_candidate_dates:
    2024-11-20
  selected validation:
    uses 2024-02-19 entry and treats the 2024-11-20 corporate-action candidate as blocked.
    peak/worst-low calculations are taken before that candidate date.
  2024 entry~pre-2024-11-20 validation: usable with caveat

001750 한양증권
  profile: atlas/symbol_profiles/001/001750.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,765
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

003240 태광산업
  profile: atlas/symbol_profiles/003/003240.json
  first_date: 1995-05-06
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,608
  non_tradable_zero_volume rows: 157
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C32 is about governance, control premium, tender cap, and execution probability. It is not a generic "governance issue" or "low-float asset-rich stock" label.

The model can over-score:

```text
control transfer headline
sale process
activist governance label
low-float asset-rich company
control-premium expectation
tender-offer or privatization rumor
one-week governance-stock volume spike
```

The C32 bridge must be stricter:

```text
governance / control event
  -> identifiable buyer or controlling block
  -> deal price, tender price, or sale-process economics
  -> closing probability and legal path
  -> float, liquidity, and minority-shareholder treatment
  -> corporate-action / split / raw-price discontinuity check
  -> cap to deal economics
  -> price survival after the first control-premium spike
```

A governance event is like a locked gate. The headline says someone has a key, but C32 asks whether the key fits this lock, whether the buyer can close, what price is printed on the key, and whether minority holders can actually walk through the gate.

---

## 5. Case 1 — 003920 남양유업

```yaml
case_id: C32_R11L94_003920_2024_02_19
symbol: "003920"
name: "남양유업"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_TRANSFER_SALE_PROCESS_ACTIVIST_GOVERNANCE_PREMIUM_CAP_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE
trigger_date: 2024-02-19
entry_date: 2024-02-19
entry_price_basis: close
entry_price: 620000
classification: positive_capped_control_transfer_premium_with_4b_and_corporate_action_caveat
calibration_usable: true
```

### Evidence interpretation

남양유업 is the constructive C32 control, but with a strict cap.

The useful C32 read is:

```text
control-transfer resolution / governance overhang removal
  -> identifiable controlling-block economics
  -> control-premium price survival
  -> later corporate-action candidate avoided
```

The stock did not deliver a straight-line move. It had a large interim drawdown and then later recovered into new highs before the 2024-11-20 corporate-action candidate. This makes it a positive C32 case, but not an unrestricted Green. It needs 4B discipline and a hard corporate-action cutoff.

### Price path

Key Stock-Web rows:

```text
2024-02-19: high 632,000 / close 620,000
2024-04-08: low 499,000 / close 502,000
2024-08-05: low 472,000 / close 475,000
2024-09-09: low 465,000 / close 474,500
2024-10-31: high 696,000 / close 691,000
2024-11-05: high 720,000 / close 704,000
2024-11-20: corporate-action candidate window begins; post-candidate rows blocked
```

Approximate path from entry close, pre-corporate-action candidate:

```text
entry_close: 620,000
peak_high_before_candidate: 720,000
MFE: +16.1%
worst_low_before_candidate: 465,000
MAE: -25.0%
```

### Interpretation

This is a C32 positive with 4B and cap:

```text
Stage2-Actionable: valid if control-transfer, buyer, legal path, and minority treatment bridge are explicit.
Stage3-Green: blocked unless closing mechanics and cap economics are explicit.
Local 4B: required because positive MFE came after a large interim drawdown.
Hard 4C: no for the pre-corporate-action validation window.
Corporate-action caveat: post-2024-11-20 rows blocked.
```

### Stress-test components

```text
raw_component_score_proxy:
  control_transfer_relevance: high
  identifiable_buyer_or_block_bridge: high
  deal_closing_bridge: medium_high
  minority_shareholder_cap_bridge: medium
  price_survival: mixed_but_positive_before_candidate
  interim_mae_penalty: high
  local_4b_overlay: required
  corporate_action_caveat_avoided: yes
```

---

## 6. Case 2 — 001750 한양증권

```yaml
case_id: C32_R11L94_001750_2024_07_24
symbol: "001750"
name: "한양증권"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_TRANSFER_SALE_PROCESS_ACTIVIST_GOVERNANCE_PREMIUM_CAP_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 16000
classification: positive_local_sale_process_control_premium_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

한양증권 is the sale-process / control-premium local-positive case.

The useful C32 bridge is:

```text
financial company sale or control-premium process
  -> identifiable transaction expectation
  -> price confirmation from sale-process optionality
  -> later cap and drawdown discipline
```

The stock moved strongly after the July trigger, but the later path broke down as deal certainty and cap economics became less clean. That makes it a local positive / 4B case, not a Green.

### Price path

Key Stock-Web rows:

```text
2024-07-24: high 16,200 / close 16,000
2024-08-05: high 19,410 / close 16,160
2024-08-06: high 19,300 / close 18,350
2024-09-12: high 17,420 / close 17,310
2024-09-20: high 17,750 / close 15,760
2024-10-31: low 12,180 / close 12,350
```

Approximate path from entry close:

```text
entry_close: 16,000
peak_high: 19,410
MFE: +21.3%
worst_low_after_entry: 12,180
MAE: -23.9%
```

### Interpretation

This is a C32 local positive with 4B:

```text
Stage2-Actionable: possible if sale process, buyer, pricing range, and closing path are explicit.
Stage3-Green: blocked without confirmed tender/sale price and closing probability.
Local 4B: required after +20% MFE and later -20%+ MAE.
Hard 4C: no, because a meaningful tradable MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  sale_process_relevance: high
  control_premium_optional_value: medium_high
  transaction_price_bridge: weak_to_medium
  closing_probability_bridge: weak_to_medium
  price_confirmation: high_initial
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 7. Case 3 — 003240 태광산업

```yaml
case_id: C32_R11L94_003240_2024_02_01
symbol: "003240"
name: "태광산업"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: CONTROL_TRANSFER_SALE_PROCESS_ACTIVIST_GOVERNANCE_PREMIUM_CAP_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 943000
classification: hard_4c_candidate_activist_governance_asset_rich_label_without_executable_monetization_bridge
calibration_usable: true
```

### Evidence interpretation

태광산업 is the activist/governance hard guardrail.

The setup can look attractive:

```text
asset-rich / low-float company
governance activism label
minority value-unlock expectation
control-premium imagination
```

But from the selected entry, the forward price path did not validate an executable bridge. The MFE was almost absent, and the later MAE was extreme. This is a classic C32 false-positive: governance salience without tender, sale, monetization, or enforceable shareholder-return mechanics.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 950,000 / close 943,000
2024-02-06: low 774,000 / close 810,000
2024-04-17: low 621,000 / close 621,000
2024-08-05: low 510,000 / close 546,000
2024-09-27: high 676,000 / close 662,000
2024-11-05: high 673,000 / close 669,000
```

Approximate path from entry close:

```text
entry_close: 943,000
peak_high: 950,000
MFE: +0.7%
worst_low_after_entry: 510,000
MAE: -45.9%
```

### Interpretation

This is a hard C32 false-positive:

```text
Stage2-Watch: possible from governance/asset-rich relevance.
Stage2-Actionable: blocked unless tender, sale, asset monetization, buyback/cancellation, or enforceable shareholder-return bridge is explicit.
Stage3-Green: blocked.
Hard 4C: yes by near-zero MFE and very high MAE.
```

The lesson is that governance label is not control-premium realization.

### Stress-test components

```text
raw_component_score_proxy:
  governance_label: high
  asset_rich_low_float_relevance: high
  executable_monetization_bridge: weak
  tender_or_control_transaction_bridge: absent
  price_confirmation: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
corporate_action_caveat_avoided_count: 1
control_transfer_or_sale_process_case_count: 2
activist_governance_label_case_count: 1
calibration_usable_trigger_count: 3
```

The three-case C32 governance/control grid:

```text
003920 남양유업:
  control-transfer positive, but only with cap and 4B;
  later corporate-action candidate is blocked.

001750 한양증권:
  sale-process / control-premium local positive;
  meaningful MFE came first, but later MAE requires 4B and closing-price discipline.

003240 태광산업:
  governance/asset-rich label failed;
  near-zero MFE and high MAE, hard 4C.
```

Shared rule:

```text
C32 is not "governance label is interesting."
C32 is "control event has identifiable buyer, price, closing path, minority-holder economics, and price survival."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C32_R11L94_003920_2024_02_19","scheduled_round":"R11","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_TRANSFER_SALE_PROCESS_ACTIVIST_GOVERNANCE_PREMIUM_CAP_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","symbol":"003920","name":"남양유업","trigger_date":"2024-02-19","entry_date":"2024-02-19","entry_price":620000,"peak_high_before_corporate_action_candidate":720000,"peak_date":"2024-11-05","worst_low_before_corporate_action_candidate":465000,"worst_low_date":"2024-09-09","mfe_pct":16.1,"mae_pct":-25.0,"classification":"positive_capped_control_transfer_premium_with_4b_and_corporate_action_caveat","calibration_usable":true,"corporate_action_caveat_avoided":true,"evidence_family":"control_transfer_premium_resolution_with_minor_holder_cap_and_corporate_action_cutoff","residual_error":"control_transfer_positive_still_requires_4b_after_interim_mae_and_corporate_action_cutoff","shadow_rule_candidate":"allow_capped_actionable_when_control_transfer_buyer_and_closing_path_confirm_but_attach_4b_after_large_interim_mae"}
{"row_type":"case","case_id":"C32_R11L94_001750_2024_07_24","scheduled_round":"R11","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_TRANSFER_SALE_PROCESS_ACTIVIST_GOVERNANCE_PREMIUM_CAP_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","symbol":"001750","name":"한양증권","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":16000,"peak_high":19410,"peak_date":"2024-08-05","worst_low_after_entry":12180,"worst_low_after_entry_date":"2024-10-31","mfe_pct":21.3,"mae_pct":-23.9,"classification":"positive_local_sale_process_control_premium_with_4b_watch","calibration_usable":true,"evidence_family":"financial_company_sale_process_control_premium_optionality_without_final_price_certainty","residual_error":"sale_process_can_create_mfe_but_green_requires_final_buyer_price_and_closing_probability","shadow_rule_candidate":"classify_sale_process_mfe_with_later_mae_as_local_4b_until_tender_or_sale_price_confirmed"}
{"row_type":"case","case_id":"C32_R11L94_003240_2024_02_01","scheduled_round":"R11","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_TRANSFER_SALE_PROCESS_ACTIVIST_GOVERNANCE_PREMIUM_CAP_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","symbol":"003240","name":"태광산업","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":943000,"peak_high":950000,"peak_date":"2024-02-01","worst_low_after_entry":510000,"worst_low_after_entry_date":"2024-08-05","mfe_pct":0.7,"mae_pct":-45.9,"classification":"hard_4c_candidate_activist_governance_asset_rich_label_without_executable_monetization_bridge","calibration_usable":true,"evidence_family":"activist_governance_asset_rich_label_without_tender_sale_asset_monetization_bridge","residual_error":"governance_salience_can_overpromote_without_executable_control_premium_or_shareholder_return_path","shadow_rule_candidate":"route_asset_rich_governance_label_to_hard_4c_if_mfe_near_zero_mae_large_and_monetization_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"CONTROL_TRANSFER_SALE_PROCESS_ACTIVIST_GOVERNANCE_PREMIUM_CAP_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"corporate_action_caveat_avoided_count":1,"control_transfer_or_sale_process_case_count":2,"activist_governance_label_case_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":94,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule_id":"C32_CONTROL_EVENT_PRICE_CLOSING_MINORITY_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C32, do not open Stage2-Actionable or Stage3-Green from governance, asset-rich, low-float, control-transfer rumor, sale-process, activist campaign, tender-offer expectation, or one-week governance-stock spike labels alone. Require identifiable buyer or controlling block, transaction/tender/sale price or credible pricing range, closing probability and legal path, float/liquidity and minority-shareholder economics, corporate-action/raw-discontinuity check, and post-trigger price survival. Control-transfer positives may be capped Actionable only when buyer, closing path, and minority economics are explicit. Sale-process cases with meaningful MFE but later MAE should remain local 4B until final buyer/price/closing evidence appears. Asset-rich governance labels with near-zero MFE and high MAE should route to hard-4C when executable monetization or shareholder-return bridge is missing.","expected_effect":"Reduce governance-label and asset-rich false positives while preserving true control-transfer or sale-process positives with explicit price, closing, and minority-holder economics.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":94,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"control_event_price_closing_minority_guard","contribution":"Adds one control-transfer positive with corporate-action cutoff, one sale-process local 4B positive, and one activist/governance hard-4C counterexample to calibrate C32 control-premium and minority-economics requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C32_CONTROL_EVENT_PRICE_CLOSING_MINORITY_BRIDGE_REQUIRED

IF canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:

  Do not open Stage3-Green from:
    - governance label alone
    - asset-rich / low-float label alone
    - control-transfer rumor alone
    - sale-process headline alone
    - activist campaign alone
    - tender-offer expectation alone
    - one-week governance-stock spike alone

  Require at least two of:
    - identifiable buyer / controlling block
    - transaction, tender, or sale price
    - credible price range and cap mechanics
    - closing probability and legal path
    - float / liquidity / minority-shareholder treatment
    - corporate-action or raw-price discontinuity check
    - low-MAE post-trigger price survival
    - fresh evidence after the governance headline

  If MFE < 5% and MAE < -30%:
    route to C32 hard-4C candidate.

  If MFE is meaningful but interim MAE is large:
    preserve as local 4B / capped positive until final buyer, price, and closing path are explicit.

  If corporate-action candidate appears inside the validation window:
    block post-candidate rows and require raw-price discontinuity caution.

  Distinguish:
    - control-transfer/sale-process cases where the key fits the lock
    - from governance or asset-rich labels where no executable transaction or shareholder-return path exists.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_94_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C32 governance/control-premium cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C32_CONTROL_EVENT_PRICE_CLOSING_MINORITY_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C32 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C32 cases agree, consider implementing a canonical guard that:
   - blocks governance-label Green without buyer/price/closing/minority bridge,
   - preserves control-transfer positives only with price survival and corporate-action cutoff,
   - keeps sale-process MFE with later MAE as local 4B,
   - routes near-zero-MFE/high-MAE asset-rich governance labels to hard-4C,
   - applies raw-price/corporate-action cutoffs inside validation windows.

Expected next schedule:
completed_round = R11
completed_loop = 94
next_round = R12
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R11
completed_loop = 94
next_round = R12
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
