# Census Mode v1 Design

Census Mode는 전체 universe에 현재 E2R 상태, 판단 깊이, source gap, 다음 action을 붙이는 상태판이다.

## Mode Split
- Daily Trigger Mode: 새 사건이 생긴 종목만 깊게 본다.
- Census Mode: 트리거 유무와 관계없이 전체 universe에 StageStatus를 붙인다.
- Deep Backfill Mode: 장기간 deep evidence ledger를 구축한다. 이번 Goal은 계획만 만든다.
- Watchlist Update Mode: Census seed를 daily trigger 추적 대상으로 넘긴다.

## Safety
- CensusAssessmentEvent는 점수 증거가 아니다.
- market anomaly와 provider failure는 점수가 아니라 pending/investigation 상태다.
- 비영점 verified score는 accepted current claim id가 있을 때만 허용한다.
- 종목명/URL 예외처리와 unbounded fetch는 금지한다.
