# Stage Lifecycle Detection

Stage lifecycle detection monitors what happens after Stage 3.

It separates:

```text
4A ongoing thesis
4B soft graduation / crowding warning
4C hard thesis break
```

## Stage 4A

4A means:

```text
Stage 3 evidence remains intact
EPS/FCF or revenue visibility remains strong
price has risen but not enough to trigger confirmed 4B
no hard thesis break
```

## Price-Only 4B Watch

If only price has gone up sharply:

```text
price_only_4b_watch
```

This is not full 4B.

Example:

```text
stock tripled
but no revision slowdown, backlog slowdown, or crowding evidence
-> price_only_4b_watch
```

## Evidence-Based 4B

4B-watch / 4B-elevated / 4B-graduated requires combinations of:

```text
high return since Stage 3
excessive 12m/24m return
valuation rerating score saturated
revision momentum slowing
backlog/order/margin slowdown
blow-off price pattern
crowding or universally bullish report tone
```

At least one non-price evidence factor is required for full 4B.

## Hard 4C

4C means thesis break.

Examples:

```text
EPS/FCF estimates down
contract cancellation or delay
ASP/margin drop
backlog/RPO decline
customer capex collapse
accounting/trust issue
dilution or financing risk invalidates thesis
```

## Backtest Labels

Reports should distinguish:

```text
detected_before_peak
detected_near_peak
detected_after_peak
price_only_warning
unknown_insufficient_evidence
```

If evidence is missing, the system must say so.
It must not invent 4B.
