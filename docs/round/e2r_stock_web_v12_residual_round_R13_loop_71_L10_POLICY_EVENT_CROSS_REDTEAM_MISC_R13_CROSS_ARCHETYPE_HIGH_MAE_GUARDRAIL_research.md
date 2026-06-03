# E2R Stock-Web v12 Residual Research — R13 Loop 71

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R13
completed_loop: 71
next_round: R1
next_loop: 72
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: HIGH_MFE_HIGH_MAE_EVENT_PATH_GUARDRAIL
output_file: e2r_stock_web_v12_residual_round_R13_loop_71_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Execution gate

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as the active execution procedure.  
`docs/core/V12_Research_No_Repeat_Index.md` is used only as the duplicate-avoidance ledger.

This is not a live stock-discovery run, not a trading recommendation, and not a `stock_agent` code patch.  
The only output is a standalone historical calibration / residual-research Markdown artifact.

### Round resolution

The immediately preceding automation artifact was:

```text
completed_round = R12
completed_loop  = 71
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Therefore:

```text
scheduled_round = R13
scheduled_loop  = 71
```

R13 is not a sector-specific round. It is a cross-archetype RedTeam / 4B / 4C / accounting trust / high-MAE checkpoint.  
This run selects:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

This is a valid R13 pairing.

---

## 1. Price atlas validation

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

Manifest notes used in this run:

```text
- OHLC is raw/unadjusted.
- Calibration shards exclude zero-volume and invalid OHLC rows.
- Corporate-action-contaminated windows are blocked by default.
- Forward windows are judged against manifest max_date = 2026-02-20.
```

---

## 2. No-repeat and R13 novelty check

The no-repeat ledger defines hard duplicate as:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This R13 file is not adding another C29/C30/C31/C32 sector-specific artifact. It aggregates already observed paths into the special R13 checkpoint:

```text
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

The no-repeat ledger shows R13 high-MAE coverage is much smaller than several sector-specific archetypes:

```text
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL:
  rows: 23
  symbols: 21
  date_range: 2020-11-06~2024-07-22
  good/bad S2: 3/5
  4B/4C: 5/4
```

Novelty of this R13 loop:

```json
{
  "cross_archetype_review": true,
  "source_archetypes_covered": [
    "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
    "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
    "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
    "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"
  ],
  "source_rounds_covered": ["R9", "R10", "R11", "R12"],
  "new_r13_scope": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "sector_specific_output": false,
  "duplicate_status": "pass"
}
```

Important reuse policy:

```text
R13 may reuse source cases from R1~R12 as cross-case evidence.
These reused cases are not counted as new sector-specific C29/C30/C31/C32 cases.
The new contribution is the cross-archetype guardrail synthesis.
```

---

## 3. Research question

Across very different archetypes, the same trap repeats:

```text
A stock shows high MFE after an event, but the path also contains deep MAE or fast post-peak collapse.
If the model lets high MFE substitute for durable non-price evidence, it will produce false Stage2/Green or delayed 4B/4C decisions.
```

This R13 checkpoint asks:

```text
Can one cross-archetype high-MAE governor reduce false positives without over-blocking genuine repair/bridge cases?
```

The mechanism is similar to a bridge load test. The headline price jump is like a truck crossing the bridge; MAE and post-peak drawdown reveal whether the structure actually held.

---

## 4. Case set

| review_case_id | source round | source archetype | symbol | role | R13 use |
|---|---|---|---|---|---|
| `R13L71_C30_002990_HIGH_MAE_FALSE_POSITIVE` | R10 | C30 | `002990` 금호건설 | low valuation / PF overhang without repair bridge | bad Stage2 / high-MAE false positive |
| `R13L71_C31_008970_POLICY_THEME_HIGH_MAE` | R11 | C31 | `008970` 동양철관 | indirect policy-theme beneficiary | price-event high MFE but high MAE |
| `R13L71_C32_036560_TENDER_CAP_HIGH_MAE` | R12 | C32 | `036560` 영풍정밀 | direct tender affiliate target near cap | cap-zone 4B / severe post-cap MAE |
| `R13L71_C32_000670_CONTROL_VEHICLE_HIGH_MAE` | R12 | C32 | `000670` 영풍 | acquirer-side / shareholder-control vehicle | governance-event high-MAE guard |
| `R13L71_C29_010690_PEAK_TO_TROUGH_4B` | R9 | C29 | `010690` 화신 | successful mobility rerating then sharp drawdown | positive case requiring timely 4B |
| `R13L71_C30_014790_REPAIR_BRIDGE_ESCAPE` | R10 | C30 | `014790` HL D&I | repairable overhang / low-MAE positive path | escape hatch: do not over-block repair cases |

Case balance:

```json
{
  "high_mae_counterexample_count": 4,
  "positive_then_4b_watch_count": 1,
  "escape_hatch_positive_count": 1,
  "cross_archetype_count": 4,
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw"
}
```

---

## 5. Stock-Web OHLC evidence and path metrics

### 5.1 C30 / `002990` 금호건설 — low valuation is not a repair bridge

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-31,5200.0,5210.0,5100.0,5210.0,39964.0,206584160.0,192528229950.0,36953595,KOSPI
2024-02-01,5250.0,5280.0,5190.0,5200.0,40300.0,211092790.0,192158694000.0,36953595,KOSPI
2024-10-25,2920.0,2990.0,2850.0,2870.0,40273.0,116185490.0,106056817650.0,36953595,KOSPI
```

Backtest:

```text
entry_date = 2024-01-31
entry_price = 5210.0
peak_price_180D = 5280.0
trough_price_180D = 2850.0
MFE_180D = +1.34%
MAE_180D = -45.30%
```

R13 interpretation:

```text
This is the cleanest high-MAE false positive in the set.
If C30 valuation cheapness or construction-cycle recovery language substitutes for balance-sheet repair evidence, the model would give Stage2 credit to a path with almost no upside and -45% MAE.
```

### 5.2 C31 / `008970` 동양철관 — indirect policy-theme MFE is not a bridge

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-06-04,1175.0,1175.0,1175.0,1175.0,7102951.0,8345967154.0,139690215750.0,118885290,KOSPI
2024-06-07,1610.0,1678.0,1285.0,1411.0,142968215.0,211189736927.0,167747144190.0,118885290,KOSPI
2024-08-05,985.0,987.0,826.0,890.0,6103922.0,5607437467.0,129945030280.0,146005652,KOSPI
```

Backtest:

```text
entry_date = 2024-06-04
entry_price = 1175.0
peak_price_180D = 1678.0
trough_price_180D = 826.0
MFE_180D = +42.81%
MAE_180D = -29.70%
```

R13 interpretation:

```text
This has large MFE, but it is an indirect policy-theme path.
Without named order / tender / contract / capex conversion, the model should classify it as local 4B watch or blocked positive stage.
```

### 5.3 C32 / `036560` 영풍정밀 — tender cap zone with severe post-cap MAE

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-10-14,30500.0,31400.0,30100.0,30750.0,1974665.0,60672934200.0,484312500000.0,15750000,KOSDAQ
2024-10-25,31200.0,32700.0,21100.0,22700.0,2888203.0,81884563050.0,357525000000.0,15750000,KOSDAQ
2024-11-13,16050.0,16260.0,15190.0,15220.0,189485.0,2948301750.0,239715000000.0,15750000,KOSDAQ
2025-04-07,10410.0,11010.0,10260.0,10290.0,29357.0,304742730.0,162067500000.0,15750000,KOSDAQ
```

Backtest:

```text
entry_date = 2024-10-14
entry_price = 30500.0
peak_price_180D = 32700.0
trough_price_180D = 10260.0
MFE_180D = +7.21%
MAE_180D = -66.36%
```

R13 interpretation:

```text
This is a direct tender-related instrument, but the entry was near the cap zone.
The low MFE and extreme MAE argue for Stage4B-CapGuard, not Stage2/Green.
```

### 5.4 C32 / `000670` 영풍 — acquirer-side control vehicle with high MAE

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-09-19,487500.0,501000.0,487000.0,501000.0,24086.0,11904668500.0,922862040000.0,1842040,KOSPI
2024-09-20,620000.0,649000.0,533000.0,570000.0,195343.0,115622888000.0,1049962800000.0,1842040,KOSPI
2024-10-08,346000.0,346000.0,335500.0,336500.0,18092.0,6104147000.0,619846460000.0,1842040,KOSPI
```

Backtest:

```text
entry_date = 2024-09-19
entry_price = 487500.0
peak_price_180D = 649000.0
trough_price_180D = 335500.0
MFE_180D = +33.13%
MAE_180D = -31.18%
```

R13 interpretation:

```text
Acquirer-side / shareholder-control vehicles can show real event relevance but poor clean-cashflow visibility.
The correct route is guarded Stage2 or local 4B watch, not Green.
```

### 5.5 C29 / `010690` 화신 — valid rerating can still require timely 4B

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2023-04-12,13990.0,16240.0,13650.0,14600.0,9719863.0,144081703290.0,509837986000.0,34920410,KOSPI
2023-07-06,20000.0,22700.0,20000.0,21000.0,3849431.0,82884467200.0,733328610000.0,34920410,KOSPI
2023-08-16,14900.0,14910.0,13210.0,13330.0,1469962.0,20001003930.0,465489065300.0,34920410,KOSPI
```

Backtest:

```text
entry_date = 2023-04-12
entry_price = 14600.0
peak_price_180D = 22700.0
trough_price_180D = 9940.0_to_10460.0_proxy_range
MFE_180D = +55.48%
MAE_180D = -31.92%
drawdown_after_peak = -56.21%
```

R13 interpretation:

```text
This is not a false positive. It is a positive rerating path with a later 4B need.
The high-MAE governor must not block Stage2 when a real volume/margin bridge exists; it should demand earlier 4B watch once peak proximity and reversal evidence arrive.
```

### 5.6 C30 / `014790` HL D&I — repair bridge escape hatch

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-31,2045.0,2090.0,2035.0,2075.0,89603.0,184618220.0,78556597075.0,37858601,KOSPI
2024-04-17,1928.0,1943.0,1928.0,1937.0,24705.0,47846373.0,73332110137.0,37858601,KOSPI
2024-08-23,2645.0,2880.0,2625.0,2870.0,371789.0,1035857620.0,108654184870.0,37858601,KOSPI
```

Backtest:

```text
entry_date = 2024-01-31
entry_price = 2075.0
peak_price_180D = 2880.0
trough_price_180D = 1928.0
MFE_180D = +38.80%
MAE_180D = -7.08%
```

R13 interpretation:

```text
This is the escape hatch. C30 should not hard-block every construction/PF-related name.
If a repair bridge exists and MAE remains low, Stage2/local 4B watch can remain valid.
```

---

## 6. Cross-archetype diagnosis

### 6.1 Common failure mode

The repeated failure mode is not “the stock went down.” It is:

```text
MFE looks large enough to validate the thesis, but MAE or post-peak collapse shows the evidence bridge was brittle.
```

This appears in different clothes:

| source archetype | false-positive costume | what the guard should notice |
|---|---|---|
| C30 PF / construction | cheap valuation / repair rumor | no verified balance-sheet repair bridge |
| C31 policy event | indirect theme beneficiary | no named order / contract / capex conversion |
| C32 tender control | cap-zone or acquirer vehicle | tender mechanics dominate, not FCF rerating |
| C29 mobility | true rerating that later rolls over | Stage2 may be correct, but 4B should arrive earlier |

### 6.2 Proposed R13 governor

```text
high_mae_guardrail_trigger:
  if MFE_30D_or_90D >= +20%
  and MAE_90D_or_180D <= -25%
  and non_price_bridge_strength in [none, weak, proxy_only]
then:
  block Stage3-Green
  block new positive weight delta
  route to Stage4B-local-watch or RedTeam-high-MAE-review
```

Escape hatch:

```text
if verified non-price bridge exists
and MAE_90D_or_180D > -15%
then:
  do not block Stage2-Actionable
  keep Stage3-Green strict
  require separate 4B watch if peak proximity emerges
```

Special case:

```text
if case is direct tender target or cap-zone event
then:
  compare entry price to known offer/cap mechanics
  if post-entry MFE is limited and MAE is extreme:
      route to Stage4B-CapGuard
```

---

## 7. Machine-readable R13 review JSONL

```jsonl
{"row_type":"r13_review_trigger","research_id":"R13L71_HIGH_MAE_GUARDRAIL","round":"R13","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","name":"금호건설","trigger_type":"Stage2-FalsePositive-PF-Overhang-NoRepairBridge","entry_date":"2024-01-31","entry_price":5210.0,"mfe_180d_pct":1.34,"mae_180d_pct":-45.30,"peak_price_180d":5280.0,"trough_price_180d":2850.0,"r13_case_role":"high_mae_false_positive","bridge_strength":"weak_or_proxy_only","guardrail_verdict":"block_positive_stage_and_require_balance_sheet_repair_bridge","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","do_not_count_as_new_sector_case":true}
{"row_type":"r13_review_trigger","research_id":"R13L71_HIGH_MAE_GUARDRAIL","round":"R13","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"008970","name":"동양철관","trigger_type":"4B-local-watch","entry_date":"2024-06-04","entry_price":1175.0,"mfe_180d_pct":42.81,"mae_180d_pct":-29.70,"peak_price_180d":1678.0,"trough_price_180d":826.0,"r13_case_role":"policy_theme_high_mfe_high_mae","bridge_strength":"weak_indirect_theme","guardrail_verdict":"block_stage2_green_without_named_order_or_contract_bridge","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","do_not_count_as_new_sector_case":true}
{"row_type":"r13_review_trigger","research_id":"R13L71_HIGH_MAE_GUARDRAIL","round":"R13","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"036560","name":"영풍정밀","trigger_type":"Stage4B-CapGuard","entry_date":"2024-10-14","entry_price":30500.0,"mfe_180d_pct":7.21,"mae_180d_pct":-66.36,"peak_price_180d":32700.0,"trough_price_180d":10260.0,"r13_case_role":"tender_cap_high_mae_counterexample","bridge_strength":"event_mechanics_not_operating_bridge","guardrail_verdict":"stage4b_cap_guard_no_green","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","do_not_count_as_new_sector_case":true}
{"row_type":"r13_review_trigger","research_id":"R13L71_HIGH_MAE_GUARDRAIL","round":"R13","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"000670","name":"영풍","trigger_type":"Stage2-Actionable-Guarded","entry_date":"2024-09-19","entry_price":487500.0,"mfe_180d_pct":33.13,"mae_180d_pct":-31.18,"peak_price_180d":649000.0,"trough_price_180d":335500.0,"r13_case_role":"acquirer_side_control_vehicle_high_mae","bridge_strength":"governance_event_medium_but_no_clean_cashflow_bridge","guardrail_verdict":"guarded_stage2_or_local_4b_watch_no_green","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","do_not_count_as_new_sector_case":true}
{"row_type":"r13_review_trigger","research_id":"R13L71_HIGH_MAE_GUARDRAIL","round":"R13","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"010690","name":"화신","trigger_type":"Stage2-Actionable","entry_date":"2023-04-12","entry_price":14600.0,"mfe_180d_pct":55.48,"mae_180d_pct":-31.92,"peak_price_180d":22700.0,"post_peak_drawdown_pct":-56.21,"r13_case_role":"valid_stage2_but_4b_should_arrive_earlier","bridge_strength":"medium_to_high_operating_bridge","guardrail_verdict":"do_not_block_stage2_but_require_peak_proximity_4b_watch","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","do_not_count_as_new_sector_case":true}
{"row_type":"r13_review_trigger","research_id":"R13L71_HIGH_MAE_GUARDRAIL","round":"R13","loop":71,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014790","name":"HL D&I","trigger_type":"Stage2-RepairBridge-Counterexample","entry_date":"2024-01-31","entry_price":2075.0,"mfe_180d_pct":38.80,"mae_180d_pct":-7.08,"peak_price_180d":2880.0,"trough_price_180d":1928.0,"r13_case_role":"escape_hatch_low_mae_repair_bridge","bridge_strength":"medium_repair_bridge","guardrail_verdict":"allow_stage2_or_local_watch_do_not_green_loosen","calibration_usable":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","do_not_count_as_new_sector_case":true}
```

---

## 8. Cross-case aggregate

```json
{
  "row_type": "aggregate",
  "research_id": "R13L71_HIGH_MAE_GUARDRAIL",
  "round": "R13",
  "loop": 71,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "review_case_count": 6,
  "source_canonical_archetype_count": 4,
  "high_mae_counterexample_count": 4,
  "valid_stage2_but_4b_needed_count": 1,
  "escape_hatch_low_mae_positive_count": 1,
  "avg_mae_180d_high_mae_cases_pct": -43.14,
  "avg_mfe_180d_high_mae_cases_pct": 21.12,
  "worst_mae_180d_pct": -66.36,
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw"
}
```

---

## 9. Shadow rule candidate

```yaml
row_type: r13_cross_archetype_rule_candidate
rule_name: R13_high_mfe_high_mae_bridge_governor
scope: cross_archetype
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
production_scoring_changed: false
shadow_weight_only: true
```

### Rule logic

```text
If a trigger produces high MFE but also high MAE, do not infer structural quality from MFE alone.

Trigger condition:
  MFE_30D_or_90D >= +20%
  AND MAE_90D_or_180D <= -25%

Then inspect bridge strength:
  bridge = verified non-price earnings / order / backlog / repair / tender mechanics / cashflow evidence

If bridge_strength in [none, weak, proxy_only, indirect_theme]:
  - block Stage3-Green
  - block new positive weight delta
  - route to local 4B watch or RedTeam high-MAE review

If bridge_strength is verified and MAE is contained:
  - allow Stage2-Actionable
  - keep Green strict
  - use peak-proximity / reversal evidence for 4B watch

If tender-cap mechanics dominate:
  - apply C32 cap-zone or cap-inversion tier router
  - do not treat cap-zone price action as operating rerating
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "r13_high_mfe_high_mae_bridge_governor",
  "scope": "cross_archetype:R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "proposal": {
    "high_mfe_threshold_pct": 20.0,
    "high_mae_threshold_pct": -25.0,
    "weak_bridge_green_allowed": false,
    "weak_bridge_positive_delta_allowed": false,
    "verified_bridge_escape_hatch": true,
    "peak_proximity_4b_watch_required_for_valid_stage2_after_large_mfe": true
  },
  "confidence": "medium",
  "apply_now": false,
  "reason": "C29/C30/C31/C32 examples show the same price-path pathology: MFE alone is not enough when MAE or post-peak collapse is severe. The escape hatch prevents overblocking real repair or operating-bridge cases."
}
```

---

## 10. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R13L71_HIGH_MAE_GUARDRAIL",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "contribution": "Adds a cross-archetype high-MFE/high-MAE governor using C29, C30, C31, and C32 paths. The governor blocks Green/positive-delta promotion when MFE is paired with severe MAE and weak bridge evidence, while preserving Stage2 for verified bridge paths and requiring earlier 4B watch for valid reratings that later roll over.",
  "source_archetypes_reviewed": ["C29", "C30", "C31", "C32"],
  "counterexample_count": 4,
  "positive_escape_hatch_count": 1,
  "valid_stage2_4b_watch_count": 1,
  "guardrail_added": "MFE >= 20% plus MAE <= -25% requires bridge-strength routing before Stage2/Green/4B decisions.",
  "4b_split": {
    "local_4b_watch": ["008970", "000670"],
    "stage4b_cap_guard": ["036560"],
    "bad_stage2_block": ["002990"],
    "valid_stage2_but_4b_needed": ["010690"],
    "escape_hatch_low_mae_repair_bridge": ["014790"]
  }
}
```

---

## 11. Validation scope

```yaml
validation_scope:
  price_source: Songdaiki/stock-web
  price_basis: tradable_raw
  price_adjustment_status: raw_unadjusted_marcap
  manifest_max_date: 2026-02-20
  forward_window_available: true
  raw_shard_used_for_weight_calibration: false
  corporate_action_contaminated_review_window:
    002990: false
    008970: false
    036560: false
    000670: false
    010690: false
    014790: false
  r13_reuse_policy:
    do_not_count_as_new_sector_case: true
    new_contribution_is_cross_archetype_synthesis: true
  production_scoring_changed: false
```

Caveats:

```text
- This R13 run reuses R9~R12 source cases as cross-case review material.
- Some source cases, especially C30 and C29, still need evidence URL repair before any production promotion.
- The R13 rule is a shadow guardrail candidate only.
- It should not loosen Stage3-Green.
```

---

## 12. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research run.

```text
You are the later batch implementation agent for Songdaiki/stock_agent.

Read this MD as one v12 R13 cross-archetype residual research artifact.

Task:
1. Ingest the R13 review rows under canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL.
2. Preserve R13 / loop 71 metadata.
3. Do not treat the reused C29/C30/C31/C32 source cases as new sector-specific cases.
4. Treat this artifact's new contribution as the cross-archetype high-MFE/high-MAE bridge governor.
5. Do not loosen Stage3-Green.
6. Do not add a production score change from this artifact alone.
7. If later batch promotion logic marks the pattern safe, implement a shadow governor:
   - MFE_30D_or_90D >= +20% and MAE_90D_or_180D <= -25% triggers bridge-strength review.
   - weak/proxy/indirect bridge blocks Green and positive delta.
   - verified bridge with contained MAE can allow Stage2.
   - valid Stage2 paths with later large drawdown should route to earlier 4B watch.
8. Respect source_proxy_only/evidence_url_pending flags from source artifacts before promotion.
```

---

## 13. Next round state

```text
completed_round = R13
completed_loop = 71
next_round = R1
next_loop = 72
round_cycle_status = loop_71_completed
```
