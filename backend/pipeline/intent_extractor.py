from pydantic import BaseModel
from typing import List


class Intent(BaseModel):
    app_type: str
    features: List[str]
    roles: List[str]
    payments_required: bool


class IntentExtractor:

    def extract(self, user_prompt: str) -> Intent:

        prompt_lower = user_prompt.lower()

        features = []

        if "login" in prompt_lower:
            features.append("login")

        if "dashboard" in prompt_lower:
            features.append("dashboard")

        if "contacts" in prompt_lower:
            features.append("contacts")

        if "payment" in prompt_lower or "premium" in prompt_lower:
            features.append("payments")

        roles = []

        if "admin" in prompt_lower:
            roles.append("admin")

        if "user" in prompt_lower:
            roles.append("user")

        return Intent(
            app_type="web_application",
            features=features,
            roles=roles,
            payments_required=(
                "payment" in prompt_lower
                or "premium" in prompt_lower
            )
        )