import os
import random
from web3 import Web3

RPCS = [os.getenv("RPC_POLYGON_1"), os.getenv("RPC_POLYGON_2")]

def get_w3():
    rpc = random.choice(RPCS)
    print(f"[Chain] Using RPC {rpc}")
    return Web3(Web3.HTTPProvider(rpc))
