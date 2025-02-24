from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from fastapi import FastAPI
import uvicorn
import config  # Import API keys from config.py

# Use Together.AI as OpenAI alternative
llm = ChatOpenAI(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",  # Change to "gemma-7b" if needed
    openai_api_key=config.TOGETHER_API_KEY,
    openai_api_base="https://api.together.xyz/v1"  # Together API base URL
)

# FastAPI setup
app = FastAPI()

@app.get("/chat")
async def chat(user_message: str):
    messages = [
        SystemMessage(content="You are a mental health support chatbot. Be empathetic and supportive."),
        HumanMessage(content=user_message)
    ]
    
    response = llm(messages)
    return {"response": response.content}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
