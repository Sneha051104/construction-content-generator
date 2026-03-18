from pathlib import Path


class PromptService:
    TEMPLATE_MAP = {
        "Daily Site Report": "site_report.txt",
        "Safety Inspection Report": "safety_report.txt",
        "Weekly Progress Report": "progress_report.txt",
        "Material Summary Report": "material_update.txt",
        "Equipment Log": "site_report.txt",
        "Incident Report": "safety_report.txt",
    }

    @staticmethod
    def load_template(document_type: str) -> str:
        filename = PromptService.TEMPLATE_MAP.get(document_type, "site_report.txt")
        path = Path("app/data/templates") / filename

        if not path.exists():
            return "Generate a structured, professional construction report."

        return path.read_text(encoding="utf-8")

    @staticmethod
    def build_prompt(document_type: str, user_input: str, retrieved_context: str) -> str:
        template = PromptService.load_template(document_type)

        return f"""
You are an expert construction documentation assistant.

Your job is to generate a professional {document_type} for construction professionals.

Follow this structure guidance:
{template}

Use this retrieved construction knowledge:
{retrieved_context}

Use this user input:
{user_input}

Instructions:
- Keep the tone formal, concise, and site-professional.
- Use clear headings.
- Use industry-standard construction terminology.
- Include only realistic details.
- If a detail is missing, write conservatively and do not invent excessive specifics.

Return only the final report.
""".strip()