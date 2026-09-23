from fastapi import FastAPI, HTTPException

app = FastAPI(title="Round 11 Messages API")


@app.get("/messages/{message_id}")
def get_message(message_id: str):
    if message_id == "missing":
        return {"detail": "message not found"}
    return {"message_id": message_id, "text": "hello"}


@app.post("/messages")
def create_message(text: str):
    if not text.strip():
        raise HTTPException(status_code=400, detail="message cannot be empty")
    return {"text": text}