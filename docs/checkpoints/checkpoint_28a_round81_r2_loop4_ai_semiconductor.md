# Checkpoint 28A Round 81 - R2 Loop 4 AI / Semiconductor / Electronics

Round 81 반영 완료.

## Scope

- source round: `docs/round/round_81.md`
- large sector: `AI_SEMICONDUCTOR_ELECTRONICS`
- loop: `R2 Loop 4 / v4.0`
- production scoring changed: `false`
- case records are candidate-generation input: `false`

이번 라운드는 “AI 수혜”를 하나의 점수 버킷으로 보지 않고, HBM 선도, HBM 후발 catch-up, AI storage NAND, AI 장비 CAPEX, advanced packaging, optical networking, 서버 ODM, neocloud, cooling, AI accelerator를 서로 다른 경제구조로 분리했다.
쉬운 예로, HBM 선도 기업은 구조적 후보가 될 수 있지만, 후발 HBM 업체는 출하만으로 부족하고 고객 qualification, yield, volume shipment, 생산 실행력이 같이 확인되어야 한다.

## Targets

- target_count: 19
- green_possible_count: 4
- watch_yellow_first_count: 13
- redteam_first_count: 2
- hard_gate_target_count: 1

핵심 변경:

- `HBM_CATCHUP_EXECUTION`: 삼성·마이크론형 후발 HBM을 HBM 선도 archetype에서 분리.
- `AI_STORAGE_NAND_SHORTAGE`: Kioxia/SanDisk류 AI storage NAND shortage를 범용 DRAM/NAND cycle에서 분리.
- `SEMI_EQUIPMENT_AI_CAPEX`: 고객사 AI/HBM CAPEX가 장비 수주, backlog, OP/EPS로 전환되는지 별도 추적.
- `REDTEAM_ACCOUNTING_TRUST_OVERLAY`: Supermicro식 감사인 사임, 공시 지연, 내부통제 이슈는 hard gate로 유지.
- `AI_CAPEX_CROWDING_OVERLAY`: 실적이 좋아도 valuation이 이미 포화된 구간은 4B overlay로 분리.
- `INDUSTRIAL_GASES_SEMICONDUCTOR_INFRA`: Round 68의 반도체용 industrial gas 축은 문서 결론의 strong candidate 범주와 호환되므로 R2 pack에 유지했다.

## Case Pack

- case_candidate_count: 18
- structural_success_count: 1
- success_candidate_count: 9
- event_premium_count: 1
- overheat_count: 2
- failed_rerating_count: 2
- stage4b_case_count: 3
- stage4c_case_count: 1

대표 케이스:

- `sk_hynix_hbm_trillion_case`
- `samsung_hbm4_shipping_case`
- `samsung_amd_hbm4_mou_case`
- `samsung_labor_strike_execution_case`
- `kioxia_ai_nand_profit_case`
- `applied_materials_ai_packaging_growth_case`
- `nvidia_cowos_l_transition_case`
- `broadcom_optical_pcb_leadtime_case`
- `foxconn_ai_server_rack_growth_case`
- `ecolab_coolit_liquid_cooling_case`
- `coreweave_openai_contract_case`
- `coreweave_expanded_openai_contract_case`
- `coreweave_downsized_ipo_debt_case`
- `cerebras_ai_accelerator_ipo_case`
- `supermicro_ey_resignation_case`
- `cxl_glass_substrate_theme_case`
- `furiosa_ai_related_stock_case`

## Outputs

- `data/e2r_case_library/cases_r2_loop4_round81.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round81_r2_loop4_v4.csv`
- `output/e2r_round81_r2_loop4_ai_semiconductor/round81_r2_loop4_ai_semiconductor_summary.md`
- `output/e2r_round81_r2_loop4_ai_semiconductor/round81_r2_loop4_case_matrix.csv`
- `output/e2r_round81_r2_loop4_ai_semiconductor/round81_r2_loop4_stage_date_plan.csv`
- `output/e2r_round81_r2_loop4_ai_semiconductor/round81_r2_loop4_green_guardrails.md`
- `output/e2r_round81_r2_loop4_ai_semiconductor/round81_r2_loop4_risk_overlays.md`
- `output/e2r_round81_r2_loop4_ai_semiconductor/round81_r2_loop4_price_validation_plan.md`
- `output/e2r_round81_r2_loop4_ai_semiconductor/round81_r2_loop4_price_fields.csv`

## Guardrails

- Round81 case pack은 calibration/evaluation material이다.
- Case record를 후보 생성 input으로 쓰지 않는다.
- Stage 3-Green 기준은 낮추지 않는다.
- “AI 수혜”, CXL, 유리기판, 뉴로모픽, 퓨리오사AI 관련주 같은 키워드만으로 Green을 만들지 않는다.
- 예를 들어 `OpenAI contract`는 neocloud의 Stage 2 visibility 근거가 될 수 있지만, debt, FCF, GPU 감가상각, 고객집중이 해결되지 않으면 Green 근거로 쓰지 않는다.
- 감사인 사임, filing delay, 내부통제, 규제 조사, related-party risk는 AI 서버 매출 성장과 별개로 hard RedTeam이다.

## Verification

- `PYTHONPATH=src python -m unittest tests.test_round81_r2_loop4_ai_semiconductor -v`
- `PYTHONPATH=src python -m e2r.cli.build_round81_r2_loop4_report`
- `PYTHONPATH=src python -m compileall -q src tests`
- `PYTHONPATH=src python -m unittest discover -s tests -v`
- `git diff --check`
