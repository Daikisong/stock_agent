# E2R Stock-Web v12 Residual Research — R11 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R11
completed_loop: 72
next_round: R12
next_loop: 72
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_CORPORATE_VALUE_UP_NONFINANCIAL_HOLDCO_POLICY_ROUTER
output_file: e2r_stock_web_v12_residual_round_R11_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
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
completed_round = R10
completed_loop = 72
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Therefore:

```text
scheduled_round = R11
scheduled_loop  = 72
```

R11 permits:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
or
L1 defense/infrastructure-linked policy event
```

This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_CORPORATE_VALUE_UP_NONFINANCIAL_HOLDCO_POLICY_ROUTER
```

This is a valid R11 pairing.

---

## 1. Why this R11/C31 run

The no-repeat ledger shows C31 is broad and already covered, but it remains useful as a policy-event router because C31 can accidentally promote broad policy beneficiaries from price alone:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT:
  rows: 155
  symbols: 63
  date_range: 2020-01-20~2024-07-31
  good/bad S2: 38/32
  4B/4C: 35/0
  URL/proxy: 0/7
  top covered symbols: UNKNOWN_SYMBOL(15), 036460(8), 112610(7), 005380(5), 005860(5), 218150(5)
```

The immediately preceding R11/L10 run in loop 71 covered a Korea East Sea gasfield policy event.  
This file deliberately avoids that event family and instead tests the 2024 Korea corporate value-up policy shock in non-financial holding-company / conglomerate-discount names:

```text
003550 LG
000880 한화
001040 CJ
```

Research question:

```text
Can C31 separate a policy event that unlocks a real shareholder-return / governance / NAV-discount rerating from a broad policy rally that fades when capital-return execution is not yet visible?
```

C31 is a policy machine. It can open the gate, but it cannot deliver the harvest by itself. For non-financial holding companies, the actual conversion chain is:

```text
policy announcement
  -> company value-up disclosure / governance plan
  -> capital-return execution or discount-narrowing proof
  -> durable valuation rerating
```

If the chain stops at the first link, the price can still spike, but Green should remain blocked.

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
| `003550` | LG | active_like / KOSPI | no 2024 overlap; old 1999~2004 candidates only | true |
| `000880` | 한화 | active_like / KOSPI | no 2024 overlap; old 1996/1999 candidates only | true |
| `001040` | CJ | active_like / KOSPI | no 2024 overlap; old 1998/1999/2007/2008 candidates only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Evidence event and trigger discipline

### Event family

```text
event_family = Korea Corporate Value-Up Program policy announcement
trigger_date = 2024-02-26
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-02-27
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_CORPORATE_VALUE_UP_NONFINANCIAL_HOLDCO_POLICY_ROUTER
```

The event is treated as a capital-market policy shock intended to encourage listed companies to improve valuation, governance, disclosure, and shareholder-return behavior. In this file, the policy event is routed through non-financial holding companies because they can be exposed to:

```text
- NAV discount narrowing
- low-PBR / conglomerate-discount rerating
- shareholder-return expectations
- governance-plan disclosure expectations
- treasury/shareholder-policy optionality
```

However, this artifact intentionally marks non-price evidence as conservative:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level value-up plan disclosure, shareholder-return execution, treasury action, dividend/buyback policy, governance reform, and NAV-discount bridge evidence still require later URL repair through filings, company IR, exchange disclosures, or regulatory documents before any production weight promotion.
```

C31 interpretation used here:

```text
C31 policy events should not score all beneficiaries the same.
A policy shock can create an option.
Only company-specific execution converts the option into Stage2/Yellow/Green.
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Searches performed before writing:

```text
003550 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT + value-up -> no direct match found
000880 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT + value-up -> no direct match found
001040 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT + value-up -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "positive_case_count": 1,
  "positive_guarded_case_count": 1,
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
| `R11L72_C31_001040_20240227` | `001040` CJ | value-up policy + non-financial holdco discount rerating with strong follow-through | positive anchor, but evidence repair required |
| `R11L72_C31_000880_20240227` | `000880` 한화 | value-up policy + conglomerate discount / shareholder-return optionality | guarded positive / later proof required |
| `R11L72_C31_003550_20240227` | `003550` LG | value-up policy rally after pre-announcement move, then fade | counterexample / policy-only fade |

The intended residual:

```text
C31 should separate:
1. non-financial holding-company value-up cases with strong post-policy follow-through;
2. guarded cases where policy optionality works but execution proof is still needed; and
3. policy-only cases where the event arrives after a pre-positioned rally and the post-event path fades.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `001040` CJ — value-up policy positive anchor

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = corporate_value_up_policy_nonfinancial_holdco_discount_rerating
entry_date = 2024-02-27
entry_price = 94000.0
entry_price_type = next_tradable_open
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
| 30 calendar days | 124000 | 2024-03-28 | 91100 | 2024-03-13 | +31.91% | -3.09% |
| 90 calendar days | 152900 | 2024-05-16 | 91100 | 2024-03-13 | +62.66% | -3.09% |
| 180 calendar days | 152900 | 2024-05-16 | 91100 | 2024-03-13 | +62.66% | -3.09% |

Interpretation:

```text
001040 is the positive anchor. The event did not merely create one candle; the post-event path produced high MFE with very small MAE.
The clean price path supports Stage2-Actionable / Stage3-Yellow consideration.
But because company-specific value-up execution evidence is not URL-repaired here, it should not automatically become Green.
```

### 6.2 `000880` 한화 — guarded value-up / conglomerate-discount rerating

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = corporate_value_up_policy_conglomerate_discount_optional_rerating
entry_date = 2024-02-27
entry_price = 28250.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,28900.0,29100.0,27400.0,28200.0,941614.0,26466147600.0,2113836327000.0,74958735,KOSPI
2024-02-27,28250.0,28600.0,27750.0,28150.0,384483.0,10869360350.0,2110088390250.0,74958735,KOSPI
2024-03-05,29400.0,30200.0,29250.0,29400.0,363814.0,10776442450.0,2203786809000.0,74958735,KOSPI
2024-04-03,26750.0,31950.0,26650.0,28650.0,3339827.0,97345478250.0,2147567757750.0,74958735,KOSPI
2024-05-24,25750.0,25900.0,25450.0,25550.0,159422.0,4085862600.0,1915195679250.0,74958735,KOSPI
2024-07-25,30450.0,31700.0,29750.0,31300.0,964637.0,29646419350.0,2346208405500.0,74958735,KOSPI
2024-07-31,31000.0,32150.0,30200.0,31200.0,402688.0,12680584450.0,2338712532000.0,74958735,KOSPI
2024-08-05,29600.0,29800.0,27800.0,28450.0,677748.0,19640831300.0,2132576010750.0,74958735,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 30200 | 2024-03-05 | 27750 | 2024-02-27 | +6.90% | -1.77% |
| 90 calendar days | 31950 | 2024-04-03 | 25450 | 2024-05-24 | +13.10% | -9.91% |
| 180 calendar days | 32150 | 2024-07-31 | 25400 | 2024-06-27 | +13.81% | -10.09% |

Interpretation:

```text
000880 is a guarded positive / policy-optionality case.
The MFE is real but not explosive, and the path had a meaningful mid-window drawdown before later recovery.
This supports Stage2-Actionable-Guarded, not Green.
A Green path would require company-specific shareholder-return, governance, NAV-discount, or capital-allocation evidence.
```

### 6.3 `003550` LG — policy-only fade / pre-positioned rally counterexample

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = corporate_value_up_policy_prepositioned_holdco_fade
entry_date = 2024-02-27
entry_price = 94400.0
entry_price_type = next_tradable_open
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
| 30 calendar days | 101500 | 2024-03-14 | 87600 | 2024-03-28 | +7.52% | -7.20% |
| 90 calendar days | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |
| 180 calendar days | 101500 | 2024-03-14 | 73900 | 2024-04-18 | +7.52% | -21.72% |

Interpretation:

```text
003550 is the counterexample branch.
The stock had already moved sharply before the formal policy-date entry, and post-entry MFE was small relative to later drawdown.
This is a C31 policy-only fade: policy relevance existed, but the post-event path did not confirm durable execution.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R11L72_C31_VALUE_UP_HOLDCO_POLICY","round":"R11","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_CORPORATE_VALUE_UP_NONFINANCIAL_HOLDCO_POLICY_ROUTER","symbol":"001040","name":"CJ","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"corporate_value_up_policy_nonfinancial_holdco_discount_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":94000.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":31.91,"mae_30d_pct":-3.09,"mfe_90d_pct":62.66,"mae_90d_pct":-3.09,"mfe_180d_pct":62.66,"mae_180d_pct":-3.09,"peak_price_180d":152900.0,"peak_date_180d":"2024-05-16","trough_price_180d":91100.0,"trough_date_180d":"2024-03-13","calibration_usable":true,"case_polarity":"positive_anchor","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_to_Yellow_if_valueup_execution_repaired","residual_error_type":"strong_policy_rerating_path_but_green_requires_company_specific_capital_return_governance_execution"}
{"row_type":"trigger","research_id":"R11L72_C31_VALUE_UP_HOLDCO_POLICY","round":"R11","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_CORPORATE_VALUE_UP_NONFINANCIAL_HOLDCO_POLICY_ROUTER","symbol":"000880","name":"한화","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"corporate_value_up_policy_conglomerate_discount_optional_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":28250.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.90,"mae_30d_pct":-1.77,"mfe_90d_pct":13.10,"mae_90d_pct":-9.91,"mfe_180d_pct":13.81,"mae_180d_pct":-10.09,"peak_price_180d":32150.0,"peak_date_180d":"2024-07-31","trough_price_180d":25400.0,"trough_date_180d":"2024-06-27","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_only_until_shareholder_return_or_nav_discount_bridge_repaired","residual_error_type":"moderate_mfe_requires_execution_evidence_before_yellow_green"}
{"row_type":"trigger","research_id":"R11L72_C31_VALUE_UP_HOLDCO_POLICY","round":"R11","loop":72,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_CORPORATE_VALUE_UP_NONFINANCIAL_HOLDCO_POLICY_ROUTER","symbol":"003550","name":"LG","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"corporate_value_up_policy_prepositioned_holdco_fade","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":94400.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":7.52,"mae_30d_pct":-7.20,"mfe_90d_pct":7.52,"mae_90d_pct":-21.72,"mfe_180d_pct":7.52,"mae_180d_pct":-21.72,"peak_price_180d":101500.0,"peak_date_180d":"2024-03-14","trough_price_180d":73900.0,"trough_date_180d":"2024-04-18","calibration_usable":true,"case_polarity":"counterexample_policy_only_fade","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_local_4B_high_MAE_watch","residual_error_type":"policy_relevance_without_company_execution_turned_into_post_event_fade"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | policy relevance | company execution visibility | capital return / NAV bridge | market mispricing | valuation rerating | governance confidence | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `001040` | 14 | 9 | 11 | 15 | 18 | 8 | 6 | 81 | Stage2/Yellow after value-up execution evidence repair; no auto-Green |
| `000880` | 13 | 7 | 8 | 10 | 9 | 7 | 6 | 60 | Stage2-Guarded only until capital-return/NAV bridge repaired |
| `003550` | 13 | 4 | 5 | 7 | 5 | 6 | 5 | 45 | blocked Stage2 or local 4B/high-MAE watch |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C31 problem is more specific:

```text
C31 policy-event false-positive mode:
  broad government policy announcement
  + sector/holdco relevance
  + no company-specific execution evidence
  + post-event MFE is small or MAE becomes large
  => block Green; use Stage2-Guarded or 4B watch at most

C31 policy-event positive mode:
  policy announcement
  + non-price company execution bridge
  + low MAE / persistent follow-through
  + capital return, governance, NAV-discount, or shareholder-plan evidence repaired
  => Stage2-Actionable / Stage3-Yellow, then Green only after execution proof
```

`001040` shows the policy-event positive anchor.  
`000880` shows the guarded middle route.  
`003550` shows why C31 cannot simply boost every pre-rallied holding company at the formal policy date.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R11L72_C31_VALUE_UP_HOLDCO_POLICY",
  "round": "R11",
  "loop": 72,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "KOREA_CORPORATE_VALUE_UP_NONFINANCIAL_HOLDCO_POLICY_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_anchor_count": 1,
  "positive_guarded_case_count": 1,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 15.44,
  "avg_mae_30d_pct": -4.02,
  "avg_mfe_90d_pct": 27.76,
  "avg_mae_90d_pct": -11.57,
  "avg_mfe_180d_pct": 27.99,
  "avg_mae_180d_pct": -11.63,
  "worst_mae_180d_pct": -21.72
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R11L72_C31_VALUE_UP_HOLDCO_POLICY",
  "local_4b_watch": [
    {
      "symbol": "003550",
      "reason": "formal policy entry arrived after pre-event rally; post-entry MFE was only +7.52% while 90D/180D MAE reached -21.72%"
    },
    {
      "symbol": "000880",
      "reason": "moderate MFE and mid-window drawdown; Stage2-Guarded only until execution proof arrives"
    }
  ],
  "full_4b_requires_non_price_evidence": [
    {
      "symbol": "001040",
      "reason": "strong MFE/low MAE path but full rerating requires company-specific value-up/capital-return execution evidence"
    }
  ],
  "blocked_green": [
    "003550",
    "000880",
    "001040 until company-specific execution evidence is URL-repaired"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_CORPORATE_VALUE_UP_NONFINANCIAL_HOLDCO_POLICY_ROUTER
rule_name: C31_valueup_policy_execution_bridge_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C31 corporate value-up / capital-market policy cases:

Tier A: policy + company execution bridge
  Conditions:
    - policy event is relevant
    - company-specific value-up plan, capital return, governance reform, buyback, dividend, or NAV-discount bridge is URL-repaired
    - 30D/90D MAE remains contained
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after execution evidence and valuation path remain aligned

Tier B: policy-only optionality
  Conditions:
    - policy event is relevant
    - company is plausible beneficiary
    - but execution evidence is missing or source-proxy-only
  Routing:
    - Stage2-Actionable-Guarded at most
    - no Green
    - no positive weight promotion

Tier C: pre-positioned policy fade
  Conditions:
    - stock had already rallied before formal policy event
    - post-entry MFE is small
    - 90D or 180D MAE worse than -20%
    - no company-specific execution bridge
  Routing:
    - blocked Stage2 or local 4B/high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c31_valueup_policy_execution_bridge_router",
  "scope": "canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "policy_relevance_alone_green_allowed": false,
    "company_specific_execution_bridge_required_for_yellow_green": true,
    "prepositioned_policy_fade_high_mae_watch_threshold_pct": -20.0,
    "stage2_guarded_allowed_when_low_mae_and_policy_relevance": true,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three non-financial holding-company value-up policy paths show that broad policy relevance alone is insufficient. CJ had strong low-MAE follow-through, Hanwha was guarded, and LG became a policy-only fade after a pre-event run. All non-price execution evidence remains URL-pending."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R11L72_C31_VALUE_UP_HOLDCO_POLICY",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "contribution": "Adds a C31 value-up policy-event router for non-financial holding-company / conglomerate-discount cases. It separates strong low-MAE policy follow-through from guarded optionality and pre-positioned policy fade. C31 should require company-specific value-up, capital-return, governance, or NAV-discount execution evidence before Yellow/Green.",
  "positive_case_added": 1,
  "positive_guarded_case_added": 1,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price execution triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C31 Green is blocked when source_proxy_only=true; policy relevance alone cannot create Green without company-specific execution bridge."
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
    001040: false
    000880: false
    003550: false
  evidence_url_pending:
    001040: true
    000880: true
    003550: true
  source_proxy_only:
    001040: true
    000880: true
    003550: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C31 policy-event residual shape and value-up execution-bridge guardrail design, but should not promote positive weights until filings/IR/exchange disclosure/regulatory documents verify company-specific value-up plans, shareholder return, buybacks, dividend policy, governance reform, or NAV-discount bridge.
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
2. Preserve R11 / loop 72 metadata.
3. Add the cases to C31_POLICY_SUBSIDY_LEGISLATION_EVENT only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/exchange disclosure/regulatory data verifies company-specific value-up plans, shareholder return, buybacks, dividend policy, governance reform, or NAV-discount bridge.
6. Add a shadow-only rule candidate named C31_valueup_policy_execution_bridge_router.
7. Do not loosen Stage3-Green.
8. Add C31-specific guards:
   - source_proxy_only -> no Green
   - policy relevance alone -> no Green
   - Stage3-Yellow/Green requires company-specific execution bridge
   - pre-positioned policy fade with 90D/180D MAE <= -20% -> local 4B/high-MAE watch or blocked positive stage
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R11
completed_loop = 72
next_round = R12
next_loop = 72
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or under-covered service/agri event
```
