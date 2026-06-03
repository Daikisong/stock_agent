# E2R Stock-Web v12 Residual Research — R1 Loop 72

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
completed_round: R1
completed_loop: 72
next_round: R2
next_loop: 72
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_BACKLOG_MARGIN_AND_MRO_CONVERSION
output_file: e2r_stock_web_v12_residual_round_R1_loop_72_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Execution gate

This file follows the v12 historical calibration prompt as the execution procedure.  
`V12_Research_No_Repeat_Index.md` is used only as the duplicate-avoidance ledger.

This is not a live stock-discovery run, not investment advice, not a trading instruction, and not a `stock_agent` code patch.  
The only output is a standalone historical calibration / sector-archetype residual Markdown artifact.

### Round resolution

The previous completed artifact in this automation chain was:

```text
completed_round = R13
completed_loop  = 71
```

Therefore:

```text
scheduled_round = R1
scheduled_loop  = 72
```

R1 must map to:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

This run selects:

```text
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

This is a valid R1/L1 pairing.

---

## 1. Why this R1/C01 run

The no-repeat ledger shows C01 is still thinly covered compared with later archetypes:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE:
  rows: 8
  symbols: 6
  date range: 2023-01-04~2024-07-31
  good/bad S2: 5/1
  4B/4C: 2/0
  URL/proxy: 0/3
```

The run therefore targets a new fine-archetype inside C01:

```text
fine_archetype_id = SHIPBUILDING_BACKLOG_MARGIN_AND_MRO_CONVERSION
```

The research question is not “shipbuilders went up.”  
The residual question is narrower:

```text
When does shipbuilding backlog / contract news deserve Stage2-Actionable credit, and when should it remain a 4B/watch or high-MAE case until margin conversion is visible?
```

---

## 2. Price atlas validation

### Manifest snapshot

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

| symbol | name | profile status | 180D corporate-action contamination | calibration usable |
|---|---|---|---|---|
| `329180` | HD현대중공업 | active_like | none listed | true |
| `010140` | 삼성중공업 | active_like | no 2024 contamination in tested window | true |
| `042660` | 한화오션 | active_like | no 2024/2025 contamination in tested window; 2023 name-change candidates are outside tested window | true |

---

## 3. External evidence summary

Evidence used as event timing anchors:

1. `010140` 삼성중공업: MarketWatch reported on 2024-07-01 that Samsung Heavy Industries secured a KRW 1.438T shipbuilding contract. This is a direct backlog-expansion trigger.

2. `329180` HD현대중공업: public coverage in 2024 described HD Hyundai Heavy Industries as a key U.S.-aligned shipbuilding/MRO capacity partner, and public source summaries also note that HD Hyundai Heavy became the first Korean shipbuilder to sign a master ship repair agreement with NAVSUP on 2024-07-11, qualifying it for U.S. Navy MRO work. This is not a pure order number, but it is a backlog/channel-opening event with defense-infrastructure adjacency.

3. `042660` 한화오션: public source summaries describe Hanwha Ocean becoming the second Korean shipbuilder to sign a NAVSUP MSRA in July 2024 and winning an MRO contract for USNS Wally Schirra on 2024-08-29, with maintenance beginning at Geoje in September 2024. Later public coverage framed this as part of a broader U.S. Navy/South Korean shipyard MRO channel.

Event-quality distinction:

```text
010140 = direct commercial order/backlog trigger
329180 = direct capacity/channel trigger + stronger margin-bridge candidate
042660 = direct MRO contract trigger, but with heavier event/defense-theme optionality and large high-MAE behavior before later rerating
```

---

## 4. No-repeat and novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Targeted repository searches before writing:

```text
329180 + C01_ORDER_BACKLOG_MARGIN_BRIDGE -> no direct match found
010140 + C01_ORDER_BACKLOG_MARGIN_BRIDGE + 2024-07-02 -> no direct match found
042660 + C01_ORDER_BACKLOG_MARGIN_BRIDGE + 2024-08-30 -> no direct match found
```

Novelty accounting:

```json
{
  "new_symbol_count": 3,
  "minimum_new_symbol_count": 2,
  "minimum_positive_case_count": 1,
  "minimum_counterexample_count": 1,
  "new_independent_case_ratio": 1.00,
  "duplicate_status": "pass"
}
```

---

## 5. Case design

| case_id | symbol | trigger family | role |
|---|---|---|---|
| `R1L72_C01_329180_20240712` | `329180` HD현대중공업 | MSRA/channel-opening + backlog/margin bridge | positive Stage2-Actionable / Green-later candidate |
| `R1L72_C01_010140_20240702` | `010140` 삼성중공업 | KRW1.438T shipbuilding contract | positive Stage2-Actionable / margin-bridge proof |
| `R1L72_C01_042660_20240830` | `042660` 한화오션 | U.S. Navy MRO contract | high-MAE delayed rerating / guardrail counterexample |

The intended residual is:

```text
C01 should separate:
1. order/backlog evidence with margin conversion, and
2. MRO/channel-opening evidence that still requires repeat order/margin proof before Green.
```

---

## 6. Stock-Web OHLC and backtest

### 6.1 `329180` HD현대중공업

Trigger:

```text
trigger_date = 2024-07-11
trigger_type = Stage2-Actionable
trigger_family = shipbuilding_MRO_channel_opening_margin_bridge
entry_date = 2024-07-12
entry_price = 158200.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-11,155800.0,160500.0,154200.0,157300.0,231112.0,36344246700.0,13964011146800.0,88773116,KOSPI
2024-07-12,158200.0,159100.0,153200.0,157600.0,154926.0,24244669700.0,13990643081600.0,88773116,KOSPI
2024-07-26,184500.0,210000.0,183500.0,207500.0,1077171.0,214368171500.0,18420421570000.0,88773116,KOSPI
2024-08-09,221000.0,222500.0,208000.0,212000.0,323259.0,68988874000.0,18819900592000.0,88773116,KOSPI
2024-09-09,170600.0,177900.0,169900.0,177900.0,144314.0,25188430400.0,15792737336400.0,88773116,KOSPI
2024-12-26,279500.0,299000.0,275000.0,298000.0,514149.0,149843023500.0,26454388568000.0,88773116,KOSPI
2025-01-03,291500.0,307500.0,282500.0,285500.0,486018.0,142453445500.0,25344724618000.0,88773116,KOSPI
2025-01-08,290000.0,304000.0,287000.0,303500.0,455309.0,135754499000.0,26942640706000.0,88773116,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 222500 | 2024-08-09 | 153200 | 2024-07-12 | +40.64% | -3.16% |
| 90D | 222500 | 2024-08-09 | 153200 | 2024-07-12 | +40.64% | -3.16% |
| 180D | 307500 | 2025-01-03 | 153200 | 2024-07-12 | +94.37% | -3.16% |

Interpretation:

```text
This is a clean C01 positive. The first signal was not just price strength; it sat on top of direct shipbuilding/MRO channel-opening evidence and later price behavior produced high MFE with small MAE.
```

### 6.2 `010140` 삼성중공업

Trigger:

```text
trigger_date = 2024-07-01
trigger_type = Stage2-Actionable
trigger_family = large_shipbuilding_contract_backlog_addition
entry_date = 2024-07-02
entry_price = 9690.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-07-01,9370.0,9870.0,9320.0,9680.0,11996745.0,115583351210.0,8518400000000.0,880000000,KOSPI
2024-07-02,9690.0,9700.0,9450.0,9620.0,5270315.0,50497965560.0,8465600000000.0,880000000,KOSPI
2024-07-17,10350.0,11000.0,10350.0,10930.0,29719406.0,321371834034.0,9618400000000.0,880000000,KOSPI
2024-07-26,11190.0,12280.0,11100.0,11870.0,42712575.0,503757504050.0,10445600000000.0,880000000,KOSPI
2024-09-09,9330.0,9830.0,9330.0,9820.0,3393854.0,32617679580.0,8641600000000.0,880000000,KOSPI
2024-11-25,12100.0,12290.0,11880.0,11910.0,11034315.0,132601325990.0,10480800000000.0,880000000,KOSPI
2024-12-30,11250.0,11450.0,11180.0,11300.0,3362236.0,37969747760.0,9944000000000.0,880000000,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 12280 | 2024-07-26 | 9290 | 2024-07-03 | +26.73% | -4.13% |
| 90D | 12280 | 2024-07-26 | 9290 | 2024-07-03 | +26.73% | -4.13% |
| 180D | 12290 | 2024-11-25 | 9290 | 2024-07-03 | +26.83% | -4.13% |

Interpretation:

```text
This is a moderate C01 positive. The KRW1.438T contract created a real backlog signal, but the MFE was lower than 329180 and subsequent path remained more range-bound. This argues for Stage2-Actionable / Yellow-before-Green rather than immediate Green.
```

### 6.3 `042660` 한화오션

Trigger:

```text
trigger_date = 2024-08-29
trigger_type = Stage2-Actionable-Guarded
trigger_family = US_Navy_MRO_contract_channel_opening
entry_date = 2024-08-30
entry_price = 33500.0
entry_price_type = next_tradable_open
```

Relevant Stock-Web rows:

```csv
d,o,h,l,c,v,a,mc,s,m
2024-08-29,32200.0,33300.0,32000.0,32700.0,1516173.0,49636401000.0,10019717983800.0,306413394,KOSPI
2024-08-30,33500.0,35300.0,33050.0,34550.0,4971118.0,171018358650.0,10586582762700.0,306413394,KOSPI
2024-09-11,29900.0,30450.0,28650.0,29050.0,1298653.0,38130164350.0,8901309095700.0,306413394,KOSPI
2024-10-31,27350.0,27450.0,26350.0,26750.0,1302949.0,34797545400.0,8196558289500.0,306413394,KOSPI
2024-11-15,39600.0,41050.0,37900.0,39100.0,14950198.0,589013546300.0,11980763705400.0,306413394,KOSPI
2025-01-24,51900.0,57100.0,51400.0,56700.0,10396751.0,563178821500.0,17373639439800.0,306413394,KOSPI
2025-02-12,65000.0,74600.0,64100.0,72900.0,18170867.0,1251647435500.0,22337536422600.0,306413394,KOSPI
2025-02-19,77000.0,81000.0,75600.0,78200.0,8074276.0,635711307000.0,23961527410800.0,306413394,KOSPI
```

Backtest:

| window | peak/high | peak date | trough/low | trough date | MFE | MAE |
|---|---:|---|---:|---|---:|---:|
| 30D | 35300 | 2024-08-30 | 28650 | 2024-09-11 | +5.37% | -14.48% |
| 90D | 41050 | 2024-11-15 | 26350 | 2024-10-31 | +22.54% | -21.34% |
| 180D | 81000 | 2025-02-19 | 26350 | 2024-10-31 | +141.79% | -21.34% |

Interpretation:

```text
This is the most important residual case in the file.
The MRO contract / U.S. Navy channel was real, but the initial path had weak 30D MFE and >20% MAE before a much later rerating wave.
The correct label is not immediate Green. It is Stage2-Actionable-Guarded, then re-evaluate only after repeated MRO/defense-order evidence or margin conversion appears.
```

---

## 7. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","research_id":"R1L72_C01_SHIPBUILDING_BACKLOG_MARGIN","round":"R1","loop":72,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_AND_MRO_CONVERSION","symbol":"329180","name":"HD현대중공업","trigger_type":"Stage2-Actionable","trigger_family":"shipbuilding_MRO_channel_opening_margin_bridge","trigger_date":"2024-07-11","entry_date":"2024-07-12","entry_price":158200.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":40.64,"mae_30d_pct":-3.16,"mfe_90d_pct":40.64,"mae_90d_pct":-3.16,"mfe_180d_pct":94.37,"mae_180d_pct":-3.16,"peak_price_180d":307500.0,"peak_date_180d":"2025-01-03","trough_price_180d":153200.0,"trough_date_180d":"2024-07-12","calibration_usable":true,"case_polarity":"positive","evidence_url_pending":false,"source_proxy_only":false,"non_price_evidence_strength":"high","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Stage3-Yellow_Green_after_margin_bridge","residual_error_type":"none_positive_anchor"}
{"row_type":"trigger","research_id":"R1L72_C01_SHIPBUILDING_BACKLOG_MARGIN","round":"R1","loop":72,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_AND_MRO_CONVERSION","symbol":"010140","name":"삼성중공업","trigger_type":"Stage2-Actionable","trigger_family":"large_shipbuilding_contract_backlog_addition","trigger_date":"2024-07-01","entry_date":"2024-07-02","entry_price":9690.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":26.73,"mae_30d_pct":-4.13,"mfe_90d_pct":26.73,"mae_90d_pct":-4.13,"mfe_180d_pct":26.83,"mae_180d_pct":-4.13,"peak_price_180d":12290.0,"peak_date_180d":"2024-11-25","trough_price_180d":9290.0,"trough_date_180d":"2024-07-03","calibration_usable":true,"case_polarity":"positive","evidence_url_pending":false,"source_proxy_only":false,"non_price_evidence_strength":"high","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable_to_Stage3-Yellow_until_margin_conversion","residual_error_type":"green_should_require_margin_conversion_not_contract_size_only"}
{"row_type":"trigger","research_id":"R1L72_C01_SHIPBUILDING_BACKLOG_MARGIN","round":"R1","loop":72,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_MARGIN_AND_MRO_CONVERSION","symbol":"042660","name":"한화오션","trigger_type":"Stage2-Actionable-Guarded","trigger_family":"US_Navy_MRO_contract_channel_opening","trigger_date":"2024-08-29","entry_date":"2024-08-30","entry_price":33500.0,"entry_price_type":"next_tradable_open","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":5.37,"mae_30d_pct":-14.48,"mfe_90d_pct":22.54,"mae_90d_pct":-21.34,"mfe_180d_pct":141.79,"mae_180d_pct":-21.34,"peak_price_180d":81000.0,"peak_date_180d":"2025-02-19","trough_price_180d":26350.0,"trough_date_180d":"2024-10-31","calibration_usable":true,"case_polarity":"counterexample_delayed_positive","evidence_url_pending":false,"source_proxy_only":false,"non_price_evidence_strength":"medium","price_only_blowoff":false,"expected_stage_current_profile":"Stage2-Actionable-Guarded_then_recheck_after_repeat_MRO_or_margin_bridge","residual_error_type":"mro_channel_opening_can_have_high_mae_before_late_rerating"}
```

---

## 8. Score simulation and raw component breakdown

This is shadow-only and does not change production scoring.

| symbol | EPS/FCF | earnings visibility | backlog quality | market mispricing | valuation rerating | capital allocation | information confidence | shadow total | intended route |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `329180` | 13 | 15 | 18 | 11 | 13 | 6 | 15 | 91 | Green allowed only after margin bridge evidence |
| `010140` | 10 | 13 | 16 | 9 | 10 | 5 | 14 | 77 | Stage2/Yellow, not immediate Green on contract size alone |
| `042660` | 7 | 9 | 12 | 13 | 12 | 5 | 11 | 69 | Stage2-Guarded; high-MAE gate before Green |

### Stress-test result

The current calibrated profile already blocks price-only blowoff.  
The remaining C01 residual is not price-only. It is **timing of backlog-to-margin conversion**.

```text
C01 positive path:
  real order/backlog/channel evidence
  + low MAE after trigger
  + repeat contract or margin conversion
  => Stage2-Actionable -> Stage3-Yellow/Green

C01 guarded path:
  real but early MRO/channel evidence
  + no near-term margin proof
  + MAE worse than -15% before MFE expansion
  => Stage2-Guarded / 4B-watch / re-evaluate after repeat evidence
```

---

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate",
  "research_id": "R1L72_C01_SHIPBUILDING_BACKLOG_MARGIN",
  "round": "R1",
  "loop": 72,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "SHIPBUILDING_BACKLOG_MARGIN_AND_MRO_CONVERSION",
  "case_count": 3,
  "calibration_usable_case_count": 3,
  "positive_case_count": 2,
  "counterexample_or_guarded_count": 1,
  "new_symbol_count": 3,
  "avg_mfe_30d_pct": 24.25,
  "avg_mae_30d_pct": -7.26,
  "avg_mfe_90d_pct": 29.97,
  "avg_mae_90d_pct": -9.54,
  "avg_mfe_180d_pct": 87.66,
  "avg_mae_180d_pct": -9.54,
  "worst_mae_180d_pct": -21.34
}
```

---

## 10. Shadow rule candidate

```yaml
row_type: canonical_archetype_rule_candidate
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_BACKLOG_MARGIN_AND_MRO_CONVERSION
rule_name: C01_shipbuilding_backlog_margin_bridge_router
production_scoring_changed: false
shadow_weight_only: true
```

### Proposed routing logic

```text
For C01 shipbuilding / heavy-industrial backlog cases:

Tier A: confirmed commercial order/backlog + margin bridge
  Conditions:
    - named contract/order or high-confidence channel-opening evidence
    - order quality or backlog conversion is visible
    - MAE after trigger is contained
  Routing:
    - allow Stage2-Actionable
    - allow Stage3-Yellow
    - allow Green only after EPS/OP margin conversion or repeated high-quality order flow

Tier B: MRO/channel-opening without margin proof
  Conditions:
    - real MRO/framework/channel event
    - future business potential is clear
    - initial price path has high MAE or weak 30D MFE
  Routing:
    - Stage2-Actionable-Guarded
    - do not give Green until repeat order or margin evidence arrives
    - if MAE worse than -15% before MFE confirmation, apply high-MAE watch
```

### Suggested shadow delta

```json
{
  "row_type": "shadow_weight",
  "axis": "c01_backlog_margin_bridge_router",
  "scope": "canonical_archetype_id:C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "proposal": {
    "commercial_order_backlog_stage2_bonus": 1.0,
    "green_requires_margin_bridge_or_repeat_order": true,
    "mro_channel_opening_stage2_guarded": true,
    "mro_channel_high_mae_watch_threshold_pct": -15.0
  },
  "confidence": "medium",
  "apply_now": false,
  "reason": "Two clean positive C01 order/backlog paths and one high-MAE delayed MRO rerating path support a router that separates commercial backlog margin bridge from early channel-opening optionality."
}
```

---

## 11. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "research_id": "R1L72_C01_SHIPBUILDING_BACKLOG_MARGIN",
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "contribution": "Adds under-covered C01 shipbuilding cases and separates clean commercial order/backlog positives from MRO/channel-opening cases that can suffer high MAE before later rerating.",
  "positive_case_added": 2,
  "counterexample_case_added": 1,
  "new_symbol_count": 3,
  "guardrail_added": "C01 Green should require margin bridge or repeated order evidence; early MRO/channel-opening signals should remain guarded when MAE exceeds -15%.",
  "4b_split": {
    "stage2_positive": ["329180", "010140"],
    "stage2_guarded_high_mae": ["042660"]
  }
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
    329180: false
    010140: false
    042660: false
  evidence_url_pending:
    329180: false
    010140: false
    042660: false
  source_proxy_only:
    329180: false
    010140: false
    042660: false
```

Limitations:

```text
- This run uses public event evidence and Stock-Web price rows.
- It does not verify all later order backlog composition by vessel type.
- It does not change production scoring.
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
2. Preserve R1 / loop 72 metadata.
3. Add the cases to C01_ORDER_BACKLOG_MARGIN_BRIDGE if parser validation passes.
4. Add a shadow-only rule candidate named C01_shipbuilding_backlog_margin_bridge_router.
5. Do not loosen Stage3-Green.
6. Do not give Green from one contract headline alone.
7. Require either margin conversion, repeated high-quality order flow, or low-MAE confirmation before C01 Green.
8. Route MRO/channel-opening signals with high MAE into Stage2-Actionable-Guarded or 4B-watch until repeat non-price evidence arrives.
9. Keep production scoring unchanged unless later batch promotion logic independently marks this axis safe.
```

---

## 14. Next round state

```text
completed_round = R1
completed_loop = 72
next_round = R2
next_loop = 72
next_large_sector_hint = L2_AI_SEMICONDUCTOR_ELECTRONICS
```
