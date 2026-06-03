# E2R Stock-Web v12 Residual Research — R13 Loop 74

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R13
completed_loop: 74
next_round: R1
next_loop: 75
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW
output_file: e2r_stock_web_v12_residual_round_R13_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
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
completed_loop  = 74
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Therefore:

```text
scheduled_round = R13
scheduled_loop  = 74
```

R13 is a cross-archetype review round, not a normal sector expansion round.  
This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id = LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW
```

This is a valid R13 scope.

---

## 1. Why this R13 run

Loop 74 produced several cases where the first-level label was plausible:

```text
policy event
governance repair / restructuring
clinical data event
security theme
mobility supplier relief
construction PF relief
commodity spread theme
battery customer conversion
```

The cross-archetype problem is that these labels can look similar at trigger time, but the forward price paths separate them.  
R13 should compress that into a reusable false-positive review rule.

The review thesis:

```text
A policy/theme/event label is not enough for Stage2 or Green.
The trigger must have either:
  (a) persistent MFE with contained MAE, or
  (b) repaired non-price evidence before promotion.

If the label is plausible but the path shows weak MFE, entry-day peak, or high MAE while evidence remains source_proxy_only,
the model should block Stage2 or cap it at Stage2-Guarded / local 4B.
```

This run deliberately includes four positive holdouts:

```text
001040 CJ
000150 두산
078600 대주전자재료
025820 이구산업
```

These prevent the R13 rule from becoming a blunt volatility filter.  
The seven counterexamples then define the false-positive geometry:

```text
003550 LG
034730 SK
454910 두산로보틱스
323990 박셀바이오
192250 케이사인
009900 명신산업
005960 동부건설
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

| symbol | name | underlying canonical | calibration usable | note |
|---|---|---|---|---|
| `001040` | CJ | C31 | true | no selected 2024 window corporate-action overlap |
| `000150` | 두산 | C32 | true | no selected 2024 window corporate-action overlap |
| `078600` | 대주전자재료 | C12 | true | no selected 2024 window corporate-action overlap |
| `025820` | 이구산업 | C15 | true | no selected 2024 window corporate-action overlap |
| `003550` | LG | C31 | true | no selected 2024 window corporate-action overlap |
| `034730` | SK | C31 | true | no selected 2024 window corporate-action overlap |
| `454910` | 두산로보틱스 | C32 | true | no selected 2024 window corporate-action overlap |
| `323990` | 박셀바이오 | C24 | true | no selected 2024 window corporate-action overlap |
| `192250` | 케이사인 | C28 | true for 180D | 2024-11-01 corporate-action candidate is after selected 180D window |
| `009900` | 명신산업 | C29 | true | no selected 2024 window corporate-action overlap |
| `005960` | 동부건설 | C30 | true | no selected 2024 window corporate-action overlap |

---

## 3. No-repeat and novelty check

Hard duplicate key for this R13 artifact:

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW + symbol + trigger_type + entry_date
```

Direct repository searches were performed on all selected symbols under this R13 pseudo-archetype:

```text
001040 / 000150 / 078600 / 025820 / 003550 / 034730 / 454910 / 323990 / 192250 / 009900 / 005960
```

Result:

```json
{
  "row_type": "novelty_check",
  "research_id": "R13L74_STAGE2_FALSE_POSITIVE_REVIEW",
  "r13_scope": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "case_count": 11,
  "underlying_canonical_count": 8,
  "symbol_count": 11,
  "positive_holdout_count": 4,
  "false_positive_or_guarded_counterexample_count": 7,
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
+ plausible evidence bridge that can be URL-repaired
= Stage2-Guarded or Yellow candidate, but still not automatic Green
```

Mechanically, the same idea appears in multiple domains:

```text
C31: value-up policy requires company-specific capital allocation
C32: governance/restructuring requires final ratio and shareholder-protection bridge
C24: clinical data requires durable endpoint/regulatory/partner bridge
C28: security theme requires recurring contract-retention bridge
C29: mobility supplier label requires customer-volume / margin bridge
C30: PF relief requires balance-sheet and liquidity bridge
```

---

## 5. Case design

| symbol | underlying canonical | R13 role | key geometry |
|---|---|---|---|
| `001040` | C31 | positive holdout | +44.15% 180D MFE / -3.09% 180D MAE |
| `000150` | C32 | positive holdout | +164.02% 180D MFE / -0.48% 180D MAE |
| `078600` | C12 | positive holdout | +89.12% 180D MFE / -1.62% 180D MAE |
| `025820` | C15 | positive holdout | +97.42% 180D MFE / -11.02% 180D MAE |
| `003550` | C31 | false positive | +7.52% 180D MFE / -21.72% 180D MAE |
| `034730` | C31 | hard false positive | +4.18% 180D MFE / -31.99% 180D MAE |
| `454910` | C32 | event-spike false positive | +15.05% 180D MFE / -43.26% 180D MAE |
| `323990` | C24 | clinical-event false positive | +2.16% 180D MFE / -43.68% 180D MAE |
| `192250` | C28 | theme-spike false positive | +0.87% 180D MFE / -50.03% 180D MAE |
| `009900` | C29 | weak-MFE supplier false positive | +3.15% 180D MFE / -38.70% 180D MAE |
| `005960` | C30 | weak-MFE slow-fade case | +2.42% 180D MFE / -11.55% 180D MAE |

---

## 6. Stock-Web OHLC and backtest excerpts

### 001040 — C31 positive holdout: value-up holding-company discount closure

### 6.1 `001040` CJ — holding-company value-up / discount closure rerating

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable
trigger_family = holding_company_valueup_discount_closure_capital_allocation_rerating
entry_date = 2024-02-27
entry_price = 94000.0
entry_price_type = next_tradable_open_after_korea_valueup_policy_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,100300.0,100400.0,92700.0,94300.0,235412.0,22409828500.0,2751390911400.0,29176998,KOSPI
2024-02-27,94000.0,94200.0,92100.0,93000.0,84642.0,7887174300.0,2713460814000.0,29176998,KOSPI
2024-03-15,96500.0,109200.0,95900.0,109200.0,688893.0,71770424800.0,3186128181600.0,29176998,KOSPI
2024-03-28,116900.0,124000.0,114000.0,122200.0,308463.0,37067135300.0,3565429155600.0,29176998,KOSPI
2024-04-05,132100.0,135500.0,127900.0,128600.0,203954.0,26583541700.0,3752161942800.0,29176998,KOSPI
2024-07-11,121100.0,123600.0,119000.0,122300.0,196597.0,23877703800.0,3568346855400.0,29176998,KOSPI
2024-08-01,130900.0,135000.0,128800.0,134900.0,101820.0,13551741600.0,3935977030200.0,29176998,KOSPI
2024-08-30,112900.0,113700.0,107000.0,111900.0,129870.0,14587244000.0,3264906076200.0,29176998,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 124000 | 2024-03-28 | 91100 | 2024-03-13 | +31.91% | -3.09% |
| 90 calendar days | 135500 | 2024-04-05 | 91100 | 2024-03-13 | +44.15% | -3.09% |
| 180 calendar days | 135500 | 2024-04-05 | 91100 | 2024-03-13 | +44.15% | -3.09% |

R13 interpretation:

```text
R13 holdout. This case prevents overblocking C31: the policy event produced persistent MFE and very low MAE, so the correct route is Stage2/Yellow after company-specific capital-allocation and shareholder-return evidence repair, not blanket rejection.
```
### 000150 — C32 positive holdout: governance-repair parent rerating

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

R13 interpretation:

```text
R13 holdout. This shows that raw governance controversy is not enough, but later governance-repair repricing can be real. The model should distinguish repaired mechanics from first-day optionality.
```
### 078600 — C12 positive holdout: customer-conversion battery material

### 6.1 `078600` 대주전자재료 — silicon-anode customer conversion low-MAE rerating

Trigger:

```text
trigger_date = 2024-03-11
trigger_type = Stage2-Actionable
trigger_family = silicon_anode_customer_conversion_low_mae_rerating
entry_date = 2024-03-12
entry_price = 86400.0
entry_price_type = next_tradable_open_after_silicon_anode_customer_rerating
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-11,80000.0,85600.0,77500.0,85200.0,586226.0,48633832700.0,1318946523600.0,15480593,KOSDAQ
2024-03-12,86400.0,95100.0,85400.0,94900.0,1144358.0,104711119200.0,1469108275700.0,15480593,KOSDAQ
2024-03-25,97000.0,102000.0,95200.0,102000.0,388838.0,38976415300.0,1579020486000.0,15480593,KOSDAQ
2024-03-26,101500.0,103200.0,96000.0,98500.0,444003.0,43900864500.0,1524838410500.0,15480593,KOSDAQ
2024-04-08,90000.0,90000.0,85000.0,88800.0,162941.0,14223802700.0,1374676658400.0,15480593,KOSDAQ
2024-05-30,105200.0,123000.0,105200.0,121300.0,2236997.0,264481416600.0,1877795930900.0,15480593,KOSDAQ
2024-06-12,154900.0,163400.0,152300.0,160000.0,1515428.0,240983991200.0,2476894880000.0,15480593,KOSDAQ
2024-09-06,100700.0,101800.0,92500.0,92900.0,421202.0,40051568800.0,1438147089700.0,15480593,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 103200 | 2024-03-26 | 85000 | 2024-04-08 | +19.44% | -1.62% |
| 90 calendar days | 128500 | 2024-06-10 | 85000 | 2024-04-08 | +48.73% | -1.62% |
| 180 calendar days | 163400 | 2024-06-12 | 85000 | 2024-04-08 | +89.12% | -1.62% |

R13 interpretation:

```text
R13 holdout. A true customer-conversion path can carry large MFE with tiny MAE. It should remain open for Stage2/Yellow after customer volume and margin evidence repair.
```
### 025820 — C15 positive holdout: copper spread pass-through path

### 6.1 `025820` 이구산업 — copper rolling spread pass-through rerating

Trigger:

```text
trigger_date = 2024-03-14
trigger_type = Stage2-Actionable-Guarded
trigger_family = copper_rolling_spread_pass_through_rerating_low_initial_mae
entry_date = 2024-03-15
entry_price = 4265.0
entry_price_type = next_tradable_open_after_copper_spread_burst
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-14,4400.0,4825.0,4185.0,4220.0,25017428.0,115472800550.0,141125240000.0,33442000,KOSPI
2024-03-15,4265.0,4760.0,4165.0,4545.0,15961509.0,72578851935.0,151993890000.0,33442000,KOSPI
2024-04-12,5690.0,6090.0,5460.0,5700.0,15223035.0,89166441390.0,190619400000.0,33442000,KOSPI
2024-04-19,6640.0,7310.0,6410.0,6790.0,47804175.0,332468400980.0,227071180000.0,33442000,KOSPI
2024-05-20,7700.0,8420.0,7400.0,7880.0,47603058.0,381542856790.0,263522960000.0,33442000,KOSPI
2024-06-05,5620.0,5680.0,5450.0,5510.0,1483416.0,8231931900.0,184265420000.0,33442000,KOSPI
2024-08-05,4365.0,4430.0,3795.0,3930.0,805374.0,3285423220.0,131427060000.0,33442000,KOSPI
2024-09-06,4080.0,4100.0,3975.0,3990.0,143785.0,577027540.0,133433580000.0,33442000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 6090 | 2024-04-12 | 4165 | 2024-03-15 | +42.79% | -2.34% |
| 90 calendar days | 8420 | 2024-05-20 | 4165 | 2024-03-15 | +97.42% | -2.34% |
| 180 calendar days | 8420 | 2024-05-20 | 3795 | 2024-08-05 | +97.42% | -11.02% |

R13 interpretation:

```text
R13 holdout. Commodity beta is risky, but this copper spread path had strong MFE and controlled MAE. The rule should preserve low-MAE spread winners while still requiring inventory/pass-through/margin evidence.
```
### 003550 — C31 false positive: policy label without execution bridge

### 6.2 `003550` LG — holding-company policy label with weak MFE and high MAE

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = holding_company_valueup_policy_label_weak_mfe_discount_reopen
entry_date = 2024-02-27
entry_price = 94400.0
entry_price_type = next_tradable_open_after_korea_valueup_policy_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,100600.0,100600.0,92700.0,93900.0,604229.0,57485392100.0,14770563242700.0,157300993,KOSPI
2024-02-27,94400.0,94500.0,92200.0,93400.0,230955.0,21587830100.0,14691912746200.0,157300993,KOSPI
2024-03-14,100200.0,101500.0,98200.0,101400.0,443284.0,44565060300.0,15950320690200.0,157300993,KOSPI
2024-03-28,88700.0,88700.0,87600.0,87600.0,244326.0,21493775200.0,13779566986800.0,157300993,KOSPI
2024-04-18,76100.0,76800.0,73900.0,76200.0,457818.0,34661107479.0,11986335666600.0,157300993,KOSPI
2024-06-13,83200.0,85300.0,81400.0,81400.0,351352.0,29108184400.0,12804300830200.0,157300993,KOSPI
2024-08-05,83800.0,83800.0,77400.0,78100.0,242747.0,19353161300.0,12285207553300.0,157300993,KOSPI
2024-09-03,79700.0,85900.0,79500.0,85400.0,563126.0,47399268700.0,13433504802200.0,157300993,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 101500 | 2024-03-14 | 87600 | 2024-03-28 | +7.52% | -7.20% |
| 90 calendar days | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |
| 180 calendar days | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |

R13 interpretation:

```text
R13 false positive. Value-up policy relevance existed, but MFE stayed below +10% and 90D/180D MAE crossed -20%. Policy label alone should not create Stage2 or Green.
```
### 034730 — C31 false positive: holding-company policy label with hard MAE

### 6.3 `034730` SK — holding-company policy label with hard MAE

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = holding_company_valueup_policy_label_weak_mfe_high_mae
entry_date = 2024-02-27
entry_price = 188800.0
entry_price_type = next_tradable_open_after_korea_valueup_policy_event
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,199800.0,199900.0,187200.0,190200.0,436018.0,83211567300.0,13922322175800.0,73198329,KOSPI
2024-02-27,188800.0,189300.0,181600.0,185500.0,253583.0,46848898900.0,13578290029500.0,73198329,KOSPI
2024-02-29,194500.0,196700.0,188800.0,191800.0,372756.0,71298040900.0,14039439502200.0,73198329,KOSPI
2024-03-12,186200.0,186200.0,178300.0,180400.0,254731.0,45982039500.0,13204978551600.0,73198329,KOSPI
2024-05-24,149300.0,151500.0,148500.0,148800.0,126956.0,18971376500.0,10891911355200.0,73198329,KOSPI
2024-06-10,184300.0,194700.0,180200.0,188600.0,1615800.0,306392365800.0,13805204849400.0,73198329,KOSPI
2024-08-05,142400.0,143000.0,128400.0,131300.0,347328.0,47025691500.0,9519604903900.0,72502703,KOSPI
2024-09-20,149600.0,156700.0,147500.0,154000.0,507998.0,78470567500.0,11165416262000.0,72502703,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 196700 | 2024-02-29 | 178300 | 2024-03-12 | +4.18% | -5.56% |
| 90 calendar days | 196700 | 2024-02-29 | 148500 | 2024-05-24 | +4.18% | -21.35% |
| 180 calendar days | 196700 | 2024-02-29 | 128400 | 2024-08-05 | +4.18% | -31.99% |

R13 interpretation:

```text
R13 hard false positive. The holding-company policy label had only +4.18% MFE while 180D MAE reached -31.99%. This is a blocked Stage2 or local 4B/high-MAE route unless capital allocation evidence appears before entry.
```
### 454910 — C32 false positive: restructuring beneficiary event spike

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

R13 interpretation:

```text
R13 event-spike false positive. The peak occurred on the entry day, then 30D MAE reached -43.26%. A first-day restructuring beneficiary spike without final ratio/shareholder-protection bridge should block Stage2.
```
### 323990 — C24 false positive: clinical event spike already spent

### 6.3 `323990` 박셀바이오 — clinical event spike without durable bridge

Trigger:

```text
trigger_date = 2024-03-25
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = clinical_data_event_spike_without_durable_regulatory_bridge
entry_date = 2024-03-26
entry_price = 23100.0
entry_price_type = next_tradable_open_after_clinical_event_spike
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-25,21450.0,24250.0,21050.0,23350.0,2889412.0,67053589950.0,536891220000.0,22993200,KOSDAQ
2024-03-26,23100.0,23200.0,22300.0,22550.0,574490.0,13038683650.0,518496660000.0,22993200,KOSDAQ
2024-03-27,23100.0,23600.0,21450.0,21450.0,1043408.0,23287366500.0,493204140000.0,22993200,KOSDAQ
2024-04-02,20050.0,20350.0,17510.0,18870.0,1888013.0,34849898710.0,433881684000.0,22993200,KOSDAQ
2024-06-26,15230.0,15370.0,15100.0,15140.0,130606.0,1983699200.0,348117048000.0,22993200,KOSDAQ
2024-08-05,15600.0,15690.0,13010.0,13670.0,405423.0,5895078700.0,314317044000.0,22993200,KOSDAQ
2024-09-11,13940.0,14180.0,13500.0,13510.0,103496.0,1424632950.0,310638132000.0,22993200,KOSDAQ
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 23600 | 2024-03-27 | 17650 | 2024-04-11 | +2.16% | -23.59% |
| 90 calendar days | 23600 | 2024-03-27 | 15100 | 2024-06-26 | +2.16% | -34.63% |
| 180 calendar days | 23600 | 2024-03-27 | 13010 | 2024-08-05 | +2.16% | -43.68% |

R13 interpretation:

```text
R13 clinical-event false positive. MFE stayed only +2.16% while 30D MAE crossed -20% and 180D MAE crossed -40%. Clinical event relevance cannot rescue an entry after the event candle has spent the upside.
```
### 192250 — C28 false positive: authentication/security theme spike

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

R13 interpretation:

```text
R13 theme-spike false positive. The authentication/security theme peaked at entry and then produced extreme MAE. This is a 4B/4C theme-spike guard case, not Stage2.
```
### 009900 — C29 false positive: EV body supplier weak-MFE high-MAE

### 6.3 `009900` 명신산업 — EV body-parts supplier relief with weak MFE and high MAE

Trigger:

```text
trigger_date = 2024-02-08
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = ev_body_parts_volume_margin_relief_weak_mfe_high_mae
entry_date = 2024-02-13
entry_price = 17130.0
entry_price_type = next_tradable_open_after_ev_body_supplier_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-08,17200.0,17250.0,17010.0,17010.0,162320.0,2774821270.0,892516962330.0,52470133,KOSPI
2024-02-13,17130.0,17410.0,17100.0,17260.0,169448.0,2926141270.0,905634495580.0,52470133,KOSPI
2024-02-15,17670.0,17670.0,17120.0,17150.0,200243.0,3450752490.0,899862780950.0,52470133,KOSPI
2024-03-07,15500.0,15540.0,15120.0,15160.0,268475.0,4086782040.0,795447216280.0,52470133,KOSPI
2024-04-08,14600.0,14700.0,14190.0,14200.0,273442.0,3917472110.0,745075888600.0,52470133,KOSPI
2024-07-03,14900.0,15400.0,14630.0,14690.0,852361.0,12840844390.0,770786253770.0,52470133,KOSPI
2024-08-05,12600.0,12640.0,10500.0,10770.0,505436.0,5809986540.0,565103332410.0,52470133,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 17670 | 2024-02-15 | 15120 | 2024-03-07 | +3.15% | -11.73% |
| 90 calendar days | 17670 | 2024-02-15 | 14190 | 2024-04-08 | +3.15% | -17.16% |
| 180 calendar days | 17670 | 2024-02-15 | 10500 | 2024-08-05 | +3.15% | -38.70% |

R13 interpretation:

```text
R13 supplier false positive. Mobility/EV supplier relevance existed, but MFE stayed near +3% and 180D MAE reached -38.70%. Customer-volume and margin evidence must precede promotion.
```
### 005960 — C30 false positive: construction PF weak-MFE slow fade

### 6.4 `005960` 동부건설 — weak-MFE PF/liquidity slow fade

Trigger:

```text
trigger_date = 2024-02-01
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = construction_pf_liquidity_weak_mfe_slow_fade
entry_date = 2024-02-02
entry_price = 5370.0
entry_price_type = next_tradable_open_after_construction_pf_relief
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-01,5350.0,5470.0,5330.0,5430.0,50896.0,275609000.0,124210506090.0,22874863,KOSPI
2024-02-02,5370.0,5430.0,5290.0,5300.0,135844.0,723172820.0,121605547900.0,22944443,KOSPI
2024-02-19,5400.0,5500.0,5360.0,5430.0,46761.0,253612090.0,124588325490.0,22944443,KOSPI
2024-02-27,5270.0,5330.0,5200.0,5220.0,63463.0,333127740.0,119769992460.0,22944443,KOSPI
2024-04-15,4830.0,4910.0,4805.0,4880.0,15986.0,77506300.0,111968881840.0,22944443,KOSPI
2024-06-13,4950.0,4980.0,4750.0,4855.0,129757.0,624270220.0,111404504975.0,22946345,KOSPI
2024-07-31,4930.0,4985.0,4925.0,4950.0,38671.0,191866010.0,113584407750.0,22946345,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 5500 | 2024-02-19 | 5200 | 2024-02-27 | +2.42% | -3.17% |
| 90 calendar days | 5500 | 2024-02-19 | 4805 | 2024-04-15 | +2.42% | -10.52% |
| 180 calendar days | 5500 | 2024-02-19 | 4750 | 2024-06-13 | +2.42% | -11.55% |

R13 interpretation:

```text
R13 weak-MFE slow-fade case. The drawdown was not catastrophic, but MFE never exceeded +2.42%. This is important because Stage2 can fail quietly by never rerating, not only by crashing.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"001040","name":"CJ","trigger_type":"Stage2-Actionable","trigger_family":"holding_company_valueup_discount_closure_capital_allocation_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":94000.0,"entry_price_type":"next_tradable_open_after_korea_valueup_policy_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":31.91,"mae_30d_pct":-3.09,"mfe_90d_pct":44.15,"mae_90d_pct":-3.09,"mfe_180d_pct":44.15,"mae_180d_pct":-3.09,"peak_price_180d":135500.0,"peak_date_180d":"2024-04-05","trough_price_180d":91100.0,"trough_date_180d":"2024-03-13","calibration_usable":true,"case_polarity":"positive_anchor_low_mae_valueup","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_capital_allocation_shareholder_return_bridge_repaired","residual_error_type":"positive_holding_discount_closure_path_requires_url_repaired_valueup_capital_allocation_and_roe_bridge_before_green","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R12_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","underlying_fine_archetype_id":"GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER","symbol":"000150","name":"두산","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"group_restructuring_governance_repair_parent_rerating","trigger_date":"2024-09-11","entry_date":"2024-09-12","entry_price":146200.0,"entry_price_type":"next_tradable_open_after_governance_repair_repricing","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":25.92,"mae_30d_pct":-0.48,"mfe_90d_pct":67.58,"mae_90d_pct":-0.48,"mfe_180d_pct":164.02,"mae_180d_pct":-0.48,"peak_price_180d":386000.0,"peak_date_180d":"2025-02-26","trough_price_180d":145500.0,"trough_date_180d":"2024-09-12","calibration_usable":true,"case_polarity":"positive_guarded_governance_repair","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_governance_value_transfer_repair_and_shareholder_return_bridge_repaired","residual_error_type":"governance_repair_parent_rerating_can_be_valid_but_green_requires_repaired_restructuring_ratio_and_capital_allocation_evidence","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R11_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","underlying_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","underlying_fine_archetype_id":"ANODE_CNT_SILICON_CAN_CUSTOMER_CONTRACT_CALLOFF_AND_HIGH_MAE_ROUTER","symbol":"078600","name":"대주전자재료","trigger_type":"Stage2-Actionable","trigger_family":"silicon_anode_customer_conversion_low_mae_rerating","trigger_date":"2024-03-11","entry_date":"2024-03-12","entry_price":86400.0,"entry_price_type":"next_tradable_open_after_silicon_anode_customer_rerating","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":19.44,"mae_30d_pct":-1.62,"mfe_90d_pct":48.73,"mae_90d_pct":-1.62,"mfe_180d_pct":89.12,"mae_180d_pct":-1.62,"peak_price_180d":163400.0,"peak_date_180d":"2024-06-12","trough_price_180d":85000.0,"trough_date_180d":"2024-04-08","calibration_usable":true,"case_polarity":"positive_anchor_low_mae","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_customer_contract_margin_bridge_repaired","residual_error_type":"positive_anchor_requires_url_repaired_customer_contract_volume_margin_bridge_before_green","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R3_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","underlying_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","underlying_fine_archetype_id":"COPPER_NONFERROUS_SPREAD_PASS_THROUGH_AND_THEME_HIGH_MAE_ROUTER","symbol":"025820","name":"이구산업","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"copper_rolling_spread_pass_through_rerating_low_initial_mae","trigger_date":"2024-03-14","entry_date":"2024-03-15","entry_price":4265.0,"entry_price_type":"next_tradable_open_after_copper_spread_burst","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":42.79,"mae_30d_pct":-2.34,"mfe_90d_pct":97.42,"mae_90d_pct":-2.34,"mfe_180d_pct":97.42,"mae_180d_pct":-11.02,"peak_price_180d":8420.0,"peak_date_180d":"2024-05-20","trough_price_180d":3795.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded_low_mae","r13_case_role":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_to_Yellow_if_copper_spread_inventory_margin_bridge_repaired","residual_error_type":"positive_copper_spread_path_requires_url_repaired_pass_through_inventory_margin_bridge_before_green","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R4_loop_74_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"003550","name":"LG","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"holding_company_valueup_policy_label_weak_mfe_discount_reopen","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":94400.0,"entry_price_type":"next_tradable_open_after_korea_valueup_policy_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.52,"mae_30d_pct":-7.2,"mfe_90d_pct":7.52,"mae_90d_pct":-21.72,"mfe_180d_pct":7.52,"mae_180d_pct":-21.72,"peak_price_180d":101500.0,"peak_date_180d":"2024-03-14","trough_price_180d":73900.0,"trough_date_180d":"2024-04-18","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_until_capital_allocation_bridge_repaired","residual_error_type":"valueup_policy_relevance_without_company_specific_capital_allocation_bridge_led_to_weak_mfe_and_high_mae","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R12_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","underlying_fine_archetype_id":"KOREA_VALUEUP_HOLDING_DISCOUNT_CAPITAL_ALLOCATION_AND_WEAK_MFE_ROUTER","symbol":"034730","name":"SK","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"holding_company_valueup_policy_label_weak_mfe_high_mae","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":188800.0,"entry_price_type":"next_tradable_open_after_korea_valueup_policy_event","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":4.18,"mae_30d_pct":-5.56,"mfe_90d_pct":4.18,"mae_90d_pct":-21.35,"mfe_180d_pct":4.18,"mae_180d_pct":-31.99,"peak_price_180d":196700.0,"peak_date_180d":"2024-02-29","trough_price_180d":128400.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_hard_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch_until_shareholder_return_roe_bridge_repaired","residual_error_type":"holding_company_valueup_label_had_low_mfe_and_180d_hard_mae_without_repaired_capital_return_or_discount_closure_bridge","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R12_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","underlying_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","underlying_fine_archetype_id":"GROUP_RESTRUCTURING_SPINOFF_RATIO_VALUE_TRANSFER_AND_REPAIR_RERATING_ROUTER","symbol":"454910","name":"두산로보틱스","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"restructuring_beneficiary_spike_without_final_ratio_execution_bridge","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":95000.0,"entry_price_type":"next_tradable_open_after_restructuring_beneficiary_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.05,"mae_30d_pct":-43.26,"mfe_90d_pct":15.05,"mae_90d_pct":-43.26,"mfe_180d_pct":15.05,"mae_180d_pct":-43.26,"peak_price_180d":109300.0,"peak_date_180d":"2024-07-12","trough_price_180d":53900.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_event_spike_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"beneficiary_spike_spent_upside_on_entry_day_and_failed_without_final_restructuring_ratio_bridge","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R11_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","underlying_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","underlying_fine_archetype_id":"CLINICAL_PLATFORM_DATA_MILESTONE_HIGH_MFE_VS_EVENT_RISK_ROUTER","symbol":"323990","name":"박셀바이오","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"clinical_data_event_spike_without_durable_regulatory_bridge","trigger_date":"2024-03-25","entry_date":"2024-03-26","entry_price":23100.0,"entry_price_type":"next_tradable_open_after_clinical_event_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.16,"mae_30d_pct":-23.59,"mfe_90d_pct":2.16,"mae_90d_pct":-34.63,"mfe_180d_pct":2.16,"mae_180d_pct":-43.68,"peak_price_180d":23600.0,"peak_date_180d":"2024-03-27","trough_price_180d":13010.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_clinical_event_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"clinical_event_entry_had_weak_mfe_and_large_mae_without_durable_data_regulatory_bridge","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R7_loop_74_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","underlying_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","underlying_fine_archetype_id":"SECURITY_AUTH_CONTRACT_RETENTION_AND_THEME_SPIKE_HIGH_MAE_ROUTER","symbol":"192250","name":"케이사인","trigger_type":"4B-local-watch","trigger_family":"quantum_authentication_security_theme_spike_without_contract_bridge","trigger_date":"2024-03-26","entry_date":"2024-03-27","entry_price":1721.0,"entry_price_type":"next_tradable_open_after_auth_security_theme_spike","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.87,"mae_30d_pct":-26.55,"mfe_90d_pct":0.87,"mae_90d_pct":-36.08,"mfe_180d_pct":0.87,"mae_180d_pct":-50.03,"peak_price_180d":1736.0,"peak_date_180d":"2024-03-27","trough_price_180d":860.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_theme_spike_extreme_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"authentication_security_theme_spike_spent_the_upside_at_entry_and_created_extreme_mae","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R8_loop_74_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","underlying_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","underlying_fine_archetype_id":"AUTO_PARTS_VOLUME_MARGIN_LOW_MAE_AND_WEAK_MFE_HIGH_MAE_ROUTER","symbol":"009900","name":"명신산업","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"ev_body_parts_volume_margin_relief_weak_mfe_high_mae","trigger_date":"2024-02-08","entry_date":"2024-02-13","entry_price":17130.0,"entry_price_type":"next_tradable_open_after_ev_body_supplier_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":3.15,"mae_30d_pct":-11.73,"mfe_90d_pct":3.15,"mae_90d_pct":-17.16,"mfe_180d_pct":3.15,"mae_180d_pct":-38.7,"peak_price_180d":17670.0,"peak_date_180d":"2024-02-15","trough_price_180d":10500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_high_mae","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_4C_high_MAE_watch","residual_error_type":"ev_body_supplier_relief_had_weak_mfe_and_high_mae_without_volume_margin_bridge","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R9_loop_74_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"trigger","research_id":"R13L74_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":74,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW","underlying_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","underlying_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","underlying_fine_archetype_id":"MIDSMALL_CONSTRUCTION_PF_RELIEF_SPIKE_AND_WEAK_MFE_SLOW_FADE_ROUTER","symbol":"005960","name":"동부건설","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"construction_pf_liquidity_weak_mfe_slow_fade","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":5370.0,"entry_price_type":"next_tradable_open_after_construction_pf_relief","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":2.42,"mae_30d_pct":-3.17,"mfe_90d_pct":2.42,"mae_90d_pct":-10.52,"mfe_180d_pct":2.42,"mae_180d_pct":-11.55,"peak_price_180d":5500.0,"peak_date_180d":"2024-02-19","trough_price_180d":4750.0,"trough_date_180d":"2024-06-13","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_slow_fade","r13_case_role":"stage2_false_positive_or_guarded_counterexample","evidence_url_pending":true,"source_proxy_only":true,"price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_only_until_pf_liquidity_repair_evidence","residual_error_type":"weak_mfe_construction_pf_relief_path_should_not_green_without_liquidity_bridge","source_loop74_artifact":"e2r_stock_web_v12_residual_round_R10_loop_74_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
```

---

## 8. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R13L74_STAGE2_FALSE_POSITIVE_REVIEW",
  "round": "R13",
  "loop": 74,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "fine_archetype_id": "LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW",
  "case_count": 11,
  "calibration_usable_case_count": 11,
  "positive_holdout_count": 4,
  "false_positive_or_guarded_counterexample_count": 7,
  "underlying_canonical_count": 8,
  "source_proxy_only_count": 11,
  "evidence_url_pending_count": 11,
  "avg_mfe_30d_pct": 14.13,
  "avg_mae_30d_pct": -11.69,
  "avg_mfe_90d_pct": 26.66,
  "avg_mae_90d_pct": -17.48,
  "avg_mfe_180d_pct": 39.1,
  "avg_mae_180d_pct": -23.38,
  "max_mfe_180d_pct": 164.02,
  "worst_mae_180d_pct": -50.03
}
```

---

## 9. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | label relevance | evidence bridge | MFE quality | MAE risk control | same-window peak risk | false-positive pressure | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `001040` | 13 | 10 | 13 | 14 | 12 | -2 | 60 | Stage2/Yellow after capital-allocation evidence repair |
| `000150` | 13 | 10 | 18 | 15 | 13 | -2 | 67 | Stage2/Yellow after governance-repair evidence |
| `078600` | 13 | 11 | 16 | 15 | 13 | -2 | 66 | Stage2/Yellow after customer-volume evidence |
| `025820` | 12 | 9 | 16 | 11 | 10 | -3 | 55 | Stage2-Guarded / Yellow after spread evidence |
| `003550` | 11 | 3 | 3 | -8 | -4 | -14 | -9 | block Green; Stage2-Guarded at most |
| `034730` | 11 | 2 | 2 | -13 | -5 | -16 | -19 | block Stage2 or local 4B watch |
| `454910` | 10 | 2 | 5 | -18 | -14 | -18 | -33 | block Stage2 / 4B-4C watch |
| `323990` | 9 | 2 | 1 | -18 | -12 | -18 | -36 | block Stage2 / 4B-4C watch |
| `192250` | 8 | 1 | 0 | -20 | -15 | -19 | -45 | 4B-4C high-MAE watch |
| `009900` | 8 | 2 | 1 | -16 | -8 | -17 | -30 | block Stage2 / 4B watch |
| `005960` | 7 | 2 | 0 | -5 | -5 | -12 | -13 | weak-MFE slow-fade counterexample |

### Score-return alignment

```text
Positive holdouts:
  001040, 000150, 078600, and 025820 show that persistent MFE with contained MAE should remain promotable after evidence repair.

False-positive group:
  003550 and 034730 show policy label without company-specific execution.
  454910 and 192250 show event/theme spikes where the peak is already spent.
  323990 shows clinical-event relevance without durable data/regulatory bridge.
  009900 shows mobility supplier relevance without volume/margin conversion.
  005960 shows a quiet Stage2 failure: not a crash, but no real MFE.
```

---

## 10. Current calibrated profile stress test

The current calibrated profile already blocks pure price-only blowoff.  
The residual issue is broader:

```text
A trigger can have a plausible label and still be a Stage2 false positive
if the forward path shows weak MFE or high MAE before the non-price bridge is repaired.
```

Proposed R13 geometry:

```text
Geometry A — positive holdout:
  MFE_90D >= +25%
  + MAE_90D > -12%
  + bridge is plausible and URL-repairable
  => Stage2-Guarded / Yellow candidate after evidence repair

Geometry B — policy/theme label without execution:
  MFE_30D < +10%
  + MAE_90D <= -20%
  + evidence remains source_proxy_only
  => block Green and cap or block Stage2

Geometry C — event spike already spent:
  peak occurs on entry day or first 5 trading days
  + MAE_30D <= -20%
  + bridge missing
  => block Stage2, route to 4B/4C watch

Geometry D — quiet weak-MFE slow fade:
  MFE_90D < +5%
  + no repaired non-price bridge
  => block Green and usually block Stage2 even if MAE is not catastrophic
```

---

## 11. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R13L74_STAGE2_FALSE_POSITIVE_REVIEW",
  "stage2_positive_or_yellow_holdouts": [
    {
      "symbol": "001040",
      "reason": "value-up holding-company path had +44.15% 180D MFE with only -3.09% MAE"
    },
    {
      "symbol": "000150",
      "reason": "governance-repair path had +164.02% 180D MFE with only -0.48% MAE"
    },
    {
      "symbol": "078600",
      "reason": "customer-conversion path had +89.12% 180D MFE with only -1.62% MAE"
    },
    {
      "symbol": "025820",
      "reason": "copper-spread path had +97.42% 180D MFE with manageable -11.02% MAE"
    }
  ],
  "blocked_stage2_or_stage2_guarded_review": [
    {
      "symbol": "003550",
      "reason": "policy label had only +7.52% MFE and -21.72% MAE"
    },
    {
      "symbol": "034730",
      "reason": "policy label had only +4.18% MFE and -31.99% MAE"
    },
    {
      "symbol": "009900",
      "reason": "mobility supplier label had only +3.15% MFE and -38.70% MAE"
    },
    {
      "symbol": "005960",
      "reason": "construction PF relief never exceeded +2.42% MFE"
    }
  ],
  "local_4b_or_4c_event_spike_watch": [
    {
      "symbol": "454910",
      "reason": "entry-day peak and -43.26% 30D/180D MAE"
    },
    {
      "symbol": "323990",
      "reason": "clinical event spike had only +2.16% MFE and -43.68% 180D MAE"
    },
    {
      "symbol": "192250",
      "reason": "theme spike had only +0.87% MFE and -50.03% 180D MAE"
    }
  ]
}
```

---

## 12. Cross-archetype rule candidate

```yaml
row_type: cross_archetype_rule_candidate
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: LOOP74_POLICY_THEME_LABEL_WITHOUT_EXECUTION_BRIDGE_REVIEW
rule_name: R13_loop74_label_without_execution_stage2_false_positive_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For source_proxy_only or evidence_url_pending cases across canonical archetypes:

Tier A: valid holdout
  Conditions:
    - MFE_90D >= +25%
    - MAE_90D > -12%
    - MFE persists beyond first event candle
    - non-price bridge is plausible and URL-repairable
  Routing:
    - Stage2-Actionable or Stage2-Guarded allowed
    - Stage3-Yellow only after evidence repair
    - Green only after URL-repaired bridge evidence exists

Tier B: policy/theme label without execution
  Conditions:
    - MFE_30D < +10%
    - MAE_90D <= -20%
    - evidence remains source_proxy_only
  Routing:
    - block Green
    - cap at Stage2-Guarded or block Stage2
    - count as Stage2 false-positive candidate

Tier C: event spike already spent
  Conditions:
    - peak occurs on entry day or within first 5 trading days
    - MAE_30D <= -20%
    - no repaired non-price bridge
  Routing:
    - block Stage2
    - route to local 4B/4C high-MAE watch

Tier D: quiet weak-MFE slow fade
  Conditions:
    - MFE_90D < +5%
    - source evidence remains unrepaired
  Routing:
    - block Green
    - block Stage2 unless later trigger has a new non-price bridge
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "r13_loop74_label_without_execution_stage2_false_positive_router",
  "scope": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "label_relevance_alone_stage2_allowed": false,
    "yellow_green_requires_url_repaired_bridge": true,
    "holdout_positive_mfe90_min_pct": 25.0,
    "holdout_positive_mae90_min_pct": -12.0,
    "weak_mfe_threshold_30d_pct": 10.0,
    "weak_mfe_mae90_threshold_pct": -20.0,
    "entry_spike_mae30_threshold_pct": -20.0,
    "quiet_slow_fade_mfe90_threshold_pct": 5.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium",
  "apply_now": false,
  "reason": "Loop 74 cross-archetype cases show four valid low-MAE / persistent-MFE holdouts and seven policy/theme/event label false positives. The rule should preserve real repaired reratings while blocking label-only Stage2 promotion."
}
```

---

## 13. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R13L74_STAGE2_FALSE_POSITIVE_REVIEW",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "contribution": "Adds a loop-74 cross-archetype Stage2 false-positive review router. The run compares four positive holdouts against seven label-only or event-spike failures across C12/C15/C24/C28/C29/C30/C31/C32. It proposes a shadow-only rule that blocks policy/theme/event relevance from creating Stage2 or Green unless the forward price path has persistent MFE with contained MAE or the non-price bridge is URL-repaired.",
  "positive_holdout_added": 4,
  "false_positive_or_guarded_counterexample_added": 7,
  "underlying_canonical_count": 8,
  "data_quality_blocker": "All selected non-price triggers remain evidence_url_pending=true and source_proxy_only=true until URL-level repair.",
  "guardrail_added": "source_proxy_only + weak MFE or entry-day spike should block Green and often block Stage2; valid low-MAE/persistent-MFE holdouts remain Stage2-Guarded until evidence repair."
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
    001040: false
    000150: false
    078600: false
    025820: false
    003550: false
    034730: false
    454910: false
    323990: false
    192250: false
    009900: false
    005960: false
  evidence_url_pending:
    001040: true
    000150: true
    078600: true
    025820: true
    003550: true
    034730: true
    454910: true
    323990: true
    192250: true
    009900: true
    005960: true
  source_proxy_only:
    001040: true
    000150: true
    078600: true
    025820: true
    003550: true
    034730: true
    454910: true
    323990: true
    192250: true
    009900: true
    005960: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
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
2. Preserve R13 / loop 74 metadata.
3. Preserve underlying_large_sector_id, underlying_canonical_archetype_id, and underlying_fine_archetype_id for every trigger row.
4. Treat all selected non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive Yellow/Green promotion until the underlying evidence bridges are repaired.
6. Add a shadow-only cross-archetype rule candidate named R13_loop74_label_without_execution_stage2_false_positive_router.
7. Do not loosen Stage3-Green.
8. Add R13-specific guards:
   - source_proxy_only -> no Green
   - label relevance alone -> no Stage2 promotion
   - MFE_30D < +10% and MAE_90D <= -20% -> block Green and cap/block Stage2
   - entry-day or first-5-day peak with MAE_30D <= -20% -> block Stage2 / 4B-4C watch
   - MFE_90D < +5% with unrepaired evidence -> quiet slow-fade counterexample
   - holdout positives require URL-repaired bridge evidence before Yellow/Green
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 16. Next round state

```text
completed_round = R13
completed_loop = 74
next_round = R1
next_loop = 75
next_large_sector_hint = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
round_schedule_status = valid
round_sector_consistency = pass
```
