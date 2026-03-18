from app.models.request_models import GenerateRequest


def build_user_input(payload: GenerateRequest) -> str:
    return f"""
Document Type: {payload.document_type}
Project Name: {payload.project_name}
Location: {payload.location}
Date: {payload.date}
Topic / Focus Area: {payload.topic}
Weather: {payload.weather}
Work Completed: {payload.work_completed}
Work In Progress: {payload.work_in_progress}
Manpower: {payload.manpower}
Materials Used: {payload.materials}
Equipment: {payload.equipment}
Quality Checks: {payload.quality_checks}
Safety Observations: {payload.safety}
Issues / Delays: {payload.issues}
Next Day Plan: {payload.next_plan}
Remarks: {payload.remarks}
""".strip()