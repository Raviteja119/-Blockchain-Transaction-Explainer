print("app.py started")

from fetch_transaction import fetch_transaction
from compress_data import compress_transaction_data
from decode_contract import decode_contract_input
from explain_transaction import explain_transaction

def run_pipeline(tx_hash):
    raw_tx = fetch_transaction(tx_hash)

    if raw_tx is None:
        print("❌ Transaction not found or RPC failed.")
        print("👉 Try a different transaction hash.")
        return None

    compressed_tx = compress_transaction_data(raw_tx)
    decoded = decode_contract_input(compressed_tx["input"])
    explanation = explain_transaction(compressed_tx, decoded)
    return explanation

if __name__ == "__main__":
    tx_hash = input("Enter Transaction Hash: ")
    output = run_pipeline(tx_hash)

    if output:
        print("\n--- Transaction Explanation ---")
        for line in output:
            print("-", line)
