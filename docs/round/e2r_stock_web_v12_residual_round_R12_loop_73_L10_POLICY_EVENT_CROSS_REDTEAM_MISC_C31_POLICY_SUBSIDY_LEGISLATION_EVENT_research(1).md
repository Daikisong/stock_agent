# E2R Stock-Web v12 Residual Research — R12 Loop 73

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R12
completed_loop: 73
next_round: R13
next_loop: 73
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_CORPORATE_VALUE_UP_AUTO_CAPITAL_RETURN_EXECUTION_ROUTER
output_file: e2r_stock_web_v12_residual_round_R12_loop_73_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
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
completed_round = R11
completed_loop  = 73
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

Therefore:

```text
scheduled_round = R12
scheduled_loop  = 73
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
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_CORPORATE_VALUE_UP_AUTO_CAPITAL_RETURN_EXECUTION_ROUTER
```

This is a valid R12 pairing.

---

## 1. Why this R12/C31 run

The no-repeat ledger shows C31 is broad and already covered, but the top-covered symbols are not the auto-supplier / auto-capital-return set tested here:

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

The previous loop-72 C31 file tested non-financial holding-company value-up cases.  
This file deliberately tests a different subtype:

```text
fine_archetype_id = KOREA_CORPORATE_VALUE_UP_AUTO_CAPITAL_RETURN_EXECUTION_ROUTER
```

Selected symbols:

```text
012330 현대모비스
000270 기아
011210 현대위아
```

Research question:

```text
Can C31 separate Korea value-up / low-PBR auto-capital-return rerating from an auto-supplier policy-relief entry where the policy label is real but the company-specific execution bridge is weak?
```

C31 is a policy-event archetype.  
The policy is the wind; the company-specific capital-return / ROE / governance / margin bridge is the sail. Without a sail, the same wind can push the stock sideways or into drawdown.

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
| `012330` | 현대모비스 | active_like / KOSPI | no 2024 overlap; old 1997~1999 candidates only | true |
| `000270` | 기아 | active_like / KOSPI | no 2024 overlap; old 1999 candidates only | true |
| `011210` | 현대위아 | active_like / KOSPI | none listed | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data.
These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Evidence event and trigger discipline

### Event family

```text
event_family = Korea Corporate Value-Up Program policy announcement / low-PBR capital-market reform
trigger_date = 2024-02-26
entry_rule = next_tradable_open_to_avoid_same_day_lookahead
entry_date = 2024-02-27
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_CORPORATE_VALUE_UP_AUTO_CAPITAL_RETURN_EXECUTION_ROUTER
```

This artifact intentionally marks non-price evidence as conservative:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level value-up plan disclosure, dividend/buyback execution, capital allocation, ROE bridge, governance reform, auto margin/volume evidence, and supplier operating leverage still require URL repair through filings, company IR, exchange disclosures, or regulatory documents before production weight promotion.
```

C31 interpretation used here:

```text
C31 policy events should not score all beneficiaries the same.
A policy shock can create the option.
Only company-specific execution converts the option into Stage2/Yellow/Green.
```

For the auto cluster, the conversion chain is:

```text
value-up policy / low-PBR rerating
  -> company-specific capital-return or governance plan
  -> ROE / margin / cash-flow durability
  -> durable valuation rerating
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
012330 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
000270 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
011210 + C31_POLICY_SUBSIDY_LEGISLATION_EVENT -> no direct match found
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
| `R12L73_C31_000270_20240227` | `000270` 기아 | auto value-up / capital-return rerating with low early MAE | positive anchor |
| `R12L73_C31_012330_20240227` | `012330` 현대모비스 | auto-parts low-PBR / governance-capital-return rerating | positive-guarded |
| `R12L73_C31_011210_20240227` | `011210` 현대위아 | auto-supplier policy relief without strong execution bridge | counterexample / weak-MFE path |

The intended residual:

```text
C31 should separate:
1. auto value-up paths with strong MFE and contained early MAE;
2. auto-parts value-up candidates that work but still need execution evidence before Green;
3. auto-supplier policy-relief cases where policy relevance exists but the price path is weak and later MAE becomes meaningful.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `000270` 기아 — auto value-up / capital-return positive anchor

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable
trigger_family = auto_valueup_capital_return_low_pbr_rerating
entry_date = 2024-02-27
entry_price = 111800.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,116000.0,116500.0,112300.0,114600.0,2748769.0,314659065400.0,46074265663800.0,402044203,KOSPI
2024-02-27,111800.0,115800.0,111800.0,112600.0,2108829.0,240137224200.0,45270177257800.0,402044203,KOSPI
2024-02-29,118300.0,126900.0,117500.0,124500.0,5862121.0,721606987100.0,50054503273500.0,402044203,KOSPI
2024-03-11,128900.0,131700.0,126100.0,126200.0,1885521.0,242610600100.0,50737978418600.0,402044203,KOSPI
2024-03-25,113100.0,113500.0,111000.0,111500.0,1550861.0,173469114400.0,44827928634500.0,402044203,KOSPI
2024-05-27,120500.0,124400.0,118600.0,122500.0,1644197.0,200829138900.0,49250414867500.0,402044203,KOSPI
2024-06-19,132200.0,135000.0,130800.0,132300.0,1606458.0,213005246200.0,52901268569100.0,399858417,KOSPI
2024-08-05,103900.0,104400.0,95000.0,96300.0,2493835.0,247987333824.0,38506365557100.0,399858417,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 131700 | 2024-03-11 | 111000 | 2024-03-25 | +17.80% | -0.72% |
| 90 calendar days | 131700 | 2024-03-11 | 101800 | 2024-04-03 | +17.80% | -8.94% |
| 180 calendar days | 135000 | 2024-06-19 | 95000 | 2024-08-05 | +20.75% | -15.03% |

Interpretation:

```text
000270 is the clean positive anchor in this R12 file.
The path produced meaningful MFE with contained early MAE. It is a valid Stage2-Actionable / Yellow candidate after URL-repaired capital-return and ROE evidence.
It should not be automatic Green from policy relevance alone.
```

### 6.2 `012330` 현대모비스 — auto-parts value-up positive-guarded case

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-Actionable-Guarded
trigger_family = auto_parts_low_pbr_governance_capital_return_rerating
entry_date = 2024-02-27
entry_price = 234500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,247000.0,247000.0,235500.0,241000.0,210199.0,50435365000.0,22570877654000.0,93655094,KOSPI
2024-02-27,234500.0,238000.0,233000.0,233500.0,282830.0,66470802500.0,21868464449000.0,93655094,KOSPI
2024-02-28,232500.0,243000.0,230000.0,242000.0,282388.0,67478534901.0,22664532748000.0,93655094,KOSPI
2024-03-14,252000.0,268000.0,251500.0,265000.0,640155.0,168343920000.0,24818599910000.0,93655094,KOSPI
2024-03-18,269500.0,270000.0,265500.0,268000.0,202563.0,54372655500.0,25099565192000.0,93655094,KOSPI
2024-05-27,221500.0,223500.0,220000.0,221000.0,167702.0,37096219500.0,20697775774000.0,93655094,KOSPI
2024-06-28,252500.0,257500.0,248500.0,251500.0,286548.0,72249804500.0,23388266141000.0,92995094,KOSPI
2024-08-05,215000.0,215500.0,200500.0,204000.0,316073.0,65278833000.0,18970999176000.0,92995094,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 270000 | 2024-03-18 | 230000 | 2024-02-28 | +15.14% | -1.92% |
| 90 calendar days | 270000 | 2024-03-18 | 220000 | 2024-05-27 | +15.14% | -6.18% |
| 180 calendar days | 270000 | 2024-03-18 | 200500 | 2024-08-05 | +15.14% | -14.50% |

Interpretation:

```text
012330 is a positive-guarded C31 case.
The 30D/90D path was usable, and even the 180D MAE stayed below the severe false-positive zone.
This is Stage2-Actionable-Guarded or Yellow after evidence repair, but Green still needs company-specific capital-return, governance, ROE, and margin evidence.
```

### 6.3 `011210` 현대위아 — policy-relevant supplier with weak MFE and later drawdown

Trigger:

```text
trigger_date = 2024-02-26
trigger_type = Stage2-FalsePositive-Candidate
trigger_family = auto_supplier_valueup_policy_relief_without_execution_bridge
entry_date = 2024-02-27
entry_price = 59800.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-26,60900.0,61000.0,58600.0,59500.0,155801.0,9257991000.0,1618107438500.0,27195083,KOSPI
2024-02-27,59800.0,60600.0,59000.0,59200.0,72798.0,4349946500.0,1609948913600.0,27195083,KOSPI
2024-03-22,60800.0,60900.0,59500.0,59900.0,110617.0,6627791900.0,1628985471700.0,27195083,KOSPI
2024-04-19,56100.0,56300.0,54500.0,55200.0,109122.0,6021930200.0,1501168581600.0,27195083,KOSPI
2024-05-27,55600.0,56900.0,55100.0,56500.0,94598.0,5321621900.0,1536522189500.0,27195083,KOSPI
2024-06-18,57700.0,61700.0,57300.0,59400.0,650343.0,39038033400.0,1615387930200.0,27195083,KOSPI
2024-08-05,50900.0,51100.0,45450.0,46150.0,211997.0,10146548500.0,1255053080450.0,27195083,KOSPI
2024-09-13,50700.0,53800.0,50700.0,51600.0,182853.0,9582080100.0,1403266282800.0,27195083,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 60900 | 2024-03-22 | 56500 | 2024-03-13 | +1.84% | -5.52% |
| 90 calendar days | 60900 | 2024-03-22 | 54500 | 2024-04-19 | +1.84% | -8.86% |
| 180 calendar days | 61700 | 2024-06-18 | 45450 | 2024-08-05 | +3.18% | -23.99% |

Interpretation:

```text
011210 is the counterexample branch.
The policy label is plausible, but post-entry MFE was too weak and the later drawdown was material.
This should not be promoted from C31 policy relevance alone. It belongs in Stage2-Guarded at most, or blocked Stage2 if no company-specific capital-return / ROE / margin bridge is repaired.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R12L73_C31_AUTO_VALUEUP_ROUTER","round":"R12","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_CORPORATE_VALUE_UP_AUTO_CAPITAL_RETURN_EXECUTION_ROUTER","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","trigger_family":"auto_valueup_capital_return_low_pbr_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":111800.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":17.80,"mae_30d_pct":-0.72,"mfe_90d_pct":17.80,"mae_90d_pct":-8.94,"mfe_180d_pct":20.75,"mae_180d_pct":-15.03,"peak_price_180d":135000.0,"peak_date_180d":"2024-06-19","trough_price_180d":95000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_anchor","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Yellow_after_capital_return_roe_bridge_repaired","residual_error_type":"positive_auto_valueup_path_requires_url_repaired_capital_return_roe_margin_evidence_before_green"}
{"row_type":"trigger","research_id":"R12L73_C31_AUTO_VALUEUP_ROUTER","round":"R12","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_CORPORATE_VALUE_UP_AUTO_CAPITAL_RETURN_EXECUTION_ROUTER","symbol":"012330","name":"현대모비스","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"auto_parts_low_pbr_governance_capital_return_rerating","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":234500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":15.14,"mae_30d_pct":-1.92,"mfe_90d_pct":15.14,"mae_90d_pct":-6.18,"mfe_180d_pct":15.14,"mae_180d_pct":-14.50,"peak_price_180d":270000.0,"peak_date_180d":"2024-03-18","trough_price_180d":200500.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_to_Yellow_if_governance_capital_return_bridge_repaired","residual_error_type":"auto_parts_valueup_path_constructive_but_green_requires_company_execution_evidence"}
{"row_type":"trigger","research_id":"R12L73_C31_AUTO_VALUEUP_ROUTER","round":"R12","loop":73,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_CORPORATE_VALUE_UP_AUTO_CAPITAL_RETURN_EXECUTION_ROUTER","symbol":"011210","name":"현대위아","trigger_type":"Stage2-FalsePositive-Candidate","trigger_family":"auto_supplier_valueup_policy_relief_without_execution_bridge","trigger_date":"2024-02-26","entry_date":"2024-02-27","entry_price":59800.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":1.84,"mae_30d_pct":-5.52,"mfe_90d_pct":1.84,"mae_90d_pct":-8.86,"mfe_180d_pct":3.18,"mae_180d_pct":-23.99,"peak_price_180d":61700.0,"peak_date_180d":"2024-06-18","trough_price_180d":45450.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_weak_mfe_material_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"blocked_Stage2_or_Stage2_Guarded_until_execution_bridge_repaired","residual_error_type":"policy_relevance_without_auto_supplier_execution_bridge_low_mfe_later_drawdown"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | policy relevance | capital-return visibility | ROE / margin bridge | governance / execution bridge | market mispricing | valuation rerating | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `000270` | 14 | 13 | 12 | 10 | 13 | 12 | 7 | 81 | Stage2/Yellow after capital-return / ROE evidence repair |
| `012330` | 13 | 10 | 9 | 10 | 11 | 10 | 7 | 70 | Stage2-Guarded / Yellow after execution bridge repair |
| `011210` | 11 | 4 | 5 | 4 | 5 | 4 | 5 | 38 | blocked Stage2 or guarded only until execution repair |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C31 problem is **policy relevance without company-specific execution**:

```text
C31 clean auto value-up path:
  policy event relevance
  + strong MFE
  + contained MAE
  + URL-repaired capital-return / ROE / governance evidence
  => Stage2-Actionable / Stage3-Yellow, possible Green after proof

C31 auto-parts guarded path:
  policy relevance is plausible
  + MFE is moderate
  + drawdown is manageable
  + execution bridge is still source_proxy_only
  => Stage2-Actionable-Guarded, no Green

C31 supplier false-positive path:
  policy label exists
  + MFE_30D < +5%
  + no company-specific capital-return / margin bridge
  + later MAE approaches high-MAE zone
  => block Stage2 or keep guarded until evidence repair
```

`000270` prevents overblocking.  
`012330` shows a constructive but still evidence-pending route.  
`011210` shows why C31 cannot boost every auto-adjacent supplier on policy relevance alone.

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R12L73_C31_AUTO_VALUEUP_ROUTER",
  "round": "R12",
  "loop": 73,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "KOREA_CORPORATE_VALUE_UP_AUTO_CAPITAL_RETURN_EXECUTION_ROUTER",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 11.59,
  "avg_mae_30d_pct": -2.72,
  "avg_mfe_90d_pct": 11.59,
  "avg_mae_90d_pct": -7.99,
  "avg_mfe_180d_pct": 13.02,
  "avg_mae_180d_pct": -17.84,
  "max_mfe_180d_pct": 20.75,
  "worst_mae_180d_pct": -23.99
}
```

---

## 10. 4B proximity split

```json
{
  "row_type": "4b_split",
  "research_id": "R12L73_C31_AUTO_VALUEUP_ROUTER",
  "stage2_positive_or_yellow_candidate": [
    {
      "symbol": "000270",
      "reason": "meaningful 180D MFE of +20.75% and contained early MAE; requires capital-return and ROE bridge before Green"
    },
    {
      "symbol": "012330",
      "reason": "constructive 30D/90D path and manageable 180D drawdown; requires governance/capital-return execution bridge before Yellow/Green"
    }
  ],
  "local_4b_or_blocked_stage2_watch": [
    {
      "symbol": "011210",
      "reason": "MFE_30D was only +1.84% and MFE_180D only +3.18%, while MAE_180D reached -23.99%"
    }
  ],
  "full_4b_or_green_requires_non_price_evidence": [
    "company-specific value-up plan",
    "dividend / buyback / total shareholder return execution",
    "ROE and operating-margin bridge",
    "governance / capital allocation plan",
    "auto volume, mix, and cash-flow durability"
  ]
}
```

---

## 11. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_CORPORATE_VALUE_UP_AUTO_CAPITAL_RETURN_EXECUTION_ROUTER
rule_name: C31_auto_valueup_execution_bridge_and_weak_mfe_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C31 Korea value-up / auto-capital-return policy cases:

Tier A: verified auto capital-return rerating
  Conditions:
    - policy event relevance is clear
    - company-specific shareholder-return, ROE, governance, or value-up execution evidence is URL-repaired
    - 30D/90D MAE remains contained
    - MFE persists beyond the policy announcement window
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after evidence repair
    - Green only after capital-return / ROE / margin evidence is verified

Tier B: auto-parts policy-relevant guarded case
  Conditions:
    - policy relevance is plausible
    - MFE is moderate and drawdown remains manageable
    - evidence_url_pending or source_proxy_only remains true
  Routing:
    - Stage2-Actionable-Guarded at most
    - no Green
    - no production positive weight promotion

Tier C: weak-MFE supplier policy false-positive
  Conditions:
    - MFE_30D < +5%
    - MFE_180D < +5%
    - MAE_180D <= -20%
    - no company-specific capital-return or operating bridge
  Routing:
    - block Stage2 or keep Stage2-Guarded only
    - local 4B/high-MAE watch
    - count as counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c31_auto_valueup_execution_bridge_and_weak_mfe_router",
  "scope": "canonical_archetype_id:C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "policy_relevance_alone_green_allowed": false,
    "capital_return_roe_governance_bridge_required_for_green": true,
    "auto_supplier_weak_mfe_threshold_30d_pct": 5.0,
    "auto_supplier_weak_mfe_threshold_180d_pct": 5.0,
    "auto_supplier_high_mae_watch_threshold_180d_pct": -20.0,
    "positive_weight_blocked_until_url_repair": true
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Two constructive auto value-up paths and one weak-MFE auto-supplier counterexample show that C31 should not boost all auto-adjacent names on policy relevance alone. Green requires company-specific capital-return, ROE, governance, margin, and cash-flow evidence."
}
```

---

## 12. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R12L73_C31_AUTO_VALUEUP_ROUTER",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "contribution": "Adds three C31 Korea value-up auto-capital-return cases and separates clean auto value-up paths from an auto-supplier policy-relief false positive. C31 Green should require URL-repaired company-specific shareholder-return, ROE, governance, margin, and cash-flow evidence.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price value-up execution triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C31 policy relevance alone cannot create Green; auto-supplier cases with MFE_30D < +5%, MFE_180D < +5%, and MAE_180D <= -20% should block Stage2 or route to local 4B/high-MAE watch."
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
    000270: false
    012330: false
    011210: false
  evidence_url_pending:
    000270: true
    012330: true
    011210: true
  source_proxy_only:
    000270: true
    012330: true
    011210: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C31 auto value-up policy-event residual shape and weak-MFE guardrail design, but should not promote positive weights until filings, IR, exchange disclosures, or regulatory documents verify company-specific value-up plans, shareholder return, buybacks, dividend policy, governance reform, ROE, margin, and cash-flow bridge.
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
2. Preserve R12 / loop 73 metadata.
3. Add the cases to C31_POLICY_SUBSIDY_LEGISLATION_EVENT only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/exchange-disclosure/regulatory data verifies company-specific value-up plans, shareholder return, buybacks, dividend policy, governance reform, ROE, margin, and cash-flow bridge.
6. Add a shadow-only rule candidate named C31_auto_valueup_execution_bridge_and_weak_mfe_router.
7. Do not loosen Stage3-Green.
8. Add C31-specific guards:
   - source_proxy_only -> no Green
   - policy relevance alone -> no Green
   - Stage3-Yellow/Green requires company-specific execution bridge
   - auto supplier with MFE_30D < +5%, MFE_180D < +5%, and MAE_180D <= -20% -> blocked Stage2 or local 4B/high-MAE watch
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 15. Next round state

```text
completed_round = R12
completed_loop = 73
next_round = R13
next_loop = 73
next_large_sector_hint = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
next_allowed_scope = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW or R13_CROSS_ARCHETYPE_4B_4C_REDTEAM or R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION or R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
