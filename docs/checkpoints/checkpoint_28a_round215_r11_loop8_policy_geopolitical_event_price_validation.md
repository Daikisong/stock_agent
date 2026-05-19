# Checkpoint 28A Round 215 R11 Loop 8 Policy Geopolitical Event Price Validation

## 목적

라운드215는 R11 정책·지정학·재난·이벤트 가격경로 검증 팩이다.

핵심 원칙은 단순하다. `정책 뉴스`, `지정학 이벤트`, `자원 발견 가능성`, `MOU`, `질병 수급 이벤트`, `과학 preprint`는 Stage 1~2나 event premium을 만들 수 있다. 하지만 Stage 3-Green은 계약, 예산, financing, 발주, 매출 전환, margin, EPS/FCF revision이 확인된 뒤에만 가능하다.

예를 들면 한국가스공사가 동해 가스 시추 승인 뉴스로 장중 30% 올라도, 시추 결과와 경제성, 상업생산 계획, 매출 전환 전에는 Green이 아니다.

## 반영 내용

- `src/e2r/sector/round215_r11_loop8_policy_geopolitical_event_price_validation.py` 추가
- `src/e2r/cli/build_round215_r11_loop8_report.py` 추가
- `tests/test_round215_r11_loop8_policy_geopolitical_event_price_validation.py` 추가
- R11 Loop 8 케이스 7개를 calibration-only case record로 구조화
- `NUCLEAR_POLICY_TO_CONTRACT`, `SMR_AI_POWER_POLICY_EVENT`, `GEOPOLITICAL_SHIPBUILDING_POLICY`, `US_SHIPBUILDING_REBUILD_POLICY` canonical archetype enum 보강
- Reuters / WSJ / AP / arXiv의 reported anchor로 계산 가능한 값만 반영
- production scoring과 candidate generation은 변경하지 않음

## 케이스 요약

| case | 판단 | Stage 3 처리 |
|---|---|---|
| 한국가스공사 | 동해 가스 resource event premium | 시추·경제성·상업성 전 Green 금지 |
| 두산에너빌리티 | 원전 policy-to-contract Stage 2 | 장비 수주잔고·마진·EPS revision 전 보류 |
| HD현대중공업/미포 | MASGA·합병·미국 조선정책 Stage 2 + 4B-watch | funded order·margin 전 보류 |
| Poultry basket | 조류독감 수입제한 one-off event | 수입제한 완화가 event fade trigger |
| LK-99 basket | speculative science overheat / thesis break | 독립 재현 실패는 4C |
| 계엄·정치 shock | macro RedTeam overlay | 개별 기업 Stage 3 신호로 사용 금지 |
| 공매도/MSCI | market-structure Stage 2 overlay | 외국인 유입·거래대금·증권사 이익 전 보류 |

## Green Gate

R11 Stage 3-Green 필수 조건:

- event_escalated_to_company_contract
- funded_budget_or_contract_amount
- financing_secured
- procurement_award_or_actual_order
- revenue_conversion_visible
- margin_or_eps_fcf_revision_visible
- repeat_demand_not_event_fade
- price_path_after_evidence

Green 금지 패턴:

- policy_news_only
- mou_only
- geopolitical_headline_only
- resource_estimate_without_drilling
- disease_import_ban_only
- preprint_or_science_claim_only
- government_announcement_basket_rally_only
- market_structure_reform_without_earnings
- price_rally_before_contract
- event_fade_risk

## 4B / 4C 보정

4B-watch는 뉴스 발표 당일 급등, 정책·MOU·자원발견 테마주 동반 급등, 과학 preprint 후 관련주 급등, 질병·재난 이벤트 급등, MOU가 계약처럼 가격에 반영되는 경우에 붙인다.

Hard 4C는 시추 실패, 경제성 부재, MOU 불발, 예산 미반영, 정책 후퇴, 수입제한 완화, 과학 claim 재현 실패, regulatory reversal, 정치 shock, 제도개선 기대 실패, contract cancellation, financing failure처럼 event thesis가 꺾일 때만 확정한다.

## 산출물

- `data/e2r_case_library/cases_r11_loop8_round215.jsonl`
- `data/sector_taxonomy/round215_r11_loop8_policy_geopolitical_event_price_validation_audit.json`
- `output/e2r_round215_r11_loop8_policy_geopolitical_event_price_validation/round215_r11_loop8_price_validation_summary.md`
- `output/e2r_round215_r11_loop8_policy_geopolitical_event_price_validation/round215_r11_loop8_case_matrix.csv`
- `output/e2r_round215_r11_loop8_policy_geopolitical_event_price_validation/round215_r11_loop8_score_adjustments.csv`
- `output/e2r_round215_r11_loop8_policy_geopolitical_event_price_validation/round215_r11_loop8_shadow_weights.csv`
- `output/e2r_round215_r11_loop8_policy_geopolitical_event_price_validation/round215_r11_loop8_deep_sub_archetypes.csv`
- `output/e2r_round215_r11_loop8_policy_geopolitical_event_price_validation/round215_r11_loop8_green_gate_review.md`
- `output/e2r_round215_r11_loop8_policy_geopolitical_event_price_validation/round215_r11_loop8_stage4b_4c_review.md`

이번 추가 패치는 원문 후반의 `shadow weight row 초안`과 `deep sub-archetype` 목록을 별도 산출물로 남긴다. 예를 들면 `NUCLEAR_POLICY_TO_CONTRACT`는 실제 계약과 예산이 붙으면 점수를 올릴 수 있지만, `EVENT_DISEASE_PEST_DEMAND`는 event fade 위험 때문에 감점축을 강하게 둔다.

## 검증

라운드215 전용 테스트와 전체 테스트를 실행한다.

```bash
PYTHONPATH=src python -m unittest tests.test_round215_r11_loop8_policy_geopolitical_event_price_validation -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m unittest discover -s tests -v
```

## 결론

라운드215는 R11의 기본값을 Stage 3-Green이 아니라 event premium으로 둔다. 정책·지정학·재난 뉴스가 커도 계약·예산·financing·발주·매출·EPS/FCF로 승격되기 전에는 Green으로 올리지 않는다.
