# E2R Stock-Web v12 Residual Research — R4 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R4
completed_loop: 72
next_round: R5
next_loop: 72
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_SUPERCYCLE_FABRICATOR_AND_INTEGRATED_PRODUCER_SPREAD
output_file: e2r_stock_web_v12_residual_round_R4_loop_72_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
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

### Round resolution

The immediately preceding completed scheduled artifact in this automation chain was:

```text
completed_round = R3
completed_loop = 72
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

Therefore:

```text
scheduled_round = R4
scheduled_loop = 72
```

R4 maps to:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

This run selects:

```text
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
```

This is a valid R4/L4 pairing.

---

## 1. Why this R4/C15 run

The no-repeat ledger shows C15 is covered, but its top-covered symbols are steel/material names rather than the copper-fabricator path tested here:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE:
  rows: 56
  symbols: 23
  date_range: 2020-08-10~2024-09-13
  good/bad S2: 20/3
  4B/4C: 15/0
  top covered symbols: 005490(9), 004020(7), 001430(4), 018470(4), 001230(3), 011170(3)
```

This run adds a copper-specific fine-archetype:

```text
fine_archetype_id = COPPER_SUPERCYCLE_FABRICATOR_AND_INTEGRATED_PRODUCER_SPREAD
```

Research question:

```text
When copper-price supercycle narratives lift all copper-linked names, can C15 separate integrated producer / defense-hedged positives from thin fabricator price-only or high-MAE blowoff paths?
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

| symbol | name | market | profile status | corporate-action candidate overlap with selected 180D window | calibration usable |
|---|---|---|---|---|---|
| `103140` | 풍산 | KOSPI | active_like | none listed | true |
| `025820` | 이구산업 | KOSPI | active_like | none in 2024 test window; old 1996/2007 candidates only | true |
| `012800` | 대창 | KOSPI | active_like | none in 2024 test window; old 1998/2008 candidates only | true |

Profile caveat:

```text
Stock-Web OHLC is raw/unadjusted marcap data. These cases are calibration-safe for the selected 2024 windows because no listed corporate-action candidate overlaps each entry~D+180 test window.
```

---

## 3. Evidence status and trigger discipline

This artifact uses a conservative evidence setting:

```text
evidence_url_pending = true
source_proxy_only = true
```

Reason:

```text
The Stock-Web price path is fully validated, but company-level spread/contract/margin evidence and copper price source evidence still require later URL repair through filings, IR, commodities data, or reports before any production weight promotion.
```

C15 interpretation:

```text
C15 is not simply “copper-linked stocks went up.”
The model should ask whether the company has:
- realizable spread / inventory / pricing leverage,
- structural shortage or cost-curve support,
- revenue or margin conversion,
- or only beta-like commodity theme exposure.
```

This run is therefore a residual-shape and guardrail file, not a production patch proposal.

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Searches performed before writing:

```text
103140 + C15_MATERIAL_SPREAD_SUPERCYCLE -> no direct match found
025820 + C15_MATERIAL_SPREAD_SUPERCYCLE -> no direct match found
012800 + C15_MATERIAL_SPREAD_SUPERCYCLE -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "minimum_positive_case_count": 1,
  "minimum_counterexample_count": 1,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass",
  "data_quality_status": "source_proxy_only_non_price_evidence"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | research role |
|---|---|---|---|
| `R4L72_C15_103140_20240415` | `103140` 풍산 | copper supercycle + integrated producer/defense hedge | positive-guarded C15 Stage2 |
| `R4L72_C15_025820_20240415` | `025820` 이구산업 | copper fabricator high-beta spread theme | positive MFE but high-MAE counterexample |
| `R4L72_C15_012800_20240521` | `012800` 대창 | copper fabricator blowoff after theme acceleration | price-theme blowoff / failed follow-through counterexample |

The intended residual:

```text
C15 should not use commodity beta MFE alone.
It should separate integrated producer / margin bridge cases from fabricator-theme blowoffs whose MFE arrives before any verified margin conversion and then reverses deeply.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `103140` 풍산 — integrated copper/defense hedge positive, but high-MAE guard

Trigger:

```text
trigger_date = 2024-04-12
trigger_type = Stage2-Actionable-Guarded
trigger_family = copper_supercycle_integrated_producer_margin_bridge
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
103140 is the cleaner C15 case because it has integrated copper exposure and defense-adjacent business mix.
However, even this cleaner path suffered -25.87% 180D MAE after the first copper peak.
Correct route: Stage2-Actionable-Guarded / Stage3-Yellow only after verified spread or earnings conversion, not immediate Green.
```

### 6.2 `025820` 이구산업 — high-beta copper fabricator with strong MFE and deep reversal

Trigger:

```text
trigger_date = 2024-04-12
trigger_type = Stage2-Actionable-Guarded
trigger_family = copper_fabricator_spread_supercycle_beta
entry_date = 2024-04-15
entry_price = 6000.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-04-12,5690.0,6090.0,5460.0,5700.0,15223035.0,89166441390.0,190619400000.0,33442000,KOSPI
2024-04-15,6000.0,6940.0,5890.0,6570.0,37392612.0,244197762220.0,219713940000.0,33442000,KOSPI
2024-04-19,6640.0,7310.0,6410.0,6790.0,47804175.0,332468400980.0,227071180000.0,33442000,KOSPI
2024-05-14,7290.0,8030.0,6970.0,7520.0,32999363.0,250635431510.0,251483840000.0,33442000,KOSPI
2024-05-20,7700.0,8420.0,7400.0,7880.0,47603058.0,381542856790.0,263522960000.0,33442000,KOSPI
2024-06-10,5380.0,5570.0,5350.0,5550.0,899704.0,4893791850.0,185603100000.0,33442000,KOSPI
2024-08-05,4365.0,4430.0,3795.0,3930.0,805374.0,3285423220.0,131427060000.0,33442000,KOSPI
2024-09-25,4990.0,5340.0,4780.0,4870.0,7851705.0,40039841520.0,162862540000.0,33442000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 8030 | 2024-05-14 | 5820 | 2024-04-17 | +33.83% | -3.00% |
| 90 calendar days | 8420 | 2024-05-20 | 4925 | 2024-07-03 | +40.33% | -17.92% |
| 180 calendar days | 8420 | 2024-05-20 | 3795 | 2024-08-05 | +40.33% | -36.75% |

Interpretation:

```text
025820 looks excellent on 30D MFE, but the 180D path reveals the fabricator-beta problem.
Without verified spread capture, the model should not promote this to Green. It is Stage2-Guarded at best, then 4B/high-MAE watch once reversal begins.
```

### 6.3 `012800` 대창 — copper theme blowoff after acceleration

Trigger:

```text
trigger_date = 2024-05-20
trigger_type = 4B-local-watch
trigger_family = copper_fabricator_theme_blowoff_after_acceleration
entry_date = 2024-05-21
entry_price = 2185.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-05-20,1695.0,2080.0,1687.0,2080.0,40234917.0,77451765879.0,189572237920.0,91140499,KOSPI
2024-05-21,2185.0,2320.0,2080.0,2175.0,69505626.0,152388771765.0,198230585325.0,91140499,KOSPI
2024-05-22,2195.0,2210.0,2000.0,2060.0,14874146.0,31303904500.0,187749427940.0,91140499,KOSPI
2024-05-30,1723.0,1740.0,1630.0,1638.0,4003930.0,6686351839.0,149288137362.0,91140499,KOSPI
2024-06-19,1470.0,1487.0,1375.0,1457.0,1105008.0,1607771039.0,132791707043.0,91140499,KOSPI
2024-08-05,1277.0,1283.0,1100.0,1161.0,1724372.0,2078029050.0,105814119339.0,91140499,KOSPI
2024-09-24,1265.0,1301.0,1265.0,1300.0,534924.0,718205446.0,118482648700.0,91140499,KOSPI
2024-10-24,1267.0,1267.0,1238.0,1238.0,192860.0,241304673.0,112831937762.0,91140499,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30 calendar days | 2320 | 2024-05-21 | 1375 | 2024-06-19 | +6.18% | -37.07% |
| 90 calendar days | 2320 | 2024-05-21 | 1100 | 2024-08-05 | +6.18% | -49.66% |
| 180 calendar days | 2320 | 2024-05-21 | 1100 | 2024-08-05 | +6.18% | -49.66% |

Interpretation:

```text
012800 is the clean counterexample.
The entry after the theme acceleration had almost no remaining upside but enormous downside.
This should be blocked from Stage2/Green and routed as 4B-local-watch or price-theme blowoff counterexample unless verified margin/spread evidence appears before the move.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R4L72_C15_COPPER_SUPERCYCLE_SPREAD","round":"R4","loop":72,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SUPERCYCLE_FABRICATOR_AND_INTEGRATED_PRODUCER_SPREAD","symbol":"103140","name":"풍산","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"copper_supercycle_integrated_producer_margin_bridge","trigger_date":"2024-04-12","entry_date":"2024-04-15","entry_price":63400.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":24.45,"mae_30d_pct":-10.41,"mfe_90d_pct":24.45,"mae_90d_pct":-12.30,"mfe_180d_pct":24.45,"mae_180d_pct":-25.87,"peak_price_180d":78900.0,"peak_date_180d":"2024-05-14","trough_price_180d":47000.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"positive_guarded","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"medium_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_to_Yellow_if_spread_bridge_verified","residual_error_type":"green_requires_verified_spread_or_margin_bridge"}
{"row_type":"trigger","research_id":"R4L72_C15_COPPER_SUPERCYCLE_SPREAD","round":"R4","loop":72,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SUPERCYCLE_FABRICATOR_AND_INTEGRATED_PRODUCER_SPREAD","symbol":"025820","name":"이구산업","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"copper_fabricator_spread_supercycle_beta","trigger_date":"2024-04-12","entry_date":"2024-04-15","entry_price":6000.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":33.83,"mae_30d_pct":-3.00,"mfe_90d_pct":40.33,"mae_90d_pct":-17.92,"mfe_180d_pct":40.33,"mae_180d_pct":-36.75,"peak_price_180d":8420.0,"peak_date_180d":"2024-05-20","trough_price_180d":3795.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_high_mfe_high_mae","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Guarded_or_4B_high_MAE_watch","residual_error_type":"fabricator_beta_high_MAE_without_verified_spread_capture"}
{"row_type":"trigger","research_id":"R4L72_C15_COPPER_SUPERCYCLE_SPREAD","round":"R4","loop":72,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SUPERCYCLE_FABRICATOR_AND_INTEGRATED_PRODUCER_SPREAD","symbol":"012800","name":"대창","trigger_type":"4B-local-watch","trigger_family":"copper_fabricator_theme_blowoff_after_acceleration","trigger_date":"2024-05-20","entry_date":"2024-05-21","entry_price":2185.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":6.18,"mae_30d_pct":-37.07,"mfe_90d_pct":6.18,"mae_90d_pct":-49.66,"mfe_180d_pct":6.18,"mae_180d_pct":-49.66,"peak_price_180d":2320.0,"peak_date_180d":"2024-05-21","trough_price_180d":1100.0,"trough_date_180d":"2024-08-05","calibration_usable":true,"case_polarity":"counterexample_price_theme_blowoff","evidence_url_pending":true,"source_proxy_only":true,"non_price_evidence_strength":"low_pending_url_repair","price_only_blowoff":true,"expected_stage_current_profile":"blocked_Stage2_or_4B_local_watch","residual_error_type":"post_acceleration_copper_theme_entry_low_MFE_extreme_MAE"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | EPS/FCF | spread visibility | structural shortage/pricing | market mispricing | valuation rerating | capital allocation | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `103140` | 10 | 12 | 13 | 10 | 9 | 5 | 7 | 66 | Stage2-Guarded / Yellow after spread bridge |
| `025820` | 5 | 6 | 9 | 11 | 8 | 3 | 5 | 47 | 4B/high-MAE watch unless verified spread capture |
| `012800` | 3 | 3 | 6 | 8 | 5 | 2 | 4 | 31 | blocked Stage2 / 4B-local-watch |

### Current calibrated profile stress test

The current calibrated profile already blocks price-only blowoff.  
The remaining C15 issue is **commodity-spread conversion**:

```text
C15 clean positive path:
  direct commodity exposure
  + realizable spread/inventory/margin bridge
  + controlled MAE
  => Stage2-Actionable / Yellow; Green only after verified margin conversion

C15 false-positive path:
  commodity-linked ticker
  + theme acceleration
  + weak or proxy-only spread evidence
  + 180D MAE worse than -25%
  => Stage2-Guarded, 4B/high-MAE watch, or blocked positive stage
```

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R4L72_C15_COPPER_SUPERCYCLE_SPREAD",
  "round": "R4",
  "loop": 72,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "COPPER_SUPERCYCLE_FABRICATOR_AND_INTEGRATED_PRODUCER_SPREAD",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_guarded_case_count": 1,
  "counterexample_count": 2,
  "new_symbol_count": 3,
  "source_proxy_only_count": 3,
  "evidence_url_pending_count": 3,
  "avg_mfe_30d_pct": 21.49,
  "avg_mae_30d_pct": -16.83,
  "avg_mfe_90d_pct": 23.65,
  "avg_mae_90d_pct": -26.63,
  "avg_mfe_180d_pct": 23.65,
  "avg_mae_180d_pct": -37.43,
  "worst_mae_180d_pct": -49.66
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_SUPERCYCLE_FABRICATOR_AND_INTEGRATED_PRODUCER_SPREAD
rule_name: C15_copper_spread_bridge_and_high_mae_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C15 copper/material spread supercycle cases:

Tier A: integrated producer / direct spread bridge
  Conditions:
    - direct commodity exposure
    - pricing or inventory leverage can plausibly flow into earnings
    - spread/margin bridge is URL-repaired
  Routing:
    - Stage2-Actionable allowed
    - Stage3-Yellow allowed after verified bridge
    - Green only after actual margin / EPS / OP conversion

Tier B: fabricator beta without verified spread capture
  Conditions:
    - stock is commodity-linked
    - rally follows commodity theme
    - spread capture is source-proxy-only
  Routing:
    - Stage2-Actionable-Guarded at most
    - no Green
    - monitor 4B/high-MAE

Tier C: post-acceleration theme blowoff
  Conditions:
    - entry occurs after large theme burst
    - MFE is small
    - MAE worse than -25%
  Routing:
    - block Stage2
    - local 4B watch / false-positive counterexample
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c15_copper_spread_bridge_and_high_mae_router",
  "scope": "canonical_archetype_id:C15_MATERIAL_SPREAD_SUPERCYCLE",
  "proposal": {
    "source_proxy_only_green_allowed": false,
    "spread_bridge_required_for_green": true,
    "fabricator_beta_stage2_cap": "guarded_only",
    "post_acceleration_theme_entry_blocks_stage2": true,
    "high_mae_watch_threshold_pct": -25.0
  },
  "confidence": "medium_low_until_url_repair",
  "apply_now": false,
  "reason": "Three new C15 copper-linked cases show that integrated producer exposure and fabricator beta need separate routing. Fabricator-theme cases can show high MFE but extreme 180D MAE without verified spread capture."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R4L72_C15_COPPER_SUPERCYCLE_SPREAD",
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "contribution": "Adds three less-repeated C15 copper-linked cases and separates integrated producer spread-bridge positives from fabricator-beta and post-acceleration blowoff counterexamples.",
  "positive_case_added": 1,
  "counterexample_case_added": 2,
  "new_symbol_count": 3,
  "data_quality_blocker": "All three non-price spread triggers require URL-level repair before positive weight promotion.",
  "guardrail_added": "C15 Green requires verified spread/margin bridge; source_proxy_only fabricator-beta rallies with 180D MAE worse than -25% should route to high-MAE watch or blocked Stage2."
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
    103140: false
    025820: false
    012800: false
  evidence_url_pending:
    103140: true
    025820: true
    012800: true
  source_proxy_only:
    103140: true
    025820: true
    012800: true
```

Limitations:

```text
- Price path is validated against Stock-Web tradable OHLC rows.
- Non-price evidence is not URL-repaired in this run.
- Therefore this artifact is useful for C15 copper-spread residual shape and high-MAE guardrail design, but should not promote positive weights until company-level spread, inventory, margin, or report evidence is attached.
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
2. Preserve R4 / loop 72 metadata.
3. Add the cases to C15_MATERIAL_SPREAD_SUPERCYCLE only if parser validation passes.
4. Treat all three non-price triggers as evidence_url_pending=true and source_proxy_only=true until URL-level evidence is repaired.
5. Do not use these rows for positive weight promotion until filings/IR/report/commodity-spread evidence verifies company-level spread, margin, inventory, or earnings conversion.
6. Add a shadow-only rule candidate named C15_copper_spread_bridge_and_high_mae_router.
7. Do not loosen Stage3-Green.
8. Add C15-specific guards:
   - source_proxy_only fabricator beta -> no Green
   - post-acceleration theme entry with low MFE and MAE worse than -25% -> block Stage2
   - Green requires spread/margin/EPS conversion
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R4
completed_loop = 72
next_round = R5
next_loop = 72
next_large_sector_hint = L5_CONSUMER_BRAND_DISTRIBUTION
```
