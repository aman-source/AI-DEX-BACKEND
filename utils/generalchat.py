from openai import OpenAI 
def general_chat(text):
  instructions= '''you are an intelligent AI
                  you are crypto bot and help in explaining everything abouth blockchain and cryptocurrencies,
                  You help users to get clarifuied about the ctyprocurrencies and their trading,
                  you are a friendly AI and help users to understand the blockchain and cryptocurrencies in a simple way,
                  return the response in italic,bold,bullet points and numbered list to make it more readable and understandable to the users.
  '''
  client = OpenAI(
    api_key="OPEN_AI_KEY"
  )
  messages=[{"role": "system", "content": instructions},{"role": "user", "content": text}]
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.2,
  )
  return {"message" :response.choices[0].message.content}
