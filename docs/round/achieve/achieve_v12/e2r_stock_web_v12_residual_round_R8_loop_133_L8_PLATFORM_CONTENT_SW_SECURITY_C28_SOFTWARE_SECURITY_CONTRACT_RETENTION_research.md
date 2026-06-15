# E2R Stock-Web v12 Residual Research — R8 / C28 Software Security Contract Retention

```yaml
output_file: e2r_stock_web_v12_residual_round_R8_loop_133_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
completed_round: R8
completed_loop: 133
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: mixed_c28_security_contract_retention_margin_bridge_leaf_set
loop_objective: coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
stock_web_calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
do_not_propose_new_weight_delta: false
```

## 1. Selection rationale

The coverage index is used as a no-repeat ledger, not as the research prompt. After prior session outputs had already touched C18, C26, C29, C30, C02, C09, C14, C10, C06, C07, C11, and C01, the remaining under-30 canonical bucket in the current index was **C28_SOFTWARE_SECURITY_CONTRACT_RETENTION**.

C28 currently has 28 representative rows in the index. The target is not to prove that “security is good”; the target is to split:

1. real contract-retention / renewal / managed-service / ARR-like evidence that converts into margin or revision;
2. stable-but-low-growth maintenance revenue that does not rerate;
3. AI/security/quantum/policy partnership vocabulary that only creates a price-only blowoff;
4. R&D-cost or operating-loss thesis break that should route to 4C rather than linger in Stage2-Watch.

```text
coverage_before = C28 rows 28
new_representative_trigger_rows = 9
coverage_after_if_accepted = C28 rows 37
need_to_30_after_if_accepted = 0
need_to_50_after_if_accepted = 13
```

## 2. Price-source validation

```text
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

All trigger rows below use next-trading-day close as `entry_price` when the evidence came after or on the trigger date. The MFE/MAE windows are calculated from the entry row through the 30/90/180 tradable-row windows, using `h` for MFE and `l` for MAE. No price after the stock-web manifest max date is fabricated.

Corporate-action screening:

```text
263860: corporate action candidates only in 2018; selected 2024/2025 windows clean.
150900: no corporate-action candidate in selected window.
067920: corporate action candidate outside selected window.
203650: selected 2024 180D window clean; later 2025 corporate-action candidates not used.
042510: selected 2024 entries finish their D+180 windows before the 2025-05 corporate-action candidate.
411080: no corporate-action candidate in selected 2024 windows.
```

## 3. Case inventory and price-path results

| case | ticker | trigger | entry | class | trigger_type | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | proposed |
|---|---:|---:|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| C28_263860_GENIAN_Q3_NAC_EDR_MANAGED_SERVICE_2024_11_14 | 263860 | 2024-11-14 | 2024-11-15 @9410 | positive | Stage2-Actionable | 16.79% | -8.82% | 40.81% | -8.82% | 153.99% | -8.82% | Stage2-Actionable |
| C28_263860_GENIAN_ANNUAL_NAC_EDR_ZERO_TRUST_2025_02_19 | 263860 | 2025-02-19 | 2025-02-20 @11110 | positive | Stage3-Yellow | 39.06% | -7.38% | 111.97% | -7.38% | 170.03% | -7.38% | Stage3-Yellow |
| C28_150900_FASOO_STABLE_RETENTION_LOW_BETA_2024_12_12 | 150900 | 2024-12-12 | 2024-12-13 @5080 | counterexample | Stage2-Watch | 6.30% | -8.56% | 10.83% | -18.31% | 10.83% | -18.31% | Stage2-Watch |
| C28_067920_IGLOO_PUBLIC_SECURITY_MONITORING_MARGIN_DRAG_2024_05_15 | 067920 | 2024-05-15 | 2024-05-16 @6210 | counterexample | Stage2-Watch | 0.16% | -10.95% | 0.16% | -20.69% | 0.16% | -23.83% | Stage2-Watch-Blocked |
| C28_203650_DREAMSECURITY_DEEPFAKE_QUANTUM_THEME_2024_03_18 | 203650 | 2024-03-18 | 2024-03-19 @3740 | counterexample | Stage4B | 1.60% | -15.78% | 1.60% | -26.47% | 4.28% | -38.90% | Stage4B |
| C28_042510_RAONSECURE_MOBILE_ID_FORECAST_BUT_Q1_LOSS_2024_05_23 | 042510 | 2024-05-23 | 2024-05-24 @2410 | counterexample | Stage2-Watch | 6.43% | -5.81% | 7.68% | -29.92% | 7.68% | -31.54% | Stage2-Watch |
| C28_042510_RAONSECURE_MOBILE_ID_PRICE_SURGE_Q1_LOSS_2024_07_02 | 042510 | 2024-07-02 | 2024-07-03 @2300 | counterexample | Stage4B | 10.87% | -26.57% | 12.83% | -27.04% | 12.83% | -28.26% | Stage4B |
| C28_411080_SANDSLAB_MS_AI_SECURITY_COLLAB_PRICE_BLOWOFF_2024_03_26 | 411080 | 2024-03-26 | 2024-03-27 @11260 | counterexample | Stage4B | 48.22% | -17.23% | 48.22% | -53.64% | 48.22% | -53.64% | Stage4B |
| C28_411080_SANDSLAB_GOV_PROJECT_RND_COST_THESIS_BREAK_2024_05_03 | 411080 | 2024-05-03 | 2024-05-07 @12080 | counterexample | Stage4C | 2.81% | -24.01% | 2.81% | -56.79% | 4.14% | -56.79% | Stage4C |

## 4. Evidence log

| symbol | trigger_date | evidence summary | source |
|---|---:|---|---|
| 263860 지니언스 | 2024-11-14 | 2024년 3Q 영업이익 22억원, 전년동기 대비 660.8% 증가. NAC 지자체/대기업 수요 확대, Cloud NAC Managed Service 고객 확보, EDR 구독형 비즈니스 확대가 동시에 확인된 trigger. | https://www.genians.co.kr/pr-room/press/20241114 |
| 263860 지니언스 | 2025-02-19 | 2024년 연결 매출 496억원, 영업이익 98억원으로 전년 대비 각각 15.7%, 52.2% 증가. NAC·EDR·제로트러스트 3대 사업 성장과 27개국 143개 고객 확보가 확인된 annual confirmation trigger. | https://www.genians.co.kr/pr-room/press/20250219 |
| 150900 파수 | 2024-12-12 | 데이터 보안/문서보안의 고객 유지력과 진입장벽은 있으나, 연결 기준 2024년 매출 461억원·영업이익 39억원으로 성장/마진 레버리지가 제한적. 안정 유지보수형 보안은 retention은 맞아도 rerating trigger로는 약했다. | https://www.fasoo.ai/financial-information |
| 067920 이글루 | 2024-05-15 | 공공 보안관제 계약 기반은 안정적이지만 파견 인력 중심 비용 구조가 영업레버리지를 막았다. 2023년 영업이익 57억원, 전년 대비 28.6% 감소 및 OPM 5.3%로, C28의 retention만으로는 Stage2-Actionable이 부족한 사례. | https://m.thebell.co.kr/m/newsview.asp?newskey=202405151413369760101175&svccode= |
| 203650 드림시큐리티 | 2024-03-18 | 딥페이크·AI해킹·총선 보안·양자암호 장비 기대가 결합된 테마성 trigger. 보안 vocabulary는 강했지만 ARR/renewal/contract retention/margin bridge가 비어 있어 C28 positive가 아니라 price-only/theme 4B로 처리해야 하는 사례. | https://www.thebigdata.co.kr/view.php?ud=202403180447191908cd1e7f0bdf_23 |
| 042510 라온시큐어 | 2024-05-23 | 모바일 신분증/디지털 ID 플랫폼 기대와 2024년 흑자전환 전망은 있었으나, entry 당시에는 1Q24 영업손실과 계절성, 플랫폼 전환의 마진 확인이 남아 있었다. 장기적으로는 2024년 흑자전환을 확인했지만, trigger 시점 Stage2-Actionable은 이른 사례. | https://www.dailyinvest.kr/news/articleView.html?idxno=58849 |
| 042510 라온시큐어 | 2024-07-02 | 모바일 신분증 기대가 재점화되었지만 1Q24 손실과 4Q 편중 구조가 남아 있었다. 가격경로는 90D/180D MAE가 -27%~-28%로, C28 positive보다 local 4B/high-MAE guard 대상이었다. | https://www.thebigdata.co.kr/view.php?ud=202407020552169831cd1e7f0bdf_23 |
| 411080 샌즈랩 | 2024-03-26 | 한국MS와 AI 기반 사이버보안 기술 협업 소식으로 주가가 상한가를 기록한 trigger. partnership headline은 강했지만 ARR/RPO/retention/renewal/margin bridge가 없어 C28 positive보다 price-only local 4B 스트레스 케이스로 분류. | https://www.etnews.com/20240326000085 |
| 411080 샌즈랩 | 2024-05-03 | AI 보안 국책과제/협업 narrative가 이어졌지만, 이후 상반기 영업손실 확대와 높은 R&D 비용 부담이 확인되며 revenue retention보다 비용 흡수 리스크가 지배했다. 180D MAE -56.79%로 hard 4C thesis-break guard가 필요했다. | https://www.ibtomato.com/ExternalView.aspx?no=13146&type=1 |

## 5. Case notes

### 5.1 263860 지니언스 — C28 positive: retention + managed service + margin bridge

The 2024-11-14 trigger is a clean C28 positive. The evidence was not just “cybersecurity demand.” It tied NAC demand in municipalities and large enterprises, Cloud NAC Managed Service customer acquisition, EDR subscription expansion, and 3Q margin acceleration into one bridge. The path confirmed it: entry at 9,410, D180 MFE +153.99%, and D180 MAE only -8.82%.

The 2025-02-19 annual trigger is the stronger Yellow confirmation. Revenue of 496억원 and operating profit of 98억원, plus 20 years of profitability and global customer expansion, converted C28 from a vocabulary bucket into a retention/margin-leverage bucket. Entry at 11,110 produced D180 MFE +170.03% with D180 MAE -7.38%.

Shadow implication: C28 should allow an earlier Stage2-Actionable / Stage3-Yellow route when evidence includes:
- recurring or managed service customer expansion,
- NAC/EDR/zero-trust cross-product growth,
- operating profit expansion,
- customer base expansion or renewal quality.

### 5.2 150900 파수 — C28 counterexample: stable retention, weak rerating

Fasoo is not a failed business case; it is a failed rerating-trigger case. The financial table shows stable revenue and operating profit, but the price path did not reward the trigger. Entry at 5,080 produced D180 MFE +10.83% and D180 MAE -18.31%.

Shadow implication: stable maintenance and loyal customers should not automatically become Stage2-Actionable. C28 needs a **retention-to-margin/revision bridge**, not merely retention.

### 5.3 067920 이글루 — C28 counterexample: public contract stability with labor-cost drag

Igloo had public-sector security-monitoring contracts and a stable business base, but the cost structure was labor-heavy. The evidence explicitly points to profitability drag: 2023 operating profit declined and OPM stayed low. Price confirmed the issue: from entry 6,210, D180 MFE was only +0.16% while D180 MAE reached -23.83%.

Shadow implication: public security contract retention should be penalized when delivery is people-intensive and does not scale.

### 5.4 203650 드림시큐리티 — C28 counterexample: deepfake/quantum/security vocabulary without retention bridge

The trigger was thematically strong: deepfake, AI hacking, election security, quantum cryptography. But there was no ARR, renewal, RPO, named enterprise contract, retention, or operating leverage bridge. Entry at 3,740 produced D180 MFE +4.28% and D180 MAE -38.90%.

Shadow implication: C28 must explicitly block **security-theme vocabulary** from being treated as C28 positive. This belongs to Stage4B or Stage2-Watch at most.

### 5.5 042510 라온시큐어 — C28 counterexample: digital ID platform forecast needs margin confirmation

Mobile ID and digital-ID platform growth were real themes, and later 2024 full-year data did confirm revenue growth and black-turnaround. But at the 2024-05 and 2024-07 trigger points, margin confirmation was still too incomplete. The price path was harsh: the May entry had D180 MAE -31.54%, and the July entry had D180 MAE -28.26%.

Shadow implication: policy/platform digital-ID evidence should not become Stage2-Actionable until the system sees:
- current margin bridge or quarterly loss improvement,
- signed deployment economics,
- platform take-rate / recurring service revenue,
- not only headline adoption.

### 5.6 411080 샌즈랩 — C28 counterexample and 4C thesis-break stress test

The 2024-03-26 MS collaboration trigger was exactly the kind of event C28 can over-score: it has Microsoft, AI, cybersecurity, partnership, and dramatic price action. But the bridge to recurring contract retention was not present. Entry at 11,260 produced an impressive D30 MFE +48.22%, but also D90/D180 MAE -53.64% and post-peak drawdown -68.72%. That is not C28 rerating; it is local 4B blowoff.

The 2024-05-03 follow-up trigger worsened the diagnosis. When R&D expense and operating-loss pressure later dominated, the case shifted from local 4B to 4C thesis-break watch. Entry at 12,080 produced D180 MAE -56.79%.

Shadow implication: C28 should route AI-security partnership spikes without revenue/retention bridge to 4B, and operating-loss/R&D-cost confirmation should route to 4C.

## 6. Score-return alignment

| case | before | after | residual error | raw component emphasis |
|---|---:|---:|---|---|
| C28_263860_GENIAN_Q3_NAC_EDR_MANAGED_SERVICE_2024_11_14 | 72.0 | 79.0 | missed_structural_positive_if_retention_managed_service_not_weighted | contract=72, margin=78, customer=76, rel_strength=72, exec_risk=24 |
| C28_263860_GENIAN_ANNUAL_NAC_EDR_ZERO_TRUST_2025_02_19 | 76.0 | 82.0 | yellow_lateness_if_global_security_customer_retention_not_recognized | contract=78, margin=83, customer=86, rel_strength=80, exec_risk=18 |
| C28_150900_FASOO_STABLE_RETENTION_LOW_BETA_2024_12_12 | 70.0 | 62.0 | retention_without_growth_leverage_false_positive | contract=63, margin=42, customer=78, rel_strength=38, exec_risk=25 |
| C28_067920_IGLOO_PUBLIC_SECURITY_MONITORING_MARGIN_DRAG_2024_05_15 | 68.0 | 55.0 | labor_intensive_security_revenue_false_positive_if_contract_retention_overweighted | contract=70, margin=24, customer=72, rel_strength=20, exec_risk=44 |
| C28_203650_DREAMSECURITY_DEEPFAKE_QUANTUM_THEME_2024_03_18 | 64.0 | 48.0 | security_theme_without_contract_retention_should_not_get_positive_stage | contract=18, margin=12, customer=35, rel_strength=70, exec_risk=55 |
| C28_042510_RAONSECURE_MOBILE_ID_FORECAST_BUT_Q1_LOSS_2024_05_23 | 69.0 | 58.0 | platform_growth_forecast_without_current_margin_bridge_high_mae | contract=55, margin=24, customer=64, rel_strength=52, exec_risk=48 |
| C28_042510_RAONSECURE_MOBILE_ID_PRICE_SURGE_Q1_LOSS_2024_07_02 | 67.0 | 52.0 | high_mae_guard_needed_for_policy_platform_theme | contract=40, margin=18, customer=58, rel_strength=68, exec_risk=58 |
| C28_411080_SANDSLAB_MS_AI_SECURITY_COLLAB_PRICE_BLOWOFF_2024_03_26 | 71.0 | 49.0 | ai_security_partnership_without_contract_retention_should_be_4b_not_stage2 | contract=20, margin=8, customer=45, rel_strength=95, exec_risk=72 |
| C28_411080_SANDSLAB_GOV_PROJECT_RND_COST_THESIS_BREAK_2024_05_03 | 66.0 | 42.0 | late_4c_if_rnd_cost_operating_loss_not_connected_to_thesis_break | contract=18, margin=5, customer=38, rel_strength=60, exec_risk=84 |


## 7. Residual contribution summary

```text
new_axis_proposed = c28_recurring_security_contract_margin_bridge_gate
sector_specific_rule_candidate = L8_SECURITY_RECURRING_REVENUE_OPERATING_LEVERAGE_GATE_V1
canonical_archetype_rule_candidate = C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
existing_axis_weakened = null
```

### Proposed C28 rule candidate

```text
C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1

IF canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
    positive_stage_credit is allowed only when at least two of the following are true:
        1. named enterprise/public customer renewal or expansion,
        2. managed-service / subscription / ARR-like revenue growth,
        3. contract-retention evidence tied to margin or revision,
        4. multi-product security expansion with customer count growth,
        5. operating leverage or FCF conversion visible in the same evidence window.

    downgrade to Stage2-Watch if:
        - revenue is stable but margin/revision bridge is weak,
        - delivery is labor-intensive and non-scalable,
        - public contract retention exists but OPM is falling.

    route to Stage4B if:
        - AI/security/quantum/MS/policy vocabulary causes price spike without contract-retention bridge,
        - D30 MFE is high but D90/D180 MAE exceeds roughly -25% and evidence is price-only/theme-only.

    route to Stage4C if:
        - operating loss, R&D expense, dilution, or cash-flow pressure directly breaks the monetization thesis.
```

### Why this is not a global rule repeat

The global calibrated profile already says price-only blowoff cannot become a positive stage and full 4B requires non-price evidence. This loop adds **C28-specific evidence grammar**:

```text
security words are not evidence;
security contracts are not enough;
security retention plus margin/revision bridge is evidence;
AI-security partnership without revenue bridge is 4B;
R&D-cost loss spiral after partnership theme is 4C.
```

## 8. Machine-readable rows

```jsonl
{"row_type":"price_source_validation","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_unadjusted_warning":true,"corporate_action_window_rule":"block if candidate dates overlap entry_date through D+180"}
{"row_type":"trigger","case_id":"C28_263860_GENIAN_Q3_NAC_EDR_MANAGED_SERVICE_2024_11_14","ticker":"263860","symbol_name":"지니언스","market":"KOSDAQ","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_NAC_EDR_RECURRING_MANAGED_SERVICE_MARGIN_BRIDGE","trigger_date":"2024-11-14","entry_date":"2024-11-15","entry_price":9410.0,"trigger_type":"Stage2-Actionable","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv","profile_path":"atlas/symbol_profiles/263/263860.json","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"MFE_30D_pct":16.79,"MAE_30D_pct":-8.82,"MFE_90D_pct":40.81,"MAE_90D_pct":-8.82,"MFE_180D_pct":153.99,"MAE_180D_pct":-8.82,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date_180D":"2025-07-11","peak_price_180D":23900.0,"drawdown_after_peak_pct":-23.01,"classification":"positive","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage2-Actionable|2024-11-15","dedupe_for_aggregate":true,"independent_evidence_weight":1.0,"evidence_url":"https://www.genians.co.kr/pr-room/press/20241114","evidence_summary":"2024년 3Q 영업이익 22억원, 전년동기 대비 660.8% 증가. NAC 지자체/대기업 수요 확대, Cloud NAC Managed Service 고객 확보, EDR 구독형 비즈니스 확대가 동시에 확인된 trigger."}
{"row_type":"score_simulation","case_id":"C28_263860_GENIAN_Q3_NAC_EDR_MANAGED_SERVICE_2024_11_14","ticker":"263860","trigger_date":"2024-11-14","entry_date":"2024-11-15","baseline_stage":"Stage2-Watch","current_calibrated_profile_stage":"Stage2-Watch","proposed_shadow_stage":"Stage2-Actionable","score_before_shadow":72.0,"score_after_shadow":79.0,"raw_component_score_breakdown_after_shadow":{"eps_fcf_explosion":18,"earnings_visibility":21,"bottleneck_pricing_power":8,"market_mispricing":14,"valuation_rerating":12,"capital_allocation":2,"information_confidence":14},"raw_domain_component_scores":{"contract_score":72,"backlog_visibility_score":62,"margin_bridge_score":78,"revision_score":65,"relative_strength_score":72,"customer_quality_score":76,"policy_or_regulatory_score":45,"valuation_repricing_score":61,"execution_risk_score":24,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"current_profile_error":"missed_structural_positive_if_retention_managed_service_not_weighted","stage_alignment_with_price_path":"aligned","green_lateness_ratio":null,"full_4b_window_proximity":null,"four_b_local_vs_full_window_note":"not_applicable"}
{"row_type":"residual_contribution","case_id":"C28_263860_GENIAN_Q3_NAC_EDR_MANAGED_SERVICE_2024_11_14","ticker":"263860","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_contribution_label":"positive_retention_margin_bridge","new_axis_proposed":"c28_recurring_security_contract_margin_bridge_gate","canonical_rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_new_weight_delta":false}
{"row_type":"trigger","case_id":"C28_263860_GENIAN_ANNUAL_NAC_EDR_ZERO_TRUST_2025_02_19","ticker":"263860","symbol_name":"지니언스","market":"KOSDAQ","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_NAC_EDR_ZERO_TRUST_GLOBAL_CUSTOMER_RETENTION","trigger_date":"2025-02-19","entry_date":"2025-02-20","entry_price":11110.0,"trigger_type":"Stage3-Yellow","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2025.csv","profile_path":"atlas/symbol_profiles/263/263860.json","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"MFE_30D_pct":39.06,"MAE_30D_pct":-7.38,"MFE_90D_pct":111.97,"MAE_90D_pct":-7.38,"MFE_180D_pct":170.03,"MAE_180D_pct":-7.38,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date_180D":"2025-09-22","peak_price_180D":30000.0,"drawdown_after_peak_pct":-34.3,"classification":"positive","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|263860|Stage3-Yellow|2025-02-20","dedupe_for_aggregate":true,"independent_evidence_weight":0.7,"evidence_url":"https://www.genians.co.kr/pr-room/press/20250219","evidence_summary":"2024년 연결 매출 496억원, 영업이익 98억원으로 전년 대비 각각 15.7%, 52.2% 증가. NAC·EDR·제로트러스트 3대 사업 성장과 27개국 143개 고객 확보가 확인된 annual confirmation trigger."}
{"row_type":"score_simulation","case_id":"C28_263860_GENIAN_ANNUAL_NAC_EDR_ZERO_TRUST_2025_02_19","ticker":"263860","trigger_date":"2025-02-19","entry_date":"2025-02-20","baseline_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage2-Actionable","proposed_shadow_stage":"Stage3-Yellow","score_before_shadow":76.0,"score_after_shadow":82.0,"raw_component_score_breakdown_after_shadow":{"eps_fcf_explosion":19,"earnings_visibility":23,"bottleneck_pricing_power":8,"market_mispricing":15,"valuation_rerating":12,"capital_allocation":3,"information_confidence":14},"raw_domain_component_scores":{"contract_score":78,"backlog_visibility_score":68,"margin_bridge_score":83,"revision_score":74,"relative_strength_score":80,"customer_quality_score":86,"policy_or_regulatory_score":52,"valuation_repricing_score":62,"execution_risk_score":18,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"current_profile_error":"yellow_lateness_if_global_security_customer_retention_not_recognized","stage_alignment_with_price_path":"aligned","green_lateness_ratio":null,"full_4b_window_proximity":null,"four_b_local_vs_full_window_note":"not_applicable"}
{"row_type":"residual_contribution","case_id":"C28_263860_GENIAN_ANNUAL_NAC_EDR_ZERO_TRUST_2025_02_19","ticker":"263860","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_contribution_label":"positive_yellow_retention_margin_leverage","new_axis_proposed":"c28_recurring_security_contract_margin_bridge_gate","canonical_rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_new_weight_delta":false}
{"row_type":"trigger","case_id":"C28_150900_FASOO_STABLE_RETENTION_LOW_BETA_2024_12_12","ticker":"150900","symbol_name":"파수","market":"KOSDAQ","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DATA_SECURITY_RENEWAL_STABLE_BUT_LOW_RERATING","trigger_date":"2024-12-12","entry_date":"2024-12-13","entry_price":5080.0,"trigger_type":"Stage2-Watch","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv","profile_path":"atlas/symbol_profiles/150/150900.json","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"MFE_30D_pct":6.3,"MAE_30D_pct":-8.56,"MFE_90D_pct":10.83,"MAE_90D_pct":-18.31,"MFE_180D_pct":10.83,"MAE_180D_pct":-18.31,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date_180D":"2025-04-02","peak_price_180D":5630.0,"drawdown_after_peak_pct":-26.29,"classification":"counterexample","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|150900|Stage2-Watch|2024-12-13","dedupe_for_aggregate":true,"independent_evidence_weight":1.0,"evidence_url":"https://www.fasoo.ai/financial-information","evidence_summary":"데이터 보안/문서보안의 고객 유지력과 진입장벽은 있으나, 연결 기준 2024년 매출 461억원·영업이익 39억원으로 성장/마진 레버리지가 제한적. 안정 유지보수형 보안은 retention은 맞아도 rerating trigger로는 약했다."}
{"row_type":"score_simulation","case_id":"C28_150900_FASOO_STABLE_RETENTION_LOW_BETA_2024_12_12","ticker":"150900","trigger_date":"2024-12-12","entry_date":"2024-12-13","baseline_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage2-Actionable","proposed_shadow_stage":"Stage2-Watch","score_before_shadow":70.0,"score_after_shadow":62.0,"raw_component_score_breakdown_after_shadow":{"eps_fcf_explosion":11,"earnings_visibility":19,"bottleneck_pricing_power":7,"market_mispricing":9,"valuation_rerating":8,"capital_allocation":2,"information_confidence":6},"raw_domain_component_scores":{"contract_score":63,"backlog_visibility_score":50,"margin_bridge_score":42,"revision_score":36,"relative_strength_score":38,"customer_quality_score":78,"policy_or_regulatory_score":20,"valuation_repricing_score":35,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"current_profile_error":"retention_without_growth_leverage_false_positive","stage_alignment_with_price_path":"requires_downgrade_or_guardrail","green_lateness_ratio":null,"full_4b_window_proximity":null,"four_b_local_vs_full_window_note":"not_applicable"}
{"row_type":"residual_contribution","case_id":"C28_150900_FASOO_STABLE_RETENTION_LOW_BETA_2024_12_12","ticker":"150900","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_contribution_label":"counterexample_retention_no_operating_leverage","new_axis_proposed":"c28_recurring_security_contract_margin_bridge_gate","canonical_rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_new_weight_delta":false}
{"row_type":"trigger","case_id":"C28_067920_IGLOO_PUBLIC_SECURITY_MONITORING_MARGIN_DRAG_2024_05_15","ticker":"067920","symbol_name":"이글루","market":"KOSDAQ","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"PUBLIC_SECURITY_MONITORING_CONTRACT_RETENTION_LABOR_COST_DRAG","trigger_date":"2024-05-15","entry_date":"2024-05-16","entry_price":6210.0,"trigger_type":"Stage2-Watch","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067920/2024.csv","profile_path":"atlas/symbol_profiles/067/067920.json","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"MFE_30D_pct":0.16,"MAE_30D_pct":-10.95,"MFE_90D_pct":0.16,"MAE_90D_pct":-20.69,"MFE_180D_pct":0.16,"MAE_180D_pct":-23.83,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date_180D":"2024-05-16","peak_price_180D":6220.0,"drawdown_after_peak_pct":-23.95,"classification":"counterexample","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|067920|Stage2-Watch|2024-05-16","dedupe_for_aggregate":true,"independent_evidence_weight":1.0,"evidence_url":"https://m.thebell.co.kr/m/newsview.asp?newskey=202405151413369760101175&svccode=","evidence_summary":"공공 보안관제 계약 기반은 안정적이지만 파견 인력 중심 비용 구조가 영업레버리지를 막았다. 2023년 영업이익 57억원, 전년 대비 28.6% 감소 및 OPM 5.3%로, C28의 retention만으로는 Stage2-Actionable이 부족한 사례."}
{"row_type":"score_simulation","case_id":"C28_067920_IGLOO_PUBLIC_SECURITY_MONITORING_MARGIN_DRAG_2024_05_15","ticker":"067920","trigger_date":"2024-05-15","entry_date":"2024-05-16","baseline_stage":"Stage2-Watch","current_calibrated_profile_stage":"Stage2-Watch","proposed_shadow_stage":"Stage2-Watch-Blocked","score_before_shadow":68.0,"score_after_shadow":55.0,"raw_component_score_breakdown_after_shadow":{"eps_fcf_explosion":8,"earnings_visibility":16,"bottleneck_pricing_power":5,"market_mispricing":8,"valuation_rerating":7,"capital_allocation":2,"information_confidence":9},"raw_domain_component_scores":{"contract_score":70,"backlog_visibility_score":55,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":20,"customer_quality_score":72,"policy_or_regulatory_score":45,"valuation_repricing_score":30,"execution_risk_score":44,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"current_profile_error":"labor_intensive_security_revenue_false_positive_if_contract_retention_overweighted","stage_alignment_with_price_path":"requires_downgrade_or_guardrail","green_lateness_ratio":null,"full_4b_window_proximity":null,"four_b_local_vs_full_window_note":"not_applicable"}
{"row_type":"residual_contribution","case_id":"C28_067920_IGLOO_PUBLIC_SECURITY_MONITORING_MARGIN_DRAG_2024_05_15","ticker":"067920","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_contribution_label":"counterexample_contract_retention_labor_cost_drag","new_axis_proposed":"c28_recurring_security_contract_margin_bridge_gate","canonical_rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_new_weight_delta":false}
{"row_type":"trigger","case_id":"C28_203650_DREAMSECURITY_DEEPFAKE_QUANTUM_THEME_2024_03_18","ticker":"203650","symbol_name":"드림시큐리티","market":"KOSDAQ","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBER_SECURITY_THEME_QUANTUM_DEEPFAKE_WITHOUT_RETENTION_BRIDGE","trigger_date":"2024-03-18","entry_date":"2024-03-19","entry_price":3740.0,"trigger_type":"Stage4B","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/203/203650/2024.csv","profile_path":"atlas/symbol_profiles/203/203650.json","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"MFE_30D_pct":1.6,"MAE_30D_pct":-15.78,"MFE_90D_pct":1.6,"MAE_90D_pct":-26.47,"MFE_180D_pct":4.28,"MAE_180D_pct":-38.9,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date_180D":"2024-12-11","peak_price_180D":3900.0,"drawdown_after_peak_pct":-11.79,"classification":"counterexample","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|203650|Stage4B|2024-03-19","dedupe_for_aggregate":true,"independent_evidence_weight":1.0,"evidence_url":"https://www.thebigdata.co.kr/view.php?ud=202403180447191908cd1e7f0bdf_23","evidence_summary":"딥페이크·AI해킹·총선 보안·양자암호 장비 기대가 결합된 테마성 trigger. 보안 vocabulary는 강했지만 ARR/renewal/contract retention/margin bridge가 비어 있어 C28 positive가 아니라 price-only/theme 4B로 처리해야 하는 사례."}
{"row_type":"score_simulation","case_id":"C28_203650_DREAMSECURITY_DEEPFAKE_QUANTUM_THEME_2024_03_18","ticker":"203650","trigger_date":"2024-03-18","entry_date":"2024-03-19","baseline_stage":"Stage2-Watch","current_calibrated_profile_stage":"Stage2-Watch","proposed_shadow_stage":"Stage4B","score_before_shadow":64.0,"score_after_shadow":48.0,"raw_component_score_breakdown_after_shadow":{"eps_fcf_explosion":6,"earnings_visibility":8,"bottleneck_pricing_power":4,"market_mispricing":9,"valuation_rerating":6,"capital_allocation":2,"information_confidence":13},"raw_domain_component_scores":{"contract_score":18,"backlog_visibility_score":14,"margin_bridge_score":12,"revision_score":15,"relative_strength_score":70,"customer_quality_score":35,"policy_or_regulatory_score":75,"valuation_repricing_score":50,"execution_risk_score":55,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":5,"accounting_trust_risk_score":12},"current_profile_error":"security_theme_without_contract_retention_should_not_get_positive_stage","stage_alignment_with_price_path":"requires_downgrade_or_guardrail","green_lateness_ratio":null,"full_4b_window_proximity":"local_or_full_4b","four_b_local_vs_full_window_note":"price-only/theme spike must not be counted as C28 positive"}
{"row_type":"residual_contribution","case_id":"C28_203650_DREAMSECURITY_DEEPFAKE_QUANTUM_THEME_2024_03_18","ticker":"203650","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_contribution_label":"counterexample_theme_vocabulary_price_only_4b","new_axis_proposed":"c28_recurring_security_contract_margin_bridge_gate","canonical_rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_new_weight_delta":false}
{"row_type":"trigger","case_id":"C28_042510_RAONSECURE_MOBILE_ID_FORECAST_BUT_Q1_LOSS_2024_05_23","ticker":"042510","symbol_name":"라온시큐어","market":"KOSDAQ","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DIGITAL_ID_PLATFORM_GROWTH_BUT_SEASONAL_LOSS_BRIDGE_MISSING","trigger_date":"2024-05-23","entry_date":"2024-05-24","entry_price":2410.0,"trigger_type":"Stage2-Watch","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv","profile_path":"atlas/symbol_profiles/042/042510.json","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"MFE_30D_pct":6.43,"MAE_30D_pct":-5.81,"MFE_90D_pct":7.68,"MAE_90D_pct":-29.92,"MFE_180D_pct":7.68,"MAE_180D_pct":-31.54,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date_180D":"2024-08-30","peak_price_180D":2595.0,"drawdown_after_peak_pct":-36.42,"classification":"counterexample","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|042510|Stage2-Watch|2024-05-24","dedupe_for_aggregate":true,"independent_evidence_weight":1.0,"evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=58849","evidence_summary":"모바일 신분증/디지털 ID 플랫폼 기대와 2024년 흑자전환 전망은 있었으나, entry 당시에는 1Q24 영업손실과 계절성, 플랫폼 전환의 마진 확인이 남아 있었다. 장기적으로는 2024년 흑자전환을 확인했지만, trigger 시점 Stage2-Actionable은 이른 사례."}
{"row_type":"score_simulation","case_id":"C28_042510_RAONSECURE_MOBILE_ID_FORECAST_BUT_Q1_LOSS_2024_05_23","ticker":"042510","trigger_date":"2024-05-23","entry_date":"2024-05-24","baseline_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage2-Actionable","proposed_shadow_stage":"Stage2-Watch","score_before_shadow":69.0,"score_after_shadow":58.0,"raw_component_score_breakdown_after_shadow":{"eps_fcf_explosion":9,"earnings_visibility":14,"bottleneck_pricing_power":6,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":2,"information_confidence":9},"raw_domain_component_scores":{"contract_score":55,"backlog_visibility_score":40,"margin_bridge_score":24,"revision_score":36,"relative_strength_score":52,"customer_quality_score":64,"policy_or_regulatory_score":70,"valuation_repricing_score":45,"execution_risk_score":48,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":9},"current_profile_error":"platform_growth_forecast_without_current_margin_bridge_high_mae","stage_alignment_with_price_path":"requires_downgrade_or_guardrail","green_lateness_ratio":null,"full_4b_window_proximity":null,"four_b_local_vs_full_window_note":"not_applicable"}
{"row_type":"residual_contribution","case_id":"C28_042510_RAONSECURE_MOBILE_ID_FORECAST_BUT_Q1_LOSS_2024_05_23","ticker":"042510","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_contribution_label":"counterexample_platform_forecast_without_margin_confirmation","new_axis_proposed":"c28_recurring_security_contract_margin_bridge_gate","canonical_rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_new_weight_delta":false}
{"row_type":"trigger","case_id":"C28_042510_RAONSECURE_MOBILE_ID_PRICE_SURGE_Q1_LOSS_2024_07_02","ticker":"042510","symbol_name":"라온시큐어","market":"KOSDAQ","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DIGITAL_ID_THEME_PRICE_SURGE_WITH_HIGH_MAE","trigger_date":"2024-07-02","entry_date":"2024-07-03","entry_price":2300.0,"trigger_type":"Stage4B","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv","profile_path":"atlas/symbol_profiles/042/042510.json","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"MFE_30D_pct":10.87,"MAE_30D_pct":-26.57,"MFE_90D_pct":12.83,"MAE_90D_pct":-27.04,"MFE_180D_pct":12.83,"MAE_180D_pct":-28.26,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date_180D":"2024-08-30","peak_price_180D":2595.0,"drawdown_after_peak_pct":-36.42,"classification":"counterexample","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|042510|Stage4B|2024-07-03","dedupe_for_aggregate":true,"independent_evidence_weight":0.6,"evidence_url":"https://www.thebigdata.co.kr/view.php?ud=202407020552169831cd1e7f0bdf_23","evidence_summary":"모바일 신분증 기대가 재점화되었지만 1Q24 손실과 4Q 편중 구조가 남아 있었다. 가격경로는 90D/180D MAE가 -27%~-28%로, C28 positive보다 local 4B/high-MAE guard 대상이었다."}
{"row_type":"score_simulation","case_id":"C28_042510_RAONSECURE_MOBILE_ID_PRICE_SURGE_Q1_LOSS_2024_07_02","ticker":"042510","trigger_date":"2024-07-02","entry_date":"2024-07-03","baseline_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage2-Watch","proposed_shadow_stage":"Stage4B","score_before_shadow":67.0,"score_after_shadow":52.0,"raw_component_score_breakdown_after_shadow":{"eps_fcf_explosion":7,"earnings_visibility":10,"bottleneck_pricing_power":5,"market_mispricing":11,"valuation_rerating":8,"capital_allocation":2,"information_confidence":9},"raw_domain_component_scores":{"contract_score":40,"backlog_visibility_score":34,"margin_bridge_score":18,"revision_score":30,"relative_strength_score":68,"customer_quality_score":58,"policy_or_regulatory_score":78,"valuation_repricing_score":46,"execution_risk_score":58,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":9},"current_profile_error":"high_mae_guard_needed_for_policy_platform_theme","stage_alignment_with_price_path":"requires_downgrade_or_guardrail","green_lateness_ratio":null,"full_4b_window_proximity":"local_or_full_4b","four_b_local_vs_full_window_note":"price-only/theme spike must not be counted as C28 positive"}
{"row_type":"residual_contribution","case_id":"C28_042510_RAONSECURE_MOBILE_ID_PRICE_SURGE_Q1_LOSS_2024_07_02","ticker":"042510","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_contribution_label":"counterexample_local_4b_high_mae","new_axis_proposed":"c28_recurring_security_contract_margin_bridge_gate","canonical_rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_new_weight_delta":false}
{"row_type":"trigger","case_id":"C28_411080_SANDSLAB_MS_AI_SECURITY_COLLAB_PRICE_BLOWOFF_2024_03_26","ticker":"411080","symbol_name":"샌즈랩","market":"KOSDAQ","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_SECURITY_PARTNERSHIP_BLOWOFF_WITHOUT_REVENUE_BRIDGE","trigger_date":"2024-03-26","entry_date":"2024-03-27","entry_price":11260.0,"trigger_type":"Stage4B","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/411/411080/2024.csv","profile_path":"atlas/symbol_profiles/411/411080.json","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"MFE_30D_pct":48.22,"MAE_30D_pct":-17.23,"MFE_90D_pct":48.22,"MAE_90D_pct":-53.64,"MFE_180D_pct":48.22,"MAE_180D_pct":-53.64,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date_180D":"2024-04-16","peak_price_180D":16690.0,"drawdown_after_peak_pct":-68.72,"classification":"counterexample","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|411080|Stage4B|2024-03-27","dedupe_for_aggregate":true,"independent_evidence_weight":1.0,"evidence_url":"https://www.etnews.com/20240326000085","evidence_summary":"한국MS와 AI 기반 사이버보안 기술 협업 소식으로 주가가 상한가를 기록한 trigger. partnership headline은 강했지만 ARR/RPO/retention/renewal/margin bridge가 없어 C28 positive보다 price-only local 4B 스트레스 케이스로 분류."}
{"row_type":"score_simulation","case_id":"C28_411080_SANDSLAB_MS_AI_SECURITY_COLLAB_PRICE_BLOWOFF_2024_03_26","ticker":"411080","trigger_date":"2024-03-26","entry_date":"2024-03-27","baseline_stage":"Stage2-Actionable","current_calibrated_profile_stage":"Stage2-Watch","proposed_shadow_stage":"Stage4B","score_before_shadow":71.0,"score_after_shadow":49.0,"raw_component_score_breakdown_after_shadow":{"eps_fcf_explosion":5,"earnings_visibility":8,"bottleneck_pricing_power":6,"market_mispricing":12,"valuation_rerating":8,"capital_allocation":1,"information_confidence":9},"raw_domain_component_scores":{"contract_score":20,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":12,"relative_strength_score":95,"customer_quality_score":45,"policy_or_regulatory_score":50,"valuation_repricing_score":68,"execution_risk_score":72,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":12,"accounting_trust_risk_score":15},"current_profile_error":"ai_security_partnership_without_contract_retention_should_be_4b_not_stage2","stage_alignment_with_price_path":"requires_downgrade_or_guardrail","green_lateness_ratio":null,"full_4b_window_proximity":"local_or_full_4b","four_b_local_vs_full_window_note":"price-only/theme spike must not be counted as C28 positive"}
{"row_type":"residual_contribution","case_id":"C28_411080_SANDSLAB_MS_AI_SECURITY_COLLAB_PRICE_BLOWOFF_2024_03_26","ticker":"411080","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_contribution_label":"counterexample_partnership_headline_price_blowoff","new_axis_proposed":"c28_recurring_security_contract_margin_bridge_gate","canonical_rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_new_weight_delta":false}
{"row_type":"trigger","case_id":"C28_411080_SANDSLAB_GOV_PROJECT_RND_COST_THESIS_BREAK_2024_05_03","ticker":"411080","symbol_name":"샌즈랩","market":"KOSDAQ","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_SECURITY_RND_COST_AND_OPERATING_LOSS_THESIS_BREAK","trigger_date":"2024-05-03","entry_date":"2024-05-07","entry_price":12080.0,"trigger_type":"Stage4C","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/411/411080/2024.csv","profile_path":"atlas/symbol_profiles/411/411080.json","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"MFE_30D_pct":2.81,"MAE_30D_pct":-24.01,"MFE_90D_pct":2.81,"MAE_90D_pct":-56.79,"MFE_180D_pct":4.14,"MAE_180D_pct":-56.79,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"peak_date_180D":"2024-09-25","peak_price_180D":12580.0,"drawdown_after_peak_pct":-54.77,"classification":"counterexample","dedupe_key":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|411080|Stage4C|2024-05-07","dedupe_for_aggregate":true,"independent_evidence_weight":0.7,"evidence_url":"https://www.ibtomato.com/ExternalView.aspx?no=13146&type=1","evidence_summary":"AI 보안 국책과제/협업 narrative가 이어졌지만, 이후 상반기 영업손실 확대와 높은 R&D 비용 부담이 확인되며 revenue retention보다 비용 흡수 리스크가 지배했다. 180D MAE -56.79%로 hard 4C thesis-break guard가 필요했다."}
{"row_type":"score_simulation","case_id":"C28_411080_SANDSLAB_GOV_PROJECT_RND_COST_THESIS_BREAK_2024_05_03","ticker":"411080","trigger_date":"2024-05-03","entry_date":"2024-05-07","baseline_stage":"Stage2-Watch","current_calibrated_profile_stage":"Stage2-Watch","proposed_shadow_stage":"Stage4C","score_before_shadow":66.0,"score_after_shadow":42.0,"raw_component_score_breakdown_after_shadow":{"eps_fcf_explosion":3,"earnings_visibility":5,"bottleneck_pricing_power":5,"market_mispricing":9,"valuation_rerating":6,"capital_allocation":1,"information_confidence":13},"raw_domain_component_scores":{"contract_score":18,"backlog_visibility_score":10,"margin_bridge_score":5,"revision_score":8,"relative_strength_score":60,"customer_quality_score":38,"policy_or_regulatory_score":60,"valuation_repricing_score":58,"execution_risk_score":84,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":18,"accounting_trust_risk_score":20},"current_profile_error":"late_4c_if_rnd_cost_operating_loss_not_connected_to_thesis_break","stage_alignment_with_price_path":"requires_downgrade_or_guardrail","green_lateness_ratio":null,"full_4b_window_proximity":"local_or_full_4b","four_b_local_vs_full_window_note":"price-only/theme spike must not be counted as C28 positive"}
{"row_type":"residual_contribution","case_id":"C28_411080_SANDSLAB_GOV_PROJECT_RND_COST_THESIS_BREAK_2024_05_03","ticker":"411080","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_contribution_label":"hard_4c_operating_loss_rnd_cost_thesis_break","new_axis_proposed":"c28_recurring_security_contract_margin_bridge_gate","canonical_rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_new_weight_delta":false}
{"row_type":"aggregate","selected_round":"R8","selected_loop":133,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":6,"calibration_usable_trigger_count":9,"representative_trigger_count":9,"positive_case_count":2,"counterexample_count":7,"stage4b_case_count":3,"stage4c_case_count":1,"current_profile_error_count":7,"coverage_before":"C28 rows 28","coverage_after_if_accepted":"C28 rows 37","next_recommended_archetypes":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|C19_BRAND_RETAIL_INVENTORY_MARGIN"}
{"row_type":"shadow_weight","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","rule_candidate":"C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1","shadow_weight_only":true,"production_scoring_changed":false,"proposed_behavior":"Increase C28 Stage2/Yellow confidence only when renewal/retention/managed-service/ARR evidence is tied to margin or revision bridge; downgrade pure cybersecurity theme, partnership, public project, or AI/security vocabulary without contract-retention proof to Stage2-Watch/4B/4C depending on price path and loss evidence.","do_not_auto_apply_weight_delta":true}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent for Songdaiki/stock_agent. Do not treat this Markdown as an already-applied scoring change. Ingest it as a v12 residual research artifact only.

Task:
1. Parse every jsonl row in section "Machine-readable rows".
2. Validate required v12 fields:
   - large_sector_id
   - canonical_archetype_id
   - trigger_type
   - entry_date
   - entry_price
   - MFE_30D_pct / MAE_30D_pct
   - MFE_90D_pct / MAE_90D_pct
   - MFE_180D_pct / MAE_180D_pct
   - price_data_source = Songdaiki/stock-web
   - price_basis = tradable_raw
   - price_adjustment_status = raw_unadjusted_marcap
3. Deduplicate by canonical_archetype_id + ticker + trigger_type + entry_date.
4. Do not apply production scoring automatically.
5. Treat proposed rule C28_RETENTION_CONTRACT_MARGIN_BRIDGE_AND_THEME_BLOWOFF_GATE_V1 as shadow_weight_only.
6. Add valid rows to v12 calibration candidate pool only if corporate_action_window_status is clean_180D_window.
7. Compare the rule candidate against existing C28 rows and especially top-covered symbols:
   012510, 030520, 042510, 047560, 263860, 018260.
8. Reject this artifact if filename, metadata round, or canonical archetype do not match:
   filename round = R8
   metadata round = R8
   large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
   canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

## 10. Next research state

```text
completed_round = R8
completed_loop = 133
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|C19_BRAND_RETAIL_INVENTORY_MARGIN
```
