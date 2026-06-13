# E2R Stock-Web V12 Residual Research — R2 / loop 218 / C06_HBM_MEMORY_CUSTOMER_CAPACITY

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 218
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id = C06_2025_HBM_BOOKED_CAPACITY_VS_QUALIFICATION_GAP_GATE_V4
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing; original Index Priority 0
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection / novelty check

The original no-repeat ledger still marks `C06_HBM_MEMORY_CUSTOMER_CAPACITY` as an under-covered Priority 0 area:

```text
index_baseline_coverage_before = C06 rows 17
index_baseline_need_to_30 = 13
index_baseline_need_to_50 = 33
```

This session has already covered C06 through loops 129, 139, and 147. Therefore this loop is not a simple row-count exercise. It is a second-order quality pass focused on 2025 cycle-phase triggers:

```text
avoid_previous_c06_trigger_families = [
  "2024 Q1/Q2 SK hynix HBM profit recovery",
  "2024 Samsung HBM qualification gap",
  "2024 late SK hynix record-profit headline",
  "2025 January broad SK/Samsung record-profit vs HBM delay split",
  "AI substrate boundary false-positive leaf"
]

new_leaf = C06_2025_HBM_BOOKED_CAPACITY_VS_QUALIFICATION_GAP_GATE_V4
new_independent_case_count = 7
same_archetype_new_symbol_count = 2
same_archetype_new_trigger_family_count = 7
reused_case_count = 0
hard_duplicate_key_reused = false
```

### Why C06 again?

C06 is the hinge where “HBM / AI memory” vocabulary can mean two very different things:

1. **Booked capacity / named customer / sold-out supply** — the evidence is already a money road.
2. **Qualification target / redesigned product / future launch** — the evidence is still a bridge under construction.

The difference is not cosmetic. In 2025 SK hynix and Samsung both had HBM headlines, but the price path separates a booked-capacity winner from a qualification-gap recovery candidate.

## 2. Price source / validation scope

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
manifest_min_date = 1995-05-02
```

Corporate-action screen:

```text
000660 / SK하이닉스:
  corporate_action_candidate_dates = [1998-07-03, 1999-01-07, 1999-07-06, 1999-10-27, 2000-01-07, 2001-06-27, 2002-06-07, 2003-04-14, 2003-04-21]
  2025 trigger windows contaminated? false

005930 / 삼성전자:
  corporate_action_candidate_dates = [1996-01-03, 1997-01-03, 2018-05-04]
  2025 trigger windows contaminated? false
```

MFE/MAE calculation rule:

```text
entry_price = close price on entry_date
MFE_ND_pct = (max high over next N tradable rows including entry row - entry_price) / entry_price * 100
MAE_ND_pct = (min low over next N tradable rows including entry row - entry_price) / entry_price * 100
rounding = 0.1 percentage point
```

All trigger rows below have complete 30D/90D/180D MFE and MAE fields. No row uses manifest-after-date prices.

## 3. Evidence ledger

| evidence_id | date | issuer | evidence family | source URL | C06 interpretation |
|---|---:|---|---|---|---|
| EV-C06-218-01 | 2025-03 | SK hynix | HBM4 samples to Nvidia / HBM3E 12-layer ramp expectation | https://pulse.mk.co.kr/news/english/11301329 | early structural positive but entry geometry still volatile |
| EV-C06-218-02 | 2025-04-24 | SK hynix | 2025 HBM sales orders secured; 2025 HBM production sold out; 12-layer HBM3E to major customers including Nvidia | https://en.yna.co.kr/view/AEN20250424001454320 | booked-capacity money road |
| EV-C06-218-03 | 2025-04-30 | Samsung Electronics | Q1 2025: lower HBM sales from export controls/deferred demand; enhanced 12H HBM3E ramp | https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2025-results | qualification / ramp gap, not yet booked-capacity proof |
| EV-C06-218-04 | 2025-01-31 | Samsung Electronics | improved HBM3E launch planned; Nvidia design requirement / slow AI-chip sales | https://www.reuters.com/technology/samsung-q4-profit-growth-slows-chip-issues-weigh-2025-01-31/ | watch, not hard positive yet |
| EV-C06-218-05 | 2025-04-01 | Samsung Electronics | 12-layer HBM3E Nvidia qualification target by May | https://www.trendforce.com/news/2025/04/01/news-samsung-accelerates-hbm3e-redesign-reportedly-targets-nvidia-approval-by-may/ | qualification-only bridge |
| EV-C06-218-06 | 2025-05-23 | Samsung Electronics | 12-layer HBM3E reportedly usable at bare-die stage; full package verification remains | https://www.trendforce.com/news/2025/05/23/news-samsung-reportedly-nears-nvidia-hbm3e-approval-but-order-outlook-remains-in-doubt/ | reset/staged positive, not Green |

## 4. Case table

| case_id | ticker | name | trigger_date | entry_date | trigger_type | result label | why it matters |
|---|---:|---|---:|---:|---|---|---|
| C06-L218-01 | 000660 | SK하이닉스 | 2025-03-21 | 2025-03-21 | Stage2-Actionable | positive + staged-entry guard | HBM4/Nvidia sample route worked, but April drawdown proves entry geometry still matters. |
| C06-L218-02 | 000660 | SK하이닉스 | 2025-04-25 | 2025-04-25 | Stage2-Actionable | clean positive | Q1 result plus sold-out HBM capacity/order visibility created a hard C06 bridge. |
| C06-L218-03 | 000660 | SK하이닉스 | 2025-05-15 | 2025-05-15 | Stage3-Yellow | positive | Follow-through after booked-capacity evidence; low forward MAE and huge MFE. |
| C06-L218-04 | 005930 | 삼성전자 | 2025-01-31 | 2025-01-31 | Stage2-Watch | counterexample to premature positive | Slow AI-chip/HBM sales warning plus redesigned product timing kept this below Actionable. |
| C06-L218-05 | 005930 | 삼성전자 | 2025-04-01 | 2025-04-01 | Stage2-Watch | counterexample / qualification-only | “Targeting Nvidia qualification” was a bridge under construction, not capacity sold out. |
| C06-L218-06 | 005930 | 삼성전자 | 2025-04-30 | 2025-04-30 | Stage4B-Watch | false-hard-4C audit | Q1 HBM sales decline was real, but later forward MFE shows it was not irreversible 4C. |
| C06-L218-07 | 005930 | 삼성전자 | 2025-05-30 | 2025-05-30 | Stage2-Actionable | staged positive | After reset, bare-die usability / verification progress allowed a staged C06 recovery read. |

## 5. Trigger rows — JSONL

```jsonl
{"case_id":"C06-L218-01","ticker":"000660","company_name":"SK하이닉스","market":"KOSPI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_2025_HBM_BOOKED_CAPACITY_VS_QUALIFICATION_GAP_GATE_V4","trigger_date":"2025-03-21","entry_date":"2025-03-21","entry_price":215500.0,"trigger_type":"Stage2-Actionable","evidence_family":"HBM4_sample_to_Nvidia_and_12H_HBM3E_ramp","evidence_url":"https://pulse.mk.co.kr/news/english/11301329","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.9,"MAE_30D_pct":-24.5,"MFE_90D_pct":42.2,"MAE_90D_pct":-24.5,"MFE_180D_pct":199.8,"MAE_180D_pct":-24.5,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"classification":"positive_with_high_mae_staged_entry_guard","current_profile_error":true,"residual_note":"C06 should not overblock SK Hynix after HBM4/HBM3E customer bridge, but entry must receive staged/high-MAE guard."}
{"case_id":"C06-L218-02","ticker":"000660","company_name":"SK하이닉스","market":"KOSPI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_2025_HBM_BOOKED_CAPACITY_VS_QUALIFICATION_GAP_GATE_V4","trigger_date":"2025-04-25","entry_date":"2025-04-25","entry_price":184400.0,"trigger_type":"Stage2-Actionable","evidence_family":"2025_HBM_orders_secured_and_capacity_sold_out","evidence_url":"https://en.yna.co.kr/view/AEN20250424001454320","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":33.7,"MAE_30D_pct":-4.2,"MFE_90D_pct":78.7,"MAE_90D_pct":-4.2,"MFE_180D_pct":327.3,"MAE_180D_pct":-4.2,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"classification":"clean_positive","current_profile_error":false,"residual_note":"Booked 2025 HBM supply, named major customers, and 12H HBM3E mix created a hard money-road bridge."}
{"case_id":"C06-L218-03","ticker":"000660","company_name":"SK하이닉스","market":"KOSPI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_2025_HBM_BOOKED_CAPACITY_VS_QUALIFICATION_GAP_GATE_V4","trigger_date":"2025-05-15","entry_date":"2025-05-15","entry_price":200500.0,"trigger_type":"Stage3-Yellow","evidence_family":"booked_capacity_follow_through_and_HBM_mix_visibility","evidence_url":"https://en.yna.co.kr/view/AEN20250424001454320","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":45.4,"MAE_30D_pct":-2.0,"MFE_90D_pct":81.5,"MAE_90D_pct":-2.0,"MFE_180D_pct":364.3,"MAE_180D_pct":-2.0,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"classification":"positive","current_profile_error":false,"residual_note":"Once booked capacity and HBM sales visibility were established, price path produced high MFE with shallow MAE."}
{"case_id":"C06-L218-04","ticker":"005930","company_name":"삼성전자","market":"KOSPI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_2025_HBM_BOOKED_CAPACITY_VS_QUALIFICATION_GAP_GATE_V4","trigger_date":"2025-01-31","entry_date":"2025-01-31","entry_price":52400.0,"trigger_type":"Stage2-Watch","evidence_family":"slow_AI_chip_sales_and_redesigned_HBM3E_timing","evidence_url":"https://www.reuters.com/technology/samsung-q4-profit-growth-slows-chip-issues-weigh-2025-01-31/","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":12.6,"MAE_30D_pct":-3.1,"MFE_90D_pct":18.3,"MAE_90D_pct":-3.1,"MFE_180D_pct":107.3,"MAE_180D_pct":-3.1,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"classification":"counterexample_to_premature_stage2_actionable","current_profile_error":true,"residual_note":"HBM recovery vocabulary existed, but Nvidia/12H volume proof was absent. Stage2-Watch was safer than Actionable."}
{"case_id":"C06-L218-05","ticker":"005930","company_name":"삼성전자","market":"KOSPI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_2025_HBM_BOOKED_CAPACITY_VS_QUALIFICATION_GAP_GATE_V4","trigger_date":"2025-04-01","entry_date":"2025-04-01","entry_price":58800.0,"trigger_type":"Stage2-Watch","evidence_family":"Nvidia_qualification_target_without_booked_volume","evidence_url":"https://www.trendforce.com/news/2025/04/01/news-samsung-accelerates-hbm3e-redesign-reportedly-targets-nvidia-approval-by-may/","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.0,"MAE_30D_pct":-10.0,"MFE_90D_pct":25.9,"MAE_90D_pct":-10.0,"MFE_180D_pct":91.2,"MAE_180D_pct":-10.0,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"classification":"counterexample_qualification_only","current_profile_error":true,"residual_note":"Qualification target alone should remain Watch until full package / commercial allocation proof appears."}
{"case_id":"C06-L218-06","ticker":"005930","company_name":"삼성전자","market":"KOSPI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_2025_HBM_BOOKED_CAPACITY_VS_QUALIFICATION_GAP_GATE_V4","trigger_date":"2025-04-30","entry_date":"2025-04-30","entry_price":55500.0,"trigger_type":"Stage4B-Watch","evidence_family":"Q1_HBM_sales_decline_export_controls_deferred_demand","evidence_url":"https://news.samsung.com/global/samsung-electronics-announces-first-quarter-2025-results","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":9.2,"MAE_30D_pct":-3.2,"MFE_90D_pct":33.3,"MAE_90D_pct":-3.2,"MFE_180D_pct":160.4,"MAE_180D_pct":-3.2,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"classification":"false_hard4c_audit","current_profile_error":true,"residual_note":"HBM sales decline was a real negative confirmation, but forward MFE shows it was a 4B/Watch reset rather than irreversible 4C."}
{"case_id":"C06-L218-07","ticker":"005930","company_name":"삼성전자","market":"KOSPI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_2025_HBM_BOOKED_CAPACITY_VS_QUALIFICATION_GAP_GATE_V4","trigger_date":"2025-05-30","entry_date":"2025-05-30","entry_price":56200.0,"trigger_type":"Stage2-Actionable","evidence_family":"bare_die_usability_and_full_package_verification_progress","evidence_url":"https://www.trendforce.com/news/2025/05/23/news-samsung-reportedly-nears-nvidia-hbm3e-approval-but-order-outlook-remains-in-doubt/","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":13.5,"MAE_30D_pct":-0.7,"MFE_90D_pct":68.2,"MAE_90D_pct":-0.7,"MFE_180D_pct":157.1,"MAE_180D_pct":-0.7,"calibration_usable":true,"corporate_action_contaminated_180D_window":false,"classification":"staged_positive","current_profile_error":true,"residual_note":"After reset, qualification progress plus shallow MAE allowed staged positive treatment, but still below booked-capacity Green."}
```

## 6. Score / return alignment

| group | rows | avg MFE90 | avg MAE90 | read-through |
|---|---:|---:|---:|---|
| SK hynix booked-capacity rows | 3 | 67.5% | -10.2% | C06 should reward booked/sold-out customer capacity; only the earliest row needs staged-entry guard. |
| Samsung qualification-gap rows | 4 | 36.4% | -4.3% | Qualification gap is not a short signal by itself; it is Watch/4B until product acceptance and allocation improve. |
| all rows | 7 | 49.8% | -6.8% | C06 should separate `booked capacity` from `qualification target`, not treat all HBM vocabulary equally. |

## 7. Current calibrated profile stress test

```text
current_profile_proxy = e2r_2_2_rolling_calibrated / e2r_2_1_stock_web_calibrated family
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual behavior observed:

1. **Good behavior to preserve**
   - SK hynix after explicit HBM sold-out / order visibility should pass Stage2-Actionable and often Yellow.
   - Pure price-only extension should still be blocked from Green.

2. **Residual error to patch**
   - Samsung 2025 HBM headlines need a qualification-gap state between Watch and Actionable.
   - A negative Samsung HBM-sales quarter should not immediately become hard 4C if redesigned/enhanced product acceptance is still live and price reset has already happened.
   - SK hynix early HBM4/sample row should not be hard-blocked, but must receive staged-entry / high-MAE guard.

```text
current_profile_error_count = 5
false_positive_like_count = 2
false_hard4c_or_overblock_count = 1
too_late_or_underpromotion_count = 2
```

## 8. Raw component score simulation

| case_id | evidence confidence | customer/capacity bridge | revision/mix bridge | valuation/entry geometry | risk guard | simulated stage |
|---|---:|---:|---:|---:|---:|---|
| C06-L218-01 | 72 | 68 | 60 | 42 | -8 | Stage2-Actionable + staged-entry |
| C06-L218-02 | 88 | 92 | 82 | 78 | 0 | Stage3-Yellow |
| C06-L218-03 | 86 | 90 | 84 | 83 | 0 | Stage3-Yellow |
| C06-L218-04 | 70 | 42 | 38 | 68 | -3 | Stage2-Watch |
| C06-L218-05 | 68 | 48 | 44 | 60 | -4 | Stage2-Watch |
| C06-L218-06 | 76 | 36 | 32 | 71 | -2 | Stage4B-Watch / false-hard4C audit |
| C06-L218-07 | 74 | 58 | 54 | 80 | 0 | Stage2-Actionable, not Green |

## 9. Shadow rule candidate

```yaml
shadow_rule_id: C06_BOOKED_CAPACITY_QUALIFICATION_GAP_AND_RESET_ENTRY_GATE_V4
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
production_scoring_changed: false
shadow_weight_only: true
rule_candidate:
  positive_unlock:
    require_any:
      - named_customer_or_major_customer_supply_confirmed
      - HBM_capacity_sold_out_or_order_secured_for_forward_year
      - reported_HBM_mix_ASP_profit_bridge
      - 12H_HBM3E_or_HBM4_volume_ramp_with_customer_allocation
    preferred_stage: Stage2-Actionable_to_Stage3-Yellow
    green_gate_note: "Green still requires reported mix/revision and not merely price heat."
  qualification_gap_watch:
    if_any:
      - qualification_target_only
      - redesigned_or_enhanced_HBM_product_pending
      - sample_or_bare_die_progress_without_package_volume
      - HBM_sales_decline_due_export_controls_or_deferred_demand
    preferred_stage: Stage2-Watch_or_Stage4B-Watch
    action: block_Green_and_block_clean_Stage2_Actionable_until_second_confirmation
  false_hard4c_audit:
    if_negative_hbm_sales_decline_but_forward_product_acceptance_live: Stage4B_Watch_not_hard_4C
    if_reset_entry_has_shallow_MAE_and_followthrough_MFE: staged_positive_allowed
  high_mae_guard:
    if MFE180 >= 100 and MAE30 <= -20:
      action: keep_thesis_positive_but_apply_staged_entry_or_position_size_guard
```

## 10. Residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c06_booked_capacity_vs_qualification_gap_reset_entry_gate_v4
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c_should_not_fire_on_quarterly_hbm_decline_alone
existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

Contribution:

- C06 should not be a generic “HBM good / HBM bad” bucket.
- SK hynix 2025 shows the clean version: booked capacity, secured sales orders, named customer route, reported HBM mix.
- Samsung 2025 shows the watch/recovery version: qualification target, HBM sales decline, redesigned product, then staged recovery.
- The important split is **booked capacity** versus **qualification gap**.

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this in the research session.

When batch-applying this MD later, ingest file:
e2r_stock_web_v12_residual_round_R2_loop_218_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md

Tasks:
1. Parse all JSONL trigger rows under section 5.
2. Confirm all rows have entry_date, entry_price, trigger_type, 30/90/180D MFE/MAE, large_sector_id, canonical_archetype_id.
3. Deduplicate by canonical_archetype_id + ticker + trigger_type + entry_date.
4. Add the shadow rule candidate only as candidate evidence for C06 runtime calibration:
   C06_BOOKED_CAPACITY_QUALIFICATION_GAP_AND_RESET_ENTRY_GATE_V4.
5. Do not loosen Stage3-Green globally.
6. Do not create generic HBM-positive bonus.
7. Implement as C06-specific guard candidate:
   - booked/sold-out/customer allocation unlocks Stage2-Actionable/Yellow;
   - qualification-only or redesigned-product-pending remains Watch/4B;
   - negative HBM sales quarter is not hard 4C if redesigned acceptance path remains alive and price reset has occurred.
8. Leave production scoring unchanged unless batch validation across representative rows supports apply_next_patch.
```

## 12. Next research state

```text
completed_round = R2
completed_loop = 218
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing; original Index Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|C11_BATTERY_ORDERBOOK_RERATING|C01_ORDER_BACKLOG_MARGIN_BRIDGE|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
