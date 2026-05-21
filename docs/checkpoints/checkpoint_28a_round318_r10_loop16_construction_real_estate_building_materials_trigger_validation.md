# Checkpoint 28A Round 318 R10 Loop 16 Trigger Validation

`docs/round/round_318.md`의 R10 Loop 16 건설·부동산·건자재 trigger-level validation을 calibration-only 자료로 반영했다.

## 반영 내용

- 신규 canonical archetype 7개를 추가하고 기존 `CONSTRUCTION_SAFETY_HARD_4C`와 함께 R10 Loop 16 target alias 8개를 매핑했다.
- Samsung E&A Fadhili, Hyundai E&C Jafurah, PF/Taeyoung, Seoul housing supply/reconstruction, Hyundai Engineering bridge safety, Samsung C&T P5, steel plate anti-dumping, BOK rate-cut/housing macro 케이스를 추가했다.
- full adjusted OHLC가 없으므로 reported event anchor만 저장하고, MFE/MAE는 `price_data_unavailable_after_deep_search`로 분리했다.
- production scoring, staging, candidate generation은 변경하지 않았다.

## 핵심 판정

- Samsung E&A / Fadhili: 계약금액과 +8.5% 이벤트 반응이 닫힌 가장 선명한 Stage2-Actionable EPC 사례다.
- Hyundai E&C / Jafurah: Aramco mega gas EPC 규모는 Stage2지만, 현대건설 몫·마진·현금흐름·가격 anchor가 없어 Green이 아니다.
- PF / Taeyoung: 정책 지원은 relief지만, PF write-off/refinancing/pre-sale 회복 전에는 4C-watch다.
- Seoul housing supply/reconstruction: 공급·재건축 완화는 Stage2지만, LTV 50%에서 40%로 tightening된 demand-control은 4B다.
- Construction safety: 사망사고는 license/fine/work suspension으로 이어질 수 있어 hard 4C다.
- Samsung C&T / P5: AI fab construction backlog는 Stage2지만, 수주금액·마진·일정·cash collection이 Green gate다.
- Steel plate anti-dumping: 철강사는 Stage2 relief일 수 있지만, 건설사는 input-cost 4B가 될 수 있다.
- BOK rate-cut: PF refinancing relief 가능성은 Stage2지만, 주택 과열·원화 약세·건설경기 둔화가 4B다.

쉬운 예시: 철강 반덤핑은 현대제철에는 좋은 뉴스일 수 있지만, 건설사에는 철강 투입비 상승이 될 수 있다. 그래서 같은 이벤트도 supplier와 builder를 같은 방향으로 점수화하면 안 된다.

## 산출물

- `src/e2r/sector/round318_r10_loop16_construction_real_estate_building_materials_trigger_validation.py`
- `src/e2r/cli/build_round318_r10_loop16_report.py`
- `tests/test_round318_r10_loop16_construction_real_estate_building_materials_trigger_validation.py`
- `data/e2r_case_library/cases_r10_loop16_round246.jsonl`
- `data/e2r_trigger_calibration/triggers_r10_loop16_round246.jsonl`
- `data/sector_taxonomy/round318_r10_loop16_construction_real_estate_building_materials_trigger_validation_audit.json`
- `data/sector_taxonomy/score_weight_profiles_round246_r10_loop16_v1.csv`
- `output/e2r_round318_r10_loop16_construction_real_estate_building_materials_trigger_validation/`

## 검증

```bash
PYTHONPATH=src python -m e2r.cli.build_round318_r10_loop16_report
PYTHONPATH=src python -m unittest tests.test_round318_r10_loop16_construction_real_estate_building_materials_trigger_validation -v
```

## 바꾸지 않은 것

- production scoring 변경 없음
- StageClassifier threshold 변경 없음
- case library를 candidate generation input으로 사용하지 않음
- Stage3-Green 강제 승격 없음
- full OHLC 없이 MFE/MAE를 만들지 않음
