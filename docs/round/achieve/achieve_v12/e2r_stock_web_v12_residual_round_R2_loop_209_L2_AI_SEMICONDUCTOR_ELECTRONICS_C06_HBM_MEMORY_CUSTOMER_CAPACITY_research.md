# E2R v12 Residual Research — R2 / L2 / C06 HBM Memory Customer Capacity
```text
selected_round: R2
selected_loop: 209
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_LAG_AND_PACKAGE_SYMPATHY_GATE_V1
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 URL/proxy quality + Priority 1 balance reinforcement
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
```
## 1. Executive Summary
이번 MD는 R2의 C07/C08 직접 수주·테스트소켓 보강 직후, 같은 L2 안에서 아직 남아 있는 C06의 핵심 경계인 **HBM customer capacity / qualification lag / package-substrate sympathy**를 분리한다. C06에서 true positive는 SK hynix처럼 customer-allocation, sold-out capacity, HBM revenue mix가 직접 확인되는 row다. 반대로 Samsung qualification lag, FCBGA/MLB/substrate product profile, memory-substrate recovery forecast는 Stage2 또는 4B/watch로 cap해야 한다.
핵심 residual은 단순하다. **HBM이라는 단어는 문패이고, 고객 배정·qualification·매출 mix·capacity allocation은 문 안으로 들어간 발자국이다.** 문패만으로 Green을 켜면 substrate sympathy와 qualification lag가 같은 신호처럼 보인다.
## 2. Price Source Validation
```text
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20
tradable_schema: d,o,h,l,c,v,a,mc,s,m
MFE_formula: (max high from entry_date through N tradable rows / entry_close - 1) * 100
MAE_formula: (min low from entry_date through N tradable rows / entry_close - 1) * 100
```
Local stock-web shards used in this run: `000660_2024/2025`, `005930_2024/2025`, `009150_2024/2025`, `007660_2024/2025`, `222800_2024/2025`, `353200_2024/2025`. All usable trigger rows had entry row, entry close, and 180 tradable forward rows available in the local stock-web mirror used for this session.
## 3. Novelty / No-Repeat Check
| ticker | trigger_type | entry_date | duplicate_key | novelty axis |
|---|---|---:|---|---|
| 000660 SK hynix | Stage2-Actionable | 2024-05-02 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage2-Actionable|2024-05-02` | direct_positive_customer_capacity |
| 000660 SK hynix | Stage3-Yellow | 2025-01-23 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY|000660|Stage3-Yellow|2025-01-23` | direct_positive_revenue_mix |
| 005930 Samsung Electronics | Stage4B | 2024-05-24 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage4B|2024-05-24` | qualification_lag_counterexample |
| 005930 Samsung Electronics | Stage2 | 2025-01-31 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY|005930|Stage2|2025-01-31` | reopen_but_customer_dependency |
| 009150 Samsung Electro-Mechanics | Stage2 | 2024-08-26 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY|009150|Stage2|2024-08-26` | package_substrate_sympathy_profile |
| 007660 ISU Petasys | Stage2-Actionable | 2024-09-24 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY|007660|Stage2-Actionable|2024-09-24` | ai_accelerator_customer_order_bridge |
| 222800 Simmtech | Stage4B | 2024-01-11 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY|222800|Stage4B|2024-01-11` | memory_substrate_forecast_false_positive |
| 353200 Daeduck Electronics | Stage2 | 2024-06-24 | `C06_HBM_MEMORY_CUSTOMER_CAPACITY|353200|Stage2|2024-06-24` | advanced_substrate_profile_not_customer_capacity |

No hard duplicate was intentionally reused from the currently visible No-Repeat ledger or the immediately preceding C07/C08/C10 runs in this session.
## 4. Trigger Price Table
| ticker | name | trigger | entry | close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough | post-peak DD |
|---|---|---|---:|---:|---:|---:|---:|---|---|---:|
| 000660 | SK hynix | Stage2-Actionable | 2024-05-02 | 173,600 | 32.20/-2.65 | 43.15/-13.31 | 43.15/-16.65 | 2024-07-11 | 2024-09-19 | -41.77 |
| 000660 | SK hynix | Stage3-Yellow | 2025-01-23 | 219,500 | 3.42/-17.40 | 9.79/-25.88 | 128.70/-25.88 | 2025-10-21 | 2025-04-09 | -6.77 |
| 005930 | Samsung Electronics | Stage4B | 2024-05-24 | 75,900 | 14.76/-3.16 | 17.00/-21.61 | 17.00/-34.26 | 2024-07-11 | 2024-11-14 | -43.81 |
| 005930 | Samsung Electronics | Stage2 | 2025-01-31 | 52,400 | 12.79/-3.05 | 18.32/-3.05 | 94.66/-3.05 | 2025-10-27 | 2025-02-03 | -1.37 |
| 009150 | Samsung Electro-Mechanics | Stage2 | 2024-08-26 | 144,200 | 1.18/-12.62 | 1.18/-26.84 | 3.88/-26.84 | 2025-02-17 | 2024-11-15 | -27.37 |
| 007660 | ISU Petasys | Stage2-Actionable | 2024-09-24 | 39,500 | 17.72/-22.78 | 17.72/-46.84 | 26.58/-46.84 | 2025-06-24 | 2024-11-18 | -6.10 |
| 222800 | Simmtech | Stage4B | 2024-01-11 | 38,800 | 1.80/-24.87 | 1.80/-28.61 | 1.80/-56.44 | 2024-01-11 | 2024-09-09 | -57.22 |
| 353200 | Daeduck Electronics | Stage2 | 2024-06-24 | 21,150 | 18.91/-0.95 | 18.91/-26.48 | 18.91/-39.15 | 2024-07-11 | 2024-12-09 | -48.83 |

## 5. Case Notes
### 000660 SK hynix — Stage2-Actionable / 2024-05-02
- **Evidence:** Reuters 2024-05-02: HBM sold out for 2024 and almost sold out for 2025; HBM3E samples and Q3 mass production schedule.
- **Source URL:** https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-hbm-chips-almost-sold-out-2025-2024-05-02/
- **Price path:** 180D MFE 43.15%, 180D MAE -16.65%, post-peak drawdown -41.77%.
- **E2R interpretation:** Stage2-Actionable preserved; Green blocked by 180D post-peak drawdown and missing cashflow repeat.

### 000660 SK hynix — Stage3-Yellow / 2025-01-23
- **Evidence:** Reuters/Yonhap/KiPost 2025-01-23: record Q4 profit; HBM became ~40% of DRAM revenue; AI memory demand expected to double.
- **Source URL:** https://www.reuters.com/technology/nvidia-supplier-sk-hynix-posts-record-quarterly-profit-2025-01-22/
- **Price path:** 180D MFE 128.70%, 180D MAE -25.88%, post-peak drawdown -6.77%.
- **E2R interpretation:** Stage3-Yellow candidate, not Green: excellent 180D MFE but 90D MAE and conventional-memory risk keep Green strict.

### 005930 Samsung Electronics — Stage4B / 2024-05-24
- **Evidence:** Reuters 2024-05-23/24: Samsung HBM3/HBM3E reportedly failed Nvidia qualification due to heat and power; Samsung denied specific failure framing but qualification lag was material.
- **Source URL:** https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/
- **Price path:** 180D MFE 17.00%, 180D MAE -34.26%, post-peak drawdown -43.81%.
- **E2R interpretation:** Stage4B watch: direct non-price negative evidence; not hard 4C because optimization/customer route remained alive.

### 005930 Samsung Electronics — Stage2 / 2025-01-31
- **Evidence:** Reuters 2025-01-31: Samsung memory recovery depended on whether 12-layer HBM3E could be supplied in volume to Nvidia; Q1 AI-chip sales expected slow.
- **Source URL:** https://www.reuters.com/technology/samsung-q4-profit-growth-slows-chip-issues-weigh-2025-01-31/
- **Price path:** 180D MFE 94.66%, 180D MAE -3.05%, post-peak drawdown -1.37%.
- **E2R interpretation:** Stage2 cap: huge later MFE, but at trigger date direct volume supply bridge was not confirmed.

### 009150 Samsung Electro-Mechanics — Stage2 / 2024-08-26
- **Evidence:** Samsung Electro-Mechanics 2024-08-26: high-performance FCBGA; share of high-value FCBGA for servers, AI, automotive, networks targeted above 50% by 2026.
- **Source URL:** https://m.samsungsem.com/global/newsroom/news/view.do?id=8382
- **Price path:** 180D MFE 3.88%, 180D MAE -26.84%, post-peak drawdown -27.37%.
- **E2R interpretation:** Stage2 cap: AI/server substrate profile, but no named HBM memory customer capacity conversion at trigger.

### 007660 ISU Petasys — Stage2-Actionable / 2024-09-24
- **Evidence:** ISU Petasys 2024 company IR: AI accelerator orders and customer progress, with customer E/B demand and 800G/switch order routes disclosed.
- **Source URL:** https://file.alphasquare.co.kr/media/pdfs/company-ir/20240924%EC%9D%B4%EC%88%98%ED%8E%98%ED%83%80%EC%8B%9C%EC%8A%A4_%ED%9A%8C%EC%82%AC%EC%86%8C%EA%B0%9C_%EB%B0%8F_%EC%A3%BC%EC%9A%94_%EA%B2%BD%EC%98%81%ED%98%84%ED%99%A9_%EC%84%A4%EB%AA%85.pdf
- **Price path:** 180D MFE 26.58%, 180D MAE -46.84%, post-peak drawdown -6.10%.
- **E2R interpretation:** Stage2-Actionable preserved but Yellow/Green blocked by deep 90D MAE and non-HBM memory issuer bridge.

### 222800 Simmtech — Stage4B / 2024-01-11
- **Evidence:** Simmtech 2024-01-11 report: memory-use substrates around 85% of revenue and recovery forecast, but no near-term customer capacity/order conversion in price path.
- **Source URL:** https://www.simmtech.com/upload/media/file/638406815140413547.pdf
- **Price path:** 180D MFE 1.80%, 180D MAE -56.44%, post-peak drawdown -57.22%.
- **E2R interpretation:** Stage4B / false-positive watch: forecast-only recovery with immediate peak and deep 180D MAE.

### 353200 Daeduck Electronics — Stage2 / 2024-06-24
- **Evidence:** Daeduck Electronics 2024-06-24/BusinessWire: large-body FCBGA substrate for AI servers/data centers, applicable to HPC/GPU/CoWoS-like packages.
- **Source URL:** https://www.businesswire.com/news/home/20240624950912/en/Daeduck-Electronics-Developed-Large-Body-FCBGA-Substrate-for-Data-Centers
- **Price path:** 180D MFE 18.91%, 180D MAE -39.15%, post-peak drawdown -48.83%.
- **E2R interpretation:** Stage2 cap: product development profile, not customer capacity/volume bridge.

## 6. Score / Return Alignment Stress Test
| ticker | trigger | role | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | total_proxy | price alignment |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 000660 | Stage2-Actionable | direct_positive_customer_capacity | 72 | 86 | 90 | 63 | 48 | 45 | 74 | 72.5 | mixed, keep capped |
| 000660 | Stage3-Yellow | direct_positive_revenue_mix | 84 | 88 | 87 | 65 | 60 | 55 | 80 | 80.0 | direct winner / Green still requires repeat bridge |
| 005930 | Stage4B | qualification_lag_counterexample | 48 | 42 | 35 | 56 | 44 | 45 | 76 | 49.5 | mixed, keep capped |
| 005930 | Stage2 | reopen_but_customer_dependency | 55 | 56 | 55 | 70 | 58 | 50 | 70 | 59.0 | direct winner / Green still requires repeat bridge |
| 009150 | Stage2 | package_substrate_sympathy_profile | 44 | 50 | 58 | 48 | 45 | 45 | 68 | 51.0 | weak forward reward |
| 007660 | Stage2-Actionable | ai_accelerator_customer_order_bridge | 62 | 73 | 68 | 60 | 52 | 45 | 70 | 65.0 | bad entry / escalation brake |
| 222800 | Stage4B | memory_substrate_forecast_false_positive | 35 | 42 | 45 | 45 | 40 | 45 | 65 | 43.0 | bad entry / escalation brake |
| 353200 | Stage2 | advanced_substrate_profile_not_customer_capacity | 42 | 46 | 55 | 50 | 45 | 45 | 66 | 49.0 | mixed, keep capped |

## 7. Residual Contribution
```text
rule_candidate: C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_AND_SYMPATHY_GATE_V1
sector_rule_candidate: L2_HBM_CUSTOMER_ALLOCATION_SECOND_BRIDGE_GATE

core_residual:
- HBM / AI memory / advanced substrate wording alone does not create Stage2-Actionable, Yellow, or Green.
- Stage2-Actionable requires at least one direct second bridge: named customer allocation, sold-out capacity, qualification pass, HBM shipment, HBM revenue mix, capacity expansion tied to customer demand, or realized margin conversion.
- Qualification lag with a live optimization/reopen path routes to Stage4B/watch, not sticky hard 4C.
- Package substrate / MLB / FCBGA / memory-substrate sympathy remains Stage2 cap unless the issuer has order, shipment, revenue, or margin conversion tied to HBM/AI customer capacity.
- High MAE on a direct bridge row blocks Yellow/Green first; it does not erase Stage2-Actionable.
- Stage3-Green remains blocked until HBM customer allocation and margin/cashflow conversion repeat across more than one evidence family.
```
## 8. Batch Ingest Self-Audit
```text
new_independent_case_count: 8
new_independent_trigger_count: 8
unique_symbol_count: 6

stage2_count: 3
stage2_actionable_count: 3
stage3_yellow_count: 1
stage4b_count: 1
stage4c_count: 0

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
missing_entry_price_count: 0
missing_actual_entry_ohlcv_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0

production_scoring_changed: false
shadow_weight_only: true
ready_for_batch_ingest: true
```
## 9. Machine-Readable JSONL Trigger Rows
```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_209_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 209, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_LAG_AND_PACKAGE_SYMPATHY_GATE_V1", "symbol": "000660", "name": "SK hynix", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-02", "entry_date": "2024-05-02", "entry_price": 173600.0, "entry_open": 169000.0, "entry_high": 174700.0, "entry_low": 169000.0, "entry_close": 173600.0, "entry_volume": 3168250, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "mfe_30d_pct": 32.2, "mae_30d_pct": -2.65, "mfe_90d_pct": 43.15, "mae_90d_pct": -13.31, "mfe_180d_pct": 43.15, "mae_180d_pct": -16.65, "peak_180d_date": "2024-07-11", "trough_180d_date": "2024-09-19", "post_peak_drawdown_180d_pct": -41.77, "case_role": "direct_positive_customer_capacity", "evidence_url": "https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-hbm-chips-almost-sold-out-2025-2024-05-02/", "evidence_summary": "Reuters 2024-05-02: HBM sold out for 2024 and almost sold out for 2025; HBM3E samples and Q3 mass production schedule.", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "component_proxy": {"eps_fcf": 72, "visibility": 86, "bottleneck": 90, "mispricing": 63, "valuation": 48, "capital": 45, "info": 74, "total_proxy": 72.5}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_209_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 209, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_LAG_AND_PACKAGE_SYMPATHY_GATE_V1", "symbol": "000660", "name": "SK hynix", "trigger_type": "Stage3-Yellow", "trigger_date": "2025-01-23", "entry_date": "2025-01-23", "entry_price": 219500.0, "entry_open": 221000.0, "entry_high": 225500.0, "entry_low": 215000.0, "entry_close": 219500.0, "entry_volume": 5994781, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "mfe_30d_pct": 3.42, "mae_30d_pct": -17.4, "mfe_90d_pct": 9.79, "mae_90d_pct": -25.88, "mfe_180d_pct": 128.7, "mae_180d_pct": -25.88, "peak_180d_date": "2025-10-21", "trough_180d_date": "2025-04-09", "post_peak_drawdown_180d_pct": -6.77, "case_role": "direct_positive_revenue_mix", "evidence_url": "https://www.reuters.com/technology/nvidia-supplier-sk-hynix-posts-record-quarterly-profit-2025-01-22/", "evidence_summary": "Reuters/Yonhap/KiPost 2025-01-23: record Q4 profit; HBM became ~40% of DRAM revenue; AI memory demand expected to double.", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "component_proxy": {"eps_fcf": 84, "visibility": 88, "bottleneck": 87, "mispricing": 65, "valuation": 60, "capital": 55, "info": 80, "total_proxy": 80.0}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_209_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 209, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_LAG_AND_PACKAGE_SYMPATHY_GATE_V1", "symbol": "005930", "name": "Samsung Electronics", "trigger_type": "Stage4B", "trigger_date": "2024-05-24", "entry_date": "2024-05-24", "entry_price": 75900.0, "entry_open": 76800.0, "entry_high": 77000.0, "entry_low": 75700.0, "entry_close": 75900.0, "entry_volume": 27891278, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "mfe_30d_pct": 14.76, "mae_30d_pct": -3.16, "mfe_90d_pct": 17.0, "mae_90d_pct": -21.61, "mfe_180d_pct": 17.0, "mae_180d_pct": -34.26, "peak_180d_date": "2024-07-11", "trough_180d_date": "2024-11-14", "post_peak_drawdown_180d_pct": -43.81, "case_role": "qualification_lag_counterexample", "evidence_url": "https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/", "evidence_summary": "Reuters 2024-05-23/24: Samsung HBM3/HBM3E reportedly failed Nvidia qualification due to heat and power; Samsung denied specific failure framing but qualification lag was material.", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "component_proxy": {"eps_fcf": 48, "visibility": 42, "bottleneck": 35, "mispricing": 56, "valuation": 44, "capital": 45, "info": 76, "total_proxy": 49.5}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_209_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 209, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_LAG_AND_PACKAGE_SYMPATHY_GATE_V1", "symbol": "005930", "name": "Samsung Electronics", "trigger_type": "Stage2", "trigger_date": "2025-01-31", "entry_date": "2025-01-31", "entry_price": 52400.0, "entry_open": 52200.0, "entry_high": 53000.0, "entry_low": 51700.0, "entry_close": 52400.0, "entry_volume": 42186279, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "mfe_30d_pct": 12.79, "mae_30d_pct": -3.05, "mfe_90d_pct": 18.32, "mae_90d_pct": -3.05, "mfe_180d_pct": 94.66, "mae_180d_pct": -3.05, "peak_180d_date": "2025-10-27", "trough_180d_date": "2025-02-03", "post_peak_drawdown_180d_pct": -1.37, "case_role": "reopen_but_customer_dependency", "evidence_url": "https://www.reuters.com/technology/samsung-q4-profit-growth-slows-chip-issues-weigh-2025-01-31/", "evidence_summary": "Reuters 2025-01-31: Samsung memory recovery depended on whether 12-layer HBM3E could be supplied in volume to Nvidia; Q1 AI-chip sales expected slow.", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "component_proxy": {"eps_fcf": 55, "visibility": 56, "bottleneck": 55, "mispricing": 70, "valuation": 58, "capital": 50, "info": 70, "total_proxy": 59.0}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_209_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 209, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_LAG_AND_PACKAGE_SYMPATHY_GATE_V1", "symbol": "009150", "name": "Samsung Electro-Mechanics", "trigger_type": "Stage2", "trigger_date": "2024-08-26", "entry_date": "2024-08-26", "entry_price": 144200.0, "entry_open": 144000.0, "entry_high": 145700.0, "entry_low": 143500.0, "entry_close": 144200.0, "entry_volume": 230543, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "mfe_30d_pct": 1.18, "mae_30d_pct": -12.62, "mfe_90d_pct": 1.18, "mae_90d_pct": -26.84, "mfe_180d_pct": 3.88, "mae_180d_pct": -26.84, "peak_180d_date": "2025-02-17", "trough_180d_date": "2024-11-15", "post_peak_drawdown_180d_pct": -27.37, "case_role": "package_substrate_sympathy_profile", "evidence_url": "https://m.samsungsem.com/global/newsroom/news/view.do?id=8382", "evidence_summary": "Samsung Electro-Mechanics 2024-08-26: high-performance FCBGA; share of high-value FCBGA for servers, AI, automotive, networks targeted above 50% by 2026.", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "component_proxy": {"eps_fcf": 44, "visibility": 50, "bottleneck": 58, "mispricing": 48, "valuation": 45, "capital": 45, "info": 68, "total_proxy": 51.0}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_209_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 209, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_LAG_AND_PACKAGE_SYMPATHY_GATE_V1", "symbol": "007660", "name": "ISU Petasys", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-24", "entry_date": "2024-09-24", "entry_price": 39500.0, "entry_open": 39300.0, "entry_high": 39500.0, "entry_low": 37800.0, "entry_close": 39500.0, "entry_volume": 1205008, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "mfe_30d_pct": 17.72, "mae_30d_pct": -22.78, "mfe_90d_pct": 17.72, "mae_90d_pct": -46.84, "mfe_180d_pct": 26.58, "mae_180d_pct": -46.84, "peak_180d_date": "2025-06-24", "trough_180d_date": "2024-11-18", "post_peak_drawdown_180d_pct": -6.1, "case_role": "ai_accelerator_customer_order_bridge", "evidence_url": "https://file.alphasquare.co.kr/media/pdfs/company-ir/20240924%EC%9D%B4%EC%88%98%ED%8E%98%ED%83%80%EC%8B%9C%EC%8A%A4_%ED%9A%8C%EC%82%AC%EC%86%8C%EA%B0%9C_%EB%B0%8F_%EC%A3%BC%EC%9A%94_%EA%B2%BD%EC%98%81%ED%98%84%ED%99%A9_%EC%84%A4%EB%AA%85.pdf", "evidence_summary": "ISU Petasys 2024 company IR: AI accelerator orders and customer progress, with customer E/B demand and 800G/switch order routes disclosed.", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "component_proxy": {"eps_fcf": 62, "visibility": 73, "bottleneck": 68, "mispricing": 60, "valuation": 52, "capital": 45, "info": 70, "total_proxy": 65.0}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_209_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 209, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_LAG_AND_PACKAGE_SYMPATHY_GATE_V1", "symbol": "222800", "name": "Simmtech", "trigger_type": "Stage4B", "trigger_date": "2024-01-11", "entry_date": "2024-01-11", "entry_price": 38800.0, "entry_open": 39250.0, "entry_high": 39500.0, "entry_low": 38600.0, "entry_close": 38800.0, "entry_volume": 354220, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "mfe_30d_pct": 1.8, "mae_30d_pct": -24.87, "mfe_90d_pct": 1.8, "mae_90d_pct": -28.61, "mfe_180d_pct": 1.8, "mae_180d_pct": -56.44, "peak_180d_date": "2024-01-11", "trough_180d_date": "2024-09-09", "post_peak_drawdown_180d_pct": -57.22, "case_role": "memory_substrate_forecast_false_positive", "evidence_url": "https://www.simmtech.com/upload/media/file/638406815140413547.pdf", "evidence_summary": "Simmtech 2024-01-11 report: memory-use substrates around 85% of revenue and recovery forecast, but no near-term customer capacity/order conversion in price path.", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "component_proxy": {"eps_fcf": 35, "visibility": 42, "bottleneck": 45, "mispricing": 45, "valuation": 40, "capital": 45, "info": 65, "total_proxy": 43.0}}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_209_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md", "selected_round": "R2", "selected_loop": 209, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "C06_HBM_CUSTOMER_CAPACITY_QUALIFICATION_LAG_AND_PACKAGE_SYMPATHY_GATE_V1", "symbol": "353200", "name": "Daeduck Electronics", "trigger_type": "Stage2", "trigger_date": "2024-06-24", "entry_date": "2024-06-24", "entry_price": 21150.0, "entry_open": 21700.0, "entry_high": 21900.0, "entry_low": 20950.0, "entry_close": 21150.0, "entry_volume": 380841, "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "mfe_30d_pct": 18.91, "mae_30d_pct": -0.95, "mfe_90d_pct": 18.91, "mae_90d_pct": -26.48, "mfe_180d_pct": 18.91, "mae_180d_pct": -39.15, "peak_180d_date": "2024-07-11", "trough_180d_date": "2024-12-09", "post_peak_drawdown_180d_pct": -48.83, "case_role": "advanced_substrate_profile_not_customer_capacity", "evidence_url": "https://www.businesswire.com/news/home/20240624950912/en/Daeduck-Electronics-Developed-Large-Body-FCBGA-Substrate-for-Data-Centers", "evidence_summary": "Daeduck Electronics 2024-06-24/BusinessWire: large-body FCBGA substrate for AI servers/data centers, applicable to HPC/GPU/CoWoS-like packages.", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false, "source_proxy_only": false, "evidence_url_pending": false, "production_scoring_changed": false, "shadow_weight_only": true, "component_proxy": {"eps_fcf": 42, "visibility": 46, "bottleneck": 55, "mispricing": 50, "valuation": 45, "capital": 45, "info": 66, "total_proxy": 49.0}}
```
## 10. Deferred Coding Agent Handoff Prompt
```text
Do not execute during this research session. Later, if batch promotion is requested, parse this MD as a v12 result file, validate all JSONL trigger rows, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and consider only scope-limited shadow rules for C06/L2. Do not loosen Stage3-Green globally. Preserve production_scoring_changed=false for this handoff unless a separate coding session explicitly applies reviewed patch specs.
```
## 11. Next Research State
```text
completed_round: R2
completed_loop: 209
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 URL/proxy quality + Priority 1 balance reinforcement
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_4C_DIRECT_ROW_REPAIR
- C06_HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_PASS_DIRECT_REVENUE_REPAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
