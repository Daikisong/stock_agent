# E2R Stock-Web v12 Residual Research — R8 / Loop 92

```yaml
scheduled_round: R8
scheduled_loop: 92
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: CYBERSECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_QUANTUM_THEME_SPIKE

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
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 92
next_round: R9
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_92_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 92
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

R8 hard gate requires:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

Recent R8 branch usage already covered:

```text
loop88: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop89: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
loop90: C27_CONTENT_IP_GLOBAL_MONETIZATION
loop91: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

This run returns to C28, but uses a different fine branch:

```text
cybersecurity contract retention / recurring revenue bridge
vs security, AI-security, and quantum-security theme spikes
```

The purpose is to separate:

```text
recurring security software / appliance contract economics
```

from:

```text
cybersecurity label or quantum/security theme beta.
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
rows: 26
symbols: 19
date_range: 2022-03-23~2024-09-04
good/bad S2: 10/4
4B/4C: 0/0
URL pending/proxy: 10/10
top covered symbols:
  058970(3), 150900(3), 042510(2), 203650(2), 307950(2), 012510(1)
```

Selected symbols:

```text
136540 윈스
053800 안랩
356680 엑스게이트
```

They avoid the C28 top-covered names and avoid the most recent R8 loop91 C26 names:

```text
067160, 273060, 236810
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
136540: same archetype, new symbol, network-security contract retention / renewal bridge capped positive
053800: same archetype, new symbol, mature cybersecurity label / political-security beta false-positive branch
356680: same archetype, new symbol, quantum/security theme spike without recurring contract bridge hard-4C branch
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
136540 윈스
  profile: atlas/symbol_profiles/136/136540.json
  first_date: 2011-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,640
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

053800 안랩
  profile: atlas/symbol_profiles/053/053800.json
  first_date: 2001-09-13
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,027
  corporate_action_candidate_dates:
    2005-03-31
  2024 entry~D+180 contamination: none

356680 엑스게이트
  profile: atlas/symbol_profiles/356/356680.json
  first_date: 2023-03-16
  last_date: 2026-02-20
  tradable_ohlcv rows: 714
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C28 is about software/security contract retention, not a generic cybersecurity label.

The model can over-score:

```text
cybersecurity headline
AI security theme
quantum encryption / VPN / appliance label
public-sector security budget hope
one-day breach or security policy sympathy
```

The actual C28 bridge is narrower:

```text
security product capability
  -> installed base
  -> renewal / maintenance / subscription retention
  -> enterprise or public-sector contract conversion
  -> gross margin / OP conversion
  -> price survival after the first security-theme spike
```

A cybersecurity stock is like a building alarm system. The headline says the world feels unsafe, but equity value comes from customers renewing contracts, paying maintenance, and expanding seats. Fear can open the door; recurring invoices keep the lights on.

---

## 5. Case 1 — 136540 윈스

```yaml
case_id: C28_R8L92_136540_2024_05_03
symbol: "136540"
name_at_trigger: "윈스"
current_or_latest_name_in_profile: "윈스테크넷"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: CYBERSECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_QUANTUM_THEME_SPIKE
trigger_date: 2024-05-03
entry_date: 2024-05-03
entry_price_basis: close
entry_price: 12850
classification: positive_capped_network_security_contract_retention_bridge
calibration_usable: true
```

### Evidence interpretation

윈스 is the capped positive in this set.

The useful C28 read is not merely "security stock." It is more specific:

```text
network security / intrusion prevention relevance
  -> enterprise or public-sector installed base
  -> renewal / maintenance revenue
  -> contract retention
  -> controlled downside and later price confirmation
```

The price path did not create an instant blowoff, but it survived and later advanced into November. This is the shape of a C28 capped positive.

### Price path

Key Stock-Web rows:

```text
2024-05-03: close 12,850
2024-05-07: high 13,090 / close 12,980
2024-07-24: high 14,450 / close 14,370
2024-08-05: low 12,000 / close 12,400
2024-11-04: high 13,300 / close 13,190
2024-11-05: high 15,750 / close 15,120
```

Approximate path from entry close:

```text
entry_close: 12,850
peak_high: 15,750
MFE: +22.6%
worst_low: 12,000
MAE: -6.6%
```

### Interpretation

This is a C28 positive, but still capped:

```text
Stage2-Actionable: allowed if contract-retention / renewal bridge is explicit.
Stage3-Green: requires recurring revenue, customer retention, and margin evidence.
Local 4B: not mandatory immediately, but monitor after a sharp late theme move.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  security_product_relevance: high
  contract_retention_bridge: medium_high
  recurring_revenue_visibility: medium
  price_survival: medium_high
  drawdown_penalty: low_to_medium
  green_cap: yes
```

---

## 6. Case 2 — 053800 안랩

```yaml
case_id: C28_R8L92_053800_2024_04_11
symbol: "053800"
name: "안랩"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: CYBERSECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_QUANTUM_THEME_SPIKE
trigger_date: 2024-04-11
entry_date: 2024-04-11
entry_price_basis: close
entry_price: 64800
classification: counterexample_mature_security_label_without_fresh_retention_margin_bridge
calibration_usable: true
```

### Evidence interpretation

안랩 is the mature-security label counterexample.

The company has real security-business relevance, but the trigger path shows why C28 cannot upgrade from label alone. The price popped briefly, then failed price survival.

The model risk:

```text
mature cybersecurity name
  -> security/political/AI-security beta
  -> one-day volume burst
  -> no new recurring contract or margin bridge
  -> high MAE follows
```

### Price path

Key Stock-Web rows:

```text
2024-04-11: close 64,800
2024-04-12: high 75,600 / close 69,200
2024-04-17: low 64,100 / close 64,100
2024-08-05: low 51,600 / close 51,600
2024-09-20: low 51,000 / close 51,000
2024-11-04: high 61,300 / close 61,200
```

Approximate path from entry close:

```text
entry_close: 64,800
peak_high: 75,600
MFE: +16.7%
worst_low: 51,000
MAE: -21.3%
```

### Interpretation

This is a false-positive / Watch cap case:

```text
Stage2-Watch: allowed from mature security relevance.
Stage2-Actionable: blocked unless fresh contract-retention, renewal, or margin bridge is explicit.
Stage3-Green: blocked.
Hard 4C: not quite, but high-MAE false-positive guard applies.
```

The lesson is that a security brand is not a contract-retention thesis by itself.

### Stress-test components

```text
raw_component_score_proxy:
  cybersecurity_label_quality: high
  fresh_contract_bridge: weak
  renewal_or_subscription_bridge: weak
  price_confirmation: local_only
  price_survival: failed
  drawdown_penalty: medium_high
```

---

## 7. Case 3 — 356680 엑스게이트

```yaml
case_id: C28_R8L92_356680_2024_03_26
symbol: "356680"
name: "엑스게이트"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: CYBERSECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_QUANTUM_THEME_SPIKE
trigger_date: 2024-03-26
entry_date: 2024-03-26
entry_price_basis: close
entry_price: 6780
classification: hard_4c_candidate_quantum_security_theme_spike_without_contract_retention_bridge
calibration_usable: true
```

### Evidence interpretation

엑스게이트 is the hard guardrail case.

It had the clearest theme-spike behavior:

```text
security appliance / VPN / quantum-security label
  -> explosive trading volume
  -> short-lived spike
  -> no demonstrated recurring contract-retention bridge
  -> severe forward drawdown
```

C28 should not treat that first spike as Green. The contract-retention bridge was missing.

### Price path

Key Stock-Web rows:

```text
2024-03-26: close 6,780
2024-03-28: high 7,140 / close 6,230
2024-04-19: low 5,350 / close 5,460
2024-05-24: low 4,960 / close 5,030
2024-08-05: low 3,100 / close 3,270
2024-08-26: high 5,060 / close 4,650
2024-10-28: high 5,890 / close 5,500
```

Approximate path from entry close:

```text
entry_close: 6,780
peak_high: 7,140
MFE: +5.3%
worst_low: 3,100
MAE: -54.3%
```

### Interpretation

This is a hard C28 false-positive:

```text
Stage2-Watch: possible from security/quantum label.
Stage2-Actionable: blocked without contract-retention evidence.
Stage3-Green: blocked.
Hard 4C: yes.
```

The later spikes in August and October prove the stock can trade as a theme, but the March entry was not a durable C28 thesis.

### Stress-test components

```text
raw_component_score_proxy:
  security_theme_label: high
  quantum_security_label: high
  recurring_contract_bridge: weak
  retention_margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C28 grid:

```text
136540 윈스:
  security contract-retention capped positive;
  controlled MAE and later MFE.

053800 안랩:
  mature cybersecurity label produced a local spike,
  but lacked a fresh renewal/margin bridge and failed price survival.

356680 엑스게이트:
  quantum/security theme spike failed badly;
  shallow MFE and extreme MAE, hard 4C.
```

Shared rule:

```text
C28 is not "security stock went up."
C28 is "security software/appliance customers renew, expand, and produce recurring revenue with margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C28_R8L92_136540_2024_05_03","scheduled_round":"R8","scheduled_loop":92,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_QUANTUM_THEME_SPIKE","symbol":"136540","name_at_trigger":"윈스","current_or_latest_name_in_profile":"윈스테크넷","trigger_date":"2024-05-03","entry_date":"2024-05-03","entry_price":12850,"peak_high":15750,"peak_date":"2024-11-05","worst_low":12000,"worst_low_date":"2024-08-05","mfe_pct":22.6,"mae_pct":-6.6,"classification":"positive_capped_network_security_contract_retention_bridge","calibration_usable":true,"evidence_family":"network_security_installed_base_renewal_maintenance_contract_retention_bridge","residual_error":"positive_path_still_needs_recurring_revenue_and_margin_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_contract_retention_and_recurring_revenue_bridge_confirm_but_cap_green_without_margin_evidence"}
{"row_type":"case","case_id":"C28_R8L92_053800_2024_04_11","scheduled_round":"R8","scheduled_loop":92,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_QUANTUM_THEME_SPIKE","symbol":"053800","name":"안랩","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":64800,"peak_high":75600,"peak_date":"2024-04-12","worst_low":51000,"worst_low_date":"2024-09-20","mfe_pct":16.7,"mae_pct":-21.3,"classification":"counterexample_mature_security_label_without_fresh_retention_margin_bridge","calibration_usable":true,"evidence_family":"mature_cybersecurity_label_without_new_contract_retention_or_margin_bridge","residual_error":"security_brand_label_can_overpromote_without_fresh_renewal_revenue_evidence","shadow_rule_candidate":"cap_mature_security_label_spikes_at_watch_yellow_if_price_survival_fails"}
{"row_type":"case","case_id":"C28_R8L92_356680_2024_03_26","scheduled_round":"R8","scheduled_loop":92,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_QUANTUM_THEME_SPIKE","symbol":"356680","name":"엑스게이트","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":6780,"peak_high":7140,"peak_date":"2024-03-28","worst_low":3100,"worst_low_date":"2024-08-05","mfe_pct":5.3,"mae_pct":-54.3,"classification":"hard_4c_candidate_quantum_security_theme_spike_without_contract_retention_bridge","calibration_usable":true,"evidence_family":"quantum_security_vpn_appliance_theme_spike_without_recurring_contract_bridge","residual_error":"security_theme_volume_burst_can_create_catastrophic_false_positive_without_contract_retention","shadow_rule_candidate":"route_security_theme_spike_to_hard_4c_if_mfe_shallow_mae_extreme_and_contract_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":92,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_VS_SECURITY_AI_QUANTUM_THEME_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":92,"canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","rule_id":"C28_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C28, do not open Stage2-Actionable or Stage3-Green from cybersecurity, AI-security, quantum-security, VPN/appliance, public-sector security, or one-day breach/theme spike labels alone. Require installed base, renewal or maintenance retention, subscription or recurring revenue visibility, enterprise/public-sector contract conversion, margin/OP bridge, and post-trigger price survival. Mature security names with local spikes should cap at Watch/Yellow without fresh contract evidence. Quantum/security theme spikes with shallow MFE and large MAE should route to hard-4C.","expected_effect":"Preserve security-software positives with renewal and recurring-revenue evidence while reducing security-label and quantum-theme false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":92,"canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_type":"software_security_contract_retention_guard","contribution":"Adds one network-security contract-retention capped positive, one mature-security label false positive, and one quantum-security hard-4C case to calibrate C28 recurring revenue and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C28_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_REQUIRED

IF canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:

  Do not open Stage3-Green from:
    - cybersecurity label alone
    - AI-security / quantum-security label alone
    - VPN / appliance label alone
    - public-sector security budget hope alone
    - one-day security theme volume spike alone

  Require at least two of:
    - installed base
    - renewal / maintenance retention
    - subscription or recurring revenue visibility
    - enterprise or public-sector contract conversion
    - seat / device / traffic expansion
    - margin or OP conversion
    - low-MAE post-trigger price survival

  If MFE < 10% and MAE < -40%:
    route to C28 hard-4C candidate.

  If MFE > 15% but MAE later exceeds -20% and no contract bridge appears:
    cap at Watch/Yellow or local 4B, not Green.

  If MFE > 20% and MAE remains controlled:
    allow Actionable only if renewal and recurring-revenue bridge is explicit.

  Distinguish:
    - network-security names with installed-base retention economics
    - from mature security brands or quantum/security theme spikes without fresh recurring-contract evidence.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_92_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C28 software/security contract-retention cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C28_CONTRACT_RETENTION_RECURRING_REVENUE_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C28 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C28 cases agree, consider implementing a canonical guard that:
   - blocks security-label Green without installed-base, renewal, recurring-revenue, and margin bridge,
   - preserves network-security positives only with price survival and recurring revenue evidence,
   - caps mature security-label spikes at Watch/Yellow,
   - routes shallow-MFE/high-MAE quantum-security spikes to hard-4C.

Expected next schedule:
completed_round = R8
completed_loop = 92
next_round = R9
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R8
completed_loop = 92
next_round = R9
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
