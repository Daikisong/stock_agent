# E2R Stock-Web v12 Residual Research — R8 / Loop 99

```yaml
scheduled_round: R8
scheduled_loop: 99
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_OFFICE_AUTHENTICATION_PKI_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
ai_office_saas_case_count: 1
authentication_security_case_count: 1
pki_certificate_security_case_count: 1
software_contract_retention_bridge_missing_count: 2
renewal_arr_margin_bridge_missing_count: 2
label_spike_without_contract_quality_count: 2
old_corporate_action_or_name_history_caveat_count: 3
row_presence_or_listing_history_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 99
next_round: R9
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_99_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 99
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

R8 is the platform / content / software / security round. The selected canonical archetype is:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

Recent R8 branch usage:

```text
loop95: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop96: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
loop97: C27_CONTENT_IP_GLOBAL_MONETIZATION
loop98: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

This run returns to C28 after the R8 branch cycle.

Selected fine branch:

```text
AI office / SaaS / authentication / PKI / security software
contract retention, renewal, customer seat expansion, ARR or recurring revenue,
enterprise vs consumer channel, cloud / labor cost, sales and R&D spend,
gross margin, OP conversion, and price survival
vs generic software / security / AI label spike
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
041020 폴라리스오피스
158430 아톤
053300 한국정보인증
```

They avoid the C28 top-covered list and recent R8 names:

```text
C28 top-covered avoid:
  058970, 150900, 042510, 203650, 307950, 012510

recent R8 avoid:
  loop98 C26: 230360, 123570, 089600
  loop97 C27: 035760, 036420, 419530
  loop96 C28: 136540, 060850, 053800
  loop95 C26: 060250, 064260, 216050
  loop94 C27: 251270, 035900, 253450
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
041020: same archetype, new symbol, AI office / SaaS software local positive with 4B / Green cap after large MFE and high MAE.
158430: same archetype, new symbol, authentication / fintech security label hard-4C candidate after shallow MFE and hard-zone MAE.
053300: same archetype, new symbol, PKI / certificate security Watch cap after shallow MFE and material MAE without contract-retention proof.
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
041020 폴라리스오피스
  profile: atlas/symbol_profiles/041/041020.json
  name history:
    인프라웨어 -> 폴라리스오피스
  first_date: 2005-10-28
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,010
  non_tradable_zero_volume rows: 1
  corporate_action_candidate_dates:
    2010-03-12, 2010-03-25, 2010-04-02, 2017-05-15
  2024 entry~D+180 contamination: none
  caveat:
    historical name/raw-discontinuity candidates are outside selected 2024 validation window.

158430 아톤
  profile: atlas/symbol_profiles/158/158430.json
  first_date: 2019-10-17
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,550
  non_tradable_zero_volume rows: 8
  corporate_action_candidate_dates:
    2023-09-06
  2024 entry~D+180 contamination: none
  caveat:
    short listing / row-presence and old corporate-action caveat outside selected 2024 validation window.

053300 한국정보인증
  profile: atlas/symbol_profiles/053/053300.json
  first_date: 2014-02-04
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 2,957
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2021-10-05
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidate is outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C28 is about software / security contract retention. It is not merely a generic "AI software" or "cybersecurity label is hot" archetype.

The model can over-score:

```text
AI office / SaaS label
authentication / fintech security label
PKI / certificate / identity security label
cloud or enterprise software label
public-sector security policy readthrough
one-week software-security volume spike
late chase after a software or AI rerating
```

The C28 bridge must be stricter:

```text
software / security contract-retention event
  -> named product, module, customer vertical, or channel
  -> enterprise contract, seat expansion, renewal, retention, or churn evidence
  -> ARR / recurring revenue / license-to-subscription mix
  -> cloud hosting, support, R&D, sales, and labor cost check
  -> gross margin and operating leverage
  -> public-sector / financial / enterprise procurement timing
  -> cybersecurity incident, compliance, or regulation-to-order path where relevant
  -> cash collection and working capital
  -> valuation discipline after the first AI / software label spike
  -> price survival after the rerating
```

A C28 software thesis is like a subscription login. The label gets the user to the door, but equity value appears only when the customer renews, seats expand, churn stays low, cloud and support cost do not leak the gross margin, and recurring revenue falls through to OP.

---

## 5. Case 1 — 041020 폴라리스오피스

```yaml
case_id: C28_R8L99_041020_2024_02_01
symbol: "041020"
name: "폴라리스오피스"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_OFFICE_AUTHENTICATION_PKI_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 6530
classification: local_positive_ai_office_saas_label_large_mfe_with_4b_green_cap_after_contract_retention_evidence_decay
calibration_usable: true
```

### Evidence interpretation

폴라리스오피스 is the constructive but capped C28 AI office / SaaS case.

The useful C28 read is not simply:

```text
AI 오피스 / 소프트웨어주가 강하다
```

It is:

```text
office software / AI productivity label
  -> potential paid conversion and subscription or license expansion
  -> enterprise / consumer user monetization optionality
  -> March-May price confirmation
  -> later 4B / Green cap because contract retention, renewal, paid conversion, and margin evidence must refresh
```

The price path produced large MFE, so this is not a failed label. However, the later drawdown into August and October means C28 should not leave the name as ordinary Green. The bridge from AI office label to durable contracts, retention, paid seats, cloud cost, and OP must be explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 6,700 / low 6,310 / close 6,530
2024-02-29: high 8,230 / close 7,940
2024-03-06: high 8,960 / close 7,970
2024-05-09: high 10,130
2024-08-05: low 4,500 / close 4,790
2024-09-09: high 6,130 / close 5,560
2024-10-25: high 5,900 / close 4,980
```

Approximate path from entry close:

```text
entry_close: 6,530
peak_high: 10,130
MFE: +55.1%
worst_low_after_entry: 4,500
MAE: -31.1%
```

### Interpretation

This is a C28 local positive / 4B case:

```text
Stage2-Actionable: possible if contract retention, paid conversion, customer seats, and margin bridge are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C: no, because large MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  ai_office_saas_relevance: high
  paid_conversion_bridge: weak_to_medium
  enterprise_contract_bridge: weak_to_medium
  retention_churn_bridge: weak
  cloud_support_cost_bridge: weak_to_medium
  margin_op_bridge: weak_to_medium
  price_confirmation: high_initial
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 6. Case 2 — 158430 아톤

```yaml
case_id: C28_R8L99_158430_2024_02_01
symbol: "158430"
name: "아톤"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_OFFICE_AUTHENTICATION_PKI_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 4355
classification: hard_4c_candidate_authentication_fintech_security_label_without_contract_retention_margin_survival
calibration_usable: true
```

### Evidence interpretation

아톤 is the authentication / fintech security hard C28 guardrail.

The label can fool the model:

```text
authentication / mobile security / fintech security
  -> financial-sector security contract readthrough
  -> identity / certificate / compliance label
  -> one-day security-stock event beta
```

But from the selected February trigger, the forward path produced shallow MFE and then moved into a hard drawdown zone. The bridge from security label to enterprise renewal, financial-customer retention, recurring security revenue, and margin survival was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 4,355 / low 4,150 / close 4,355
2024-03-13: high 4,535 / close 4,475
2024-07-30: high 4,260 / close 3,715
2024-08-05: low 2,885 / close 3,100
2024-09-03: high 4,255 / close 4,115
2024-11-05: high 4,695 / close 4,290
```

Approximate path from entry close:

```text
entry_close: 4,355
peak_high_after_entry: 4,695
MFE: +7.8%
worst_low_after_entry: 2,885
MAE: -33.8%
```

### Interpretation

This is a hard C28 false-positive candidate:

```text
Stage2-Watch: possible from authentication and fintech security relevance.
Stage2-Actionable: blocked unless contract renewal, customer retention, security service ARR, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and hard-zone MAE.
Later event caveat: November spike should be treated as renewed event evidence, not automatic validation of the February trigger.
```

The lesson is that security relevance is not contract-retention margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  authentication_security_label: high
  financial_customer_bridge: weak_to_medium
  contract_retention_bridge: weak
  recurring_revenue_bridge: weak
  cloud_support_cost_bridge: weak
  margin_op_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 053300 한국정보인증

```yaml
case_id: C28_R8L99_053300_2024_02_01
symbol: "053300"
name: "한국정보인증"
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: AI_OFFICE_AUTHENTICATION_PKI_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5020
classification: watch_cap_pki_certificate_security_label_without_incremental_contract_retention_or_margin_bridge
calibration_usable: true
```

### Evidence interpretation

한국정보인증 is the PKI / certificate security Watch cap.

The setup had plausible C28 relevance:

```text
PKI / certificate / identity security
  -> digital identity and compliance readthrough
  -> enterprise / financial / public-sector authentication demand
```

But the February trigger did not validate Actionable or Green. MFE was shallow, the stock drifted into material MAE by August, and the September security-label spike did not hold enough to prove durable contract retention or margin conversion.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,190 / low 4,990 / close 5,020
2024-02-16: high 5,430 / close 5,400
2024-04-09: low 4,860 / close 4,860
2024-08-05: low 3,600 / close 3,705
2024-09-03: high 4,665 / close 4,585
2024-10-25: low 3,765 / close 3,795
```

Approximate path from entry close:

```text
entry_close: 5,020
peak_high: 5,430
MFE: +8.2%
worst_low_after_entry: 3,600
MAE: -28.3%
```

### Interpretation

This is a C28 Watch / Yellow cap:

```text
Stage2-Watch: valid from PKI / identity security relevance.
Stage2-Actionable: blocked unless contract renewal, customer retention, compliance-driven order, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no, because MAE did not cross the hard threshold.
Local 4B: monitor if September security spike is treated as a new event window.
```

The lesson is that a certificate/security label is not incremental contract-retention proof.

### Stress-test components

```text
raw_component_score_proxy:
  pki_certificate_security_relevance: high
  enterprise_customer_bridge: weak_to_medium
  public_financial_channel_bridge: weak_to_medium
  retention_renewal_bridge: weak
  recurring_revenue_bridge: weak_to_medium
  margin_op_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: material
  actionability_cap: Watch/Yellow
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
ai_office_saas_case_count: 1
authentication_security_case_count: 1
pki_certificate_security_case_count: 1
software_contract_retention_bridge_missing_count: 2
renewal_arr_margin_bridge_missing_count: 2
label_spike_without_contract_quality_count: 2
old_corporate_action_or_name_history_caveat_count: 3
row_presence_or_listing_history_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C28 software/security grid:

```text
041020 폴라리스오피스:
  AI office / SaaS software label positive;
  large MFE first, then high MAE, local 4B / Green cap.

158430 아톤:
  authentication / fintech security label failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.

053300 한국정보인증:
  PKI / certificate security relevance;
  shallow MFE and material MAE, Watch/Yellow cap.
```

Shared rule:

```text
C28 is not "software/security/AI label is hot."
C28 is "contract retention, customer renewal, seat expansion, ARR or recurring revenue, cloud/support cost, and OP margin are visible."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C28_R8L99_041020_2024_02_01","scheduled_round":"R8","scheduled_loop":99,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_AUTHENTICATION_PKI_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE","symbol":"041020","name":"폴라리스오피스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":6530,"peak_high":10130,"peak_date":"2024-05-09","worst_low_after_entry":4500,"worst_low_after_entry_date":"2024-08-05","mfe_pct":55.1,"mae_pct":-31.1,"classification":"local_positive_ai_office_saas_label_large_mfe_with_4b_green_cap_after_contract_retention_evidence_decay","calibration_usable":true,"old_corporate_action_or_name_history_caveat":true,"evidence_family":"ai_office_saas_paid_conversion_enterprise_contract_retention_cloud_support_margin_bridge","residual_error":"ai_office_software_label_can_create_large_mfe_but_requires_4b_when_contract_retention_and_margin_evidence_decays","shadow_rule_candidate":"classify_large_mfe_then_high_mae_ai_office_saas_cases_as_local_4b_not_green_without_retention_margin_refresh"}
{"row_type":"case","case_id":"C28_R8L99_158430_2024_02_01","scheduled_round":"R8","scheduled_loop":99,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_AUTHENTICATION_PKI_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE","symbol":"158430","name":"아톤","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":4355,"peak_high":4695,"peak_date":"2024-11-05","worst_low_after_entry":2885,"worst_low_after_entry_date":"2024-08-05","mfe_pct":7.8,"mae_pct":-33.8,"classification":"hard_4c_candidate_authentication_fintech_security_label_without_contract_retention_margin_survival","calibration_usable":true,"short_listing_or_row_presence_caveat":true,"old_corporate_action_caveat_outside_window":true,"event_window_separation_required":true,"evidence_family":"authentication_fintech_security_label_without_financial_customer_contract_retention_recurring_revenue_margin_bridge","residual_error":"authentication_security_label_can_fail_when_contract_retention_and_margin_bridge_missing","shadow_rule_candidate":"route_authentication_security_label_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_retention_margin_bridge_missing"}
{"row_type":"case","case_id":"C28_R8L99_053300_2024_02_01","scheduled_round":"R8","scheduled_loop":99,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_AUTHENTICATION_PKI_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE","symbol":"053300","name":"한국정보인증","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5020,"peak_high":5430,"peak_date":"2024-02-16","worst_low_after_entry":3600,"worst_low_after_entry_date":"2024-08-05","mfe_pct":8.2,"mae_pct":-28.3,"classification":"watch_cap_pki_certificate_security_label_without_incremental_contract_retention_or_margin_bridge","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"pki_certificate_identity_security_label_without_contract_renewal_customer_retention_compliance_order_margin_bridge","residual_error":"pki_security_relevance_can_overpromote_without_incremental_contract_retention_or_margin_evidence","shadow_rule_candidate":"cap_pki_certificate_security_label_at_watch_yellow_if_mfe_shallow_and_retention_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":99,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_AUTHENTICATION_PKI_SECURITY_SAAS_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_VS_SOFTWARE_SECURITY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"ai_office_saas_case_count":1,"authentication_security_case_count":1,"pki_certificate_security_case_count":1,"software_contract_retention_bridge_missing_count":2,"renewal_arr_margin_bridge_missing_count":2,"label_spike_without_contract_quality_count":2,"old_corporate_action_or_name_history_caveat_count":3,"row_presence_or_listing_history_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":99,"canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","rule_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C28 software/security contract-retention cases, do not open Stage2-Actionable or Stage3-Green from AI office/SaaS, authentication, fintech security, PKI/certificate/identity security, cloud/enterprise software, public-sector security policy readthrough, one-week software-security volume spike, or late chase after software/AI rerating labels alone. Require named product/module/customer vertical/channel, enterprise contract, seat expansion, renewal, retention, churn evidence, ARR/recurring revenue or license-to-subscription mix, cloud hosting/support/R&D/sales/labor cost check, gross margin and operating leverage, public-sector/financial/enterprise procurement timing, cybersecurity incident or compliance regulation-to-order path where relevant, cash collection and working capital, valuation discipline after the first AI/software label spike, and post-trigger price survival. AI office/SaaS names with large MFE followed by high MAE should remain local 4B unless contract retention, paid conversion, and margin evidence refresh. Authentication/fintech security labels with shallow MFE and hard-zone MAE should route to hard-4C when contract retention and recurring revenue bridge are missing. PKI/certificate security labels with shallow MFE and material MAE should cap at Watch/Yellow without incremental retention evidence.","expected_effect":"Preserve true software/security contract-retention positives while reducing generic AI-office, authentication, PKI, certificate, security-policy, and SaaS-label false positives where renewal, retention, ARR, cost, and OP evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":99,"canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_type":"software_security_contract_retention_renewal_margin_guard","contribution":"Adds one AI office/SaaS local-positive 4B case, one authentication security hard-4C counterexample, and one PKI certificate Watch cap to calibrate C28 contract retention, renewal, recurring revenue, cloud/support cost, operating leverage, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:

  Do not open Stage3-Green from:
    - AI office / SaaS label alone
    - authentication / fintech security label alone
    - PKI / certificate / identity security label alone
    - cloud or enterprise software label alone
    - public-sector security policy readthrough alone
    - one-week software-security volume spike alone
    - late chase after software / AI rerating alone

  Require at least two of:
    - named product / module / customer vertical / channel
    - enterprise contract / seat expansion / renewal / retention / churn evidence
    - ARR / recurring revenue / license-to-subscription mix
    - cloud hosting / support / R&D / sales / labor cost check
    - gross margin and operating leverage
    - public-sector / financial / enterprise procurement timing
    - cybersecurity incident, compliance, or regulation-to-order path where relevant
    - cash collection and working-capital timing
    - low-MAE post-trigger price survival
    - fresh evidence after the software/security headline

  If MFE < 10% and MAE <= -30%:
    route to C28 hard-4C candidate.

  If MFE is large but retention / ARR / margin evidence is stale:
    preserve as local 4B or capped positive, not Green.

  If MFE is shallow and bridge is security-label only:
    cap at Watch/Yellow.

  If later renewed security/AI event appears after first-window failure:
    create a new event window; do not retroactively validate the failed first trigger.

  Distinguish:
    - software/security names where users renew, seats expand, recurring revenue grows, and OP margin appears
    - from labels where product salience rerates first and retention/margin proof fails.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C28 software/security contract-retention cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_RENEWAL_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C28 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C28 cases agree, consider implementing a canonical guard that:
   - blocks software/security Green without named product/customer, contract, retention, renewal, ARR, churn, and margin bridge,
   - treats large-MFE/high-MAE AI office/SaaS cases as local 4B unless retention evidence refreshes,
   - routes shallow-MFE/hard-MAE authentication security labels to hard-4C,
   - caps PKI/certificate security labels at Watch/Yellow without incremental contract retention evidence,
   - separates renewed event windows from earlier failed security/software triggers,
   - applies name-history, short-listing, row-presence, and old corporate-action caveats.

Expected next schedule:
completed_round = R8
completed_loop = 99
next_round = R9
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R8
completed_loop = 99
next_round = R9
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
