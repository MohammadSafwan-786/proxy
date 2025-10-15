from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        messages = data.get("messages", [])
        user_input = messages[-1]["content"] if messages else "Hello"

        # Simple logic to simulate smart replies
        if "capital of france" in user_input.lower():
            reply = "🇫🇷 The capital of France is Paris."
        elif "2 + 2" in user_input:
            reply = "🧮 2 + 2 equals 4."
        elif "einstein" in user_input.lower():
            reply = "🧠 Albert Einstein was a physicist known for the theory of relativity."
        else:
            reply = f"🤖 You asked: '{user_input}'. Here's a smart reply!"

            print("Reply:", reply)


        return JSONResponse(content={
            "choices": [{
                "message": {
                    "content": reply
                }
            }]
        })

    except Exception as e:
        return JSONResponse(content={
            "choices": [{
                "message": {
                    "content": f"❌ Error: {str(e)}"
                }
            }]
        }, status_code=500)
