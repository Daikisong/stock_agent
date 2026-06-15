# E2R v12 Residual Research — R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / loop 172

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 1. Selection metadata

```text
selected_round = R11
selected_loop = 172
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/thin-P2 clearing
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = mixed_c31_policy_implementation_budget_commercial_bridge_leaf_set
loop_objective = URL-backed_quality_repair|policy_event_false_positive_mining|4B_exit_guard|legal_reversal_timing_test|canonical_archetype_compression
```

### Why C31 now

The original No-Repeat Index shows C31 at 118 representative rows, already above the 50-row minimum, so this is not a raw coverage pass. After loops 121-171 cleared the thin P0/P1 axes and then touched several P2 quality-repair groups, C31 remained the largest unreviewed policy-event axis in this session. The value here is not another policy headline sample; it is separating **binding policy with budget/implementation/commercial conversion** from **policy vocabulary that creates a temporary theme wick and then decays**.

## 2. Stock-Web price basis

```text
primary_price_source = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
entry_price_rule = close of entry_date in stock-web tradable shard
MFE_N_pct = (max high from entry_date through D+N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through D+N tradable rows / entry_price - 1) * 100
```

All eight trigger rows have 30D/90D/180D MFE and MAE. No row has a corporate-action candidate inside the entry~D+180 window. Corporate-action notes are preserved in each JSONL row.

## 3. Thesis compressed

C31 should not be a “government said something” bucket. It should behave like a fuse box: the policy headline is only the switch. Current must still pass through **law/budget/implementation → company direct exposure → revenue/profit conversion → price-path timing**. If any wire is missing, Stage2-Actionable should not light up.

이번 pass에서 보인 구조는 세 갈래다.

1. **Policy + immediate profit bridge works**: KEPCO tariff hikes were reflected in sales/profit and the price path had strong MFE with almost no MAE.
2. **Policy + direct industry exposure still needs exit guard**: YBMNet and Satrec had credible policy exposure, but their later drawdowns show why C31 needs a local 4B/high-MAE guard.
3. **Policy vocabulary alone fails**: AI textbook vendors, telemedicine vendors, space proxies, and medical-quota education names can spike, but without procurement/call-off/reimbursement/earnings bridge they often become false Stage2 rows.

## 4. Evidence map

| policy family | direct policy evidence | company bridge source | C31 interpretation |
|---|---|---|---|
| AI digital textbook | Ministry of Education announced AI digital textbook plan on 2023-06-08 and 2025 rollout scope | i-Scream AI textbook page / YBM AI digital education materials | legal/implementation exists, but procurement/revenue conversion and reversal risk must be checked |
| Telemedicine | Reuters reported full temporary allowance at all hospitals/clinics on 2024-02-23 | Bit Computer telemedicine/HIS profile / Ubcare EMR platform network | emergency deregulation is not the same as reimbursed recurring revenue |
| Space agency / KASA | Reuters reported KASA launch and long-term space investment plan on 2024-05-30 | Satrec satellite systems / MSIT space-agency policy | direct satellite systems exposure can work, but pure policy beta needs 4B guard |
| Electricity tariff | Yonhap reported KEPCO Q3 profit and rate-hike contribution | KEPCO official newsroom | tariff policy had immediate sales/profit bridge |
| Medical school quota | medical-school quota expansion and court/policy conflict | MegaMD education beta | student quota headline is not a durable listed-company earnings bridge |

## 5. Trigger summary table

| case | ticker | name | trigger | entry | entry_px | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | label |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C31_R11_L172_01 | 289010 | 아이스크림에듀 | Stage2-Watch | 2023-06-09 | 5050 | 17.23 | -13.86 | 17.23 | -25.94 | 17.23 | -31.68 | counterexample |
| C31_R11_L172_02 | 057030 | YBM넷 | Stage2-Watch | 2023-06-09 | 4765 | 11.44 | -21.51 | 11.44 | -30.95 | 31.37 | -30.95 | positive_with_4B_exit_guard |
| C31_R11_L172_03 | 032850 | 비트컴퓨터 | Stage2-Watch | 2024-02-26 | 7730 | 10.09 | -24.32 | 10.09 | -28.2 | 10.09 | -41.14 | counterexample |
| C31_R11_L172_04 | 032620 | 유비케어 | Stage2-Watch | 2024-02-26 | 6490 | 9.86 | -27.27 | 9.86 | -29.12 | 9.86 | -48.92 | counterexample |
| C31_R11_L172_05 | 211270 | AP위성 | Stage2-Watch | 2024-05-31 | 16470 | 17.49 | -17.43 | 17.49 | -41.71 | 17.49 | -41.71 | counterexample |
| C31_R11_L172_06 | 099320 | 쎄트렉아이 | Stage2-Actionable | 2024-05-31 | 47700 | 22.64 | -2.52 | 22.64 | -33.75 | 22.64 | -33.75 | positive_with_4B_exit_guard |
| C31_R11_L172_07 | 015760 | 한국전력 | Stage2-Actionable | 2023-11-14 | 17400 | 13.51 | -0.4 | 46.26 | -0.4 | 46.26 | -0.4 | positive |
| C31_R11_L172_08 | 133750 | 메가엠디 | Stage2-Watch | 2024-02-07 | 2850 | 24.74 | -6.32 | 24.74 | -22.63 | 24.74 | -42.21 | counterexample |


## 6. Case notes

### C31_R11_L172_01 — 아이스크림에듀 / AI textbook policy / counterexample

The Ministry of Education policy was real, and i-Scream had direct AI textbook product exposure. But the price path says the market paid for the policy switch before the procurement and monetization wires were visible. MFE_30D was +17.23%, but 180D MAE reached -31.68%. This should remain Stage2-Watch unless textbook approval, school adoption, paid seat count, or margin bridge is visible.

### C31_R11_L172_02 — YBM넷 / AI textbook policy / positive with 4B exit guard

YBM had direct digital/e-learning and AI material exposure. It produced a delayed MFE_180D of +31.37%, but the same row carried MAE_90D of -30.95%. This is not clean Green material. It is useful as a policy-implementation positive only when paired with local 4B/high-MAE exit logic.

### C31_R11_L172_03 — 비트컴퓨터 / telemedicine emergency deregulation / counterexample

Telemedicine was fully allowed during the medical crisis, and Bit Computer had telemedicine/HIS exposure. Yet the event was emergency operational permission, not a stable reimbursement law or recurring revenue contract. Entry-date MFE never exceeded +10.09% while MAE_180D reached -41.14%. C31 should block policy-only telemedicine Stage2-Actionable rows.

### C31_R11_L172_04 — 유비케어 / telemedicine and EMR platform / counterexample

Ubcare had a real EMR platform and medical network. But the 2024 telemedicine policy did not immediately translate into reimbursed remote-care revenue. The stock peaked near entry and then drew down to MAE_180D -48.92%. This is a clean residual false-positive sample.

### C31_R11_L172_05 — AP위성 / KASA policy beta / counterexample

KASA was an institutional policy event, but AP Satellite’s path shows the danger of buying the policy noun. The entry day was effectively the peak, MFE_180D stayed at +17.49%, and MAE_180D fell to -41.71%. Without signed program orders or revenue timing, this is Stage2-Watch / local 4B only.

### C31_R11_L172_06 — 쎄트렉아이 / KASA + satellite systems / positive with 4B exit guard

Satrec had cleaner direct exposure to satellite systems, ground systems, imagery services, and geospatial analytics. KASA created a plausible demand umbrella, and the row reached MFE_90D/MFE_180D +22.64%. But MAE_180D was -33.75%, so the correct patch is not “policy = Green”; it is “direct exposure can be Stage2-Actionable, but exit guard remains mandatory.”

### C31_R11_L172_07 — 한국전력 / electricity tariff to profit / positive

This is the cleanest C31 positive in the batch. The policy mechanism was tariff hikes, and Yonhap explicitly linked KEPCO’s Q3 turnaround to higher electricity bills. The price row produced MFE_90D/MFE_180D +46.26% with MAE_180D only -0.40%. This is the archetype’s ideal: policy lever → company P&L bridge → low-MAE repricing.

### C31_R11_L172_08 — 메가엠디 / medical-school quota / counterexample

The medical-school quota policy produced a strong thematic MFE_30D of +24.74%, but it had no durable listed-company revenue bridge and later carried MAE_180D -42.21%. This is the textbook C31 false positive: policy beneficiary imagination without call-off, contract, pricing, or earnings conversion.

## 7. Machine-readable trigger rows JSONL

```jsonl
{"row_type": "trigger", "case_id": "C31_R11_L172_01", "round": "R11", "loop": 172, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE", "ticker": "289010", "name": "아이스크림에듀", "event_title": "AI digital textbook policy rollout", "evidence_date": "2023-06-08", "entry_date": "2023-06-09", "entry_price": 5050.0, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "MFE_30D_pct": 17.23, "MAE_30D_pct": -13.86, "MFE_90D_pct": 17.23, "MAE_90D_pct": -25.94, "MFE_180D_pct": 17.23, "MAE_180D_pct": -31.68, "D30_date": "2023-07-21", "D90_date": "2023-10-23", "D180_date": "2024-03-05", "peak_180D_date": "2023-06-21", "trough_180D_date": "2023-11-10", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180D_contaminated": false, "profile_check": "profile corporate_action_candidate_count=0; window_180D clean", "evidence_url": "https://english.moe.go.kr/boardCnts/viewRenewal.do?boardID=254&boardSeq=95291&lev=0&m=0202&opType=N&page=2&s=english", "company_bridge_url": "https://www.i-screammedia.com/en/business_ai_textbook.html", "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|289010|Stage2-Watch|2023-06-09"}
{"row_type": "trigger", "case_id": "C31_R11_L172_02", "round": "R11", "loop": 172, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE", "ticker": "057030", "name": "YBM넷", "event_title": "AI digital textbook publisher/edtech bridge", "evidence_date": "2023-06-08", "entry_date": "2023-06-09", "entry_price": 4765.0, "trigger_type": "Stage2-Watch", "case_label": "positive_with_4B_exit_guard", "MFE_30D_pct": 11.44, "MAE_30D_pct": -21.51, "MFE_90D_pct": 11.44, "MAE_90D_pct": -30.95, "MFE_180D_pct": 31.37, "MAE_180D_pct": -30.95, "D30_date": "2023-07-21", "D90_date": "2023-10-23", "D180_date": "2024-03-05", "peak_180D_date": "2023-12-13", "trough_180D_date": "2023-07-26", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180D_contaminated": false, "profile_check": "profile corporate_action_candidate_dates=2005-04-21,2010-01-25; no overlap with 2023-06-09~D180", "evidence_url": "https://english.moe.go.kr/boardCnts/viewRenewal.do?boardID=254&boardSeq=95291&lev=0&m=0202&opType=N&page=2&s=english", "company_bridge_url": "https://www.ybmcloud.com/aidt/present", "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|057030|Stage2-Watch|2023-06-09"}
{"row_type": "trigger", "case_id": "C31_R11_L172_03", "round": "R11", "loop": 172, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE", "ticker": "032850", "name": "비트컴퓨터", "event_title": "Full telemedicine allowance during medical crisis", "evidence_date": "2024-02-23", "entry_date": "2024-02-26", "entry_price": 7730.0, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "MFE_30D_pct": 10.09, "MAE_30D_pct": -24.32, "MFE_90D_pct": 10.09, "MAE_90D_pct": -28.2, "MFE_180D_pct": 10.09, "MAE_180D_pct": -41.14, "D30_date": "2024-04-09", "D90_date": "2024-07-09", "D180_date": "2024-11-21", "peak_180D_date": "2024-02-26", "trough_180D_date": "2024-11-13", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180D_contaminated": false, "profile_check": "profile corporate_action_candidate_dates only 1999~2000; no overlap with 2024 window", "evidence_url": "https://www.reuters.com/world/asia-pacific/south-korea-fully-allow-telemedicine-all-hospitals-clinics-2024-02-23/", "company_bridge_url": "https://www.bit.kr/eng/index.php", "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|032850|Stage2-Watch|2024-02-26"}
{"row_type": "trigger", "case_id": "C31_R11_L172_04", "round": "R11", "loop": 172, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE", "ticker": "032620", "name": "유비케어", "event_title": "Telemedicine/EMR platform policy beta", "evidence_date": "2024-02-23", "entry_date": "2024-02-26", "entry_price": 6490.0, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "MFE_30D_pct": 9.86, "MAE_30D_pct": -27.27, "MFE_90D_pct": 9.86, "MAE_90D_pct": -29.12, "MFE_180D_pct": 9.86, "MAE_180D_pct": -48.92, "D30_date": "2024-04-09", "D90_date": "2024-07-09", "D180_date": "2024-11-21", "peak_180D_date": "2024-02-26", "trough_180D_date": "2024-11-14", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180D_contaminated": false, "profile_check": "profile corporate_action_candidate_dates through 2018-05-11; no overlap with 2024 window", "evidence_url": "https://www.reuters.com/world/asia-pacific/south-korea-fully-allow-telemedicine-all-hospitals-clinics-2024-02-23/", "company_bridge_url": "https://www.mk.co.kr/en/it/10969249", "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|032620|Stage2-Watch|2024-02-26"}
{"row_type": "trigger", "case_id": "C31_R11_L172_05", "round": "R11", "loop": 172, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE", "ticker": "211270", "name": "AP위성", "event_title": "KASA launch / space-economy policy", "evidence_date": "2024-05-30", "entry_date": "2024-05-31", "entry_price": 16470.0, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "MFE_30D_pct": 17.49, "MAE_30D_pct": -17.43, "MFE_90D_pct": 17.49, "MAE_90D_pct": -41.71, "MFE_180D_pct": 17.49, "MAE_180D_pct": -41.71, "D30_date": "2024-07-15", "D90_date": "2024-10-16", "D180_date": "2025-02-28", "peak_180D_date": "2024-05-31", "trough_180D_date": "2024-09-09", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180D_contaminated": false, "profile_check": "profile corporate_action_candidate_count=0; window_180D clean", "evidence_url": "https://www.reuters.com/science/south-korea-plans-mars-landing-2045-it-launches-first-space-agency-2024-05-30/", "company_bridge_url": "https://www.msit.go.kr/eng/bbs/view.do?bbsSeqNo=42&mId=4&mPid=2&nttSeqNo=950&sCode=eng", "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|211270|Stage2-Watch|2024-05-31"}
{"row_type": "trigger", "case_id": "C31_R11_L172_06", "round": "R11", "loop": 172, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE", "ticker": "099320", "name": "쎄트렉아이", "event_title": "KASA launch / satellite systems policy bridge", "evidence_date": "2024-05-30", "entry_date": "2024-05-31", "entry_price": 47700.0, "trigger_type": "Stage2-Actionable", "case_label": "positive_with_4B_exit_guard", "MFE_30D_pct": 22.64, "MAE_30D_pct": -2.52, "MFE_90D_pct": 22.64, "MAE_90D_pct": -33.75, "MFE_180D_pct": 22.64, "MAE_180D_pct": -33.75, "D30_date": "2024-07-15", "D90_date": "2024-10-16", "D180_date": "2025-02-28", "peak_180D_date": "2024-07-01", "trough_180D_date": "2024-09-09", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180D_contaminated": false, "profile_check": "profile corporate_action_candidate_date includes 2024-01-08, before 2024-05-31 entry; no 180D overlap", "evidence_url": "https://www.reuters.com/science/south-korea-plans-mars-landing-2045-it-launches-first-space-agency-2024-05-30/", "company_bridge_url": "https://www.satreci.com/", "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|099320|Stage2-Actionable|2024-05-31"}
{"row_type": "trigger", "case_id": "C31_R11_L172_07", "round": "R11", "loop": 172, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE", "ticker": "015760", "name": "한국전력", "event_title": "Electricity tariff hikes -> KEPCO profit bridge", "evidence_date": "2023-11-13", "entry_date": "2023-11-14", "entry_price": 17400.0, "trigger_type": "Stage2-Actionable", "case_label": "positive", "MFE_30D_pct": 13.51, "MAE_30D_pct": -0.4, "MFE_90D_pct": 46.26, "MAE_90D_pct": -0.4, "MFE_180D_pct": 46.26, "MAE_180D_pct": -0.4, "D30_date": "2023-12-27", "D90_date": "2024-03-27", "D180_date": "2024-08-07", "peak_180D_date": "2024-03-14", "trough_180D_date": "2023-11-14", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180D_contaminated": false, "profile_check": "profile corporate_action_candidate_count=0; window_180D clean", "evidence_url": "https://en.yna.co.kr/view/AEN20231113005751320", "company_bridge_url": "https://www.kepco.co.kr/eng/index.do", "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|015760|Stage2-Actionable|2023-11-14"}
{"row_type": "trigger", "case_id": "C31_R11_L172_08", "round": "R11", "loop": 172, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE", "ticker": "133750", "name": "메가엠디", "event_title": "Medical school quota expansion education-policy beta", "evidence_date": "2024-02-06", "entry_date": "2024-02-07", "entry_price": 2850.0, "trigger_type": "Stage2-Watch", "case_label": "counterexample", "MFE_30D_pct": 24.74, "MAE_30D_pct": -6.32, "MFE_90D_pct": 24.74, "MAE_90D_pct": -22.63, "MFE_180D_pct": 24.74, "MAE_180D_pct": -42.21, "D30_date": "2024-03-25", "D90_date": "2024-06-24", "D180_date": "2024-11-06", "peak_180D_date": "2024-03-05", "trough_180D_date": "2024-08-05", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_180D_contaminated": false, "profile_check": "profile corporate_action_candidate_count=0; window_180D clean", "evidence_url": "https://www.chosun.com/english/national-en/2024/02/07/5ERYNGUGKFDZNEXJ3UGIU6KGBA/", "company_bridge_url": "https://apnews.com/article/945b27253b1166109e3ce1c1a402f39e", "dedupe_key": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT|133750|Stage2-Watch|2024-02-07"}
```

## 8. Raw component score simulation JSONL

```jsonl
{"row_type": "score_simulation", "case_id": "C31_R11_L172_01", "ticker": "289010", "policy_specificity_score": 55, "legal_budget_binding_score": 40, "company_direct_exposure_score": 30, "commercial_conversion_bridge_score": 35, "price_alignment_score": 45, "policy_reversal_or_delay_risk_score": 82, "simulated_current_profile_error": true, "intended_shadow_rule_effect": "upgrade only when policy has binding budget/implementation plus company-level revenue or profit bridge; otherwise keep Stage2-Watch/4B guard"}
{"row_type": "score_simulation", "case_id": "C31_R11_L172_02", "ticker": "057030", "policy_specificity_score": 74, "legal_budget_binding_score": 67, "company_direct_exposure_score": 58, "commercial_conversion_bridge_score": 55, "price_alignment_score": 63, "policy_reversal_or_delay_risk_score": 70, "simulated_current_profile_error": true, "intended_shadow_rule_effect": "upgrade only when policy has binding budget/implementation plus company-level revenue or profit bridge; otherwise keep Stage2-Watch/4B guard"}
{"row_type": "score_simulation", "case_id": "C31_R11_L172_03", "ticker": "032850", "policy_specificity_score": 55, "legal_budget_binding_score": 40, "company_direct_exposure_score": 30, "commercial_conversion_bridge_score": 35, "price_alignment_score": 45, "policy_reversal_or_delay_risk_score": 82, "simulated_current_profile_error": true, "intended_shadow_rule_effect": "upgrade only when policy has binding budget/implementation plus company-level revenue or profit bridge; otherwise keep Stage2-Watch/4B guard"}
{"row_type": "score_simulation", "case_id": "C31_R11_L172_04", "ticker": "032620", "policy_specificity_score": 55, "legal_budget_binding_score": 40, "company_direct_exposure_score": 30, "commercial_conversion_bridge_score": 35, "price_alignment_score": 45, "policy_reversal_or_delay_risk_score": 82, "simulated_current_profile_error": true, "intended_shadow_rule_effect": "upgrade only when policy has binding budget/implementation plus company-level revenue or profit bridge; otherwise keep Stage2-Watch/4B guard"}
{"row_type": "score_simulation", "case_id": "C31_R11_L172_05", "ticker": "211270", "policy_specificity_score": 55, "legal_budget_binding_score": 40, "company_direct_exposure_score": 30, "commercial_conversion_bridge_score": 35, "price_alignment_score": 45, "policy_reversal_or_delay_risk_score": 82, "simulated_current_profile_error": true, "intended_shadow_rule_effect": "upgrade only when policy has binding budget/implementation plus company-level revenue or profit bridge; otherwise keep Stage2-Watch/4B guard"}
{"row_type": "score_simulation", "case_id": "C31_R11_L172_06", "ticker": "099320", "policy_specificity_score": 74, "legal_budget_binding_score": 67, "company_direct_exposure_score": 58, "commercial_conversion_bridge_score": 55, "price_alignment_score": 63, "policy_reversal_or_delay_risk_score": 70, "simulated_current_profile_error": true, "intended_shadow_rule_effect": "upgrade only when policy has binding budget/implementation plus company-level revenue or profit bridge; otherwise keep Stage2-Watch/4B guard"}
{"row_type": "score_simulation", "case_id": "C31_R11_L172_07", "ticker": "015760", "policy_specificity_score": 82, "legal_budget_binding_score": 78, "company_direct_exposure_score": 70, "commercial_conversion_bridge_score": 72, "price_alignment_score": 75, "policy_reversal_or_delay_risk_score": 30, "simulated_current_profile_error": false, "intended_shadow_rule_effect": "upgrade only when policy has binding budget/implementation plus company-level revenue or profit bridge; otherwise keep Stage2-Watch/4B guard"}
{"row_type": "score_simulation", "case_id": "C31_R11_L172_08", "ticker": "133750", "policy_specificity_score": 55, "legal_budget_binding_score": 40, "company_direct_exposure_score": 30, "commercial_conversion_bridge_score": 35, "price_alignment_score": 45, "policy_reversal_or_delay_risk_score": 82, "simulated_current_profile_error": true, "intended_shadow_rule_effect": "upgrade only when policy has binding budget/implementation plus company-level revenue or profit bridge; otherwise keep Stage2-Watch/4B guard"}
```

## 9. Aggregate row

```json
{"row_type": "aggregate", "round": "R11", "loop": 172, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "usable_trigger_row_count": 8, "representative_trigger_count": 8, "positive_case_count": 1, "positive_with_4B_exit_guard_count": 2, "counterexample_count": 5, "stage4b_watch_or_overlay_count": 7, "current_profile_error_count": 7, "avg_MFE_90D_pct": 19.97, "avg_MAE_90D_pct": -26.59, "avg_MFE_180D_pct": 22.46, "avg_MAE_180D_pct": -33.84, "source_proxy_only_count": 0, "evidence_url_pending_count": 0}
```

## 10. Narrative-only rows blocked from calibration

```jsonl
{"row_type": "narrative_only", "case_id": "C31_R11_L172_N01", "topic": "AI textbook rollback after launch", "reason": "event date 2025-10/2025-12 has insufficient 180-trading-day forward window under stock-web max_date=2026-02-20; useful as future C31 legal/reversal-risk audit only", "evidence_url": "https://restofworld.org/2025/south-korea-ai-textbook/"}
{"row_type": "narrative_only", "case_id": "C31_R11_L172_N02", "topic": "formal telemedicine amendment after pilot period", "reason": "late-2025 legal passage has insufficient 180D window; keep as future C31 implementation-confirmation row, not current calibration trigger", "evidence_url": "https://iclg.com/practice-areas/digital-health-laws-and-regulations/korea/"}
```

These narrative-only rows are useful future watchpoints but are not promotion rows because stock-web cannot yet provide a full 180-trading-day forward window from the late-2025 event dates.

## 11. Current calibrated profile stress test

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stress_target = residual C31 policy-event false positives
observed_failure_mode = policy/legal vocabulary can still overpower missing company-level commercial bridge
current_profile_error_count = 7
positive_case_count = 1
positive_with_4B_exit_guard_count = 2
counterexample_count = 5
```

The current profile already blocks price-only blowoff and requires non-price evidence for full 4B. The remaining C31 issue is subtler: **non-price evidence exists, but it is sometimes only government intent, not company monetization**. A Ministry plan, emergency permission, KASA launch, or quota expansion is real evidence; it is just the wrong layer of evidence if the company cannot show budget/tender/reimbursement/earnings conversion.

## 12. Shadow rule candidate

```text
canonical_archetype_rule_candidate = C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE_GATE_V1
sector_specific_rule_candidate = L10_POLICY_EVENT_LEGAL_BINDING_AND_COMPANY_CONVERSION_GATE_V1
new_axis_proposed = c31_policy_implementation_budget_commercial_bridge_gate
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|local_4b_watch_guard
existing_axis_weakened = null
```

### Rule draft

For C31, Stage2-Actionable requires at least two of the following four bridges:

1. **Binding policy bridge**: law, cabinet decision, official rollout date, tariff decision, budget allocation, approved textbook/program list, or official procurement framework.
2. **Company direct-exposure bridge**: named product/service that maps directly to the policy mechanism, not just sector adjacency.
3. **Commercial conversion bridge**: tender/order, reimbursement, tariff-to-sales, paid users, procurement volume, contract, or margin/revision evidence.
4. **Timing bridge**: entry occurs before policy euphoria exhausts the move; if 30D MFE is followed by 90D or 180D MAE below -20%, force local 4B/high-MAE guard.

If only the first bridge exists, keep Stage2-Watch or counterexample. If bridges 1+2 exist but bridge 3 is absent, allow Stage2-Watch only. If bridges 1+2+3 exist and MAE risk is controlled, allow Stage2-Actionable. If bridges exist but MAE_90D or MAE_180D is below -20%, attach 4B exit guard and block Stage3-Green.

## 13. Residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
new_independent_case_count = 8
reused_case_count = 0
same_archetype_new_symbol_count = 8
same_archetype_new_trigger_family_count = 5
calibration_usable_case_count = 8
calibration_usable_trigger_count = 8
source_proxy_only_count = 0
evidence_url_pending_count = 0
auto_selected_coverage_gap = index baseline C31 rows 118 -> 126 if accepted; session-aware first dedicated C31 pass after loop171 C32
```

This pass does not propose a broad weight increase. It proposes a guard: policy-event evidence should be treated like a permit, not like revenue. The engine should ask whether the permit has found a tollbooth.

## 14. Deferred Coding Agent Handoff Prompt

```text
You are the later coding agent. Do not rerun this research. Ingest this MD as a v12 standalone residual research artifact.

Implement only after batch validation:
- Parse all row_type=trigger JSONL rows.
- Validate standard filename/metadata consistency.
- Confirm price_source=Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap.
- Confirm all usable trigger rows include entry_date, entry_price, trigger_type, 30/90/180D MFE and MAE.
- Deduplicate by canonical_archetype_id + ticker + trigger_type + entry_date.
- Treat C31_POLICY_IMPLEMENTATION_BUDGET_COMMERCIAL_BRIDGE_GATE_V1 as a shadow rule candidate only.
- Do not loosen Stage3-Green thresholds.
- Consider a C31-specific Stage2 bridge requirement that distinguishes policy intent from company monetization.
- Attach local 4B/high-MAE guard when MAE_90D or MAE_180D <= -20 even if policy evidence is real.
```

## 15. Next research state

```text
completed_round = R11
completed_loop = 172
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/thin-P2 clearing
next_recommended_archetypes = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|C31_POLICY_SUBSIDY_LEGISLATION_EVENT_SECOND_PASS
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
