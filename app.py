from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from text_extraction import get_function_based_conversation

app = FastAPI()

# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/api/chatbot")
async def chatbot(message: Message):
    user_message = message.message
    
    # Log the received message
    print("Received message:", user_message)

    # Static response from the bot
    bot_response = get_function_based_conversation(user_message)

    return {"bot_response": bot_response}
  
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
