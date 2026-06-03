# E2R Stock-Web v12 Residual Research — R8 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R8
completed_loop: 73
next_round: R9
next_loop: 73
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_AND_POST_LAUNCH_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R8_loop_73_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
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
completed_loop  = 73
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

Therefore:

```text
scheduled_round = R8
scheduled_loop  = 73
```

R8 maps to:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

This run selects:

```text
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_AND_POST_LAUNCH_HIGH_MAE_ROUTER
```

This is a valid R8/L8 pairing.

---

## 1. Why this R8/C27 run

The no-repeat ledger shows C27 is already meaningfully covered, but the most repeated cases are concentrated in K-pop / studio / already-tested content IP names:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION:
  rows: 93
  symbols: 23
  date_range: 2016-03-24~2024-07-04
  good/bad S2: 31/8
  4B/4C: 24/7
  URL/proxy: 0/0
  top covered symbols: 035900(12), 352820(9), 194480(7), 253450(7), 122870(6), 293490(6)
```

This file avoids the top-covered names and tests game IP / live-service monetization:

```text
259960 크래프톤
225570 넥슨게임즈
036570 엔씨소프트
```

Research question:

```text
Can C27 distinguish durable global game-IP monetization from post-launch or turnaround rallies where first-month MFE is not enough to prove live-service retention, ARPU, content cadence, or operating leverage?
```

C27 is a monetization archetype, not a launch-day popularity archetype. A game launch can be a fireworks burst. A live-service IP is a power plant: it must keep generating users, ARPU, repeat content, and margins after the first bright launch candle.

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
| `259960` | 크래프톤 | active_like / KOSPI | none listed | true |
| `225570` | 넥슨게임즈 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2022-04-15 | true |
| `036570` | 엔씨소프트 | active_like / KOSPI | no 2024 overlap; old 2003 candidates only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
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
The Stock-Web price path is fully validated, but company-level game launch metrics, global user retention, ARPU, Steam/mobile ranking persistence, content cadence, live-service monetization, platform fee mix, and operating leverage evidence still require later URL repair through filings, IR decks, app/PC ranking data, disclosures, or sell-side reports before production weight promotion.
```

C27 interpretation used here:

```text
C27 is not simply “content/game stock rose.”
It asks whether IP popularity converts into durable monetization:
- active users and retention,
- ARPU / in-app purchase / PC sales quality,
- global launch persistence,
- content cadence,
- marketing cost discipline,
- and operating-margin conversion.
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
259960 + C27_CONTENT_IP_GLOBAL_MONETIZATION -> no direct match found
225570 + C27_CONTENT_IP_GLOBAL_MONETIZATION -> no direct match found
036570 + C27_CONTENT_IP_GLOBAL_MONETIZATION -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 1,
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
| `R8L73_C27_259960_20240213` | `259960` 크래프톤 | global game-IP live-service monetization rerating | positive anchor / durable IP monetization path |
| `R8L73_C27_225570_20240703` | `225570` 넥슨게임즈 | global launch / live-service hit narrative | high-MFE / high-MAE counterexample |
| `R8L73_C27_036570_20240926` | `036570` 엔씨소프트 | legacy-IP turnaround / content pipeline rerating | guarded counterexample / delayed high-MAE |

The intended residual:

```text
C27 should separate:
1. durable global game-IP monetization with persistent MFE and contained MAE;
2. post-launch live-service hit narratives where first-month MFE is real but retention and monetization remain unproven;
3. legacy-IP turnaround rallies that require pipeline evidence before Yellow/Green.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `259960` 크래프톤 — durable global game-IP monetization positive anchor

Trigger:

```text
trigger_date = 2024-02-08
trigger_type = Stage2-Actionable
trigger_family = global_game_ip_liveops_monetization_rerating
entry_date = 2024-02-13
entry_price = 219500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-08,213000.0,216000.0,211500.0,214000.0,125582.0,26880070500.0,10350001502000.0,48364493,KOSPI
2024-02-13,219500.0,230000.0,219000.0,230000.0,285922.0,64327285000.0,11123833390000.0,48364493,KOSPI
2024-02-16,243000.0,243500.0,236000.0,237500.0,64520.0,15397264000.0,11486567087500.0,48364493,KOSPI
2024-03-06,215000.0,218000.0,210500.0,213000.0,70286.0,14921617500.0,10301637009000.0,48364493,KOSPI
2024-05-09,269000.0,271000.0,255000.0,263500.0,430254.0,113265822536.0,12744043905500.0,48364493,KOSPI
2024-06-21,293000.0,297000.0,290000.0,297000.0,477134.0,141055111000.0,14222796291000.0,47888203,KOSPI
2024-07-30,289500.0,302000.0,289500.0,292500.0,99829.0,29478915000.0,14007942877500.0,47890403,KOSPI
2024-08-09,282500.0,295000.0,278000.0,294500.0,130482.0,37716999500.0,14103723683500.0,47890403,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 243500 | 2024-02-16 | 210500 | 2024-03-06 | +10.93% | -4.10% |
| 90 calendar days | 271000 | 2024-05-09 | 210500 | 2024-03-06 | +23.46% | -4.10% |
| 180 calendar days | 302000 | 2024-07-30 | 210500 | 2024-03-06 | +37.59% | -4.10% |

Interpretation:

```text
259960 is the clean C27 positive anchor.
The MFE was persistent across 30D/90D/180D and the MAE stayed contained.
This is the pattern C27 should keep as Stage2-Actionable / Yellow candidate after URL repair.
Green still requires live-service retention, monetization, and margin evidence rather than price alone.
```

### 6.2 `225570` 넥슨게임즈 — global launch hit narrative with high MFE and high MAE

Trigger:

```text
trigger_date = 2024-07-02
trigger_type = Stage2-Actionable-Guarded
trigger_family = global_launch_live_service_hit_narrative_high_mae
entry_date = 2024-07-03
entry_price = 18610.0
entry_price_type = next_tradable_open_after_launch_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-02,15100.0,15690.0,14620.0,15650.0,1322754.0,21340125910.0,1029829000500.0,65803770,KOSDAQ
2024-07-03,18610.0,18950.0,16490.0,17900.0,13677089.0,244724081220.0,1177887483000.0,65803770,KOSDAQ
2024-07-08,20500.0,22400.0,20050.0,21500.0,10017413.0,213924588680.0,1415168055000.0,65821770,KOSDAQ
2024-08-01,24050.0,30200.0,23900.0,28800.0,12093813.0,342892555550.0,1895666976000.0,65821770,KOSDAQ
2024-08-09,28000.0,30950.0,27550.0,28850.0,6249161.0,183599250500.0,1899650464500.0,65845770,KOSDAQ
2024-09-10,15360.0,15360.0,14760.0,14860.0,797948.0,11934045870.0,978563305640.0,65852174,KOSDAQ
2024-11-14,13530.0,13810.0,13020.0,13020.0,831826.0,11061228880.0,857499465480.0,65860174,KOSDAQ
2024-12-09,13050.0,13290.0,12560.0,12560.0,747238.0,9521918520.0,827203785440.0,65860174,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 30200 | 2024-08-01 | 16490 | 2024-07-03 | +62.28% | -11.39% |
| 90 calendar days | 30950 | 2024-08-09 | 14760 | 2024-09-10 | +66.31% | -20.69% |
| 180 calendar days | 30950 | 2024-08-09 | 12560 | 2024-12-09 | +66.31% | -32.51% |

Interpretation:

```text
225570 is the high-MFE/high-MAE C27 trap.
The launch narrative created powerful MFE, but the 90D/180D path revealed a retention/monetization uncertainty that price-only logic would miss.
This should be Stage2-Guarded or local 4B/high-MAE watch until live-service retention, global monetization, and operating leverage are URL-repaired.
```

### 6.3 `036570` 엔씨소프트 — legacy-IP turnaround rerating with delayed high-MAE

Trigger:

```text
trigger_date = 2024-09-25
trigger_type = Stage2-Actionable-Guarded
trigger_family = legacy_ip_turnaround_content_pipeline_rerating
entry_date = 2024-09-26
entry_price = 200000.0
entry_price_type = next_tradable_open_after_turnaround_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-09-25,194500.0,203500.0,193000.0,198500.0,197268.0,39316366600.0,4357873367000.0,21954022,KOSPI
2024-09-26,200000.0,206500.0,198200.0,206000.0,118101.0,24008456300.0,4522528532000.0,21954022,KOSPI
2024-10-25,210500.0,221000.0,210000.0,213500.0,135749.0,29165687000.0,4687183697000.0,21954022,KOSPI
2024-12-03,246500.0,248000.0,235000.0,239000.0,148457.0,36050342500.0,5247011258000.0,21954022,KOSPI
2024-12-09,197500.0,199000.0,188500.0,190000.0,150346.0,28757222100.0,4171264180000.0,21954022,KOSPI
2025-01-23,178000.0,178700.0,172800.0,173000.0,74975.0,13108798300.0,3798045806000.0,21954022,KOSPI
2025-03-11,158900.0,160900.0,157300.0,159300.0,70825.0,11255627650.0,3497275704600.0,21954022,KOSPI
2025-03-25,161100.0,162200.0,159500.0,161300.0,29268.0,4708259850.0,3541183748600.0,21954022,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 221000 | 2024-10-25 | 188500 | 2024-10-16 | +10.50% | -5.75% |
| 90 calendar days | 248000 | 2024-12-03 | 188500 | 2024-12-09 | +24.00% | -5.75% |
| 180 calendar days | 248000 | 2024-12-03 | 157300 | 2025-03-11 | +24.00% | -21.35% |

Interpretation:

```text
036570 is a guarded legacy-IP turnaround case.
The first 90D path was constructive, but the 180D path crossed the high-MAE zone.
This is not a clean false positive, but it is not Green either. It should remain Stage2-Guarded until pipeline proof, launch KPIs, monetization, and cost discipline are URL-repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R8L73_C27_GAME_IP_MONETIZATION_ROUTER","round":"R8","loop":73,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_AND_POST_LAUNCH_HIGH_MAE_ROUTER","symbol":"259960","name":"크래프톤","trigger_type":"Stage2-Actionable","trigger_family":"global_game_ip_liveops_monetization_rerating","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":219500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.93,"mae_30d_pct":-4.10,"mfe_90d_pct":23.46,"mae_90d_pct":-4.10,"mfe_180d_pct":37.59,"mae_180d_pct":-4.10,"peak_price_180d":302000.0,"peak_date_180d":"2024-07-30","trough_price_180d":210500.0,"trough_date_180d":"2024-03-06","calibration_usable":true,"case_polarity":"positive_anchor","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_liveops_retention_monetization_margin_bridge_repaired","residual_error_type":"positive_anchor_requires_url_repaired_live_service_and_margin_evidence_before_green"}
{"row_type":"trigger","research_id":"R8L73_C27_GAME_IP_MONETIZATION_ROUTER","round":"R8","loop":73,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_AND_POST_LAUNCH_HIGH_MAE_ROUTER","symbol":"225570","name":"넥슨게임즈","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"global_launch_live_service_hit_narrative_high_mae","trigger_date":"2024-07-02","entry_date":"2024-07-03","entry_price":18610.0,"entry_price_type":"next_tradable_open_after_launch_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":62.28,"mae_30d_pct":-11.39,"mfe_90d_pct":66.31,"mae_90d_pct":-20.69,"mfe_180d_pct":66.31,"mae_180d_pct":-32.51,"peak_price_180d":30950.0,"peak_date_180d":"2024-08-09","trough_price_180d":12560.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_retention_monetization_evidence_repaired","residual_error_type":"post_launch_mfe_overwhelmed_by_180d_high_mae_without_verified_liveops_bridge"}
{"row_type":"trigger","research_id":"R8L73_C27_GAME_IP_MONETIZATION_ROUTER","round":"R8","loop":73,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_AND_POST_LAUNCH_HIGH_MAE_ROUTER","symbol":"036570","name":"엔씨소프트","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"legacy_ip_turnaround_content_pipeline_rerating","trigger_date":"2024-09-25","entry_date":"2024-09-26","entry_price":200000.0,"entry_price_type":"next_tradable_open_after_turnaround_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.50,"mae_30d_pct":-5.75,"mfe_90d_pct":24.00,"mae_90d_pct":-5.75,"mfe_180d_pct":24.00,"mae_180d_pct":-21.35,"peak_price_180d":248000.0,"peak_date_180d":"2024-12-03","trough_price_180d":157300.0,"trough_date_180d":"2025-03-11","calibration_usable":true,"case_polarity":"counterexample_delayed_high_mae_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_until_pipeline_launch_kpi_margin_bridge_repaired","residual_error_type":"legacy_ip_turnaround_rerating_needs_pipeline_kpi_and_cost_bridge_before_green"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | IP quality | global monetization / retention | live-service cadence | market mispricing | valuation rerating | operating leverage | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `259960` | 15 | 14 | 13 | 11 | 12 | 12 | 7 | 84 | Stage2/Yellow after live-service monetization evidence repair |
| `225570` | 11 | 8 | 7 | 16 | 15 | 6 | 5 | 68 | Stage2-Guarded or 4B/high-MAE watch |
| `036570` | 10 | 7 | 8 | 10 | 9 | 6 | 5 | 55 | Stage2-Guarded until pipeline KPI and margin bridge repaired |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C27 risk is **launch-day MFE without live-service proof**:

```text
C27 clean path:
  established global IP
  + persistent MFE
  + contained MAE
  + URL-repaired retention, ARPU, live-service cadence, and operating leverage
  => Stage2-Actionable / Yellow, possible Green after proof

C27 post-launch high-MFE trap:
  global launch hype is real
  + first-month MFE is large
  + evidence remains source_proxy_only
  + 90D MAE <= -20% or 180D MAE <= -30%
  => Stage2-Guarded or local 4B/high-MAE watch, no Green

C27 legacy turnaround route:
  pipeline/turnaround narrative produces MFE
  + 180D MAE crosses -20%
  + pipeline KPI and cost discipline are not repaired
  => Stage2-Guarded until evidence bridge is visible
```

`259960` prevents overblocking.  
`225570` shows that a strong launch can still be a high-MAE trap.  
`036570` shows that turnaround IP can work temporarily, but Green requires proof that the new pipeline is not just a valuation rebound.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R8L73_C27_GAME_IP_MONETIZATION_ROUTER",
  "round": "R8",
  "loop": 73,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_AND_POST_LAUNCH_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 27.90,
  "avg_mae_30d_pct": -7.08,
  "avg_mfe_90d_pct": 37.92,
  "avg_mae_90d_pct": -10.18,
  "avg_mfe_180d_pct": 42.63,
  "avg_mae_180d_pct": -19.32,
  "max_mfe_180d_pct": 66.31,
  "worst_mae_180d_pct": -32.51
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R8L73_C27_GAME_IP_MONETIZATION_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "259960",
      "reason": "persistent MFE and contained MAE; requires URL-repaired retention/ARPU/live-service margin bridge before Green"
    }
  ],
  "local_4b_watch": [
    {
      "symbol": "225570",
      "reason": "launch MFE was very strong, but MAE_90D reached -20.69% and MAE_180D reached -32.51%"
    },
    {
      "symbol": "036570",
      "reason": "turnaround rerating had constructive 90D MFE, but MAE_180D reached -21.35%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "global launch retention",
    "ARPU / monetization quality",
    "live-service content cadence",
    "platform ranking persistence",
    "marketing cost discipline",
    "operating-margin conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_AND_POST_LAUNCH_HIGH_MAE_ROUTER
rule_name: C27_game_ip_liveops_monetization_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C27 content/game IP monetization cases:

Tier A: verified durable global IP monetization
  Conditions:
    - launch or IP relevance is backed by URL-repaired retention, ARPU, ranking persistence, or revenue evidence
    - 30D/90D MAE is contained
    - MFE persists beyond one launch window
    - margin / operating leverage bridge is visible
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after live-service monetization and margin evidence are verified

Tier B: high-MFE launch without retention bridge
  Conditions:
    - first-month MFE is strong
    - source_proxy_only or evidence_url_pending remains true
    - 90D MAE <= -20% or 180D MAE <= -30%
  Routing:
    - Stage2-Actionable-Guarded at most
    - local 4B/high-MAE watch
    - no Green

Tier C: legacy-IP turnaround without KPI bridge
  Conditions:
    - turnaround or pipeline rerating creates MFE
    - pipeline KPI / launch data / cost discipline evidence is missing
    - 180D MAE <= -20%
  Routing:
    - Stage2-Guarded
    - no Green until KPI and margin bridge are repaired
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c27_game_ip_liveops_monetization_and_high_mae_router",
  "scope": "canonical_archetype_id:C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "liveops_retention_arpu_bridge_required_for_green": true,
    "launch_hype_stage2_cap": "guarded_only_until_url_repair",
    "high_mae_watch_threshold_90d_pct": -20.0,
    "high_mae_watch_threshold_180d_pct": -30.0,
    "legacy_turnaround_high_mae_threshold_180d_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One durable global IP positive and two game-IP launch/turnaround high-MAE cases show that C27 should require URL-repaired retention, monetization, and operating-leverage evidence before Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R8L73_C27_GAME_IP_MONETIZATION_ROUTER",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "contribution": "Adds three non-top-covered C27 game-IP monetization cases and separates a durable global live-service monetization path from high-MFE post-launch and legacy-turnaround paths that later suffer high MAE. C27 Green should require URL-repaired retention, ARPU, ranking persistence, content cadence, and operating leverage evidence.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price game-IP monetization triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C27 source_proxy_only launch cases with 90D MAE <= -20% or 180D MAE <= -30% should route to Stage2-Guarded or 4B/high-MAE watch; legacy-turnaround cases with 180D MAE <= -20% require KPI repair before Yellow/Green."
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
    259960: false
    225570: false
    036570: false
  evidence_url_pending:
    259960: true
    225570: true
    036570: true
  source_proxy_only:
    259960: true
    225570: true
    036570: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C27 game-IP residual shape and high-MAE guardrail design, but should not promote positive weights until filings/IR/app-ranking/PC-ranking/report data verifies retention, ARPU, global monetization, content cadence, and operating leverage.
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
2. Preserve R8 / loop 73 metadata.
3. Add the cases to C27_CONTENT_IP_GLOBAL_MONETIZATION only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/app-ranking/PC-ranking/report data verifies retention, ARPU, global monetization, content cadence, and operating leverage.
6. Add a shadow-only rule candidate named C27_game_ip_liveops_monetization_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C27-specific guards:
   - source_proxy_only -> no Green
   - launch hype without repaired live-service retention bridge -> Stage2-Guarded at most
   - 90D MAE <= -20% or 180D MAE <= -30% -> local 4B/high-MAE watch
   - legacy turnaround with 180D MAE <= -20% -> no Yellow/Green until KPI repair
   - Green requires repaired retention/ARPU/content-cadence/margin bridge
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R8
completed_loop = 73
next_round = R9
next_loop = 73
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING
```
