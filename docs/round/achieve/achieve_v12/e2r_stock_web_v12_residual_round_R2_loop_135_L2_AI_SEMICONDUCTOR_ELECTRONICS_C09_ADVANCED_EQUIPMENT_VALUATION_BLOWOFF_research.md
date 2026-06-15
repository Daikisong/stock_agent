# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 135
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = mixed_c09_second_pass_order_backed_vs_qualification_blowoff_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|high_MAE_guardrail_stress_test
output_filename = e2r_stock_web_v12_residual_round_R2_loop_135_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
```

This loop adds 5 new independent cases, 4 counterexamples, and 5 residual errors for R2/L2/C09. It is a second-pass C09 study after loop126, but it does not reuse the loop126 DIT / Park Systems / YC / Auros / Intekplus set.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_C09_qualification_and_order_bridge_shadow_profile
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

C09 is not a claim that advanced equipment companies are structurally bad. It is the pressure valve for cases where the market capitalizes a future equipment bridge before the bridge is actually built. The sector-specific residual problem in this pass is the boundary between four evidence states:

1. **signed named-customer order** — can be Stage2-Actionable even inside C09;
2. **QA / qualification stage** — can be Stage2-Watch but should not be Actionable;
3. **IP/risk-removal event** — reduces risk, but does not equal revenue bridge;
4. **technology vocabulary / HBM label only** — remains Stage4B-Watch or false-positive block when price has already run.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R2 |
| selected_loop | 135 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF |
| sector | AI / semiconductor / advanced equipment |
| scope | TC bonder, high-pressure hydrogen annealing, laser compression bonding, CXL/HBM burn-in tester |
| non-scope | C06 customer HBM capacity, C07 HBM equipment order relative strength, C08 test socket/customer quality, C10 memory equipment recovery cycle |

## 3. Previous Coverage / Duplicate Avoidance Check

| check | result |
|---|---|
| No-Repeat priority | C09 Priority 0, Index rows 10, need to 30 = 20, need to 50 = 40 |
| session-aware prior C09 | loop126 added DIT, Park Systems, YC, Auros, Intekplus; this loop avoids those exact symbols and trigger families |
| selected symbols | 042700, 403870, 122640, 412350, 253590 |
| exact duplicate key avoided | canonical_archetype_id + symbol + trigger_type + entry_date not repeated from loop126 |
| same-symbol reuse inside loop | HPSP has two different trigger families: March value-chain blowoff and October patent-win risk-removal |
| minimum new symbol count | 5 >= 2 |
| minimum positive/counter balance | positive 2, counterexample 4 |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| price_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| manifest_max_date | 2026-02-20 |
| MFE/MAE method | max high / min low from entry_date through 30/90/180 tradable rows |
| corporate action policy | 180D contaminated windows blocked; selected windows clean |

## 5. Historical Eligibility Gate

All representative trigger rows are historical. Each entry_date exists in a stock-web tradable shard. Every trigger has at least 180 forward trading rows by the stock-web manifest max date. Required `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct` are present in the table and JSONL rows. No selected 180D window overlaps a corporate-action candidate date.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| TC_BONDER_NAMED_CUSTOMER_ORDER_BACKED_EXCEPTION | C09 | A signed named-customer contract prevents the case from being treated as pure price blowoff, but supplier diversification still caps Green. |
| HPA_MONOPOLY_NVIDIA_VALUECHAIN_PRICE_BLOWOFF | C09 | HPA monopoly and AI value-chain narrative can be over-capitalized when fresh order/revenue bridge is absent. |
| HPA_PATENT_WIN_NOT_REVENUE_BRIDGE_HIGH_MAE | C09 | Patent victory is risk-removal evidence, not direct demand conversion. |
| HPA_EVALUATION_AND_IP_LITIGATION_NOT_PO | C09 | Evaluation-stage equipment plus patent litigation is not equal to PO or production revenue. |
| LCB_QUALIFICATION_HURDLE_NOT_PRODUCTION_ORDER | C09 | HBM bonding technology under qualification has hurdles before production and yield validation. |
| HBM_BURNIN_TESTER_QA_STAGE_LOCAL_RERATING | C09 | QA-stage tester evidence can produce a tradable local rerating, but high MAE blocks Actionable promotion. |

## 7. Case Selection Summary

|case_id|symbol|company_name|trigger_type|role|entry_date|entry_price|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|C09_R2L135_042700_20250516_TCBONDER_CONTRACT|042700|한미반도체|Stage2-Actionable|positive|2025-05-16|91,500|19.13|-14.54|140.44|-14.54|current_profile_correct_but_needs_competition_discount|
|C09_R2L135_403870_20240319_NVIDIA_VALUECHAIN_BLOWOFF|403870|HPSP|Stage4B|counterexample|2024-03-19|51,800|6.76|-39.58|6.76|-56.27|current_profile_false_positive_if_promoted|
|C09_R2L135_403870_20241031_PATENT_WIN_HIGH_MAE|403870|HPSP|Stage2|counterexample|2024-10-31|30,750|26.02|-21.14|26.02|-31.22|current_profile_false_positive_if_stage2_actionable|
|C09_R2L135_122640_20240704_HPA_EVALUATION_NOT_PO|122640|예스티|Stage2|counterexample|2024-07-04|18,600|20.7|-55.27|20.7|-58.55|current_profile_false_positive_if_evaluation_equals_order|
|C09_R2L135_412350_20240604_LCB_QUAL_HURDLE|412350|레이저쎌|Stage4B|counterexample|2024-06-04|10,600|6.04|-56.6|6.04|-71.51|current_profile_false_positive_if_tech_interest_promoted|
|C09_R2L135_253590_20240605_HBM_QA_LOCAL_RALLY|253590|네오셈|Stage2|positive|2024-06-05|11,280|53.1|-34.22|53.1|-34.22|current_profile_mixed_too_late_if_ignored_too_aggressive_if_actionable|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 4
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 6
calibration_usable_trigger_count = 6
representative_trigger_count = 6
current_profile_error_count = 5
```

Positive does not mean immediate Green. In this loop, Hanmi Semiconductor is the clean order-backed exception, while Neosem is only a watch-level local rerating because the evidence was QA-stage, not mass-production revenue. The other four triggers demonstrate why C09 needs a stricter bridge before Stage2-Actionable.

## 9. Evidence Source Map

|symbol|company|trigger_date|source_summary|source_url|
|---|---|---|---|---|
|042700|한미반도체|2025-05-16|SK하이닉스 HBM TC 본더 공급계약 428억원, 한화세미텍 동시 발주 및 공급망 다변화 문맥까지 확인되어 순수 valuation blowoff가 아니라 order-backed exception으로 분류.|https://www.thelec.kr/news/articleView.html?idxno=36050|
|403870|HPSP|2024-03-19|고압수소어닐링 독점·TSMC/엔비디아 밸류체인 narrative는 강했지만 trigger 시점에는 신규 수주/증설 매출 인식 bridge가 약했고, 이후 180D MAE가 크게 발생.|https://www.thebell.co.kr/front/newsview.asp?key=202403191025415680108856|
|403870|HPSP|2024-10-31|특허 무효심판 승소와 소극적 권리범위 심판 각하는 독점 유지 가능성을 높였지만, 보고서상 2025년 장비투자 하향과 EPS 하향이 병존했고 180D MAE가 컸다.|https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2024103122140877K_02_04.pdf&inlineYn=Y&saveKey=research.pdf|
|122640|예스티|2024-07-04|고압수소어닐링 품질평가 막바지와 HBM 장비 누적 수주가 있었지만 본격 양산은 내년 예상, 특허 분쟁 진행 중이라 HPA narrative를 PO와 동일하게 볼 수 없었다.|https://www.newspim.com/news/view/20240628000238|
|412350|레이저쎌|2024-06-04|LCB가 HBM 생산성 신기술로 조명됐지만 기사 자체가 qualification, 양산라인 적용, 수율 검증이라는 관문을 명시했다. 이후 180D MAE가 매우 컸다.|https://m.thebell.co.kr/m/newsview.asp?newskey=202405251150592160106234&svccode=|
|253590|네오셈|2024-06-05|HBM 검사장비가 삼성전자 QA 단계에 들어갔다는 새 정보가 있었고 30/90D MFE가 컸다. 그러나 양산 적용 전 단계라 MAE도 커서 Actionable이 아니라 Stage2-Watch가 맞다.|https://www.thebell.co.kr/front/newsview.asp?key=202406050911561880105029|


## 10. Price Data Source Map

|symbol|company_name|profile_path|price_shards|corporate_action_window_status|
|---|---|---|---|---|
|042700|한미반도체|atlas/symbol_profiles/042/042700.json|atlas/ohlcv_tradable_by_symbol_year/042/042700/2025.csv / atlas/ohlcv_tradable_by_symbol_year/042/042700/2026.csv|clean_180D_window|
|403870|HPSP|atlas/symbol_profiles/403/403870.json|atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv / atlas/ohlcv_tradable_by_symbol_year/403/403870/2025.csv|clean_180D_window|
|403870|HPSP|atlas/symbol_profiles/403/403870.json|atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv / atlas/ohlcv_tradable_by_symbol_year/403/403870/2025.csv|clean_180D_window|
|122640|예스티|atlas/symbol_profiles/122/122640.json|atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv / atlas/ohlcv_tradable_by_symbol_year/122/122640/2025.csv|clean_180D_window|
|412350|레이저쎌|atlas/symbol_profiles/412/412350.json|atlas/ohlcv_tradable_by_symbol_year/412/412350/2024.csv / atlas/ohlcv_tradable_by_symbol_year/412/412350/2025.csv|clean_180D_window|
|253590|네오셈|atlas/symbol_profiles/253/253590.json|atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv / atlas/ohlcv_tradable_by_symbol_year/253/253590/2025.csv|clean_180D_window|


## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|current_profile_verdict|trigger_outcome_label|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_C09_R2L135_042700_20250516_S2A|042700|한미반도체|Stage2-Actionable|2025-05-16|2025-05-16|91,500|19.13|-14.54|19.13|-14.54|140.44|-14.54|2026-01-30|220,000|-18.0|current_profile_correct_but_needs_competition_discount|named_customer_order_backed_positive_exception|
|TRG_C09_R2L135_403870_20240319_4B|403870|HPSP|Stage4B|2024-03-19|2024-03-19|51,800|6.76|-25.87|6.76|-39.58|6.76|-56.27|2024-03-28|55,300|-59.04|current_profile_false_positive_if_promoted|monopoly_story_without_fresh_order_blowoff|
|TRG_C09_R2L135_403870_20241031_S2WATCH|403870|HPSP|Stage2|2024-10-31|2024-10-31|30,750|26.02|-18.05|26.02|-21.14|26.02|-31.22|2024-11-06|38,750|-45.42|current_profile_false_positive_if_stage2_actionable|patent_win_needs_revenue_bridge_before_actionable|
|TRG_C09_R2L135_122640_20240704_S2WATCH|122640|예스티|Stage2|2024-07-04|2024-07-04|18,600|20.7|-23.01|20.7|-55.27|20.7|-58.55|2024-07-16|22,450|-65.66|current_profile_false_positive_if_evaluation_equals_order|evaluation_phase_and_litigation_high_mae_counterexample|
|TRG_C09_R2L135_412350_20240604_4B|412350|레이저쎌|Stage4B|2024-06-04|2024-06-04|10,600|6.04|-17.26|6.04|-56.6|6.04|-71.51|2024-06-04|11,240|-73.13|current_profile_false_positive_if_tech_interest_promoted|qualification_hurdle_hbm_bonding_blowoff_counterexample|
|TRG_C09_R2L135_253590_20240605_S2WATCH|253590|네오셈|Stage2|2024-06-05|2024-06-05|11,280|53.1|-15.96|53.1|-34.22|53.1|-34.22|2024-07-04|17,270|-57.04|current_profile_mixed_too_late_if_ignored_too_aggressive_if_actionable|qa_stage_local_rerating_but_high_mae_watch_only|


## 12. Trigger-Level OHLC Backtest Tables

The OHLC computation used entry_date close as entry_price. If evidence was published after the close but still belongs to the same trading-day reaction family, the same-day close is used conservatively; otherwise the next tradable row would be used. In this set all entries exist directly in the tradable shard.

|trigger_id|price_shard_path|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|drawdown_after_peak_pct|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_C09_R2L135_042700_20250516_S2A|atlas/ohlcv_tradable_by_symbol_year/042/042700/2025.csv / atlas/ohlcv_tradable_by_symbol_year/042/042700/2026.csv|2025-05-16|91,500|19.13|-14.54|19.13|-14.54|140.44|-14.54|2026-01-30|220,000|-18.0|
|TRG_C09_R2L135_403870_20240319_4B|atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv / atlas/ohlcv_tradable_by_symbol_year/403/403870/2025.csv|2024-03-19|51,800|6.76|-25.87|6.76|-39.58|6.76|-56.27|2024-03-28|55,300|-59.04|
|TRG_C09_R2L135_403870_20241031_S2WATCH|atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv / atlas/ohlcv_tradable_by_symbol_year/403/403870/2025.csv|2024-10-31|30,750|26.02|-18.05|26.02|-21.14|26.02|-31.22|2024-11-06|38,750|-45.42|
|TRG_C09_R2L135_122640_20240704_S2WATCH|atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv / atlas/ohlcv_tradable_by_symbol_year/122/122640/2025.csv|2024-07-04|18,600|20.7|-23.01|20.7|-55.27|20.7|-58.55|2024-07-16|22,450|-65.66|
|TRG_C09_R2L135_412350_20240604_4B|atlas/ohlcv_tradable_by_symbol_year/412/412350/2024.csv / atlas/ohlcv_tradable_by_symbol_year/412/412350/2025.csv|2024-06-04|10,600|6.04|-17.26|6.04|-56.6|6.04|-71.51|2024-06-04|11,240|-73.13|
|TRG_C09_R2L135_253590_20240605_S2WATCH|atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv / atlas/ohlcv_tradable_by_symbol_year/253/253590/2025.csv|2024-06-05|11,280|53.1|-15.96|53.1|-34.22|53.1|-34.22|2024-07-04|17,270|-57.04|


## 13. Score / Return Alignment

|symbol|trigger_date|trigger_type|score_before_shadow|score_after_shadow|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|alignment_read|
|---|---|---|---|---|---|---|---|---|---|
|042700|2025-05-16|Stage2-Actionable|76.0|81.0|19.13|-14.54|140.44|-14.54|named_customer_order_backed_positive_exception|
|403870|2024-03-19|Stage4B|77.0|67.0|6.76|-39.58|6.76|-56.27|monopoly_story_without_fresh_order_blowoff|
|403870|2024-10-31|Stage2|75.0|69.0|26.02|-21.14|26.02|-31.22|patent_win_needs_revenue_bridge_before_actionable|
|122640|2024-07-04|Stage2|74.0|65.0|20.7|-55.27|20.7|-58.55|evaluation_phase_and_litigation_high_mae_counterexample|
|412350|2024-06-04|Stage4B|72.0|60.0|6.04|-56.6|6.04|-71.51|qualification_hurdle_hbm_bonding_blowoff_counterexample|
|253590|2024-06-05|Stage2|71.0|72.0|53.1|-34.22|53.1|-34.22|qa_stage_local_rerating_but_high_mae_watch_only|


The alignment problem is asymmetric. Hanmi's signed order had a large positive 180D MFE, so the shadow rule should not over-penalize all advanced equipment cases. But HPSP March, HPSP October, YEST, and LaserCell show that technology leadership, IP victory, evaluation stage, and qualification narrative are not enough to become Actionable. Neosem sits in the middle: the new QA-stage evidence did produce a local +53.10% path, but the -34.22% MAE says the right label is Stage2-Watch with a high-MAE guard.

## 14. Raw Component Score Breakdown

Component columns are directional raw research scores for later deterministic coding-agent interpretation. They are not production-score changes.

|trigger_id|eps_fcf_explosion|visibility|bottleneck_pricing|mispricing|valuation_rerating|capital_allocation|info_confidence|raw_component_total|shadow_score_after|
|---|---|---|---|---|---|---|---|---|---|
|TRG_C09_R2L135_042700_20250516_S2A|14|16|15|13|12|5|6|81|81.0|
|TRG_C09_R2L135_403870_20240319_4B|12|8|15|10|4|3|5|57|67.0|
|TRG_C09_R2L135_403870_20241031_S2WATCH|10|9|15|9|6|3|6|58|69.0|
|TRG_C09_R2L135_122640_20240704_S2WATCH|9|8|12|11|3|3|5|51|65.0|
|TRG_C09_R2L135_412350_20240604_4B|8|6|10|10|2|2|4|42|60.0|
|TRG_C09_R2L135_253590_20240605_S2WATCH|11|10|12|11|9|4|6|63|72.0|


## 15. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| Would current profile catch all cases? | Not fully. The global price-only and 4B rules help, but C09 still needs a qualification/order bridge distinction. |
| Was Stage2 bonus too strong? | Too strong if QA, qualification, patent victory, or HBM vocabulary is treated as equivalent to PO/revenue bridge. |
| Was Yellow 75 too high/low? | Appropriate for signed order evidence; too low for high-valuation narratives if no customer order or revenue timing exists. |
| Was Green 87/revision 55 too strict? | Appropriate. None of these should be Green at trigger; even Hanmi has competition/supplier-diversification discount. |
| Was price-only blowoff guard appropriate? | Kept and strengthened. C09 needs a more explicit advanced-equipment evidence ladder. |
| Was full 4B non-price requirement appropriate? | Kept. However, C09 should allow Stage4B-Watch when non-price evidence says qualification is unfinished or IP risk remains unresolved. |
| Was hard 4C routing late? | No hard 4C row is proposed here; the loop is about Stage2/4B boundary and high-MAE watch gating. |

## 16. Stage2 / Yellow / Green Comparison

| symbol | trigger | suggested before | suggested after C09 shadow gate | reason |
|---|---|---|---|---|
| 042700 | 2025-05-16 SK hynix TC bonder contract | Stage2-Actionable | Stage2-Actionable / Yellow watch, not Green | Named customer, contract value, and delivery timing are real; competition discount caps Green. |
| 403870 | 2024-03-19 Nvidia/TSMC value-chain monopoly narrative | Stage2 or Yellow if narrative-heavy | Stage4B-Watch | No fresh order/revenue bridge; MFE180 only +6.76% versus MAE180 -56.27%. |
| 403870 | 2024-10-31 patent victory | Stage2-Actionable if risk-removal overweighted | Stage2-Watch | IP victory is real, but 2025 capex/EPS uncertainty and MAE180 -31.22% block Actionable. |
| 122640 | 2024-07-04 HPA evaluation / HBM equipment | Stage2 | Stage2-Watch / 4B-Watch | Evaluation and patent dispute are not PO; MAE180 -58.55%. |
| 412350 | 2024-06-04 LCB HBM qualification | Stage2 | Stage4B-Watch | Article explicitly says qualification and mass-production hurdles remain; MAE180 -71.51%. |
| 253590 | 2024-06-05 HBM tester QA stage | ignored or over-promoted | Stage2-Watch only | New information drove local +53.10% MFE, but QA-stage and -34.22% MAE block Actionable. |

## 17. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | entry_date | MFE_30D_pct | MAE_30D_pct | MFE_180D_pct | MAE_180D_pct | 4B interpretation |
|---|---:|---:|---:|---:|---:|---:|---|
| TRG_C09_R2L135_403870_20240319_4B | 403870 | 2024-03-19 | 6.76 | -25.87 | 6.76 | -56.27 | Full 4B-watch was justified; price never built a durable rerating path. |
| TRG_C09_R2L135_412350_20240604_4B | 412350 | 2024-06-04 | 6.04 | -17.26 | 6.04 | -71.51 | Qualification hurdle plus poor path should remain 4B-watch/false-positive block. |
| TRG_C09_R2L135_253590_20240605_S2WATCH | 253590 | 2024-06-05 | 53.10 | -15.96 | 53.10 | -34.22 | Not a pure 4B failure; watch-level signal had a local opportunity but Actionable would be too risky. |

## 18. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L2_C09_ADVANCED_EQUIPMENT_EVIDENCE_LADDER_V2
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS / C09
proposal_type = sector_specific_shadow_only
production_scoring_changed = false
```

For advanced semiconductor equipment, use an evidence ladder before Stage2-Actionable:

```text
Tier A: signed named-customer order + contract value + delivery period -> Stage2-Actionable allowed, Green still blocked until revision/margin bridge.
Tier B: QA / qualification / evaluation stage -> Stage2-Watch only; high-MAE guard applies.
Tier C: IP victory / risk-removal -> Stage2-Watch only unless order/revenue bridge appears.
Tier D: technology vocabulary / HBM / AI / Nvidia value-chain label without PO -> Stage4B-Watch or false-positive block when price has already expanded.
```

## 19. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C09_ORDER_BACKED_VS_QUALIFICATION_LADDER_AND_HIGH_MAE_GATE_V2
scope = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
positive_exception_examples = 042700_20250516, 253590_20240605_watch_only
false_positive_examples = 403870_20240319, 403870_20241031, 122640_20240704, 412350_20240604
new_axis_proposed = c09_order_backed_vs_qualification_ladder
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened = null
```

The rule is not “equipment expensive = bad.” It is more like a customs gate. A signed order is a passport. QA/evaluation is a boarding pass with no visa. IP victory is a removed obstacle, not arrival at the destination. HBM vocabulary alone is a travel brochure.

## 20. Residual Contribution Summary

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 6
new_trigger_family_count = 6
positive_case_count = 2
counterexample_count = 4
current_profile_error_count = 5
diversity_score_summary = second_pass_C09_uses_new_symbols_and_new_trigger_families_vs_loop126; adds signed_order_vs_qualification_vs_patent_victory_boundaries
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

This loop adds 5 new independent cases, 4 counterexamples, and 5 residual errors for R2/L2/C09.

## 21. Machine-Readable Rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_C09_R2L135_042700_20250516_S2A", "case_id": "C09_R2L135_042700_20250516_TCBONDER_CONTRACT", "selected_round": "R2", "selected_loop": 135, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "TC_BONDER_NAMED_CUSTOMER_ORDER_BACKED_EXCEPTION", "symbol": "042700", "company_name": "한미반도체", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-05-16", "entry_date": "2025-05-16", "entry_price": 91500, "price_source": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 19.13, "MAE_30D_pct": -14.54, "MFE_90D_pct": 19.13, "MAE_90D_pct": -14.54, "MFE_180D_pct": 140.44, "MAE_180D_pct": -14.54, "peak_date": "2026-01-30", "peak_price": 220000, "drawdown_after_peak_pct": -18.0, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C09|042700|Stage2-Actionable|2025-05-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "positive_or_counterexample": "positive", "current_profile_verdict": "current_profile_correct_but_needs_competition_discount", "evidence_url": "https://www.thelec.kr/news/articleView.html?idxno=36050", "source_url": "https://www.thelec.kr/news/articleView.html?idxno=36050", "score_before": 76.0, "score_after": 81.0, "trigger_outcome_label": "named_customer_order_backed_positive_exception"}
{"row_type": "trigger", "trigger_id": "TRG_C09_R2L135_403870_20240319_4B", "case_id": "C09_R2L135_403870_20240319_NVIDIA_VALUECHAIN_BLOWOFF", "selected_round": "R2", "selected_loop": 135, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HPA_MONOPOLY_NVIDIA_VALUECHAIN_PRICE_BLOWOFF", "symbol": "403870", "company_name": "HPSP", "trigger_type": "Stage4B", "trigger_date": "2024-03-19", "entry_date": "2024-03-19", "entry_price": 51800, "price_source": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 6.76, "MAE_30D_pct": -25.87, "MFE_90D_pct": 6.76, "MAE_90D_pct": -39.58, "MFE_180D_pct": 6.76, "MAE_180D_pct": -56.27, "peak_date": "2024-03-28", "peak_price": 55300, "drawdown_after_peak_pct": -59.04, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C09|403870|Stage4B|2024-03-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "positive_or_counterexample": "counterexample", "current_profile_verdict": "current_profile_false_positive_if_promoted", "evidence_url": "https://www.thebell.co.kr/front/newsview.asp?key=202403191025415680108856", "source_url": "https://www.thebell.co.kr/front/newsview.asp?key=202403191025415680108856", "score_before": 77.0, "score_after": 67.0, "trigger_outcome_label": "monopoly_story_without_fresh_order_blowoff"}
{"row_type": "trigger", "trigger_id": "TRG_C09_R2L135_403870_20241031_S2WATCH", "case_id": "C09_R2L135_403870_20241031_PATENT_WIN_HIGH_MAE", "selected_round": "R2", "selected_loop": 135, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HPA_PATENT_WIN_NOT_REVENUE_BRIDGE_HIGH_MAE", "symbol": "403870", "company_name": "HPSP", "trigger_type": "Stage2", "trigger_date": "2024-10-31", "entry_date": "2024-10-31", "entry_price": 30750, "price_source": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 26.02, "MAE_30D_pct": -18.05, "MFE_90D_pct": 26.02, "MAE_90D_pct": -21.14, "MFE_180D_pct": 26.02, "MAE_180D_pct": -31.22, "peak_date": "2024-11-06", "peak_price": 38750, "drawdown_after_peak_pct": -45.42, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C09|403870|Stage2|2024-10-31", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "positive_or_counterexample": "counterexample", "current_profile_verdict": "current_profile_false_positive_if_stage2_actionable", "evidence_url": "https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2024103122140877K_02_04.pdf&inlineYn=Y&saveKey=research.pdf", "source_url": "https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2024103122140877K_02_04.pdf&inlineYn=Y&saveKey=research.pdf", "score_before": 75.0, "score_after": 69.0, "trigger_outcome_label": "patent_win_needs_revenue_bridge_before_actionable"}
{"row_type": "trigger", "trigger_id": "TRG_C09_R2L135_122640_20240704_S2WATCH", "case_id": "C09_R2L135_122640_20240704_HPA_EVALUATION_NOT_PO", "selected_round": "R2", "selected_loop": 135, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HPA_EVALUATION_AND_IP_LITIGATION_NOT_PO", "symbol": "122640", "company_name": "예스티", "trigger_type": "Stage2", "trigger_date": "2024-07-04", "entry_date": "2024-07-04", "entry_price": 18600, "price_source": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 20.7, "MAE_30D_pct": -23.01, "MFE_90D_pct": 20.7, "MAE_90D_pct": -55.27, "MFE_180D_pct": 20.7, "MAE_180D_pct": -58.55, "peak_date": "2024-07-16", "peak_price": 22450, "drawdown_after_peak_pct": -65.66, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C09|122640|Stage2|2024-07-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "positive_or_counterexample": "counterexample", "current_profile_verdict": "current_profile_false_positive_if_evaluation_equals_order", "evidence_url": "https://www.newspim.com/news/view/20240628000238", "source_url": "https://www.newspim.com/news/view/20240628000238", "score_before": 74.0, "score_after": 65.0, "trigger_outcome_label": "evaluation_phase_and_litigation_high_mae_counterexample"}
{"row_type": "trigger", "trigger_id": "TRG_C09_R2L135_412350_20240604_4B", "case_id": "C09_R2L135_412350_20240604_LCB_QUAL_HURDLE", "selected_round": "R2", "selected_loop": 135, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "LCB_QUALIFICATION_HURDLE_NOT_PRODUCTION_ORDER", "symbol": "412350", "company_name": "레이저쎌", "trigger_type": "Stage4B", "trigger_date": "2024-06-04", "entry_date": "2024-06-04", "entry_price": 10600, "price_source": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 6.04, "MAE_30D_pct": -17.26, "MFE_90D_pct": 6.04, "MAE_90D_pct": -56.6, "MFE_180D_pct": 6.04, "MAE_180D_pct": -71.51, "peak_date": "2024-06-04", "peak_price": 11240, "drawdown_after_peak_pct": -73.13, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C09|412350|Stage4B|2024-06-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "positive_or_counterexample": "counterexample", "current_profile_verdict": "current_profile_false_positive_if_tech_interest_promoted", "evidence_url": "https://m.thebell.co.kr/m/newsview.asp?newskey=202405251150592160106234&svccode=", "source_url": "https://m.thebell.co.kr/m/newsview.asp?newskey=202405251150592160106234&svccode=", "score_before": 72.0, "score_after": 60.0, "trigger_outcome_label": "qualification_hurdle_hbm_bonding_blowoff_counterexample"}
{"row_type": "trigger", "trigger_id": "TRG_C09_R2L135_253590_20240605_S2WATCH", "case_id": "C09_R2L135_253590_20240605_HBM_QA_LOCAL_RALLY", "selected_round": "R2", "selected_loop": 135, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_BURNIN_TESTER_QA_STAGE_LOCAL_RERATING", "symbol": "253590", "company_name": "네오셈", "trigger_type": "Stage2", "trigger_date": "2024-06-05", "entry_date": "2024-06-05", "entry_price": 11280, "price_source": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "MFE_30D_pct": 53.1, "MAE_30D_pct": -15.96, "MFE_90D_pct": 53.1, "MAE_90D_pct": -34.22, "MFE_180D_pct": 53.1, "MAE_180D_pct": -34.22, "peak_date": "2024-07-04", "peak_price": 17270, "drawdown_after_peak_pct": -57.04, "forward_window_trading_days": 180, "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C09|253590|Stage2|2024-06-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "positive_or_counterexample": "positive", "current_profile_verdict": "current_profile_mixed_too_late_if_ignored_too_aggressive_if_actionable", "evidence_url": "https://www.thebell.co.kr/front/newsview.asp?key=202406050911561880105029", "source_url": "https://www.thebell.co.kr/front/newsview.asp?key=202406050911561880105029", "score_before": 71.0, "score_after": 72.0, "trigger_outcome_label": "qa_stage_local_rerating_but_high_mae_watch_only"}
```

## 22. Aggregate Row

```json
{
  "row_type": "aggregate",
  "selected_round": "R2",
  "selected_loop": 135,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "calibration_usable_case_count": 6,
  "calibration_usable_trigger_count": 6,
  "representative_trigger_count": 6,
  "positive_case_count": 2,
  "counterexample_count": 4,
  "current_profile_error_count": 5,
  "coverage_before_index_baseline": 10,
  "coverage_after_if_accepted_index_baseline": 16,
  "coverage_before_session_aware_after_loop126": 16,
  "coverage_after_if_accepted_session_aware": 22,
  "need_to_30_after_if_accepted_session_aware": 8,
  "need_to_50_after_if_accepted_session_aware": 28,
  "rule_candidate": "C09_ORDER_BACKED_VS_QUALIFICATION_LADDER_AND_HIGH_MAE_GATE_V2",
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 23. Shadow Weight Candidate

```json
{
  "row_type": "shadow_weight_candidate",
  "rule_id": "C09_ORDER_BACKED_VS_QUALIFICATION_LADDER_AND_HIGH_MAE_GATE_V2",
  "scope": "canonical_archetype_id=C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "proposal_type": "shadow_only_for_later_batch_review",
  "do_not_apply_now": true,
  "intended_effect": {
    "signed_named_customer_order_with_contract_size": "+Stage2ActionableBridge",
    "QA_or_qualification_without_PO": "cap_at_Stage2_Watch",
    "patent_or_IP_win_without_revenue_bridge": "cap_at_Stage2_Watch",
    "technology_vocabulary_after_price_expansion": "route_to_Stage4B_Watch_or_false_positive_block",
    "high_MAE_after_local_spike": "apply_high_MAE_guard_before_Actionable"
  },
  "positive_support": [
    "042700_20250516",
    "253590_20240605_watch_only"
  ],
  "counterexample_support": [
    "403870_20240319",
    "403870_20241031",
    "122640_20240704",
    "412350_20240604"
  ]
}
```

## 24. Narrative-Only / Rejected Rows

```text
narrative_only_or_rejected_count = 0
rows_missing_required_mfe_mae = 0
rows_missing_entry_price_or_date = 0
rows_with_noncanonical_trigger_type = 0
rows_with_corporate_action_contamination = 0
```

## 25. Batch Ingest Self-Audit

```text
expected_v12_result_file = true
filename_pattern_pass = true
metadata_filename_consistency = pass
jsonl_trigger_row_count = 6
calibration_usable_trigger_count = 6
representative_trigger_count = 6
new_weight_evidence_candidate_count = 6
guardrail_candidate_count = 5
narrative_only_or_rejected_count = 0
rows_missing_required_mfe_mae = 0
rows_missing_entry_price_or_date = 0
rows_with_noncanonical_trigger_type = 0
rows_with_compact_mfe_mae_alias_only = 0
ready_for_batch_ingest = true
```

## 26. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

Later coding agent task:
1. Ingest this MD as a standard v12 result file.
2. Parse the trigger JSONL rows.
3. Verify filename/metadata consistency for R2 loop 135 L2 C09.
4. Confirm all trigger rows have required 30/90/180D MFE/MAE, entry_date, entry_price, price_source, price_basis, price_adjustment_status, large_sector_id, canonical_archetype_id, same_entry_group_id, and aggregate_group_role.
5. Add this loop to C09 coverage only if no hard duplicate key exists.
6. Evaluate shadow rule C09_ORDER_BACKED_VS_QUALIFICATION_LADDER_AND_HIGH_MAE_GATE_V2 against existing C09 promotion decisions.
7. If accepted, implement only a scope-limited C09 patch candidate. Do not change global Stage2, Green, 4B, or 4C thresholds.
```

## 27. Next Research State

```text
completed_round = R2
completed_loop = 135
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|C06_HBM_MEMORY_CUSTOMER_CAPACITY|C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|C11_BATTERY_ORDERBOOK_RERATING
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
