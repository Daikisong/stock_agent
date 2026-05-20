# Checkpoint 28A Round 289 R7 Loop 14 Bio Healthcare Medical Device Price Validation

## 반영 내용

- `docs/round/round_289.md`의 R7 Loop 14 바이오·헬스케어·의료기기 가격경로 검증 라운드를 case-library pack으로 반영했다.
- Samsung Biologics, Celltrion, SK Bioscience, Alteogen, Yuhan, Hugel, ADEL, global clinical/FDA failure reference를 분리했다.
- 생산 scoring, candidate generation, StageClassifier threshold는 바꾸지 않았다.
- full adjusted OHLC가 없는 구간은 `price_data_unavailable_after_deep_search` 또는 `partial_reported_anchor`로 남겼다.

## 핵심 교정

바이오 R7에서는 `FDA 승인`, `CMO 공장`, `기술수출`, `미국 출시` 같은 단어를 바로 Green으로 쓰면 안 된다. 예를 들어 Samsung Biologics의 미국 공장 인수는 좋은 Stage 2 증거지만, 실제 가동률과 batch margin이 확인되기 전에는 Green 증거가 아니다.

강화한 shadow evidence:

- FDA approval-to-launch conversion
- royalty / milestone probability
- facility utilization
- FDA inspection and tech transfer
- CMO recurring order visibility
- clinical endpoint quality
- partner execution quality
- patent / IP freedom-to-operate
- reimbursement and market access
- physician adoption and sell-through

감점해야 할 패턴:

- FDA headline only
- facility acquisition only
- CMO capacity without utilization
- tech-export upfront only
- early-stage deal without Phase 2/3
- approval without reimbursement
- aesthetic launch without doctor adoption
- unresolved patent dispute
- clinical hold or CRL

## Case Summary

- Samsung Biologics: `evidence_good_but_price_failed`. $280M U.S. facility 인수와 60,000L capacity가 있었지만 보도 anchor 기준 주가는 -0.4%, KOSPI는 +2.0%였다.
- Celltrion: U.S. factory tariff hedge Stage 2. Product transfer, utilization, market share, margin이 필요하다.
- SK Bioscience: IDT Biologika M&A event premium. +11.7% price anchor는 있으나 backlog와 plant utilization이 필요하다.
- Alteogen: Keytruda Qlex 관련 strongest structural candidate. FDA approval과 30~40% adoption target은 강하지만 royalty conversion과 patent/IP gate가 남아 있다.
- Yuhan: oncology license Stage 2. Rybrevant + lazertinib approval은 좋지만 launch uptake, royalty economics, manufacturing gate가 필요하다.
- Hugel: Letybo U.S. launch Stage 2. Physician adoption, distributor margin, safety compliance가 필요하다.
- ADEL / Sanofi: unlisted Korean biotech tech-export Stage 2 reference. Upfront와 총 deal value만으로 listed Green read-through를 만들지 않는다.
- Global clinical/FDA failure reference: HilleVax, Corcept, PepGen 사례를 sector hard 4C reference로 둔다. 직접 KRX hard 4C는 확정하지 않았다.

## 산출물

- `src/e2r/sector/round289_r7_loop14_biotech_healthcare_device_price_validation.py`
- `src/e2r/cli/build_round289_r7_loop14_report.py`
- `tests/test_round289_r7_loop14_biotech_healthcare_device_price_validation.py`
- `data/e2r_case_library/cases_r7_loop14_round289.jsonl`
- `data/sector_taxonomy/round289_r7_loop14_biotech_healthcare_device_price_validation_audit.json`
- `output/e2r_round289_r7_loop14_biotech_healthcare_device_price_validation/`

## 변경하지 않은 것

- Production scoring 변경 없음.
- Candidate generation input으로 사용하지 않음.
- Stage 3-Green threshold를 낮추지 않음.
- OHLC나 stage price를 발명하지 않음.
- 투자 권고 문구 없음.
