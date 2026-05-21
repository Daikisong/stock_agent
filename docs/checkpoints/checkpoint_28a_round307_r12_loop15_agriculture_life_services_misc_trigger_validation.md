# Checkpoint 28A Round 307 R12 Loop 15 Trigger-level Calibration

## 반영 내용

- R12 농업·생활서비스·기타 trigger-level validation을 추가했다.
- Fertilizer export controls, feed wheat tender failure, AI digital textbook rollback, hagwon structural demand, Naver/Uber/Baemin M&A, Coupang data breach, Pinkfong IPO, plastic recycling policy false-positive를 구조화했다.
- full adjusted OHLC window는 확보하지 못했으므로 reported event return, IPO/debut price anchor, affected-user count, policy trigger, demand/price data를 별도 anchor로 저장했다.
- 생산 scoring, staging, candidate generation은 변경하지 않았다.

## 생성 파일

- `src/e2r/sector/round307_r12_loop15_agriculture_life_services_misc_trigger_validation.py`
- `src/e2r/cli/build_round307_r12_loop15_report.py`
- `tests/test_round307_r12_loop15_agriculture_life_services_misc_trigger_validation.py`
- `data/e2r_case_library/cases_r12_loop15_round235.jsonl`
- `data/e2r_trigger_calibration/triggers_r12_loop15_round235.jsonl`
- `data/sector_taxonomy/round307_r12_loop15_agriculture_life_services_misc_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round235_r12_loop15_v1.csv`
- `output/e2r_round307_r12_loop15_agriculture_life_services_misc_trigger_validation/`

## 핵심 보정

- 비료/농업 input shock은 국내 ASP, inventory, sales volume, margin pass-through가 없으면 Stage2 event에 머문다.
- AI textbook 같은 교육 policy는 school contract, paid adoption, teacher/parent acceptance가 없으면 Green 금지다.
- 생활서비스 platform은 data-security trust가 hard gate다.
- food-delivery M&A teaser는 binding offer, KFTC approval, take-rate economics 전에는 4B-watch다.
- Pinkfong 같은 IP/edutainment IPO는 recurring licensing, merchandise, next-IP revenue 전에는 one-hit-wonder 4B overlay가 필요하다.
- recycling policy는 official recycling-rate headline이 아니라 tipping fee, cleanup contract, utilization, treatment margin이 닫혀야 한다.

## Stage 판정

- Stage2 event candidates: `5`
- Stage2-Actionable candidates: `1`
- Stage3-Yellow candidates: `4`
- Stage3-Green confirmed: `0`
- Stage4B watch: `5`
- Stage4C watch: `5`
- hard 4C cases: `1`

## 쉬운 예시

비료 수출 제한은 화재경보기처럼 “봐야 한다”는 신호다. 하지만 국내 비료 회사가 실제로 더 높은 가격에 팔고, 재고가 있으며, 마진이 좋아졌다는 증거가 나오기 전에는 Stage3 증거가 아니다.

## 금지 사항

- Stage3-Green 기준을 낮추지 않는다.
- round307 case를 candidate-generation input으로 쓰지 않는다.
- M&A teaser, policy headline, supply shock, viral IP, recycling headline을 Green evidence로 쓰지 않는다.
- full adjusted OHLC가 없는데 MFE/MAE를 만들지 않는다.
