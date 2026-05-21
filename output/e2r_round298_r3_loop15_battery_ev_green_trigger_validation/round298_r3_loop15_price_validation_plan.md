# Round 298 Price Validation Plan

- reported_event_anchor_not_full_ohlc 상태를 유지한다.
- full adjusted OHLC가 없다는 이유로 Stage2/Yellow 후보를 강등하지 않는다.
- full OHLC가 없는데 MFE/MAE를 발명하지 않는다.
- 다음 단계에서는 각 trigger date 기준 30/90/180일 MFE/MAE와 below-entry 여부를 채운다.
