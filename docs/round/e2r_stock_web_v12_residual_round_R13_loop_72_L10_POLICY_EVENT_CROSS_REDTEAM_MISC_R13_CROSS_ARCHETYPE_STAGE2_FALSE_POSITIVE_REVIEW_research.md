# E2R Stock-Web v12 Residual Research — R13 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R13
completed_loop: 72
next_round: R1
next_loop: 73
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER
output_file: e2r_stock_web_v12_residual_round_R13_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
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
completed_loop  = 72
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Therefore:

```text
scheduled_round = R13
scheduled_loop  = 72
```

R13 is not a normal sector-expansion round. It must use only cross-archetype review scopes.  
This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id = SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER
```

This is a valid R13 scope.

---

## 1. Why this R13 run

The no-repeat ledger shows the R13 Stage2 false-positive review bucket is still thin compared with R13 4B/4C red-team:

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW:
  rows: 12
  symbols: 12
  date_range: 2021-07-06~2024-05-29
  good/bad S2: 3/3
  4B/4C: 1/1
  URL/proxy: 0/0
```

R13 loop 72 therefore uses a cross-archetype review rather than another sector file.  
The file tests a pattern that appeared repeatedly in loop 72 outputs:

```text
source_proxy_only or event-driven evidence
  + Stage2-looking price move
  + no verified company-specific bridge
  + later high MAE
  => should be blocked from Green and often blocked from Stage2
```

The review uses cases from three underlying canonical archetypes:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

A single positive holdout is included to avoid turning the rule into a blunt “all policy/event moves are bad” filter.

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

| symbol | name | underlying canonical | profile status | corporate-action overlap with tested window | calibration usable |
|---|---|---|---|---|---|
| `001040` | CJ | C31 | active_like / KOSPI | no 2024 overlap; old 1998/1999/2007/2008 candidates only | true |
| `003550` | LG | C31 | active_like / KOSPI | no 2024 overlap; old 1999~2004 candidates only | true |
| `003070` | 코오롱글로벌 | C30 | active_like / KOSPI | no 2024 overlap; 2023 and 2025 candidates outside tested window | true |
| `000150` | 두산 | C32 | active_like / KOSPI | no 2024 overlap; old 1997~1999 candidates only | true |
| `454910` | 두산로보틱스 | C32 | active_like / KOSPI | none listed | true |
| `241560` | 두산밥캣 | C32 | active_like / KOSPI | none listed | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. No-repeat and novelty check

Hard duplicate key from the ledger:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

For this R13 artifact the hard key uses the R13 review pseudo-archetype:

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW + symbol + trigger_type + entry_date
```

Targeted searches during the loop-72 underlying artifact creation found no direct match for the underlying C30/C31/C32 hard keys.  
This R13 file is not claiming a new sector-archetype discovery. It is a cross-archetype review layer over validated Stock-Web price paths.

Novelty accounting:

```json
{
  "row_type": "novelty_check",
  "research_id": "R13L72_STAGE2_FALSE_POSITIVE_REVIEW",
  "r13_scope": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "case_count": 6,
  "underlying_canonical_count": 3,
  "symbol_count": 6,
  "positive_holdout_count": 1,
  "false_positive_or_guardrail_count": 5,
  "duplicate_status": "pass_for_r13_cross_archetype_review",
  "new_independent_case_ratio": 1.00
}
```

---

## 4. Review thesis

The false-positive pattern being tested is:

```text
event relevance is real
but non-price conversion evidence is missing or source-proxy-only
and the price path shows early MFE followed by severe MAE
```

This file distinguishes three different mechanisms that can look deceptively similar at trigger time:

```text
C30 credit relief:
  a balance-sheet/PF rally can start before liquidity repair is actually visible

C31 policy optionality:
  a policy event can lift plausible beneficiaries even when company execution is not yet present

C32 governance restructuring:
  a group-control or exchange-ratio event can move value between listed entities and create severe minority-holder drawdown
```

The positive holdout is `001040` CJ. It shows that policy-event cases should not be mechanically blocked when price/MAE alignment is strong.  
The other five cases show why Green must still require verified non-price bridges.

---

## 5. Case design

| case_id | symbol | underlying canonical | trigger family | R13 role |
|---|---|---|---|---|
| `R13L72_001040_C31_20240227` | `001040` CJ | C31 | value-up policy holdco rerating | positive holdout / Green still requires evidence repair |
| `R13L72_003550_C31_20240227` | `003550` LG | C31 | value-up policy pre-positioned holdco fade | Stage2 false-positive |
| `R13L72_003070_C30_20240627` | `003070` 코오롱글로벌 | C30 | construction credit-relief squeeze | Stage2 false-positive / 4B-4C watch |
| `R13L72_000150_C32_20240712` | `000150` 두산 | C32 | parent-control vehicle restructuring squeeze | guardrail-positive, later recovery after extreme MAE |
| `R13L72_454910_C32_20240712` | `454910` 두산로보틱스 | C32 | high-valuation beneficiary narrative | Stage2 false-positive |
| `R13L72_241560_C32_20240712` | `241560` 두산밥캣 | C32 | exchange-ratio / minority-holder fairness risk | Stage2 false-positive |

---

## 6. Stock-Web OHLC and backtest

### 6.1 Positive holdout — `001040` CJ

Trigger:

```text
underlying_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
trigger_date = 2024-02-26
entry_date = 2024-02-27
entry_price = 94000.0
trigger_type = Stage2-Actionable-Guarded
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,100300.0,100400.0,92700.0,94300.0,235412.0,22409828500.0,2751390911400.0,29176998,KOSPI
2024-02-27,94000.0,94200.0,92100.0,93000.0,84642.0,7887174300.0,2713460814000.0,29176998,KOSPI
2024-03-15,96500.0,109200.0,95900.0,109200.0,688893.0,71770424800.0,3186128181600.0,29176998,KOSPI
2024-03-28,116900.0,124000.0,114000.0,122200.0,308463.0,37067135300.0,3565429155600.0,29176998,KOSPI
2024-05-10,135000.0,147500.0,133300.0,145500.0,376365.0,53883039900.0,4245253209000.0,29176998,KOSPI
2024-05-16,149300.0,152900.0,146800.0,152700.0,167202.0,25279241300.0,4455327594600.0,29176998,KOSPI
2024-07-04,116400.0,119400.0,105700.0,106400.0,335362.0,36719909200.0,3104432587200.0,29176998,KOSPI
2024-08-01,130900.0,135000.0,128800.0,134900.0,101820.0,13551741600.0,3935977030200.0,29176998,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 124000 | 2024-03-28 | 91100 | 2024-03-13 | +31.91% | -3.09% |
| 90D | 152900 | 2024-05-16 | 91100 | 2024-03-13 | +62.66% | -3.09% |
| 180D | 152900 | 2024-05-16 | 91100 | 2024-03-13 | +62.66% | -3.09% |

R13 interpretation:

```text
This is the holdout. A source-proxy policy event can still have a clean price path.
But Green remains blocked until company-specific value-up / capital-return / governance evidence is URL-repaired.
```

### 6.2 C31 false positive — `003550` LG

Trigger:

```text
underlying_canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
trigger_date = 2024-02-26
entry_date = 2024-02-27
entry_price = 94400.0
trigger_type = Stage2-FalsePositive-Candidate
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-19,98000.0,103600.0,96800.0,103500.0,808969.0,82584142700.0,16280652775500.0,157300993,KOSPI
2024-02-26,100600.0,100600.0,92700.0,93900.0,604229.0,57485392100.0,14770563242700.0,157300993,KOSPI
2024-02-27,94400.0,94500.0,92200.0,93400.0,230955.0,21587830100.0,14691912746200.0,157300993,KOSPI
2024-03-14,100200.0,101500.0,98200.0,101400.0,443284.0,44565060300.0,15950320690200.0,157300993,KOSPI
2024-03-28,88700.0,88700.0,87600.0,87600.0,244326.0,21493775200.0,13779566986800.0,157300993,KOSPI
2024-04-18,76100.0,76800.0,73900.0,76200.0,457818.0,34661107479.0,11986335666600.0,157300993,KOSPI
2024-05-16,82400.0,82800.0,80700.0,81000.0,263759.0,21521039100.0,12741380433000.0,157300993,KOSPI
2024-08-05,83800.0,83800.0,77400.0,78100.0,242747.0,19353161300.0,12285207553300.0,157300993,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 101500 | 2024-03-14 | 87600 | 2024-03-28 | +7.52% | -7.20% |
| 90D | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |
| 180D | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |

R13 interpretation:

```text
Policy relevance existed, but post-entry upside was small and MAE crossed the -20% high-MAE threshold.
This is a Stage2 false-positive candidate unless company execution evidence is repaired.
```

### 6.3 C30 false positive — `003070` 코오롱글로벌

Trigger:

```text
underlying_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
trigger_date = 2024-06-26
entry_date = 2024-06-27
entry_price = 14150.0
trigger_type = 4B-local-watch
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-26,13810.0,14500.0,13220.0,13630.0,529069.0,7320671250.0,258052878190.0,18932713,KOSPI
2024-06-27,14150.0,15200.0,13600.0,13630.0,2062450.0,30126741120.0,258052878190.0,18932713,KOSPI
2024-07-03,12840.0,12900.0,11680.0,11730.0,297984.0,3593070830.0,222080723490.0,18932713,KOSPI
2024-07-25,10310.0,10370.0,10010.0,10320.0,129417.0,1320545600.0,195385598160.0,18932713,KOSPI
2024-08-05,9610.0,9620.0,8500.0,8800.0,124324.0,1113766920.0,166607874400.0,18932713,KOSPI
2024-11-12,9100.0,11970.0,8770.0,10850.0,2751981.0,30735571850.0,205419936050.0,18932713,KOSPI
2024-12-09,8550.0,8560.0,7920.0,7960.0,100042.0,808168200.0,150704395480.0,18932713,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 15200 | 2024-06-27 | 10010 | 2024-07-25 | +7.42% | -29.26% |
| 90D | 15200 | 2024-06-27 | 8500 | 2024-08-05 | +7.42% | -39.93% |
| 180D | 15200 | 2024-06-27 | 7920 | 2024-12-09 | +7.42% | -44.03% |

R13 interpretation:

```text
This is a pure high-MAE false-positive pattern.
The trigger candle's upside was small and the drawdown was immediate. C30 must remain credit-risk-first.
```

### 6.4 C32 guardrail-positive — `000150` 두산

Trigger:

```text
underlying_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
trigger_date = 2024-07-11
entry_date = 2024-07-12
entry_price = 263500.0
trigger_type = 4B-local-watch
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
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 263500 | 2024-07-12 | 122000 | 2024-08-05 | +0.00% | -53.70% |
| 90D | 263500 | 2024-07-12 | 122000 | 2024-08-05 | +0.00% | -53.70% |
| 180D | 304500 | 2025-01-07 | 122000 | 2024-08-05 | +15.56% | -53.70% |

R13 interpretation:

```text
This is the important guardrail-positive case.
A later recovery does not validate the event-day Stage2/Green. The path first went through a -53.70% drawdown, so the initial trigger must be routed as 4B/high-MAE watch.
```

### 6.5 C32 false positive — `454910` 두산로보틱스

Trigger:

```text
underlying_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
trigger_date = 2024-07-11
entry_date = 2024-07-12
entry_price = 95000.0
trigger_type = Stage2-FalsePositive-Candidate
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,81500.0,86200.0,81100.0,85300.0,2032864.0,171787964200.0,5529144294000.0,64819980,KOSPI
2024-07-12,95000.0,109300.0,92200.0,105700.0,15292160.0,1552990227300.0,6851471886000.0,64819980,KOSPI
2024-07-25,75100.0,76400.0,72700.0,73400.0,1575540.0,116703314700.0,4757786532000.0,64819980,KOSPI
2024-08-05,66600.0,66700.0,53900.0,59300.0,919934.0,57094799600.0,3843824814000.0,64819980,KOSPI
2024-08-29,65000.0,73600.0,64900.0,69300.0,1359963.0,95883580400.0,4492024614000.0,64819980,KOSPI
2025-01-02,56600.0,67800.0,56200.0,67000.0,4171511.0,264594735400.0,4342938660000.0,64819980,KOSPI
2025-01-08,64900.0,65500.0,62600.0,63000.0,639841.0,40775828300.0,4083658740000.0,64819980,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 109300 | 2024-07-12 | 53900 | 2024-08-05 | +15.05% | -43.26% |
| 90D | 109300 | 2024-07-12 | 53900 | 2024-08-05 | +15.05% | -43.26% |
| 180D | 109300 | 2024-07-12 | 53900 | 2024-08-05 | +15.05% | -43.26% |

R13 interpretation:

```text
This is the cleanest C32 false-positive branch.
The same trigger day created both the peak and the warning sign. Without final structure and earnings bridge, no Stage2/Green promotion should occur.
```

### 6.6 C32 false positive — `241560` 두산밥캣

Trigger:

```text
underlying_canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
trigger_date = 2024-07-11
entry_date = 2024-07-12
entry_price = 51500.0
trigger_type = Stage2-FalsePositive-Candidate
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,51500.0,52000.0,50500.0,52000.0,252359.0,12966110100.0,5212956632000.0,100249166,KOSPI
2024-07-12,51500.0,59500.0,49850.0,54600.0,6789108.0,366749381750.0,5473604463600.0,100249166,KOSPI
2024-07-25,47000.0,47950.0,41150.0,44150.0,1981380.0,86261552550.0,4426000678900.0,100249166,KOSPI
2024-08-05,38400.0,38700.0,33350.0,34250.0,813194.0,29212468650.0,3433533935500.0,100249166,KOSPI
2024-08-29,43250.0,45950.0,40050.0,42050.0,2948285.0,125679147650.0,4215477430300.0,100249166,KOSPI
2025-01-08,41600.0,42350.0,41500.0,42000.0,614640.0,25834673900.0,4210464972000.0,100249166,KOSPI
2025-01-24,49550.0,53400.0,48900.0,52500.0,778621.0,39897620100.0,5263081215000.0,100249166,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 59500 | 2024-07-12 | 33350 | 2024-08-05 | +15.53% | -35.24% |
| 90D | 59500 | 2024-07-12 | 33350 | 2024-08-05 | +15.53% | -35.24% |
| 180D | 59500 | 2024-07-12 | 33350 | 2024-08-05 | +15.53% | -35.24% |

R13 interpretation:

```text
This is the minority-holder / exchange-ratio false-positive branch.
The market initially repriced the event, but the path punished anyone treating the headline as clean Stage2.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R13L72_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"001040","name":"CJ","trigger_type":"Stage2-Actionable-Guarded-HoldoutPositive","trigger_family":"valueup_policy_holdco_positive_holdout","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":94000.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":31.91,"mae_30d_pct":-3.09,"mfe_90d_pct":62.66,"mae_90d_pct":-3.09,"mfe_180d_pct":62.66,"mae_180d_pct":-3.09,"peak_price_180d":152900.0,"peak_date_180d":"2024-05-16","trough_price_180d":91100.0,"trough_date_180d":"2024-03-13","calibration_usable":true,"case_polarity":"positive_holdout","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2_Guarded_to_Yellow_if_execution_repaired","residual_error_type":"holdout_positive_prevents_overblocking_but_green_requires_evidence_repair"}
{"row_type":"trigger","research_id":"R13L72_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER","underlying_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"003550","name":"LG","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"valueup_policy_prepositioned_holdco_fade","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":94400.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.52,"mae_30d_pct":-7.20,"mfe_90d_pct":7.52,"mae_90d_pct":-21.72,"mfe_180d_pct":7.52,"mae_180d_pct":-21.72,"peak_price_180d":101500.0,"peak_date_180d":"2024-03-14","trough_price_180d":73900.0,"trough_date_180d":"2024-04-18","calibration_usable":true,"case_polarity":"counterexample_policy_fade","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_watch","residual_error_type":"policy_relevance_without_execution_and_high_mae"}
{"row_type":"trigger","research_id":"R13L72_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER","underlying_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"003070","name":"코오롱글로벌","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"construction_credit_relief_squeeze_high_mae","trigger_date":"2024-06-26","entry_date":"2024-06-27","entry_price":14150.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.42,"mae_30d_pct":-29.26,"mfe_90d_pct":7.42,"mae_90d_pct":-39.93,"mfe_180d_pct":7.42,"mae_180d_pct":-44.03,"peak_price_180d":15200.0,"peak_date_180d":"2024-06-27","trough_price_180d":7920.0,"trough_date_180d":"2024-12-09","calibration_usable":true,"case_polarity":"counterexample_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"4B_or_4C_watch","residual_error_type":"credit_relief_squeeze_small_mfe_extreme_mae"}
{"row_type":"trigger","research_id":"R13L72_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER","underlying_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"000150","name":"두산","trigger_type":"4B-local-watch-GuardrailPositive","trigger_family":"parent_control_vehicle_later_recovery_after_extreme_mae","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":263500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":0.00,"mae_30d_pct":-53.70,"mfe_90d_pct":0.00,"mae_90d_pct":-53.70,"mfe_180d_pct":15.56,"mae_180d_pct":-53.70,"peak_price_180d":304500.0,"peak_date_180d":"2025-01-07","trough_price_180d":122000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"guardrail_positive","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"local_4B_watch_then_recheck_after_final_terms","residual_error_type":"later_recovery_after_extreme_mae_does_not_validate_initial_stage2_green"}
{"row_type":"trigger","research_id":"R13L72_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER","underlying_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"454910","name":"두산로보틱스","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"high_valuation_beneficiary_restructuring_narrative","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":95000.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.05,"mae_30d_pct":-43.26,"mfe_90d_pct":15.05,"mae_90d_pct":-43.26,"mfe_180d_pct":15.05,"mae_180d_pct":-43.26,"peak_price_180d":109300.0,"peak_date_180d":"2024-07-12","trough_price_180d":53900.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"beneficiary_narrative_mfe_overwhelmed_by_high_mae"}
{"row_type":"trigger","research_id":"R13L72_STAGE2_FALSE_POSITIVE_REVIEW","round":"R13","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER","underlying_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"241560","name":"두산밥캣","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"exchange_ratio_minorityholder_fairness_risk","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":51500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.53,"mae_30d_pct":-35.24,"mfe_90d_pct":15.53,"mae_90d_pct":-35.24,"mfe_180d_pct":15.53,"mae_180d_pct":-35.24,"peak_price_180d":59500.0,"peak_date_180d":"2024-07-12","trough_price_180d":33350.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_exchange_ratio_fairness","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_4B_high_MAE_watch","residual_error_type":"minorityholder_exchange_ratio_risk_high_mae"}
```

---

## 8. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R13L72_STAGE2_FALSE_POSITIVE_REVIEW",
  "round": "R13",
  "loop": 72,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "fine_archetype_id": "SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER",
  "case_count": 6,
  "calibration_usable_case_count": 6,
  "positive_holdout_count": 1,
  "guardrail_positive_count": 1,
  "counterexample_count": 4,
  "underlying_canonical_count": 3,
  "source_proxy_only_count": 6,
  "evidence_url_pending_count": 6,
  "avg_mfe_30d_pct": 12.90,
  "avg_mae_30d_pct": -28.62,
  "avg_mfe_90d_pct": 18.03,
  "avg_mae_90d_pct": -32.82,
  "avg_mfe_180d_pct": 20.62,
  "avg_mae_180d_pct": -33.51,
  "max_mfe_180d_pct": 62.66,
  "worst_mae_180d_pct": -53.70
}
```

---

## 9. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | underlying canonical | evidence bridge quality | initial MFE quality | MAE risk | event/path clarity | information confidence | false-positive pressure | shadow total | intended route |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `001040` | C31 | 7 | 15 | 15 | 11 | 6 | -3 | 51 | holdout positive; Yellow only after execution repair |
| `003550` | C31 | 3 | 5 | -10 | 5 | 5 | -12 | -4 | blocked Stage2 / local 4B watch |
| `003070` | C30 | 2 | 4 | -18 | 4 | 4 | -16 | -20 | 4B/4C watch |
| `000150` | C32 | 5 | 2 | -20 | 6 | 5 | -18 | -20 | local 4B; later recovery does not validate initial Green |
| `454910` | C32 | 2 | 7 | -18 | 4 | 4 | -17 | -18 | blocked Stage2 / high-MAE watch |
| `241560` | C32 | 2 | 7 | -15 | 3 | 4 | -16 | -15 | blocked Stage2 / exchange-ratio risk |

### Stress-test conclusion

The model should not treat `source_proxy_only=true` as an automatic rejection.  
`001040` proves that a source-proxy event can have a clean, aligned path.  
But the evidence bar for Yellow/Green must rise sharply when the path has any of the following features:

```text
- post-entry MFE < +10% and 90D MAE <= -20%
- first-day peak followed by 30D MAE <= -25%
- later recovery only after MAE <= -40%
- event type involves value transfer across related parties
- credit/PF or minority-holder fairness risk is unresolved
```

---

## 10. Cross-archetype rule candidate

```yaml
row_type: cross_archetype_rule_candidate
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: SOURCE_PROXY_EVENT_STAGE2_FALSE_POSITIVE_AND_HIGH_MAE_ROUTER
rule_name: R13_source_proxy_event_false_positive_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C30/C31/C32 and other event-driven cases:

Tier A: source-proxy event with aligned price path
  Conditions:
    - evidence is source-proxy-only or URL-pending
    - 30D and 90D MAE remain contained
    - MFE is persistent, not just same-day peak
    - event has plausible non-price conversion bridge
  Routing:
    - Stage2-Actionable-Guarded allowed
    - Stage3-Yellow only after evidence repair
    - Green blocked until URL-repaired bridge evidence arrives

Tier B: source-proxy event with weak MFE and high MAE
  Conditions:
    - MFE_90D < +15%
    - MAE_90D <= -20%
    - evidence bridge remains source-proxy-only
  Routing:
    - block Stage2 promotion
    - local 4B/high-MAE watch
    - count as Stage2 false-positive review case

Tier C: first-day peak then extreme drawdown
  Conditions:
    - peak occurs on entry day or within 5 trading days
    - MAE_30D <= -25%
    - event involves governance restructuring, credit/PF relief, minority-holder fairness, or policy-only optionality
  Routing:
    - block Green
    - route to 4B/4C red-team
    - later recovery does not retroactively validate initial Stage2/Green
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "r13_source_proxy_event_false_positive_high_mae_router",
  "scope": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "yellow_green_requires_url_repaired_bridge": true,
    "weak_mfe_high_mae_blocks_stage2": true,
    "weak_mfe_threshold_90d_pct": 15.0,
    "high_mae_threshold_90d_pct": -20.0,
    "first_day_peak_high_mae_threshold_30d_pct": -25.0,
    "later_recovery_after_extreme_mae_does_not_validate_initial_green": true
  },
  "confidence": "medium",
  "apply_now": false,
  "reason": "Six cross-archetype cases show that source-proxy event evidence can be acceptable only when price/MAE alignment is clean. Five of six cases show that weak or same-day MFE followed by high MAE should block Stage2/Green until URL-repaired non-price bridge evidence exists."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R13L72_STAGE2_FALSE_POSITIVE_REVIEW",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW",
  "contribution": "Adds an R13 cross-archetype Stage2 false-positive router for source-proxy event cases. It compares C31 policy optionality, C30 PF/balance-sheet relief, and C32 governance restructuring. The holdout positive CJ prevents overblocking, while LG, Kolon Global, Doosan, Doosan Robotics, and Doosan Bobcat show that weak MFE or same-day peak followed by high MAE should block Stage2/Green until URL-repaired bridge evidence exists.",
  "positive_holdout_added": 1,
  "guardrail_positive_added": 1,
  "counterexample_case_added": 4,
  "underlying_canonical_count": 3,
  "data_quality_blocker": "All six non-price event triggers require URL-level repair before any Yellow/Green promotion.",
  "guardrail_added": "For source_proxy_only event cases, weak MFE plus 90D MAE <= -20%, or first-day peak plus 30D MAE <= -25%, should route to local 4B/high-MAE watch or blocked Stage2."
}
```

---

## 12. Validation scope

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
    003550: false
    003070: false
    000150: false
    454910: false
    241560: false
  evidence_url_pending:
    001040: true
    003550: true
    003070: true
    000150: true
    454910: true
    241560: true
  source_proxy_only:
    001040: true
    003550: true
    003070: true
    000150: true
    454910: true
    241560: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact should be treated as a cross-archetype guardrail / review artifact, not a positive scoring promotion artifact.
- It should not be read as a current investment view.
```

---

## 13. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 historical residual research artifact.

Task:
1. Ingest the machine-readable trigger rows.
2. Preserve R13 / loop 72 metadata.
3. Add the cases under R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW if parser validation passes.
4. Preserve underlying_canonical_archetype_id for every trigger row.
5. Treat all six non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
6. Do not use these rows for positive Yellow/Green promotion until the underlying C30/C31/C32 evidence bridges are repaired.
7. Add a shadow-only cross-archetype rule candidate named R13_source_proxy_event_false_positive_high_mae_router.
8. Do not loosen Stage3-Green.
9. Add R13-specific guards:
   - source_proxy_only -> no Green
   - source_proxy_only + MFE_90D < +15% + MAE_90D <= -20% -> block Stage2
   - first-day peak + MAE_30D <= -25% -> local 4B/high-MAE watch or 4C red-team
   - later recovery after extreme MAE does not retroactively validate initial Stage2/Green
   - holdout positives may remain Stage2-Guarded / Yellow candidates only after URL repair
10. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R13
completed_loop = 72
next_round = R1
next_loop = 73
next_large_sector_hint = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```
