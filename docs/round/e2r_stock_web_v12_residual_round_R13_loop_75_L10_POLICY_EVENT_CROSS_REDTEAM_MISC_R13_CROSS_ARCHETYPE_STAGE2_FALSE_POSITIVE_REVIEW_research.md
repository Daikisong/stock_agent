# E2R Stock-Web v12 Residual Research — R13 Loop 75

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R13
completed_loop: 75
next_round: R1
next_loop: 76
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW
output_file: e2r_stock_web_v12_residual_round_R13_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
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
completed_loop  = 75
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER
```

Therefore:

```text
scheduled_round = R13
scheduled_loop  = 75
```

R13 is a cross-archetype review round rather than a normal sector expansion round.  
This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id = LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW
```

This is a valid R13 scope.

---

## 1. Why this R13 run

Loop 75 generated many cases where the first label looked investable:

```text
grid/datacenter CAPEX
advanced semiconductor equipment
battery equipment orderbook
strategic resource policy supply
brand inventory-margin repair
financial value-up / capital return
medical device export/reimbursement
content IP / game launch
battery IRA / utilization
construction PF relief
defensive-yield value-up
low-birth childcare policy
```

The cross-archetype residual is:

```text
A plausible label is not enough.
Stage2 requires either:
  1. persistent MFE with controlled MAE, or
  2. URL-repaired non-price bridge evidence before promotion.

If the case is source_proxy_only and the forward path has weak MFE, entry-day peak, or high MAE,
the model should block Green and often block Stage2.
```

This run deliberately includes seven positive holdouts:

```text
033100 제룡전기
337930 브랜드엑스코퍼레이션
340570 티앤엘
039490 키움증권
259960 크래프톤
014790 HL D&I
013990 아가방컴퍼니
```

These prevent the R13 rule from becoming a blunt anti-theme filter.  
The nine counterexamples then define the false-positive geometry:

```text
189860 서전기전
322310 오로스테크놀로지
217820 원익피앤이
278280 천보
214680 디알텍
225570 넥슨게임즈
407400 꿈비
317530 캐리소프트
002410 범양건영
```

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

| symbol | name | underlying canonical | calibration usable | note |
|---|---|---|---|---|
| `033100` | 제룡전기 | C02 | true | no selected 2024 window corporate-action overlap |
| `337930` | 브랜드엑스코퍼레이션/젝시믹스 | C19 | true | no selected 2024 window corporate-action overlap |
| `340570` | 티앤엘 | C25 | true | no selected 2024 window corporate-action overlap |
| `039490` | 키움증권 | C21 | true | no selected 2024 window corporate-action overlap |
| `259960` | 크래프톤 | C27 | true | no selected 2024 window corporate-action overlap |
| `014790` | HL D&I | C30 | true | no selected 2024 window corporate-action overlap |
| `013990` | 아가방컴퍼니 | C31 | true | no selected 2024 window corporate-action overlap |
| `189860` | 서전기전 | C02 | true | no selected 2024 window corporate-action overlap |
| `322310` | 오로스테크놀로지 | C09 | true | no selected 2024 window corporate-action overlap |
| `217820` | 원익피앤이 | C11 | true | no selected 2024 window corporate-action overlap |
| `278280` | 천보 | C13 | true | no selected 2024 window corporate-action overlap |
| `214680` | 디알텍 | C25 | true | no selected 2024 window corporate-action overlap |
| `225570` | 넥슨게임즈 | C27 | true | no selected 2024 window corporate-action overlap |
| `407400` | 꿈비 | C31 | true | no selected 2024 window corporate-action overlap |
| `317530` | 캐리소프트 | C31 | true for 180D | 2024-11-18 candidate after selected 180D window |
| `002410` | 범양건영 | C30 | true | no selected 2024 window corporate-action overlap |

---

## 3. No-repeat and novelty check

Hard duplicate key for this R13 artifact:

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW + symbol + trigger_type + entry_date
```

Direct repository searches were performed for representative selected symbols under this R13 pseudo-archetype:

```text
013990 / 225570 / 278280 / 317530
```

Result:

```json
{
  "row_type": "novelty_check",
  "research_id": "R13L75_STAGE2_FALSE_POSITIVE_REVIEW",
  "r13_scope": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "case_count": 16,
  "underlying_canonical_count": 10,
  "symbol_count": 16,
  "positive_holdout_count": 7,
  "false_positive_or_guarded_counterexample_count": 9,
  "duplicate_status": "pass_for_r13_cross_archetype_review",
  "new_independent_case_ratio": 1.00
}
```

---

## 4. Review thesis

The cross-archetype failure shape is:

```text
source_proxy_only or evidence_url_pending
+ plausible policy/theme/event label
+ weak MFE, entry-day peak, or high MAE
= no Green; often no Stage2
```

The holdout shape is:

```text
persistent MFE
+ contained MAE
+ plausible bridge that can be URL-repaired
= Stage2-Guarded or Yellow candidate, but still not automatic Green
```

Loop 75 adds a useful distinction:

```text
High MFE is necessary but not sufficient.
The model must ask whether MFE survives the next bridge:
- order backlog and margin for grid/equipment,
- delivery and customer call-off for battery equipment/materials,
- sell-through and channel inventory for consumer/childcare,
- shareholder return and cash-flow for financial/value-up,
- retention/ARPPU/live-ops for game IP,
- PF/refinancing/working-capital for construction.
```

---

## 5. Case design

| symbol | name | underlying canonical | R13 role | 180D MFE / MAE |
|---|---|---|---|---|
| `033100` | 제룡전기 | C02_POWER_GRID_DATACENTER_CAPEX | positive holdout | +270.22% / -5.51% |
| `337930` | 브랜드엑스코퍼레이션/젝시믹스 | C19_BRAND_RETAIL_INVENTORY_MARGIN | positive holdout | +161.33% / -0.59% |
| `340570` | 티앤엘 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | positive holdout | +52.48% / -1.29% |
| `039490` | 키움증권 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | positive holdout | +36.25% / -1.68% |
| `259960` | 크래프톤 | C27_CONTENT_IP_GLOBAL_MONETIZATION | positive holdout | +37.59% / -4.10% |
| `014790` | HL D&I | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | positive holdout | +42.22% / -0.49% |
| `013990` | 아가방컴퍼니 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | positive holdout | +70.95% / -1.67% |
| `189860` | 서전기전 | C02_POWER_GRID_DATACENTER_CAPEX | false positive / guard | +0.12% / -52.55% |
| `322310` | 오로스테크놀로지 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | false positive / guard | +12.88% / -54.85% |
| `217820` | 원익피앤이 | C11_BATTERY_ORDERBOOK_RERATING | false positive / guard | +9.28% / -56.74% |
| `278280` | 천보 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | false positive / guard | +2.38% / -49.22% |
| `214680` | 디알텍 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | false positive / guard | +6.06% / -53.45% |
| `225570` | 넥슨게임즈 | C27_CONTENT_IP_GLOBAL_MONETIZATION | false positive / guard | +65.51% / -32.83% |
| `407400` | 꿈비 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | false positive / guard | +18.64% / -34.62% |
| `317530` | 캐리소프트 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | false positive / guard | +12.13% / -30.70% |
| `002410` | 범양건영 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | false positive / guard | +1.29% / -33.03% |

---

## 6. Stock-Web OHLC and backtest excerpts

### 033100 — C02 positive holdout: transformer/grid CAPEX order-margin rerating

### 6.1 `033100` 제룡전기 — small/mid transformer grid/datacenter CAPEX positive anchor

Trigger:

```text
trigger_date = 2024-03-04
trigger_type = Stage2-Actionable
trigger_family = small_mid_transformer_grid_datacenter_capex_order_margin_rerating
entry_date = 2024-03-05
entry_price = 27200.0
entry_price_type = next_tradable_open_after_transformer_capex_order_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-04,21750.0,27200.0,21750.0,27200.0,5746788.0,149308673550.0,436897524800.0,16062409,KOSDAQ
2024-03-05,27200.0,27900.0,25700.0,27300.0,2574584.0,69485465450.0,438503765700.0,16062409,KOSDAQ
2024-03-08,30300.0,33850.0,30050.0,32550.0,3911304.0,125532485250.0,522831412950.0,16062409,KOSDAQ
2024-04-04,48550.0,55500.0,48400.0,53000.0,3370262.0,178441960050.0,851307677000.0,16062409,KOSDAQ
2024-05-13,75800.0,80700.0,68300.0,71500.0,3196414.0,236886628500.0,1148462243500.0,16062409,KOSDAQ
2024-06-21,72400.0,89400.0,71700.0,84500.0,5208004.0,423812403700.0,1357273560500.0,16062409,KOSDAQ
2024-07-11,98000.0,100700.0,94300.0,95900.0,810617.0,79154020100.0,1540385023100.0,16062409,KOSDAQ
2024-08-05,65700.0,68300.0,57700.0,62400.0,932399.0,59653534700.0,1002294321600.0,16062409,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 55500 | 2024-04-04 | 25700 | 2024-03-05 | +104.04% | -5.51% |
| 90 calendar days | 80700 | 2024-05-13 | 25700 | 2024-03-05 | +196.69% | -5.51% |
| 180 calendar days | 100700 | 2024-07-11 | 25700 | 2024-03-05 | +270.22% | -5.51% |

R13 interpretation:

```text
R13 holdout. This case prevents overblocking C02: the grid/datacenter CAPEX label was not just a theme candle because MFE expanded to +270.22% while MAE stayed only -5.51%. It remains source-proxy-only, so Yellow/Green still needs order backlog, customer, delivery, capacity, and margin evidence repair.
```
### 337930 — C19 positive holdout: athleisure inventory-destock margin leverage

### 6.1 `337930` 브랜드엑스코퍼레이션/젝시믹스 — athleisure inventory-destock / margin leverage rerating

Trigger:

```text
trigger_date = 2024-05-28
trigger_type = Stage2-Actionable
trigger_family = athleisure_brand_inventory_destock_margin_operating_leverage_rerating
entry_date = 2024-05-29
entry_price = 5120.0
entry_price_type = next_tradable_open_after_athleisure_brand_margin_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-28,4985.0,5170.0,4985.0,5120.0,149762.0,762446685.0,149844935680.0,29266589,KOSDAQ
2024-05-29,5120.0,5840.0,5090.0,5750.0,1093903.0,6077965470.0,168282886750.0,29266589,KOSDAQ
2024-05-31,5680.0,6280.0,5660.0,5960.0,2018929.0,12213770740.0,174428870440.0,29266589,KOSDAQ
2024-06-24,5960.0,6900.0,5850.0,6330.0,6362602.0,41601048290.0,185257508370.0,29266589,KOSDAQ
2024-06-28,6800.0,7170.0,6700.0,6950.0,1150463.0,7997790830.0,203402793550.0,29266589,KOSDAQ
2024-07-10,8270.0,9140.0,8180.0,8520.0,3269645.0,28381894490.0,249734380440.0,29311547,KOSDAQ
2024-08-09,10820.0,12280.0,10780.0,11430.0,12992643.0,149626887540.0,335030982210.0,29311547,KOSDAQ
2024-10-07,12540.0,13380.0,11700.0,11880.0,2331468.0,29446166650.0,348221178360.0,29311547,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7170 | 2024-06-28 | 5090 | 2024-05-29 | +40.04% | -0.59% |
| 90 calendar days | 12280 | 2024-08-09 | 5090 | 2024-05-29 | +139.84% | -0.59% |
| 180 calendar days | 13380 | 2024-10-07 | 5090 | 2024-05-29 | +161.33% | -0.59% |

R13 interpretation:

```text
R13 holdout. This prevents overblocking C19: inventory-destock and brand-margin mechanics can become real operating leverage when MFE compounds and MAE stays nearly flat. Green still needs inventory, sell-through, channel, and margin evidence.
```
### 340570 — C25 positive holdout: wound-care consumable export/reorder

### 6.1 `340570` 티앤엘 — wound-care consumable export/reorder positive anchor

Trigger:

```text
trigger_date = 2024-03-18
trigger_type = Stage2-Actionable
trigger_family = woundcare_medical_consumable_export_reorder_margin_rerating
entry_date = 2024-03-19
entry_price = 50500.0
entry_price_type = next_tradable_open_after_woundcare_export_reorder_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-18,47600.0,48200.0,46600.0,47350.0,61407.0,2920744300.0,384860800000.0,8128000,KOSDAQ
2024-03-19,50500.0,52700.0,49850.0,51300.0,450689.0,23133609850.0,416966400000.0,8128000,KOSDAQ
2024-03-29,52200.0,54100.0,51600.0,53600.0,121466.0,6468531400.0,435660800000.0,8128000,KOSDAQ
2024-04-11,61000.0,63500.0,58000.0,59900.0,346955.0,21133689100.0,486867200000.0,8128000,KOSDAQ
2024-05-16,65300.0,71600.0,64100.0,70800.0,658584.0,45076416300.0,575462400000.0,8128000,KOSDAQ
2024-06-24,70000.0,74100.0,69500.0,71600.0,236914.0,17075471300.0,581964800000.0,8128000,KOSDAQ
2024-08-05,56700.0,57000.0,50400.0,53500.0,230099.0,12438957400.0,434848000000.0,8128000,KOSDAQ
2024-08-21,75800.0,77000.0,73000.0,74500.0,215649.0,16126146100.0,605536000000.0,8128000,KOSDAQ
2024-09-13,65500.0,66900.0,64900.0,66500.0,54617.0,3600090100.0,540512000000.0,8128000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 63500 | 2024-04-11 | 49850 | 2024-03-19 | +25.74% | -1.29% |
| 90 calendar days | 71600 | 2024-05-16 | 49850 | 2024-03-19 | +41.78% | -1.29% |
| 180 calendar days | 77000 | 2024-08-21 | 49850 | 2024-03-19 | +52.48% | -1.29% |

R13 interpretation:

```text
R13 holdout. This shows that a medical consumable export/reorder path can be durable: +52.48% 180D MFE with only -1.29% MAE. It remains Stage2/Yellow-after-repair, not price-only Green.
```
### 039490 — C21 positive holdout: brokerage ROE/capital-return rerating

### 6.1 `039490` 키움증권 — brokerage value-up / ROE capital-return rerating

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-Actionable
trigger_family = brokerage_valueup_roe_capital_return_low_mae_rerating
entry_date = 2024-02-02
entry_price = 107300.0
entry_price_type = next_tradable_open_after_financial_valueup_brokerage_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,96100.0,108200.0,96100.0,107600.0,300681.0,31664789100.0,2821993565600.0,26226706,KOSPI
2024-02-02,107300.0,113800.0,105500.0,112200.0,197312.0,21719104200.0,2942636413200.0,26226706,KOSPI
2024-02-23,122700.0,127500.0,121200.0,126400.0,158770.0,20017684200.0,3315055638400.0,26226706,KOSPI
2024-03-05,130100.0,135900.0,130000.0,134800.0,113712.0,15282958400.0,3535359968800.0,26226706,KOSPI
2024-03-15,133800.0,136600.0,129600.0,131300.0,107076.0,14162349900.0,3443566497800.0,26226706,KOSPI
2024-07-11,139900.0,146200.0,138100.0,144600.0,143375.0,20650017600.0,3691161687600.0,25526706,KOSPI
2024-08-05,123500.0,124000.0,115200.0,118500.0,107170.0,12829777600.0,3024914661000.0,25526706,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 127500 | 2024-02-23 | 105500 | 2024-02-02 | +18.83% | -1.68% |
| 90 calendar days | 136600 | 2024-03-15 | 105500 | 2024-02-02 | +27.31% | -1.68% |
| 180 calendar days | 146200 | 2024-07-11 | 105500 | 2024-02-02 | +36.25% | -1.68% |

R13 interpretation:

```text
R13 holdout. Brokerage value-up can work when the path has persistent MFE and tiny MAE. The lesson is not to block financial value-up broadly, but to demand ROE, capital-return, risk-asset, and earnings-quality proof.
```
### 259960 — C27 positive holdout: global game-IP live-ops rerating

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

R13 interpretation:

```text
R13 holdout. Global game-IP live-ops is different from a one-week launch spike: MFE expanded through 180D while MAE stayed contained. It keeps the C27 router from overblocking durable IP monetization.
```
### 014790 — C30 positive holdout: mid/small construction PF-relief high-MFE/low-MAE

### 6.2 `014790` HL D&I — mid/small contractor PF-policy relief high-MFE / low-MAE path

Trigger:

```text
trigger_date = 2024-06-03
trigger_type = Stage2-Actionable-Guarded
trigger_family = midsmall_contractor_pf_policy_relief_high_mfe_low_mae
entry_date = 2024-06-04
entry_price = 2025.0
entry_price_type = next_tradable_open_after_midsmall_construction_policy_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-03,2010.0,2025.0,2010.0,2025.0,68223.0,137620175.0,76663667025.0,37858601,KOSPI
2024-06-04,2025.0,2390.0,2015.0,2105.0,1688164.0,3722706085.0,79692355105.0,37858601,KOSPI
2024-06-20,2285.0,2660.0,2250.0,2395.0,3475236.0,8673943680.0,90671349395.0,37858601,KOSPI
2024-07-19,2410.0,2645.0,2360.0,2540.0,905239.0,2288707345.0,96160846540.0,37858601,KOSPI
2024-08-05,2445.0,2465.0,2210.0,2250.0,295634.0,679151525.0,85181852250.0,37858601,KOSPI
2024-08-23,2645.0,2880.0,2625.0,2870.0,371789.0,1035857620.0,108654184870.0,37858601,KOSPI
2024-12-02,2360.0,2380.0,2270.0,2320.0,57024.0,131972885.0,87831954320.0,37858601,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 2660 | 2024-06-20 | 2015 | 2024-06-04 | +31.36% | -0.49% |
| 90 calendar days | 2880 | 2024-08-23 | 2015 | 2024-06-04 | +42.22% | -0.49% |
| 180 calendar days | 2880 | 2024-08-23 | 2015 | 2024-06-04 | +42.22% | -0.49% |

R13 interpretation:

```text
R13 holdout. Construction/PF relief can sometimes reprice cleanly. This case had +42.22% MFE with only -0.49% MAE, so C30 should allow Stage2-Guarded while demanding PF/liquidity/project-margin evidence for Yellow/Green.
```
### 013990 — C31 positive holdout: low-birth childcare policy theme high-MFE

### 6.1 `013990` 아가방컴퍼니 — low-birth childcare brand policy-theme high-MFE holdout

Trigger:

```text
trigger_date = 2024-01-02
trigger_type = Stage2-Actionable-Guarded
trigger_family = low_birth_policy_childcare_brand_theme_high_mfe_low_mae_entry
entry_date = 2024-01-03
entry_price = 4200.0
entry_price_type = next_tradable_open_after_low_birth_childcare_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-02,3945.0,4335.0,3935.0,4335.0,4043998.0,16850363895.0,142567468560.0,32887536,KOSDAQ
2024-01-03,4200.0,5630.0,4130.0,5630.0,27999034.0,144862786370.0,185156827680.0,32887536,KOSDAQ
2024-01-04,6020.0,6180.0,5550.0,5680.0,38385383.0,223788377330.0,186801204480.0,32887536,KOSDAQ
2024-01-18,7040.0,7180.0,6000.0,6140.0,26729185.0,180027315740.0,201929471040.0,32887536,KOSDAQ
2024-02-29,6090.0,6940.0,6090.0,6450.0,23866582.0,157666474260.0,212124607200.0,32887536,KOSDAQ
2024-04-02,5110.0,5120.0,4925.0,5010.0,589074.0,2944556875.0,164766555360.0,32887536,KOSDAQ
2024-06-28,4650.0,4750.0,4570.0,4645.0,698571.0,3253014220.0,152762604720.0,32887536,KOSDAQ
2024-07-01,4715.0,4905.0,4700.0,4840.0,1122692.0,5414296525.0,159175674240.0,32887536,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7180 | 2024-01-18 | 4130 | 2024-01-03 | +70.95% | -1.67% |
| 90 calendar days | 7180 | 2024-01-18 | 4130 | 2024-01-03 | +70.95% | -1.67% |
| 180 calendar days | 7180 | 2024-01-18 | 4130 | 2024-01-03 | +70.95% | -1.67% |

R13 interpretation:

```text
R13 holdout. Low-birth policy themes can generate real MFE. The correct rule is not blanket rejection; it is Stage2-Guarded with a requirement for policy execution, sell-through, channel, and margin evidence.
```
### 189860 — C02 false positive: switchgear/grid theme spike already spent

### 6.3 `189860` 서전기전 — switchgear/grid theme spike without order bridge

Trigger:

```text
trigger_date = 2024-05-28
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = switchgear_grid_theme_spike_without_order_margin_bridge
entry_date = 2024-05-29
entry_price = 8440.0
entry_price_type = next_tradable_open_after_switchgear_grid_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-28,6000.0,7730.0,5890.0,7730.0,4518862.0,31274314530.0,74971569400.0,9698780,KOSDAQ
2024-05-29,8440.0,8450.0,7020.0,7020.0,4099236.0,31858595710.0,68085435600.0,9698780,KOSDAQ
2024-06-04,6560.0,6570.0,6190.0,6300.0,421143.0,2654555600.0,61102314000.0,9698780,KOSDAQ
2024-06-24,5800.0,5800.0,5550.0,5610.0,87048.0,492315720.0,54410155800.0,9698780,KOSDAQ
2024-08-05,5350.0,5350.0,4510.0,4805.0,175594.0,870204975.0,46602637900.0,9698780,KOSDAQ
2024-10-11,4110.0,4145.0,4005.0,4080.0,32619.0,132744140.0,39571022400.0,9698780,KOSDAQ
2024-11-25,4860.0,4860.0,4695.0,4770.0,37056.0,175790985.0,46263180600.0,9698780,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8450 | 2024-05-29 | 5550 | 2024-06-24 | +0.12% | -34.24% |
| 90 calendar days | 8450 | 2024-05-29 | 4510 | 2024-08-05 | +0.12% | -46.56% |
| 180 calendar days | 8450 | 2024-05-29 | 4005 | 2024-10-11 | +0.12% | -52.55% |

R13 interpretation:

```text
R13 false positive. The switchgear/grid theme peaked on the entry day and then suffered -52.55% 180D MAE. This is the archetypal label-only small-cap theme spike that should block Stage2.
```
### 322310 — C09 false positive: advanced metrology entry-day peak/high-MAE

### 6.2 `322310` 오로스테크놀로지 — overlay metrology entry-day peak / high-MAE counterexample

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = overlay_metrology_equipment_theme_spike_without_order_bridge
entry_date = 2024-02-27
entry_price = 36100.0
entry_price_type = next_tradable_open_after_overlay_metrology_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,34200.0,36900.0,33000.0,35450.0,372773.0,13275844750.0,332043913900.0,9366542,KOSDAQ
2024-02-27,36100.0,40750.0,34050.0,37200.0,1848333.0,70098981500.0,348435362400.0,9366542,KOSDAQ
2024-03-14,33700.0,33700.0,32300.0,32850.0,141358.0,4630580600.0,307690904700.0,9366542,KOSDAQ
2024-04-23,28200.0,28400.0,27000.0,27000.0,159341.0,4390267450.0,252896634000.0,9366542,KOSDAQ
2024-05-27,24700.0,25050.0,23750.0,24400.0,150441.0,3642403950.0,228543624800.0,9366542,KOSDAQ
2024-07-04,22500.0,27050.0,22400.0,26600.0,931713.0,23726250100.0,249150017200.0,9366542,KOSDAQ
2024-08-05,19950.0,19980.0,16300.0,16860.0,178735.0,3261903150.0,157919898120.0,9366542,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 40750 | 2024-02-27 | 32300 | 2024-03-14 | +12.88% | -10.53% |
| 90 calendar days | 40750 | 2024-02-27 | 23750 | 2024-05-27 | +12.88% | -34.21% |
| 180 calendar days | 40750 | 2024-02-27 | 16300 | 2024-08-05 | +12.88% | -54.85% |

R13 interpretation:

```text
R13 false positive. Advanced equipment relevance was plausible, but the peak occurred on the entry day and 180D MAE reached -54.85%. C09 needs an entry-peak/high-MAE brake.
```
### 217820 — C11 false positive: formation equipment weak-MFE extreme-MAE

### 6.2 `217820` 원익피앤이 — formation equipment relief spike with extreme MAE

Trigger:

```text
trigger_date = 2024-02-14
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_formation_equipment_orderbook_relief_weak_mfe_high_mae
entry_date = 2024-02-15
entry_price = 6680.0
entry_price_type = next_tradable_open_after_formation_equipment_relief_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-14,6200.0,6630.0,6200.0,6580.0,1172900.0,7639943920.0,312250998220.0,47454559,KOSDAQ
2024-02-15,6680.0,7300.0,6580.0,6870.0,4446465.0,31202272170.0,326012820330.0,47454559,KOSDAQ
2024-03-05,5740.0,5810.0,5650.0,5710.0,274357.0,1561530240.0,270965531890.0,47454559,KOSDAQ
2024-05-14,5030.0,5120.0,5010.0,5050.0,98743.0,498114510.0,239645522950.0,47454559,KOSDAQ
2024-06-18,4720.0,4780.0,4530.0,4530.0,314776.0,1453316600.0,214969152270.0,47454559,KOSDAQ
2024-08-05,3650.0,3650.0,2890.0,3045.0,303407.0,991845210.0,144499132155.0,47454559,KOSDAQ
2024-09-06,3025.0,3045.0,2935.0,2945.0,82552.0,244391215.0,139753676255.0,47454559,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7300 | 2024-02-15 | 5650 | 2024-03-05 | +9.28% | -15.42% |
| 90 calendar days | 7300 | 2024-02-15 | 5010 | 2024-05-14 | +9.28% | -25.00% |
| 180 calendar days | 7300 | 2024-02-15 | 2890 | 2024-08-05 | +9.28% | -56.74% |

R13 interpretation:

```text
R13 false positive. The battery equipment/orderbook label existed, but MFE stayed below +10% and 180D MAE reached -56.74%. Stage2 should require customer/order/delivery/margin bridge evidence.
```
### 278280 — C13 false positive: electrolyte utilization weak-MFE extreme-MAE

### 6.3 `278280` 천보 — electrolyte additive recovery label with weak MFE and extreme MAE

Trigger:

```text
trigger_date = 2024-02-21
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = electrolyte_additive_utilization_recovery_weak_mfe_extreme_mae
entry_date = 2024-02-22
entry_price = 96500.0
entry_price_type = next_tradable_open_after_electrolyte_utilization_recovery_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-21,90800.0,99800.0,90000.0,95600.0,164733.0,15846436600.0,956000000000.0,10000000,KOSDAQ GLOBAL
2024-02-22,96500.0,98800.0,95100.0,97700.0,102695.0,10006757900.0,977000000000.0,10000000,KOSDAQ GLOBAL
2024-03-15,89100.0,89200.0,86200.0,86400.0,63835.0,5550171500.0,864000000000.0,10000000,KOSDAQ GLOBAL
2024-04-19,72400.0,72800.0,71200.0,71700.0,24849.0,1782264100.0,717000000000.0,10000000,KOSDAQ GLOBAL
2024-06-12,79100.0,82200.0,77800.0,78000.0,66521.0,5289492600.0,780000000000.0,10000000,KOSDAQ GLOBAL
2024-08-05,60600.0,60800.0,49000.0,50400.0,99184.0,5352917450.0,504000000000.0,10000000,KOSDAQ
2024-10-07,62700.0,65500.0,62300.0,65300.0,42212.0,2727560900.0,653000000000.0,10000000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 98800 | 2024-02-22 | 86200 | 2024-03-15 | +2.38% | -10.67% |
| 90 calendar days | 98800 | 2024-02-22 | 71200 | 2024-04-19 | +2.38% | -26.22% |
| 180 calendar days | 98800 | 2024-02-22 | 49000 | 2024-08-05 | +2.38% | -49.22% |

R13 interpretation:

```text
R13 false positive. Battery utilization recovery had almost no forward MFE and almost -50% 180D MAE. This is a clean weak-MFE high-MAE materials utilization failure.
```
### 214680 — C25 false positive: X-ray detector export theme weak-MFE extreme-MAE

### 6.3 `214680` 디알텍 — digital X-ray detector export-theme spike

Trigger:

```text
trigger_date = 2024-07-15
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = digital_xray_detector_export_theme_spike_high_mae
entry_date = 2024-07-16
entry_price = 4290.0
entry_price_type = next_tradable_open_after_xray_detector_export_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-15,3965.0,4465.0,3855.0,4145.0,26550964.0,111571474250.0,305598862660.0,73727108,KOSDAQ
2024-07-16,4290.0,4290.0,4100.0,4130.0,7161123.0,29945926175.0,304492956040.0,73727108,KOSDAQ
2024-07-19,4480.0,4550.0,3860.0,3860.0,11516003.0,49089894245.0,284586636880.0,73727108,KOSDAQ
2024-08-05,3490.0,3490.0,2840.0,2975.0,3216798.0,10205988105.0,219338146300.0,73727108,KOSDAQ
2024-09-09,2670.0,2880.0,2655.0,2805.0,770384.0,2099520025.0,206804537940.0,73727108,KOSDAQ
2024-10-07,3080.0,3460.0,3020.0,3275.0,22808670.0,75762110650.0,241456278700.0,73727108,KOSDAQ
2024-12-09,2115.0,2170.0,1997.0,1997.0,1588998.0,3226046034.0,147796480238.0,74009254,KOSDAQ
2025-01-10,2415.0,2415.0,2345.0,2355.0,314371.0,744059275.0,174305923170.0,74015254,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 4550 | 2024-07-19 | 2840 | 2024-08-05 | +6.06% | -33.80% |
| 90 calendar days | 4550 | 2024-07-19 | 2655 | 2024-09-09 | +6.06% | -38.11% |
| 180 calendar days | 4550 | 2024-07-19 | 1997 | 2024-12-09 | +6.06% | -53.45% |

R13 interpretation:

```text
R13 false positive. The medical X-ray/export theme produced only +6.06% MFE and -53.45% 180D MAE. Export/reimbursement labels need actual order/channel/margin evidence.
```
### 225570 — C27 guarded counterexample: new-title launch high-MFE later-MAE

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

R13 interpretation:

```text
R13 guarded counterexample. The launch had huge MFE, but later MAE reached -32.83%. C27 must distinguish launch traffic from retention, ARPPU, live-ops, and margin durability.
```
### 407400 — C31 false positive: childcare product entry-day peak/high-MAE

### 6.3 `407400` 꿈비 — childcare product entry-day peak / high-MAE counterexample

Trigger:

```text
trigger_date = 2024-01-02
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = low_birth_policy_childcare_product_entry_day_peak_high_mae
entry_date = 2024-01-03
entry_price = 12390.0
entry_price_type = next_tradable_open_after_low_birth_childcare_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-02,12170.0,12600.0,12040.0,12600.0,980913.0,12135125130.0,154469372400.0,12259474,KOSDAQ
2024-01-03,12390.0,14700.0,12230.0,13410.0,8097482.0,110708948340.0,164399546340.0,12259474,KOSDAQ
2024-01-04,13540.0,13650.0,12520.0,12810.0,1486101.0,19297293900.0,157043861940.0,12259474,KOSDAQ
2024-02-01,10070.0,10190.0,9740.0,9980.0,134012.0,1332275460.0,122349550520.0,12259474,KOSDAQ
2024-03-20,9290.0,10960.0,9290.0,10150.0,5042367.0,52405637070.0,124433661100.0,12259474,KOSDAQ
2024-04-08,8310.0,8350.0,8100.0,8210.0,68262.0,558961640.0,100650281540.0,12259474,KOSDAQ
2024-07-01,8840.0,9570.0,8820.0,9240.0,1858802.0,17208583220.0,113277539760.0,12259474,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 14700 | 2024-01-03 | 9740 | 2024-02-01 | +18.64% | -21.39% |
| 90 calendar days | 14700 | 2024-01-03 | 8920 | 2024-04-02 | +18.64% | -28.01% |
| 180 calendar days | 14700 | 2024-01-03 | 8100 | 2024-04-08 | +18.64% | -34.62% |

R13 interpretation:

```text
R13 false positive. The childcare policy theme peaked on entry day and produced high MAE immediately. Low-birth policy relevance alone should not create Stage2.
```
### 317530 — C31 false positive: kids-content policy label weak-MFE/high-MAE

### 6.4 `317530` 캐리소프트 — kids-content policy label with weak-MFE / high-MAE

Trigger:

```text
trigger_date = 2024-01-02
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = low_birth_policy_kids_content_theme_weak_mfe_high_mae
entry_date = 2024-01-03
entry_price = 5440.0
entry_price_type = next_tradable_open_after_low_birth_kids_content_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-02,5140.0,5370.0,5130.0,5370.0,68766.0,361490650.0,37435322520.0,6971196,KOSDAQ
2024-01-03,5440.0,5970.0,5240.0,5650.0,517199.0,2951411870.0,39387257400.0,6971196,KOSDAQ
2024-01-04,5950.0,6000.0,5510.0,5590.0,198752.0,1137136760.0,38968985640.0,6971196,KOSDAQ
2024-02-02,4600.0,4700.0,4455.0,4670.0,15908.0,73674570.0,32555485320.0,6971196,KOSDAQ
2024-02-21,4740.0,6100.0,4740.0,5190.0,2767024.0,15921831675.0,36180507240.0,6971196,KOSDAQ
2024-04-02,4875.0,4875.0,4600.0,4700.0,16740.0,78335305.0,32764621200.0,6971196,KOSDAQ
2024-07-01,3965.0,4150.0,3770.0,3880.0,132617.0,519884670.0,27048240480.0,6971196,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6000 | 2024-01-04 | 4455 | 2024-02-02 | +10.29% | -18.11% |
| 90 calendar days | 6100 | 2024-02-21 | 4455 | 2024-02-02 | +12.13% | -18.11% |
| 180 calendar days | 6100 | 2024-02-21 | 3770 | 2024-07-01 | +12.13% | -30.70% |

R13 interpretation:

```text
R13 false positive. Kids-content policy adjacency produced weak MFE and -30.70% 180D MAE. The missing link is monetization or policy execution, not the policy label itself.
```
### 002410 — C30 false positive: PF relief weak-MFE slow fade

### 6.4 `002410` 범양건영 — weak-MFE small-contractor PF slow fade

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = small_contractor_low_pbr_pf_relief_weak_mfe_slow_fade
entry_date = 2024-02-02
entry_price = 1780.0
entry_price_type = next_tradable_open_after_small_contractor_low_pbr_pf_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,1767.0,1784.0,1750.0,1767.0,36120.0,63933427.0,43878112194.0,24831982,KOSPI
2024-02-02,1780.0,1803.0,1767.0,1787.0,61197.0,109390158.0,44374751834.0,24831982,KOSPI
2024-02-28,1668.0,1721.0,1668.0,1721.0,67810.0,115183488.0,42735841022.0,24831982,KOSPI
2024-03-05,1701.0,1709.0,1667.0,1667.0,167138.0,283788467.0,41394913994.0,24831982,KOSPI
2024-04-08,1399.0,1432.0,1367.0,1421.0,168953.0,235660026.0,35286246422.0,24831982,KOSPI
2024-07-03,1259.0,1262.0,1192.0,1233.0,109604.0,133177832.0,30617833806.0,24831982,KOSPI
2024-07-30,1404.0,1572.0,1364.0,1376.0,1151067.0,1708707433.0,34168807232.0,24831982,KOSPI
2024-08-05,1323.0,1347.0,1198.0,1198.0,199593.0,254521880.0,29748714436.0,24831982,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 1803 | 2024-02-02 | 1668 | 2024-02-28 | +1.29% | -6.29% |
| 90 calendar days | 1803 | 2024-02-02 | 1367 | 2024-04-08 | +1.29% | -23.20% |
| 180 calendar days | 1803 | 2024-02-02 | 1192 | 2024-07-03 | +1.29% | -33.03% |

R13 interpretation:

```text
R13 false positive. This is the quiet PF slow-fade failure: MFE stayed near +1% while MAE widened. Stage2 can fail by not rerating, not only by crashing.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","underlying_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","underlying_fine_archetype_id":"SMALL_MID_TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_AND_THEME_SPIKE_ROUTER","symbol":"033100","name":"제룡전기","trigger_type":"Stage2-Actionable","trigger_family":"small_mid_transformer_grid_datacenter_capex_order_margin_rerating","trigger_date":"2024-03-04","entry_date":"2024-03-05","entry_price":27200.0,"entry_price_type":"next_tradable_open_after_transformer_capex_order_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":104.04,"mae_30d_pct":-5.51,"mfe_90d_pct":196.69,"mae_90d_pct":-5.51,"mfe_180d_pct":270.22,"mae_180d_pct":-5.51,"peak_price_180d":100700.0,"peak_date_180d":"2024-07-11","trough_price_180d":25700.0,"trough_date_180d":"2024-03-05","calibration_usable":true,"case_polarity":"positive_anchor_transformer_low_mae","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_transformer_order_backlog_margin_bridge_repaired","residual_error_type":"positive_transformer_capex_path_requires_url_repaired_order_backlog_customer_margin_evidence_before_green","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R1_loop_75_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","underlying_canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","underlying_fine_archetype_id":"APPAREL_ATHLEISURE_BRAND_INVENTORY_DESTOCK_MARGIN_AND_WEAK_MFE_ROUTER","symbol":"337930","name":"브랜드엑스코퍼레이션/젝시믹스","trigger_type":"Stage2-Actionable","trigger_family":"athleisure_brand_inventory_destock_margin_operating_leverage_rerating","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":5120.0,"entry_price_type":"next_tradable_open_after_athleisure_brand_margin_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":40.04,"mae_30d_pct":-0.59,"mfe_90d_pct":139.84,"mae_90d_pct":-0.59,"mfe_180d_pct":161.33,"mae_180d_pct":-0.59,"peak_price_180d":13380.0,"peak_date_180d":"2024-10-07","trough_price_180d":5090.0,"trough_date_180d":"2024-05-29","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_brand_margin","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_inventory_destock_sellthrough_margin_bridge_repaired","residual_error_type":"positive_athleisure_brand_margin_path_requires_url_repaired_inventory_sellthrough_channel_margin_bridge_before_green","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R5_loop_75_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","underlying_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","underlying_fine_archetype_id":"AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER","symbol":"340570","name":"티앤엘","trigger_type":"Stage2-Actionable","trigger_family":"woundcare_medical_consumable_export_reorder_margin_rerating","trigger_date":"2024-03-18","entry_date":"2024-03-19","entry_price":50500.0,"entry_price_type":"next_tradable_open_after_woundcare_export_reorder_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":25.74,"mae_30d_pct":-1.29,"mfe_90d_pct":41.78,"mae_90d_pct":-1.29,"mfe_180d_pct":52.48,"mae_180d_pct":-1.29,"peak_price_180d":77000.0,"peak_date_180d":"2024-08-21","trough_price_180d":49850.0,"trough_date_180d":"2024-03-19","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_medical_consumable_export","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_export_reorder_margin_bridge_repaired","residual_error_type":"positive_woundcare_consumable_export_path_requires_url_repaired_export_reorder_customer_margin_evidence_before_green","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R7_loop_75_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","underlying_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","underlying_fine_archetype_id":"BROKERAGE_CAPITAL_RETURN_ROE_VALUEUP_AND_WEAK_MFE_BALANCE_SHEET_ROUTER","symbol":"039490","name":"키움증권","trigger_type":"Stage2-Actionable","trigger_family":"brokerage_valueup_roe_capital_return_low_mae_rerating","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":107300.0,"entry_price_type":"next_tradable_open_after_financial_valueup_brokerage_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.83,"mae_30d_pct":-1.68,"mfe_90d_pct":27.31,"mae_90d_pct":-1.68,"mfe_180d_pct":36.25,"mae_180d_pct":-1.68,"peak_price_180d":146200.0,"peak_date_180d":"2024-07-11","trough_price_180d":105500.0,"trough_date_180d":"2024-02-02","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_brokerage_valueup","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_roe_capital_return_earnings_quality_bridge_repaired","residual_error_type":"positive_brokerage_valueup_path_requires_url_repaired_roe_shareholder_return_and_earnings_quality_bridge_before_green","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R6_loop_75_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","underlying_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","underlying_fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_LAUNCH_AND_BLOCKCHAIN_EVENT_HIGH_MAE_ROUTER","symbol":"259960","name":"크래프톤","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"global_game_ip_liveops_earnings_reacceleration_low_mae_rerating","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":219500.0,"entry_price_type":"next_tradable_open_after_game_ip_earnings_liveops_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.93,"mae_30d_pct":-4.1,"mfe_90d_pct":23.46,"mae_90d_pct":-4.1,"mfe_180d_pct":37.59,"mae_180d_pct":-4.1,"peak_price_180d":302000.0,"peak_date_180d":"2024-07-30","trough_price_180d":210500.0,"trough_date_180d":"2024-03-06","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_global_game_ip","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_liveops_revenue_margin_cashflow_bridge_repaired","residual_error_type":"positive_global_game_ip_path_requires_url_repaired_liveops_revenue_margin_and_new_title_pipeline_bridge_before_green","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R8_loop_75_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","underlying_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","underlying_fine_archetype_id":"REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"014790","name":"HL D&I","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"midsmall_contractor_pf_policy_relief_high_mfe_low_mae","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":2025.0,"entry_price_type":"next_tradable_open_after_midsmall_construction_policy_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":31.36,"mae_30d_pct":-0.49,"mfe_90d_pct":42.22,"mae_90d_pct":-0.49,"mfe_180d_pct":42.22,"mae_180d_pct":-0.49,"peak_price_180d":2880.0,"peak_date_180d":"2024-08-23","trough_price_180d":2015.0,"trough_date_180d":"2024-06-04","calibration_usable":true,"case_polarity":"positive_guarded_high_mfe_low_mae","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_pf_liquidity_project_margin_cashflow_bridge_repaired","residual_error_type":"policy_relief_high_mfe_low_mae_path_should_not_be_overblocked_but_green_requires_balance_sheet_project_margin_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER","symbol":"013990","name":"아가방컴퍼니","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"low_birth_policy_childcare_brand_theme_high_mfe_low_mae_entry","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":4200.0,"entry_price_type":"next_tradable_open_after_low_birth_childcare_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":70.95,"mae_30d_pct":-1.67,"mfe_90d_pct":70.95,"mae_90d_pct":-1.67,"mfe_180d_pct":70.95,"mae_180d_pct":-1.67,"peak_price_180d":7180.0,"peak_date_180d":"2024-01-18","trough_price_180d":4130.0,"trough_date_180d":"2024-01-03","calibration_usable":true,"case_polarity":"positive_guarded_policy_theme_high_mfe","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_only_if_childcare_policy_execution_sellthrough_margin_bridge_repaired","residual_error_type":"low_birth_policy_theme_had_real_mfe_but_green_requires_url_repaired_childcare_demand_sellthrough_margin_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","underlying_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","underlying_fine_archetype_id":"SMALL_MID_TRANSFORMER_CABLE_SWITCHGEAR_GRID_DATACENTER_CAPEX_AND_THEME_SPIKE_ROUTER","symbol":"189860","name":"서전기전","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"switchgear_grid_theme_spike_without_order_margin_bridge","trigger_date":"2024-05-28","entry_date":"2024-05-29","entry_price":8440.0,"entry_price_type":"next_tradable_open_after_switchgear_grid_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.12,"mae_30d_pct":-34.24,"mfe_90d_pct":0.12,"mae_90d_pct":-46.56,"mfe_180d_pct":0.12,"mae_180d_pct":-52.55,"peak_price_180d":8450.0,"peak_date_180d":"2024-05-29","trough_price_180d":4005.0,"trough_date_180d":"2024-10-11","calibration_usable":true,"case_polarity":"counterexample_theme_spike_extreme_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"switchgear_grid_theme_entry_spent_upside_on_entry_day_and_failed_without_order_backlog_margin_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R1_loop_75_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","underlying_canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","underlying_fine_archetype_id":"ADVANCED_METROLOGY_INSPECTION_ORDER_BRIDGE_AND_VALUATION_BLOWOFF_ROUTER","symbol":"322310","name":"오로스테크놀로지","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"overlay_metrology_equipment_theme_spike_without_order_bridge","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":36100.0,"entry_price_type":"next_tradable_open_after_overlay_metrology_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":12.88,"mae_30d_pct":-10.53,"mfe_90d_pct":12.88,"mae_90d_pct":-34.21,"mfe_180d_pct":12.88,"mae_180d_pct":-54.85,"peak_price_180d":40750.0,"peak_date_180d":"2024-02-27","trough_price_180d":16300.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_entry_day_peak_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"overlay_metrology_theme_spike_peaked_on_entry_day_and_failed_without_order_customer_margin_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","underlying_canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","underlying_fine_archetype_id":"SECOND_TIER_BATTERY_EQUIPMENT_ORDERBOOK_BRIDGE_AND_HIGH_MAE_ROUTER","symbol":"217820","name":"원익피앤이","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_formation_equipment_orderbook_relief_weak_mfe_high_mae","trigger_date":"2024-02-14","entry_date":"2024-02-15","entry_price":6680.0,"entry_price_type":"next_tradable_open_after_formation_equipment_relief_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":9.28,"mae_30d_pct":-15.42,"mfe_90d_pct":9.28,"mae_90d_pct":-25.0,"mfe_180d_pct":9.28,"mae_180d_pct":-56.74,"peak_price_180d":7300.0,"peak_date_180d":"2024-02-15","trough_price_180d":2890.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_customer_order_margin_bridge_repaired","residual_error_type":"formation_equipment_orderbook_relief_had_weak_mfe_and_extreme_mae_without_customer_delivery_margin_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R3_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","underlying_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","underlying_fine_archetype_id":"COPPER_FOIL_CATHODE_ELECTROLYTE_UTILIZATION_IRA_AMPC_AND_HIGH_MAE_ROUTER","symbol":"278280","name":"천보","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"electrolyte_additive_utilization_recovery_weak_mfe_extreme_mae","trigger_date":"2024-02-21","entry_date":"2024-02-22","entry_price":96500.0,"entry_price_type":"next_tradable_open_after_electrolyte_utilization_recovery_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.38,"mae_30d_pct":-10.67,"mfe_90d_pct":2.38,"mae_90d_pct":-26.22,"mfe_180d_pct":2.38,"mae_180d_pct":-49.22,"peak_price_180d":98800.0,"peak_date_180d":"2024-02-22","trough_price_180d":49000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"electrolyte_utilization_recovery_label_had_weak_mfe_and_extreme_mae_without_customer_volume_margin_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R9_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","underlying_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","underlying_fine_archetype_id":"AESTHETIC_DEVICE_WOUNDCARE_XRAY_EXPORT_REIMBURSEMENT_AND_HIGH_MAE_ROUTER","symbol":"214680","name":"디알텍","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"digital_xray_detector_export_theme_spike_high_mae","trigger_date":"2024-07-15","entry_date":"2024-07-16","entry_price":4290.0,"entry_price_type":"next_tradable_open_after_xray_detector_export_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.06,"mae_30d_pct":-33.8,"mfe_90d_pct":6.06,"mae_90d_pct":-38.11,"mfe_180d_pct":6.06,"mae_180d_pct":-53.45,"peak_price_180d":4550.0,"peak_date_180d":"2024-07-19","trough_price_180d":1997.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"xray_detector_export_theme_spike_had_weak_mfe_and_extreme_mae_without_export_order_margin_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R7_loop_75_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","underlying_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","underlying_fine_archetype_id":"GAME_IP_GLOBAL_LIVEOPS_LAUNCH_AND_BLOCKCHAIN_EVENT_HIGH_MAE_ROUTER","symbol":"225570","name":"넥슨게임즈","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"new_game_launch_global_concurrency_high_mfe_later_drawdown","trigger_date":"2024-07-03","entry_date":"2024-07-04","entry_price":18700.0,"entry_price_type":"next_tradable_open_after_new_game_launch_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":61.5,"mae_30d_pct":-8.02,"mfe_90d_pct":65.51,"mae_90d_pct":-21.07,"mfe_180d_pct":65.51,"mae_180d_pct":-32.83,"peak_price_180d":30950.0,"peak_date_180d":"2024-08-09","trough_price_180d":12560.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_high_mfe_later_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_retention_monetization_margin_bridge_repaired","residual_error_type":"new_game_launch_had_large_mfe_but_later_high_mae_requires_retention_arppu_margin_bridge_before_yellow_green","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R8_loop_75_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER","symbol":"407400","name":"꿈비","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"low_birth_policy_childcare_product_entry_day_peak_high_mae","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":12390.0,"entry_price_type":"next_tradable_open_after_low_birth_childcare_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.64,"mae_30d_pct":-21.39,"mfe_90d_pct":18.64,"mae_90d_pct":-28.01,"mfe_180d_pct":18.64,"mae_180d_pct":-34.62,"peak_price_180d":14700.0,"peak_date_180d":"2024-01-03","trough_price_180d":8100.0,"trough_date_180d":"2024-04-08","calibration_usable":true,"case_polarity":"counterexample_entry_day_peak_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"low_birth_childcare_entry_day_spike_had_high_mae_without_policy_execution_or_sellthrough_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"LOW_BIRTH_CHILDCARE_POLICY_THEME_SELLTHROUGH_AND_ENTRY_SPIKE_HIGH_MAE_ROUTER","symbol":"317530","name":"캐리소프트","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"low_birth_policy_kids_content_theme_weak_mfe_high_mae","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":5440.0,"entry_price_type":"next_tradable_open_after_low_birth_kids_content_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.29,"mae_30d_pct":-18.11,"mfe_90d_pct":12.13,"mae_90d_pct":-18.11,"mfe_180d_pct":12.13,"mae_180d_pct":-30.7,"peak_price_180d":6100.0,"peak_date_180d":"2024-02-21","trough_price_180d":3770.0,"trough_date_180d":"2024-07-01","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch_until_kids_content_monetization_bridge_repaired","residual_error_type":"kids_content_policy_label_had_weak_mfe_and_high_mae_without_monetization_or_policy_execution_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R12_loop_75_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L75_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":75,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW","underlying_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","underlying_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","underlying_fine_archetype_id":"REGIONAL_CONTRACTOR_LOW_PBR_PF_REPAIR_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"002410","name":"범양건영","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"small_contractor_low_pbr_pf_relief_weak_mfe_slow_fade","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":1780.0,"entry_price_type":"next_tradable_open_after_small_contractor_low_pbr_pf_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.29,"mae_30d_pct":-6.29,"mfe_90d_pct":1.29,"mae_90d_pct":-23.2,"mfe_180d_pct":1.29,"mae_180d_pct":-33.03,"peak_price_180d":1803.0,"peak_date_180d":"2024-02-02","trough_price_180d":1192.0,"trough_date_180d":"2024-07-03","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_fade_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch","residual_error_type":"small_contractor_pf_relief_label_had_almost_no_mfe_and_later_high_mae_without_liquidity_repair_bridge","source_loop75_artifact":"e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
```

---

## 8. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R13L75_STAGE2_FALSE_POSITIVE_REVIEW",
  "round": "R13",
  "loop": 75,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "fine_archetype_id": "LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW",
  "case_count": 16,
  "calibration_usable_case_count": 16,
  "positive_holdout_count": 7,
  "false_positive_or_guarded_counterexample_count": 9,
  "underlying_canonical_count": 10,
  "source_proxy_only_count": 16,
  "evidence_url_pending_count": 16,
  "avg_mfe_30d_pct": 26.52,
  "avg_mae_30d_pct": -10.86,
  "avg_mfe_90d_pct": 41.91,
  "avg_mae_90d_pct": -17.24,
  "avg_mfe_180d_pct": 49.96,
  "avg_mae_180d_pct": -25.83,
  "max_mfe_180d_pct": 270.22,
  "worst_mae_180d_pct": -56.74
}
```

---

## 9. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | label relevance | bridge evidence | MFE quality | MAE risk control | entry-peak risk | false-positive pressure | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `033100` | 15 | 10 | 20 | 14 | 12 | -2 | 69 | Stage2/Yellow after order/margin evidence repair |
| `337930` | 13 | 10 | 18 | 15 | 13 | -2 | 67 | Stage2/Yellow after sell-through/margin evidence repair |
| `340570` | 13 | 10 | 14 | 15 | 13 | -2 | 63 | Stage2/Yellow after export-reorder evidence repair |
| `039490` | 12 | 10 | 12 | 15 | 13 | -2 | 60 | Stage2/Yellow after ROE/capital-return evidence repair |
| `259960` | 12 | 9 | 11 | 13 | 12 | -2 | 55 | Stage2/Yellow after live-ops/retention evidence repair |
| `014790` | 10 | 7 | 13 | 15 | 12 | -2 | 55 | Stage2-Guarded / Yellow after PF evidence repair |
| `013990` | 10 | 5 | 15 | 14 | 10 | -3 | 51 | Stage2-Guarded until policy/sell-through evidence repair |
| `189860` | 8 | 1 | 0 | -20 | -15 | -20 | -46 | block Stage2 / 4B-4C watch |
| `322310` | 9 | 2 | 3 | -20 | -15 | -19 | -40 | block Stage2 / 4B-4C watch |
| `217820` | 8 | 2 | 2 | -20 | -12 | -19 | -39 | block Stage2 / 4B-4C watch |
| `278280` | 8 | 2 | 0 | -19 | -13 | -19 | -41 | block Stage2 / 4B-4C watch |
| `214680` | 8 | 2 | 1 | -20 | -10 | -19 | -38 | block Stage2 / 4B-4C watch |
| `225570` | 12 | 4 | 14 | -11 | -5 | -12 | 2 | Stage2-Guarded at most / local 4B watch |
| `407400` | 9 | 2 | 5 | -13 | -15 | -18 | -30 | block Stage2 / local 4B watch |
| `317530` | 7 | 2 | 3 | -12 | -8 | -16 | -24 | block Stage2 / local 4B watch |
| `002410` | 7 | 2 | 0 | -13 | -9 | -16 | -29 | block Stage2 / weak-MFE slow-fade watch |

### Score-return alignment

```text
Positive holdouts:
  033100, 337930, 340570, 039490, 259960, 014790, and 013990 show that real MFE with contained MAE should remain promotable after evidence repair.

False-positive group:
  189860, 322310, 407400 show entry-day or near-entry peaks that spent the upside immediately.
  217820, 278280, 214680 show weak-MFE / extreme-MAE paths.
  225570 shows high-MFE launch success that still needs retention and monetization proof because later MAE widened.
  317530 shows policy adjacency without monetization.
  002410 shows quiet slow-fade failure where MFE never appears.
```

---

## 10. Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining residual is broader:

```text
A case can pass the first label test and still fail Stage2 if:
  - the peak is already near entry,
  - 90D/180D MAE crosses a high-MAE threshold,
  - MFE never expands,
  - or the required non-price bridge is still source_proxy_only.
```

Proposed loop-75 cross-archetype geometry:

```text
Geometry A — valid holdout:
  MFE_90D >= +20%
  + MAE_90D > -10%
  + MFE is not only an entry-day wick
  + bridge is plausible and URL-repairable
  => Stage2-Guarded / Yellow candidate after evidence repair

Geometry B — entry-day or first-5-day peak:
  peak occurs on entry day or first five trading days
  + MAE_30D <= -20% or MAE_90D <= -30%
  + evidence remains source_proxy_only
  => block Stage2, local 4B/4C watch

Geometry C — weak-MFE high-MAE:
  MFE_30D < +10%
  + MAE_90D <= -20% or MAE_180D <= -30%
  + no repaired bridge
  => block Stage2 or local 4B/high-MAE watch

Geometry D — high-MFE later-MAE:
  MFE_30D >= +40%
  + MAE_180D <= -30%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, no Yellow/Green

Geometry E — quiet slow fade:
  MFE_90D < +5%
  + no repaired bridge
  => block Green and usually block Stage2 even if the first drawdown is not catastrophic
```

---

## 11. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R13L75_STAGE2_FALSE_POSITIVE_REVIEW",
  "stage2_positive_or_yellow_holdouts": [
    {
      "symbol": "033100",
      "reason": "grid transformer path had +270.22% MFE with only -5.51% MAE"
    },
    {
      "symbol": "337930",
      "reason": "athleisure inventory-margin path had +161.33% MFE with only -0.59% MAE"
    },
    {
      "symbol": "340570",
      "reason": "medical consumable export path had +52.48% MFE with only -1.29% MAE"
    },
    {
      "symbol": "039490",
      "reason": "brokerage value-up path had +36.25% MFE with only -1.68% MAE"
    },
    {
      "symbol": "259960",
      "reason": "global game-IP path had +37.59% MFE with only -4.10% MAE"
    },
    {
      "symbol": "014790",
      "reason": "construction PF relief path had +42.22% MFE with only -0.49% MAE"
    },
    {
      "symbol": "013990",
      "reason": "childcare policy theme had +70.95% MFE with only -1.67% MAE"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "225570",
      "reason": "new game launch had +65.51% MFE but -32.83% 180D MAE"
    },
    {
      "symbol": "317530",
      "reason": "policy-adjacent kids content had weak +12.13% MFE and -30.70% 180D MAE"
    }
  ],
  "blocked_stage2_or_4b_4c_watch": [
    {
      "symbol": "189860",
      "reason": "entry-day peak with +0.12% MFE and -52.55% 180D MAE"
    },
    {
      "symbol": "322310",
      "reason": "entry-day peak with -54.85% 180D MAE"
    },
    {
      "symbol": "217820",
      "reason": "MFE stayed below +10% while 180D MAE reached -56.74%"
    },
    {
      "symbol": "278280",
      "reason": "MFE stayed only +2.38% while 180D MAE reached -49.22%"
    },
    {
      "symbol": "214680",
      "reason": "MFE stayed only +6.06% while 180D MAE reached -53.45%"
    },
    {
      "symbol": "407400",
      "reason": "entry-day childcare-policy peak and -34.62% 180D MAE"
    },
    {
      "symbol": "002410",
      "reason": "quiet PF slow fade with only +1.29% MFE and -33.03% 180D MAE"
    }
  ]
}
```

---

## 12. Cross-archetype rule candidate

```yaml
row_type: cross_archetype_rule_candidate
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: LOOP75_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_REVIEW
rule_name: R13_loop75_label_only_stage2_false_positive_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For source_proxy_only or evidence_url_pending trigger candidates across canonical archetypes:

Tier A: valid holdout
  Conditions:
    - MFE_90D >= +20%
    - MAE_90D > -10%
    - peak is not only an entry-day/first-5-day wick
    - non-price bridge is plausible and URL-repairable
  Routing:
    - Stage2-Actionable or Stage2-Guarded allowed
    - Stage3-Yellow only after evidence repair
    - Green only after URL-repaired bridge evidence exists

Tier B: entry-day / first-5-day peak false positive
  Conditions:
    - peak occurs on entry day or first 5 trading days
    - MAE_30D <= -20% or MAE_90D <= -30%
    - evidence remains source_proxy_only
  Routing:
    - block Stage2
    - local 4B / 4C high-MAE watch

Tier C: weak-MFE high-MAE false positive
  Conditions:
    - MFE_30D < +10%
    - MAE_90D <= -20% or MAE_180D <= -30%
    - no repaired non-price bridge
  Routing:
    - block Green
    - block Stage2 or local 4B/high-MAE watch

Tier D: high-MFE later-MAE candidate
  Conditions:
    - MFE_30D >= +40%
    - MAE_180D <= -30%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - no Yellow/Green
    - require bridge repair

Tier E: quiet slow fade
  Conditions:
    - MFE_90D < +5%
    - bridge evidence remains unrepaired
  Routing:
    - block Green
    - generally block Stage2 unless a later independent trigger appears
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "r13_loop75_label_only_stage2_false_positive_and_high_mae_router",
  "scope": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "label_relevance_alone_stage2_allowed": false,
    "yellow_green_requires_url_repaired_bridge": true,
    "holdout_positive_mfe90_min_pct": 20.0,
    "holdout_positive_mae90_min_pct": -10.0,
    "entry_spike_mae30_threshold_pct": -20.0,
    "entry_spike_mae90_threshold_pct": -30.0,
    "weak_mfe_threshold_30d_pct": 10.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "weak_mfe_hard_mae180_threshold_pct": -30.0,
    "high_mfe_later_mae_mfe30_threshold_pct": 40.0,
    "high_mfe_later_mae180_threshold_pct": -30.0,
    "quiet_slow_fade_mfe90_threshold_pct": 5.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium",
  "apply_now": false,
  "reason": "Loop 75 cross-archetype cases show seven valid holdouts and nine label-only or high-MAE failures. The rule preserves real low-MAE/persistent-MFE winners while blocking weak-MFE, entry-peak, high-MAE, and quiet slow-fade candidates without URL-repaired bridge evidence."
}
```

---

## 13. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R13L75_STAGE2_FALSE_POSITIVE_REVIEW",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "contribution": "Adds a loop-75 cross-archetype Stage2 false-positive review router. The run compares seven positive holdouts against nine label-only or high-MAE failures across C02/C09/C11/C13/C19/C21/C25/C27/C30/C31. It proposes a shadow-only rule that blocks policy/theme/event relevance from creating Stage2 or Green unless the forward price path has persistent MFE with controlled MAE or the non-price bridge is URL-repaired.",
  "positive_holdout_added": 7,
  "false_positive_or_guarded_counterexample_added": 9,
  "underlying_canonical_count": 10,
  "new_independent_case_count": 16,
  "data_quality_blocker": "All selected non-price triggers remain evidence_url_pending=true and source_proxy_only=true until URL-level repair.",
  "guardrail_added": "source_proxy_only + weak MFE, entry-day peak, later high-MAE, or quiet slow fade should block Green and often block Stage2; valid low-MAE/persistent-MFE holdouts remain Stage2-Guarded until evidence repair."
}
```

One-line contribution:

```text
This loop adds 16 cross-archetype review cases, 7 positive holdouts, and 9 false-positive/guarded counterexamples for R13/L10/R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW.
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
    033100: false
    337930: false
    340570: false
    039490: false
    259960: false
    014790: false
    013990: false
    189860: false
    322310: false
    217820: false
    278280: false
    214680: false
    225570: false
    407400: false
    317530: false
    002410: false
  evidence_url_pending:
    033100: true
    337930: true
    340570: true
    039490: true
    259960: true
    014790: true
    013990: true
    189860: true
    322310: true
    217820: true
    278280: true
    214680: true
    225570: true
    407400: true
    317530: true
    002410: true
  source_proxy_only:
    033100: true
    337930: true
    340570: true
    039490: true
    259960: true
    014790: true
    013990: true
    189860: true
    322310: true
    217820: true
    278280: true
    214680: true
    225570: true
    407400: true
    317530: true
    002410: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows in the underlying loop-75 artifacts.
- Non-price evidence is not URL-repaired in this run.
- This is a cross-archetype Stage2 false-positive review file, not a positive scoring promotion file.
- It should not be read as a current investment view.
```

---

## 15. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact.

Task:
1. Ingest the machine-readable trigger rows under R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW.
2. Preserve R13 / loop 75 metadata.
3. Preserve underlying_large_sector_id, underlying_canonical_archetype_id, and underlying_fine_archetype_id for every trigger row.
4. Treat all selected non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive Yellow/Green promotion until the underlying evidence bridges are repaired.
6. Add a shadow-only cross-archetype rule candidate named R13_loop75_label_only_stage2_false_positive_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add R13-specific guards:
   - source_proxy_only -> no Green
   - label relevance alone -> no Stage2 promotion
   - MFE_90D >= +20% and MAE_90D > -10% can remain Stage2-Guarded / Yellow watch only after evidence repair
   - entry-day or first-5-day peak with MAE_30D <= -20% or MAE_90D <= -30% -> block Stage2 / 4B-4C watch
   - MFE_30D < +10% and MAE_90D <= -20% or MAE_180D <= -30% -> block Stage2 or local 4B/high-MAE watch
   - MFE_30D >= +40% with MAE_180D <= -30% -> Stage2-Guarded at most until bridge repair
   - MFE_90D < +5% with unrepaired evidence -> quiet slow-fade counterexample
   - holdout positives require URL-repaired bridge evidence before Yellow/Green
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 16. Next round state

```text
completed_round = R13
completed_loop = 75
next_round = R1
next_loop = 76
next_large_sector_hint = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
round_schedule_status = valid
round_sector_consistency = pass
```
