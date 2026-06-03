# E2R Stock-Web v12 Residual Research — R11 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R11
completed_loop: 74
next_round: R12
next_loop: 74
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER
output_file: e2r_stock_web_v12_residual_round_R11_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
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
completed_loop  = 74
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Therefore:

```text
scheduled_round = R11
scheduled_loop  = 74
```

R11 permits:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
or
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID when the case is defense/policy-linked
```

This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER
```

This is a valid R11/L10 pairing.

---

## 1. Why this R11/C32 run

The no-repeat ledger shows C32 is already covered, but the top-covered symbols are concentrated in control fights and tender-cap names:

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

This file deliberately avoids those top-covered symbols and tests a different governance subtype:

```text
000150 두산
454910 두산로보틱스
241560 두산밥캣
034020 두산에너빌리티
```

Research question:

```text
Can C32 separate a real governance-repair rerating from a group restructuring event spike where the first candle reflects optionality, but the ratio, value-transfer, shareholder-protection, and execution bridge are not yet repaired?
```

C32 is a governance-event archetype. A tender price, control premium, or restructuring ratio is not just news; it is a ceiling, a floor, or a value-transfer map. The model should read the map before it follows the crowd. When the ratio is unresolved, the first candle can be a magnet; when the market starts demanding shareholder protection, the same event can turn into a trapdoor.

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
| `000150` | 두산 | active_like / KOSPI | no 2024 overlap; latest listed candidate 1999-12-03 | true |
| `454910` | 두산로보틱스 | active_like / KOSPI | none listed | true |
| `241560` | 두산밥캣 | active_like / KOSPI | none listed | true |
| `034020` | 두산에너빌리티 | active_like / KOSPI | no 2024 overlap; latest listed candidate 2020-12-24 | true |

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
The Stock-Web price path is fully validated, but company-level restructuring ratio, shareholder-protection mechanism, appraisal rights, final board/shareholder approval, revised governance structure, value-transfer map, and capital-allocation evidence still require later URL repair through filings, exchange disclosures, merger/spin-off documents, company IR, or regulatory documents before production weight promotion.
```

C32 interpretation used here:

```text
C32 is not simply “governance stock rose.”
It asks whether event optionality is mechanically convertible:
- tender price / control premium / ratio map,
- shareholder-protection and appraisal-right quality,
- final approval and execution path,
- value-transfer risk between group entities,
- capital allocation or shareholder-return bridge,
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
000150 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP -> no direct match found
241560 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP -> no direct match found
454910 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP -> no direct match found
034020 + C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 4,
  "minimum_new_symbol_count": 2,
  "positive_guarded_case_count": 1,
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
| `R11L74_C32_000150_20240912` | `000150` 두산 | governance repair / parent rerating after restructuring controversy | positive-guarded repair rerating |
| `R11L74_C32_454910_20240712` | `454910` 두산로보틱스 | restructuring beneficiary spike without final ratio bridge | event-spike high-MAE counterexample |
| `R11L74_C32_241560_20240712` | `241560` 두산밥캣 | value-transfer / ratio risk event | high-MAE counterexample |
| `R11L74_C32_034020_20240712` | `034020` 두산에너빌리티 | spin-off/restructuring ratio event | high-MAE counterexample |

The intended residual:

```text
C32 should separate:
1. governance-repair rerating after the market starts pricing shareholder-protection and value-transfer repair;
2. first-day beneficiary spikes where entry-day MFE is quickly overwhelmed by MAE;
3. value-transfer / spin-off ratio events where corporate action mechanics are not yet investable enough for Yellow/Green.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `000150` 두산 — governance-repair parent rerating

Trigger:

```text
trigger_date = 2024-09-11
trigger_type = Stage2-Actionable-Guarded
trigger_family = group_restructuring_governance_repair_parent_rerating
entry_date = 2024-09-12
entry_price = 146200.0
entry_price_type = next_tradable_open_after_governance_repair_repricing
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-09-11,145300.0,147100.0,140600.0,142800.0,63874.0,9159834200.0,2359603638000.0,16523835,KOSPI
2024-09-12,146200.0,160800.0,145500.0,160100.0,273577.0,42694004300.0,2645465983500.0,16523835,KOSPI
2024-10-11,174100.0,184100.0,174100.0,182900.0,126708.0,22942369700.0,3022209421500.0,16523835,KOSPI
2024-11-14,232000.0,245000.0,230000.0,232500.0,193797.0,45442695000.0,3841791637500.0,16523835,KOSPI
2024-12-17,269500.0,273500.0,261000.0,265000.0,159469.0,42789880500.0,4378816275000.0,16523835,KOSPI
2025-01-24,326500.0,335500.0,318000.0,332500.0,100849.0,33156403000.0,5494175137500.0,16523835,KOSPI
2025-02-26,367000.0,386000.0,360500.0,367500.0,153607.0,57148804500.0,6072509362500.0,16523835,KOSPI
2025-03-11,288000.0,327000.0,282000.0,324000.0,272452.0,84390462250.0,5353722540000.0,16523835,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 184100 | 2024-10-11 | 145500 | 2024-09-12 | +25.92% | -0.48% |
| 90 calendar days | 245000 | 2024-11-14 | 145500 | 2024-09-12 | +67.58% | -0.48% |
| 180 calendar days | 386000 | 2025-02-26 | 145500 | 2024-09-12 | +164.02% | -0.48% |

Interpretation:

```text
000150 is the positive-guarded repair-rerating holdout.
The important distinction is entry timing: the original July restructuring spike was not the clean signal, but the later governance-repair repricing had persistent MFE and near-zero MAE.
C32 should allow this path, but only after URL-repaired evidence shows that shareholder-protection, ratio repair, approval path, and capital allocation are visible.
```

### 6.2 `454910` 두산로보틱스 — restructuring beneficiary spike without final bridge

Trigger:

```text
trigger_date = 2024-07-11
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = restructuring_beneficiary_spike_without_final_ratio_execution_bridge
entry_date = 2024-07-12
entry_price = 95000.0
entry_price_type = next_tradable_open_after_restructuring_beneficiary_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,81500.0,86200.0,81100.0,85300.0,2032864.0,171787964200.0,5529144294000.0,64819980,KOSPI
2024-07-12,95000.0,109300.0,92200.0,105700.0,15292160.0,1552990227300.0,6851471886000.0,64819980,KOSPI
2024-07-25,75100.0,76400.0,72700.0,73400.0,1575540.0,116703314700.0,4757786532000.0,64819980,KOSPI
2024-08-05,66600.0,66700.0,53900.0,59300.0,919934.0,57094799600.0,3843824814000.0,64819980,KOSPI
2024-09-20,66500.0,66600.0,64700.0,65900.0,337332.0,22096806200.0,4271636682000.0,64819980,KOSPI
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
454910 is the hard C32 event-spike counterexample.
The peak occurred on entry day, then the 30D path already crossed the severe high-MAE zone.
This should block Stage2/Green unless final restructuring mechanics and value-transfer protection are repaired before entry.
```

### 6.3 `241560` 두산밥캣 — value-transfer / ratio risk event

Trigger:

```text
trigger_date = 2024-07-11
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = value_transfer_ratio_risk_event_spike_high_mae
entry_date = 2024-07-12
entry_price = 51500.0
entry_price_type = next_tradable_open_after_restructuring_ratio_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,51500.0,52000.0,50500.0,52000.0,252359.0,12966110100.0,5212956632000.0,100249166,KOSPI
2024-07-12,51500.0,59500.0,49850.0,54600.0,6789108.0,366749381750.0,5473604463600.0,100249166,KOSPI
2024-07-25,47000.0,47950.0,41150.0,44150.0,1981380.0,86261552550.0,4426000678900.0,100249166,KOSPI
2024-08-05,38400.0,38700.0,33350.0,34250.0,813194.0,29212468650.0,3433533935500.0,100249166,KOSPI
2024-09-20,42150.0,42900.0,41000.0,42550.0,896967.0,37972539100.0,4265602013300.0,100249166,KOSPI
2025-01-08,41600.0,42350.0,41500.0,42000.0,614640.0,25834673900.0,4210464972000.0,100249166,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 59500 | 2024-07-12 | 33350 | 2024-08-05 | +15.53% | -35.24% |
| 90 calendar days | 59500 | 2024-07-12 | 33350 | 2024-08-05 | +15.53% | -35.24% |
| 180 calendar days | 59500 | 2024-07-12 | 33350 | 2024-08-05 | +15.53% | -35.24% |

Interpretation:

```text
241560 is the value-transfer counterexample.
It had a clear event candle, but the drawdown immediately showed that shareholders were not simply receiving a clean control-premium rerating.
This should route to local 4B/high-MAE watch until ratio fairness, shareholder-protection, and final approval evidence are repaired.
```

### 6.4 `034020` 두산에너빌리티 — spin-off/restructuring ratio event

Trigger:

```text
trigger_date = 2024-07-11
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = spinoff_ratio_restructuring_event_high_mae_without_clear_shareholder_value_bridge
entry_date = 2024-07-12
entry_price = 20800.0
entry_price_type = next_tradable_open_after_spinoff_restructuring_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,21850.0,22150.0,21400.0,21850.0,9593927.0,209256696850.0,13996261040100.0,640561146,KOSPI
2024-07-12,20800.0,21700.0,19970.0,20900.0,25828467.0,536557704100.0,13387727951400.0,640561146,KOSPI
2024-07-18,23850.0,25000.0,20900.0,21000.0,63401772.0,1430000978200.0,13451784066000.0,640561146,KOSPI
2024-08-05,17280.0,17290.0,15150.0,15860.0,8528030.0,140762396920.0,10159299775560.0,640561146,KOSPI
2024-09-19,18500.0,18750.0,18310.0,18710.0,4720304.0,87822549170.0,11984899041660.0,640561146,KOSPI
2025-01-08,18690.0,18900.0,18370.0,18900.0,3834048.0,71439399070.0,12106605659400.0,640561146,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 25000 | 2024-07-18 | 15150 | 2024-08-05 | +20.19% | -27.16% |
| 90 calendar days | 25000 | 2024-07-18 | 15150 | 2024-08-05 | +20.19% | -27.16% |
| 180 calendar days | 25000 | 2024-07-18 | 15150 | 2024-08-05 | +20.19% | -27.16% |

Interpretation:

```text
034020 is a spin-off / ratio high-MAE counterexample.
MFE was meaningful, but the first 30D drawdown already crossed the high-MAE guardrail.
The event should stay guarded or 4B until the spin-off ratio, shareholder value bridge, and final execution path are repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R11L74_C32_DOOSAN_RESTRUCTURING_ROUTER","round":"R11","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER","symbol":"000150","name":"두산","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"group_restructuring_governance_repair_parent_rerating","trigger_date":"2024-09-11","entry_date":"2024-09-12","entry_price":146200.0,"entry_price_type":"next_tradable_open_after_governance_repair_repricing","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":25.92,"mae_30d_pct":-0.48,"mfe_90d_pct":67.58,"mae_90d_pct":-0.48,"mfe_180d_pct":164.02,"mae_180d_pct":-0.48,"peak_price_180d":386000.0,"peak_date_180d":"2025-02-26","trough_price_180d":145500.0,"trough_date_180d":"2024-09-12","calibration_usable":true,"case_polarity":"positive_guarded_governance_repair","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_governance_value_transfer_repair_and_shareholder_return_bridge_repaired","residual_error_type":"governance_repair_parent_rerating_can_be_valid_but_green_requires_repaired_restructuring_ratio_and_capital_allocation_evidence"}
{"row_type":"trigger","research_id":"R11L74_C32_DOOSAN_RESTRUCTURING_ROUTER","round":"R11","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER","symbol":"454910","name":"두산로보틱스","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"restructuring_beneficiary_spike_without_final_ratio_execution_bridge","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":95000.0,"entry_price_type":"next_tradable_open_after_restructuring_beneficiary_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.05,"mae_30d_pct":-43.26,"mfe_90d_pct":15.05,"mae_90d_pct":-43.26,"mfe_180d_pct":15.05,"mae_180d_pct":-43.26,"peak_price_180d":109300.0,"peak_date_180d":"2024-07-12","trough_price_180d":53900.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_event_spike_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"beneficiary_spike_spent_upside_on_entry_day_and_failed_without_final_restructuring_ratio_bridge"}
{"row_type":"trigger","research_id":"R11L74_C32_DOOSAN_RESTRUCTURING_ROUTER","round":"R11","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER","symbol":"241560","name":"두산밥캣","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"value_transfer_ratio_risk_event_spike_high_mae","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":51500.0,"entry_price_type":"next_tradable_open_after_restructuring_ratio_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.53,"mae_30d_pct":-35.24,"mfe_90d_pct":15.53,"mae_90d_pct":-35.24,"mfe_180d_pct":15.53,"mae_180d_pct":-35.24,"peak_price_180d":59500.0,"peak_date_180d":"2024-07-12","trough_price_180d":33350.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_value_transfer_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch_until_ratio_shareholder_protection_bridge_repaired","residual_error_type":"value_transfer_and_ratio_uncertainty_overwhelmed_initial_event_mfe"}
{"row_type":"trigger","research_id":"R11L74_C32_DOOSAN_RESTRUCTURING_ROUTER","round":"R11","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"spinoff_ratio_restructuring_event_high_mae_without_clear_shareholder_value_bridge","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":20800.0,"entry_price_type":"next_tradable_open_after_spinoff_restructuring_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":20.19,"mae_30d_pct":-27.16,"mfe_90d_pct":20.19,"mae_90d_pct":-27.16,"mfe_180d_pct":20.19,"mae_180d_pct":-27.16,"peak_price_180d":25000.0,"peak_date_180d":"2024-07-18","trough_price_180d":15150.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_spinoff_ratio_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_spinoff_ratio_shareholder_value_bridge_repaired","residual_error_type":"spinoff_ratio_event_had_mfe_but_30d_mae_crossed_high_mae_guardrail_without_value_bridge"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | governance event clarity | ratio / tender cap map | shareholder-protection bridge | execution/finality | market mispricing | value-transfer risk control | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `000150` | 11 | 9 | 10 | 9 | 15 | 8 | 6 | 68 | Stage2-Guarded / Yellow after governance repair evidence |
| `454910` | 6 | 3 | 2 | 3 | 9 | 1 | 4 | 28 | blocked Stage2 / 4B-4C high-MAE watch |
| `241560` | 5 | 3 | 2 | 3 | 7 | 1 | 4 | 25 | blocked Stage2 or local 4B watch |
| `034020` | 6 | 4 | 3 | 4 | 8 | 2 | 4 | 31 | Stage2-Guarded at most / 4B high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining C32 issue is **governance-event optionality without a repaired mechanical bridge**:

```text
C32 repair rerating path:
  governance controversy reprices after repair / shareholder-protection signal
  + MFE persists beyond the initial event window
  + MAE remains contained
  + URL-repaired ratio/finality/capital-allocation evidence exists
  => Stage2-Guarded / Yellow, possible Green after proof

C32 first-day beneficiary spike:
  event optionality creates entry-day MFE
  + MAE_30D <= -30%
  + bridge evidence remains source_proxy_only
  => block Stage2 or route to 4B/4C high-MAE watch

C32 value-transfer/spin-off ratio risk:
  MFE is present
  + MAE_30D <= -25%
  + shareholder-protection / ratio fairness not repaired
  => Stage2-Guarded at most, local 4B watch, no Green
```

`000150` prevents overblocking: governance repair can become a real rerating.  
`454910`, `241560`, and `034020` show why the first restructuring candle should not be promoted without a repaired value-transfer map.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R11L74_C32_DOOSAN_RESTRUCTURING_ROUTER",
  "round": "R11",
  "loop": 74,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "fine_archetype_id": "GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER",
  "case_count": 4,
  "calibration_usable_case_count": 4,
  "positive_guarded_case_count": 1,
  "counterexample_count": 3,
  "new_symbol_count": 4,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "avg_mfe_30d_pct": 19.17,
  "avg_mae_30d_pct": -26.54,
  "avg_mfe_90d_pct": 29.59,
  "avg_mae_90d_pct": -26.54,
  "avg_mfe_180d_pct": 53.7,
  "avg_mae_180d_pct": -26.54,
  "max_mfe_180d_pct": 164.02,
  "worst_mae_180d_pct": -43.26
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R11L74_C32_DOOSAN_RESTRUCTURING_ROUTER",
  "stage2_guarded_or_yellow_candidate": [
    {
      "symbol": "000150",
      "reason": "governance-repair entry had +164.02% 180D MFE with only -0.48% MAE; requires repaired ratio/shareholder-protection/capital-allocation evidence before Green"
    }
  ],
  "local_4b_high_mae_watch": [
    {
      "symbol": "034020",
      "reason": "spin-off/restructuring ratio event had +20.19% MFE but -27.16% 30D/180D MAE"
    },
    {
      "symbol": "241560",
      "reason": "value-transfer/ratio event had +15.53% MFE but -35.24% MAE"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "454910",
      "reason": "beneficiary spike peaked on entry day and then reached -43.26% MAE"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "final restructuring ratio and value-transfer map",
    "shareholder-protection / appraisal-right quality",
    "board / shareholder / regulatory approval path",
    "tender cap or control premium mechanics",
    "capital allocation and shareholder-return bridge"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER
rule_name: C32_governance_repair_vs_restructuring_event_spike_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C32 governance / control-premium / restructuring cases:

Tier A: verified governance-repair rerating
  Conditions:
    - event has moved from raw optionality to repaired mechanics
    - ratio, shareholder protection, approval path, and capital allocation are URL-repaired
    - MAE remains contained
    - MFE persists beyond one event candle
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after final mechanics and shareholder-value bridge are verified

Tier B: first-day beneficiary spike
  Conditions:
    - MFE peaks on entry day or first 5 trading days
    - MAE_30D <= -30%
    - evidence remains source_proxy_only
  Routing:
    - block Stage2
    - local 4B / 4C high-MAE watch
    - count as counterexample

Tier C: spin-off / ratio / value-transfer risk
  Conditions:
    - MFE_30D >= +10%
    - MAE_30D <= -25%
    - final ratio or shareholder-protection bridge is missing
  Routing:
    - Stage2-Guarded at most
    - local 4B watch
    - no Green
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c32_governance_repair_vs_restructuring_event_spike_high_mae_router",
  "scope": "canonical_archetype_id:C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "final_ratio_shareholder_protection_bridge_required_for_green": true,
    "governance_repair_stage2_guarded_allowed": true,
    "entry_day_peak_high_mae_blocks_stage2": true,
    "beneficiary_spike_mae30_threshold_pct": -30.0,
    "ratio_value_transfer_mae30_threshold_pct": -25.0,
    "ratio_value_transfer_mfe30_threshold_pct": 10.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "One governance-repair positive path and three restructuring/spin-off high-MAE counterexamples show that C32 should not promote raw restructuring optionality without final ratio, shareholder-protection, and value-transfer evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R11L74_C32_DOOSAN_RESTRUCTURING_ROUTER",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP",
  "contribution": "Adds four non-top-covered C32 group-restructuring governance cases and separates a later governance-repair parent rerating from first-day beneficiary, value-transfer, and spin-off ratio high-MAE counterexamples. C32 Green should require URL-repaired final ratio, shareholder-protection, approval path, value-transfer map, tender/control-premium mechanics, and capital-allocation evidence.",
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 3,
  "new_symbol_count": 4,
  "data_quality_blocker": "All four non-price governance/restructuring triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C32 source_proxy_only first-day beneficiary spikes with MAE_30D <= -30% should block Stage2; restructuring ratio/value-transfer cases with MFE_30D >= +10% and MAE_30D <= -25% should cap at Stage2-Guarded or local 4B until evidence repair."
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
- Therefore this artifact is useful for C32 governance / restructuring-ratio residual shape and high-MAE guardrail design, but should not promote positive weights until filings, exchange disclosures, merger/spin-off documents, company IR, or regulatory documents verify final ratio, approval path, shareholder protection, value-transfer map, and capital allocation.
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
2. Preserve R11 / loop 74 metadata.
3. Add the cases to C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP only if parser validation passes.
4. Treat all four non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/exchange-disclosure/merger-document/company-IR/regulatory data verifies final restructuring ratio, approval path, shareholder protection, value-transfer map, tender/control-premium mechanics, and capital allocation.
6. Add a shadow-only rule candidate named C32_governance_repair_vs_restructuring_event_spike_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C32-specific guards:
   - source_proxy_only -> no Green
   - Green requires repaired final ratio / shareholder-protection / value-transfer bridge
   - governance-repair entries with persistent MFE and contained MAE may remain Stage2-Guarded until evidence repair
   - first-day beneficiary spike with MAE_30D <= -30% -> block Stage2 or 4B/4C high-MAE watch
   - restructuring ratio/value-transfer case with MFE_30D >= +10% and MAE_30D <= -25% -> Stage2-Guarded at most
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R11
completed_loop = 74
next_round = R12
next_loop = 74
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
round_schedule_status = valid
round_sector_consistency = pass
```
