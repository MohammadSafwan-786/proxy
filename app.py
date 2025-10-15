from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(request: Request):
    data = await request.json()
    messages = data.get("messages", [])
    user_input = messages[-1]["content"] if messages else "Hello"
    reply = f"🤖 You asked: '{user_input}'. Here's a smart reply!"
    return JSONResponse(content={
        "choices": [{
            "message": {
                "content": reply
            }
        }]
    })
