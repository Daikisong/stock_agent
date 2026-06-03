# E2R Stock-Web v12 Residual Research — R11 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R11
completed_loop: 73
next_round: R12
next_loop: 73
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_POLICY_FRAMEWORK_SECOND_TIER_BACKLOG_AND_GEOPOLITICAL_THEME_ROUTER
output_file: e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
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
completed_round = R10
completed_loop  = 73
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Therefore:

```text
scheduled_round = R11
scheduled_loop  = 73
```

R11 permits either:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
or
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID when the case is defense/policy-linked
```

This run selects the L1 defense-linked branch:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_EXPORT_POLICY_FRAMEWORK_SECOND_TIER_BACKLOG_AND_GEOPOLITICAL_THEME_ROUTER
```

This is a valid R11 pairing.

---

## 1. Why this R11/C03 run

The no-repeat ledger shows C03 is already covered, but concentrated in major defense exporters and high-repeat names:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG:
  rows: 74
  symbols: 14
  date_range: 2022-01-17~2024-11-12
  good/bad S2: 30/7
  4B/4C: 20/1
  URL/proxy: 0/0
  top covered symbols: 064350(19), 272210(9), UNKNOWN_SYMBOL(9), 012450(8), 047810(5), 079550(5)
```

This run avoids the top-covered prime-contractors and tests second-tier / adjacent defense names:

```text
103140 풍산
003570 SNT다이내믹스
065450 빅텍
```

Research question:

```text
Can C03 separate true defense-export / backlog / munitions-capacity rerating from geopolitical theme spikes whose first candle is not supported by export framework, backlog conversion, or margin evidence?
```

C03 should behave like an export-contract filter, not a war-headline amplifier. The market often lights up anything that smells like defense when geopolitical tension rises. But durable Stage2/Yellow should come from contract framework, delivery schedule, backlog, production capacity, and margin conversion. A siren can be loud without becoming revenue.

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
| `103140` | 풍산 | active_like / KOSPI | none listed | true |
| `003570` | SNT다이내믹스 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2006-04-05 | true |
| `065450` | 빅텍 | active_like / KOSDAQ | no 2024 overlap; latest listed candidate 2009-11-24 | true |

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
The Stock-Web price path is fully validated, but company-level defense export contract, framework agreement, delivery schedule, order backlog, ammunition/vehicle powertrain capacity, customer country, and margin bridge evidence still require later URL repair through filings, IR decks, defense procurement releases, company disclosures, or sell-side reports before production weight promotion.
```

C03 interpretation used here:

```text
C03 is not simply “defense stock rose.”
It asks whether geopolitical and policy relevance converts into:
- export framework or firm contract,
- delivery schedule,
- order backlog conversion,
- production-capacity or munitions scarcity,
- customer/country quality,
- and margin conversion.
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
103140 + C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG -> no direct match found
003570 + C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG -> no direct match found
065450 + C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R11L73_C03_003570_20240202` | `003570` SNT다이내믹스 | defense vehicle powertrain / export-backlog second-tier rerating | positive anchor |
| `R11L73_C03_103140_20240415` | `103140` 풍산 | munitions / defense material export-capacity rerating | positive-guarded, later high-MAE watch |
| `R11L73_C03_065450_20240118` | `065450` 빅텍 | geopolitical defense theme spike without export framework bridge | counterexample / 4B local watch |

The intended residual:

```text
C03 should separate:
1. defense-adjacent capacity/backlog rerating with persistent MFE and contained MAE;
2. munitions/material defense rerating that works initially but needs backlog/margin proof before Green;
3. geopolitical theme spikes where the entry comes after the alarm bell and the remaining return/risk is poor.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `003570` SNT다이내믹스 — defense powertrain / export-backlog positive anchor

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable
trigger_family = defense_vehicle_powertrain_export_backlog_rerating
entry_date = 2024-02-02
entry_price = 15950.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,14610.0,15640.0,14520.0,15540.0,457334.0,7050167950.0,516746911380.0,33252697,KOSPI
2024-02-02,15950.0,17000.0,15270.0,15580.0,454584.0,7311641770.0,518077019260.0,33252697,KOSPI
2024-02-29,18350.0,19240.0,18320.0,18670.0,163052.0,3070318210.0,620827852990.0,33252697,KOSPI
2024-03-29,16720.0,19950.0,16680.0,17420.0,1766919.0,32659071220.0,579261981740.0,33252697,KOSPI
2024-06-28,21900.0,22450.0,21600.0,22450.0,67130.0,1473961900.0,746523047650.0,33252697,KOSPI
2024-07-26,20800.0,26750.0,20650.0,21150.0,1678210.0,39069562200.0,703294541550.0,33252697,KOSPI
2024-08-05,22000.0,22500.0,18600.0,19870.0,309407.0,6373367850.0,660731089390.0,33252697,KOSPI
2024-09-20,22300.0,26000.0,21800.0,25750.0,1527973.0,38024599350.0,856256947750.0,33252697,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 19240 | 2024-02-29 | 15100 | 2024-02-06 | +20.63% | -5.33% |
| 90 calendar days | 19950 | 2024-03-29 | 15100 | 2024-02-06 | +25.08% | -5.33% |
| 180 calendar days | 26750 | 2024-07-26 | 15100 | 2024-02-06 | +67.71% | -5.33% |

Interpretation:

```text
003570 is the clean C03 positive anchor in this run.
It has persistent MFE, contained MAE, and a second-tier defense powertrain/backlog profile.
Even here, Green still requires URL-repaired export/order/backlog/margin evidence, but the price path supports Stage2-Actionable / Yellow consideration.
```

### 6.2 `103140` 풍산 — munitions / defense material rerating, but later high-MAE watch

Trigger:

```text
trigger_date = 2024-04-12
trigger_type = Stage2-Actionable-Guarded
trigger_family = munitions_defense_material_export_capacity_rerating
entry_date = 2024-04-15
entry_price = 63400.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-12,60200.0,67500.0,59600.0,61600.0,2301877.0,145094424100.0,1726295524800.0,28024278,KOSPI
2024-04-15,63400.0,65400.0,59300.0,60300.0,1072650.0,66125959500.0,1689863963400.0,28024278,KOSPI
2024-04-16,59400.0,61200.0,56800.0,58500.0,705582.0,41570667200.0,1639420263000.0,28024278,KOSPI
2024-05-02,67500.0,75000.0,67000.0,72700.0,2814129.0,202221190900.0,2037365010600.0,28024278,KOSPI
2024-05-14,78100.0,78900.0,75600.0,76300.0,625384.0,48386189700.0,2138252411400.0,28024278,KOSPI
2024-06-10,56500.0,57700.0,55600.0,57600.0,431470.0,24457483000.0,1614198412800.0,28024278,KOSPI
2024-08-05,53300.0,54100.0,47000.0,49400.0,499656.0,25562625600.0,1384399333200.0,28024278,KOSPI
2024-10-07,67300.0,68700.0,66300.0,67800.0,602246.0,40797246400.0,1900046048400.0,28024278,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 78900 | 2024-05-14 | 56800 | 2024-04-16 | +24.45% | -10.41% |
| 90 calendar days | 78900 | 2024-05-14 | 55600 | 2024-06-10 | +24.45% | -12.30% |
| 180 calendar days | 78900 | 2024-05-14 | 47000 | 2024-08-05 | +24.45% | -25.87% |

Interpretation:

```text
103140 is a positive-guarded C03 case.
The 30D/90D route was usable, but 180D MAE crossed the -25% guardrail.
This should not be automatic Green. It needs URL-repaired munitions/export capacity, customer, delivery, and margin bridge evidence.
```

### 6.3 `065450` 빅텍 — geopolitical defense theme spike without export framework bridge

Trigger:

```text
trigger_date = 2024-01-17
trigger_type = 4B-local-watch
trigger_family = geopolitical_defense_theme_spike_without_export_framework_bridge
entry_date = 2024-01-18
entry_price = 6600.0
entry_price_type = next_tradable_open_after_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-16,5140.0,6140.0,4940.0,5660.0,51615567.0,293582947335.0,162174848000.0,28652800,KOSDAQ
2024-01-17,5800.0,7230.0,5660.0,6900.0,105257194.0,692199610630.0,197704320000.0,28652800,KOSDAQ
2024-01-18,6600.0,7070.0,6080.0,6140.0,34390877.0,222536880970.0,175928192000.0,28652800,KOSDAQ
2024-01-25,5120.0,5230.0,4880.0,4905.0,2732391.0,13696653405.0,140541984000.0,28652800,KOSDAQ
2024-02-16,5320.0,5680.0,5260.0,5480.0,5136557.0,28236940220.0,157017344000.0,28652800,KOSDAQ
2024-03-29,4825.0,4850.0,4720.0,4770.0,620305.0,2965124880.0,136673856000.0,28652800,KOSDAQ
2024-07-11,4880.0,4910.0,4700.0,4805.0,741214.0,3562558280.0,137676704000.0,28652800,KOSDAQ
2024-08-05,5250.0,5490.0,4510.0,4890.0,16470185.0,85941263400.0,140112192000.0,28652800,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7070 | 2024-01-18 | 4880 | 2024-01-25 | +7.12% | -26.06% |
| 90 calendar days | 7070 | 2024-01-18 | 4720 | 2024-03-29 | +7.12% | -28.48% |
| 180 calendar days | 7070 | 2024-01-18 | 4700 | 2024-07-11 | +7.12% | -28.79% |

Interpretation:

```text
065450 is the clean C03 counterexample.
It moved on defense/geopolitical tension, but after the event-day spike the remaining upside was small and MAE was immediately severe.
This should route to local 4B/high-MAE watch and should not become Stage2/Green without a real export framework or backlog bridge.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R11L73_C03_DEFENSE_EXPORT_ROUTER","round":"R11","loop":73,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_POLICY_FRAMEWORK_SECOND_TIER_BACKLOG_AND_GEOPOLITICAL_THEME_ROUTER","symbol":"003570","name":"SNT다이내믹스","trigger_type":"Stage2-Actionable","trigger_family":"defense_vehicle_powertrain_export_backlog_rerating","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":15950.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":20.63,"mae_30d_pct":-5.33,"mfe_90d_pct":25.08,"mae_90d_pct":-5.33,"mfe_180d_pct":67.71,"mae_180d_pct":-5.33,"peak_price_180d":26750.0,"peak_date_180d":"2024-07-26","trough_price_180d":15100.0,"trough_date_180d":"2024-02-06","calibration_usable":true,"case_polarity":"positive_anchor","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_export_backlog_delivery_margin_bridge_repaired","residual_error_type":"positive_anchor_requires_url_repaired_defense_backlog_export_margin_bridge_before_green"}
{"row_type":"trigger","research_id":"R11L73_C03_DEFENSE_EXPORT_ROUTER","round":"R11","loop":73,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_POLICY_FRAMEWORK_SECOND_TIER_BACKLOG_AND_GEOPOLITICAL_THEME_ROUTER","symbol":"103140","name":"풍산","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"munitions_defense_material_export_capacity_rerating","trigger_date":"2024-04-12","entry_date":"2024-04-15","entry_price":63400.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":24.45,"mae_30d_pct":-10.41,"mfe_90d_pct":24.45,"mae_90d_pct":-12.30,"mfe_180d_pct":24.45,"mae_180d_pct":-25.87,"peak_price_180d":78900.0,"peak_date_180d":"2024-05-14","trough_price_180d":47000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_high_mae_later","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_munitions_export_capacity_margin_bridge_repaired","residual_error_type":"munitions_capacity_rerating_worked_initially_but_180d_mae_blocks_green_without_bridge"}
{"row_type":"trigger","research_id":"R11L73_C03_DEFENSE_EXPORT_ROUTER","round":"R11","loop":73,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_POLICY_FRAMEWORK_SECOND_TIER_BACKLOG_AND_GEOPOLITICAL_THEME_ROUTER","symbol":"065450","name":"빅텍","trigger_type":"4B-local-watch","trigger_family":"geopolitical_defense_theme_spike_without_export_framework_bridge","trigger_date":"2024-01-17","entry_date":"2024-01-18","entry_price":6600.0,"entry_price_type":"next_tradable_open_after_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.12,"mae_30d_pct":-26.06,"mfe_90d_pct":7.12,"mae_90d_pct":-28.48,"mfe_180d_pct":7.12,"mae_180d_pct":-28.79,"peak_price_180d":7070.0,"peak_date_180d":"2024-01-18","trough_price_180d":4700.0,"trough_date_180d":"2024-07-11","calibration_usable":true,"case_polarity":"counterexample_geopolitical_theme_spike","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"4B_local_watch_or_blocked_positive_stage","residual_error_type":"geopolitical_theme_spike_low_mfe_high_mae_without_export_framework_backlog_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | export framework / contract | backlog / delivery visibility | capacity / scarcity bridge | market mispricing | valuation rerating | margin conversion | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `003570` | 12 | 13 | 11 | 12 | 13 | 9 | 7 | 77 | Stage2/Yellow after export-backlog evidence repair |
| `103140` | 10 | 9 | 13 | 12 | 10 | 7 | 6 | 67 | Stage2-Guarded; no Green until munitions/export bridge repair |
| `065450` | 3 | 2 | 4 | 8 | 5 | 2 | 4 | 28 | local 4B/high-MAE watch; blocked Stage2/Green |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C03 risk is **headline defense relevance without backlog conversion**:

```text
C03 clean path:
  defense export/backlog relevance
  + persistent MFE
  + contained MAE
  + URL-repaired contract/delivery/margin evidence
  => Stage2-Actionable / Yellow, possible Green after proof

C03 positive-guarded path:
  defense material or munitions scarcity relevance
  + initial MFE
  + later 180D MAE <= -25%
  + bridge still source_proxy_only
  => Stage2-Guarded; no Green

C03 geopolitical-theme false-positive:
  defense/geopolitical spike
  + peak occurs immediately at or after entry
  + MFE_30D < +10%
  + MAE_30D <= -20%
  + no export framework/backlog evidence
  => local 4B/high-MAE watch or blocked positive stage
```

`003570` prevents overblocking because its path remained aligned.  
`103140` shows a valid but guarded defense material route.  
`065450` is the reminder that a siren is not a backlog.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R11L73_C03_DEFENSE_EXPORT_ROUTER",
  "round": "R11",
  "loop": 73,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "fine_archetype_id": "DEFENSE_EXPORT_POLICY_FRAMEWORK_SECOND_TIER_BACKLOG_AND_GEOPOLITICAL_THEME_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 17.40,
  "avg_mae_30d_pct": -13.93,
  "avg_mfe_90d_pct": 18.88,
  "avg_mae_90d_pct": -15.37,
  "avg_mfe_180d_pct": 33.09,
  "avg_mae_180d_pct": -20.00,
  "max_mfe_180d_pct": 67.71,
  "worst_mae_180d_pct": -28.79
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R11L73_C03_DEFENSE_EXPORT_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "003570",
      "reason": "persistent 180D MFE of +67.71% with only -5.33% MAE; requires URL-repaired export/backlog/delivery/margin bridge before Green"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "103140",
      "reason": "defense material / munitions route worked initially, but 180D MAE reached -25.87%; requires munitions capacity/export bridge repair"
    }
  ],
  "blocked_stage2_or_theme_spike": [
    {
      "symbol": "065450",
      "reason": "geopolitical spike had only +7.12% MFE and -26.06% 30D MAE; no export-framework bridge"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "defense export framework or firm contract",
    "delivery schedule / backlog conversion",
    "customer country and procurement quality",
    "production capacity or munitions scarcity evidence",
    "gross margin / operating margin conversion"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_POLICY_FRAMEWORK_SECOND_TIER_BACKLOG_AND_GEOPOLITICAL_THEME_ROUTER
rule_name: C03_defense_export_backlog_vs_geopolitical_theme_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C03 defense export / backlog cases:

Tier A: verified export/backlog defense winner
  Conditions:
    - export framework, firm contract, customer country, or delivery schedule evidence is URL-repaired
    - 30D/90D MAE is contained
    - MFE persists beyond a single event candle
    - margin conversion is visible or later confirmed
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after backlog and margin bridge are verified

Tier B: defense material / munitions positive-guarded path
  Conditions:
    - capacity or scarcity relevance is plausible
    - price path has MFE
    - 180D MAE crosses -25%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Actionable-Guarded at most
    - local 4B watch if drawdown expands
    - no Green

Tier C: geopolitical theme spike without export framework
  Conditions:
    - MFE_30D < +10%
    - MAE_30D <= -20%
    - peak occurs on entry day or immediately after entry
    - no contract/backlog bridge
  Routing:
    - block Stage2
    - route to local 4B/high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c03_defense_export_backlog_vs_geopolitical_theme_router",
  "scope": "canonical_archetype_id:C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "export_backlog_delivery_margin_bridge_required_for_green": true,
    "defense_material_high_mae_stage2_cap": "guarded_only_until_url_repair",
    "geopolitical_theme_weak_mfe_threshold_30d_pct": 10.0,
    "geopolitical_theme_high_mae_threshold_30d_pct": -20.0,
    "same_window_theme_peak_blocks_stage2": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two defense/backlog-positive paths and one geopolitical-theme counterexample show that C03 should reward persistent low-MAE defense export/backlog paths, but block weak-MFE theme spikes without contract or delivery evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R11L73_C03_DEFENSE_EXPORT_ROUTER",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "contribution": "Adds three non-top-covered C03 defense/export/backlog cases and separates a clean second-tier defense powertrain rerating from a guarded munitions/material path and a geopolitical theme spike counterexample. C03 Green should require URL-repaired export framework, backlog, delivery schedule, customer, and margin evidence.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price defense/export triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C03 geopolitical theme spikes with MFE_30D < +10% and MAE_30D <= -20% should block Stage2 or route to local 4B/high-MAE watch; defense material paths with 180D MAE worse than -25% should cap at Stage2-Guarded until evidence repair."
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
    003570: false
    103140: false
    065450: false
  evidence_url_pending:
    003570: true
    103140: true
    065450: true
  source_proxy_only:
    003570: true
    103140: true
    065450: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C03 defense export / backlog residual shape and geopolitical-theme high-MAE guardrail design, but should not promote positive weights until filings, IR, procurement releases, defense-contract disclosures, or reports verify export framework, backlog, delivery schedule, customer quality, capacity, and margin conversion.
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
2. Preserve R11 / loop 73 metadata.
3. Add the cases to C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/procurement-release/defense-contract/report data verifies export framework, backlog, delivery schedule, customer country, production capacity, and margin conversion.
6. Add a shadow-only rule candidate named C03_defense_export_backlog_vs_geopolitical_theme_router.
7. Do not loosen Stage3-Green.
8. Add C03-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired export/backlog/delivery/margin bridge
   - defense material path with 180D MAE <= -25% -> Stage2-Guarded at most until evidence repair
   - geopolitical theme spike with MFE_30D < +10% and MAE_30D <= -20% -> block Stage2 or local 4B/high-MAE watch
   - same-window theme peak without contract evidence -> no Stage2/Green promotion
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R11
completed_loop = 73
next_round = R12
next_loop = 73
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```
