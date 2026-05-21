# Round 326 R5 Loop 17 Price Validation Plan

Full adjusted OHLC is still unavailable for this round.
Reported event anchors are stored separately from future OHLC backfill rows.

Required future backfill:
- adjusted OHLC around each trigger date
- MFE/MAE 30D/90D/180D/1Y
- below-entry and drawdown-after-peak flags
- basket-level validation for tourism and K-beauty where a single listed beneficiary is ambiguous
- no invented price paths
