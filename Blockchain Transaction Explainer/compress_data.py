def compress_transaction_data(tx):
    compressed = {
        "from": tx.get("from"),
        "to": tx.get("to"),
        "value_eth": int(tx.get("value", "0x0"), 16) / 10**18,
        "gas": int(tx.get("gas", "0x0"), 16),
        "input": tx.get("input")
    }
    return compressed
