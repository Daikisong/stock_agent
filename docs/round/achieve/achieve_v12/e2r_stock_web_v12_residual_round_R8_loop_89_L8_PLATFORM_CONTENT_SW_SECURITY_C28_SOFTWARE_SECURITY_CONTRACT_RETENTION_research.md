# E2R Stock-Web v12 Residual Research — R8 / Loop 89 / L8 / C28

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R8
scheduled_loop: 89
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_SOFTWARE_SECURITY_CONTRACT_RETENTION_REVENUE_BRIDGE_VS_HEADLINE_PRICE_ONLY_FADE

output_format: one_standalone_markdown_file
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

price_source_repo: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
reused_case_count: 0
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 89
next_round: R9
next_loop: 89
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Research intent

This run continues the sequential v12 scheduler after:

```text
previous_completed_round = R7
previous_completed_loop  = 89
previous_next_round      = R8
previous_next_loop       = 89
```

The R8 hard gate requires `L8_PLATFORM_CONTENT_SW_SECURITY`, so this file avoids additional bio/healthcare or consumer/financial cases and focuses only on platform/content/software/security residuals.

The previous R8 loop 88 already covered `C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE`, so this run intentionally shifts to `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION`.

C28 is a useful residual target because the No-Repeat index shows it is not as over-covered as C21/C29/C30/C31 and has no explicit 4B/4C rows in the current summary:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
rows = 26
symbols = 19
positive/counterexample = 10/4
4B/4C = 0/0
top repeated symbols = 058970, 150900, 042510, 203650, 307950, 012510
```

This run therefore avoids the top repeated symbols and selects three new C28 symbols:

```text
030520  한글과컴퓨터
047560  이스트소프트
053800  안랩
```

The residual question is:

> When software/security/AI headlines create a sharp price move, does the E2R model require real recurring revenue, enterprise contract retention, renewal expansion, ARR-like visibility, or margin/EPS conversion before allowing Stage2-Actionable / Stage3-Green?  
> Or can it be fooled by price-only AI/security momentum?

---

## 2. Novelty and duplicate check

### Hard duplicate key

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

### Selected rows

| symbol | name | trigger_type | entry_date | duplicate_status |
|---|---:|---|---:|---|
| 030520 | 한글과컴퓨터 | Stage2-Actionable-Candidate + Local-4B | 2024-01-08 | new C28 symbol/date/trigger |
| 047560 | 이스트소프트 | Stage4B-Local / Stage2-FalsePositive-Candidate | 2024-01-08 | new C28 symbol/date/trigger |
| 053800 | 안랩 | Stage2-FalsePositive-Candidate | 2024-01-25 | new C28 symbol/date/trigger |

These do not repeat the top-covered C28 combinations listed in the No-Repeat Index:

```text
058970, 150900, 042510, 203650, 307950, 012510
```

---

## 3. Stock-web profile validation

| symbol | tradable status | profile years include trigger year | corporate-action caveat relevant to 2024~D+180? | calibration usable |
|---|---:|---:|---:|---:|
| 030520 | active_like | yes | historical candidates only: 1997~2006 | true |
| 047560 | active_like | yes | historical candidates only: 2015 | true |
| 053800 | active_like | yes | historical candidate only: 2005 | true |

All three selected windows are outside the listed corporate-action candidate dates, so the 30D/90D/180D rows are usable under the default v12 rule.

---

## 4. Case table

### 4.1 030520 한글과컴퓨터 — AI office/document software momentum that did produce early MFE but needed 4B discipline

```yaml
symbol: "030520"
name: "한글과컴퓨터"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_OFFICE_DOCUMENT_SOFTWARE_REVENUE_BRIDGE_VS_AI_HEADLINE_PRICE_SPIKE
trigger_type: Stage2-Actionable-Candidate + Local-4B
entry_date: 2024-01-08
entry_price_close: 19460
entry_basis: next_tradable_or_same_day_close
calibration_usable: true

price_path:
  D0_close: 19460
  local_peak_date: 2024-01-22
  local_peak_high: 38450
  local_MFE_pct: 97.59
  local_peak_close: 35150
  local_close_MFE_pct: 80.63
  later_low_date: 2024-08-05
  later_low: 15100
  MAE_vs_entry_pct: -22.40

classification:
  outcome_label: positive_with_local_4b_overlay
  positive_case: true
  counterexample: false
  local_4b_overlay: true
  hard_4c_candidate: false
```

#### Interpretation

Hancom behaved like a classic C28 early positive: the stock-web path shows a fast rerating from the January AI/software trigger zone. A document productivity company can plausibly convert AI features into paid software upgrades, cloud office adoption, enterprise seats, and operating leverage.

But the path also shows why C28 should not blindly treat software/AI headlines as Green. A move from 19,460 to 38,450 happened very quickly, but the later 180D window also reached 15,100. That means the trigger worked as a high-MFE opportunity but needed local-4B discipline once price ran far ahead of revenue/contract-retention confirmation.

#### Raw component score sketch

```yaml
raw_component_score_breakdown:
  evidence_revision: 44
  business_quality_bridge: 30
  price_path_alignment: 24
  risk_guardrail_penalty: -12
  local_4b_penalty: -8
  estimated_total_before_stage_gate: 78
  stage_call:
    baseline_profile: Stage2-Actionable
    calibrated_profile: Stage2-Actionable with local-4B overlay
    green_allowed: false
```

#### Rule lesson

```text
C28 positive should require at least one of:
- paid AI software adoption / enterprise seat expansion,
- cloud transition with recurring revenue visibility,
- renewal/retention data,
- margin/EPS bridge.

If only AI headline + price breakout exists, allow Stage2 watch/actionable only with 4B proximity guard.
```

---

### 4.2 047560 이스트소프트 — AI software/avatar momentum that became a local-4B trap

```yaml
symbol: "047560"
name: "이스트소프트"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_AVATAR_SOFTWARE_HEADLINE_VS_RECURRING_REVENUE_CONTRACT_BRIDGE
trigger_type: Stage4B-Local / Stage2-FalsePositive-Candidate
entry_date: 2024-01-08
entry_price_close: 25650
entry_basis: next_tradable_or_same_day_close
calibration_usable: true

price_path:
  D0_close: 25650
  local_peak_date: 2024-01-29
  local_peak_high: 49800
  local_MFE_pct: 94.15
  later_low_date: 2024-08-05
  later_low: 11220
  MAE_vs_entry_pct: -56.26

classification:
  outcome_label: local_4b_then_hard_4c_candidate
  positive_case: false
  counterexample: true
  local_4b_overlay: true
  hard_4c_candidate: true
```

#### Interpretation

ESTsoft is the sharper residual error. The January 2024 AI/software theme produced nearly a double in the raw path, but the move then collapsed into a deep drawdown. This is exactly where C28 needs to separate “AI software headline” from “contract-retained recurring software business.”

A price-only model could mark this as a spectacular winner. A calibrated trigger-level model should instead say:

```text
MFE exists, but the quality of the trigger is insufficient for Green.
Price-only blowoff => local 4B.
If recurring revenue / enterprise contract / margin conversion is absent, full-window rerating is blocked.
```

#### Raw component score sketch

```yaml
raw_component_score_breakdown:
  evidence_revision: 24
  business_quality_bridge: 14
  price_path_alignment_30D: 30
  price_path_alignment_180D: -20
  price_only_blowoff_penalty: -18
  contract_retention_absence_penalty: -14
  estimated_total_before_stage_gate: 52
  stage_call:
    baseline_profile: could_over_promote_due_to_MFE
    calibrated_profile: Stage4B-local / Stage2 false-positive candidate
    green_allowed: false
    hard_4c_watch: true
```

#### Rule lesson

```text
For C28, AI/software headline should not count as contract-retention evidence.
A fast 30D/60D MFE without recurring revenue proof should be treated as local 4B, not Green.
```

---

### 4.3 053800 안랩 — real cybersecurity franchise, but no acceleration bridge

```yaml
symbol: "053800"
name: "안랩"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: CYBERSECURITY_STABLE_CONTRACT_BASE_WITHOUT_NEW_ACCELERATION_BRIDGE
trigger_type: Stage2-FalsePositive-Candidate
entry_date: 2024-01-25
entry_price_close: 74000
entry_basis: same_day_close
calibration_usable: true

price_path:
  D0_close: 74000
  local_peak_date: 2024-01-29
  local_peak_high: 75800
  local_MFE_pct: 2.43
  later_low_date: 2024-08-05
  later_low: 51600
  MAE_vs_entry_pct: -30.27

classification:
  outcome_label: counterexample
  positive_case: false
  counterexample: true
  local_4b_overlay: false
  hard_4c_candidate: false
```

#### Interpretation

AhnLab is a different kind of C28 counterexample. It is not a speculative AI blowoff; it is a real cybersecurity franchise. But a real security business is not automatically an E2R rerating trigger. The stock-web path after the January trigger zone shows almost no MFE and meaningful drawdown.

This implies that C28 should not reward “cybersecurity is structurally important” as if it were a fresh earnings acceleration. The model needs evidence of:

```text
- contract win / renewal expansion,
- ARR-like or managed-security service growth,
- margin leverage,
- EPS/OP revision,
- cross-sell or cloud/security product adoption.
```

Without that bridge, stable cybersecurity quality is a business description, not a trigger.

#### Raw component score sketch

```yaml
raw_component_score_breakdown:
  evidence_revision: 18
  business_quality_bridge: 22
  price_path_alignment: -8
  contract_retention_visibility: 12
  acceleration_absence_penalty: -18
  estimated_total_before_stage_gate: 26
  stage_call:
    baseline_profile: Watch
    calibrated_profile: Stage2 false-positive candidate / no actionable upgrade
    green_allowed: false
```

---

## 5. Aggregate backtest table

| symbol | entry date | entry close | peak high in inspected window | MFE | low in inspected window | MAE | label |
|---|---:|---:|---:|---:|---:|---:|---|
| 030520 | 2024-01-08 | 19,460 | 38,450 | +97.6% | 15,100 | -22.4% | positive + local 4B |
| 047560 | 2024-01-08 | 25,650 | 49,800 | +94.2% | 11,220 | -56.3% | local 4B / hard 4C candidate |
| 053800 | 2024-01-25 | 74,000 | 75,800 | +2.4% | 51,600 | -30.3% | counterexample |

Aggregate interpretation:

```yaml
aggregate:
  usable_trigger_count: 3
  positive: 1
  counterexample: 2
  local_4b: 2
  hard_4c_candidate: 1
  calibration_weight_use: residual_rule_candidate_only
```

This is not a request to change global weights. The sample says C28 needs a stricter archetype-specific bridge:

```text
software_or_security_headline_score should be capped unless:
  recurring_revenue_visibility == true
  OR enterprise_contract_retention_expansion == true
  OR named_customer / renewal / ARR / margin bridge exists
```

---

## 6. Score-return alignment stress test

### 6.1 What the current calibrated profile already handles well

The v12 calibrated profile already has several protective concepts:

```text
- price-only blowoff should not upgrade to positive stage by itself
- full 4B requires non-price evidence
- hard 4C routes to 4C
- Stage3 Green requires evidence breadth, not only price
```

These are highly relevant for C28 because two very different failure modes appear:

```text
1. AI software price-only blowoff:
   047560, and partially 030520 after the early MFE.
2. Quality/stable cybersecurity business without acceleration:
   053800.
```

### 6.2 Residual error

The remaining risk is not that the model misses the existence of price momentum. The risk is that it sees software/security labels and treats them as automatically recurring, high-margin, scalable, and therefore Stage2/Green-worthy.

That is structurally wrong. Software and security are like a subscription gym: a membership base matters, but the rerating comes when retention, ARPU, seat expansion, and operating leverage show up. A signboard that says “AI gym” does not prove members are paying more or staying longer.

---

## 7. Proposed C28 shadow rule candidate

```yaml
rule_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_BRIDGE_GATE
rule_type: canonical_archetype_specific_shadow_rule
production_scoring_changed: false
do_not_apply_now: true

trigger_scope:
  canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY

positive_gate:
  require_any:
    - named_enterprise_contract_or_renewal_expansion
    - recurring_revenue_or_subscription_metric_growth
    - ARR_like_visibility_or_cloud_seat_expansion
    - cyber_security_managed_service_order_growth
    - operating_margin_or_EPS_revision_bridge

guardrail:
  if software_AI_security_headline_only and no_revenue_contract_bridge:
    max_stage: Watch_or_Stage2_Yellow
    block_stage3_green: true

  if local_MFE_ge_50pct_with_no_non_price_bridge:
    set_local_4b_overlay: true
    block_full_green: true

  if 90D_or_180D_MAE_le_-35pct after local_MFE_ge_50pct:
    mark_hard_4c_candidate: true
```

---

## 8. JSONL usable trigger rows

```jsonl
{"research_session":"post_calibrated_sector_archetype_residual_research","scheduled_round":"R8","scheduled_loop":89,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_DOCUMENT_SOFTWARE_REVENUE_BRIDGE_VS_AI_HEADLINE_PRICE_SPIKE","symbol":"030520","name":"한글과컴퓨터","trigger_type":"Stage2-Actionable-Candidate+Local-4B","entry_date":"2024-01-08","entry_price":19460,"price_basis":"tradable_raw","peak_high":38450,"peak_high_date":"2024-01-22","mfe_pct":97.59,"low_after_entry":15100,"low_after_entry_date":"2024-08-05","mae_pct":-22.40,"outcome_label":"positive_with_local_4b_overlay","positive_case":true,"counterexample":false,"local_4b_overlay":true,"hard_4c_candidate":false,"calibration_usable":true,"production_scoring_changed":false}
{"research_session":"post_calibrated_sector_archetype_residual_research","scheduled_round":"R8","scheduled_loop":89,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_AVATAR_SOFTWARE_HEADLINE_VS_RECURRING_REVENUE_CONTRACT_BRIDGE","symbol":"047560","name":"이스트소프트","trigger_type":"Stage4B-Local+Stage2-FalsePositive-Candidate","entry_date":"2024-01-08","entry_price":25650,"price_basis":"tradable_raw","peak_high":49800,"peak_high_date":"2024-01-29","mfe_pct":94.15,"low_after_entry":11220,"low_after_entry_date":"2024-08-05","mae_pct":-56.26,"outcome_label":"local_4b_then_hard_4c_candidate","positive_case":false,"counterexample":true,"local_4b_overlay":true,"hard_4c_candidate":true,"calibration_usable":true,"production_scoring_changed":false}
{"research_session":"post_calibrated_sector_archetype_residual_research","scheduled_round":"R8","scheduled_loop":89,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_STABLE_CONTRACT_BASE_WITHOUT_NEW_ACCELERATION_BRIDGE","symbol":"053800","name":"안랩","trigger_type":"Stage2-FalsePositive-Candidate","entry_date":"2024-01-25","entry_price":74000,"price_basis":"tradable_raw","peak_high":75800,"peak_high_date":"2024-01-29","mfe_pct":2.43,"low_after_entry":51600,"low_after_entry_date":"2024-08-05","mae_pct":-30.27,"outcome_label":"counterexample","positive_case":false,"counterexample":true,"local_4b_overlay":false,"hard_4c_candidate":false,"calibration_usable":true,"production_scoring_changed":false}
```

---

## 9. Validation scope

```yaml
validation_scope:
  price_source: Songdaiki/stock-web
  inspected_shards:
    - atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv
    - atlas/ohlcv_tradable_by_symbol_year/047/047560/2024.csv
    - atlas/ohlcv_tradable_by_symbol_year/053/053800/2024.csv
  inspected_profiles:
    - atlas/symbol_profiles/030/030520.json
    - atlas/symbol_profiles/047/047560.json
    - atlas/symbol_profiles/053/053800.json
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  forward_window_available_by_manifest: true
  corporate_action_window_blocked: false
```

---

## 10. Residual contribution summary

```yaml
residual_contribution_summary:
  new_symbol_count: 3
  new_independent_case_count: 3
  canonical_archetype_rule_candidate: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_BRIDGE_GATE
  useful_for:
    - separating software/security business quality from fresh acceleration trigger
    - blocking AI-software price-only blowoff from Green
    - identifying local 4B when MFE is huge but contract/revenue bridge is absent
    - preserving positive C28 cases when recurring software revenue and operating leverage are visible

  loop_contribution_label: residual_error_found
  do_not_propose_new_weight_delta: true
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent. Do not treat this Markdown as a command to change production scoring immediately.

Goal:
- Add a canonical-archetype-specific shadow validation test for C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.
- Use this MD as a research artifact only.
- Implement no production-score change unless a later batch-calibration instruction explicitly approves it.

Research artifact:
- e2r_stock_web_v12_residual_round_R8_loop_89_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md

Suggested shadow rule:
- For C28, require recurring revenue / enterprise contract retention / ARR-like cloud seat expansion / managed-security order growth / margin-EPS bridge before Stage3 Green.
- If software/AI/security headline exists but no contract/revenue bridge exists, cap at Watch or Stage2 Yellow.
- If local MFE >= 50% but no non-price bridge exists, add local 4B overlay and block Green.
- If 90D/180D MAE <= -35% after local MFE >= 50%, mark hard-4C candidate for calibration review.

Do not:
- Patch production scoring directly.
- Add live scan logic.
- Use current-stock discovery.
- Treat these rows as investment recommendations.
```
