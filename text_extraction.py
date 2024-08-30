import json

import openai
from openai import OpenAI

from functions import generate_swap_function
from utils.generalchat import general_chat
from utils.swap_trade_buy_sell import swap_trade_buy_sell


def get_function_based_conversation(text):
  
    # Extracting the conversation from the text
  instructions= '''you are an intelligent AI
                  You get usertext and return arguments
                  You help users to get the function based conversation
                  you are crypto bot and help in selling and buying of cryptocurrencies
  '''
  openai.api_key = "API_KEY"
  client = OpenAI(
     api_key="OPEN_AI_KEY"
  )
  messages=[{"role": "system", "content": instructions},{"role": "user", "content": text}]
  tools = [generate_swap_function()] 
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    tools=tools,
    tool_choice = "auto",
    temperature=0.2,
  )
  
  response_message = response.choices[0].message
  tool_calls = response_message.tool_calls
  if tool_calls:
    available_functions = {
      "swap_trade_buy_sell": swap_trade_buy_sell
    }
    
    messages.append(response_message)
    
    for tool_call in tool_calls:
      function_name = tool_call.function.name
      function = available_functions[function_name]
      function_args = json.loads(tool_call.function.arguments)
      if function:
        # parameters = tool_call.parameters
        result = function(function_args)
        # messages.append({"role": "system", "content": result})
        
    return result
  else:
    return general_chat(text)
