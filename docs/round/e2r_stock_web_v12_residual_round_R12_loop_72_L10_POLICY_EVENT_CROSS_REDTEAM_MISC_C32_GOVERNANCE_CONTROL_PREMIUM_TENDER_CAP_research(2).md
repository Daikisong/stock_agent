# E2R Stock-Web v12 Residual Research — R12 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R12
completed_loop: 72
next_round: R13
next_loop: 72
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD
output_file: e2r_stock_web_v12_residual_round_R12_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
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

The active prompt fixes the research mode:

```text
primary_price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap

production_scoring_changed = false
shadow_weight_only = true
must_use_actual_stock_web_1D_OHLC = true
must_include_backtest_result = true
must_include_current_calibrated_profile_stress_test = true
must_output_every_usable_trigger_as_jsonl = true
```

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R11
completed_loop  = 72
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Therefore:

```text
scheduled_round = R12
scheduled_loop  = 72
```

R12 permits:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
or
under-covered service/agri/event sector
```

This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD
```

This is a valid R12 pairing.

---

## 1. Why this R12/C32 run

The no-repeat ledger shows C32 is already broad and active, but top coverage is concentrated in other governance/control-premium cases:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:
  rows: 122
  symbols: 20
  date_range: 2020-11-16~2024-12-06
  good/bad S2: 45/23
  4B/4C: 35/11
  URL/proxy: 0/0
  top covered symbols: 010130(31), 041510(26), 011200(11), 008930(9), UNKNOWN_SYMBOL(8), 000240(5)
```

The previous R12 C32 artifact in loop 71 tested a contested tender/control-premium case.  
This run deliberately uses a different C32 subtype:

```text
fine_archetype_id = DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD
```

The target event cluster is the July 2024 Doosan group restructuring / merger / spin-off plan involving Doosan, Doosan Robotics, Doosan Bobcat, and Doosan Enerbility. It is not a tender-offer cap case. It is a governance-restructuring / exchange-ratio / minority-holder fairness case. It belongs in C32 because the market was not pricing an operating earnings revision first; it was pricing a control-structure decision and the redistribution of value across related listed entities.

Research question:

```text
Can C32 prevent a governance-restructuring event from being misread as Stage2/Green when the first-day MFE is followed by severe MAE across the group structure?
```

This is the opposite of a clean “control premium” setup. The first candle gives the appearance of a new value map; the next weeks reveal whether the map is a bridge or a maze.

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
| `000150` | 두산 | active_like / KOSPI | no 2024 overlap; old 1997~1999 candidates only | true |
| `454910` | 두산로보틱스 | active_like / KOSPI | none listed | true |
| `241560` | 두산밥캣 | active_like / KOSPI | none listed | true |
| `034020` | 두산에너빌리티 | active_like / KOSPI | no 2024 overlap; old 2019/2020 candidates only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Evidence event and trigger discipline

### Event family

```text
event_family = Doosan group restructuring / merger / split-off / exchange-ratio controversy
trigger_date = 2024-07-11
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-07-12
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD
```

This event is treated as a C32 governance/restructuring shock, not as a normal earnings revision. The core mechanism is:

```text
group-level control restructuring
  -> listed-entity value redistribution
  -> exchange-ratio / minority-holder fairness question
  -> regulatory / shareholder pushback risk
  -> 4B/4C timing problem
```

This artifact intentionally marks non-price evidence as conservative:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but URL-level evidence for the formal restructuring filing, exchange ratio, board approvals, shareholder fairness debate, regulatory review, later revisions, and final implementation status still requires later URL repair through filings, DART, exchange disclosure, company IR, or news source archiving before production weight promotion.
```

C32 interpretation used here:

```text
C32 should not treat governance restructuring as automatic value creation.
A restructuring can move value between pockets inside the same coat. The model has to ask whose pocket receives value, whose pocket loses optionality, and whether minority-holder fairness or regulatory risk changes the path.
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
000150 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP -> no direct match found
454910 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP -> no direct match found
241560 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP -> no direct match found
034020 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "guardrail_positive_case_count": 1,
  "counterexample_count": 3,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R12L72_C32_000150_20240712` | `000150` 두산 | parent-control vehicle restructuring squeeze | guardrail-positive / full-window recovery but extreme early MAE |
| `R12L72_C32_454910_20240712` | `454910` 두산로보틱스 | high-valuation beneficiary narrative | counterexample / first-day MFE then severe MAE |
| `R12L72_C32_241560_20240712` | `241560` 두산밥캣 | target / value-transfer fairness controversy | counterexample / exchange-ratio minority-holder risk |
| `R12L72_C32_034020_20240712` | `034020` 두산에너빌리티 | split/holder-side restructuring exposure | counterexample / event-volatility high MAE |

The intended residual:

```text
C32 should treat group restructuring as a tiered governance event:
- parent/control vehicle can recover later, but early high MAE still blocks Green at the event trigger;
- beneficiary narrative can spike, but valuation and fairness risk can quickly reverse it;
- target or transfer vehicle can suffer direct value-transfer drawdown;
- split/holder-side listed entity needs the exchange-ratio and final implementation bridge before positive staging.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `000150` 두산 — parent-control vehicle with later recovery but extreme initial MAE

Trigger:

```text
trigger_date = 2024-07-11
trigger_type = 4B-local-watch
trigger_family = parent_control_vehicle_restructuring_squeeze
entry_date = 2024-07-12
entry_price = 263500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,235000.0,246000.0,232000.0,241500.0,154313.0,37454287500.0,3990506152500.0,16523835,KOSPI
2024-07-12,263500.0,263500.0,221000.0,237000.0,626925.0,150539605500.0,3916148895000.0,16523835,KOSPI
2024-07-25,184000.0,184000.0,170800.0,172000.0,331864.0,58245662200.0,2842099620000.0,16523835,KOSPI
2024-08-05,142200.0,143000.0,122000.0,128100.0,502710.0,66626020800.0,2116703263500.0,16523835,KOSPI
2024-09-20,164900.0,171300.0,163600.0,164900.0,122190.0,20397207800.0,2724780391500.0,16523835,KOSPI
2025-01-03,265000.0,293500.0,259000.0,289500.0,243799.0,68032264500.0,4783650232500.0,16523835,KOSPI
2025-01-07,299000.0,304500.0,288500.0,296500.0,93470.0,27575119000.0,4899317077500.0,16523835,KOSPI
2025-01-08,291500.0,297000.0,288500.0,292000.0,112394.0,32801938500.0,4824959820000.0,16523835,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 263500 | 2024-07-12 | 122000 | 2024-08-05 | +0.00% | -53.70% |
| 90 calendar days | 263500 | 2024-07-12 | 122000 | 2024-08-05 | +0.00% | -53.70% |
| 180 calendar days | 304500 | 2025-01-07 | 122000 | 2024-08-05 | +15.56% | -53.70% |

Interpretation:

```text
000150 is a guardrail-positive C32 case.
It recovered later, but the event trigger itself was a terrible Stage2/Green entry because the next month carried more than -50% MAE.
This teaches the model to split local 4B/restructuring squeeze from full-window recovery.
```

### 6.2 `454910` 두산로보틱스 — beneficiary narrative spike that failed quickly

Trigger:

```text
trigger_date = 2024-07-11
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = high_valuation_beneficiary_restructuring_narrative
entry_date = 2024-07-12
entry_price = 95000.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,81500.0,86200.0,81100.0,85300.0,2032864.0,171787964200.0,5529144294000.0,64819980,KOSPI
2024-07-12,95000.0,109300.0,92200.0,105700.0,15292160.0,1552990227300.0,6851471886000.0,64819980,KOSPI
2024-07-22,83400.0,83500.0,79700.0,79700.0,910491.0,73354471000.0,5166152406000.0,64819980,KOSPI
2024-07-25,75100.0,76400.0,72700.0,73400.0,1575540.0,116703314700.0,4757786532000.0,64819980,KOSPI
2024-08-05,66600.0,66700.0,53900.0,59300.0,919934.0,57094799600.0,3843824814000.0,64819980,KOSPI
2024-08-29,65000.0,73600.0,64900.0,69300.0,1359963.0,95883580400.0,4492024614000.0,64819980,KOSPI
2025-01-02,56600.0,67800.0,56200.0,67000.0,4171511.0,264594735400.0,4342938660000.0,64819980,KOSPI
2025-01-08,64900.0,65500.0,62600.0,63000.0,639841.0,40775828300.0,4083658740000.0,64819980,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 109300 | 2024-07-12 | 53900 | 2024-08-05 | +15.05% | -43.26% |
| 90 calendar days | 109300 | 2024-07-12 | 53900 | 2024-08-05 | +15.05% | -43.26% |
| 180 calendar days | 109300 | 2024-07-12 | 53900 | 2024-08-05 | +15.05% | -43.26% |

Interpretation:

```text
454910 is the clean high-valuation beneficiary counterexample.
A one-day governance narrative created MFE, but the same window quickly delivered much larger downside.
This should never be Stage3-Green without a final approved structure and a verified earnings/cash-flow bridge.
```

### 6.3 `241560` 두산밥캣 — transfer target / minority-holder fairness risk

Trigger:

```text
trigger_date = 2024-07-11
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = restructuring_target_exchange_ratio_minorityholder_risk
entry_date = 2024-07-12
entry_price = 51500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,51500.0,52000.0,50500.0,52000.0,252359.0,12966110100.0,5212956632000.0,100249166,KOSPI
2024-07-12,51500.0,59500.0,49850.0,54600.0,6789108.0,366749381750.0,5473604463600.0,100249166,KOSPI
2024-07-25,47000.0,47950.0,41150.0,44150.0,1981380.0,86261552550.0,4426000678900.0,100249166,KOSPI
2024-08-05,38400.0,38700.0,33350.0,34250.0,813194.0,29212468650.0,3433533935500.0,100249166,KOSPI
2024-08-29,43250.0,45950.0,40050.0,42050.0,2948285.0,125679147650.0,4215477430300.0,100249166,KOSPI
2024-09-20,42150.0,42900.0,41000.0,42550.0,896967.0,37972539100.0,4265602013300.0,100249166,KOSPI
2025-01-08,41600.0,42350.0,41500.0,42000.0,614640.0,25834673900.0,4210464972000.0,100249166,KOSPI
2025-01-24,49550.0,53400.0,48900.0,52500.0,778621.0,39897620100.0,5263081215000.0,100249166,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 59500 | 2024-07-12 | 33350 | 2024-08-05 | +15.53% | -35.24% |
| 90 calendar days | 59500 | 2024-07-12 | 33350 | 2024-08-05 | +15.53% | -35.24% |
| 180 calendar days | 59500 | 2024-07-12 | 33350 | 2024-08-05 | +15.53% | -35.24% |

Interpretation:

```text
241560 is the minority-holder fairness counterexample.
The first-day MFE looks tempting, but the value-transfer controversy and exchange-ratio uncertainty are exactly the non-price risks that should cap Stage2 and block Green.
```

### 6.4 `034020` 두산에너빌리티 — split/holder-side restructuring exposure

Trigger:

```text
trigger_date = 2024-07-11
trigger_type = Stage2-Actionable-Guarded
trigger_family = split_holder_side_restructuring_exposure
entry_date = 2024-07-12
entry_price = 20800.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,21850.0,22150.0,21400.0,21850.0,9593927.0,209256696850.0,13996261040100.0,640561146,KOSPI
2024-07-12,20800.0,21700.0,19970.0,20900.0,25828467.0,536557704100.0,13387727951400.0,640561146,KOSPI
2024-07-18,23850.0,25000.0,20900.0,21000.0,63401772.0,1430000978200.0,13451784066000.0,640561146,KOSPI
2024-07-25,19750.0,20200.0,18910.0,18930.0,9151927.0,176652240510.0,12125822493780.0,640561146,KOSPI
2024-08-05,17280.0,17290.0,15150.0,15860.0,8528030.0,140762396920.0,10159299775560.0,640561146,KOSPI
2024-08-29,18420.0,18450.0,17660.0,17750.0,4748040.0,84970799080.0,11369960341500.0,640561146,KOSPI
2025-01-08,18690.0,18900.0,18370.0,18900.0,3834048.0,71439399070.0,12106605659400.0,640561146,KOSPI
2025-01-17,21500.0,22000.0,21150.0,21750.0,13756111.0,296277738600.0,13932204925500.0,640561146,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 25000 | 2024-07-18 | 15150 | 2024-08-05 | +20.19% | -27.16% |
| 90 calendar days | 25000 | 2024-07-18 | 15150 | 2024-08-05 | +20.19% | -27.16% |
| 180 calendar days | 25000 | 2024-07-18 | 15150 | 2024-08-05 | +20.19% | -27.16% |

Interpretation:

```text
034020 is the least severe of the initial restructuring cases, but the -27% MAE is still too large for unqualified positive staging.
It may remain Stage2-Actionable-Guarded only if the final structure and holder-side economics are URL-repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R12L72_C32_DOOSAN_RESTRUCTURING_GUARD","round":"R12","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD","symbol":"000150","name":"두산","trigger_type":"4B-local-watch","trigger_family":"parent_control_vehicle_restructuring_squeeze","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":263500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.00,"mae_30d_pct":-53.70,"mfe_90d_pct":0.00,"mae_90d_pct":-53.70,"mfe_180d_pct":15.56,"mae_180d_pct":-53.70,"peak_price_180d":304500.0,"peak_date_180d":"2025-01-07","trough_price_180d":122000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"guardrail_positive","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"4B_local_watch_then_recheck_after_final_restructuring_economics","residual_error_type":"parent_control_vehicle_later_recovery_does_not_validate_event_trigger_green"}
{"row_type":"trigger","research_id":"R12L72_C32_DOOSAN_RESTRUCTURING_GUARD","round":"R12","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD","symbol":"454910","name":"두산로보틱스","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"high_valuation_beneficiary_restructuring_narrative","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":95000.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.05,"mae_30d_pct":-43.26,"mfe_90d_pct":15.05,"mae_90d_pct":-43.26,"mfe_180d_pct":15.05,"mae_180d_pct":-43.26,"peak_price_180d":109300.0,"peak_date_180d":"2024-07-12","trough_price_180d":53900.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"beneficiary_narrative_first_day_mfe_was_overwhelmed_by_high_mae"}
{"row_type":"trigger","research_id":"R12L72_C32_DOOSAN_RESTRUCTURING_GUARD","round":"R12","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD","symbol":"241560","name":"두산밥캣","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"restructuring_target_exchange_ratio_minorityholder_risk","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":51500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.53,"mae_30d_pct":-35.24,"mfe_90d_pct":15.53,"mae_90d_pct":-35.24,"mfe_180d_pct":15.53,"mae_180d_pct":-35.24,"peak_price_180d":59500.0,"peak_date_180d":"2024-07-12","trough_price_180d":33350.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_exchange_ratio_fairness","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"minorityholder_exchange_ratio_risk_should_block_positive_stage"}
{"row_type":"trigger","research_id":"R12L72_C32_DOOSAN_RESTRUCTURING_GUARD","round":"R12","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"split_holder_side_restructuring_exposure","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":20800.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":20.19,"mae_30d_pct":-27.16,"mfe_90d_pct":20.19,"mae_90d_pct":-27.16,"mfe_180d_pct":20.19,"mae_180d_pct":-27.16,"peak_price_180d":25000.0,"peak_date_180d":"2024-07-18","trough_price_180d":15150.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2_Guarded_or_4B_watch_until_final_structure_verified","residual_error_type":"holder_side_restructuring_mfe_does_not_clear_high_mae_gate"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | governance event relevance | exchange-ratio / fairness clarity | beneficiary economics | market mispricing | valuation rerating | regulatory/shareholder risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `000150` | 15 | 6 | 9 | 11 | 10 | 3 | 5 | 59 | local 4B watch; later recovery does not validate event Green |
| `454910` | 14 | 4 | 8 | 12 | 12 | 2 | 4 | 56 | blocked Stage2 or 4B/high-MAE watch |
| `241560` | 15 | 3 | 4 | 9 | 7 | 2 | 4 | 44 | blocked Stage2; exchange-ratio fairness risk |
| `034020` | 13 | 5 | 7 | 10 | 8 | 4 | 5 | 52 | Stage2-Guarded or 4B watch only |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C32 problem is **governance event path-dependence**:

```text
C32 clean control-premium path:
  clear tender/control price or final exchange terms
  + minority-holder economics are transparent
  + legal/regulatory path is clear
  + MAE is contained
  => Stage2-Actionable / Yellow; Green only after final structure and economics are verified

C32 restructuring false-positive path:
  group restructuring headline
  + first-day MFE
  + unclear exchange ratio / value transfer / minority-holder fairness
  + 30D MAE worse than -25%
  => local 4B/high-MAE watch or blocked positive stage
```

The July 2024 Doosan cluster is the second case. The same event created first-day MFE across several entities, but all four tested paths produced severe MAE. This is precisely the kind of C32 event where the model must become suspicious of the map: when value moves inside a group, one ticker’s “premium” can be another ticker’s leakage.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R12L72_C32_DOOSAN_RESTRUCTURING_GUARD",
  "round": "R12",
  "loop": 72,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "guardrail_positive_case_count": 1,
  "counterexample_count": 3,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 12.69,
  "avg_mae_30d_pct": -39.84,
  "avg_mfe_90d_pct": 12.69,
  "avg_mae_90d_pct": -39.84,
  "avg_mfe_180d_pct": 16.58,
  "avg_mae_180d_pct": -39.84,
  "worst_mae_180d_pct": -53.70
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R12L72_C32_DOOSAN_RESTRUCTURING_GUARD",
  "local_4b_watch": [
    {
      "symbol": "000150",
      "reason": "parent-control vehicle recovered by D+180, but only after -53.70% MAE; event trigger itself is a 4B/high-MAE warning"
    },
    {
      "symbol": "034020",
      "reason": "holder-side economics may be relevant, but -27.16% MAE blocks unqualified Stage2/Green"
    }
  ],
  "blocked_positive_stage": [
    {
      "symbol": "454910",
      "reason": "beneficiary narrative produced +15.05% MFE but -43.26% MAE"
    },
    {
      "symbol": "241560",
      "reason": "exchange-ratio / minority-holder fairness path produced +15.53% MFE but -35.24% MAE"
    }
  ],
  "full_4b_requires_non_price_evidence": [
    "final approved restructuring terms",
    "exchange-ratio fairness evidence",
    "minority-holder approval or regulatory clearance",
    "post-restructuring earnings or cash-flow bridge"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: DOOSAN_GROUP_RESTRUCTURING_EXCHANGE_RATIO_MINORHOLDER_GUARD
rule_name: C32_group_restructuring_exchange_ratio_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C32 group restructuring / exchange-ratio events:

Tier A: verified final structure with clear holder economics
  Conditions:
    - final exchange ratio, merger/split terms, and shareholder approvals are URL-repaired
    - minority-holder fairness and regulatory path are clear
    - post-event MAE is contained
    - business-level earnings/cash-flow bridge exists
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after final terms and economics are confirmed

Tier B: headline restructuring with unclear value transfer
  Conditions:
    - group restructuring is announced
    - stock reacts with first-day MFE
    - exchange-ratio fairness / minority-holder economics are still disputed or source-proxy-only
  Routing:
    - Stage2-Actionable-Guarded at most
    - no Green
    - no production positive weight promotion

Tier C: high-MAE governance squeeze
  Conditions:
    - 30D MAE <= -25%
    - first-day or short-window MFE is followed by severe reversal
    - evidence is source_proxy_only
  Routing:
    - local 4B/high-MAE watch
    - blocked positive stage
    - count as counterexample or guardrail-positive if later full-window recovery occurs only after deep drawdown
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c32_group_restructuring_exchange_ratio_high_mae_router",
  "scope": "canonical_archetype_id:C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "restructuring_headline_alone_stage2_cap": "guarded_only",
    "exchange_ratio_fairness_required_for_yellow_green": true,
    "minorityholder_risk_blocks_green": true,
    "high_mae_watch_threshold_30d_pct": -25.0,
    "later_recovery_after_extreme_mae_does_not_validate_initial_green": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Four Doosan restructuring paths show severe MAE after first-day governance-event MFE. The cluster supports a C32 router that blocks Green until final structure, exchange-ratio fairness, minority-holder risk, and post-restructuring economics are URL-repaired."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R12L72_C32_DOOSAN_RESTRUCTURING_GUARD",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "contribution": "Adds a C32 group-restructuring exchange-ratio guardrail. The Doosan July 2024 cluster shows that governance restructuring can create first-day MFE while producing severe MAE across parent, beneficiary, target, and holder-side entities. C32 should require final approved terms, exchange-ratio fairness, minority-holder risk resolution, and business/economic bridge before Yellow/Green.",
  "guardrail_positive_case_added": 1,
  "counterexample_case_added": 3,
  "new_symbol_count": 4,
  "data_quality_blocker": "All four non-price restructuring triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C32 Green is blocked when source_proxy_only=true and 30D MAE is worse than -25%, even if first-day MFE is positive."
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
    000150: false
    454910: false
    241560: false
    034020: false
  evidence_url_pending:
    000150: true
    454910: true
    241560: true
    034020: true
  source_proxy_only:
    000150: true
    454910: true
    241560: true
    034020: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C32 group-restructuring / exchange-ratio / high-MAE guardrail design, but should not promote positive weights until filings, DART, exchange disclosures, company IR, or archived news verify final terms, exchange-ratio fairness, minority-holder treatment, approval status, regulatory review, and post-restructuring economics.
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
2. Preserve R12 / loop 72 metadata.
3. Add the cases to C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/DART/exchange-disclosure/company-IR/news-archive data verifies final restructuring terms, exchange-ratio fairness, minority-holder treatment, approval status, regulatory review, and post-restructuring economics.
6. Add a shadow-only rule candidate named C32_group_restructuring_exchange_ratio_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C32-specific guards:
   - source_proxy_only -> no Green
   - group restructuring headline alone -> Stage2-Guarded at most
   - exchange-ratio fairness and final terms required for Yellow/Green
   - 30D MAE <= -25% without repaired evidence -> local 4B/high-MAE watch or blocked positive stage
   - later full-window recovery after extreme MAE does not validate initial Green
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R12
completed_loop = 72
next_round = R13
next_loop = 72
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
next_allowed_scope = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW or R13_CROSS_ARCHETYPE_4B_4C_REDTEAM or R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION or R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
