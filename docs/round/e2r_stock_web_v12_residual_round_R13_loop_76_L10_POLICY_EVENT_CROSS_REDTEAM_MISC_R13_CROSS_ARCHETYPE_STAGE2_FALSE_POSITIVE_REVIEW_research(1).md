# E2R Stock-Web v12 Residual Research — R13 Loop 76

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R13
completed_loop: 76
next_round: R1
next_loop: 77
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW
output_file: e2r_stock_web_v12_residual_round_R13_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
do_not_count_as_new_case: true
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

### No-repeat index handling

The no-repeat ledger explicitly states that R13 cross-checkpoint rows are accepted as `trigger` rows but must use `do_not_count_as_new_case=true` so duplicated case weight is blocked.

```text
R13 cross checkpoint rows = trigger accepted, do_not_count_as_new_case=true
Hard duplicate key = canonical_archetype_id + symbol + trigger_type + entry_date
```

This R13 file therefore reuses already validated loop-76 sector cases as cross-archetype review evidence, but does **not** count them as new independent canonical cases.

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R12
completed_loop  = 76
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER
```

Therefore:

```text
scheduled_round = R13
scheduled_loop  = 76
```

R13 is a cross-archetype review round rather than a normal sector expansion round.  
This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id = LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW
```

This is a valid R13 scope.

---

## 1. Why this R13 run

Loop 76 generated a useful cross-sector pattern:

```text
C01 shipbuilding backlog
C10 memory equipment recovery
C12 battery customer contract / call-off risk
C15 materials spread
C18 consumer export reorder
C22 insurance rate / reserve cycle
C24 bio trial-event risk
C28 software/security contract retention
C30 construction PF balance-sheet risk
C31 policy-event value-up / education policy themes
```

The cross-archetype residual is:

```text
A plausible label is not enough.
Stage2 requires either:
  1. persistent MFE with controlled MAE, or
  2. URL-repaired non-price bridge evidence before promotion.

If the case is source_proxy_only and the forward path has weak MFE, entry-day/early peak, high MAE, or delayed MFE after early drawdown,
the model should block Green and often block Stage2.
```

This run deliberately includes eight positive holdouts:

```text
000150 두산
226950 올릭스
089030 테크윙
003960 사조대림
329180 HD현대중공업
103140 풍산
012630 HDC
307950 현대오토에버
```

These prevent the R13 rule from becoming a blunt anti-theme filter.

It then includes ten counterexamples / guarded failures:

```text
299030 하나기술
001470 삼부토건
011150 CJ씨푸드
039440 에스티아이
133750 메가엠디
091580 상신이디피
058970 엠로
057030 YBM넷
034730 SK
293780 압타바이오
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

The selected R13 rows are inherited from loop-76 artifacts whose Stock-Web 1D OHLC excerpts and 30D/90D/180D MFE/MAE calculations are embedded below.

---

## 3. No-repeat and novelty check

Hard duplicate key for this R13 artifact:

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW + symbol + trigger_type + entry_date
```

Representative repository searches were performed for the education-policy C31 names used in the immediate R12 file and returned no direct prior C31 matches:

```text
133750 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
100220 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
057030 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
289010 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
```

R13 cross-archetype rows are intentionally marked as not-new:

```json
{
  "row_type": "novelty_check",
  "research_id": "R13L76_STAGE2_FALSE_POSITIVE_REVIEW",
  "r13_scope": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "case_count": 18,
  "underlying_canonical_count": 10,
  "symbol_count": 18,
  "positive_holdout_count": 8,
  "false_positive_or_guarded_counterexample_count": 10,
  "do_not_count_as_new_case": true,
  "duplicate_status": "pass_for_r13_cross_archetype_review"
}
```

---

## 4. Review thesis

The cross-archetype failure shape is:

```text
source_proxy_only or evidence_url_pending
+ plausible policy/theme/order/event label
+ weak MFE, early peak, early high MAE, or later high MAE
= no Green; often no Stage2
```

The holdout shape is:

```text
persistent MFE
+ controlled MAE
+ plausible bridge that can be URL-repaired
= Stage2-Guarded or Yellow candidate, but still not automatic Green
```

Loop 76 adds a useful bridge taxonomy:

```text
C01 backlog label -> backlog quality, delivery, contract margin, cost pass-through
C10 memory equipment label -> customer order, qualification, delivery, margin
C11 battery orderbook label -> customer delivery, acceptance, revenue recognition, cash collection
C12 customer-contract label -> call-off schedule, volume, pass-through, working capital
C15 spread label -> inventory, pass-through, demand, product mix, margin
C18 export label -> reorder, channel inventory, overseas sell-through, product mix
C22 insurance label -> reserve adequacy, CSM/earnings quality, solvency, shareholder return
C24 bio event label -> data quality, endpoint, partner economics, regulatory path, cash runway
C28 software/security label -> contract retention, recurring revenue, deployment, churn, margin
C30 PF relief label -> PF exposure, refinancing, working capital, project margin, cash flow
C31 policy label -> company-specific execution bridge, not policy relevance alone
```

---

## 5. Case design

| symbol | name | underlying canonical | R13 role | 180D MFE / MAE |
|---|---|---|---|---|
| `000150` | 두산 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | positive holdout | +177.08% / -5.78% |
| `226950` | 올릭스 | C24_BIO_TRIAL_DATA_EVENT_RISK | positive holdout | +252.15% / -0.54% |
| `089030` | 테크윙 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | positive holdout | +172.31% / -3.08% |
| `003960` | 사조대림 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | positive holdout | +150.63% / -12.66% |
| `329180` | HD현대중공업 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | positive holdout | +101.54% / -1.45% |
| `103140` | 풍산 | C15_MATERIAL_SPREAD_SUPERCYCLE | positive holdout | +70.04% / -4.53% |
| `012630` | HDC | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | positive holdout | +41.13% / -1.60% |
| `307950` | 현대오토에버 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | positive holdout | +27.03% / -2.44% |
| `299030` | 하나기술 | C11_BATTERY_ORDERBOOK_RERATING | false positive / guard | +3.68% / -64.14% |
| `001470` | 삼부토건 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | false positive / guard | +10.83% / -61.43% |
| `011150` | CJ씨푸드 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | false positive / guard | +3.18% / -59.78% |
| `039440` | 에스티아이 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | false positive / guard | +21.49% / -46.07% |
| `133750` | 메가엠디 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | false positive / guard | +18.50% / -45.10% |
| `091580` | 상신이디피 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | false positive / guard | +10.16% / -44.39% |
| `058970` | 엠로 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | false positive / guard | +28.24% / -36.30% |
| `057030` | YBM넷 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | false positive / guard | +20.13% / -36.28% |
| `034730` | SK | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | false positive / guard | +4.18% / -31.99% |
| `293780` | 압타바이오 | C24_BIO_TRIAL_DATA_EVENT_RISK | false positive / guard | +127.46% / -27.61% |

---

## 6. Stock-Web OHLC and backtest excerpts

### 000150 — C31 positive holdout: value-up holding-company capital-allocation rerating

### 6.1 `000150` 두산 — holding-company value-up / capital-allocation positive anchor

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable
trigger_family = korea_valueup_holding_company_capital_allocation_ai_industrial_repricing_low_mae
entry_date = 2024-02-27
entry_price = 95100.0
entry_price_type = next_tradable_open_after_korea_valueup_holding_company_policy_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,99300.0,102300.0,95700.0,95900.0,164838.0,16109125728.0,1584635776500.0,16523835,KOSPI
2024-02-27,95100.0,96300.0,90200.0,90600.0,129340.0,11931220400.0,1497059451000.0,16523835,KOSPI
2024-02-28,90600.0,92400.0,89600.0,91700.0,88864.0,8068719600.0,1515235669500.0,16523835,KOSPI
2024-03-18,144300.0,163400.0,143700.0,162000.0,602761.0,93052813500.0,2676861270000.0,16523835,KOSPI
2024-05-27,208500.0,218500.0,202000.0,206500.0,315232.0,65739517300.0,3412171927500.0,16523835,KOSPI
2024-07-12,263500.0,263500.0,221000.0,237000.0,626925.0,150539605500.0,3916148895000.0,16523835,KOSPI
2024-08-05,142200.0,143000.0,122000.0,128100.0,502710.0,66626020800.0,2116703263500.0,16523835,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 163400 | 2024-03-18 | 89600 | 2024-02-28 | +71.82% | -5.78% |
| 90 calendar days | 218500 | 2024-05-27 | 89600 | 2024-02-28 | +129.76% | -5.78% |
| 180 calendar days | 263500 | 2024-07-12 | 89600 | 2024-02-28 | +177.08% | -5.78% |

R13 interpretation:

```text
R13 holdout. This case prevents overblocking C31 policy-event/value-up themes: the holding-company value-up path compounded to +177.08% 180D MFE while MAE stayed -5.78%. It still needs URL-repaired capital allocation, shareholder-return, NAV discount-release, and earnings-quality evidence before Green.
```
### 226950 — C24 positive holdout: RNA therapeutics platform/trial-event rerating

### 6.1 `226950` 올릭스 — RNA therapeutics trial-platform low-MAE persistent-MFE path

Trigger:

```text
trigger_date = 2024-07-10
trigger_type = Stage2-Actionable-Guarded
trigger_family = rna_therapeutics_trial_platform_event_low_mae_persistent_mfe
entry_date = 2024-07-11
entry_price = 9300.0
entry_price_type = next_tradable_open_after_rna_therapeutics_trial_platform_event_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-10,9370.0,9600.0,9150.0,9280.0,46951.0,435963080.0,154384474240.0,16636258,KOSDAQ
2024-07-11,9300.0,10760.0,9250.0,10410.0,236563.0,2413168640.0,173183445780.0,16636258,KOSDAQ
2024-07-22,13860.0,17300.0,13700.0,16070.0,3376252.0,53188049670.0,267344666060.0,16636258,KOSDAQ
2024-08-05,14510.0,15460.0,13060.0,13980.0,332037.0,4800417480.0,232677094620.0,16643569,KOSDAQ
2024-09-13,18100.0,19130.0,16720.0,18890.0,615363.0,11235310970.0,320635025330.0,16973797,KOSDAQ
2024-10-08,18300.0,21950.0,18300.0,21600.0,1733336.0,35854806320.0,366634015200.0,16973797,KOSDAQ
2024-10-24,30300.0,32750.0,28950.0,30100.0,843190.0,25943220450.0,518870512300.0,17238223,KOSDAQ
2025-01-07,19130.0,19130.0,17300.0,17410.0,575914.0,10258916450.0,321381165930.0,18459573,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 17300 | 2024-07-22 | 9250 | 2024-07-11 | +86.02% | -0.54% |
| 90 calendar days | 21950 | 2024-10-08 | 9250 | 2024-07-11 | +136.02% | -0.54% |
| 180 calendar days | 32750 | 2024-10-24 | 9250 | 2024-07-11 | +252.15% | -0.54% |

R13 interpretation:

```text
R13 holdout. C24 should not become a blanket anti-bio filter: this RNA/platform event produced +252.15% 180D MFE with only -0.54% MAE. The promotion gate remains trial data, endpoint credibility, partner economics, regulatory path, and cash runway.
```
### 089030 — C10 positive holdout: memory test-handler / HBM-cycle rerating

### 6.1 `089030` 테크윙 — memory test handler / HBM cycle positive anchor

Trigger:

```text
trigger_date = 2024-03-11
trigger_type = Stage2-Actionable
trigger_family = memory_test_handler_hbm_cycle_low_mae_persistent_mfe
entry_date = 2024-03-12
entry_price = 26000.0
entry_price_type = next_tradable_open_after_memory_test_handler_cycle_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-11,23350.0,24100.0,21850.0,23900.0,984145.0,22708974600.0,892752115500.0,37353645,KOSDAQ
2024-03-12,26000.0,28000.0,25200.0,26850.0,3360798.0,90473580250.0,1002945368250.0,37353645,KOSDAQ
2024-04-11,33650.0,39100.0,33350.0,38700.0,2637442.0,97864810200.0,1445586061500.0,37353645,KOSDAQ
2024-05-28,40900.0,45200.0,40550.0,43500.0,1916853.0,83046502300.0,1624883557500.0,37353645,KOSDAQ
2024-07-11,67800.0,70800.0,67200.0,68700.0,874088.0,60222114100.0,2566195411500.0,37353645,KOSDAQ
2024-08-05,41450.0,43700.0,37200.0,39150.0,2515253.0,103307240150.0,1462395201750.0,37353645,KOSDAQ
2024-09-06,32700.0,33000.0,30900.0,31700.0,1027687.0,32730488750.0,1184110546500.0,37353645,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 39100 | 2024-04-11 | 25200 | 2024-03-12 | +50.38% | -3.08% |
| 90 calendar days | 45200 | 2024-05-28 | 25200 | 2024-03-12 | +73.85% | -3.08% |
| 180 calendar days | 70800 | 2024-07-11 | 25200 | 2024-03-12 | +172.31% | -3.08% |

R13 interpretation:

```text
R13 holdout. Memory test-handler/HBM-cycle relevance was return-aligned: +172.31% 180D MFE with only -3.08% MAE. C10 should preserve this route while requiring customer/order/qualification/margin evidence for Yellow/Green.
```
### 003960 — C18 positive holdout: K-food processed seafood export-channel reorder

### 6.1 `003960` 사조대림 — K-food / processed seafood export-channel reorder positive anchor

Trigger:

```text
trigger_date = 2024-05-16
trigger_type = Stage2-Actionable
trigger_family = kfood_processed_seafood_export_channel_reorder_low_mae_rerating
entry_date = 2024-05-17
entry_price = 43850.0
entry_price_type = next_tradable_open_after_kfood_export_reorder_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-16,42450.0,45200.0,41800.0,44000.0,137202.0,6016431900.0,403236548000.0,9164467,KOSPI
2024-05-17,43850.0,47800.0,43450.0,44800.0,188049.0,8630451600.0,410568121600.0,9164467,KOSPI
2024-06-07,42950.0,42950.0,41500.0,42350.0,34328.0,1443935800.0,388115177450.0,9164467,KOSPI
2024-06-14,47450.0,61600.0,46750.0,61600.0,984182.0,55960562550.0,564531167200.0,9164467,KOSPI
2024-06-28,79600.0,94300.0,74200.0,90900.0,866950.0,74330788100.0,833050050300.0,9164467,KOSPI
2024-07-09,108500.0,109900.0,97700.0,99500.0,1307373.0,136290793500.0,911864466500.0,9164467,KOSPI
2024-08-05,62200.0,62700.0,52800.0,57700.0,283449.0,16514106100.0,528789745900.0,9164467,KOSPI
2024-11-13,39050.0,39700.0,38300.0,38300.0,31686.0,1230424200.0,350999086100.0,9164467,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 61600 | 2024-06-14 | 41500 | 2024-06-07 | +40.48% | -5.36% |
| 90 calendar days | 109900 | 2024-07-09 | 41500 | 2024-06-07 | +150.63% | -5.36% |
| 180 calendar days | 109900 | 2024-07-09 | 38300 | 2024-11-13 | +150.63% | -12.66% |

R13 interpretation:

```text
R13 holdout. K-food/export-channel relevance produced a large +150.63% MFE. Because 180D MAE later reached -12.66%, the route is positive but still bridge-gated: reorder, channel inventory, overseas sell-through, product mix, and margin evidence are required.
```
### 329180 — C01 positive holdout: large shipbuilder backlog/delivery leverage

### 6.2 `329180` HD현대중공업 — large shipbuilder backlog / delivery leverage positive anchor

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable
trigger_family = large_shipbuilder_backlog_margin_delivery_leverage_rerating
entry_date = 2024-02-27
entry_price = 110400.0
entry_price_type = next_tradable_open_after_shipbuilding_backlog_margin_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,110500.0,111400.0,109200.0,109700.0,107007.0,11779258900.0,9738410825200.0,88773116,KOSPI
2024-02-27,110400.0,115500.0,108800.0,114900.0,244823.0,27844907000.0,10200031028400.0,88773116,KOSPI
2024-03-20,122800.0,127800.0,122800.0,125800.0,172740.0,21722751500.0,11167657992800.0,88773116,KOSPI
2024-05-13,138400.0,146000.0,137200.0,143500.0,358025.0,51240585000.0,12738942146000.0,88773116,KOSPI
2024-07-26,184500.0,210000.0,183500.0,207500.0,1077171.0,214368171500.0,18420421570000.0,88773116,KOSPI
2024-08-09,221000.0,222500.0,208000.0,212000.0,323259.0,68988874000.0,18819900592000.0,88773116,KOSPI
2024-08-26,196200.0,197300.0,189200.0,191100.0,310304.0,59380385200.0,16964542467600.0,88773116,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 127800 | 2024-03-20 | 108800 | 2024-02-27 | +15.76% | -1.45% |
| 90 calendar days | 146000 | 2024-05-13 | 108800 | 2024-02-27 | +32.25% | -1.45% |
| 180 calendar days | 222500 | 2024-08-09 | 108800 | 2024-02-27 | +101.54% | -1.45% |

R13 interpretation:

```text
R13 holdout. The shipbuilding backlog/margin route had +101.54% MFE and only -1.45% MAE. This is the clean C01 proof that backlog-to-delivery conversion can be Stage2/Yellow quality after evidence repair.
```
### 103140 — C15 positive holdout: copper/material spread pass-through

### 6.1 `103140` 풍산 — copper spread / defense-ammo material pass-through positive anchor

Trigger:

```text
trigger_date = 2024-03-07
trigger_type = Stage2-Actionable
trigger_family = copper_spread_defense_ammo_material_pass_through_low_mae_rerating
entry_date = 2024-03-08
entry_price = 46400.0
entry_price_type = next_tradable_open_after_copper_spread_defense_material_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-07,45000.0,51300.0,44900.0,46100.0,1930617.0,92592720500.0,1291919215800.0,28024278,KOSPI
2024-03-08,46400.0,48700.0,46350.0,48400.0,765449.0,36607460450.0,1356375055200.0,28024278,KOSPI
2024-03-13,45300.0,45750.0,44300.0,44450.0,407219.0,18216155800.0,1245679157100.0,28024278,KOSPI
2024-04-05,53200.0,53800.0,51500.0,51700.0,341662.0,17935563600.0,1448855172600.0,28024278,KOSPI
2024-04-12,60200.0,67500.0,59600.0,61600.0,2301877.0,145094424100.0,1726295524800.0,28024278,KOSPI
2024-05-14,78100.0,78900.0,75600.0,76300.0,625384.0,48386189700.0,2138252411400.0,28024278,KOSPI
2024-08-05,53300.0,54100.0,47000.0,49400.0,499656.0,25562625600.0,1384399333200.0,28024278,KOSPI
2024-09-04,63600.0,65300.0,62200.0,64100.0,304688.0,19624025100.0,1796356219800.0,28024278,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 53800 | 2024-04-05 | 44300 | 2024-03-13 | +15.95% | -4.53% |
| 90 calendar days | 78900 | 2024-05-14 | 44300 | 2024-03-13 | +70.04% | -4.53% |
| 180 calendar days | 78900 | 2024-05-14 | 44300 | 2024-03-13 | +70.04% | -4.53% |

R13 interpretation:

```text
R13 holdout. Copper/material spread was not just a label: +70.04% 180D MFE with -4.53% MAE. It remains Green-blocked until inventory, pass-through, product mix, customer demand, and margin conversion are URL-repaired.
```
### 012630 — C30 positive holdout: housing holdco / PF relief low-MAE rerating

### 6.1 `012630` HDC — housing holdco low-PBR / PF relief low-MAE rerating

Trigger:

```text
trigger_date = 2024-01-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = housing_holdco_low_pbr_pf_relief_project_margin_low_mae_rerating
entry_date = 2024-01-29
entry_price = 6880.0
entry_price_type = next_tradable_open_after_housing_pf_low_pbr_relief_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-26,6600.0,6830.0,6600.0,6830.0,134560.0,908541750.0,408035954430.0,59741721,KOSPI
2024-01-29,6880.0,7210.0,6770.0,7170.0,272079.0,1919873380.0,428348139570.0,59741721,KOSPI
2024-02-07,8650.0,8820.0,8410.0,8810.0,458707.0,3972111550.0,526324562010.0,59741721,KOSPI
2024-03-13,7800.0,7880.0,7620.0,7840.0,126827.0,981202850.0,468375092640.0,59741721,KOSPI
2024-07-26,8820.0,9710.0,8820.0,9650.0,835390.0,7899624570.0,576507607650.0,59741721,KOSPI
2024-08-05,9650.0,9800.0,8900.0,9280.0,621155.0,5789571020.0,554403170880.0,59741721,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8820 | 2024-02-07 | 6770 | 2024-01-29 | +28.20% | -1.60% |
| 90 calendar days | 8820 | 2024-02-07 | 6770 | 2024-01-29 | +28.20% | -1.60% |
| 180 calendar days | 9710 | 2024-07-26 | 6770 | 2024-01-29 | +41.13% | -1.60% |

R13 interpretation:

```text
R13 holdout. Housing/PF relief can work when MAE is contained: +41.13% 180D MFE with only -1.60% MAE. C30 should not reject every PF-relief path, but must require PF/refinancing/cash-flow evidence.
```
### 307950 — C28 positive holdout: enterprise/vehicle software contract-retention

### 6.1 `307950` 현대오토에버 — enterprise/vehicle software contract-retention low-MAE rerating

Trigger:

```text
trigger_date = 2024-04-23
trigger_type = Stage2-Actionable-Guarded
trigger_family = enterprise_vehicle_software_contract_retention_low_mae_rerating
entry_date = 2024-04-24
entry_price = 143200.0
entry_price_type = next_tradable_open_after_enterprise_vehicle_software_contract_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-23,142000.0,143100.0,139700.0,140200.0,57161.0,8062720200.0,3844842276400.0,27423982,KOSPI
2024-04-24,143200.0,154700.0,142500.0,154200.0,413460.0,62441203600.0,4228778024400.0,27423982,KOSPI
2024-04-30,170000.0,173500.0,154000.0,154000.0,1092422.0,180095160500.0,4223293228000.0,27423982,KOSPI
2024-07-11,177600.0,181900.0,175000.0,175000.0,168755.0,30102374000.0,4799196850000.0,27423982,KOSPI
2024-08-05,151100.0,154000.0,139700.0,144500.0,178185.0,26384993600.0,3962765399000.0,27423982,KOSPI
2024-09-20,166000.0,168800.0,163700.0,165300.0,106855.0,17781638000.0,4533184224600.0,27423982,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 173500 | 2024-04-30 | 142500 | 2024-04-24 | +21.16% | -0.49% |
| 90 calendar days | 181900 | 2024-07-11 | 142500 | 2024-04-24 | +27.03% | -0.49% |
| 180 calendar days | 181900 | 2024-07-11 | 139700 | 2024-08-05 | +27.03% | -2.44% |

R13 interpretation:

```text
R13 holdout. Enterprise software contract-retention can be lower-volatility but useful: +27.03% 180D MFE with only -2.44% MAE. C28 Yellow/Green still requires recurring revenue, renewal, deployment, and margin evidence.
```
### 299030 — C11 false positive: battery equipment orderbook weak-MFE extreme-MAE

### 6.3 `299030` 하나기술 — battery formation/assembly equipment weak-MFE extreme-MAE path

Trigger:

```text
trigger_date = 2024-03-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_formation_assembly_equipment_orderbook_weak_mfe_extreme_mae
entry_date = 2024-03-11
entry_price = 67900.0
entry_price_type = next_tradable_open_after_battery_equipment_orderbook_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-08,64000.0,73100.0,61400.0,67200.0,1377695.0,95170104800.0,548392790400.0,8160607,KOSDAQ
2024-03-11,67900.0,68200.0,65300.0,66000.0,230075.0,15362079200.0,538600062000.0,8160607,KOSDAQ
2024-03-12,66000.0,70400.0,66000.0,68100.0,336558.0,23072862300.0,555737336700.0,8160607,KOSDAQ
2024-04-09,57100.0,58400.0,56100.0,56300.0,47130.0,2680527300.0,459442174100.0,8160607,KOSDAQ
2024-05-31,54500.0,56800.0,52700.0,53000.0,198430.0,10750358100.0,432512171000.0,8160607,KOSDAQ
2024-08-05,30150.0,30550.0,24350.0,25450.0,167450.0,4567850200.0,207941591850.0,8170593,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 70400 | 2024-03-12 | 56100 | 2024-04-09 | +3.68% | -17.38% |
| 90 calendar days | 70400 | 2024-03-12 | 52700 | 2024-05-31 | +3.68% | -22.39% |
| 180 calendar days | 70400 | 2024-03-12 | 24350 | 2024-08-05 | +3.68% | -64.14% |

R13 interpretation:

```text
R13 false positive. Battery equipment/orderbook relevance was not enough: MFE stayed only +3.68% while 180D MAE reached -64.14%. This is a clean weak-MFE/extreme-MAE equipment-label failure.
```
### 001470 — C30 false positive: small contractor policy/political spike high-MAE

### 6.3 `001470` 삼부토건 — political/reconstruction construction spike with high MAE

Trigger:

```text
trigger_date = 2024-02-13
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = small_contractor_political_reconstruction_pf_spike_high_mae
entry_date = 2024-02-14
entry_price = 2585.0
entry_price_type = next_tradable_open_after_small_contractor_policy_political_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-13,2155.0,2630.0,2100.0,2585.0,71228864.0,176867053360.0,528010171590.0,204259254,KOSPI
2024-02-14,2585.0,2690.0,2410.0,2570.0,36708335.0,93719951850.0,524946282780.0,204259254,KOSPI
2024-03-13,2230.0,2650.0,2210.0,2400.0,30313060.0,75168457415.0,490222209600.0,204259254,KOSPI
2024-03-15,2565.0,2865.0,2430.0,2690.0,77629103.0,208864960205.0,549457393260.0,204259254,KOSPI
2024-04-08,1670.0,1836.0,1510.0,1540.0,27138794.0,43821880838.0,314559251160.0,204259254,KOSPI
2024-08-08,1162.0,1162.0,997.0,1014.0,24310605.0,25809434098.0,226742389536.0,223611824,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 2865 | 2024-03-15 | 2210 | 2024-03-13 | +10.83% | -14.51% |
| 90 calendar days | 2865 | 2024-03-15 | 1510 | 2024-04-08 | +10.83% | -41.59% |
| 180 calendar days | 2865 | 2024-03-15 | 997 | 2024-08-08 | +10.83% | -61.43% |

R13 interpretation:

```text
R13 false positive. Construction policy/political relevance produced only +10.83% MFE and then -61.43% 180D MAE. C30 must hard-block political construction spikes without PF/cash-flow repair.
```
### 011150 — C18 false positive: late seafood export theme spike weak-MFE extreme-MAE

### 6.4 `011150` CJ씨푸드 — late seafood export theme spike with weak MFE and extreme MAE

Trigger:

```text
trigger_date = 2024-06-14
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = late_seafood_export_theme_spike_weak_mfe_extreme_mae
entry_date = 2024-06-17
entry_price = 6290.0
entry_price_type = next_tradable_open_after_late_seafood_export_theme_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-14,5140.0,6460.0,4920.0,6320.0,71598499.0,425627690990.0,227082485360.0,35930773,KOSPI
2024-06-17,6290.0,6490.0,5740.0,6040.0,22421670.0,137179192910.0,217021868920.0,35930773,KOSPI
2024-07-05,4555.0,4615.0,4460.0,4475.0,970527.0,4392922265.0,160790209175.0,35930773,KOSPI
2024-08-05,3760.0,3795.0,3270.0,3420.0,1067423.0,3803931580.0,122883243660.0,35930773,KOSPI
2024-11-13,2815.0,2900.0,2780.0,2790.0,354438.0,998486810.0,100246856670.0,35930773,KOSPI
2024-12-09,2700.0,2740.0,2530.0,2725.0,577683.0,1525563970.0,97911356425.0,35930773,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6490 | 2024-06-17 | 4460 | 2024-07-05 | +3.18% | -29.09% |
| 90 calendar days | 6490 | 2024-06-17 | 3270 | 2024-08-05 | +3.18% | -48.01% |
| 180 calendar days | 6490 | 2024-06-17 | 2530 | 2024-12-09 | +3.18% | -59.78% |

R13 interpretation:

```text
R13 false positive. The late seafood export theme peaked immediately and delivered only +3.18% MFE with -59.78% 180D MAE. C18 needs an entry-peak/late-theme high-MAE brake.
```
### 039440 — C10 false positive: memory subsystem event first-window MFE later hard-MAE

### 6.3 `039440` 에스티아이 — memory subsystem event with later hard MAE

Trigger:

```text
trigger_date = 2024-03-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = memory_subsystem_equipment_event_mfe_later_hard_mae
entry_date = 2024-03-11
entry_price = 35600.0
entry_price_type = next_tradable_open_after_memory_subsystem_equipment_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-08,36400.0,39550.0,35700.0,37000.0,2502464.0,94342914350.0,585710000000.0,15830000,KOSDAQ
2024-03-11,35600.0,41200.0,34550.0,38400.0,2960083.0,114112042350.0,607872000000.0,15830000,KOSDAQ
2024-03-13,40100.0,43250.0,38750.0,38750.0,2438199.0,99405111200.0,613412500000.0,15830000,KOSDAQ
2024-04-11,31200.0,33450.0,31100.0,33350.0,334044.0,10932590700.0,527930500000.0,15830000,KOSDAQ
2024-04-18,36100.0,42600.0,35650.0,42000.0,4000134.0,161030472100.0,664860000000.0,15830000,KOSDAQ
2024-08-05,23500.0,23700.0,20000.0,21100.0,517792.0,11552154550.0,334013000000.0,15830000,KOSDAQ
2024-09-06,20000.0,20150.0,19200.0,19400.0,281427.0,5483560740.0,307102000000.0,15830000,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 43250 | 2024-03-13 | 32050 | 2024-04-09 | +21.49% | -9.97% |
| 90 calendar days | 43250 | 2024-03-13 | 31500 | 2024-05-31 | +21.49% | -11.52% |
| 180 calendar days | 43250 | 2024-03-13 | 19200 | 2024-09-06 | +21.49% | -46.07% |

R13 interpretation:

```text
R13 false positive. Memory-equipment first-window MFE did not save the path: 180D MAE reached -46.07%. C10 should not promote without order/customer/margin bridge evidence.
```
### 133750 — C31 false positive: medical education policy moderate-MFE extreme-MAE

### 6.3 `133750` 메가엠디 — medical education policy theme moderate-MFE / extreme-MAE path

Trigger:

```text
trigger_date = 2024-02-06
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = medical_education_policy_theme_moderate_mfe_extreme_mae
entry_date = 2024-02-07
entry_price = 3000.0
entry_price_type = next_tradable_open_after_medical_education_policy_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-06,3515.0,3670.0,2975.0,2995.0,22166019.0,75820537405.0,70104195615.0,23407077,KOSDAQ
2024-02-07,3000.0,3095.0,2850.0,2850.0,1956714.0,5764157155.0,66710169450.0,23407077,KOSDAQ
2024-02-14,2690.0,3130.0,2670.0,2895.0,5608190.0,16407991630.0,67763487915.0,23407077,KOSDAQ
2024-03-05,3315.0,3555.0,3205.0,3240.0,7937414.0,26751332380.0,75838929480.0,23407077,KOSDAQ
2024-04-19,2315.0,2315.0,2205.0,2280.0,181112.0,408062175.0,53368135560.0,23407077,KOSDAQ
2024-08-05,2005.0,2035.0,1647.0,1740.0,306837.0,573536733.0,40728313980.0,23407077,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 3555 | 2024-03-05 | 2670 | 2024-02-14 | +18.50% | -11.00% |
| 90 calendar days | 3555 | 2024-03-05 | 2205 | 2024-04-19 | +18.50% | -26.50% |
| 180 calendar days | 3555 | 2024-03-05 | 1647 | 2024-08-05 | +18.50% | -45.10% |

R13 interpretation:

```text
R13 false positive. Medical education policy relevance produced only moderate MFE and -45.10% MAE. C31 education-policy themes need policy-to-revenue conversion, not only policy attention.
```
### 091580 — C12 false positive: battery-can customer relief weak-MFE high-MAE

### 6.3 `091580` 상신이디피 — battery-can customer-contract relief weak-MFE / high-MAE counterexample

Trigger:

```text
trigger_date = 2024-03-07
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = battery_can_customer_contract_relief_weak_mfe_high_mae
entry_date = 2024-03-08
entry_price = 18790.0
entry_price_type = next_tradable_open_after_battery_can_customer_relief_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-07,15950.0,19440.0,15810.0,18000.0,3526915.0,64200433390.0,245307942000.0,13628219,KOSDAQ
2024-03-08,18790.0,19320.0,17830.0,18390.0,1785418.0,33326694850.0,250622947410.0,13628219,KOSDAQ
2024-03-20,19180.0,20700.0,19070.0,19480.0,1377974.0,27512495350.0,265477706120.0,13628219,KOSDAQ
2024-05-30,14500.0,14710.0,14000.0,14550.0,94453.0,1363412030.0,195380586450.0,13428219,KOSDAQ
2024-08-05,12410.0,12450.0,10450.0,10760.0,217188.0,2454597590.0,144487636440.0,13428219,KOSDAQ
2024-09-04,11500.0,11510.0,11110.0,11310.0,62062.0,699364850.0,151873156890.0,13428219,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 20700 | 2024-03-20 | 16950 | 2024-04-05 | +10.16% | -9.79% |
| 90 calendar days | 20700 | 2024-03-20 | 14000 | 2024-05-30 | +10.16% | -25.49% |
| 180 calendar days | 20700 | 2024-03-20 | 10450 | 2024-08-05 | +10.16% | -44.39% |

R13 interpretation:

```text
R13 false positive. Battery-can customer relief showed only +10.16% MFE and -44.39% 180D MAE. C12 must require customer volume, call-off, pass-through, and margin evidence.
```
### 058970 — C28 guarded counterexample: SaaS/AI contract MFE later high-MAE

### 6.2 `058970` 엠로 — procurement SaaS / AI contract MFE with later high MAE

Trigger:

```text
trigger_date = 2024-03-20
trigger_type = Stage2-Actionable-Guarded
trigger_family = enterprise_procurement_saas_ai_contract_mfe_later_high_mae
entry_date = 2024-03-21
entry_price = 59500.0
entry_price_type = next_tradable_open_after_procurement_saas_ai_contract_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-20,57300.0,59300.0,57300.0,59000.0,67411.0,3929357300.0,661515080000.0,11212120,KOSDAQ
2024-03-21,59500.0,63600.0,59000.0,63600.0,220197.0,13591344900.0,713090832000.0,11212120,KOSDAQ
2024-03-27,70000.0,72000.0,65800.0,68000.0,422348.0,29263914300.0,762424160000.0,11212120,KOSDAQ
2024-05-31,74500.0,76300.0,72900.0,75100.0,171030.0,12784147600.0,842030212000.0,11212120,KOSDAQ
2024-08-05,46000.0,46700.0,39000.0,39700.0,311711.0,13142396350.0,445121164000.0,11212120,KOSDAQ
2024-08-08,39650.0,40300.0,37900.0,39300.0,131141.0,5114698750.0,440636316000.0,11212120,KOSDAQ
2024-09-20,48300.0,51900.0,48300.0,51500.0,106782.0,5392504900.0,610466477000.0,11853718,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 72000 | 2024-03-27 | 56200 | 2024-04-16 | +21.01% | -5.55% |
| 90 calendar days | 76300 | 2024-05-31 | 56200 | 2024-04-16 | +28.24% | -5.55% |
| 180 calendar days | 76300 | 2024-05-31 | 37900 | 2024-08-08 | +28.24% | -36.30% |

R13 interpretation:

```text
R13 guarded counterexample. SaaS/AI procurement relevance created real +28.24% MFE but later -36.30% MAE. C28 should cap this at Stage2-Guarded until contract retention, ARR, deployment, and margin evidence are repaired.
```
### 057030 — C31 guarded counterexample: online education policy initial-MFE later high-MAE

### 6.2 `057030` YBM넷 — online education policy theme initial-MFE / later-MAE branch

Trigger:

```text
trigger_date = 2024-02-06
trigger_type = Stage2-Actionable-Guarded
trigger_family = online_education_policy_theme_initial_mfe_later_drawdown
entry_date = 2024-02-07
entry_price = 4645.0
entry_price_type = next_tradable_open_after_private_education_policy_theme_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-06,5060.0,5090.0,4645.0,4645.0,637402.0,3111828110.0,75772477565.0,16312697,KOSDAQ
2024-02-07,4645.0,4690.0,4580.0,4645.0,101323.0,469399630.0,75772477565.0,16312697,KOSDAQ
2024-02-16,4525.0,4610.0,4435.0,4610.0,154861.0,700319830.0,75201533170.0,16312697,KOSDAQ
2024-02-29,4525.0,5580.0,4460.0,4905.0,8068188.0,41946005145.0,80013778785.0,16312697,KOSDAQ
2024-03-14,4605.0,4670.0,4300.0,4400.0,284356.0,1254500505.0,71775866800.0,16312697,KOSDAQ
2024-04-05,4010.0,4025.0,3910.0,4000.0,44378.0,175055340.0,65250788000.0,16312697,KOSDAQ
2024-08-05,3445.0,3530.0,2960.0,3100.0,151208.0,486065565.0,50569360700.0,16312697,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 5580 | 2024-02-29 | 4435 | 2024-02-16 | +20.13% | -4.52% |
| 90 calendar days | 5580 | 2024-02-29 | 3910 | 2024-04-05 | +20.13% | -15.82% |
| 180 calendar days | 5580 | 2024-02-29 | 2960 | 2024-08-05 | +20.13% | -36.28% |

R13 interpretation:

```text
R13 guarded counterexample. Online education policy MFE existed, but -36.28% 180D MAE blocks Yellow/Green. Paid conversion and revenue bridge matter more than the policy label.
```
### 034730 — C31 false positive: value-up holdco weak-MFE high-MAE

### 6.4 `034730` SK — value-up holding-company policy label with weak MFE and high MAE

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = korea_valueup_holding_company_policy_label_weak_mfe_high_mae
entry_date = 2024-02-27
entry_price = 188800.0
entry_price_type = next_tradable_open_after_korea_valueup_holdco_policy_label
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,199800.0,199900.0,187200.0,190200.0,436018.0,83211567300.0,13922322175800.0,73198329,KOSPI
2024-02-27,188800.0,189300.0,181600.0,185500.0,253583.0,46848898900.0,13578290029500.0,73198329,KOSPI
2024-02-29,194500.0,196700.0,188800.0,191800.0,372756.0,71298040900.0,14039439502200.0,73198329,KOSPI
2024-04-19,155100.0,157500.0,153400.0,155500.0,118931.0,18435400800.0,11382340159500.0,73198329,KOSPI
2024-05-24,149300.0,151500.0,148500.0,148800.0,126956.0,18971376500.0,10891911355200.0,73198329,KOSPI
2024-08-05,142400.0,143000.0,128400.0,131300.0,347328.0,47025691500.0,9519604903900.0,72502703,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 196700 | 2024-02-29 | 178300 | 2024-03-12 | +4.18% | -5.56% |
| 90 calendar days | 196700 | 2024-02-29 | 148500 | 2024-05-24 | +4.18% | -21.35% |
| 180 calendar days | 196700 | 2024-02-29 | 128400 | 2024-08-05 | +4.18% | -31.99% |

R13 interpretation:

```text
R13 false positive. Value-up holdco relevance peaked early and produced only +4.18% MFE against -31.99% 180D MAE. C31 should block Stage2 without portfolio restructuring/shareholder-return evidence.
```
### 293780 — C24 guarded counterexample: early-high-MAE clinical event with delayed MFE

### 6.4 `293780` 압타바이오 — clinical-event gapdown, delayed-MFE after early high MAE

Trigger:

```text
trigger_date = 2024-02-28
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = clinical_event_failure_gapdown_then_delayed_mfe_high_mae
entry_date = 2024-02-29
entry_price = 6810.0
entry_price_type = next_tradable_open_after_clinical_event_risk_gapdown
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-28,6810.0,6920.0,6770.0,6890.0,45668.0,311924880.0,153639186740.0,22298866,KOSDAQ
2024-02-29,6810.0,6850.0,4935.0,5290.0,2732136.0,14869059380.0,117961001140.0,22298866,KOSDAQ
2024-03-28,6750.0,7530.0,6730.0,7110.0,470186.0,3397292890.0,158544937260.0,22298866,KOSDAQ
2024-05-27,5300.0,5370.0,4930.0,5220.0,69263.0,358262525.0,116400080520.0,22298866,KOSDAQ
2024-07-11,12150.0,15490.0,11910.0,14600.0,4010937.0,57976859390.0,325563443600.0,22298866,KOSDAQ
2024-08-05,9980.0,9990.0,8500.0,9050.0,751207.0,6993512200.0,201804737300.0,22298866,KOSDAQ
2024-08-19,8850.0,9020.0,7400.0,8360.0,1111681.0,9103598340.0,186418519760.0,22298866,KOSDAQ
2024-08-27,8400.0,8550.0,8150.0,8240.0,111160.0,926826540.0,183742655840.0,22298866,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 7530 | 2024-03-28 | 4935 | 2024-02-29 | +10.57% | -27.53% |
| 90 calendar days | 7530 | 2024-03-28 | 4930 | 2024-05-27 | +10.57% | -27.61% |
| 180 calendar days | 15490 | 2024-07-11 | 4930 | 2024-05-27 | +127.46% | -27.61% |

R13 interpretation:

```text
R13 guarded counterexample. The later +127.46% MFE does not erase the entry’s first -27.53% 30D MAE. C24 must treat early clinical-event drawdown as local 4B unless data thesis is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"000150","name":"두산","trigger_type":"Stage2-Actionable","trigger_family":"korea_valueup_holding_company_capital_allocation_ai_industrial_repricing_low_mae","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":95100.0,"entry_price_type":"next_tradable_open_after_korea_valueup_holding_company_policy_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":71.82,"mae_30d_pct":-5.78,"mfe_90d_pct":129.76,"mae_90d_pct":-5.78,"mfe_180d_pct":177.08,"mae_180d_pct":-5.78,"peak_price_180d":263500.0,"peak_date_180d":"2024-07-12","trough_price_180d":89600.0,"trough_date_180d":"2024-02-28","calibration_usable":true,"case_polarity":"positive_anchor_valueup_holdco_low_mae","r13_case_role":"positive_holdout","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_capital_allocation_earnings_quality_shareholder_return_bridge_repaired","residual_error_type":"holding_company_valueup_path_supports_positive_route_but_green_requires_url_repaired_capital_allocation_earnings_and_shareholder_return_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R11_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","underlying_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","underlying_fine_archetype_id":"ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"226950","name":"올릭스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"rna_therapeutics_trial_platform_event_low_mae_persistent_mfe","trigger_date":"2024-07-10","entry_date":"2024-07-11","entry_price":9300.0,"entry_price_type":"next_tradable_open_after_rna_therapeutics_trial_platform_event_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":86.02,"mae_30d_pct":-0.54,"mfe_90d_pct":136.02,"mae_90d_pct":-0.54,"mfe_180d_pct":252.15,"mae_180d_pct":-0.54,"peak_price_180d":32750.0,"peak_date_180d":"2024-10-24","trough_price_180d":9250.0,"trough_date_180d":"2024-07-11","calibration_usable":true,"case_polarity":"positive_guarded_rna_platform_low_mae","r13_case_role":"positive_holdout","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_trial_data_partnering_cash_runway_bridge_repaired","residual_error_type":"rna_trial_platform_event_path_supports_positive_route_but_green_requires_url_repaired_trial_data_partnering_cash_runway_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R7_loop_76_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","underlying_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","underlying_fine_archetype_id":"MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER","symbol":"089030","name":"테크윙","trigger_type":"Stage2-Actionable","trigger_family":"memory_test_handler_hbm_cycle_low_mae_persistent_mfe","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":26000.0,"entry_price_type":"next_tradable_open_after_memory_test_handler_cycle_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":50.38,"mae_30d_pct":-3.08,"mfe_90d_pct":73.85,"mae_90d_pct":-3.08,"mfe_180d_pct":172.31,"mae_180d_pct":-3.08,"peak_price_180d":70800.0,"peak_date_180d":"2024-07-11","trough_price_180d":25200.0,"trough_date_180d":"2024-03-12","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_memory_test_handler","r13_case_role":"positive_holdout","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_customer_order_delivery_margin_bridge_repaired","residual_error_type":"memory_test_handler_cycle_path_supports_positive_route_but_green_requires_url_repaired_order_customer_margin_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","underlying_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","underlying_fine_archetype_id":"KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER","symbol":"003960","name":"사조대림","trigger_type":"Stage2-Actionable","trigger_family":"kfood_processed_seafood_export_channel_reorder_low_mae_rerating","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":43850.0,"entry_price_type":"next_tradable_open_after_kfood_export_reorder_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":40.48,"mae_30d_pct":-5.36,"mfe_90d_pct":150.63,"mae_90d_pct":-5.36,"mfe_180d_pct":150.63,"mae_180d_pct":-12.66,"peak_price_180d":109900.0,"peak_date_180d":"2024-07-09","trough_price_180d":38300.0,"trough_date_180d":"2024-11-13","calibration_usable":true,"case_polarity":"positive_anchor_kfood_export_low_mae","r13_case_role":"positive_holdout","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_export_reorder_channel_margin_bridge_repaired","residual_error_type":"kfood_processed_seafood_export_path_supports_positive_route_but_green_requires_url_repaired_reorder_channel_inventory_margin_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R5_loop_76_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","underlying_canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","underlying_fine_archetype_id":"SHIPBUILDING_ENGINE_BACKLOG_MARGIN_LOW_MAE_AND_WEAK_MFE_ROUTER","symbol":"329180","name":"HD현대중공업","trigger_type":"Stage2-Actionable","trigger_family":"large_shipbuilder_backlog_margin_delivery_leverage_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":110400.0,"entry_price_type":"next_tradable_open_after_shipbuilding_backlog_margin_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.76,"mae_30d_pct":-1.45,"mfe_90d_pct":32.25,"mae_90d_pct":-1.45,"mfe_180d_pct":101.54,"mae_180d_pct":-1.45,"peak_price_180d":222500.0,"peak_date_180d":"2024-08-09","trough_price_180d":108800.0,"trough_date_180d":"2024-02-27","calibration_usable":true,"case_polarity":"positive_anchor_large_shipbuilder_low_mae","r13_case_role":"positive_holdout","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_order_backlog_delivery_margin_bridge_repaired","residual_error_type":"large_shipbuilder_backlog_margin_path_supports_positive_route_but_green_requires_url_repaired_margin_delivery_evidence","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R1_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","underlying_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","underlying_fine_archetype_id":"COPPER_STAINLESS_NICKEL_SPREAD_PASS_THROUGH_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"103140","name":"풍산","trigger_type":"Stage2-Actionable","trigger_family":"copper_spread_defense_ammo_material_pass_through_low_mae_rerating","trigger_date":"2024-03-07","entry_date":"2024-03-08","entry_price":46400.0,"entry_price_type":"next_tradable_open_after_copper_spread_defense_material_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.95,"mae_30d_pct":-4.53,"mfe_90d_pct":70.04,"mae_90d_pct":-4.53,"mfe_180d_pct":70.04,"mae_180d_pct":-4.53,"peak_price_180d":78900.0,"peak_date_180d":"2024-05-14","trough_price_180d":44300.0,"trough_date_180d":"2024-03-13","calibration_usable":true,"case_polarity":"positive_anchor_copper_spread_low_mae","r13_case_role":"positive_holdout","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_copper_spread_inventory_pass_through_margin_bridge_repaired","residual_error_type":"copper_spread_path_supports_positive_route_but_green_requires_url_repaired_inventory_pass_through_customer_margin_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R4_loop_76_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","underlying_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","underlying_fine_archetype_id":"REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER","symbol":"012630","name":"HDC","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"housing_holdco_low_pbr_pf_relief_project_margin_low_mae_rerating","trigger_date":"2024-01-26","entry_date":"2024-01-29","entry_price":6880.0,"entry_price_type":"next_tradable_open_after_housing_pf_low_pbr_relief_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":28.2,"mae_30d_pct":-1.6,"mfe_90d_pct":28.2,"mae_90d_pct":-1.6,"mfe_180d_pct":41.13,"mae_180d_pct":-1.6,"peak_price_180d":9710.0,"peak_date_180d":"2024-07-26","trough_price_180d":6770.0,"trough_date_180d":"2024-01-29","calibration_usable":true,"case_polarity":"positive_guarded_low_mae_housing_holdco","r13_case_role":"positive_holdout","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_pf_liquidity_project_margin_cashflow_bridge_repaired","residual_error_type":"housing_holdco_low_pbr_pf_relief_path_had_low_mae_mfe_but_green_requires_url_repaired_balance_sheet_project_margin_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R10_loop_76_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","underlying_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","underlying_fine_archetype_id":"ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER","symbol":"307950","name":"현대오토에버","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"enterprise_vehicle_software_contract_retention_low_mae_rerating","trigger_date":"2024-04-23","entry_date":"2024-04-24","entry_price":143200.0,"entry_price_type":"next_tradable_open_after_enterprise_vehicle_software_contract_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.16,"mae_30d_pct":-0.49,"mfe_90d_pct":27.03,"mae_90d_pct":-0.49,"mfe_180d_pct":27.03,"mae_180d_pct":-2.44,"peak_price_180d":181900.0,"peak_date_180d":"2024-07-11","trough_price_180d":139700.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_enterprise_software_low_mae","r13_case_role":"positive_holdout","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_contract_retention_margin_and_recurring_revenue_bridge_repaired","residual_error_type":"enterprise_software_contract_retention_path_had_low_mae_but_green_requires_url_repaired_contract_retention_recurring_revenue_margin_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R8_loop_76_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","underlying_canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","underlying_fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"299030","name":"하나기술","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_formation_assembly_equipment_orderbook_weak_mfe_extreme_mae","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":67900.0,"entry_price_type":"next_tradable_open_after_battery_equipment_orderbook_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.68,"mae_30d_pct":-17.38,"mfe_90d_pct":3.68,"mae_90d_pct":-22.39,"mfe_180d_pct":3.68,"mae_180d_pct":-64.14,"peak_price_180d":70400.0,"peak_date_180d":"2024-03-12","trough_price_180d":24350.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_extreme_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_orderbook_delivery_cash_margin_bridge_repaired","residual_error_type":"battery_equipment_orderbook_label_had_weak_mfe_and_extreme_mae_without_customer_delivery_cash_margin_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R9_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","underlying_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","underlying_fine_archetype_id":"REGIONAL_HOUSING_HOLDCO_PF_RELIEF_LOW_MAE_AND_POLITICAL_SPIKE_HIGH_MAE_ROUTER","symbol":"001470","name":"삼부토건","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"small_contractor_political_reconstruction_pf_spike_high_mae","trigger_date":"2024-02-13","entry_date":"2024-02-14","entry_price":2585.0,"entry_price_type":"next_tradable_open_after_small_contractor_policy_political_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.83,"mae_30d_pct":-14.51,"mfe_90d_pct":10.83,"mae_90d_pct":-41.59,"mfe_180d_pct":10.83,"mae_180d_pct":-61.43,"peak_price_180d":2865.0,"peak_date_180d":"2024-03-15","trough_price_180d":997.0,"trough_date_180d":"2024-08-08","calibration_usable":true,"case_polarity":"counterexample_policy_political_spike_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"small_contractor_policy_political_spike_had_limited_mfe_and_extreme_mae_without_pf_liquidity_cashflow_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R10_loop_76_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","underlying_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","underlying_fine_archetype_id":"KFOOD_SEAFOOD_PROCESSED_FOOD_EXPORT_REORDER_AND_LATE_SPIKE_HIGH_MAE_ROUTER","symbol":"011150","name":"CJ씨푸드","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"late_seafood_export_theme_spike_weak_mfe_extreme_mae","trigger_date":"2024-06-14","entry_date":"2024-06-17","entry_price":6290.0,"entry_price_type":"next_tradable_open_after_late_seafood_export_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.18,"mae_30d_pct":-29.09,"mfe_90d_pct":3.18,"mae_90d_pct":-48.01,"mfe_180d_pct":3.18,"mae_180d_pct":-59.78,"peak_price_180d":6490.0,"peak_date_180d":"2024-06-17","trough_price_180d":2530.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_late_spike_weak_mfe_extreme_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"late_seafood_export_theme_spike_had_entry_peak_weak_mfe_and_extreme_mae_without_reorder_channel_margin_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R5_loop_76_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","underlying_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","underlying_fine_archetype_id":"MEMORY_TEST_CMP_SUBSYSTEM_RECOVERY_LOW_MAE_AND_HIGH_MAE_ROUTER","symbol":"039440","name":"에스티아이","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"memory_subsystem_equipment_event_mfe_later_hard_mae","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":35600.0,"entry_price_type":"next_tradable_open_after_memory_subsystem_equipment_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.49,"mae_30d_pct":-9.97,"mfe_90d_pct":21.49,"mae_90d_pct":-11.52,"mfe_180d_pct":21.49,"mae_180d_pct":-46.07,"peak_price_180d":43250.0,"peak_date_180d":"2024-03-13","trough_price_180d":19200.0,"trough_date_180d":"2024-09-06","calibration_usable":true,"case_polarity":"counterexample_first_window_mfe_later_hard_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_high_MAE_watch_until_customer_order_margin_bridge_repaired","residual_error_type":"memory_equipment_label_had_first_window_mfe_but_180d_hard_mae_blocks_yellow_green_without_order_margin_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER","symbol":"133750","name":"메가엠디","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"medical_education_policy_theme_moderate_mfe_extreme_mae","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":3000.0,"entry_price_type":"next_tradable_open_after_medical_education_policy_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":18.5,"mae_30d_pct":-11.0,"mfe_90d_pct":18.5,"mae_90d_pct":-26.5,"mfe_180d_pct":18.5,"mae_180d_pct":-45.1,"peak_price_180d":3555.0,"peak_date_180d":"2024-03-05","trough_price_180d":1647.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_moderate_mfe_extreme_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_medical_education_revenue_bridge_repaired","residual_error_type":"medical_education_policy_theme_had_only_moderate_mfe_and_extreme_mae_without_policy_to_revenue_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R12_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","underlying_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","underlying_fine_archetype_id":"ELECTROLYTE_CNT_CAN_CUSTOMER_CONTRACT_LOCALIZATION_AND_CALL_OFF_HIGH_MAE_ROUTER","symbol":"091580","name":"상신이디피","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"battery_can_customer_contract_relief_weak_mfe_high_mae","trigger_date":"2024-03-07","entry_date":"2024-03-08","entry_price":18790.0,"entry_price_type":"next_tradable_open_after_battery_can_customer_relief_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.16,"mae_30d_pct":-9.79,"mfe_90d_pct":10.16,"mae_90d_pct":-25.49,"mfe_180d_pct":10.16,"mae_180d_pct":-44.39,"peak_price_180d":20700.0,"peak_date_180d":"2024-03-20","trough_price_180d":10450.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch_until_customer_contract_volume_margin_bridge_repaired","residual_error_type":"battery_can_customer_contract_relief_had_weak_mfe_and_high_mae_without_volume_margin_and_call_off_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R3_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","underlying_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","underlying_fine_archetype_id":"ENTERPRISE_SOFTWARE_DIGITAL_ID_SECURITY_CONTRACT_RETENTION_AND_WEAK_MFE_ROUTER","symbol":"058970","name":"엠로","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"enterprise_procurement_saas_ai_contract_mfe_later_high_mae","trigger_date":"2024-03-20","entry_date":"2024-03-21","entry_price":59500.0,"entry_price_type":"next_tradable_open_after_procurement_saas_ai_contract_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":21.01,"mae_30d_pct":-5.55,"mfe_90d_pct":28.24,"mae_90d_pct":-5.55,"mfe_180d_pct":28.24,"mae_180d_pct":-36.3,"peak_price_180d":76300.0,"peak_date_180d":"2024-05-31","trough_price_180d":37900.0,"trough_date_180d":"2024-08-08","calibration_usable":true,"case_polarity":"counterexample_mfe_later_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_saas_backlog_retention_margin_bridge_repaired","residual_error_type":"enterprise_procurement_saas_ai_label_had_mfe_but_180d_mae_blocks_yellow_green_without_contract_retention_margin_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R8_loop_76_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_PRIVATE_EDUCATION_POLICY_THEME_AND_HIGH_MAE_ROUTER","symbol":"057030","name":"YBM넷","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"online_education_policy_theme_initial_mfe_later_drawdown","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":4645.0,"entry_price_type":"next_tradable_open_after_private_education_policy_theme_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":20.13,"mae_30d_pct":-4.52,"mfe_90d_pct":20.13,"mae_90d_pct":-15.82,"mfe_180d_pct":20.13,"mae_180d_pct":-36.28,"peak_price_180d":5580.0,"peak_date_180d":"2024-02-29","trough_price_180d":2960.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_initial_mfe_later_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_local_4B_watch_until_enrollment_platform_revenue_bridge_repaired","residual_error_type":"online_education_policy_theme_had_initial_mfe_but_180d_high_mae_blocks_yellow_green_without_revenue_conversion_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R12_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"034730","name":"SK","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"korea_valueup_holding_company_policy_label_weak_mfe_high_mae","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":188800.0,"entry_price_type":"next_tradable_open_after_korea_valueup_holdco_policy_label","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.18,"mae_30d_pct":-5.56,"mfe_90d_pct":4.18,"mae_90d_pct":-21.35,"mfe_180d_pct":4.18,"mae_180d_pct":-31.99,"peak_price_180d":196700.0,"peak_date_180d":"2024-02-29","trough_price_180d":128400.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch_until_portfolio_restructuring_capital_return_bridge_repaired","residual_error_type":"holding_company_valueup_policy_label_had_weak_mfe_and_180d_high_mae_without_capital_allocation_and_discount_release_bridge","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R11_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L76_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":76,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW","underlying_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","underlying_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","underlying_fine_archetype_id":"ADC_RNA_VACCINE_TRIAL_PLATFORM_EVENT_MFE_AND_HIGH_MAE_ROUTER","symbol":"293780","name":"압타바이오","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"clinical_event_failure_gapdown_then_delayed_mfe_high_mae","trigger_date":"2024-02-28","entry_date":"2024-02-29","entry_price":6810.0,"entry_price_type":"next_tradable_open_after_clinical_event_risk_gapdown","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.57,"mae_30d_pct":-27.53,"mfe_90d_pct":10.57,"mae_90d_pct":-27.61,"mfe_180d_pct":127.46,"mae_180d_pct":-27.61,"peak_price_180d":15490.0,"peak_date_180d":"2024-07-11","trough_price_180d":4930.0,"trough_date_180d":"2024-05-27","calibration_usable":true,"case_polarity":"counterexample_early_high_mae_delayed_mfe","r13_case_role":"stage2_false_positive_or_guarded_counterexample","do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"local_4B_watch_even_if_later_mfe_until_trial_data_thesis_repaired","residual_error_type":"clinical_event_risk_case_had_delayed_mfe_but_entry_first_absorbed_high_mae_and_requires_trial_data_repair_before_positive_stage","source_loop76_artifact":"e2r_stock_web_v12_residual_round_R7_loop_76_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md"}
```

---

## 8. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R13L76_STAGE2_FALSE_POSITIVE_REVIEW",
  "round": "R13",
  "loop": 76,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "fine_archetype_id": "LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW",
  "case_count": 18,
  "calibration_usable_case_count": 18,
  "positive_holdout_count": 8,
  "false_positive_or_guarded_counterexample_count": 10,
  "underlying_canonical_count": 10,
  "do_not_count_as_new_case": true,
  "source_proxy_only_count": 18,
  "evidence_url_pending_count": 18,
  "avg_mfe_30d_pct": 25.19,
  "avg_mae_30d_pct": -8.76,
  "avg_mfe_90d_pct": 43.26,
  "avg_mae_90d_pct": -14.93,
  "avg_mfe_180d_pct": 68.88,
  "avg_mae_180d_pct": -26.95,
  "max_mfe_180d_pct": 252.15,
  "worst_mae_180d_pct": -64.14
}
```

---

## 9. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | label relevance | bridge evidence | MFE quality | MAE risk control | delayed/entry-peak risk | false-positive pressure | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `226950` | 13 | 8 | 20 | 15 | 12 | -2 | 66 | Stage2/Yellow after trial-data bridge repair |
| `000150` | 13 | 8 | 19 | 13 | 11 | -2 | 62 | Stage2/Yellow after capital-allocation bridge repair |
| `089030` | 13 | 8 | 18 | 14 | 12 | -2 | 63 | Stage2/Yellow after customer/order bridge repair |
| `003960` | 12 | 7 | 16 | 9 | 9 | -3 | 50 | Stage2/Yellow after reorder/channel bridge repair |
| `329180` | 12 | 8 | 14 | 14 | 12 | -2 | 58 | Stage2/Yellow after backlog/delivery bridge repair |
| `103140` | 11 | 7 | 12 | 13 | 11 | -2 | 52 | Stage2/Yellow after spread/margin bridge repair |
| `012630` | 10 | 6 | 10 | 14 | 12 | -2 | 50 | Stage2-Guarded / Yellow after PF bridge repair |
| `307950` | 10 | 6 | 8 | 14 | 12 | -2 | 48 | Stage2-Guarded / Yellow after contract-retention bridge repair |
| `299030` | 8 | 1 | 0 | -22 | -10 | -20 | -43 | block Stage2 / 4B-4C watch |
| `001470` | 8 | 1 | 3 | -21 | -11 | -20 | -40 | block Stage2 / 4B-4C watch |
| `011150` | 7 | 1 | 0 | -22 | -15 | -20 | -49 | block Stage2 / 4B-4C watch |
| `039440` | 9 | 2 | 5 | -17 | -7 | -16 | -24 | local 4B/high-MAE watch |
| `133750` | 8 | 1 | 4 | -17 | -8 | -18 | -30 | block Stage2 / 4B-4C watch |
| `091580` | 8 | 1 | 2 | -17 | -8 | -18 | -32 | block Stage2 / 4B-4C watch |
| `058970` | 10 | 3 | 7 | -12 | -5 | -12 | -9 | Stage2-Guarded at most |
| `057030` | 8 | 2 | 5 | -12 | -5 | -13 | -15 | Stage2-Guarded / 4B watch |
| `034730` | 8 | 1 | 0 | -13 | -9 | -16 | -29 | block Stage2 / local 4B watch |
| `293780` | 8 | 1 | 14 | -10 | -18 | -14 | -19 | local 4B despite delayed MFE |

### Score-return alignment

```text
Positive holdouts:
  226950, 000150, 089030, 003960, 329180, 103140, 012630, and 307950 show that real persistent MFE with controlled or tolerable MAE should remain promotable after evidence repair.

False-positive / guarded failure group:
  299030, 001470, 011150, 133750, and 091580 show weak-MFE or moderate-MFE paths where high MAE should block Stage2.
  039440, 058970, and 057030 show first-window-MFE or high-MFE paths that later draw down hard enough to cap at Stage2-Guarded.
  034730 shows policy relevance with weak MFE and high MAE.
  293780 shows why delayed MFE should not override early clinical-event MAE.
```

---

## 10. Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The remaining residual is broader and should become a cross-archetype shadow guardrail:

```text
A case can pass the first label test and still fail Stage2 if:
  - MFE never expands,
  - the peak occurs early and the bridge is unrepaired,
  - 90D/180D MAE crosses a high-MAE threshold,
  - delayed MFE arrives only after early high MAE,
  - or the required non-price bridge remains source_proxy_only.
```

Proposed loop-76 cross-archetype geometry:

```text
Geometry A — valid holdout:
  MFE_90D >= +20%
  + MAE_90D > -10%
  + bridge is plausible and URL-repairable
  => Stage2-Guarded / Yellow candidate after evidence repair

Geometry B — high-MFE but later-high-MAE:
  MFE_30D >= +20%
  + MAE_180D <= -30%
  + evidence remains source_proxy_only
  => Stage2-Guarded at most, no Yellow/Green

Geometry C — weak-MFE high-MAE:
  MFE_90D < +10%
  + MAE_90D <= -20% or MAE_180D <= -30%
  + no repaired bridge
  => block Stage2 or local 4B/high-MAE watch

Geometry D — extreme-MAE label failure:
  MAE_180D <= -50%
  + MFE fails to compensate or evidence is source_proxy_only
  => hard block Stage2 / 4B-4C watch

Geometry E — delayed-MFE after early high MAE:
  MAE_30D <= -20%
  + later MFE appears
  + bridge evidence remains unrepaired during the drawdown window
  => delayed MFE does not override local 4B risk
```

---

## 11. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R13L76_STAGE2_FALSE_POSITIVE_REVIEW",
  "stage2_positive_or_yellow_holdouts": [
    {
      "symbol": "226950",
      "reason": "RNA/platform event path had +252.15% 180D MFE with only -0.54% MAE"
    },
    {
      "symbol": "000150",
      "reason": "value-up holdco path had +177.08% 180D MFE with only -5.78% MAE"
    },
    {
      "symbol": "089030",
      "reason": "memory test-handler path had +172.31% 180D MFE with only -3.08% MAE"
    },
    {
      "symbol": "003960",
      "reason": "K-food export path had +150.63% MFE; still needs reorder/channel bridge because 180D MAE reached -12.66%"
    },
    {
      "symbol": "329180",
      "reason": "shipbuilder backlog path had +101.54% 180D MFE with only -1.45% MAE"
    },
    {
      "symbol": "103140",
      "reason": "copper/material spread path had +70.04% 180D MFE with only -4.53% MAE"
    },
    {
      "symbol": "012630",
      "reason": "housing/PF relief path had +41.13% 180D MFE with only -1.60% MAE"
    },
    {
      "symbol": "307950",
      "reason": "enterprise software path had +27.03% 180D MFE with only -2.44% MAE"
    }
  ],
  "stage2_guarded_or_local_4b_watch": [
    {
      "symbol": "058970",
      "reason": "SaaS/procurement AI path had +28.24% MFE but -36.30% 180D MAE"
    },
    {
      "symbol": "057030",
      "reason": "online education path had +20.13% MFE but -36.28% 180D MAE"
    },
    {
      "symbol": "039440",
      "reason": "memory equipment event had first-window MFE but -46.07% 180D MAE"
    },
    {
      "symbol": "293780",
      "reason": "clinical-event path had delayed MFE but first absorbed -27.53% 30D MAE"
    }
  ],
  "blocked_stage2_or_4b_4c_watch": [
    {
      "symbol": "299030",
      "reason": "battery equipment label had only +3.68% MFE and -64.14% 180D MAE"
    },
    {
      "symbol": "001470",
      "reason": "construction political spike had only +10.83% MFE and -61.43% 180D MAE"
    },
    {
      "symbol": "011150",
      "reason": "late seafood export theme had only +3.18% MFE and -59.78% 180D MAE"
    },
    {
      "symbol": "133750",
      "reason": "medical education policy theme had +18.50% MFE and -45.10% 180D MAE"
    },
    {
      "symbol": "091580",
      "reason": "battery-can customer relief had +10.16% MFE and -44.39% 180D MAE"
    },
    {
      "symbol": "034730",
      "reason": "value-up holdco policy label had only +4.18% MFE and -31.99% 180D MAE"
    }
  ]
}
```

---

## 12. Cross-archetype rule candidate

```yaml
row_type: cross_archetype_rule_candidate
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: LOOP76_LABEL_ONLY_STAGE2_FALSE_POSITIVE_AND_BRIDGE_GUARDRAIL_REVIEW
rule_name: R13_loop76_label_only_stage2_false_positive_and_bridge_guardrail_router
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
    - non-price bridge is plausible and URL-repairable
  Routing:
    - Stage2-Actionable or Stage2-Guarded allowed
    - Stage3-Yellow only after evidence repair
    - Green only after URL-repaired bridge evidence exists

Tier B: high-MFE but later-high-MAE candidate
  Conditions:
    - MFE_30D >= +20%
    - MAE_180D <= -30%
    - evidence remains source_proxy_only
  Routing:
    - Stage2-Guarded at most
    - no Yellow/Green
    - require bridge repair

Tier C: weak-MFE high-MAE false positive
  Conditions:
    - MFE_90D < +10%
    - MAE_90D <= -20% or MAE_180D <= -30%
    - no repaired non-price bridge
  Routing:
    - block Green
    - block Stage2 or local 4B/high-MAE watch

Tier D: extreme-MAE label failure
  Conditions:
    - MAE_180D <= -50%
    - evidence remains source_proxy_only
  Routing:
    - block Stage2
    - 4B/4C high-MAE watch

Tier E: delayed-MFE after early high MAE
  Conditions:
    - MAE_30D <= -20%
    - later MFE appears
    - bridge evidence was unrepaired during the drawdown window
  Routing:
    - local 4B watch
    - no Yellow/Green from final-window MFE alone
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "r13_loop76_label_only_stage2_false_positive_and_bridge_guardrail_router",
  "scope": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "label_relevance_alone_stage2_allowed": false,
    "yellow_green_requires_url_repaired_bridge": true,
    "holdout_positive_mfe90_min_pct": 20.0,
    "holdout_positive_mae90_min_pct": -10.0,
    "high_mfe_later_mae_mfe30_threshold_pct": 20.0,
    "high_mfe_later_mae180_threshold_pct": -30.0,
    "weak_mfe_threshold_90d_pct": 10.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "weak_mfe_mae180_threshold_pct": -30.0,
    "extreme_mae180_threshold_pct": -50.0,
    "early_high_mae30_threshold_pct": -20.0,
    "delayed_mfe_does_not_override_early_high_mae_without_bridge_repair": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium",
  "apply_now": false,
  "reason": "Loop 76 cross-archetype cases show eight valid holdouts and ten label-only, high-MAE, weak-MFE, or delayed-MFE failures. The rule preserves real persistent-MFE winners while blocking bridge-less policy/theme/order/event labels."
}
```

---

## 13. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R13L76_STAGE2_FALSE_POSITIVE_REVIEW",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "contribution": "Adds a loop-76 cross-archetype Stage2 false-positive review router. The run compares eight positive holdouts against ten label-only or high-MAE failures across C01/C10/C11/C12/C15/C18/C22/C24/C28/C30/C31. It proposes a shadow-only guardrail that blocks policy/theme/order/event relevance from creating Stage2 or Green unless the forward price path has persistent MFE with controlled MAE or the non-price bridge is URL-repaired.",
  "positive_holdout_added": 8,
  "false_positive_or_guarded_counterexample_added": 10,
  "underlying_canonical_count": 10,
  "review_case_count": 18,
  "do_not_count_as_new_case": true,
  "data_quality_blocker": "All selected non-price triggers remain evidence_url_pending=true and source_proxy_only=true until URL-level repair.",
  "guardrail_added": "source_proxy_only + weak MFE, later high MAE, extreme MAE, or delayed MFE after early high MAE should block Green and often block Stage2; valid persistent-MFE holdouts remain Stage2-Guarded until evidence repair."
}
```

One-line contribution:

```text
This loop adds 18 cross-archetype review rows, 8 positive holdouts, and 10 false-positive/guarded counterexamples for R13/L10/R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW. These rows are do_not_count_as_new_case=true.
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
  do_not_count_as_new_case: true
  corporate_action_contaminated_180D_window:
    000150: false
    226950: false
    089030: false
    003960: false
    329180: false
    103140: false
    012630: false
    307950: false
    299030: false
    001470: false
    011150: false
    039440: false
    133750: false
    091580: false
    058970: false
    057030: false
    034730: false
    293780: false
  evidence_url_pending:
    all_selected_rows: true
  source_proxy_only:
    all_selected_rows: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows in the underlying loop-76 artifacts.
- Non-price evidence is not URL-repaired in this run.
- This is a cross-archetype Stage2 false-positive review file, not a positive scoring promotion file.
- R13 rows are do_not_count_as_new_case=true and should be used as guardrail evidence, not as new canonical-case count.
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
2. Preserve R13 / loop 76 metadata.
3. Preserve underlying_large_sector_id, underlying_canonical_archetype_id, and underlying_fine_archetype_id for every trigger row.
4. Treat all selected non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Mark every selected row do_not_count_as_new_case=true.
6. Do not use these rows for positive Yellow/Green promotion until the underlying evidence bridges are repaired.
7. Add a shadow-only cross-archetype rule candidate named R13_loop76_label_only_stage2_false_positive_and_bridge_guardrail_router.
8. Do not loosen Stage3-Green.
9. Add R13-specific guards:
   - source_proxy_only -> no Green
   - label relevance alone -> no Stage2 promotion
   - MFE_90D >= +20% and MAE_90D > -10% can remain Stage2-Guarded / Yellow watch only after evidence repair
   - MFE_30D >= +20% and MAE_180D <= -30% -> Stage2-Guarded at most until bridge repair
   - MFE_90D < +10% and MAE_90D <= -20% or MAE_180D <= -30% -> block Stage2 or local 4B/high-MAE watch
   - MAE_180D <= -50% -> block Stage2 / 4B-4C watch
   - MAE_30D <= -20% with delayed MFE -> delayed MFE does not override early high MAE unless bridge evidence is repaired
   - holdout positives require URL-repaired bridge evidence before Yellow/Green
10. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 16. Next round state

```text
completed_round = R13
completed_loop = 76
next_round = R1
next_loop = 77
next_large_sector_hint = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
round_schedule_status = valid
round_sector_consistency = pass
```
