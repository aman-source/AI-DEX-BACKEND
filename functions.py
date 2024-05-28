def generate_swap_function():
    return {
      "type": "function",
      "function":{
        "name":"swap_trade_buy_sell",
        "description":"sell/buy/swap one cryptocurrency for another cryptocurrency",
        "parameters":{
          "type": "object",
          "properties": {
            "token1": {
              "type": "string",
              "description": "the cryptocurrency to sell"
            },
            "token2": {
              "type": "string",
              "description": "the cryptocurrency to buy"
            },
            "amount": {
              "type": "number",
              "description": "the amount of the 'from' cryptocurrency to sell"
            },
            # "price": {
            #   "type": "number",
            #   "description": "the price of the 'to' cryptocurrency"
            # }
          }
        }
      }
    }
