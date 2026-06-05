# E2R Stock-Web v12 Residual Research — R8 / Loop 96

```yaml
scheduled_round: R8
scheduled_loop: 96
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SECURITY_ERP_SOFTWARE_MAINTENANCE_RECURRING_REVENUE_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE

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
security_software_case_count: 2
erp_software_case_count: 1
name_history_caveat_count: 1
row_presence_or_tradeability_caveat_count: 1
contract_retention_bridge_missing_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 96
next_round: R9
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_96_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 96
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

R8 hard gate requires:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

Recent R8 branch usage:

```text
loop91: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop92: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
loop93: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop94: C27_CONTENT_IP_GLOBAL_MONETIZATION
loop95: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

This run returns to C28 after the R8 branch cycle, but avoids the C28 top-covered names and uses a different fine branch:

```text
security / ERP / enterprise software
maintenance, renewal, subscription, recurring revenue, retention, and margin bridge
vs generic software/security label spike
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
136540 윈스 / 윈스테크넷
060850 영림원소프트랩
053800 안랩
```

They avoid the C28 top-covered list and avoid recent R8 loop95 C26 names:

```text
loop95 avoid: 060250, 064260, 216050
loop94 avoid: 251270, 035900, 253450
loop93 avoid: 230360, 214320, 089600
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
136540: same archetype, new symbol, network-security software retention positive with name-history caveat and Green cap
060850: same archetype, new symbol, ERP software maintenance/subscription local positive followed by material MAE 4B cap
053800: same archetype, new symbol, endpoint/security software label hard-4C candidate without incremental contract-retention margin survival
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
136540 윈스 / 윈스테크넷
  profile: atlas/symbol_profiles/136/136540.json
  current_or_latest_name in profile: 윈스테크넷
  name history includes:
    윈스, 2014-04-11 to 2025-04-15
    윈스테크넷, 2011-05-02 to 2026-02-20
  selected 2024 trigger name:
    윈스
  first_date: 2011-05-02
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,640
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    overlapping name-history metadata; use 2024 market-recognized name 윈스 for trigger narrative.

060850 영림원소프트랩
  profile: atlas/symbol_profiles/060/060850.json
  first_date: 2020-08-12
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,353
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

053800 안랩
  profile: atlas/symbol_profiles/053/053800.json
  name history:
    안철수연구소 until 2012-04-20
    안랩 from 2012-04-23
  first_date: 2001-09-13
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,027
  non_tradable_zero_volume rows: 1
  corporate_action_candidate_dates:
    2005-03-31
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity caveat exists outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C28 is about software/security contract retention. It is not a generic "software stock" or "cybersecurity label" archetype.

The model can over-score:

```text
cybersecurity / endpoint security label
network security appliance label
ERP or enterprise software label
public-sector digitalization headline
AI / cloud / SaaS readthrough
low-float software volume spike
one-week software-security stock rebound
```

The C28 bridge must be stricter:

```text
software / security contract event
  -> named customer segment or contract base
  -> renewal / maintenance / subscription retention
  -> ARR or recurring service revenue
  -> upsell / license expansion / seat growth
  -> gross-margin and cloud/service cost structure
  -> sales/marketing and R&D leverage
  -> customer concentration / public-sector budget risk
  -> margin / OP conversion
  -> price survival after the first software-label spike
```

A C28 software thesis is like a building access card system. The label says customers need security, but C28 asks whether customers renew the license, expand seats, pay maintenance, keep churn low, and leave margin after cloud, support, R&D, and sales cost.

---

## 5. Case 1 — 136540 윈스 / 윈스테크넷

```yaml
case_id: C28_R8L96_136540_2024_02_01
symbol: "136540"
name_at_trigger: "윈스"
current_or_latest_profile_name: "윈스테크넷"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SECURITY_ERP_SOFTWARE_MAINTENANCE_RECURRING_REVENUE_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 12990
classification: positive_capped_network_security_contract_retention_margin_bridge_with_name_history_caveat
calibration_usable: true
```

### Evidence interpretation

윈스 is the constructive C28 control in this set.

The useful C28 read is not simply:

```text
보안주가 움직였다
```

It is:

```text
network-security / intrusion-prevention software and appliance base
  -> enterprise and public-sector renewal demand
  -> maintenance and service retention
  -> contract-margin optionality
  -> price survival with controlled drawdown
```

The forward path produced a meaningful MFE while MAE stayed controlled. This supports a capped positive. However, Green still requires renewal, maintenance, public-sector order, service-margin, and operating-leverage evidence, not just the security label.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 13,090 / close 12,990
2024-03-15: high 13,250 / close 13,160
2024-07-29: high 14,620 / close 14,400
2024-08-05: low 12,000 / close 12,400
2024-11-05: high 15,750 / close 15,120
```

Approximate path from entry close:

```text
entry_close: 12,990
peak_high: 15,750
MFE: +21.2%
worst_low_after_entry: 12,000
MAE: -7.6%
```

### Interpretation

This is a C28 capped positive:

```text
Stage2-Actionable: possible if renewal/maintenance/subscription and contract-margin bridge are explicit.
Stage3-Green: blocked without fresh customer retention and operating-leverage evidence.
Local 4B: monitor after +20% MFE if order/renewal evidence becomes stale.
Hard 4C: no.
Name-history caveat: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  network_security_relevance: high
  contract_retention_bridge: medium_high
  maintenance_service_revenue_bridge: medium
  margin_op_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 060850 영림원소프트랩

```yaml
case_id: C28_R8L96_060850_2024_02_01
symbol: "060850"
name: "영림원소프트랩"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SECURITY_ERP_SOFTWARE_MAINTENANCE_RECURRING_REVENUE_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 9250
classification: local_positive_erp_software_maintenance_subscription_with_4b_after_material_mae
calibration_usable: true
```

### Evidence interpretation

영림원소프트랩 is the ERP software local-positive / 4B cap.

The setup had real C28 relevance:

```text
ERP / enterprise software
  -> maintenance and recurring service revenue
  -> digitalization and SMB/enterprise software demand
  -> early local price confirmation
```

The forward path produced a meaningful local MFE, especially around the April spike. But the later path lost price survival. This is not a pure hard-4C because a tradable MFE came first. It is a local positive that needs 4B unless fresh renewal, subscription, and margin evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 9,290 / close 9,250
2024-02-28: high 9,400 / close 9,370
2024-04-05: high 11,270 / close 9,110
2024-08-05: low 7,310 / close 7,610
2024-09-09: low 7,160 / close 7,230
2024-10-25: low 6,730 / close 6,730
```

Approximate path from entry close:

```text
entry_close: 9,250
peak_high: 11,270
MFE: +21.8%
worst_low_after_entry: 6,670
MAE: -27.9%
```

### Interpretation

This is a C28 local positive with 4B:

```text
Stage2-Watch: valid from ERP / enterprise-software relevance.
Stage2-Actionable: possible only if maintenance renewal, subscription mix, and margin bridge are explicit.
Stage3-Green: blocked after material MAE unless fresh contract retention evidence appears.
Local 4B: required.
Hard 4C: not primary because meaningful MFE came first and MAE did not cross the hard threshold.
```

### Stress-test components

```text
raw_component_score_proxy:
  erp_software_relevance: high
  maintenance_retention_bridge: medium
  subscription_revenue_bridge: weak_to_medium
  service_margin_bridge: weak_to_medium
  price_confirmation: medium_high_initial
  post_burst_survival: weak
  local_4b_overlay: required
```

---

## 7. Case 3 — 053800 안랩

```yaml
case_id: C28_R8L96_053800_2024_02_01
symbol: "053800"
name: "안랩"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SECURITY_ERP_SOFTWARE_MAINTENANCE_RECURRING_REVENUE_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 73000
classification: hard_4c_candidate_endpoint_security_label_without_incremental_contract_retention_margin_survival
calibration_usable: true
```

### Evidence interpretation

안랩 is the security-software hard C28 guardrail.

The label is high quality:

```text
endpoint security / cybersecurity software
  -> enterprise/public security demand
  -> maintenance and subscription optionality
  -> security-policy or cyber-risk salience
```

But from the selected 2024 entry, the path did not validate incremental contract retention or margin survival. MFE was shallow, while the stock later entered a hard drawdown zone. The model should not promote a mature security label into Actionable/Green without renewal growth, ARR/service revenue, customer expansion, and operating-margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 74,000 / close 73,000
2024-02-21: high 74,800 / close 74,000
2024-04-12: high 75,600 / close 69,200
2024-08-05: low 51,600 / close 51,600
2024-09-20: low 51,000 / close 51,000
2024-11-07: high 63,500
```

Approximate path from entry close:

```text
entry_close: 73,000
peak_high: 75,600
MFE: +3.6%
worst_low_after_entry: 51,000
MAE: -30.1%
```

### Interpretation

This is a hard C28 false-positive candidate:

```text
Stage2-Watch: possible from endpoint security and software relevance.
Stage2-Actionable: blocked unless renewal, maintenance/subscription, ARR/service revenue, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes by shallow MFE and -30% MAE.
Row/tradeability caveat: only minor historical old raw-discontinuity / single zero-volume caveat outside 2024 window.
```

The lesson is that a cybersecurity label is not contract-retention margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  endpoint_security_relevance: very_high
  renewal_retention_bridge: weak_from_price_path
  subscription_service_revenue_bridge: weak_to_medium
  operating_margin_bridge: weak_to_medium
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
security_software_case_count: 2
erp_software_case_count: 1
name_history_caveat_count: 1
row_presence_or_tradeability_caveat_count: 1
contract_retention_bridge_missing_count: 2
calibration_usable_trigger_count: 3
```

The three-case C28 software/security grid:

```text
136540 윈스:
  network security retention positive;
  meaningful MFE and low MAE, but Green requires renewal and margin evidence.

060850 영림원소프트랩:
  ERP maintenance/subscription local positive;
  meaningful MFE first, later material MAE, 4B required.

053800 안랩:
  mature endpoint-security label failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.
```

Shared rule:

```text
C28 is not "security or software label is quality."
C28 is "renewals, maintenance, subscriptions, customer expansion, service margin, and operating leverage are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C28_R8L96_136540_2024_02_01","scheduled_round":"R8","scheduled_loop":96,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_ERP_SOFTWARE_MAINTENANCE_RECURRING_REVENUE_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE","symbol":"136540","name_at_trigger":"윈스","current_or_latest_profile_name":"윈스테크넷","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":12990,"peak_high":15750,"peak_date":"2024-11-05","worst_low_after_entry":12000,"worst_low_after_entry_date":"2024-08-05","mfe_pct":21.2,"mae_pct":-7.6,"classification":"positive_capped_network_security_contract_retention_margin_bridge_with_name_history_caveat","calibration_usable":true,"name_history_caveat":true,"evidence_family":"network_security_contract_retention_maintenance_service_revenue_margin_bridge","residual_error":"positive_security_software_path_requires_green_cap_without_refreshed_renewal_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_renewal_maintenance_and_margin_bridge_confirm_but_cap_green_without_fresh_evidence"}
{"row_type":"case","case_id":"C28_R8L96_060850_2024_02_01","scheduled_round":"R8","scheduled_loop":96,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_ERP_SOFTWARE_MAINTENANCE_RECURRING_REVENUE_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE","symbol":"060850","name":"영림원소프트랩","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":9250,"peak_high":11270,"peak_date":"2024-04-05","worst_low_after_entry":6670,"worst_low_after_entry_date":"2024-11-07","mfe_pct":21.8,"mae_pct":-27.9,"classification":"local_positive_erp_software_maintenance_subscription_with_4b_after_material_mae","calibration_usable":true,"evidence_family":"erp_software_maintenance_subscription_label_without_sustained_retention_margin_survival","residual_error":"erp_maintenance_label_can_create_mfe_but_fail_green_without_subscription_retention_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_material_mae_erp_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C28_R8L96_053800_2024_02_01","scheduled_round":"R8","scheduled_loop":96,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_ERP_SOFTWARE_MAINTENANCE_RECURRING_REVENUE_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE","symbol":"053800","name":"안랩","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":73000,"peak_high":75600,"peak_date":"2024-04-12","worst_low_after_entry":51000,"worst_low_after_entry_date":"2024-09-20","mfe_pct":3.6,"mae_pct":-30.1,"classification":"hard_4c_candidate_endpoint_security_label_without_incremental_contract_retention_margin_survival","calibration_usable":true,"row_presence_or_tradeability_caveat":true,"evidence_family":"endpoint_security_label_without_incremental_renewal_subscription_margin_bridge","residual_error":"mature_security_label_can_fail_when_contract_retention_and_margin_bridge_missing","shadow_rule_candidate":"route_endpoint_security_label_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_renewal_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":96,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_ERP_SOFTWARE_MAINTENANCE_RECURRING_REVENUE_RETENTION_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"security_software_case_count":2,"erp_software_case_count":1,"name_history_caveat_count":1,"row_presence_or_tradeability_caveat_count":1,"contract_retention_bridge_missing_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":96,"canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","rule_id":"C28_RENEWAL_MAINTENANCE_SUBSCRIPTION_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C28, do not open Stage2-Actionable or Stage3-Green from cybersecurity, endpoint security, network security appliance, ERP, enterprise software, public-sector digitalization, AI/cloud/SaaS readthrough, low-float software spike, or one-week software/security rebound labels alone. Require named customer segment or contract base, renewal/maintenance/subscription retention, ARR or recurring service revenue, upsell/license expansion/seat growth, gross-margin and cloud/service cost structure, sales/marketing and R&D leverage, customer concentration or public-sector budget risk check, margin/OP conversion, and post-trigger price survival. Network-security positives with meaningful MFE and controlled MAE may be capped Actionable when renewal and service-margin bridge is explicit, but Green requires fresh evidence. ERP maintenance labels with meaningful MFE followed by material MAE should remain local 4B unless subscription/retention evidence refreshes. Mature endpoint-security labels with shallow MFE and hard-zone MAE should route to hard-4C when incremental contract-retention and margin bridge are missing.","expected_effect":"Preserve true software/security retention positives while reducing generic cybersecurity, ERP, SaaS, and software-label false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":96,"canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_type":"renewal_maintenance_subscription_margin_guard","contribution":"Adds one network-security capped positive, one ERP software local 4B case, and one endpoint-security hard-4C candidate to calibrate C28 renewal, maintenance, subscription, customer expansion, service-margin, and operating-leverage requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C28_RENEWAL_MAINTENANCE_SUBSCRIPTION_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:

  Do not open Stage3-Green from:
    - cybersecurity / endpoint security label alone
    - network-security appliance label alone
    - ERP / enterprise software label alone
    - public-sector digitalization headline alone
    - AI / cloud / SaaS readthrough alone
    - low-float software volume spike alone
    - one-week software/security rebound alone

  Require at least two of:
    - named customer segment or contract base
    - renewal / maintenance / subscription retention
    - ARR or recurring service revenue
    - upsell / license expansion / seat growth
    - gross-margin and cloud/service cost structure
    - sales/marketing and R&D leverage
    - customer concentration or public-sector budget-risk control
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the software/security headline

  If MFE < 8% and MAE <= -30%:
    route to C28 hard-4C candidate.

  If MFE > 15% but later MAE is material:
    preserve as local 4B / event burst, not Green, unless renewal/subscription/margin evidence appears.

  If MFE is meaningful and MAE controlled:
    allow capped Actionable only when retention and margin bridge are explicit.

  Distinguish:
    - software/security names where renewals and service revenue become margin
    - from software labels where demand does not survive churn, budget, R&D, or sales-cost risk.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_96_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C28 software/security contract-retention cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C28_RENEWAL_MAINTENANCE_SUBSCRIPTION_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C28 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C28 cases agree, consider implementing a canonical guard that:
   - blocks software/security Green without customer base, renewal, maintenance, subscription, ARR/service revenue, and margin bridge,
   - preserves network-security positives only with price survival and fresh renewal evidence,
   - treats meaningful-MFE/material-MAE ERP software cases as local 4B,
   - routes shallow-MFE/hard-zone-MAE mature endpoint-security labels to hard-4C,
   - applies name-history and row/tradeability caveats.

Expected next schedule:
completed_round = R8
completed_loop = 96
next_round = R9
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R8
completed_loop = 96
next_round = R9
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
