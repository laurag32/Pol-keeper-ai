import os
from web3 import Web3
from utils.tx import record_skip

def harvest(vault_id, vault_address, w3: Web3, account):
    try:
        tx = {
            "from": account.address,
            "to": vault_address,
            "data": "0x4641257d",
            "gas": 300000,
            "gasPrice": w3.eth.gas_price,
            "nonce": w3.eth.get_transaction_count(account.address),
        }

        if os.getenv("DRY_RUN", "true").lower() == "true":
            print(f"[DRY_RUN] Autofarm would harvest {vault_id}")
            return

        tx_hash = w3.eth.send_transaction(tx)
        print(f"[Autofarm] Harvest SENT {vault_id} → {tx_hash.hex()}")

    except Exception as e:
        print(f"[Autofarm] Error on {vault_id}: {e}")
        record_skip(vault_id)
