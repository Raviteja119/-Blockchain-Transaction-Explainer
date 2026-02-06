def decode_contract_input(input_data):
    if input_data == "0x":
        return {
            "type": "ETH Transfer",
            "function": "Direct Transfer"
        }

    return {
        "type": "Smart Contract Call",
        "function": "Contract Interaction",
        "raw_input": input_data[:20] + "..."
    }
