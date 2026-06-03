# E2R Stock-Web v12 Residual Research — R8 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R8
completed_loop: 75
next_round: R9
next_loop: 75
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_GLOBAL_LIVEOPS_LAUNCH_AND_BLOCKCHAIN_EVENT_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R8_loop_75_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
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
completed_loop  = 75
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

Therefore:

```text
scheduled_round = R8
scheduled_loop  = 75
```

R8 maps to:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

This run selects:

```text
canonical_archetype_id = C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id = GAME_IP_GLOBAL_LIVEOPS_LAUNCH_AND_BLOCKCHAIN_EVENT_HIGH_MAE_ROUTER
```

This is a valid R8/L8 pairing.

---

## 1. Why this R8/C27 run

The no-repeat ledger shows C27 is already covered, but top coverage is concentrated in entertainment agencies, webtoon/studio, and major content names:

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

This file avoids those top-covered C27 symbols and tests game-IP monetization / live-ops / launch-event cases:

```text
259960 크래프톤
225570 넥슨게임즈
112040 위메이드
```

Research question:

```text
Can C27 separate durable global game-IP monetization from new-title or blockchain-game event spikes where MFE is real but later MAE exposes retention, ARPPU, token-economics, and margin uncertainty?
```

C27 is an IP monetization archetype. A game launch is the opening weekend; a rerating needs the whole season. The signal must travel from launch buzz to retention, live-ops revenue, ARPPU, regional mix, platform fees, and margin. If players leave or token economics wobble, the event candle becomes a launchpad with no fuel.

---

## 2. Price atlas validation

### Stock-Web manifest snapshot

```json
{
  "price_atlas_repo": "Songdaiki/stock-web",
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
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
| `225570` | 넥슨게임즈 | active_like / KOSDAQ | no 2024 overlap; latest candidate 2022-04-15 | true |
| `112040` | 위메이드 | active_like / KOSDAQ | no 2024 overlap; latest candidates 2021-09-13 / 2021-10-06 | true |

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
The Stock-Web price path is fully validated, but company-level game revenue, active-user retention, payer conversion, ARPPU, live-ops cadence, global-region mix, platform fees, launch tail durability, token economics, and operating-margin evidence still require later URL repair through filings, IR decks, app-market data, Steam/console metrics, or sell-side reports before production weight promotion.
```

C27 interpretation used here:

```text
C27 is not simply “game stock rose.”
It asks whether content IP is monetization-convertible:
- launch traffic and retention,
- live-ops revenue and ARPPU,
- payer conversion and regional mix,
- new-title pipeline durability,
- platform fee / marketing spend / margin,
- token economics where relevant,
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
259960 + C27_CONTENT_IP_GLOBAL_MONETIZATION -> no direct match found
225570 + C27_CONTENT_IP_GLOBAL_MONETIZATION -> no direct match found
112040 + C27_CONTENT_IP_GLOBAL_MONETIZATION -> no direct match found
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
| `R8L75_C27_259960_20240213` | `259960` 크래프톤 | global game-IP live-ops / earnings reacceleration | positive-guarded low-MAE |
| `R8L75_C27_225570_20240704` | `225570` 넥슨게임즈 | new global title launch / high MFE later drawdown | high-MFE later-MAE counterexample |
| `R8L75_C27_112040_20240312` | `112040` 위메이드 | blockchain-game IP / token event high-MFE high-MAE | event-MFE overwhelmed counterexample |

The intended residual:

```text
C27 should separate:
1. global game-IP live-ops paths where MFE persists and MAE remains contained;
2. new title launches where first-window MFE is large but later MAE requires retention and monetization proof;
3. blockchain/token game-IP events where event MFE is overwhelmed by later drawdown unless token economics and cash-flow bridge are repaired.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `259960` 크래프톤 — global game-IP live-ops / earnings reacceleration

Trigger:

```text
trigger_date = 2024-02-08
trigger_type = Stage2-Actionable-Guarded
trigger_family = global_game_ip_liveops_earnings_reacceleration_low_mae_rerating
entry_date = 2024-02-13
entry_price = 219500.0
entry_price_type = next_tradable_open_after_game_ip_earnings_liveops_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-08,213000.0,216000.0,211500.0,214000.0,125582.0,26880070500.0,10350001502000.0,48364493,KOSPI
2024-02-13,219500.0,230000.0,219000.0,230000.0,285922.0,64327285000.0,11123833390000.0,48364493,KOSPI
2024-02-16,243000.0,243500.0,236000.0,237500.0,64520.0,15397264000.0,11486567087500.0,48364493,KOSPI
2024-03-06,215000.0,218000.0,210500.0,213000.0,70286.0,14921617500.0,10301637009000.0,48364493,KOSPI
2024-03-27,250000.0,265000.0,248000.0,257000.0,371514.0,95267164000.0,12429674701000.0,48364493,KOSPI
2024-05-09,269000.0,271000.0,255000.0,263500.0,430254.0,113265822536.0,12744043905500.0,48364493,KOSPI
2024-07-30,289500.0,302000.0,289500.0,292500.0,99829.0,29478915000.0,14007942877500.0,47890403,KOSPI
2024-08-05,285000.0,286500.0,260000.0,273000.0,173656.0,47632247000.0,13074080019000.0,47890403,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 243500 | 2024-02-16 | 210500 | 2024-03-06 | +10.93% | -4.10% |
| 90 calendar days | 271000 | 2024-05-09 | 210500 | 2024-03-06 | +23.46% | -4.10% |
| 180 calendar days | 302000 | 2024-07-30 | 210500 | 2024-03-06 | +37.59% | -4.10% |

Interpretation:

```text
259960 is the C27 positive-guarded anchor.
The path was not a one-day launch spike; MFE expanded from 30D to 180D while MAE stayed contained.
This can support Stage2-Guarded / Yellow after URL-repaired live-ops revenue, margin, and pipeline evidence. It should not become Green from price path alone.
```

### 6.2 `225570` 넥슨게임즈 — new global title launch with later drawdown

Trigger:

```text
trigger_date = 2024-07-03
trigger_type = Stage2-Actionable-Guarded
trigger_family = new_game_launch_global_concurrency_high_mfe_later_drawdown
entry_date = 2024-07-04
entry_price = 18700.0
entry_price_type = next_tradable_open_after_new_game_launch_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-03,18610.0,18950.0,16490.0,17900.0,13677089.0,244724081220.0,1177887483000.0,65803770,KOSDAQ
2024-07-04,18700.0,19630.0,17720.0,19200.0,10054501.0,189241099640.0,1263432384000.0,65803770,KOSDAQ
2024-07-16,18200.0,18200.0,17200.0,17550.0,1921762.0,33769284480.0,1155172063500.0,65821770,KOSDAQ
2024-08-01,24050.0,30200.0,23900.0,28800.0,12093813.0,342892555550.0,1895666976000.0,65821770,KOSDAQ
2024-08-09,28000.0,30950.0,27550.0,28850.0,6249161.0,183599250500.0,1899650464500.0,65845770,KOSDAQ
2024-09-10,15360.0,15360.0,14760.0,14860.0,797948.0,11934045870.0,978563305640.0,65852174,KOSDAQ
2024-10-17,15000.0,15160.0,14760.0,14760.0,467448.0,6954852150.0,972096168240.0,65860174,KOSDAQ
2024-12-09,13050.0,13290.0,12560.0,12560.0,747238.0,9521918520.0,827203785440.0,65860174,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 30200 | 2024-08-01 | 17200 | 2024-07-16 | +61.50% | -8.02% |
| 90 calendar days | 30950 | 2024-08-09 | 14760 | 2024-09-10 | +65.51% | -21.07% |
| 180 calendar days | 30950 | 2024-08-09 | 12560 | 2024-12-09 | +65.51% | -32.83% |

Interpretation:

```text
225570 is the high-MFE later-MAE warning.
The new-title launch produced a large forward upside window, but the 90D/180D drawdown shows why launch concurrency alone cannot become Green.
C27 should cap this at Stage2-Guarded or local 4B watch until retention, ARPPU, live-ops, and margin evidence are repaired.
```

### 6.3 `112040` 위메이드 — blockchain-game IP / token event high-MFE high-MAE

Trigger:

```text
trigger_date = 2024-03-11
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = blockchain_game_ip_token_event_high_mfe_high_mae
entry_date = 2024-03-12
entry_price = 55000.0
entry_price_type = next_tradable_open_after_blockchain_game_ip_event_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-11,51900.0,55200.0,50800.0,55000.0,1722560.0,91821854900.0,1864388680000.0,33897976,KOSDAQ
2024-03-12,55000.0,61400.0,53900.0,60300.0,2477262.0,142851981900.0,2044047952800.0,33897976,KOSDAQ
2024-03-20,73500.0,80500.0,72700.0,76100.0,5081342.0,395267236300.0,2579635973600.0,33897976,KOSDAQ
2024-03-29,61300.0,61700.0,58100.0,60200.0,989207.0,59193306700.0,2040658155200.0,33897976,KOSDAQ
2024-04-15,48950.0,50100.0,48250.0,48400.0,816364.0,39971153650.0,1640662038400.0,33897976,KOSDAQ
2024-06-11,41300.0,41400.0,39900.0,40750.0,354047.0,14370760500.0,1383400682250.0,33948483,KOSDAQ
2024-08-05,36250.0,37100.0,32150.0,33150.0,383466.0,13190754550.0,1125392211450.0,33948483,KOSDAQ
2024-08-27,31100.0,31400.0,29200.0,30150.0,376742.0,11242689700.0,1023546762450.0,33948483,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 80500 | 2024-03-20 | 53700 | 2024-03-15 | +46.36% | -2.36% |
| 90 calendar days | 80500 | 2024-03-20 | 41800 | 2024-06-10 | +46.36% | -24.00% |
| 180 calendar days | 80500 | 2024-03-20 | 29200 | 2024-08-27 | +46.36% | -46.91% |

Interpretation:

```text
112040 is the event-MFE-overwhelmed counterexample.
The first-window upside was large, but the later drawdown was severe enough to block Yellow/Green without durable monetization evidence.
This is exactly the C27 case where token economics, user retention, real game revenue, and cash-flow bridge must be repaired before any positive-stage promotion.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R8L75_C27_GAME_IP_MONETIZATION_ROUTER","round":"R8","loop":75,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_LAUNCH_AND_BLOCKCHAIN_EVENT_HIGH_MAE_ROUTER","symbol":"259960","name":"크래프톤","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"global_game_ip_liveops_earnings_reacceleration_low_mae_rerating","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":219500.0,"entry_price_type":"next_tradable_open_after_game_ip_earnings_liveops_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.93,"mae_30d_pct":-4.1,"mfe_90d_pct":23.46,"mae_90d_pct":-4.1,"mfe_180d_pct":37.59,"mae_180d_pct":-4.1,"peak_price_180d":302000.0,"peak_date_180d":"2024-07-30","trough_price_180d":210500.0,"trough_date_180d":"2024-03-06","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_global_game_ip","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_liveops_revenue_margin_cashflow_bridge_repaired","residual_error_type":"positive_global_game_ip_path_requires_url_repaired_liveops_revenue_margin_and_new_title_pipeline_bridge_before_green"}
{"row_type":"trigger","research_id":"R8L75_C27_GAME_IP_MONETIZATION_ROUTER","round":"R8","loop":75,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_LAUNCH_AND_BLOCKCHAIN_EVENT_HIGH_MAE_ROUTER","symbol":"225570","name":"넥슨게임즈","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"new_game_launch_global_concurrency_high_mfe_later_drawdown","trigger_date":"2024-07-03","entry_date":"2024-07-04","entry_price":18700.0,"entry_price_type":"next_tradable_open_after_new_game_launch_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":61.5,"mae_30d_pct":-8.02,"mfe_90d_pct":65.51,"mae_90d_pct":-21.07,"mfe_180d_pct":65.51,"mae_180d_pct":-32.83,"peak_price_180d":30950.0,"peak_date_180d":"2024-08-09","trough_price_180d":12560.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_high_mfe_later_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_retention_monetization_margin_bridge_repaired","residual_error_type":"new_game_launch_had_large_mfe_but_later_high_mae_requires_retention_arppu_margin_bridge_before_yellow_green"}
{"row_type":"trigger","research_id":"R8L75_C27_GAME_IP_MONETIZATION_ROUTER","round":"R8","loop":75,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_LAUNCH_AND_BLOCKCHAIN_EVENT_HIGH_MAE_ROUTER","symbol":"112040","name":"위메이드","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"blockchain_game_ip_token_event_high_mfe_high_mae","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":55000.0,"entry_price_type":"next_tradable_open_after_blockchain_game_ip_event_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":46.36,"mae_30d_pct":-2.36,"mfe_90d_pct":46.36,"mae_90d_pct":-24.0,"mfe_180d_pct":46.36,"mae_180d_pct":-46.91,"peak_price_180d":80500.0,"peak_date_180d":"2024-03-20","trough_price_180d":29200.0,"trough_date_180d":"2024-08-27","calibration_usable":true,"case_polarity":"counterexample_event_mfe_overwhelmed_by_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_user_retention_token_economics_cashflow_bridge_repaired","residual_error_type":"blockchain_game_ip_event_created_large_mfe_but_mae_overwhelmed_without_durable_monetization_and_token_economics_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | IP strength | live-ops / retention | monetization / ARPPU | pipeline durability | market mispricing | margin / cash-flow bridge | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `259960` | 13 | 11 | 10 | 10 | 10 | 10 | 6 | 70 | Stage2-Guarded / Yellow after evidence repair |
| `225570` | 11 | 5 | 5 | 6 | 13 | 4 | 5 | 49 | Stage2-Guarded or local 4B watch |
| `112040` | 9 | 3 | 3 | 4 | 12 | 2 | 4 | 37 | Stage2-Guarded at most / 4B high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C27 issue is **content-IP event relevance without durable monetization conversion**:

```text
C27 durable game-IP path:
  global IP / live-ops relevance
  + MFE expands across 90D/180D
  + MAE remains contained
  + URL-repaired revenue, margin, and pipeline bridge
  => Stage2-Guarded / Yellow candidate, possible Green after proof

C27 launch-high-MFE later-MAE path:
  launch traffic or concurrency drives high MFE
  + MAE_90D <= -20% or MAE_180D <= -30%
  + retention / ARPPU / margin bridge remains source_proxy_only
  => Stage2-Guarded at most, local 4B watch, no Green

C27 blockchain/token event path:
  token or blockchain-game event drives MFE
  + 180D MAE <= -40%
  + token economics and real cash-flow bridge missing
  => 4B/high-MAE watch or blocked Stage2
```

`259960` prevents overblocking.  
`225570` shows why launch-window MFE is not the same as durable monetization.  
`112040` shows why event/token-linked content-IP rallies need a hard high-MAE guard.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R8L75_C27_GAME_IP_MONETIZATION_ROUTER",
  "round": "R8",
  "loop": 75,
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "fine_archetype_id": "GAME_IP_GLOBAL_LIVEOPS_LAUNCH_AND_BLOCKCHAIN_EVENT_HIGH_MAE_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 39.6,
  "avg_mae_30d_pct": -4.83,
  "avg_mfe_90d_pct": 45.11,
  "avg_mae_90d_pct": -16.39,
  "avg_mfe_180d_pct": 49.82,
  "avg_mae_180d_pct": -27.95,
  "max_mfe_180d_pct": 65.51,
  "worst_mae_180d_pct": -46.91
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R8L75_C27_GAME_IP_MONETIZATION_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "259960",
      "reason": "global game-IP path had +37.59% 180D MFE with only -4.10% MAE"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "225570",
      "reason": "new-title launch had +65.51% MFE but 180D MAE reached -32.83%; requires retention/ARPPU/margin bridge"
    }
  ],
  "blocked_stage2_or_4b_high_mae_watch": [
    {
      "symbol": "112040",
      "reason": "blockchain-game IP event had +46.36% MFE but 180D MAE reached -46.91%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "launch traffic and retention",
    "live-ops revenue and ARPPU",
    "payer conversion and regional mix",
    "new-title pipeline durability",
    "platform fees / marketing spend / margin bridge",
    "token economics and cash-flow bridge where relevant"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: GAME_IP_GLOBAL_LIVEOPS_LAUNCH_AND_BLOCKCHAIN_EVENT_HIGH_MAE_ROUTER
rule_name: C27_game_ip_liveops_launch_retention_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C27 game/content IP global monetization cases:

Tier A: verified durable game-IP monetization
  Conditions:
    - live-ops revenue, retention, monetization, margin, and pipeline evidence are URL-repaired
    - MFE_90D >= +20%
    - MAE_90D > -10%
    - MFE persists beyond one launch/event candle
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after retention / ARPPU / margin bridge is verified

Tier B: launch-window MFE with later high MAE
  Conditions:
    - MFE_30D >= +40%
    - MAE_90D <= -20% or MAE_180D <= -30%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - local 4B watch
    - no Green

Tier C: blockchain/token event high-MAE
  Conditions:
    - event/token thesis produces MFE
    - MAE_180D <= -40%
    - durable user monetization and token-economics bridge is missing
  Routing:
    - block Yellow/Green
    - local 4B/high-MAE watch or blocked Stage2
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c27_game_ip_liveops_launch_retention_and_high_mae_router",
  "scope": "canonical_archetype_id:C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "retention_arppu_margin_pipeline_bridge_required_for_green": true,
    "verified_game_ip_mfe90_threshold_pct": 20.0,
    "verified_game_ip_mae90_min_pct": -10.0,
    "launch_mfe30_threshold_pct": 40.0,
    "launch_later_mae90_threshold_pct": -20.0,
    "launch_later_hard_mae180_threshold_pct": -30.0,
    "blockchain_token_hard_mae180_threshold_pct": -40.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One durable low-MAE game-IP path and two high-MFE/high-MAE launch or token-event paths show that C27 should require URL-repaired retention, ARPPU, margin, pipeline, and token-economics evidence before Yellow/Green."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R8L75_C27_GAME_IP_MONETIZATION_ROUTER",
  "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY",
  "canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION",
  "contribution": "Adds three non-top-covered C27 game/content IP monetization cases and separates durable global game-IP live-ops rerating from launch-window and blockchain/token event high-MAE paths. C27 Yellow/Green should require URL-repaired retention, live-ops revenue, ARPPU, payer conversion, regional mix, pipeline durability, platform-fee/marketing-cost control, margin, and token-economics evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "current_profile_error_count": 2,
  "diversity_score_summary": {
    "new_symbol_bonus": 9,
    "counterexample_gap_bonus": 4,
    "residual_error_bonus": 10,
    "wrong_round_penalty": 0,
    "repeated_same_symbol_penalty": 0,
    "net_interpretive_score": 23
  },
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "data_quality_blocker": "All three non-price game/content-IP triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C27 source_proxy_only launch-window cases with MFE_30D >= +40% but MAE_90D <= -20% or MAE_180D <= -30% should cap at Stage2-Guarded; blockchain/token event cases with MAE_180D <= -40% should block Yellow/Green until monetization evidence is repaired."
}
```

One-line contribution:

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.
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
    112040: false
  evidence_url_pending:
    259960: true
    225570: true
    112040: true
  source_proxy_only:
    259960: true
    225570: true
    112040: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C27 game/content-IP monetization residual shape and high-MAE launch/event guardrail design, but should not promote positive weights until filings, IR, app-market data, Steam/console metrics, or reports verify retention, live-ops revenue, ARPPU, payer conversion, regional mix, pipeline, platform fees, marketing cost, margin, and token economics.
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
2. Preserve R8 / loop 75 metadata.
3. Add the cases to C27_CONTENT_IP_GLOBAL_MONETIZATION only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/app-market/Steam-console/report data verifies retention, live-ops revenue, ARPPU, payer conversion, regional mix, pipeline durability, platform fees, marketing cost, margin, and token economics where relevant.
6. Add a shadow-only rule candidate named C27_game_ip_liveops_launch_retention_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C27-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired retention / ARPPU / margin / pipeline bridge
   - MFE_90D >= +20% and MAE_90D > -10% may remain Stage2-Guarded / Yellow watch after evidence repair
   - launch-window MFE_30D >= +40% with MAE_90D <= -20% or MAE_180D <= -30% -> Stage2-Guarded at most / local 4B watch
   - blockchain/token event with MAE_180D <= -40% -> block Yellow/Green and route to 4B/high-MAE watch unless token-economics and cash-flow bridge is repaired
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R8
completed_loop = 75
next_round = R9
next_loop = 75
next_large_sector_hint = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING
round_schedule_status = valid
round_sector_consistency = pass
```
