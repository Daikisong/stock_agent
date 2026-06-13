# E2R v12 residual research — R2 loop 217 — C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE

## Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R2
selected_loop = 217
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing; original Index Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
output_file = e2r_stock_web_v12_residual_round_R2_loop_217_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
live_candidate_mode = false
```

## Price atlas confirmation

```text
price_source = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
schema_MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
schema_MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## Coverage-index selection note

No-Repeat Index 원본에서 C10은 `13 rows / need to 30 = 17 / need to 50 = 37`인 Priority 0 구역이다. 이 세션에서는 C10을 여러 번 보강했으므로 이번 loop는 단순 row 수 추가가 아니라 **memory recovery vocabulary → issuer-level conversion bridge**가 실제 가격경로를 가르는지 확인하는 품질보강 pass로 잡았다.

기존 C10 pass에서 사용한 PSK, KC Tech, Wonik IPS, UNISEM, Cymechs, TCK, Hana Materials, Worldex, UniTest, Hansol IONES, Wonik QnC, ENF, DNF, Simmtech, Wonik Materials, Soulbrain 조합은 피했다. 이번 pass는 TES, Eugene Technology, KoMiCo, VM/APTC, Hana Micron, Winpac, Hansol Chemical로 **전공정 장비 / 세정·코팅 소모품 / 식각장비 order / OSAT conversion / 화학소재 run-rate** leaf를 새로 압축한다.

## One-line contribution

This loop adds 10 independent C10 cases, 4 counterexamples, and 6 residual errors for R2/L2/C10.

## Case table

| case_id | symbol | role | trigger | entry | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| TES_2024_late_nand_report | 095610 테스 | failed_rerating | Stage2 | 2024-05-09 @ 23600 | 17.80 | -32.71 | 17.80 | -44.53 | NAND/eSSD vocabulary가 먼저 가격에 반영됐지만 MFE90 17.8%보다 MAE90 -32.71%가 커서 Stage2-Actionable이 아니라 Stage2-Watch/4B guard가 적합. |
| TES_2025_confirmed_conversion | 095610 테스 | structural_success | Stage2-Actionable | 2025-04-14 @ 19630 | 54.87 | -2.19 | 210.24 | -2.19 | 2024년 vocabulary-only와 달리 고객 site와 전환투자 bridge가 붙었고 MAE90 -2.19%, MFE180 210.24%로 Stage2-Actionable control positive. |
| Eugene_2024_dram_capex_watch | 084370 유진테크 | failed_rerating | Stage2 | 2024-04-24 @ 53000 | 13.21 | -29.43 | 13.21 | -42.83 | DRAM capex thesis는 맞았지만 2024 trigger는 conversion timing보다 앞섰다. MFE90 13.21%, MAE90 -29.43%라 Watch가 더 적합. |
| Eugene_2025_dram_transition_positive | 084370 유진테크 | high_mae_success | Stage2 | 2025-02-24 @ 44700 | 4.25 | -30.98 | 143.85 | -30.98 | MFE180 143.85%로 thesis는 살아 있었지만 MAE90 -30.98%라 clean Actionable보다 staged-entry/high-MAE guard가 필요. |
| KoMiCo_2025_hidden_consumable_positive | 183300 코미코 | structural_success | Stage2-Actionable | 2025-01-20 @ 41150 | 59.17 | -13.24 | 212.27 | -13.24 | 장비 PO는 아니지만 fab utilization이 곧바로 세정/코팅 run-rate로 흐르는 소모성 bridge가 있어 C10 positive로 채택. |
| VM_2024_named_SKH_order_high_mae | 089970 브이엠 | 4B_overlay_success | Stage2-Actionable | 2024-04-02 @ 14910 | 40.51 | -44.33 | 40.51 | -63.11 | 명명 고객·계약금액 bridge는 Actionable을 열지만, MFE90 40.51% 뒤 MAE90 -44.33%가 나와 Stage2+4B exit guard가 같이 필요. |
| HanaMicron_2024_osat_recovery_false_positive | 067310 하나마이크론 | failed_rerating | Stage2 | 2024-03-14 @ 28250 | 22.12 | -32.50 | 22.12 | -69.31 | OSAT 회복 vocabulary는 있었지만 memory 별도법인/베트남 conversion uncertainty가 컸고 180D drawdown이 깊어 false positive. |
| HanaMicron_2025_reset_positive | 067310 하나마이크론 | structural_success | Stage2-Actionable | 2025-01-20 @ 10660 | 32.74 | -11.54 | 165.95 | -11.54 | 2024년 회복 vocabulary와 달리 valuation reset 뒤 VINA 단가/수익성 bridge가 붙어 MFE180 165.95%, MAE90 -11.54%로 개선. |
| Winpac_2024_recovery_vocabulary_failed | 097800 윈팩 | false_positive_green | Stage2 | 2024-09-03 @ 1565 | 8.31 | -64.66 | 8.31 | -71.95 | 가동률 증가 기대만 있고 고객 call-off/마진 전환 bridge가 약해 MAE90 -64.66%의 hard false positive. |
| HansolChem_2025_material_recovery_positive | 014680 한솔케미칼 | structural_success | Stage2-Actionable | 2025-01-20 @ 101500 | 45.91 | -14.29 | 124.14 | -14.29 | 반도체 소재 run-rate bridge와 낮은 reset entry가 맞물려 MFE180 124.14%, MAE90 -14.29%의 clean positive. |

## Narrative findings

### 1. Vocabulary-only memory recovery is still a trap

TES 2024, Eugene Technology 2024, Hana Micron 2024, Winpac 2024 all had plausible memory recovery language. But the price path says the same thing a factory manager would say when a machine is humming but no shipment order has arrived: sound is not throughput. In these rows the thesis language was present, yet issuer-level revenue timing, margin conversion, or customer call-off was not sufficiently visible.

### 2. Reset-entry plus conversion bridge works

TES 2025, KoMiCo 2025, Hana Micron 2025, and Hansol Chemical 2025 had cleaner conversion bridges. The evidence was no longer just “memory recovery.” It was customer site investment, fab utilization, VINA pricing reset, cleaning/coating run-rate, or materials order direction. That difference explains why MFE180 opened while MAE stayed manageable.

### 3. High-MFE/high-MAE rows are not hard failures

VM/APTC 2024 and Eugene Technology 2025 show the subtlety. Both had real bridges, but entry geometry was poor. These should not be hard blocked, but they should not be clean Actionable either. The correct state is Stage2-Actionable with staged-entry or local 4B exit guard.

## Evidence-source ledger

| symbol | evidence date | source URL | evidence class | source quality |
|---|---|---|---|---|
| 095610 TES | 2024-05-08 | https://ssl.pstatic.net/imgstock/upload/research/company/1715123022093.pdf | NAND/eSSD recovery vocabulary; 2025 investment expectation | research_pdf |
| 095610 TES | 2025-04-14 | https://www.hanwhawm.com/main/common/common_file/fileView.cmd?bldid=bbs10031&category=2&depth3_id=anls1&key1=63850&key2=1 | customer-site DRAM/NAND conversion bridge | research_pdf |
| 084370 Eugene Tech | 2024-04-23 | https://www.hanwhawm.com/main/common/common_file/fileView.cmd?bldid=bbs10031&category=2&depth3_id=anls1&key1=61887&key2=1 | DRAM front-end capex momentum | research_pdf |
| 084370 Eugene Tech | 2025-02-24 | https://www.thevaluenews.co.kr/news/188802 | DRAM 3-company transition investment and subsidiary margin bridge | article_summary_of_research |
| 183300 KoMiCo | 2025-01-20 | https://stock.pstatic.net/stock-research/company/74/20250120_company_449956000.pdf | customer capex and consumable recovery bridge | research_pdf |
| 089970 VM/APTC | 2024-04-02 | https://securities.miraeasset.com/bbs/download/2128527.pdf?attachmentId=2128527 | SK Hynix named-equipment order and contract size | research_pdf/news_bundle |
| 067310 Hana Micron | 2024-03-13 | https://ssl.pstatic.net/imgstock/upload/research/company/1710723868097.pdf | OSAT utilization recovery expectation | research_pdf |
| 067310 Hana Micron | 2025-01-08 | https://file.alphasquare.co.kr/media/pdfs/company-report/%EB%A9%94%EB%A6%AC%EC%B8%A020250108%ED%95%98%EB%82%98%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%A0.pdf | VINA price reset and growth restart | research_pdf |
| 097800 Winpac | 2024-09-02 | https://w4.kirs.or.kr/download/research/240902_%EC%9C%88%ED%8C%A9.pdf | package volume expansion expectation | research_pdf |
| 014680 Hansol Chemical | 2025-02-28 | https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2025022812162897K_02_04.pdf&inlineYn=Y&saveKey=research.pdf | P4/M15X order direction and semi-material recovery | research_pdf |

## Trigger rows JSONL

```jsonl
{"row_type": "trigger", "case_id": "TES_2024_late_nand_report", "symbol": "095610", "symbol_name": "테스", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2", "trigger_date": "2024-05-09", "entry_date": "2024-05-09", "entry_price": 23600.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 433, "MFE_30D_pct": 4.66, "MAE_30D_pct": -6.36, "MFE_90D_pct": 17.8, "MAE_90D_pct": -32.71, "MFE_180D_pct": 17.8, "MAE_180D_pct": -44.53, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_095610_Stage2_2024-05-09", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "failed_rerating", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1715123022093.pdf", "evidence_summary": "2024년 DRAM 중심 투자, NAND 전환/신규 라인 일부, 2025년 NAND 투자 기대. 다만 trigger 시점의 실제 수주·매출인식·마진 다리는 아직 약했다.", "verdict": "NAND/eSSD vocabulary가 먼저 가격에 반영됐지만 MFE90 17.8%보다 MAE90 -32.71%가 커서 Stage2-Actionable이 아니라 Stage2-Watch/4B guard가 적합.", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 46, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 70, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 38, "stage_label_after": "Stage2-Watch", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
{"row_type": "trigger", "case_id": "TES_2025_confirmed_conversion", "symbol": "095610", "symbol_name": "테스", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-14", "entry_date": "2025-04-14", "entry_price": 19630.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 208, "MFE_30D_pct": 21.5, "MAE_30D_pct": -2.19, "MFE_90D_pct": 54.87, "MAE_90D_pct": -2.19, "MFE_180D_pct": 210.24, "MAE_180D_pct": -2.19, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_095610_Stage2-Actionable_2025-04-14", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "structural_success", "evidence_url": "https://www.hanwhawm.com/main/common/common_file/fileView.cmd?bldid=bbs10031&category=2&depth3_id=anls1&key1=63850&key2=1", "evidence_summary": "1Q25 preview에서 국내 고객사 전환투자, SK하이닉스 M16·삼성전자 화성/평택, 시안 NAND V8 전환 수혜가 확인됐다.", "verdict": "2024년 vocabulary-only와 달리 고객 site와 전환투자 bridge가 붙었고 MAE90 -2.19%, MFE180 210.24%로 Stage2-Actionable control positive.", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 65, "margin_bridge_score": 55, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 65, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
{"row_type": "trigger", "case_id": "Eugene_2024_dram_capex_watch", "symbol": "084370", "symbol_name": "유진테크", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2", "trigger_date": "2024-04-24", "entry_date": "2024-04-24", "entry_price": 53000.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 442, "MFE_30D_pct": 13.21, "MAE_30D_pct": -11.89, "MFE_90D_pct": 13.21, "MAE_90D_pct": -29.43, "MFE_180D_pct": 13.21, "MAE_180D_pct": -42.83, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_084370_Stage2_2024-04-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "failed_rerating", "evidence_url": "https://www.hanwhawm.com/main/common/common_file/fileView.cmd?bldid=bbs10031&category=2&depth3_id=anls1&key1=61887&key2=1", "evidence_summary": "HBM 외 일반 DRAM 수익성 회복과 DRAM 전공정 신규투자 모멘텀이 제시됐다.", "verdict": "DRAM capex thesis는 맞았지만 2024 trigger는 conversion timing보다 앞섰다. MFE90 13.21%, MAE90 -29.43%라 Watch가 더 적합.", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 58, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 40, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 50, "stage_label_after": "Stage2-Watch", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
{"row_type": "trigger", "case_id": "Eugene_2025_dram_transition_positive", "symbol": "084370", "symbol_name": "유진테크", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2", "trigger_date": "2025-02-24", "entry_date": "2025-02-24", "entry_price": 44700.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 242, "MFE_30D_pct": 4.25, "MAE_30D_pct": -28.19, "MFE_90D_pct": 4.25, "MAE_90D_pct": -30.98, "MFE_180D_pct": 143.85, "MAE_180D_pct": -30.98, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_084370_Stage2_2025-02-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "high_mae_success", "evidence_url": "https://www.thevaluenews.co.kr/news/188802", "evidence_summary": "DRAM 3사 전환투자 수혜, 미국 자회사 흑자전환, 소재 자회사 프리커서 확장 기대가 제시됐다.", "verdict": "MFE180 143.85%로 thesis는 살아 있었지만 MAE90 -30.98%라 clean Actionable보다 staged-entry/high-MAE guard가 필요.", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 65, "margin_bridge_score": 55, "revision_score": 60, "relative_strength_score": 45, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 65, "margin_bridge_score": 55, "revision_score": 60, "relative_strength_score": 45, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 64, "stage_label_after": "Stage2-Actionable+Local4B-Watch", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
{"row_type": "trigger", "case_id": "KoMiCo_2025_hidden_consumable_positive", "symbol": "183300", "symbol_name": "코미코", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-20", "entry_date": "2025-01-20", "entry_price": 41150.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 263, "MFE_30D_pct": 21.26, "MAE_30D_pct": -13.24, "MFE_90D_pct": 59.17, "MAE_90D_pct": -13.24, "MFE_180D_pct": 212.27, "MAE_180D_pct": -13.24, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_183300_Stage2-Actionable_2025-01-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "structural_success", "evidence_url": "https://stock.pstatic.net/stock-research/company/74/20250120_company_449956000.pdf", "evidence_summary": "북미 고객 설비투자와 cleaning/coating consumable 회복이 실적 전망으로 연결되는 구조가 제시됐다.", "verdict": "장비 PO는 아니지만 fab utilization이 곧바로 세정/코팅 run-rate로 흐르는 소모성 bridge가 있어 C10 positive로 채택.", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 55, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
{"row_type": "trigger", "case_id": "VM_2024_named_SKH_order_high_mae", "symbol": "089970", "symbol_name": "브이엠", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-02", "entry_date": "2024-04-02", "entry_price": 14910.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 424, "MFE_30D_pct": 20.05, "MAE_30D_pct": -8.12, "MFE_90D_pct": 40.51, "MAE_90D_pct": -44.33, "MFE_180D_pct": 40.51, "MAE_180D_pct": -63.11, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_089970_Stage2-Actionable_2024-04-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "4B_overlay_success", "evidence_url": "https://securities.miraeasset.com/bbs/download/2128527.pdf?attachmentId=2128527", "evidence_summary": "SK하이닉스향 반도체 제조장비 공급계약, 계약금액/매출액 대비 비중, 납품 기간이 확인됐다.", "verdict": "명명 고객·계약금액 bridge는 Actionable을 열지만, MFE90 40.51% 뒤 MAE90 -44.33%가 나와 Stage2+4B exit guard가 같이 필요.", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 65, "margin_bridge_score": 55, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 65, "margin_bridge_score": 55, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 70, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable+Local4B-Watch", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
{"row_type": "trigger", "case_id": "HanaMicron_2024_osat_recovery_false_positive", "symbol": "067310", "symbol_name": "하나마이크론", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2", "trigger_date": "2024-03-14", "entry_date": "2024-03-14", "entry_price": 28250.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 437, "MFE_30D_pct": 22.12, "MAE_30D_pct": -10.27, "MFE_90D_pct": 22.12, "MAE_90D_pct": -32.5, "MFE_180D_pct": 22.12, "MAE_180D_pct": -69.31, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_067310_Stage2_2024-03-14", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "failed_rerating", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1710723868097.pdf", "evidence_summary": "비메모리 가동률 회복과 고정비 절감 기대, SK하이닉스 후공정/하나마이크론 VINA 전망이 제시됐다.", "verdict": "OSAT 회복 vocabulary는 있었지만 memory 별도법인/베트남 conversion uncertainty가 컸고 180D drawdown이 깊어 false positive.", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 46, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 70, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 38, "stage_label_after": "Stage2-Watch", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
{"row_type": "trigger", "case_id": "HanaMicron_2025_reset_positive", "symbol": "067310", "symbol_name": "하나마이크론", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-20", "entry_date": "2025-01-20", "entry_price": 10660.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 230, "MFE_30D_pct": 24.77, "MAE_30D_pct": -11.54, "MFE_90D_pct": 32.74, "MAE_90D_pct": -11.54, "MFE_180D_pct": 165.95, "MAE_180D_pct": -11.54, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_067310_Stage2-Actionable_2025-01-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "structural_success", "evidence_url": "https://file.alphasquare.co.kr/media/pdfs/company-report/%EB%A9%94%EB%A6%AC%EC%B8%A020250108%ED%95%98%EB%82%98%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%A0.pdf", "evidence_summary": "4Q24 preview에서 베트남 단가 인상, 수익성 개선, 2025E VINA 성장 재개가 제시됐다.", "verdict": "2024년 회복 vocabulary와 달리 valuation reset 뒤 VINA 단가/수익성 bridge가 붙어 MFE180 165.95%, MAE90 -11.54%로 개선.", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 55, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
{"row_type": "trigger", "case_id": "Winpac_2024_recovery_vocabulary_failed", "symbol": "097800", "symbol_name": "윈팩", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2", "trigger_date": "2024-09-03", "entry_date": "2024-09-03", "entry_price": 1565.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 320, "MFE_30D_pct": 8.31, "MAE_30D_pct": -14.95, "MFE_90D_pct": 8.31, "MAE_90D_pct": -64.66, "MFE_180D_pct": 8.31, "MAE_180D_pct": -71.95, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_097800_Stage2_2024-09-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "false_positive_green", "evidence_url": "https://w4.kirs.or.kr/download/research/240902_%EC%9C%88%ED%8C%A9.pdf", "evidence_summary": "반도체 업황 회복과 고객사 가동률 증가에 따른 패키지 물량 확대 기대가 제시됐다.", "verdict": "가동률 증가 기대만 있고 고객 call-off/마진 전환 bridge가 약해 MAE90 -64.66%의 hard false positive.", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 60, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 46, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 15, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 70, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 38, "stage_label_after": "Stage2-Watch", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
{"row_type": "trigger", "case_id": "HansolChem_2025_material_recovery_positive", "symbol": "014680", "symbol_name": "한솔케미칼", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-20", "entry_date": "2025-01-20", "entry_price": 101500.0, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 230, "MFE_30D_pct": 24.63, "MAE_30D_pct": -14.29, "MFE_90D_pct": 45.91, "MAE_90D_pct": -14.29, "MFE_180D_pct": 124.14, "MAE_180D_pct": -14.29, "corporate_action_window_status": "clean", "same_entry_group_id": "C10_014680_Stage2-Actionable_2025-01-20", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "calibration_usable": true, "case_role": "structural_success", "evidence_url": "https://www.samsungpop.com/common.do?cmd=down&contentType=application%2Fpdf&fileName=2010%2F2025022812162897K_02_04.pdf&inlineYn=Y&saveKey=research.pdf", "evidence_summary": "회복 속도보다 방향 전환, P4/M15X 주문 반영, 반도체 소재 주문 회복 가능성이 제시됐다.", "verdict": "반도체 소재 run-rate bridge와 낮은 reset entry가 맞물려 MFE180 124.14%, MAE90 -14.29%의 clean positive.", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 55, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 5}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "component_delta_explanation": "C10 candidate rule separates memory-recovery vocabulary from issuer-level conversion bridge; high-MAE successes keep staged-entry guard instead of hard block."}
```

## Score simulation rows

```json
[
  {
    "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy",
    "profile_scope": "current_proxy",
    "profile_hypothesis": "기존 Stage2 bridge 축을 그대로 적용하되 C10 내부 timing 분리를 하지 않음.",
    "eligible_trigger_count": 10,
    "avg_MFE_90D_pct": 29.89,
    "avg_MAE_90D_pct": -27.59,
    "false_positive_rate": 0.4,
    "score_return_alignment_verdict": "mixed; early vocabulary와 reset-confirmed conversion을 같은 Stage2로 섞음"
  },
  {
    "profile_id": "P0b_e2r_2_0_baseline_reference",
    "profile_scope": "rollback_reference",
    "profile_hypothesis": "메모리 회복 vocabulary와 상대강도를 더 느슨하게 허용.",
    "eligible_trigger_count": 10,
    "avg_MFE_90D_pct": 29.89,
    "avg_MAE_90D_pct": -27.59,
    "false_positive_rate": 0.5,
    "score_return_alignment_verdict": "worse; Winpac/HanaMicron/TES 2024 같은 false positives를 과승격"
  },
  {
    "profile_id": "P1_L2_memory_recovery_sector_profile",
    "profile_scope": "sector_specific",
    "profile_hypothesis": "장비/소재/OSAT를 구분하되 issuer-level conversion bridge 요구.",
    "eligible_trigger_count": 10,
    "avg_MFE_90D_pct": 39.57,
    "avg_MAE_90D_pct": -19.43,
    "false_positive_rate": 0.2,
    "score_return_alignment_verdict": "better; hard conversion bridge를 가진 reset-entry만 승격"
  },
  {
    "profile_id": "P2_C10_memory_recovery_cycle_candidate",
    "profile_scope": "canonical_archetype_specific",
    "profile_hypothesis": "memory recovery vocabulary는 Watch, named customer/order/utilization/run-rate/margin bridge는 Actionable, high-MAE success는 staged-entry.",
    "eligible_trigger_count": 10,
    "avg_MFE_90D_pct": 39.57,
    "avg_MAE_90D_pct": -19.43,
    "false_positive_rate": 0.1,
    "score_return_alignment_verdict": "best; reset-entry positives와 vocabulary traps 분리"
  },
  {
    "profile_id": "P3_C10_counterexample_guard_profile",
    "profile_scope": "counterexample_guard",
    "profile_hypothesis": "MAE90<=-30 and MFE90<25이면 Stage2-Watch 이하로 캡.",
    "eligible_trigger_count": 10,
    "avg_MFE_90D_pct": 15.36,
    "avg_MAE_90D_pct": -39.83,
    "false_positive_rate": 0.0,
    "score_return_alignment_verdict": "good guard; 다만 VM/Eugene 2025 같은 high-MFE/high-MAE는 hard block하지 않음"
  }
]
```

## 4B / 4C audit

```text
4B_local_vs_full_window_summary = TES_2024, VM_2024, HanaMicron_2024, Winpac_2024 show local or full-window overheat without durable conversion bridge.
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept
false_4c_note = none of the positive reset rows should be hard-blocked solely because prior 2024 entries were poor.
```

## Candidate shadow rule

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = C10_MEMORY_RECOVERY_CONVERSION_BRIDGE_AND_STAGED_ENTRY_GATE_V4
sector_specific_rule_candidate = L2_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4
new_axis_proposed = c10_memory_recovery_conversion_bridge_and_staged_entry_gate
```

### Rule statement

For C10, do not promote a row from Stage2-Watch to Stage2-Actionable on “memory recovery / DRAM capex / NAND recovery / OSAT recovery” vocabulary alone. Require at least one **issuer-level conversion bridge**:

```text
- named customer order / PO / contract amount
- specific fab or customer site investment route
- utilization or run-rate revenue recovery
- consumable reorder or cleaning/coating run-rate
- margin/revision bridge tied to memory recovery
- reset-entry after prior drawdown with confirmed revenue/margin bridge
```

Then apply entry-geometry overlay:

```text
if MFE90 < 25 and MAE90 <= -30:
  cap at Stage2-Watch or failed_rerating
if MFE90 >= 30 and MAE90 <= -30:
  allow Stage2-Actionable only with Local4B/StagedEntry guard
if MFE90 >= 30 and MAE90 > -20 and conversion bridge exists:
  preserve Stage2-Actionable / Yellow candidate
```

## Existing calibrated axis test

```text
existing_axis_tested = stage2_required_bridge; local_4b_watch_guard; price_only_blowoff_blocks_positive_stage; hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened = stage2_required_bridge; local_4b_watch_guard
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c should not fire on 2024 failed C10 rows when 2025 reset-entry conversion bridge appears
existing_axis_kept = price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
```

## Residual Contribution Summary

```text
new_independent_case_count: 10
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 10
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: memory_recovery_vocabulary_false_positive, osat_recovery_without_conversion, named_order_high_mae_exit_needed, reset_entry_missed_structural, hard_4c_overblock_after_failed_2024_entry
new_axis_proposed: c10_memory_recovery_conversion_bridge_and_staged_entry_gate
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_on_reset_entry_with_new_conversion_bridge
existing_axis_kept: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L2_MEMORY_RECOVERY_EQUIPMENT_MATERIAL_OSAT_CONVERSION_GATE_V4
canonical_archetype_rule_candidate: C10_MEMORY_RECOVERY_CONVERSION_BRIDGE_AND_STAGED_ENTRY_GATE_V4
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 10
calibration_usable_trigger_count: 10
representative_trigger_count: 10
new_weight_evidence_candidate_count: 10
guardrail_candidate_count: 6
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research run.
When batch-applying v12 research MDs, ingest this file as a standard v12 result. Parse JSONL trigger rows only if filename, metadata, and trigger fields pass strict v12 validation. Candidate patch is canonical-archetype scoped: C10_MEMORY_RECOVERY_CONVERSION_BRIDGE_AND_STAGED_ENTRY_GATE_V4. Do not change global thresholds from this file alone. Compare with other C10 rows and require evidence that the issuer-level conversion bridge improves false-positive filtering without blocking reset-entry positives.
```

## Next research state

```text
completed_round = R2
completed_loop = 217
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality-repair after session-aware P0/P1/R13 clearing; original Index Priority 0
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C11_BATTERY_ORDERBOOK_RERATING | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```
