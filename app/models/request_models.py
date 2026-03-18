from pydantic import BaseModel
from typing import Optional


class GenerateRequest(BaseModel):
    document_type: str
    project_name: Optional[str] = ""
    location: Optional[str] = ""
    date: Optional[str] = ""
    topic: Optional[str] = ""
    weather: Optional[str] = ""
    work_completed: Optional[str] = ""
    work_in_progress: Optional[str] = ""
    manpower: Optional[str] = ""
    materials: Optional[str] = ""
    equipment: Optional[str] = ""
    quality_checks: Optional[str] = ""
    safety: Optional[str] = ""
    issues: Optional[str] = ""
    next_plan: Optional[str] = ""
    remarks: Optional[str] = ""