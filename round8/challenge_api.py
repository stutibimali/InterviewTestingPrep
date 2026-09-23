from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Round 8 Tasks API")


class TaskUpdate(BaseModel):
    task_id: str
    completed: bool
    note: str = Field(default="")


@app.put("/tasks/{task_id}")
def update_task(task_id: str, update: TaskUpdate):
    if task_id != update.task_id:
        return {"detail": "task identifiers do not match"}
    return {"task_id": task_id, "completed": update.completed, "note": update.note}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    if task_id == "protected":
        raise HTTPException(status_code=405, detail="task cannot be deleted")
    return {"deleted": task_id}