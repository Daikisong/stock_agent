# E2R Stock-Web v12 Residual Research — R13 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R13
completed_loop: 73
next_round: R1
next_loop: 74
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER
output_file: e2r_stock_web_v12_residual_round_R13_loop_73_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Execution gate

This file follows the v12 historical calibration prompt as the execution procedure.  
`V12_Research_No_Repeat_Index.md` is used only as the duplicate-avoidance ledger.

This is not a live stock discovery run, not investment advice, not a trading instruction, and not a `stock_agent` code patch.  
The only output is a standalone historical calibration / cross-archetype residual Markdown artifact.

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
completed_round = R12
completed_loop  = 73
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Therefore:

```text
scheduled_round = R13
scheduled_loop  = 73
```

R13 is not a normal sector-expansion round. It must use only cross-archetype review scopes.  
This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id = LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER
```

This is a valid R13 scope.

---

## 1. Why this R13 run

The no-repeat ledger shows the R13 high-MAE guardrail bucket is still far smaller than the broad R13 4B/4C red-team bucket:

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM:
  rows: 368
  symbols: 153

R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL:
  rows: 23
  symbols: 21
  date_range: 2020-11-06~2024-07-22
  good/bad S2: 3/5
  4B/4C: 5/4
```

Loop 73 produced many sector-specific guardrail candidates. R13 should compress those into a cross-archetype rule that later implementation can apply consistently.

The review thesis:

```text
A trigger can have valid theme/evidence relevance and still be wrong as Stage2/Green
when the price path shows weak MFE, same-window peak, or delayed high MAE
before the non-price bridge is URL-repaired.
```

This run deliberately includes two positive holdouts:

```text
089030 테크윙
340570 티앤엘
```

These keep the rule from becoming a blunt “high volatility = reject” filter. The counterexamples then define the guardrail:

```text
299030 하나기술
020150 롯데에너지머티리얼즈
017040 광명전기
149980 하이로닉
225570 넥슨게임즈
065450 빅텍
```

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

| symbol | name | underlying canonical | profile / corporate-action status | calibration usable |
|---|---|---|---|---|
| `089030` | 테크윙 | C08 | active_like; no 2024 corporate-action overlap | true |
| `340570` | 티앤엘 | C25 | active_like; no 2024 corporate-action overlap | true |
| `299030` | 하나기술 | C11 | active_like; no 2024 corporate-action overlap | true |
| `020150` | 롯데에너지머티리얼즈 | C13 | active_like; none listed | true |
| `017040` | 광명전기 | C02 | active_like; no 2024 corporate-action overlap | true |
| `149980` | 하이로닉 | C25 | active_like; no 2024 corporate-action overlap | true |
| `225570` | 넥슨게임즈 | C27 | active_like; no 2024 corporate-action overlap | true |
| `065450` | 빅텍 | C03 | active_like; no 2024 corporate-action overlap | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

For this R13 artifact, the hard key uses the R13 review pseudo-archetype:

```text
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL + symbol + trigger_type + entry_date
```

Targeted repository searches performed in this run:

```text
089030 + R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL -> no direct match found
299030 + R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL -> no direct match found
020150 + R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL -> no direct match found
225570 + R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL -> no direct match found
```

Novelty accounting:

```json
{
  "row_type": "novelty_check",
  "research_id": "R13L73_HIGH_MAE_GUARDRAIL",
  "r13_scope": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "case_count": 8,
  "underlying_canonical_count": 7,
  "symbol_count": 8,
  "positive_holdout_count": 2,
  "counterexample_count": 6,
  "duplicate_status": "pass_for_r13_cross_archetype_review",
  "new_independent_case_ratio": 1.00
}
```

---

## 4. Review thesis

The cross-archetype pattern being tested is:

```text
source_proxy_only or evidence_url_pending
+ plausible sector/theme relevance
+ price path shows weak MFE, same-window peak, or delayed high MAE
= no Green and often no Stage2 until URL-repaired bridge evidence exists
```

The mechanism differs by sector, but the failure shape rhymes:

```text
C02/C03: theme headline without order/backlog/export bridge
C11/C13: orderbook/JV/utilization label without customer or margin bridge
C25/C27: launch/device excitement without repeat-demand / monetization bridge
```

The positive holdouts show the inverse:

```text
persistent MFE
+ contained MAE
+ plausible URL-repairable evidence bridge
= Stage2/Yellow candidate, but still not automatic Green
```

---

## 5. Case design

| symbol | underlying canonical | role | key path shape |
|---|---|---|---|
| `089030` | C08 | positive holdout | +289.01% 180D MFE / -3.52% 180D MAE |
| `340570` | C25 | positive holdout | +52.48% 180D MFE / -1.29% 180D MAE |
| `299030` | C11 | hard counterexample | +11.27% 180D MFE / -65.34% 180D MAE |
| `020150` | C13 | hard counterexample | +5.65% 180D MFE / -60.64% 180D MAE |
| `017040` | C02 | theme-spike counterexample | +23.65% 180D MFE / -53.45% 180D MAE |
| `149980` | C25 | post-spike false positive | +1.30% 180D MFE / -50.97% 180D MAE |
| `225570` | C27 | high-MFE / high-MAE trap | +66.31% 180D MFE / -32.51% 180D MAE |
| `065450` | C03 | geopolitical theme spike | +7.12% 180D MFE / -28.79% 180D MAE |

---

## 6. Stock-Web OHLC and backtest excerpts

### 089030 — C08 positive holdout: HBM/test-handler customer-quality

### 6.1 `089030` 테크윙 — HBM/test-handler customer-quality positive anchor

Trigger:

```text
trigger_date = 2024-02-08
trigger_type = Stage2-Actionable
trigger_family = HBM_test_handler_customer_quality_breakout
entry_date = 2024-02-13
entry_price = 18200.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-08,15490.0,17640.0,15490.0,17400.0,3200495.0,53478356970.0,649953423000.0,37353645,KOSDAQ
2024-02-13,18200.0,19970.0,18090.0,18690.0,5859501.0,111737150520.0,698139625050.0,37353645,KOSDAQ
2024-02-19,18210.0,21800.0,18070.0,21550.0,7745873.0,159588823220.0,804971049750.0,37353645,KOSDAQ
2024-03-15,28600.0,30850.0,27800.0,30300.0,1230532.0,35920895300.0,1131815443500.0,37353645,KOSDAQ
2024-04-11,33650.0,39100.0,33350.0,38700.0,2637442.0,97864810200.0,1445586061500.0,37353645,KOSDAQ
2024-05-28,40900.0,45200.0,40550.0,43500.0,1916853.0,83046502300.0,1624883557500.0,37353645,KOSDAQ
2024-06-27,54000.0,59800.0,53300.0,59100.0,1324663.0,76380432400.0,2207600419500.0,37353645,KOSDAQ
2024-07-11,67800.0,70800.0,67200.0,68700.0,874088.0,60222114100.0,2566195411500.0,37353645,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 29500 | 2024-03-14 | 17560 | 2024-02-14 | +62.09% | -3.52% |
| 90 calendar days | 39100 | 2024-04-11 | 17560 | 2024-02-14 | +114.84% | -3.52% |
| 180 calendar days | 70800 | 2024-07-11 | 17560 | 2024-02-14 | +289.01% | -3.52% |

R13 interpretation:

```text
R13 holdout. This case prevents overblocking: high-MFE can be legitimate when MAE stays contained and customer-quality evidence can later be URL-repaired. The rule should not punish persistent low-MAE winners.
```
### 340570 — C25 positive holdout: medical consumable export-commercialization

### 6.1 `340570` 티앤엘 — medical consumable export-commercialization positive anchor

Trigger:

```text
trigger_date = 2024-03-18
trigger_type = Stage2-Actionable
trigger_family = woundcare_medical_consumable_export_commercialization
entry_date = 2024-03-19
entry_price = 50500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-18,47600.0,48200.0,46600.0,47350.0,61407.0,2920744300.0,384860800000.0,8128000,KOSDAQ
2024-03-19,50500.0,52700.0,49850.0,51300.0,450689.0,23133609850.0,416966400000.0,8128000,KOSDAQ
2024-04-11,61000.0,63500.0,58000.0,59900.0,346955.0,21133689100.0,486867200000.0,8128000,KOSDAQ
2024-05-16,65300.0,71600.0,64100.0,70800.0,658584.0,45076416300.0,575462400000.0,8128000,KOSDAQ
2024-06-24,70000.0,74100.0,69500.0,71600.0,236914.0,17075471300.0,581964800000.0,8128000,KOSDAQ
2024-08-20,74000.0,76500.0,72100.0,75600.0,285883.0,21380733700.0,614476800000.0,8128000,KOSDAQ
2024-09-04,66500.0,68600.0,65500.0,67200.0,70468.0,4744636500.0,546201600000.0,8128000,KOSDAQ
2024-09-23,73000.0,75800.0,72700.0,74000.0,237492.0,17549749500.0,601472000000.0,8128000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 63500 | 2024-04-11 | 49850 | 2024-03-19 | +25.74% | -1.29% |
| 90 calendar days | 71600 | 2024-05-16 | 49850 | 2024-03-19 | +41.78% | -1.29% |
| 180 calendar days | 77000 | 2024-08-21 | 49850 | 2024-03-19 | +52.48% | -1.29% |

R13 interpretation:

```text
R13 holdout. This is a commercial-bridge style positive: persistent MFE, tiny MAE, and a plausible medical-consumable export path. Green still requires URL repair, but the high-MAE guard must leave this path open.
```
### 299030 — C11 thesis-break: battery equipment orderbook relief failure

### 6.3 `299030` 하나기술 — orderbook thesis break / relief failure

Trigger:

```text
trigger_date = 2024-06-20
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_equipment_orderbook_thesis_break_relief_failure
entry_date = 2024-06-21
entry_price = 48350.0
entry_price_type = next_tradable_open_after_gap_down
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-20,57400.0,57800.0,56000.0,56000.0,103236.0,5728279000.0,456993992000.0,8160607,KOSDAQ
2024-06-21,48350.0,53800.0,48350.0,50700.0,590368.0,30018518200.0,413742774900.0,8160607,KOSDAQ
2024-06-24,49050.0,49600.0,40550.0,41150.0,800557.0,35003545750.0,335808978050.0,8160607,KOSDAQ
2024-07-19,30800.0,31550.0,30500.0,31550.0,56577.0,1748527350.0,257782209150.0,8170593,KOSDAQ
2024-08-05,30150.0,30550.0,24350.0,25450.0,167450.0,4567850200.0,207941591850.0,8170593,KOSDAQ
2024-11-15,20300.0,21800.0,18500.0,20600.0,102683.0,2077357750.0,164695146000.0,7994910,KOSDAQ
2024-12-09,17760.0,18500.0,16760.0,16860.0,57836.0,1000907410.0,134794182600.0,7994910,KOSDAQ
2024-12-18,18820.0,19540.0,18820.0,19400.0,22777.0,438988660.0,155101254000.0,7994910,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 53800 | 2024-06-21 | 30500 | 2024-07-19 | +11.27% | -36.92% |
| 90 calendar days | 53800 | 2024-06-21 | 24350 | 2024-08-05 | +11.27% | -49.64% |
| 180 calendar days | 53800 | 2024-06-21 | 16760 | 2024-12-09 | +11.27% | -65.34% |

R13 interpretation:

```text
R13 hard failure. The first window had only +11.27% MFE and already -36.92% MAE; by 180D the path reached -65.34%. This is a thesis-break relief candle, not Stage2.
```
### 020150 — C13 utilization failure: copper-foil customer call-off

### 6.3 `020150` 롯데에너지머티리얼즈 — copper-foil utilization / call-off relief failure

Trigger:

```text
trigger_date = 2024-06-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = copperfoil_utilization_customer_calloff_relief_failure
entry_date = 2024-06-27
entry_price = 53100.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,53100.0,55100.0,53100.0,53300.0,315190.0,17005953500.0,2457707505500.0,46110835,KOSPI
2024-06-27,53100.0,54100.0,51700.0,52000.0,267020.0,14086406500.0,2397763420000.0,46110835,KOSPI
2024-07-03,54900.0,56100.0,52100.0,52900.0,344462.0,18519786300.0,2439263171500.0,46110835,KOSPI
2024-07-26,37450.0,37750.0,36300.0,36800.0,237532.0,8718396300.0,1696878728000.0,46110835,KOSPI
2024-08-05,36100.0,36750.0,30500.0,32200.0,468908.0,15821669100.0,1484768887000.0,46110835,KOSPI
2024-09-05,40050.0,45650.0,40050.0,43000.0,1121196.0,48476794250.0,1982765905000.0,46110835,KOSPI
2024-11-14,30300.0,30650.0,28100.0,28100.0,332305.0,9635744550.0,1295714463500.0,46110835,KOSPI
2024-12-09,22100.0,22400.0,20900.0,21000.0,212907.0,4555484550.0,968327535000.0,46110835,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 56100 | 2024-07-03 | 36300 | 2024-07-26 | +5.65% | -31.64% |
| 90 calendar days | 56100 | 2024-07-03 | 30500 | 2024-08-05 | +5.65% | -42.56% |
| 180 calendar days | 56100 | 2024-07-03 | 20900 | 2024-12-09 | +5.65% | -60.64% |

R13 interpretation:

```text
R13 hard failure. Copper-foil/utilization relevance existed, but MFE was only +5.65% while 30D MAE reached -31.64% and 180D MAE reached -60.64%. This should route to 4C/high-MAE watch.
```
### 017040 — C02 theme spike: low-price power-equipment blowoff

### 6.3 `017040` 광명전기 — low-price electrical equipment theme spike, then 4B/4C drawdown

Trigger:

```text
trigger_date = 2024-05-03
trigger_type = 4B-local-watch
trigger_family = low_price_power_equipment_theme_spike_without_order_bridge
entry_date = 2024-05-07
entry_price = 2685.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-03,2735.0,2735.0,2655.0,2660.0,1421432.0,3814490845.0,115278055900.0,43337615,KOSPI
2024-05-07,2685.0,3270.0,2670.0,3185.0,43351466.0,133598176775.0,138030303775.0,43337615,KOSPI
2024-05-08,3090.0,3320.0,3020.0,3060.0,15800256.0,49840216860.0,132613101900.0,43337615,KOSPI
2024-05-13,2495.0,3030.0,2400.0,2670.0,26914087.0,73195203245.0,115711432050.0,43337615,KOSPI
2024-06-05,2240.0,2255.0,2185.0,2205.0,640390.0,1417008300.0,95559441075.0,43337615,KOSPI
2024-08-05,1935.0,1999.0,1614.0,1744.0,1349197.0,2463892933.0,75580800560.0,43337615,KOSPI
2024-10-25,1452.0,1464.0,1390.0,1391.0,651453.0,925115812.0,60282622465.0,43337615,KOSPI
2024-10-31,1338.0,1415.0,1250.0,1368.0,1534948.0,2041411136.0,59285857320.0,43337615,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 3320 | 2024-05-08 | 2185 | 2024-06-05 | +23.65% | -18.62% |
| 90 calendar days | 3320 | 2024-05-08 | 1614 | 2024-08-05 | +23.65% | -39.89% |
| 180 calendar days | 3320 | 2024-05-08 | 1250 | 2024-10-31 | +23.65% | -53.45% |

R13 interpretation:

```text
R13 hard failure. The power-equipment theme spike had a visible first spark, but the 180D drawdown reached -53.45%. Low-price theme moves need an order/backlog bridge before Stage2.
```
### 149980 — C25 post-spike: aesthetic-device weak follow-through

### 6.3 `149980` 하이로닉 — aesthetic-device spike with weak follow-through

Trigger:

```text
trigger_date = 2024-06-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = aesthetic_device_theme_spike_weak_followthrough
entry_date = 2024-06-27
entry_price = 10810.0
entry_price_type = next_tradable_open_after_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,9190.0,11250.0,9170.0,10510.0,13305769.0,141345208930.0,195395225130.0,18591363,KOSDAQ
2024-06-27,10810.0,10950.0,10010.0,10230.0,3297875.0,34411113750.0,190189643490.0,18591363,KOSDAQ
2024-07-26,9060.0,9350.0,8410.0,8610.0,486263.0,4217401920.0,160071635430.0,18591363,KOSDAQ
2024-08-05,7460.0,7520.0,6450.0,6770.0,680779.0,4822642880.0,125863527510.0,18591363,KOSDAQ
2024-09-09,10050.0,10640.0,8280.0,8280.0,7028504.0,66456185330.0,153936485640.0,18591363,KOSDAQ
2024-10-16,6700.0,8710.0,6600.0,7400.0,9022074.0,70914685460.0,137576086200.0,18591363,KOSDAQ
2024-11-13,6060.0,6210.0,5920.0,5920.0,123620.0,746915490.0,110078628960.0,18594363,KOSDAQ
2024-12-09,5780.0,6020.0,5300.0,5310.0,222108.0,1217213060.0,98736067530.0,18594363,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 10950 | 2024-06-27 | 8410 | 2024-07-26 | +1.30% | -22.20% |
| 90 calendar days | 10950 | 2024-06-27 | 6450 | 2024-08-05 | +1.30% | -40.33% |
| 180 calendar days | 10950 | 2024-06-27 | 5300 | 2024-12-09 | +1.30% | -50.97% |

R13 interpretation:

```text
R13 hard failure. The event candle was already the ceiling: MFE was only +1.30% while 180D MAE reached -50.97%. This should block Stage2 unless a fresh commercial bridge appears before entry.
```
### 225570 — C27 post-launch: high-MFE/high-MAE live-service trap

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

R13 interpretation:

```text
R13 mixed high-MFE/high-MAE trap. Launch MFE was real at +66.31%, but 180D MAE reached -32.51%. This is not a simple false positive; it is a 4B/high-MAE guard until retention and monetization are repaired.
```
### 065450 — C03 geopolitical theme: defense spike without backlog bridge

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

R13 interpretation:

```text
R13 theme-spike failure. The defense/geopolitical alarm produced only +7.12% MFE and immediate -26.06% 30D MAE. It should remain 4B/local watch without export-framework/backlog evidence.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R13L73_HIGH_MAE_GUARDRAIL","round":"R13","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER","underlying_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","underlying_canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","underlying_fine_archetype_id":"HBM_TEST_OSAT_SECOND_TIER_CUSTOMER_QUALITY_AND_HIGH_MAE_ROUTER","symbol":"089030","name":"테크윙","trigger_type":"Stage2-Actionable","trigger_family":"HBM_test_handler_customer_quality_breakout","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":18200.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":62.09,"mae_30d_pct":-3.52,"mfe_90d_pct":114.84,"mae_90d_pct":-3.52,"mfe_180d_pct":289.01,"mae_180d_pct":-3.52,"peak_price_180d":70800.0,"peak_date_180d":"2024-07-11","trough_price_180d":17560.0,"trough_date_180d":"2024-02-14","calibration_usable":true,"case_polarity":"positive_anchor","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_or_Green_after_customer_quality_evidence_repaired","residual_error_type":"positive_anchor_requires_url_repaired_customer_order_margin_bridge_before_green","source_loop73_artifact":"e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md"}
{"row_type":"trigger","research_id":"R13L73_HIGH_MAE_GUARDRAIL","round":"R13","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER","underlying_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","underlying_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","underlying_fine_archetype_id":"AESTHETIC_MEDICAL_DEVICE_EXPORT_COMMERCIALIZATION_AND_HIGH_MAE_ROUTER","symbol":"340570","name":"티앤엘","trigger_type":"Stage2-Actionable","trigger_family":"woundcare_medical_consumable_export_commercialization","trigger_date":"2024-03-18","entry_date":"2024-03-19","entry_price":50500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":25.74,"mae_30d_pct":-1.29,"mfe_90d_pct":41.78,"mae_90d_pct":-1.29,"mfe_180d_pct":52.48,"mae_180d_pct":-1.29,"peak_price_180d":77000.0,"peak_date_180d":"2024-08-21","trough_price_180d":49850.0,"trough_date_180d":"2024-03-19","calibration_usable":true,"case_polarity":"positive_anchor","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_export_reimbursement_margin_bridge_repaired","residual_error_type":"positive_anchor_requires_url_repaired_export_regulatory_repeat_demand_margin_evidence_before_green","source_loop73_artifact":"e2r_stock_web_v12_residual_round_R7_loop_73_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"trigger","research_id":"R13L73_HIGH_MAE_GUARDRAIL","round":"R13","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER","underlying_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","underlying_canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","underlying_fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_RERATING_AND_HIGH_MAE_ROUTER","symbol":"299030","name":"하나기술","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_equipment_orderbook_thesis_break_relief_failure","trigger_date":"2024-06-20","entry_date":"2024-06-21","entry_price":48350.0,"entry_price_type":"next_tradable_open_after_gap_down","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":11.27,"mae_30d_pct":-36.92,"mfe_90d_pct":11.27,"mae_90d_pct":-49.64,"mfe_180d_pct":11.27,"mae_180d_pct":-65.34,"peak_price_180d":53800.0,"peak_date_180d":"2024-06-21","trough_price_180d":16760.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_thesis_break","r13_case_role":"high_mae_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"relief_attempt_after_orderbook_thesis_break_had_low_mfe_extreme_mae","source_loop73_artifact":"e2r_stock_web_v12_residual_round_R3_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md"}
{"row_type":"trigger","research_id":"R13L73_HIGH_MAE_GUARDRAIL","round":"R13","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER","underlying_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","underlying_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","underlying_fine_archetype_id":"BATTERY_US_JV_AMPC_UTILIZATION_PARENT_SEPARATOR_COPPERFOIL_HIGH_MAE_ROUTER","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"copperfoil_utilization_customer_calloff_relief_failure","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":53100.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":5.65,"mae_30d_pct":-31.64,"mfe_90d_pct":5.65,"mae_90d_pct":-42.56,"mfe_180d_pct":5.65,"mae_180d_pct":-60.64,"peak_price_180d":56100.0,"peak_date_180d":"2024-07-03","trough_price_180d":20900.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_extreme_mae","r13_case_role":"high_mae_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4C_high_MAE_watch_until_utilization_customer_margin_bridge_repaired","residual_error_type":"copperfoil_utilization_relief_entry_low_mfe_extreme_mae","source_loop73_artifact":"e2r_stock_web_v12_residual_round_R9_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md"}
{"row_type":"trigger","research_id":"R13L73_HIGH_MAE_GUARDRAIL","round":"R13","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER","underlying_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","underlying_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","underlying_fine_archetype_id":"SECOND_TIER_POWER_EQUIPMENT_GRID_CAPEX_AND_DATACENTER_RELIEF_RALLY_GUARD","symbol":"017040","name":"광명전기","trigger_type":"4B-local-watch","trigger_family":"low_price_power_equipment_theme_spike_without_order_bridge","trigger_date":"2024-05-03","entry_date":"2024-05-07","entry_price":2685.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":23.65,"mae_30d_pct":-18.62,"mfe_90d_pct":23.65,"mae_90d_pct":-39.89,"mfe_180d_pct":23.65,"mae_180d_pct":-53.45,"peak_price_180d":3320.0,"peak_date_180d":"2024-05-08","trough_price_180d":1250.0,"trough_date_180d":"2024-10-31","calibration_usable":true,"case_polarity":"counterexample_theme_blowoff","r13_case_role":"high_mae_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":true,"expected_stage_current_profile":"4B_local_watch_or_4C_high_MAE_guard","residual_error_type":"low_price_grid_theme_spike_low_mfe_extreme_mae_should_block_stage2_green","source_loop73_artifact":"e2r_stock_web_v12_residual_round_R1_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","research_id":"R13L73_HIGH_MAE_GUARDRAIL","round":"R13","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER","underlying_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","underlying_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","underlying_fine_archetype_id":"AESTHETIC_MEDICAL_DEVICE_EXPORT_COMMERCIALIZATION_AND_HIGH_MAE_ROUTER","symbol":"149980","name":"하이로닉","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"aesthetic_device_theme_spike_weak_followthrough","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":10810.0,"entry_price_type":"next_tradable_open_after_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.3,"mae_30d_pct":-22.2,"mfe_90d_pct":1.3,"mae_90d_pct":-40.33,"mfe_180d_pct":1.3,"mae_180d_pct":-50.97,"peak_price_180d":10950.0,"peak_date_180d":"2024-06-27","trough_price_180d":5300.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_low_mfe_high_mae","r13_case_role":"high_mae_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"post_spike_medical_device_entry_low_mfe_extreme_mae_without_fresh_commercial_bridge","source_loop73_artifact":"e2r_stock_web_v12_residual_round_R7_loop_73_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"trigger","research_id":"R13L73_HIGH_MAE_GUARDRAIL","round":"R13","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER","underlying_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","underlying_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","underlying_fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_MONETIZATION_AND_POST_LAUNCH_HIGH_MAE_ROUTER","symbol":"225570","name":"넥슨게임즈","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"global_launch_live_service_hit_narrative_high_mae","trigger_date":"2024-07-02","entry_date":"2024-07-03","entry_price":18610.0,"entry_price_type":"next_tradable_open_after_launch_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":62.28,"mae_30d_pct":-11.39,"mfe_90d_pct":66.31,"mae_90d_pct":-20.69,"mfe_180d_pct":66.31,"mae_180d_pct":-32.51,"peak_price_180d":30950.0,"peak_date_180d":"2024-08-09","trough_price_180d":12560.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","r13_case_role":"high_mae_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch_until_retention_monetization_evidence_repaired","residual_error_type":"post_launch_mfe_overwhelmed_by_180d_high_mae_without_verified_liveops_bridge","source_loop73_artifact":"e2r_stock_web_v12_residual_round_R8_loop_73_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"trigger","research_id":"R13L73_HIGH_MAE_GUARDRAIL","round":"R13","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER","underlying_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","underlying_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","underlying_fine_archetype_id":"DEFENSE_EXPORT_POLICY_FRAMEWORK_SECOND_TIER_BACKLOG_AND_GEOPOLITICAL_THEME_ROUTER","symbol":"065450","name":"빅텍","trigger_type":"4B-local-watch","trigger_family":"geopolitical_defense_theme_spike_without_export_framework_bridge","trigger_date":"2024-01-17","entry_date":"2024-01-18","entry_price":6600.0,"entry_price_type":"next_tradable_open_after_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.12,"mae_30d_pct":-26.06,"mfe_90d_pct":7.12,"mae_90d_pct":-28.48,"mfe_180d_pct":7.12,"mae_180d_pct":-28.79,"peak_price_180d":7070.0,"peak_date_180d":"2024-01-18","trough_price_180d":4700.0,"trough_date_180d":"2024-07-11","calibration_usable":true,"case_polarity":"counterexample_geopolitical_theme_spike","r13_case_role":"high_mae_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":true,"expected_stage_current_profile":"4B_local_watch_or_blocked_positive_stage","residual_error_type":"geopolitical_theme_spike_low_mfe_high_mae_without_export_framework_backlog_bridge","source_loop73_artifact":"e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md"}
```

---

## 8. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R13L73_HIGH_MAE_GUARDRAIL",
  "round": "R13",
  "loop": 73,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "fine_archetype_id": "LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER",
  "case_count": 8,
  "calibration_usable_case_count": 8,
  "positive_holdout_count": 2,
  "counterexample_count": 6,
  "underlying_canonical_count": 7,
  "source_proxy_only_count": 8,
  "evidence_url_pending_count": 8,
  "avg_mfe_30d_pct": 24.89,
  "avg_mae_30d_pct": -18.96,
  "avg_mfe_90d_pct": 33.99,
  "avg_mae_90d_pct": -28.3,
  "avg_mfe_180d_pct": 57.1,
  "avg_mae_180d_pct": -37.06,
  "max_mfe_180d_pct": 289.01,
  "worst_mae_180d_pct": -65.34
}
```

---

## 9. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | bridge quality | MFE quality | MAE risk | same-window peak risk | information confidence | false-positive pressure | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `089030` | 13 | 18 | 18 | 14 | 7 | -2 | 68 | holdout positive; Yellow/Green only after customer-quality URL repair |
| `340570` | 12 | 13 | 17 | 13 | 7 | -2 | 60 | holdout positive; Yellow after commercial bridge URL repair |
| `299030` | 2 | 4 | -20 | -14 | 4 | -18 | -42 | block Stage2; 4C/high-MAE watch |
| `020150` | 2 | 3 | -20 | -12 | 4 | -19 | -42 | block Stage2; 4C/high-MAE watch |
| `017040` | 2 | 6 | -18 | -10 | 4 | -17 | -33 | 4B-to-4C high-MAE watch |
| `149980` | 2 | 1 | -18 | -15 | 4 | -18 | -44 | block Stage2; post-spike false positive |
| `225570` | 5 | 14 | -12 | -6 | 5 | -13 | -7 | Stage2-Guarded / 4B high-MAE watch |
| `065450` | 1 | 3 | -13 | -14 | 4 | -17 | -36 | local 4B / blocked positive stage |

### Score-return alignment

```text
High MFE alone is not sufficient:
  225570 had +66.31% 180D MFE but -32.51% 180D MAE.
  017040 had +23.65% 180D MFE but -53.45% 180D MAE.

Weak MFE plus high MAE is a hard fail:
  149980 had +1.30% 180D MFE and -50.97% 180D MAE.
  020150 had +5.65% 180D MFE and -60.64% 180D MAE.
  065450 had +7.12% 180D MFE and -28.79% 180D MAE.

The guardrail must preserve real winners:
  089030 and 340570 show persistent MFE with contained MAE.
```

---

## 10. Current calibrated profile stress test

The current calibrated profile already contains:

```text
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The remaining residual problem is broader than pure blowoff:

```text
A case can be non-price-plausible but still wrong as Stage2/Green
when source evidence is pending and the forward path shows high MAE.
```

The proposed R13 router should not be sector-specific. It should watch for path geometry:

```text
Geometry A — valid holdout:
  MFE_90D >= +25%
  + MAE_90D > -10%
  + evidence bridge is plausible but URL-pending
  => Stage2-Guarded / Yellow candidate after URL repair, no automatic Green

Geometry B — weak-MFE high-MAE:
  MFE_30D < +10%
  + MAE_30D <= -20% or MAE_90D <= -30%
  + evidence remains source_proxy_only
  => block Stage2 or route to 4B/4C watch

Geometry C — high-MFE high-MAE:
  MFE_30D >= +25%
  + MAE_90D <= -20% or MAE_180D <= -30%
  + bridge evidence not repaired
  => Stage2-Guarded at most, local 4B/high-MAE watch, no Green
```

---

## 11. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R13L73_HIGH_MAE_GUARDRAIL",
  "stage2_positive_or_yellow_holdouts": [
    {
      "symbol": "089030",
      "reason": "persistent +289.01% 180D MFE with only -3.52% MAE; keep open as positive after customer-quality evidence repair"
    },
    {
      "symbol": "340570",
      "reason": "persistent +52.48% 180D MFE with only -1.29% MAE; keep open after export/commercialization evidence repair"
    }
  ],
  "local_4b_high_mae_watch": [
    {
      "symbol": "225570",
      "reason": "high MFE but 90D/180D MAE crossed high-MAE guardrails; needs retention/monetization repair"
    },
    {
      "symbol": "017040",
      "reason": "theme spike with -53.45% 180D MAE; needs order/backlog bridge repair"
    },
    {
      "symbol": "065450",
      "reason": "geopolitical theme spike with immediate -26.06% 30D MAE; needs export-framework/backlog bridge"
    }
  ],
  "blocked_stage2_or_4c_watch": [
    {
      "symbol": "299030",
      "reason": "thesis-break relief attempt with -65.34% 180D MAE"
    },
    {
      "symbol": "020150",
      "reason": "utilization/call-off failure with -60.64% 180D MAE"
    },
    {
      "symbol": "149980",
      "reason": "post-spike weak-MFE entry with -50.97% 180D MAE"
    }
  ]
}
```

---

## 12. Cross-archetype rule candidate

```yaml
row_type: cross_archetype_rule_candidate
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: LOOP73_WEAK_MFE_HIGH_MAE_AND_HOLDOUT_ROUTER
rule_name: R13_loop73_source_proxy_high_mae_geometry_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For cross-archetype source_proxy_only or evidence_url_pending cases:

Tier A: holdout positive
  Conditions:
    - MFE_90D >= +25%
    - MAE_90D > -10%
    - MFE persists beyond the first event candle
    - non-price bridge is plausible and URL-repairable
  Routing:
    - Stage2-Actionable or Stage2-Guarded allowed
    - Stage3-Yellow only after evidence repair
    - Green only after URL-repaired bridge evidence exists

Tier B: weak-MFE high-MAE failure
  Conditions:
    - MFE_30D < +10%
    - MAE_30D <= -20% or MAE_90D <= -30%
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - block Stage2
    - local 4B / 4C high-MAE watch
    - count as false-positive counterexample

Tier C: high-MFE high-MAE trap
  Conditions:
    - MFE_30D >= +25%
    - MAE_90D <= -20% or MAE_180D <= -30%
    - bridge evidence is not URL-repaired
  Routing:
    - Stage2-Guarded at most
    - local 4B/high-MAE watch
    - no Green
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "r13_loop73_source_proxy_high_mae_geometry_router",
  "scope": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "yellow_green_requires_url_repaired_bridge": true,
    "holdout_positive_mfe90_min_pct": 25.0,
    "holdout_positive_mae90_min_pct": -10.0,
    "weak_mfe_threshold_30d_pct": 10.0,
    "weak_mfe_high_mae_blocks_stage2": true,
    "weak_mfe_high_mae_threshold_30d_pct": -20.0,
    "weak_mfe_high_mae_threshold_90d_pct": -30.0,
    "high_mfe_high_mae_stage2_cap": "guarded_only_until_url_repair",
    "high_mfe_high_mae_threshold_90d_pct": -20.0,
    "high_mfe_high_mae_threshold_180d_pct": -30.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium",
  "apply_now": false,
  "reason": "Loop 73 cross-archetype evidence shows two valid low-MAE holdouts and six high-MAE failures across C02/C03/C11/C13/C25/C27. The rule should preserve persistent low-MAE winners while blocking weak-MFE/high-MAE and capping high-MFE/high-MAE traps."
}
```

---

## 13. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R13L73_HIGH_MAE_GUARDRAIL",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "contribution": "Adds a loop-73 cross-archetype high-MAE geometry router. The run compares persistent low-MAE holdouts against six weak-MFE or high-MFE/high-MAE failures across grid, defense, battery equipment, battery utilization, medical device, and game IP archetypes. It proposes a shadow-only path rule that preserves low-MAE winners while blocking weak-MFE/high-MAE failures and capping high-MFE/high-MAE traps until URL-repaired bridge evidence exists.",
  "positive_holdout_added": 2,
  "counterexample_case_added": 6,
  "underlying_canonical_count": 7,
  "data_quality_blocker": "All eight non-price triggers remain evidence_url_pending=true and source_proxy_only=true until URL-level repair.",
  "guardrail_added": "source_proxy_only + weak MFE + high MAE should block Stage2; high-MFE/high-MAE traps should cap at Stage2-Guarded or local 4B until bridge evidence is repaired."
}
```

---

## 14. Validation scope

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
    089030: false
    340570: false
    299030: false
    020150: false
    017040: false
    149980: false
    225570: false
    065450: false
  evidence_url_pending:
    089030: true
    340570: true
    299030: true
    020150: true
    017040: true
    149980: true
    225570: true
    065450: true
  source_proxy_only:
    089030: true
    340570: true
    299030: true
    020150: true
    017040: true
    149980: true
    225570: true
    065450: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- This is a cross-archetype guardrail file, not a positive scoring promotion file.
- It should not be read as a current investment view.
```

---

## 15. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact.

Task:
1. Ingest the machine-readable trigger rows under R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL.
2. Preserve R13 / loop 73 metadata.
3. Preserve underlying_large_sector_id, underlying_canonical_archetype_id, and underlying_fine_archetype_id for every trigger row.
4. Treat all eight non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive Yellow/Green promotion until the underlying evidence bridges are repaired.
6. Add a shadow-only cross-archetype rule candidate named R13_loop73_source_proxy_high_mae_geometry_router.
7. Do not loosen Stage3-Green.
8. Add R13-specific guards:
   - source_proxy_only -> no Green
   - MFE_30D < +10% and MAE_30D <= -20% -> block Stage2
   - MFE_30D < +10% and MAE_90D <= -30% -> block Stage2 / 4C watch
   - MFE_30D >= +25% and MAE_90D <= -20% -> Stage2-Guarded at most
   - MFE_30D >= +25% and MAE_180D <= -30% -> local 4B/high-MAE watch, no Green
   - holdout positives require URL-repaired bridge evidence before Yellow/Green
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 16. Next round state

```text
completed_round = R13
completed_loop = 73
next_round = R1
next_loop = 74
next_large_sector_hint = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```
