import os
import time
import requests
from utils.chain import get_w3
from beefy.beefy_keeper import harvest as beefy_harvest
from autofarm.autofarm_keeper import harvest as autofarm_harvest
from balancer.balancer_keeper import harvest as balancer_harvest

MIN_PROFIT_USD = float(os.getenv("MIN_PROFIT_USD", "3"))
MAX_TVL = float(os.getenv("MAX_TVL", "5000000"))
MIN_IDLE_HOURS = float(os.getenv("MIN_IDLE_HOURS", "3"))

SKIPPED_VAULTS = set()

def record_skip(vault_id):
    SKIPPED_VAULTS.add(vault_id)
    print(f"[Watcher] Skipping future attempts for {vault_id}")

def run_watcher():
    w3 = get_w3()
    while True:
        try:
            # Example: fetch Beefy vaults
            resp = requests.get("https://api.beefy.finance/vaults").json()
            for vault_id, vault in resp.items():
                if vault_id in SKIPPED_VAULTS:
                    continue
                if vault.get("tvl", 0) > MAX_TVL:
                    continue
                if vault.get("lastHarvest", 999999) < MIN_IDLE_HOURS * 3600:
                    continue

                est_profit = 5  # placeholder
                if est_profit < MIN_PROFIT_USD:
                    continue

                print(f"[Watcher] Found Beefy task {vault_id}")
                beefy_harvest(vault_id, vault["earnedTokenAddress"], w3, w3.eth.account.from_key(os.getenv("PRIVATE_KEY")))

        except Exception as e:
            print(f"[Watcher] Error in loop: {e}")

        time.sleep(30)
