# Checkpoint 28A Round 181 R10 Loop 11 Construction / Real Estate / Materials

## 반영 요약

- 입력 문서: `docs/round/round_181.md`
- 대섹터: `CONSTRUCTION_REAL_ESTATE_MATERIALS`
- 신규/보강 canonical target: 13개
- 케이스 후보: 13개
- 생산 scoring 변경: 없음
- case library의 candidate-generation 사용: 없음

## 핵심 원칙

건설·부동산·건자재는 “수주잔고”, “PF 지원”, “AI 데이터센터”, “고배당 리츠”, “시멘트 가격인상” 이름만으로 Stage 3를 줄 수 없다.

쉬운 예시는 이렇다.

- 삼성E&A Fadhili 수주: 계약금액과 고객명은 강한 Stage 2 증거지만, 원가율과 현금전환이 확인되기 전에는 Green이 아니다.
- 삼성물산 AI 데이터센터 option: OpenAI/AWS 한국 데이터센터 수요는 Stage 1~2 macro 증거지만, 실제 EPC 계약·tenant·NOI/AFFO가 없으면 Green이 아니다.
- 태영건설 PF workout: 정부 지원책이 있어도 debt rescheduling/workout은 hard 4C 기준점이다.
- HDC현대산업개발 광주 붕괴: 주택 경기나 브랜드 회복보다 안전·품질 hard gate가 먼저다.

## 추가 산출물

- `src/e2r/sector/round181_r10_loop11_construction_real_estate_materials.py`
- `src/e2r/cli/build_round181_r10_loop11_report.py`
- `tests/test_round181_r10_loop11_construction_real_estate_materials.py`
- `data/e2r_case_library/cases_r10_loop11_round181.jsonl`
- `data/sector_taxonomy/score_weight_profiles_round181_r10_loop11_v11.csv`
- `output/e2r_round181_r10_loop11_construction_real_estate_materials/`

## Stage Gate 보강

- Stage 1 cap: PF 지원, 금리인하, EPC 수주, AI 데이터센터, 재건정책, 시멘트 가격인상, 고배당 리츠 headline은 45점 cap.
- Stage 2 cap: 계약금액·고객명·완공시점·PF refinancing·tenant/occupancy·NOI/AFFO·가격전가 확인 전에는 70점 cap.
- Stage 3: 8개 조건 중 5개 이상 필요.
- Stage 4B: price가 narrative보다 먼저 가면 4B-watch.
- Stage 4C: PF workout, 대형 안전사고, 배당삭감, tenant 없음, 담합/과징금, 희석 이벤트는 hard gate.

## 검증

```bash
PYTHONPATH=src python -m unittest tests.test_round181_r10_loop11_construction_real_estate_materials -v
PYTHONPATH=src python -m e2r.cli.build_round181_r10_loop11_report
```

Round 181은 R10 건설·부동산·건자재 score 설계용 calibration pack이다. Production StageClassifier threshold는 변경하지 않았다.
