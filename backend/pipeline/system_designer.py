from pydantic import BaseModel
from typing import List

from backend.pipeline.intent_extractor import Intent


class SystemDesign(BaseModel):
    entities: List[str]
    pages: List[str]
    roles: List[str]


class SystemDesigner:

    def design(self, intent: Intent) -> SystemDesign:

        entities = []
        pages = []

        if "contacts" in intent.features:
            entities.append("Contact")

        if "payments" in intent.features:
            entities.append("Subscription")

        if "login" in intent.features:
            pages.append("LoginPage")

        if "dashboard" in intent.features:
            pages.append("DashboardPage")

        pages.append("HomePage")

        return SystemDesign(
            entities=entities,
            pages=pages,
            roles=intent.roles
        )