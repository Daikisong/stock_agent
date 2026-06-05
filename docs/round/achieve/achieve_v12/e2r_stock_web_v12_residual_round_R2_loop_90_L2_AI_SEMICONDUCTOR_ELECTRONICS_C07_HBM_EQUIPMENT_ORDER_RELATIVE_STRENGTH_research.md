# E2R Stock-Web v12 Residual Research — R2 Loop 90

```yaml
schema_version: e2r_stock_web_v12_residual_research_md
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research

scheduled_round: R2
scheduled_loop: 90
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM3E_ADVANCED_PACKAGING_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_CONVERSION_BRIDGE

previous_completed_round: R1
previous_completed_loop: 90
completed_round: R2
completed_loop: 90
next_round: R3
next_loop: 90

round_schedule_status: valid
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
do_not_propose_new_weight_delta: true
```

---

## 1. Execution boundary

This file is a standalone historical calibration / residual-research artifact. It does **not** patch `stock_agent`, does **not** inspect `src/e2r`, does **not** create a live watchlist, and does **not** change production scoring.

Allowed actions used here:

```text
- Use Songdaiki/stock-web 1D OHLCV shards.
- Use stock_agent V12_Research_No_Repeat_Index only as duplicate / coverage ledger.
- Confirm historical trigger dates and entry prices.
- Compare current calibrated profile behaviour against realized return path.
- Produce shadow, deferred, coding-agent handoff only.
```

---

## 2. Schedule resolution

The latest completed generated artifact before this run was:

```text
completed_round = R1
completed_loop  = 90
next_round      = R2
next_loop       = 90
```

Therefore this run is:

```text
scheduled_round = R2
scheduled_loop  = 90
```

R2 hard gate:

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
```

Selected archetype:

```text
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

Why C07 now:

```text
- R2 loop89 already used C06_HBM_MEMORY_CUSTOMER_CAPACITY.
- C07 coverage is still shallow: 11 rows / 9 symbols.
- Top-covered C07 symbols are avoided: 042700, 064760, 003160, 036200, 036540, 039440.
- This run focuses on the residual gap: HBM/AI equipment relative-strength can look correct locally, but without named order / capacity / revenue conversion it can be a 4B or 4C trap.
```

---

## 3. Price atlas validation

Primary price source:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Manifest checkpoint:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14,354,401
raw_row_count = 15,214,118
symbol_count = 5,414
active_like_symbol_count = 2,868
inactive_or_delisted_like_symbol_count = 2,546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Important caveat:

```text
raw/unadjusted OHLC is used. Corporate-action-contaminated windows are blocked by default.
All three selected 2024 trigger windows are outside the listed corporate-action candidate dates for their profiles.
```

---

## 4. No-repeat / novelty check

No-Repeat Index C07 snapshot:

```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
rows = 11
symbols = 9
date_range = 2024-02-13~2024-06-14
good/bad S2 = 7/0
4B/4C = 1/0
top covered symbols = 042700(2), 064760(2), 003160(1), 036200(1), 036540(1), 039440(1)
```

Duplicate gate:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols:

| ticker | name | C07 top-covered? | duplicate status | use |
|---:|---|---:|---|---|
| 039030 | 이오테크닉스 | no | useful expansion | HBM/laser-equipment relative-strength, but weak conversion bridge |
| 031980 | 피에스케이홀딩스 | no | useful expansion | packaging/post-process equipment price-positive, local 4B |
| 403870 | HPSP | no | useful expansion | advanced-equipment beta without order bridge, hard 4C candidate |

---

## 5. Historical evidence frame

The shared historical macro/sector trigger is:

```text
trigger_family = HBM3E_AI_ACCELERATOR_EQUIPMENT_DEMAND
trigger_date = 2024-03-19
entry_rule = next_trading_day close
entry_date = 2024-03-20
```

Non-price evidence basis:

```text
- SK Hynix began mass production of HBM3E in March 2024.
- Initial shipments were directed to Nvidia.
- SK Hynix HBM capacity was reported as fully booked for 2024.
- Nvidia's Blackwell cycle used HBM3E and intensified market focus on HBM supply-chain bottlenecks.
```

Interpretation rule:

```text
The sector trigger is real. The calibration error is not "HBM is fake."
The residual error is that the model may over-upgrade secondary equipment names if it sees only:
  AI/HBM label + relative strength + liquidity burst
without:
  named customer
  equipment qualification
  purchase order / backlog
  capacity allocation
  delivery timing
  revenue / margin conversion
```

---

## 6. Case-level backtest summary

### 6.1 Aggregate table

Entry uses the 2024-03-20 tradable close. MFE/MAE are calculated on observed high/low rows after entry inside the available 2024 forward path.

| case_id | ticker | name | entry_date | entry_close | observed_peak | peak_date | MFE | observed_trough | trough_date | MAE | classification |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C07-R2L90-001 | 031980 | 피에스케이홀딩스 | 2024-03-20 | 45,500 | 85,300 | 2024-06-19 | +87.5% | 29,650 | 2024-12-02 | -34.8% | positive_with_local_4B |
| C07-R2L90-002 | 039030 | 이오테크닉스 | 2024-03-20 | 192,100 | 266,000 | 2024-04-04 | +38.5% | 113,500 | 2024-11-29 | -40.9% | local_4B_then_high_MAE_counterexample |
| C07-R2L90-003 | 403870 | HPSP | 2024-03-20 | 51,400 | 55,300 | 2024-03-28 | +7.6% | 22,650 | 2024-08-05 | -55.9% | hard_4C_candidate |

### 6.2 Case 1 — 031980 피에스케이홀딩스

```yaml
case_id: C07-R2L90-001
ticker: "031980"
name: 피에스케이홀딩스
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
trigger_type: HBM3E_ADVANCED_PACKAGING_EQUIPMENT_RELATIVE_STRENGTH
trigger_date: 2024-03-19
entry_date: 2024-03-20
entry_price: 45500
peak_price: 85300
peak_date: 2024-06-19
trough_price: 29650
trough_date: 2024-12-02
mfe_pct: 87.5
mae_pct: -34.8
case_label: positive_with_local_4B
calibration_usable: true
```

Path reading:

```text
This is the cleanest price-positive in this run. The stock was not only a one-day response: it continued from 45,500 on 2024-03-20 to an 85,300 high on 2024-06-19.
However, the same path later fell toward 29,650 by 2024-12-02. The trigger was therefore strong enough for C07 positive evidence but too volatile for unconditional Green if the model cannot show order / revenue conversion.
```

Calibration implication:

```text
C07 can reward relative strength after confirmed HBM3E production only when the stock has additional conversion evidence.
Without that bridge, positive classification should carry a local 4B overlay after +60~80% MFE.
```

### 6.3 Case 2 — 039030 이오테크닉스

```yaml
case_id: C07-R2L90-002
ticker: "039030"
name: 이오테크닉스
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
trigger_type: HBM3E_LASER_EQUIPMENT_RELATIVE_STRENGTH
trigger_date: 2024-03-19
entry_date: 2024-03-20
entry_price: 192100
peak_price: 266000
peak_date: 2024-04-04
trough_price: 113500
trough_date: 2024-11-29
mfe_pct: 38.5
mae_pct: -40.9
case_label: local_4B_then_high_MAE_counterexample
calibration_usable: true
```

Path reading:

```text
The price path validates a local HBM-equipment burst: 192,100 entry to 266,000 high in about two weeks.
But the forward path then breaks the thesis if the model had treated the move as sustained Green. By late 2024 the stock reached a 113,500 low.
```

Calibration implication:

```text
This is the classic C07 residual error:
  correct sector call
  wrong stage persistence
If the model cannot attach a named customer/order/revenue conversion bridge, the right status is not Stage3-Green. It should be Stage2-Actionable / Yellow cap with a local 4B overlay.
```

### 6.4 Case 3 — 403870 HPSP

```yaml
case_id: C07-R2L90-003
ticker: "403870"
name: HPSP
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
trigger_type: HBM_ADVANCED_EQUIPMENT_PRICE_BETA_WITHOUT_ORDER_BRIDGE
trigger_date: 2024-03-19
entry_date: 2024-03-20
entry_price: 51400
peak_price: 55300
peak_date: 2024-03-28
trough_price: 22650
trough_date: 2024-08-05
mfe_pct: 7.6
mae_pct: -55.9
case_label: hard_4C_candidate
calibration_usable: true
```

Path reading:

```text
HPSP had the right broad label — advanced semiconductor equipment — but the post-trigger price path did not validate a sustained C07 rerating. MFE was shallow, and the later drawdown was severe.
```

Calibration implication:

```text
HPSP should be a hard negative control for C07:
  do not let "advanced equipment + HBM market heat + relative liquidity" substitute for named order / delivery / revenue bridge.
```

---

## 7. Current calibrated profile stress test

Profile premise:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Stress-test result:

| ticker | likely old failure mode | current profile improvement | remaining residual |
|---:|---|---|---|
| 031980 | under-rewarding strong HBM equipment relative strength | allows Stage2/Y if cross-evidence exists | must apply 4B after parabolic MFE without confirmed order/revenue bridge |
| 039030 | over-holding local HBM burst as persistent Green | price-only block helps | needs C07-specific “order conversion required for Green persistence” |
| 403870 | treating advanced-equipment label as HBM order proxy | 4C routing helps if thesis breaks | needs C07-specific hard cap when MFE is shallow and MAE exceeds -35% |

---

## 8. Shadow rule candidate

```yaml
shadow_rule_id: C07_HBM_EQUIPMENT_ORDER_CONVERSION_REQUIRED_FOR_GREEN
scope:
  large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
  canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
condition:
  all:
    - HBM/AI equipment theme or relative-strength trigger is present
    - no named customer/order/qualification/backlog/revenue conversion evidence
    - price path already shows +25% or more local MFE OR liquidity burst
action:
  - cap_stage: Stage2-Actionable or Stage3-Yellow
  - block_stage3_green: true
  - attach_local_4B_overlay: true
  - require_non_price_bridge_for_green:
      - named customer
      - purchase order / backlog / capacity allocation
      - delivery timing
      - revenue / margin conversion
      - explicit management guidance or filed order disclosure
negative_control:
  if MFE_30D < 10% and MAE_90D <= -30%:
    route_to: hard_4C_candidate
```

Plain-language rule:

```text
C07 is allowed to be fast, but it is not allowed to be hollow.
HBM-equipment relative strength can open the door; named order/revenue conversion must keep the door open.
```

---

## 9. Machine-readable rows

### 9.1 case rows

```jsonl
{"row_type":"case","case_id":"C07-R2L90-001","round":"R2","loop":90,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM3E_ADVANCED_PACKAGING_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_CONVERSION_BRIDGE","symbol":"031980","name":"피에스케이홀딩스","case_label":"positive_with_local_4B","calibration_usable":true}
{"row_type":"case","case_id":"C07-R2L90-002","round":"R2","loop":90,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM3E_ADVANCED_PACKAGING_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_CONVERSION_BRIDGE","symbol":"039030","name":"이오테크닉스","case_label":"local_4B_then_high_MAE_counterexample","calibration_usable":true}
{"row_type":"case","case_id":"C07-R2L90-003","round":"R2","loop":90,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM3E_ADVANCED_PACKAGING_EQUIPMENT_RELATIVE_STRENGTH_VS_ORDER_REVENUE_CONVERSION_BRIDGE","symbol":"403870","name":"HPSP","case_label":"hard_4C_candidate","calibration_usable":true}
```

### 9.2 trigger rows

```jsonl
{"row_type":"trigger","case_id":"C07-R2L90-001","symbol":"031980","trigger_type":"HBM3E_ADVANCED_PACKAGING_EQUIPMENT_RELATIVE_STRENGTH","trigger_date":"2024-03-19","entry_date":"2024-03-20","entry_price":45500,"peak_price":85300,"peak_date":"2024-06-19","trough_price":29650,"trough_date":"2024-12-02","mfe_pct":87.47,"mae_pct":-34.84,"local_4b_overlay":true,"hard_4c_candidate":false}
{"row_type":"trigger","case_id":"C07-R2L90-002","symbol":"039030","trigger_type":"HBM3E_LASER_EQUIPMENT_RELATIVE_STRENGTH","trigger_date":"2024-03-19","entry_date":"2024-03-20","entry_price":192100,"peak_price":266000,"peak_date":"2024-04-04","trough_price":113500,"trough_date":"2024-11-29","mfe_pct":38.47,"mae_pct":-40.92,"local_4b_overlay":true,"hard_4c_candidate":false}
{"row_type":"trigger","case_id":"C07-R2L90-003","symbol":"403870","trigger_type":"HBM_ADVANCED_EQUIPMENT_PRICE_BETA_WITHOUT_ORDER_BRIDGE","trigger_date":"2024-03-19","entry_date":"2024-03-20","entry_price":51400,"peak_price":55300,"peak_date":"2024-03-28","trough_price":22650,"trough_date":"2024-08-05","mfe_pct":7.59,"mae_pct":-55.93,"local_4b_overlay":false,"hard_4c_candidate":true}
```

### 9.3 score simulation rows

```jsonl
{"row_type":"score_simulation","case_id":"C07-R2L90-001","symbol":"031980","baseline_stage_estimate":"Stage2-Actionable_to_Stage3-Yellow","current_profile_expected_stage":"Stage3-Yellow_with_4B_watch","residual_error":"Green should require order/revenue conversion; price-positive alone is insufficient","suggested_shadow_action":"cap Green unless order/revenue bridge exists"}
{"row_type":"score_simulation","case_id":"C07-R2L90-002","symbol":"039030","baseline_stage_estimate":"Stage3-Yellow_or_Green_possible","current_profile_expected_stage":"Stage2-Actionable_or_Yellow_with_local_4B","residual_error":"local MFE is real but forward drawdown invalidates persistent Green","suggested_shadow_action":"time-decay local 4B after +25% MFE if no order conversion"}
{"row_type":"score_simulation","case_id":"C07-R2L90-003","symbol":"403870","baseline_stage_estimate":"Stage2_false_positive_possible","current_profile_expected_stage":"Watch_or_4C_candidate","residual_error":"advanced-equipment label cannot substitute for C07 order bridge","suggested_shadow_action":"route to 4C if shallow MFE and high MAE"}
```

### 9.4 aggregate rows

```jsonl
{"row_type":"aggregate","round":"R2","loop":90,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":3,"same_archetype_new_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_weight","round":"R2","loop":90,"shadow_rule_id":"C07_HBM_EQUIPMENT_ORDER_CONVERSION_REQUIRED_FOR_GREEN","target":"canonical_archetype_specific_stage_cap","proposed_change_type":"shadow_rule_only","production_scoring_changed":false,"implementation_now":false}
{"row_type":"residual_contribution","round":"R2","loop":90,"contribution":"C07 residual: HBM equipment relative strength should open Stage2/Yellow, but Stage3-Green requires named order/customer/qualification/revenue conversion. Price-only or label-only advanced-equipment beta should be capped or routed to 4C after shallow MFE/high MAE."}
```

---

## 10. Residual contribution summary

```text
new_independent_case_count = 3
same_archetype_new_symbol_count = 3

positive_case_count = 1
counterexample_count = 2
local_4b_overlay_case_count = 2
hard_4c_candidate_count = 1
calibration_usable_trigger_count = 3

loop_contribution_label = residual_error_found
do_not_propose_new_weight_delta = true
```

Key finding:

```text
C07 needs a conversion bridge, not just an HBM label.
The 2024 HBM3E trigger was real, but stock-level outcomes split sharply:
  - PSK Holdings: strong MFE, but local 4B needed.
  - EO Technics: local burst, then high-MAE path.
  - HPSP: shallow MFE and large drawdown, hard 4C candidate.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent for stock_agent. Do not run this handoff unless explicitly instructed in a separate coding session.

Input research artifact:
e2r_stock_web_v12_residual_round_R2_loop_90_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md

Task:
Review the C07 shadow rule candidate only. Do not infer production code structure from this Markdown alone. Locate the actual scoring implementation and tests in the repository before patching.

Research conclusion to evaluate:
For C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, Stage3-Green should require named order/customer/qualification/backlog/revenue conversion. HBM/AI equipment relative strength alone should cap at Stage2-Actionable or Stage3-Yellow and attach a local 4B overlay after large MFE without conversion evidence. If MFE is shallow and MAE is severe, route to hard 4C candidate.

Required safety:
- Preserve existing global calibrated profile.
- Do not change stage2_actionable_evidence_bonus.
- Do not change stage3_yellow_total_min or stage3_green_total_min globally.
- Implement only a sector/archetype-specific rule if tests confirm the rule is needed.
- Add tests for:
  1. PSK Holdings-like positive_with_local_4B.
  2. EO Technics-like local_4B_then_high_MAE.
  3. HPSP-like shallow-MFE/high-MAE hard 4C candidate.
```
