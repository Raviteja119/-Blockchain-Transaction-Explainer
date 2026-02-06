def explain_transaction(tx, decoded):
    explanation = []

    explanation.append(
        f"The transaction was sent from {tx['from']} to {tx['to']}."
    )

    explanation.append(
        f"The value transferred was {tx['value_eth']} ETH."
    )

    explanation.append(
        f"Gas limit used for this transaction was {tx['gas']} units."
    )

    if decoded["type"] == "Smart Contract Call":
        explanation.append(
            "This transaction interacts with a smart contract."
        )
    else:
        explanation.append(
            "This is a simple Ether transfer."
        )

    return explanation
