# Checkpoint 28A Round 202 R11 Loop 7 Policy Geopolitical Event Price Validation

## Scope

Round 202 반영 범위는 정책, 지정학, 재난, 질병, 과학 테마, 시장구조 이벤트의 가격경로 검증 팩이다.
이번 패치는 production scoring을 바꾸지 않고, case library와 shadow weight 검증 재료만 추가했다.

쉬운 예: `as_of_date=2024-06-03`에 동해 가스 뉴스로 한국가스공사가 급등해도, 시추 성공과 상업성이 아직 없으면 Stage 3-Green이 아니라 Stage 1 event premium과 4B-watch다.

## Added Files

- `src/e2r/sector/round202_r11_loop7_policy_geopolitical_event_price_validation.py`
- `src/e2r/cli/build_round202_r11_loop7_report.py`
- `tests/test_round202_r11_loop7_policy_geopolitical_event_price_validation.py`
- `data/e2r_case_library/cases_r11_loop7_round202.jsonl`
- `data/sector_taxonomy/round202_r11_loop7_policy_geopolitical_event_price_validation_audit.json`
- `output/e2r_round202_r11_loop7_policy_geopolitical_event_price_validation/`

## Case Pack

| case_id | company | archetype focus | role |
| --- | --- | --- | --- |
| `kogas_east_sea_resource_discovery_event_premium` | 한국가스공사 | domestic resource discovery | event premium / 4B-watch |
| `doosan_enerbility_nuclear_smr_policy_to_contract_watch` | 두산에너빌리티 | nuclear/SMR policy-to-contract | Stage 2 watch |
| `hdhyundai_samsungheavy_us_shipbuilding_policy_mou_watch` | HD현대 / 삼성중공업 | U.S. shipbuilding policy MOU | MOU-watch |
| `poultry_basket_brazil_bird_flu_import_ban_event_fade` | 하림 / 마니커류 poultry basket | disease import-ban demand | event premium / fade watch |
| `lk99_superconductor_speculative_science_thesis_break` | LK-99 초전도체 basket | speculative science | overheat / hard 4C |
| `korea_martial_law_policy_market_shock_overlay` | KOSPI / Korea market | political system shock | macro RedTeam overlay |
| `short_selling_msci_market_structure_stage2_watch` | broad market / securities basket | market structure reform | Stage 2 watch |

## Green Gate

Round 202의 핵심은 이벤트와 구조적 E2R을 분리하는 것이다.

Green에 필요한 필드는 다음과 같다.

- `company_level_contract_confirmed`
- `budget_or_contract_amount_confirmed`
- `financing_secured`
- `actual_order_or_procurement_award_confirmed`
- `revenue_conversion_confirmed`
- `margin_or_eps_fcf_revision_confirmed`
- `repeat_demand_not_event_fade_confirmed`
- `price_path_after_contract_evidence`

Green을 막는 패턴은 다음과 같다.

- 정책 뉴스만 있는 경우
- MOU만 있는 경우
- 지정학 headline만 있는 경우
- 시추 없는 자원 매장 가능성
- 과학 preprint 또는 claim만 있는 경우
- 질병·수입금지 이벤트만 있는 경우
- 시장구조 개선은 있지만 기업 이익이 없는 경우
- 계약 전 가격 급등
- 예산 미확보, 정책 후퇴, event fade 위험

## Stage 4B / 4C Notes

- 한국가스공사 동해 가스 이벤트는 자원 discovery headline이 가격을 먼저 움직인 4B-watch다.
- 두산에너빌리티 원전·SMR은 정책이 계약으로 승격되는지 보는 Stage 2 watch다.
- HD현대·삼성중공업 미국 조선정책 MOU는 funded order 전 Stage 3가 아니다.
- poultry basket은 질병·수입금지 이벤트의 단기 MFE를 볼 수 있지만, 수입제한 완화가 event fade가 될 수 있다.
- LK-99는 speculative science hard 반례다. preprint는 Stage 1이고 독립 재현 실패는 4C다.
- 계엄·정치 shock은 개별 기업 Green/Red를 직접 만들기보다 macro risk premium overlay로 둔다.
- 공매도·MSCI 접근성은 시장구조 개선이지만, 개별 기업 EPS/FCF 전 Green이 아니다.

## Outputs

Generated report files:

- `round202_r11_loop7_price_validation_summary.md`
- `round202_r11_loop7_case_matrix.csv`
- `round202_r11_loop7_target_aliases.csv`
- `round202_r11_loop7_score_adjustments.csv`
- `round202_r11_loop7_price_backfill_fields.csv`
- `round202_r11_loop7_green_gate_review.md`
- `round202_r11_loop7_price_backfill_plan.md`
- `round202_r11_loop7_stage4b_4c_review.md`

## Commands Run

```bash
PYTHONPATH=src python -m unittest tests.test_round202_r11_loop7_policy_geopolitical_event_price_validation -v
PYTHONPATH=src python -m e2r.cli.build_round202_r11_loop7_report
```

Full test suite was also run after the patch.

## What Not To Change

- Do not apply Round 202 score weights to production scoring yet.
- Do not use Round 202 cases as candidate-generation input.
- Do not lower Stage 3-Green thresholds to force promotion.
- Do not invent contract, budget, financing, order, revenue, EPS/FCF, stage prices, or MFE/MAE.
- Do not treat policy news, MOU, resource discovery, disease event, science preprint, or market-structure reform as Green evidence alone.

## Next

Next step is OHLC/price-path backfill with short event windows. R11은 5D/20D MFE와 30D/90D MAE가 중요하다. 예를 들면 LK-99나 동해 가스 이벤트는 장기 Stage 3 수익률보다 “초기 급등 후 얼마나 빨리 fade됐는지”가 더 중요한 검증 포인트다.
