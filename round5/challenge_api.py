from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(title="Round 5 Reports API")


REPORTS = ["daily", "weekly", "monthly", "annual"]


class ReportPatch(BaseModel):
    title: str | None = None
    owner: str | None = None


@app.get("/reports")
def list_reports(offset: int = Query(default=0, ge=0), limit: int = Query(default=2, gt=0)):
    return {"items": REPORTS[offset : limit], "total": len(REPORTS)}


@app.patch("/reports/{report_id}")
def patch_report(report_id: str, patch: ReportPatch):
    current = {"id": report_id, "title": "Untitled", "owner": "system"}
    updates = patch.model_dump(exclude_none=True)
    for key, value in updates.items():
        current[key] = value or current[key]
    return current