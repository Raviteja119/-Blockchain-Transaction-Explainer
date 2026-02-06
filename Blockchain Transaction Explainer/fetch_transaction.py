from web3 import Web3
from web3.exceptions import TransactionNotFound
from config import ETH_RPC_URL

w3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))

def fetch_transaction(tx_hash):
    try:
        tx = w3.eth.get_transaction(tx_hash)
    except TransactionNotFound:
        return None
    except Exception as e:
        print("RPC Error:", e)
        return None

    return {
        "from": tx["from"],
        "to": tx["to"],
        "value": hex(tx["value"]),
        "gas": hex(tx["gas"]),
        "input": tx["input"]
    }
