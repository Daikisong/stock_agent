# E2R Stock-Web v12 Residual Research — R8 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R8
completed_loop: 74
next_round: R9
next_loop: 74
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SECURITY_AUTH_CONTRACT_RETENTION_AND_THEME_SPIKE_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R8_loop_74_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Execution gate

This file follows the v12 historical calibration prompt as the execution procedure.  
`V12_Research_No_Repeat_Index.md` is used only as the duplicate-avoidance ledger.

This is not a live stock discovery run, not investment advice, not a trading instruction, and not a `stock_agent` code patch.  
The only output is a standalone historical calibration / sector-archetype residual Markdown artifact.

The active execution prompt fixes the research mode:

```text
primary_price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap

production_scoring_changed = false
shadow_weight_only = true
must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_include_score_return_alignment = true
must_include_current_calibrated_profile_stress_test = true
must_include_positive_and_counterexample_balance = true
must_output_every_usable_trigger_as_jsonl = true
```

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R7
completed_loop  = 74
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

Therefore:

```text
scheduled_round = R8
scheduled_loop  = 74
```

R8 maps to:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

This run selects:

```text
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = SECURITY_AUTH_CONTRACT_RETENTION_AND_THEME_SPIKE_HIGH_MAE_ROUTER
```

This is a valid R8/L8 pairing.

---

## 1. Why this R8/C28 run

The no-repeat ledger shows C28 is already covered, but the top symbols are concentrated in larger software/security names:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
  rows: 87
  symbols: 18
  date_range: 2019-05-27~2024-07-22
  good/bad S2: 26/6
  4B/4C: 21/3
  URL/proxy: 0/0
  top covered symbols: 012510(20), 053800(16), 263860(12), 030520(7), 131370(6), 042510(4)
```

This file avoids those top-covered names and adds three lower-repeat security/authentication cases:

```text
136540 윈스
203650 드림시큐리티
192250 케이사인
```

Research question:

```text
Can C28 separate low-MAE security contract-retention rerating from authentication/security theme spikes where the entry has weak MFE and later high MAE before recurring revenue or contract retention evidence is repaired?
```

C28 is a retention archetype. A security headline is the alarm bell; recurring contract revenue is the locked door. The model should not reward the bell alone. It must ask whether maintenance contracts, renewals, public-sector or enterprise deal continuity, margin, and cash conversion keep the door closed after the first spike.

---

## 2. Price atlas validation

### Stock-Web manifest snapshot

```json
{
  "price_atlas_repo": "Songdaiki/stock-web",
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "research_pack_default_price_basis": "tradable_raw"
}
```

All price rows below use:

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

### Candidate profile checks

| symbol | name | market/profile status | corporate-action candidate overlap with selected 180D window | calibration usable |
|---|---|---|---|---|
| `136540` | 윈스 | active_like / KOSDAQ | none listed | true |
| `203650` | 드림시큐리티 | active_like / KOSDAQ | no 2024 overlap; latest relevant candidate before 2024 was 2019-11-26 | true |
| `192250` | 케이사인 | active_like / KOSDAQ | 2024-11-01 candidate exists, but it is after the selected 2024-03-27 entry plus 180 calendar days | true for 180D window |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 180D windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
For 192250, 1Y/2Y would be contaminated_or_unavailable because of the 2024-11-01 corporate-action candidate, but 30D/90D/180D are usable.
```

---

## 3. Evidence status and trigger discipline

This artifact intentionally uses conservative non-price evidence flags:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level security contract renewal, enterprise/public-sector customer retention, authentication recurring revenue, subscription/maintenance mix, cloud/security appliance margin, and cash-conversion evidence still require later URL repair through filings, IR decks, public procurement data, contract disclosures, or sell-side reports before production weight promotion.
```

C28 interpretation used here:

```text
C28 is not simply “security stock rose.”
It asks whether software/security revenue is retention-convertible:
- recurring maintenance or subscription revenue,
- enterprise/public-sector contract renewal,
- customer retention / expansion,
- authentication or security appliance installed-base monetization,
- margin and cash conversion,
- and contained MAE after the trigger.
```

This file is therefore a residual/guardrail artifact, not a positive production patch.

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
136540 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
203650 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
192250 + C28_SOFTWARE_SECURITY_CONTRACT_RETENTION -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R8L74_C28_136540_20240503` | `136540` 윈스 | network security contract-retention low-MAE rerating | positive-guarded low-MAE holdout |
| `R8L74_C28_203650_20240215` | `203650` 드림시큐리티 | authentication/security theme relief with low MFE and high MAE | weak-MFE high-MAE counterexample |
| `R8L74_C28_192250_20240327` | `192250` 케이사인 | authentication/security theme spike without contract bridge | 4B/4C high-MAE counterexample |

The intended residual:

```text
C28 should separate:
1. security-contract retention paths where MFE is modest but MAE stays controlled;
2. authentication/security theme relief moves where the revenue-retention bridge is not proven and 180D MAE becomes severe;
3. theme spikes that spend the upside on the entry day and then fail the Stage2 capital-preservation test.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `136540` 윈스 — network security contract-retention low-MAE rerating

Trigger:

```text
trigger_date = 2024-05-02
trigger_type = Stage2-Actionable-Guarded
trigger_family = network_security_contract_retention_low_mae_rerating
entry_date = 2024-05-03
entry_price = 12750.0
entry_price_type = next_tradable_open_after_security_contract_retention_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-03,12750.0,12980.0,12750.0,12850.0,71902.0,924663010.0,175327481700.0,13644162,KOSDAQ
2024-05-13,13010.0,13080.0,12660.0,12880.0,24571.0,314502910.0,175736806560.0,13644162,KOSDAQ
2024-05-17,13230.0,13270.0,13110.0,13240.0,17304.0,228393570.0,180648704880.0,13644162,KOSDAQ
2024-06-11,13600.0,14050.0,13600.0,13850.0,70958.0,985546570.0,188971643700.0,13644162,KOSDAQ
2024-06-28,14620.0,14950.0,14620.0,14670.0,41958.0,620264370.0,200159856540.0,13644162,KOSDAQ
2024-08-05,12820.0,12940.0,12000.0,12400.0,39016.0,484508400.0,169187608800.0,13644162,KOSDAQ
2024-09-24,12560.0,12800.0,12550.0,12800.0,5736.0,72822730.0,174645273600.0,13644162,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 13270 | 2024-05-17 | 12660 | 2024-05-13 | +4.08% | -0.71% |
| 90 calendar days | 14950 | 2024-06-28 | 12660 | 2024-05-13 | +17.25% | -0.71% |
| 180 calendar days | 14950 | 2024-06-28 | 12000 | 2024-08-05 | +17.25% | -5.88% |

Interpretation:

```text
136540 is the low-MAE positive-guarded holdout.
The MFE was not explosive, but the risk path was clean. That is important for C28 because contract-retention software/security names may rerate through stability rather than blowoff.
It can remain Stage2-Guarded / Yellow candidate after URL-repaired recurring-revenue, renewal, and margin evidence.
```

### 6.2 `203650` 드림시큐리티 — authentication/security theme relief with high MAE

Trigger:

```text
trigger_date = 2024-02-14
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = authentication_security_theme_relief_low_mfe_high_mae
entry_date = 2024-02-15
entry_price = 3830.0
entry_price_type = next_tradable_open_after_security_auth_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-14,3690.0,3830.0,3665.0,3795.0,873726.0,3299407400.0,192048836430.0,50605754,KOSDAQ
2024-02-15,3830.0,4060.0,3810.0,4020.0,3969854.0,15780341660.0,203435131080.0,50605754,KOSDAQ
2024-02-27,3705.0,3755.0,3650.0,3675.0,406435.0,1499258215.0,185976145950.0,50605754,KOSDAQ
2024-03-13,3835.0,4075.0,3785.0,3940.0,2916481.0,11587615535.0,199386670760.0,50605754,KOSDAQ
2024-04-11,3295.0,3340.0,3265.0,3330.0,306850.0,1014137425.0,168517160820.0,50605754,KOSDAQ
2024-08-05,2685.0,2740.0,2285.0,2295.0,519724.0,1295341590.0,116140205430.0,50605754,KOSDAQ
2024-08-27,2965.0,3215.0,2950.0,3120.0,4101364.0,12881632680.0,157889952480.0,50605754,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 4075 | 2024-03-13 | 3650 | 2024-02-27 | +6.40% | -4.70% |
| 90 calendar days | 4075 | 2024-03-13 | 3265 | 2024-04-11 | +6.40% | -14.75% |
| 180 calendar days | 4075 | 2024-03-13 | 2285 | 2024-08-05 | +6.40% | -40.34% |

Interpretation:

```text
203650 is the weak-MFE / high-MAE counterexample.
The security/authentication theme was plausible, but the forward path never produced enough upside to justify the later -40.34% drawdown.
This should block Stage2 or route to local 4B/high-MAE watch until contract retention and recurring revenue evidence are repaired.
```

### 6.3 `192250` 케이사인 — authentication/security theme spike without contract bridge

Trigger:

```text
trigger_date = 2024-03-26
trigger_type = 4B-local-watch
trigger_family = quantum_authentication_security_theme_spike_without_contract_bridge
entry_date = 2024-03-27
entry_price = 1721.0
entry_price_type = next_tradable_open_after_auth_security_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-26,1241.0,1614.0,1241.0,1614.0,61177012.0,91693653056.0,114063408798.0,70671257,KOSDAQ
2024-03-27,1721.0,1736.0,1487.0,1487.0,43331685.0,69573623150.0,105088159159.0,70671257,KOSDAQ
2024-04-09,1277.0,1394.0,1264.0,1310.0,5420821.0,7296815510.0,92579346670.0,70671257,KOSDAQ
2024-06-24,1134.0,1144.0,1100.0,1131.0,564587.0,630190938.0,79929191667.0,70671257,KOSDAQ
2024-08-05,1032.0,1041.0,860.0,902.0,961944.0,918876712.0,63745473814.0,70671257,KOSDAQ
2024-08-27,958.0,1143.0,958.0,1079.0,14935834.0,16291962153.0,76254286303.0,70671257,KOSDAQ
2024-09-23,1035.0,1050.0,1008.0,1012.0,324678.0,332428446.0,71519312084.0,70671257,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 1736 | 2024-03-27 | 1264 | 2024-04-09 | +0.87% | -26.55% |
| 90 calendar days | 1736 | 2024-03-27 | 1100 | 2024-06-24 | +0.87% | -36.08% |
| 180 calendar days | 1736 | 2024-03-27 | 860 | 2024-08-05 | +0.87% | -50.03% |

Interpretation:

```text
192250 is the hard theme-spike counterexample.
The event candle had already spent the upside at entry. The forward windows show almost no MFE and severe MAE.
This belongs in local 4B/4C high-MAE watch, not Stage2/Green, unless a real contract-retention or recurring-revenue bridge existed before the entry.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R8L74_C28_SECURITY_CONTRACT_RETENTION_ROUTER","round":"R8","loop":74,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_AUTH_CONTRACT_RETENTION_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"136540","name":"윈스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"network_security_contract_retention_low_mae_rerating","trigger_date":"2024-05-02","entry_date":"2024-05-03","entry_price":12750.0,"entry_price_type":"next_tradable_open_after_security_contract_retention_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.08,"mae_30d_pct":-0.71,"mfe_90d_pct":17.25,"mae_90d_pct":-0.71,"mfe_180d_pct":17.25,"mae_180d_pct":-5.88,"peak_price_180d":14950.0,"peak_date_180d":"2024-06-28","trough_price_180d":12000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_low_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_contract_retention_margin_bridge_repaired","residual_error_type":"low_mae_security_contract_path_requires_url_repaired_retention_recurring_revenue_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R8L74_C28_SECURITY_CONTRACT_RETENTION_ROUTER","round":"R8","loop":74,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_AUTH_CONTRACT_RETENTION_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"203650","name":"드림시큐리티","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"authentication_security_theme_relief_low_mfe_high_mae","trigger_date":"2024-02-14","entry_date":"2024-02-15","entry_price":3830.0,"entry_price_type":"next_tradable_open_after_security_auth_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.4,"mae_30d_pct":-4.7,"mfe_90d_pct":6.4,"mae_90d_pct":-14.75,"mfe_180d_pct":6.4,"mae_180d_pct":-40.34,"peak_price_180d":4075.0,"peak_date_180d":"2024-03-13","trough_price_180d":2285.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_low_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch_until_contract_retention_bridge_repaired","residual_error_type":"security_auth_theme_had_low_mfe_and_later_high_mae_without_recurring_contract_bridge"}
{"row_type":"trigger","research_id":"R8L74_C28_SECURITY_CONTRACT_RETENTION_ROUTER","round":"R8","loop":74,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_AUTH_CONTRACT_RETENTION_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"192250","name":"케이사인","trigger_type":"4B-local-watch","trigger_family":"quantum_authentication_security_theme_spike_without_contract_bridge","trigger_date":"2024-03-26","entry_date":"2024-03-27","entry_price":1721.0,"entry_price_type":"next_tradable_open_after_auth_security_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.87,"mae_30d_pct":-26.55,"mfe_90d_pct":0.87,"mae_90d_pct":-36.08,"mfe_180d_pct":0.87,"mae_180d_pct":-50.03,"peak_price_180d":1736.0,"peak_date_180d":"2024-03-27","trough_price_180d":860.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_theme_spike_extreme_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"authentication_security_theme_spike_spent_the_upside_at_entry_and_created_extreme_mae"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | contract-retention bridge | recurring revenue visibility | customer quality | margin / cash conversion | market mispricing | theme-spike risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `136540` | 11 | 10 | 10 | 8 | 6 | 10 | 6 | 61 | Stage2-Guarded / Yellow after retention evidence repair |
| `203650` | 4 | 3 | 4 | 3 | 4 | 2 | 4 | 24 | blocked Stage2 or 4B/high-MAE watch |
| `192250` | 2 | 2 | 3 | 2 | 3 | 0 | 4 | 16 | 4B/4C high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C28 issue is **security theme relevance without retention conversion**:

```text
C28 low-MAE retention path:
  enterprise/public-sector security contract relevance
  + low MAE
  + modest but improving MFE
  + URL-repaired renewal/recurring-revenue/margin evidence
  => Stage2-Guarded / Yellow candidate

C28 authentication theme weak-MFE path:
  security/authentication label exists
  + MFE_90D < +10%
  + MAE_180D <= -35%
  + no recurring contract bridge
  => block Stage2 or local 4B/high-MAE watch

C28 same-window theme spike:
  peak occurs on entry day
  + MFE_30D < +5%
  + MAE_30D <= -20%
  => route to local 4B/4C watch
```

`136540` prevents overblocking.  
`203650` shows why weak-MFE security-authentication rallies should be capped.  
`192250` is the hard 4B/4C guardrail: the theme spark was real, but the contract-retention bridge was missing.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R8L74_C28_SECURITY_CONTRACT_RETENTION_ROUTER",
  "round": "R8",
  "loop": 74,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "fine_archetype_id": "SECURITY_AUTH_CONTRACT_RETENTION_AND_THEME_SPIKE_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 3.78,
  "avg_mae_30d_pct": -10.65,
  "avg_mfe_90d_pct": 8.17,
  "avg_mae_90d_pct": -17.18,
  "avg_mfe_180d_pct": 8.17,
  "avg_mae_180d_pct": -32.08,
  "max_mfe_180d_pct": 17.25,
  "worst_mae_180d_pct": -50.03
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R8L74_C28_SECURITY_CONTRACT_RETENTION_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "136540",
      "reason": "modest MFE but very contained MAE; suitable as a contract-retention holdout after evidence repair"
    }
  ],
  "blocked_stage2_or_local_4b_watch": [
    {
      "symbol": "203650",
      "reason": "MFE stayed at +6.40% while 180D MAE reached -40.34%; recurring contract bridge was not visible"
    },
    {
      "symbol": "192250",
      "reason": "entry-day peak with only +0.87% MFE and -50.03% 180D MAE; theme spike without contract bridge"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "maintenance / subscription / recurring security revenue",
    "enterprise or public-sector renewal evidence",
    "contract retention and customer expansion",
    "authentication installed-base monetization",
    "gross margin and cash conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SECURITY_AUTH_CONTRACT_RETENTION_AND_THEME_SPIKE_HIGH_MAE_ROUTER
rule_name: C28_security_contract_retention_vs_theme_spike_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C28 software/security contract-retention cases:

Tier A: verified contract-retention winner
  Conditions:
    - renewal, maintenance/subscription, or recurring security revenue evidence is URL-repaired
    - MAE remains contained
    - MFE improves beyond the first event candle
    - margin / cash conversion is visible
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after retention and recurring-revenue bridge are verified

Tier B: weak-MFE security/authentication theme
  Conditions:
    - MFE_90D < +10%
    - MAE_180D <= -35%
    - bridge evidence remains source_proxy_only
  Routing:
    - block Stage2 or local 4B/high-MAE watch
    - no Green

Tier C: entry-day theme spike
  Conditions:
    - MFE_30D < +5%
    - MAE_30D <= -20%
    - peak occurs on entry day or first 5 trading days
    - no contract-retention bridge
  Routing:
    - block Stage2
    - route to local 4B/4C watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c28_security_contract_retention_vs_theme_spike_high_mae_router",
  "scope": "canonical_archetype_id:C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "contract_retention_recurring_revenue_bridge_required_for_green": true,
    "low_mae_retention_stage2_guarded_allowed": true,
    "weak_mfe_threshold_90d_pct": 10.0,
    "weak_mfe_hard_mae_threshold_180d_pct": -35.0,
    "entry_day_spike_mfe30_threshold_pct": 5.0,
    "entry_day_spike_mae30_threshold_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One low-MAE security retention holdout and two weak-MFE/high-MAE authentication/security theme counterexamples show that C28 should require URL-repaired contract retention and recurring-revenue evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R8L74_C28_SECURITY_CONTRACT_RETENTION_ROUTER",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
  "contribution": "Adds three non-top-covered C28 security/authentication cases and separates a low-MAE network-security contract-retention path from weak-MFE/high-MAE authentication/security theme spikes. C28 Green should require URL-repaired recurring revenue, renewal, customer retention, installed-base monetization, margin, and cash-conversion evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price security/contract-retention triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C28 source_proxy_only cases with MFE_90D < +10% and MAE_180D <= -35% should block Stage2 or route to local 4B/high-MAE watch; entry-day theme spikes with MFE_30D < +5% and MAE_30D <= -20% should route to 4B/4C watch."
}
```

---

## 13. Validation scope

```yaml
validation_scope:
  price_source: Songdaiki/stock-web
  price_basis: tradable_raw
  price_adjustment_status: raw_unadjusted_marcap
  manifest_max_date: 2026-02-20
  forward_window_required: 180_calendar_days
  forward_window_available: true
  raw_shard_used_for_weight_calibration: false
  corporate_action_contaminated_180D_window:
    136540: false
    203650: false
    192250: false
  evidence_url_pending:
    136540: true
    203650: true
    192250: true
  source_proxy_only:
    136540: true
    203650: true
    192250: true
  special_handling:
    192250:
      corporate_action_candidate_date: "2024-11-01"
      note: "Entry~D+180 window is before the candidate date; 1Y/2Y fields would be contaminated_or_unavailable."
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C28 security/software contract-retention residual shape and high-MAE guardrail design, but should not promote positive weights until filings, IR, public procurement, contract disclosure, or report data verifies renewal, recurring revenue, customer retention, margin, and cash conversion.
- It should not be read as a current investment view.
```

---

## 14. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact.

Task:
1. Ingest the machine-readable trigger rows.
2. Preserve R8 / loop 74 metadata.
3. Add the cases to C28_SOFTWARE_SECURITY_CONTRACT_RETENTION only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/procurement/contract-disclosure/report data verifies recurring security revenue, renewal, customer retention, installed-base monetization, margin, and cash conversion.
6. Add a shadow-only rule candidate named C28_security_contract_retention_vs_theme_spike_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C28-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired contract-retention / recurring-revenue / margin bridge
   - low-MAE retention paths may stay Stage2-Guarded until evidence repair
   - MFE_90D < +10% and MAE_180D <= -35% -> block Stage2 or local 4B/high-MAE watch
   - MFE_30D < +5% and MAE_30D <= -20% after entry-day theme spike -> 4B/4C watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R8
completed_loop = 74
next_round = R9
next_loop = 74
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING
round_schedule_status = valid
round_sector_consistency = pass
```
