# E2R v12 residual research — R5 loop 113 — C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R5
selected_loop = 113
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_LEGACY_BRAND_LABEL_FALSE_POSITIVE
output_format = one_standalone_markdown_file
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Scope guard

이번 작업은 코딩 작업도 아니고, `stock_agent` 레포 반영 작업도 아니고, 현재 live 후보 탐색도 아니다.
산출물은 나중에 coding agent가 batch 반영할 수 있는 독립 실행형 historical calibration Markdown이다.

이번 MD는 다음을 하지 않는다.

```text
- 현재 종목 추천
- live watchlist 생성
- 2026년 현재 Stage3 후보 스캔
- 자동매매
- 증권사 API 연결
- stock_agent src/e2r 코드 확인
- stock_agent 코드 패치 작성
- production scoring 즉시 변경
```

## 2. Coverage / no-repeat basis

`V12_Research_No_Repeat_Index.md` 기준 C20은 Priority 1 보강 대상이다.

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rows = 33
need_to_50 = 17
조사 포인트 = K-food/K-beauty 글로벌 유통, sell-through, OPM/revision
```

이번 case set은 기존 C20에서 이미 사용한 다음 조합을 피했다.

```text
실리콘투 / 코스맥스 / 아모레퍼시픽
브이티 / 한국콜마 / 클리오
코스메카코리아 / 씨앤씨인터내셔널 / 아이패밀리에스씨
```

신규 case set은 다음과 같다.

```text
950140 잉글우드랩
214420 토니모리
018250 애경산업
051900 LG생활건강
```

## 3. Price source

가격 row는 `Songdaiki/stock-web`의 calibration shard를 사용했다.

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis = tradable_raw
```

Corporate-action-contaminated window는 기본적으로 calibration에서 block해야 한다.
이번 네 케이스의 2025-06-05 이후 window는 각 profile상 직접적인 corporate-action block이 없다.

## 4. External trigger spine

공통 trigger는 **2025-06-05 Reuters K-beauty U.S. demand / ecommerce / offline retail expansion 기사**다.

핵심 해석은 다음이다.

```text
K-beauty category demand = positive context
U.S. ecommerce / Sephora / Ulta / Target / Costco retail-channel entry = channel expansion context
contract manufacturer scalable production model = ODM/OPM leverage context
그러나 category headline만으로 개별 상장사의 revenue / margin / revision이 확정되는 것은 아니다.
```

따라서 C20에서는 다음 다리를 확인해야 한다.

```text
sell-through → reorder → inventory normalization → ODM utilization or brand revenue → OPM/revision
```

## 5. Case table

| case | symbol | entry | peak | MFE | MAE | classification |
|---|---:|---:|---:|---:|---:|---|
| 잉글우드랩 | 950140 | 2025-06-05 close 10,650 | 2025-11-07 high 16,910 | +58.78% | -3.94% | positive_with_full_4B_watch |
| 토니모리 | 214420 | 2025-06-05 close 9,390 | 2025-06-20 high 13,610 | +44.94% | -21.83% | positive_high_MAE_brand_channel_4B_watch |
| 애경산업 | 018250 | 2025-06-05 close 15,140 | 2025-07-14 high 19,230 | +27.01% | -19.09% | boundary_false_positive_high_MAE_watch |
| LG생활건강 | 051900 | 2025-06-05 close 340,500 | 2025-06-20 high 355,500 | +4.41% | -25.55% | hard_counterexample_legacy_large_cap_kbeauty_label |

## 6. Case notes

### 6.1 잉글우드랩 — ODM / U.S. manufacturing exposure positive, but full-window 4B watch

```text
symbol = 950140
entry_date = 2025-06-05
entry_price = 10,650
peak_date = 2025-11-07
peak_high = 16,910
MFE = +58.78%
MAE low = 10,230 on 2026-01-19
MAE = -3.94%
```

잉글우드랩은 2025년 K-beauty U.S. demand와 contract-manufacturing scalability narrative에 가장 잘 맞는 가격경로를 보였다.
다만 peak가 2025-11-07로 trigger 후 상당히 늦고, firm-specific customer/order/utilization source는 이번 실행에서 충분히 repair하지 못했으므로 Stage3-Green 확정이 아니라 `positive_with_full_4B_watch`로 둔다.

Residual lesson:

```text
ODM/manufacturing exposure는 C20에서 brand-label보다 더 좋은 bridge가 될 수 있다.
하지만 U.S. customer mix, order backlog, utilization, gross margin revision이 확인되어야 Stage3-Green.
```

### 6.2 토니모리 — global brand/channel positive, but high-MAE 4B watch

```text
symbol = 214420
entry_date = 2025-06-05
entry_price = 9,390
peak_date = 2025-06-20
peak_high = 13,610
MFE = +44.94%
MAE low = 7,340 on 2025-11-27
MAE = -21.83%
```

토니모리는 global K-beauty brand/channel 레이블에 강하게 반응했다.
하지만 후행 MAE가 -20%를 넘었으므로, 단순 “해외 매장/글로벌 브랜드” 레이블을 Stage3-Green으로 승격하면 잔여 오류가 생긴다.

Residual lesson:

```text
Brand awareness ≠ sell-through.
해외 채널 존재 ≠ repeat reorder.
C20은 viral/channel headline에서 company-specific reorder/margin bridge를 요구해야 한다.
```

### 6.3 애경산업 — brand-channel boundary false positive / high-MAE watch

```text
symbol = 018250
entry_date = 2025-06-05
entry_price = 15,140
peak_date = 2025-07-14
peak_high = 19,230
MFE = +27.01%
MAE low = 12,250 on 2026-01-09
MAE = -19.09%
```

애경산업은 단기 MFE가 있었지만 drawdown도 컸다.
즉 brand/channel label은 C20에 들어갈 수는 있지만, Stage2-Actionable 이상으로 올리려면 firm-specific overseas sales, retailer sell-through, inventory and margin evidence가 필요하다.

Residual lesson:

```text
C20에서 “브랜드 보유”는 입구일 뿐이다.
sell-through / reorder / OPM revision 없이 부여된 점수는 4B watch로 낮춰야 한다.
```

### 6.4 LG생활건강 — legacy large-cap K-beauty label hard counterexample

```text
symbol = 051900
entry_date = 2025-06-05
entry_price = 340,500
peak_date = 2025-06-20
peak_high = 355,500
MFE = +4.41%
MAE low = 253,500 on 2026-02-02
MAE = -25.55%
```

LG생활건강은 대형 화장품 포트폴리오와 글로벌 브랜드 assets를 갖고 있어도 Reuters의 K-beauty category headline을 그대로 equity alpha로 번역하지 못한 케이스다.
legacy brand mix, China exposure, margin/revision drag가 해결되지 않으면 K-beauty category demand가 개별 주가로 전달되지 않는다.

Residual lesson:

```text
대형 legacy cosmetic company는 K-beauty category winner가 아닐 수 있다.
C20은 category export growth와 company-specific growth를 분리해야 한다.
```

## 7. Residual diagnosis

현재 profile이 여전히 틀릴 수 있는 지점은 다음이다.

```text
1. K-beauty global distribution headline을 너무 넓게 Stage2/Stage3로 번역한다.
2. 브랜드 인지도, 해외 매장, category export growth를 company-level reorder로 오인한다.
3. ODM/manufacturing bridge와 legacy-brand label을 같은 강도로 본다.
4. short squeeze / theme blowoff / viral spike를 sell-through 증거로 오인한다.
5. China drag, inventory, gross margin, OPM/revision 확인이 없으면 peak 이후 MAE가 커진다.
```

## 8. Shadow rule candidate

```text
rule_id = c20_company_specific_sellthrough_reorder_opm_revision_bridge_required_v3
scope = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION

IF K-beauty / global distribution / U.S. retail / ecommerce headline exists
AND company-specific evidence confirms at least one of:
  - retailer sell-through
  - repeat reorder
  - inventory normalization
  - ODM order/utilization
  - gross margin or OPM revision
  - export sales acceleration traceable to the listed company
THEN allow Stage2-Actionable or Stage3-Yellow consideration.

IF evidence is only:
  - category export headline
  - global brand awareness
  - overseas store/channel existence
  - social-media virality
  - legacy large-cap cosmetic exposure
THEN cap at Stage2 / 4B watch.

IF price-only MFE is high but MAE later exceeds ~18–20%
AND no firm-specific margin/reorder bridge appears
THEN mark as high-MAE 4B or 4C-prone counterexample.
```

This is shadow-only. Production scoring is not changed in this run.

## 9. Machine-readable rows

### 9.1 case_rows

```jsonl
{"row_type":"case","no_repeat_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|950140|K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05|2025-06-05","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_LEGACY_BRAND_LABEL_FALSE_POSITIVE","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","symbol":"950140","name":"잉글우드랩","trigger_date":"2025-06-05","entry_date":"2025-06-05","entry_price":10650,"peak_date":"2025-11-07","peak_high":16910,"mfe_pct":58.78,"mae_date":"2026-01-19","mae_low":10230,"mae_pct":-3.94,"classification":"positive_with_full_4B_watch","source_repair_needed":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","no_repeat_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|214420|K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05|2025-06-05","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_LEGACY_BRAND_LABEL_FALSE_POSITIVE","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","symbol":"214420","name":"토니모리","trigger_date":"2025-06-05","entry_date":"2025-06-05","entry_price":9390,"peak_date":"2025-06-20","peak_high":13610,"mfe_pct":44.94,"mae_date":"2025-11-27","mae_low":7340,"mae_pct":-21.83,"classification":"positive_high_MAE_brand_channel_4B_watch","source_repair_needed":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","no_repeat_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|018250|K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05|2025-06-05","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_LEGACY_BRAND_LABEL_FALSE_POSITIVE","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","symbol":"018250","name":"애경산업","trigger_date":"2025-06-05","entry_date":"2025-06-05","entry_price":15140,"peak_date":"2025-07-14","peak_high":19230,"mfe_pct":27.01,"mae_date":"2026-01-09","mae_low":12250,"mae_pct":-19.09,"classification":"boundary_false_positive_high_MAE_watch","source_repair_needed":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","no_repeat_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|051900|K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05|2025-06-05","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_LEGACY_BRAND_LABEL_FALSE_POSITIVE","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","symbol":"051900","name":"LG생활건강","trigger_date":"2025-06-05","entry_date":"2025-06-05","entry_price":340500,"peak_date":"2025-06-20","peak_high":355500,"mfe_pct":4.41,"mae_date":"2026-02-02","mae_low":253500,"mae_pct":-25.55,"classification":"hard_counterexample_legacy_large_cap_kbeauty_label","source_repair_needed":false,"production_scoring_changed":false,"shadow_weight_only":true}
```

### 9.2 trigger_rows

```jsonl
{"row_type":"trigger","trigger_id":"K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05","symbol":"950140","name":"잉글우드랩","trigger_date":"2025-06-05","trigger_evidence_type":"global_distribution_sellthrough_reorder_margin_bridge","entry_price_basis":"trigger_date_close_from_stock_web_tradable_raw","no_repeat_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|950140|K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05|2025-06-05"}
{"row_type":"trigger","trigger_id":"K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05","symbol":"214420","name":"토니모리","trigger_date":"2025-06-05","trigger_evidence_type":"global_distribution_sellthrough_reorder_margin_bridge","entry_price_basis":"trigger_date_close_from_stock_web_tradable_raw","no_repeat_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|214420|K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05|2025-06-05"}
{"row_type":"trigger","trigger_id":"K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05","symbol":"018250","name":"애경산업","trigger_date":"2025-06-05","trigger_evidence_type":"global_distribution_sellthrough_reorder_margin_bridge","entry_price_basis":"trigger_date_close_from_stock_web_tradable_raw","no_repeat_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|018250|K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05|2025-06-05"}
{"row_type":"trigger","trigger_id":"K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05","symbol":"051900","name":"LG생활건강","trigger_date":"2025-06-05","trigger_evidence_type":"global_distribution_sellthrough_reorder_margin_bridge","entry_price_basis":"trigger_date_close_from_stock_web_tradable_raw","no_repeat_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|051900|K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05|2025-06-05"}
```

### 9.3 score_simulation_rows

```jsonl
{"row_type":"score_simulation","symbol":"950140","name":"잉글우드랩","current_profile_expected_error":true,"old_profile_likely_stage":"Stage2_or_Stage3_by_K-beauty/global_distribution_label","proposed_shadow_stage":"Stage2_Actionable_or_Stage3_Yellow_only_if_sellthrough_reorder_opm_revision_confirmed","reason":"미국 수요/이커머스/오프라인 리테일 확장 국면에서 미국 ODM·manufacturing 노출이 강한 가격경로로 반응한 케이스. 다만 peak가 늦고 2025-11-07 blowoff 성격이 있어 full 4B watch."}
{"row_type":"score_simulation","symbol":"214420","name":"토니모리","current_profile_expected_error":true,"old_profile_likely_stage":"Stage2_or_Stage3_by_K-beauty/global_distribution_label","proposed_shadow_stage":"Stage2_Actionable_or_Stage3_Yellow_only_if_sellthrough_reorder_opm_revision_confirmed","reason":"글로벌 브랜드/해외 채널 레이블이 강한 단기 MFE로 번역됐지만 후행 MAE가 커서 sell-through·reorder·OPM revision 없이 Stage3-Green 금지."}
{"row_type":"score_simulation","symbol":"018250","name":"애경산업","current_profile_expected_error":true,"old_profile_likely_stage":"Stage2_or_Stage3_by_K-beauty/global_distribution_label","proposed_shadow_stage":"Stage2_Actionable_or_Stage3_Yellow_only_if_sellthrough_reorder_opm_revision_confirmed","reason":"브랜드/채널 레이블은 단기 MFE를 만들었지만 후행 손실이 커서 C20에서 회사별 해외 sell-through와 수익성 전환 확인이 필요함을 보여주는 경계선 반례."}
{"row_type":"score_simulation","symbol":"051900","name":"LG생활건강","current_profile_expected_error":true,"old_profile_likely_stage":"Stage2_or_Stage3_by_K-beauty/global_distribution_label","proposed_shadow_stage":"4B_watch_or_4C_if_no_company_specific_bridge","reason":"K-beauty 글로벌 수요 headline과 대형 화장품 포트폴리오가 있어도 legacy brand mix, China drag, margin/revision 미확인 상태에서는 equity path가 약할 수 있음을 보여주는 hard counterexample."}
```

### 9.4 aggregate_rows

```jsonl
{"row_type":"aggregate","round":"R5","loop":113,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","new_independent_case_count":4,"reused_case_count":0,"positive_case_count":2,"boundary_false_positive_count":1,"counterexample_count":2,"verified_url_repair_needed_count":2,"full_window_blocked_count":0,"current_profile_error_count":4,"coverage_gap_before":"rows 33, need_to_50 17"}
```

### 9.5 shadow_weight_rows

```jsonl
{"row_type":"shadow_weight","rule_id":"c20_company_specific_sellthrough_reorder_opm_revision_bridge_required_v3","scope":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","proposal":"K-beauty/global distribution headline alone remains at Stage2/4B watch; add Stage2-Actionable/Stage3 only when company-specific sell-through, reorder, inventory normalization, ODM utilization, or OPM/revision bridge is present.","positive_signal":["confirmed U.S./global retailer sell-through","repeat reorder","ODM order/utilization data","gross margin/OPM revision","inventory normalization"],"negative_signal":["legacy brand label only","category export headline only","China decline offset not resolved","single social-media spike without reorder evidence","high-MAE post-spike path"],"production_scoring_changed":false,"shadow_weight_only":true}
```

### 9.6 residual_contribution_rows

```jsonl
{"row_type":"residual_contribution","contribution_label":"canonical_archetype_rule_candidate","new_axis":"c20_kbeauty_us_retail_sellthrough_to_company_margin_bridge","existing_axis_strengthened":"full_4b_requires_non_price_evidence for C20 K-beauty/global-brand/ODM rallies","existing_axis_weakened":null}
```

### 9.7 narrative_only_rows

```jsonl
{"row_type":"narrative_only","note":"Reuters 2025-06-05 is a category-level trigger. It supports K-beauty demand/retail-channel context, not automatic company-level revenue or margin conversion."}
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research session.

```text
You are a coding agent operating on Songdaiki/stock_agent.

Input artifact:
e2r_stock_web_v12_residual_round_R5_loop_113_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md

Task:
Batch-ingest this artifact together with other v12 residual research MDs.
Do not treat this single MD as sufficient to patch production scoring.
Extract the JSONL rows under case_rows, trigger_rows, score_simulation_rows, aggregate_rows, shadow_weight_rows, residual_contribution_rows, and narrative_only_rows.
Append or merge them into the research calibration registry according to the project’s existing artifact schema.

Important constraints:
- Do not run live scans.
- Do not create current stock recommendations.
- Do not connect brokerage APIs.
- Do not change production scoring from this MD alone.
- Treat proposed rule c20_company_specific_sellthrough_reorder_opm_revision_bridge_required_v3 as shadow-only until batch evidence supports it.
- Preserve no_repeat_key uniqueness:
  C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|symbol|K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_REUTERS_2025_06_05|entry_date
```

## 11. Final state summary

```text
selected_round = R5
selected_loop = 113
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id = K_BEAUTY_US_ECOMMERCE_OFFLINE_RETAIL_ODM_BRAND_SELLTHROUGH_BRIDGE_VS_LEGACY_BRAND_LABEL_FALSE_POSITIVE

new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 2
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 2
boundary_false_positive_count = 1
counterexample_count = 2
current_profile_error_count = 4
verified_url_repair_needed_count = 2

do_not_propose_new_weight_delta = false
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate

new_axis_proposed = c20_kbeauty_us_retail_sellthrough_to_company_margin_bridge
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C20 K-beauty/global-brand/ODM rallies
existing_axis_weakened = null

next_recommended_archetypes = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C22_INSURANCE_RATE_CYCLE_RESERVE
```
