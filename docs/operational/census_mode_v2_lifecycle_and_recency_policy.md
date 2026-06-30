# Census Mode v2 Lifecycle and Recency Policy

- CensusAssessmentEvent는 전 종목 평가를 여는 행정 이벤트이며 점수 근거가 아니다.
- CandidateEvent, MarketAnomaly, stored source snapshot은 조사를 여는 트리거일 수 있지만 점수 근거가 아니다.
- accepted current claim과 score contribution id가 연결된 경우에만 verified score가 열린다.
- 오래된 리포트나 뉴스는 현재 claim으로 lifecycle refresh되기 전까지 SOURCE_PENDING 또는 NEEDS_REFRESH다.
- UNKNOWN은 PRESENT도 ABSENT도 아니다.

쉬운 예: 2023년 좋은 리포트가 있어도 2026년 현재 원문 claim으로 다시 살아나지 않으면 점수는 0이고, 상태는 refresh 대상이다.
