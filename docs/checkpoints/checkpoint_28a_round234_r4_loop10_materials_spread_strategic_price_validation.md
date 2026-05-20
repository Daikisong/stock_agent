# Checkpoint 28A Round 234 R4 Loop 10 Materials Spread Strategic Resources Price Validation

## 반영 내용

- `docs/round/round_234.md`의 R4 Loop 10 라운드를 calibration-only 검증팩으로 구조화했다.
- 전략광물, 석유화학 구조조정, 정유 스프레드, 리튬 resource security, 철강 policy CAPEX, 소재계약 quality break, 비중국 polysilicon, 구리/방산 M&A optionality를 비교했다.
- Reuters/FT/MarketWatch류 reported anchor에서 확인된 프로젝트 규모, 계약 붕괴, 이벤트 수익률, 설비중단, 실적 beat/miss 수치만 저장했다.
- 원시 수정주가 OHLC가 없는 항목은 `price_data_unavailable_after_deep_search` 또는 `reported_*_not_full_ohlc`로 명시했다.
- production scoring과 candidate generation은 변경하지 않았다.

## 핵심 케이스

- Korea Zinc: $7.4B Tennessee critical-minerals refinery, 540,000 tons output, 11 critical minerals, 2025 OP 1.2T KRW는 Stage 2 후보지만, $1.9B share issue, governance battle, -13% injunction shock 때문에 Green은 보류했다.
- Lotte Chemical / HD Hyundai Chemical: Daesan NCC 1.1M tpy 3년 shutdown, 1.2T KRW 증자, 2T KRW 이상 지원은 restructuring relief지만 spread, OPM, FCF 전에는 Green이 아니다.
- SK Innovation / S-Oil: Q1 2026 OP 2.2T KRW와 estimate beat +57.1%는 강하지만 refining은 cycle이고 SK On loss drag가 남아 Stage 2 watch로 남겼다.
- POSCO / MinRes lithium JV: $765M deal과 Wodgina/Mt Marion indirect 15% stake는 resource-security Stage 2지만, spodumene이 2022 peak 대비 여전히 -85% 이상 낮아 downstream margin 확인이 필요하다.
- Hyundai Steel: $5.8B-$6.0B Louisiana plant와 tariff hedge narrative는 당일 +5% 후 -4.4%, 이후 -21.2% drawdown으로 policy CAPEX false-positive 방지 사례로 저장했다.
- L&F: Tesla 4680 cathode contract value가 $2.9B에서 $7,386으로 붕괴한 hard 4C anchor로 추가했다.
- OCI Holdings: Texas $1.2B expansion과 10GW by 2027은 Stage 2지만, SpaceX supply talk는 unconfirmed media report라 event premium/4B-watch로 분리했다.
- Poongsan: Hanwha acquisition rumor는 1.5T KRW 규모로 보도됐지만 6일 만에 fade되어 M&A optionality event premium으로 처리했다.

## Green Gate 보강

R4 Stage 3-Green은 단순히 `전략자원`, `리튬`, `구조조정`, `관세 hedge`, `미확정 고객 보도`가 아니다.

예를 들어, `Tesla 고객명 + 대형 계약금액`은 좋아 보일 수 있지만 실제 call-off와 계약 가치가 무너지면 hard 4C다. 반대로 refinery나 lithium price rally처럼 가격이 움직여도 FCF와 margin이 잠기지 않으면 cycle/event premium으로 먼저 본다.

필수 조건:

- actual product spread
- cost curve advantage
- supply discipline 또는 capacity shutdown 확인
- inventory build 부재
- FCF after working capital
- price floor 또는 offtake
- medium-term EPS revision
- capex/dilution risk 통과
- policy/tariff/sanction stress 통과
- evidence 이후 price path 확인

금지 조건:

- commodity price spike only
- strategic material headline only
- tender offer premium
- governance battle only
- policy support without FCF
- unconfirmed media report
- M&A rumor without transaction
- restructuring plan without margin
- lithium/polysilicon price event only
- customer name or contract headline without call-off

## 산출물

- `data/e2r_case_library/cases_r4_loop10_round234.jsonl`
- `data/sector_taxonomy/round234_r4_loop10_materials_spread_strategic_price_validation_audit.json`
- `output/e2r_round234_r4_loop10_materials_spread_strategic_price_validation/round234_r4_loop10_price_validation_summary.md`
- `output/e2r_round234_r4_loop10_materials_spread_strategic_price_validation/round234_r4_loop10_case_matrix.csv`
- `output/e2r_round234_r4_loop10_materials_spread_strategic_price_validation/round234_r4_loop10_shadow_weights.csv`
- `output/e2r_round234_r4_loop10_materials_spread_strategic_price_validation/round234_r4_loop10_green_gate_review.md`
- `output/e2r_round234_r4_loop10_materials_spread_strategic_price_validation/round234_r4_loop10_stage4b_4c_review.md`
- `output/e2r_round234_r4_loop10_materials_spread_strategic_price_validation/round234_r4_loop10_price_validation_plan.md`

## 검증

- `PYTHONPATH=src python -m unittest tests/test_round234_r4_loop10_materials_spread_strategic_price_validation.py -v`
- `PYTHONPATH=src python -m e2r.cli.build_round234_r4_loop10_report`

## 다음 단계

- 원시 수정주가 OHLC를 확보하면 `reported_*_not_full_ohlc` 항목의 MFE/MAE를 정밀 backfill한다.
- R4 shadow weight는 아직 production scoring에 적용하지 않는다.
- 다음 shadow scoring 라운드에서는 `actual_product_spread`, `fcf_after_working_capital`, `offtake`, `contract_quality`, `governance_redteam`, `hard4c_sensitivity`를 비교 축으로 사용한다.
