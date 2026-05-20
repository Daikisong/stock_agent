# Checkpoint 28A Round 279 R10 Loop 13 Construction Real Estate Building Materials Price Validation

## 반영 범위

- source round: `docs/round/round_279.md`
- analyst round id: `round_207`
- large sector: `CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS`
- production scoring changed: `false`
- candidate generation input: `false`
- shadow weight only: `true`
- full adjusted OHLC complete: `false`

이번 라운드는 건설/부동산/PF/건자재를 “정책지원이나 수주 headline”이 아니라 실제 현금흐름으로 검증하도록 case library를 확장했다.

쉬운 예로, `40.6T KRW 건설사 지원책`은 산소 공급 같은 relief다. 환자가 회복됐다는 증거는 아니므로, PF 차환 성공, 분양률, 미분양 감소, 원가율, 현금회수까지 확인되어야 Green 후보가 된다.

## 추가한 canonical archetype

- `REAL_ESTATE_PF_LIQUIDITY_4C_WATCH`
- `OVERSEAS_EPC_MEGA_ORDER_STAGE2_NOT_GREEN`
- `NUCLEAR_INFRA_PREFERRED_BIDDER_STAGE2`
- `CONSTRUCTION_MATERIAL_DEMAND_BREAK`
- `SEOUL_PROPERTY_POLICY_EVENT_PREMIUM`
- `STEEL_PLATE_CONSTRUCTION_RELIEF_AND_EXPORT_RISK`
- `HOUSING_SUPPLY_RATE_CUT_POLICY_RELIEF`

기존 `CONSTRUCTION_SAFETY_HARD_REFERENCE`는 그대로 재사용했다.

## 추가한 case pack

- Real-estate PF / Taeyoung reference: PF 연체율 0.37% -> 2.70%, 40.6T KRW 지원, 1T -> 5T KRW syndicated loan. `4C-watch + policy relief`.
- Samsung E&A / GS E&C Fadhili: $7.7B 프로젝트, Samsung E&A 추정 $6B, 당일 +8.5%. `Stage 2 + 4B-watch`, Green은 EPC margin/working capital 확인 후.
- Czech nuclear infrastructure: preferred bidder, Doosan +48%, KEPCO E&C +41%, Westinghouse/EDF legal appeal. `Stage 2 + legal 4C-watch`.
- Hyundai Steel construction-material demand: rebar -10% 전망, net-profit estimate -73%, 이후 anti-dumping relief +5.8%. `evidence_good_but_price_failed`.
- Seoul property policy/rate-cut gate: 서울 가격 +0.38% MoM, 강남/서초/송파/용산 거래허가, 가계부채 1,927.3T KRW. `event premium + macroprudential watch`.
- Anseong highway construction collapse: 사망 3명, 부상 6명, 50m 구조물 5개 붕괴. 직접 상장사 hard 4C는 아니지만 sector safety hard reference.
- Korean builders liquidity package: 보증, 추가대출, market-stabilising fund. `policy relief`, Green 아님.
- Steel plate anti-dumping: 27.91~38.02% 관세, Hyundai Steel +5.8%, POSCO +3.9%. `event premium`, 실제 수요/spread/FCF 필요.

## Green gate 보강

R10 Stage 3-Green 필수 확인 항목:

- `PF_refinancing_success_confirmed`
- `project_profitability_filter_confirmed`
- `pre_sale_ratio_confirmed`
- `unsold_inventory_reduction_confirmed`
- `EPC_margin_visibility_confirmed`
- `working_capital_control_confirmed`
- `unbilled_receivables_control_confirmed`
- `final_contract_signed_confirmed`
- `legal_appeal_clearance_confirmed`
- `construction_safety_trust_confirmed`
- `building_material_demand_spread_confirmed`
- `price_path_after_evidence`

금지 패턴:

- `order_headline_only`
- `preferred_bidder_only`
- `policy_support_only`
- `tariff_relief_only`
- `rate_cut_property_expectation_only`
- `housing_price_rebound_without_cashflow`
- `PF_support_without_profitability`
- `EPC_backlog_without_margin`
- `safety_incident_unresolved`

## 4B / 4C 해석

- 해외 EPC 수주 당일 +5~10% 급등은 4B-watch다. 예: Samsung E&A Fadhili +8.5%.
- 원전 preferred bidder로 3개월 +40% 이상 움직이면 final contract 전 4B-watch다.
- PF default/workout, PF delinquency spike, fatal construction-site accident, legal appeal blocking contract, unbilled receivables surge는 4C gate다.
- 이번 round에서 direct listed hard 4C는 확정하지 않았고, Anseong 사고는 sector safety hard reference로만 둔다.

## 생성 파일

- `data/e2r_case_library/cases_r10_loop13_round279.jsonl`
- `data/sector_taxonomy/round279_r10_loop13_construction_real_estate_building_materials_price_validation_audit.json`
- `output/e2r_round279_r10_loop13_construction_real_estate_building_materials_price_validation/round279_r10_loop13_price_validation_summary.md`
- `output/e2r_round279_r10_loop13_construction_real_estate_building_materials_price_validation/round279_r10_loop13_case_matrix.csv`
- `output/e2r_round279_r10_loop13_construction_real_estate_building_materials_price_validation/round279_r10_loop13_shadow_weights.csv`
- `output/e2r_round279_r10_loop13_construction_real_estate_building_materials_price_validation/round279_r10_loop13_green_gate_review.md`
- `output/e2r_round279_r10_loop13_construction_real_estate_building_materials_price_validation/round279_r10_loop13_stage4b_4c_review.md`

## 검증

- `PYTHONPATH=src python -m unittest tests.test_round279_r10_loop13_construction_real_estate_building_materials_price_validation -v`

결과: 통과.

## 다음 작업

R11 Loop 13에서는 이 pack을 production scoring에 직접 적용하지 말고, shadow score에서 PF 차환/분양률/EPC margin/미청구공사/safety trust 축이 후보 stage를 어떻게 바꾸는지 먼저 비교해야 한다.
