# Round-33 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep synthetic, global reference, event, and theme cases as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before any production scoring change.

## Priority Validation
- Media/ad: platform monetization versus client budget and traditional ad decline.
- Packaging/agri/livestock: pricing and FCF versus cost, disease, weather, and mature-cycle risks.
- Regulated consumer/apparel: approval and channel evidence versus legal, IP, product safety, inventory, and markdown.
- AI software/NFT: recurring revenue and compute/IP control versus theme-only liquidity or no-revenue rallies.
