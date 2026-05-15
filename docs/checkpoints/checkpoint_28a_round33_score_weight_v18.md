# Checkpoint 28A Round 33: Score-Weight v1.8 Calibration

## Scope

Round 33 반영은 production scoring 변경이 아니라 calibration/evaluation 자료 확장이다.

추가 범위:

- `MEDIA_AD_CONTENT_CYCLE`
- `PAPER_PACKAGING_CYCLE`
- `SMART_FARM_AGRI_TECH`
- `CONSUMER_REGULATED_PRODUCT`
- `APPAREL_FAST_FASHION`
- `AI_SOFTWARE_APPLICATION`
- `METAVERSE_NFT_THEME`
- `FOOD_AGRI_LIVESTOCK_CYCLE`

## Outputs

- `src/e2r/sector/round33_score_weight_v18.py`
- `src/e2r/cli/build_round33_score_weight_report.py`
- `tests/test_round33_score_weight_v18.py`
- `data/e2r_case_library/cases_v15_round33.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round33_v18.csv`
- `output/e2r_round33_score_weight_v18/`

## Summary

- target_count: 8
- case_candidate_count: 32
- success_candidate_count: 10
- stage4c_case_count: 6
- green_possible_count: 1
- watch_yellow_first_count: 4
- redteam_first_count: 3
- production_scoring_changed: false
- case_records_are_candidate_generation_input: false

## Key Calibration Notes

- 광고/미디어는 스트리밍 광고 플랫폼처럼 반복 광고 inventory와 ARPU/OPM이 있으면 후보가 될 수 있지만, 전통 방송/광고대행 cycle은 보수적으로 본다.
- 제지/포장재는 가격인상과 FCF가 있어야 Stage 2 후보이며, 성숙 산업/과잉경쟁/원가 리스크 때문에 Green은 제한한다.
- 스마트팜은 실제 수주, 운영계약, 반복 서비스가 있어야 후보이고 보조금/기술장벽만으로는 부족하다.
- 규제형 소비재는 승인 뉴스가 Stage 1/2 신호일 수 있지만, 실제 허가, 매출, 마진, 법적 안정성 전까지 Green으로 보지 않는다.
- 의류/fast fashion은 재고 회전과 채널 확장이 있어도 IP, 제품안전, 규제, markdown 리스크를 강하게 본다.
- AI 소프트웨어는 반복 구독/API 매출과 compute cost 통제가 있어야 하며 저작권, 라이선스, 데이터 프라이버시는 hard gate다.
- NFT/메타버스와 농축산 질병/날씨 이벤트는 대부분 RedTeam-first다.

## Guardrails

- 케이스 ID와 종목명은 candidate-generation input이 아니다.
- 점수비중 v1.8은 production scoring에 적용하지 않았다.
- stage date, 가격, 광고 ARPU, 포장재 가격인상, 스마트팜 계약, 규제 승인, 재고 회전, AI 구독 매출, 라이선스 상태, NFT 거래량, 질병 정상화는 추정해서 채우지 않았다.
- Stage 3-Green 기준은 낮추지 않았다.

## Verification

```bash
PYTHONPATH=src python -m unittest tests.test_round33_score_weight_v18 -v
PYTHONPATH=src python -m compileall -q src tests
PYTHONPATH=src python -m e2r.cli.build_round33_score_weight_report
```

Round 33 전용 테스트는 통과했다.
