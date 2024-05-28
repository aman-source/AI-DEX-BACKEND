def swap_trade_buy_sell(*args, **kwargs):
    try:
        # Extract positional arguments safely
        token1 = args[0].get('token1', None) if args else None
        token2 = args[0].get('token2', None) if args else None
        amountOfToken1 = args[0].get('amount', None) if args else None
    except (IndexError, KeyError) as e:
        return f"An error occurred: {e}"

    # Extract keyword arguments if needed
    # token1 = kwargs.get('token1', token1)
    # token2 = kwargs.get('token2', token2)
    # amountOfToken1 = kwargs.get('amountOfToken1', amountOfToken1)

    # Check for missing parameters and return specific error messages
    if not token1:
        return {"message":"Oops! It looks like you forgot to specify the token you want to sell. Please provide the token you want to swap from."}
    if not token2:
        return {"message":"Hmm, I didn't catch the token you want to receive. Can you specify it, please?"}
    if amountOfToken1 is None:
        return {"message":"Oh no! You didn't mention the amount you want to swap. Please provide that amount."}

    return {
        "token1": token1,
        "token2": token2,
        "amountOfToken1": amountOfToken1,
        "message": f"Your transaction has been submitted for swapping {amountOfToken1} {token1} to {token2}."
    }

# Example usage:
args = [{"token1": "BTC", "token2": "ETH", "amount": 1.5}]
print(swap_trade_buy_sell(*args))
