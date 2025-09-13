# Keeper Bot (Polygon only)

## Features
- Harvest Beefy, Autofarm, Balancer vaults.
- Polygon-only with 2 RPC rotation.
- Watcher filters: low TVL, min profit, idle hours.
- DRY_RUN safety mode.
- Auto-skip broken vaults.

## Usage
1. Deploy to Railway.
2. Set env variables:
   - PRIVATE_KEY
   - PUBLIC_ADDRESS
   - RPC_POLYGON_1
   - RPC_POLYGON_2
   - DRY_RUN=true
   - MIN_PROFIT_USD=3
   - MAX_TVL=5000000
   - MIN_IDLE_HOURS=3
3. Start with DRY_RUN, then flip to false when confident.
