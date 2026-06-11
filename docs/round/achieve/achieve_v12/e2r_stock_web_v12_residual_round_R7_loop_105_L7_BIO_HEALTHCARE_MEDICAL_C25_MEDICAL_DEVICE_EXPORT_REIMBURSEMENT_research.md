# e2r stock-web v12 residual research — R7 / L7 / C25

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R7
selected_loop = 105
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = DIAGNOSTIC_KIT_EXPORT_AND_AESTHETIC_DEVICE_INSTALLED_BASE_REVENUE_BRIDGE_VS_ONE_TIME_PANDEMIC_DEMAND_FADE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Execution boundary

This run follows the v12 execution boundary: it is not coding work, not repository patching, not live candidate discovery, and not production scoring modification. The only output is this standalone historical calibration / sector-archetype residual research Markdown file.

The only price source used here is `Songdaiki/stock-web` actual 1D OHLCV rows from the committed atlas. The price atlas is raw/unadjusted FinanceData/marcap data, and corporate-action-contaminated windows are blocked by default.

## 2. Coverage and duplicate avoidance

No-Repeat / coverage target selected `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT`, which remains under the 50-row practical calibration target.

Previously used C25 symbols were avoided:
- Classys / Dentium / VUNO
- Huvitz / i-SENS / Ray

New symbol set in this run:
- `096530` 씨젠
- `137310` 에스디바이오센서
- `336570` 원텍

The run deliberately mixes molecular diagnostics, rapid antigen diagnostics, and aesthetic medical equipment. This makes the residual rule more useful: C25 should not treat every medical-device headline as the same signal. A reusable C25 rule needs to distinguish recurring installed-base / reimbursement / export conversion from one-off pandemic kit demand or theme-driven re-rating.

## 3. Price atlas basis

```json
{
  "source_repo": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "max_date": "2026-02-20",
  "corporate_action_policy": "block contaminated windows by default"
}
```

## 4. External evidence spine

### 4.1 씨젠 / Seegene diagnostics evidence

Seegene is a molecular diagnostics / IVD company. The source proxy used here is the 2020 COVID diagnostic kit ramp: MFDS emergency authorization for Seegene’s Allplex 2019-nCoV Assay, subsequent production/distribution scale-up, FDA emergency authorization, and broad international sales of the assay. This is not merely a medical-device label; it is a diagnostic-kit export/revenue conversion case.

External source:
- Seegene company background and COVID assay authorization / scale-up proxy: https://en.wikipedia.org/wiki/Seegene

### 4.2 SD Biosensor rapid antigen evidence

SD Biosensor is used as a rapid-antigen/self-test demand spike case. The key residual question is not whether rapid tests had demand; they clearly did. The question is whether that demand was durable enough for C25 Stage3 / Green scoring, or whether it was a one-off pandemic procurement / at-home-test spike that should fade.

External source proxies:
- Reuters / Roche partnership proxy for rapid antibody / antigen diagnostic platform context: https://www.reuters.com/world/uk/britain-swiss-firm-roche-say-covid-19-tests-can-detect-mutant-virus-2020-12-23/
- Health/FDA recall context confirming SD Biosensor at-home test product presence and U.S. authorization risk distinction: https://www.health.com/condition/infectious-diseases/coronavirus/at-home-covid-test-recall-list

### 4.3 Wontech aesthetic medical device evidence

Wontech is used as an aesthetic medical-device / installed-base candidate rather than a pandemic diagnostics case. Its official site positions the company as a medical-beauty / aesthetic-and-medical technology firm and lists Oligio / Oligio X RF-device products, export footprint / export-ratio news snippets, and global family sites. This is closer to a C25 recurring device-installed-base / consumable-service channel than one-off diagnostic kit demand.

External source:
- Wontech official site: https://wontech.com/

## 5. Case-level calibration

### Case 1 — `096530` 씨젠: COVID molecular diagnostic export ramp positive with peak-fade watch

```text
case_id = C25_096530_SEEGENE_COVID_MOLECULAR_DIAGNOSTIC_EXPORT_RAMP_2020
symbol = 096530
name = 씨젠
trigger_date = 2020-03-13
entry_date = 2020-03-13
entry_price = 49,350
peak_date = 2020-08-10
peak_high = 322,200
mfe_pct = +552.89
mae_low_date = 2020-03-13
mae_low = 46,400
mae_pct = -5.98
later_fade_reference = 2020-11-25 low 175,300
peak_to_later_fade_pct = -45.59
classification = positive_with_full_4B_peak_fade_watch
```

Price rows used:
- `2020-03-13, ..., l=46400, c=49350`
- `2020-08-10, ..., h=322200`
- `2020-11-25, ..., l=175300`

Interpretation:
Seegene is a clean example of C25 working when the medical-device / diagnostics label converts into actual regulatory authorization, manufacturing scale, export demand, and revenue conversion. The v12 profile should allow this kind of trigger to climb into Stage3-Yellow/Green candidate territory, but only with peak-fade awareness: the same case also shows a large post-peak drawdown after the emergency-demand phase matured.

Residual lesson:
C25 should not simply score “diagnostics” as a static theme. It should score:
- authorization / regulatory permission,
- manufacturing or distribution scale,
- export destination breadth,
- order / revenue conversion,
- durability after emergency demand.

### Case 2 — `137310` 에스디바이오센서: rapid antigen / self-test demand spike, high-MFE but hard fade

```text
case_id = C25_137310_SDBIOSENSOR_RAPID_ANTIGEN_SELF_TEST_OMICRON_SPIKE_2022
symbol = 137310
name = 에스디바이오센서
trigger_date = 2022-01-28
entry_date = 2022-01-28
entry_price = 60,500
peak_date = 2022-02-04
peak_high = 81,000
mfe_pct = +33.88
mae_low_date = 2022-09-28
mae_low = 25,050
mae_pct = -58.60
classification = counterexample_high_MFE_high_MAE_one_time_pandemic_demand_fade
```

Price rows used:
- `2022-01-28, ..., h=61000, l=56000, c=60500`
- `2022-02-04, ..., h=81000`
- `2022-09-28, ..., l=25050`

Interpretation:
This case proves why C25 needs a one-time-demand penalty. The rapid-test/self-test narrative produced a strong short-term MFE, but the later path collapsed as pandemic testing demand normalized and product/regulatory risks became more visible. If the current profile gives full C25 credit to “rapid antigen test demand” without checking recurring platform revenue or post-pandemic demand durability, it will over-score the setup.

Residual lesson:
C25 should penalize one-off pandemic diagnostic demand unless there is clear evidence of:
- recurring diagnostic menu expansion,
- installed analyzer base,
- reimbursed routine testing demand,
- diversified non-COVID test portfolio,
- durable distributor or hospital procurement channel.

### Case 3 — `336570` 원텍: aesthetic medical device / installed-base export positive, source-repair required

```text
case_id = C25_336570_WONTECH_AESTHETIC_RF_DEVICE_EXPORT_INSTALLED_BASE_2023
symbol = 336570
name = 원텍
trigger_date = 2023-02-13
entry_date = 2023-02-13
entry_price = 5,490
peak_date = 2023-08-31
peak_high = 15,110
mfe_pct = +175.23
mae_low_date = 2023-03-24
mae_low = 5,250
mae_pct = -4.37
classification = positive_source_repair_required_installed_base_device_export_watch
```

Price rows used:
- `2023-02-13, ..., c=5490`
- `2023-03-24, ..., l=5250`
- `2023-08-31, ..., h=15110`

Interpretation:
Wontech is useful because it is not a pandemic-diagnostics proxy. It points toward the classic C25 device pattern: aesthetic medical equipment, RF/laser product lines, global expansion, installed-base formation, and potential recurring training / service / consumable economics. The price path is strong and relatively low-MAE from this trigger date, but the exact company-specific 2023 source URL should be repaired before production weighting. The official company source is enough to classify the company and product family, not enough to prove a precise 2023 order/revision trigger.

Residual lesson:
This is a good C25 shadow-rule candidate, not an immediate production-weight candidate. The trigger needs source repair around:
- product shipment / export approval,
- distributor expansion,
- recurring service / consumable evidence,
- OPM or revenue revision.

## 6. Current profile error mode

The residual problem is not “C25 is weak.” It is that C25 contains two very different mechanisms:

1. **Emergency diagnostics / pandemic procurement**
   - explosive MFE can occur,
   - but the signal often decays violently as one-off demand normalizes,
   - high-MFE does not equal durable Stage3.

2. **Installed-base medical devices / exportable equipment**
   - slower but more durable if order backlog, distributor expansion, installed base, and recurring revenue are visible,
   - should receive better C25 quality credit than generic “medical device” labels.

The profile should therefore split C25 into at least two sub-axes:
- `c25_diagnostics_emergency_demand_one_time_fade_penalty`
- `c25_installed_base_export_reimbursement_recurring_revenue_bridge_bonus`

## 7. Stage simulation

```json
{
  "score_simulation": [
    {
      "case_id": "C25_096530_SEEGENE_COVID_MOLECULAR_DIAGNOSTIC_EXPORT_RAMP_2020",
      "current_profile_likely_stage": "Stage3-Green_or_4B",
      "proposed_stage": "Stage3-Green_with_peak_fade_watch",
      "reason": "Authorization + manufacturing scale + export/revenue conversion were real; later peak fade should not erase the historical positive but should cap forward extrapolation."
    },
    {
      "case_id": "C25_137310_SDBIOSENSOR_RAPID_ANTIGEN_SELF_TEST_OMICRON_SPIKE_2022",
      "current_profile_likely_stage": "Stage2_or_Stage3_theme",
      "proposed_stage": "4B_to_4C_watch",
      "reason": "High short-term MFE but severe full-window MAE; one-time pandemic/self-test demand is not durable C25 without recurring portfolio evidence."
    },
    {
      "case_id": "C25_336570_WONTECH_AESTHETIC_RF_DEVICE_EXPORT_INSTALLED_BASE_2023",
      "current_profile_likely_stage": "Stage2-Actionable",
      "proposed_stage": "Stage2-Actionable_source_repair_required",
      "reason": "Strong price path and correct installed-base device type, but exact company-specific 2023 source URL needs repair before batch weight adoption."
    }
  ]
}
```

## 8. Shadow rule candidate

```json
{
  "shadow_weight_rule_candidate": {
    "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
    "rule_name": "c25_installed_base_reimbursement_export_recurring_revenue_bridge_required_shadow_only",
    "production_scoring_changed": false,
    "rule_intent": "Separate durable medical-device installed-base / reimbursement / export revenue conversion from one-time emergency diagnostic kit demand.",
    "positive_conditions": [
      "regulatory authorization or reimbursement approval is explicit",
      "company-specific product or device scope is confirmed",
      "export / distributor / installed-base channel is visible",
      "recurring revenue, consumables, service, or routine testing demand is visible",
      "revenue or margin revision confirms conversion"
    ],
    "penalty_conditions": [
      "one-time pandemic or emergency procurement without non-COVID portfolio conversion",
      "generic medical-device label without company-specific scope",
      "diagnostic kit demand spike with no routine-testing / analyzer-base bridge",
      "high-MFE followed by severe MAE before durable revenue confirmation",
      "source proxy only without trigger-date-specific company evidence"
    ],
    "suggested_weight_delta_shadow_only": {
      "installed_base_reimbursement_export_bridge": "+0.35",
      "explicit_recurring_revenue_or_consumable_bridge": "+0.25",
      "one_time_emergency_diagnostic_demand_penalty": "-0.45",
      "source_proxy_only_trigger_penalty": "-0.20"
    }
  }
}
```

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C25_096530_SEEGENE_COVID_MOLECULAR_DIAGNOSTIC_EXPORT_RAMP_2020","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"096530","name":"씨젠","trigger_date":"2020-03-13","entry_date":"2020-03-13","entry_price":49350,"peak_date":"2020-08-10","peak_high":322200,"mfe_pct":552.89,"mae_low_date":"2020-03-13","mae_low":46400,"mae_pct":-5.98,"classification":"positive_with_full_4B_peak_fade_watch","source_status":"verified_proxy","reused_case":false}
{"row_type":"case","case_id":"C25_137310_SDBIOSENSOR_RAPID_ANTIGEN_SELF_TEST_OMICRON_SPIKE_2022","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"137310","name":"에스디바이오센서","trigger_date":"2022-01-28","entry_date":"2022-01-28","entry_price":60500,"peak_date":"2022-02-04","peak_high":81000,"mfe_pct":33.88,"mae_low_date":"2022-09-28","mae_low":25050,"mae_pct":-58.60,"classification":"counterexample_high_MFE_high_MAE_one_time_pandemic_demand_fade","source_status":"verified_proxy","reused_case":false}
{"row_type":"case","case_id":"C25_336570_WONTECH_AESTHETIC_RF_DEVICE_EXPORT_INSTALLED_BASE_2023","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"336570","name":"원텍","trigger_date":"2023-02-13","entry_date":"2023-02-13","entry_price":5490,"peak_date":"2023-08-31","peak_high":15110,"mfe_pct":175.23,"mae_low_date":"2023-03-24","mae_low":5250,"mae_pct":-4.37,"classification":"positive_source_repair_required_installed_base_device_export_watch","source_status":"source_repair_required","reused_case":false}
{"row_type":"aggregate","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":3,"reused_case_count":0,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"verified_url_repair_needed_count":1,"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true}
{"row_type":"shadow_weight","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","rule_name":"c25_installed_base_reimbursement_export_recurring_revenue_bridge_required_shadow_only","production_scoring_changed":false,"installed_base_reimbursement_export_bridge_delta":0.35,"recurring_revenue_or_consumable_bridge_delta":0.25,"one_time_emergency_diagnostic_demand_penalty_delta":-0.45,"source_proxy_only_trigger_penalty_delta":-0.20}
{"row_type":"residual_contribution","round":"R7","loop":105,"canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c25_diagnostics_emergency_demand_fade_penalty_vs_installed_base_recurring_revenue_bridge","existing_axis_strengthened":"full_4b_requires_non_price_evidence scoped to C25 diagnostics/device-label rallies"}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not treat this MD as a request to change production scoring immediately.

Read this standalone research MD and batch it with other v12 residual research files. Extract only machine-readable rows and candidate shadow rules. Validate duplicate keys using:
canonical_archetype_id + symbol + trigger_type + entry_date.

Candidate rule:
- canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
- rule_name = c25_installed_base_reimbursement_export_recurring_revenue_bridge_required_shadow_only
- goal = split durable installed-base / reimbursement / export recurring revenue bridge from one-time pandemic diagnostics demand.

Do not patch production weights until enough C25 rows are accumulated and cross-validated.
```

## 11. Final bookkeeping

```text
이번 라운드: R7 / Loop 105 / L7_BIO_HEALTHCARE_MEDICAL
selected_round: R7
selected_loop: 105
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: DIAGNOSTIC_KIT_EXPORT_AND_AESTHETIC_DEVICE_INSTALLED_BASE_REVENUE_BRIDGE_VS_ONE_TIME_PANDEMIC_DEMAND_FADE

new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable case 수: 3
calibration_usable trigger 수: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
verified_url_repair_needed_count: 1

diversity_score_summary: C25 Priority 1 보강 + Seegene molecular diagnostic authorization/export ramp positive + SD Biosensor rapid-test one-time pandemic-demand high-MFE/high-MAE counterexample + Wontech aesthetic-device installed-base positive/source-repair watch
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C25 rows 33, 50-row target까지 17 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c25_diagnostics_emergency_demand_fade_penalty_vs_installed_base_recurring_revenue_bridge
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C25 diagnostics/device-label rallies
existing_axis_weakened: null
next_recommended_archetypes: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C22_INSURANCE_RATE_CYCLE_RESERVE, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```
