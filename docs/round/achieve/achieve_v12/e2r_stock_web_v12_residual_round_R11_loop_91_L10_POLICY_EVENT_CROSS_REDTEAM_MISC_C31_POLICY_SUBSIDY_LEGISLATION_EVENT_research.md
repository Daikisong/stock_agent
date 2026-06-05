# E2R Stock-Web v12 Residual Research — R11 / Loop 91

```yaml
scheduled_round: R11
scheduled_loop: 91
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: AI_SEMICONDUCTOR_POLICY_FUND_TO_COMPANY_EARNINGS_BRIDGE_VS_GENERIC_CHIP_POLICY_BETA

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
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 91
next_round: R12
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_91_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 91
```

R11 can use:

```text
L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

unless the branch is explicitly policy-defense-linked. This run selects L10 and C31 because the branch is a national policy / subsidy / industrial-strategy event rather than ordinary semiconductor-sector research.

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

Selected symbols:

```text
000660 SK하이닉스
005930 삼성전자
000990 DB하이텍
```

These avoid the C31 top-covered symbols and avoid recent R11 loop90 Doosan C32 names:

```text
454910, 034020, 241560
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
000660: same archetype, new symbol, direct AI memory / HBM policy-beneficiary bridge
005930: same archetype, new symbol, broad national champion / execution-gap policy beta branch
000990: same archetype, new symbol, legacy foundry / system semiconductor policy label local-burst branch
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
000660 SK하이닉스
  profile: atlas/symbol_profiles/000/000660.json
  first_date: 1997-01-03
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,263
  corporate_action_candidate_dates:
    1998-07-03, 1999-01-07, 1999-07-06, 1999-10-27, 2000-01-07,
    2001-06-27, 2002-06-07, 2003-04-14, 2003-04-21
  2024 entry~D+180 contamination: none

005930 삼성전자
  profile: atlas/symbol_profiles/005/005930.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,761
  corporate_action_candidate_dates:
    1996-01-03, 1997-01-03, 2018-05-04
  2024 entry~D+180 contamination: none

000990 DB하이텍
  profile: atlas/symbol_profiles/000/000990.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,763
  corporate_action_candidate_dates:
    1997-04-01, 1997-11-07, 1999-06-11, 2007-05-21
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-04-09
South Korea AI semiconductor policy / subsidy event:
  - 9.4 trillion won AI investment by 2027
  - separate 1.4 trillion won fund for AI semiconductor firms
  - national effort to protect semiconductor leadership and AI chip competitiveness
```

This is a C31 policy/subsidy/legislation event, not an ordinary R2 semiconductor case. The policy was real, but the investable bridge is not universal.

The model can over-score:

```text
AI policy
semiconductor subsidy
national champion
system semiconductor target
semiconductor supply-chain support
```

The correct bridge is narrower:

```text
policy or subsidy
  -> company-specific exposure
  -> actual product/customer fit
  -> CAPEX or R&D funding relevance
  -> revenue or margin conversion
  -> execution gap check
  -> post-trigger price survival
```

A policy fund is like irrigation water. It matters only if the company owns a field connected to the channel and can turn the water into a crop.

---

## 5. Case 1 — 000660 SK하이닉스

```yaml
case_id: C31_R11L91_000660_2024_04_09
symbol: "000660"
name: "SK하이닉스"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: AI_SEMICONDUCTOR_POLICY_FUND_TO_COMPANY_EARNINGS_BRIDGE_VS_GENERIC_CHIP_POLICY_BETA
trigger_date: 2024-04-09
entry_date: 2024-04-09
entry_price_basis: close
entry_price: 182900
classification: positive_direct_ai_memory_hbm_policy_bridge_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

SK하이닉스 is the strongest policy-to-company bridge in this set.

The C31 bridge is not simply:

```text
AI policy exists.
```

It is:

```text
AI policy and national semiconductor support
  -> direct HBM / AI memory exposure
  -> customer demand and capacity expansion
  -> revenue and margin revision
  -> price confirmation
```

This is why SK하이닉스 worked better than broad or indirect semiconductor names.

### Price path

Key Stock-Web rows:

```text
2024-04-09: close 182,900
2024-05-23: high 204,000 / close 200,000
2024-06-13: high 226,500 / close 222,000
2024-06-19: high 243,000 / close 233,500
2024-07-11: high 248,500 / close 241,000
2024-09-09: low 150,500 / close 157,000
```

Approximate path from entry close:

```text
entry_close: 182,900
peak_high: 248,500
MFE: +35.9%
worst_low_after_peak: 150,500
MAE vs entry: -17.7%
peak_to_later_low_drawdown: -39.4%
```

### Interpretation

This is a positive but not a free Green.

```text
Stage2-Actionable: valid when direct HBM/AI memory product bridge is explicit.
Stage3-Green: allowed only when customer demand, capacity, and margin revision confirm.
Local 4B: required after +35% MFE and ~40% peak drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  policy_relevance: high
  direct_ai_memory_exposure: high
  product_customer_fit: high
  earnings_revision_bridge: high
  price_confirmation: high
  drawdown_after_peak: high
  local_4b_overlay: required
```

---

## 6. Case 2 — 005930 삼성전자

```yaml
case_id: C31_R11L91_005930_2024_04_09
symbol: "005930"
name: "삼성전자"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: AI_SEMICONDUCTOR_POLICY_FUND_TO_COMPANY_EARNINGS_BRIDGE_VS_GENERIC_CHIP_POLICY_BETA
trigger_date: 2024-04-09
entry_date: 2024-04-09
entry_price_basis: close
entry_price: 83600
classification: hard_4c_candidate_national_champion_policy_beta_without_execution_bridge
calibration_usable: true
```

### Evidence interpretation

삼성전자는 national champion으로 정책 관련성이 크다. 그러나 C31은 정책 관련성 자체가 아니라 정책이 실제 execution bridge로 연결되는지를 묻는다.

The failure mode:

```text
national AI semiconductor policy
  -> broad Samsung policy beta
  -> model opens Green
  -> HBM/execution gap and memory-cycle uncertainty remain
  -> high MAE follows
```

The policy was real. The company is real. The bridge at this trigger was not enough for Green.

### Price path

Key Stock-Web rows:

```text
2024-04-09: close 83,600
2024-04-15: low 81,200 / close 82,200
2024-07-05: high 87,100 / close 87,100
2024-07-08: high 88,600 / close 87,400
2024-09-19: low 62,200 / close 63,100
2024-11-14: low 49,900 / close 49,900
```

Approximate path from entry close:

```text
entry_close: 83,600
peak_high: 88,600
MFE: +6.0%
worst_low: 49,900
MAE: -40.3%
```

### Interpretation

This is the hard C31 guardrail case.

```text
Stage2-Watch: valid from national policy relevance.
Stage2-Actionable: blocked unless AI/HBM execution and earnings bridge are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes.
```

The lesson is that national champion status can be a halo, but a halo is not an earnings bridge.

### Stress-test components

```text
raw_component_score_proxy:
  policy_relevance: high
  national_champion_status: high
  direct_ai_execution_bridge: weak_to_medium_at_trigger
  hbm_execution_gap_penalty: high
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: required
```

---

## 7. Case 3 — 000990 DB하이텍

```yaml
case_id: C31_R11L91_000990_2024_04_09
symbol: "000990"
name: "DB하이텍"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: AI_SEMICONDUCTOR_POLICY_FUND_TO_COMPANY_EARNINGS_BRIDGE_VS_GENERIC_CHIP_POLICY_BETA
trigger_date: 2024-04-09
entry_date: 2024-04-09
entry_price_basis: close
entry_price: 44300
classification: local_burst_but_high_mae_legacy_foundry_policy_label
calibration_usable: true
```

### Evidence interpretation

DB하이텍 is the indirect semiconductor-policy case. It had a plausible label:

```text
system semiconductor / foundry / domestic chip supply chain
```

But C31 should not read that label as the same as AI semiconductor policy monetization. The forward path produced a strong local burst in June, then failed price survival.

This is the exact C31 4B boundary:

```text
policy label can create a trade
but not durable Green without revenue/margin conversion
```

### Price path

Key Stock-Web rows:

```text
2024-04-09: close 44,300
2024-05-23: high 46,150 / close 44,700
2024-06-18: high 46,450 / close 45,400
2024-06-20: high 58,900 / close 57,100
2024-07-04: high 52,500 / close 52,000
2024-09-09: low 35,200 / close 36,650
2024-11-13: low 31,400 / close 31,600
```

Approximate path from entry close:

```text
entry_close: 44,300
peak_high: 58,900
MFE: +33.0%
worst_low: 31,400
MAE: -29.1%
peak_to_later_low_drawdown: -46.7%
```

### Interpretation

This is a local-burst / high-MAE counterexample:

```text
Stage2-Watch: valid.
Stage2-Actionable: possible only as local 4B if event trading rules are explicit.
Stage3-Green: blocked without customer/product/margin bridge.
Hard 4C: borderline, but primary label is local burst failure.
```

### Stress-test components

```text
raw_component_score_proxy:
  policy_relevance: medium
  system_semiconductor_label: high
  direct_ai_revenue_bridge: weak
  margin_conversion_visibility: weak
  local_price_burst: high
  price_survival: failed
  drawdown_penalty: high
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C31 policy grid:

```text
000660 SK하이닉스:
  direct AI memory/HBM bridge;
  positive, but local 4B after large MFE and peak drawdown.

005930 삼성전자:
  national champion policy halo;
  shallow MFE and high MAE without explicit execution bridge.

000990 DB하이텍:
  system semiconductor / foundry policy label;
  strong local burst but failed durable price survival.
```

Shared rule:

```text
C31 semiconductor policy is not "all chip stocks benefit."
C31 semiconductor policy is "policy money and national strategy flow through the exact product, customer, CAPEX, and margin bridge of this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R11L91_000660_2024_04_09","scheduled_round":"R11","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AI_SEMICONDUCTOR_POLICY_FUND_TO_COMPANY_EARNINGS_BRIDGE_VS_GENERIC_CHIP_POLICY_BETA","symbol":"000660","name":"SK하이닉스","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":182900,"peak_high":248500,"peak_date":"2024-07-11","worst_low_after_peak":150500,"worst_low_after_peak_date":"2024-09-09","mfe_pct":35.9,"mae_pct":-17.7,"peak_to_later_low_drawdown_pct":-39.4,"classification":"positive_direct_ai_memory_hbm_policy_bridge_with_4b_watch","calibration_usable":true,"evidence_family":"direct_ai_memory_hbm_policy_product_customer_margin_bridge","residual_error":"positive_entry_but_large_drawdown_requires_local_4b_overlay","shadow_rule_candidate":"allow_actionable_when_policy_maps_to_direct_hbm_product_customer_margin_bridge; attach_4b_after_large_peak_drawdown"}
{"row_type":"case","case_id":"C31_R11L91_005930_2024_04_09","scheduled_round":"R11","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AI_SEMICONDUCTOR_POLICY_FUND_TO_COMPANY_EARNINGS_BRIDGE_VS_GENERIC_CHIP_POLICY_BETA","symbol":"005930","name":"삼성전자","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":83600,"peak_high":88600,"peak_date":"2024-07-08","worst_low":49900,"worst_low_date":"2024-11-14","mfe_pct":6.0,"mae_pct":-40.3,"classification":"hard_4c_candidate_national_champion_policy_beta_without_execution_bridge","calibration_usable":true,"evidence_family":"national_champion_chip_policy_beta_without_ai_hbm_execution_bridge","residual_error":"national_policy_halo_can_overpromote_to_green_without_company_specific_execution_bridge","shadow_rule_candidate":"block_actionable_green_when_policy_relevance_high_but_mfe_shallow_mae_large_and_execution_gap_unresolved"}
{"row_type":"case","case_id":"C31_R11L91_000990_2024_04_09","scheduled_round":"R11","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AI_SEMICONDUCTOR_POLICY_FUND_TO_COMPANY_EARNINGS_BRIDGE_VS_GENERIC_CHIP_POLICY_BETA","symbol":"000990","name":"DB하이텍","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":44300,"peak_high":58900,"peak_date":"2024-06-20","worst_low":31400,"worst_low_date":"2024-11-13","mfe_pct":33.0,"mae_pct":-29.1,"peak_to_later_low_drawdown_pct":-46.7,"classification":"local_burst_but_high_mae_legacy_foundry_policy_label","calibration_usable":true,"evidence_family":"system_semiconductor_foundry_policy_label_without_direct_ai_revenue_margin_bridge","residual_error":"policy_label_can_create_local_burst_but_fail_price_survival_without_margin_bridge","shadow_rule_candidate":"keep_indirect_policy_label_burst_as_4b_watch_not_green_if_product_customer_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AI_SEMICONDUCTOR_POLICY_FUND_TO_COMPANY_EARNINGS_BRIDGE_VS_GENERIC_CHIP_POLICY_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":91,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_POLICY_TO_COMPANY_EARNINGS_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 semiconductor/AI policy events, do not open Stage2-Actionable or Stage3-Green from national semiconductor policy, subsidy, fund, AI initiative, or national champion label alone. Require company-specific product exposure, customer demand, CAPEX/R&D funding relevance, execution bridge, revenue and margin conversion, and post-trigger price survival. Direct HBM/AI memory beneficiaries may be Actionable when product/customer/margin bridge is explicit. Broad national champion or legacy foundry labels should cap at Watch/4B unless execution and margin bridge confirm. Shallow-MFE/high-MAE cases route to hard-4C.","expected_effect":"Preserve direct AI-memory policy positives while reducing broad semiconductor-policy halo false positives and indirect foundry label local-burst failures.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":91,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"ai_semiconductor_policy_to_company_earnings_bridge_guard","contribution":"Adds one direct HBM/AI-memory policy positive, one national-champion hard-4C candidate, and one indirect foundry local-burst failure to calibrate C31 policy-recipient mapping.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_POLICY_TO_COMPANY_EARNINGS_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [AI_semiconductor, chip_subsidy, national_industrial_strategy]:

  Do not open Stage3-Green from:
    - national AI semiconductor policy headline alone
    - subsidy or policy fund headline alone
    - national champion status alone
    - system semiconductor label alone
    - one-month semiconductor policy beta alone

  Require at least two of:
    - direct product exposure to the policy target
    - customer demand or named customer bridge
    - CAPEX/R&D funding relevance
    - execution gap check
    - revenue or margin revision
    - low-MAE post-trigger price survival
    - new evidence after policy headline

  If MFE < 10% and MAE < -30%:
    route to C31 hard-4C candidate.

  If MFE > 25% but peak-to-later-low drawdown > -35%:
    preserve as positive or local burst only with 4B watch unless fresh revision bridge appears.

  Distinguish:
    - direct HBM/AI memory beneficiaries
    - from broad national champion or legacy foundry policy labels without company-specific earnings conversion.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 AI-semiconductor policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_POLICY_TO_COMPANY_EARNINGS_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 policy cases agree, consider implementing a canonical guard that:
   - blocks policy/subsidy/national-champion Green without company-specific product/customer/margin bridge,
   - preserves direct HBM/AI-memory positives with price survival,
   - attaches local 4B after large MFE and deep peak drawdown,
   - routes shallow-MFE/high-MAE broad policy-beta cases to hard-4C.

Expected next schedule:
completed_round = R11
completed_loop = 91
next_round = R12
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R11
completed_loop = 91
next_round = R12
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
