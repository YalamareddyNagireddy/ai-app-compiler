from pydantic import BaseModel
from typing import Dict

from backend.pipeline.system_designer import SystemDesign


class AppSchema(BaseModel):
    ui_schema: Dict
    api_schema: Dict
    db_schema: Dict
    auth_rules: Dict


class SchemaGenerator:

    def generate(self, design: SystemDesign) -> AppSchema:

        ui_schema = {
            "pages": design.pages
        }

        api_schema = {
            "endpoints": [
                {
                    "path": "/login",
                    "method": "POST"
                },
                {
                    "path": "/contacts",
                    "method": "GET"
                }
            ]
        }

        db_schema = {
            "tables": design.entities
        }

        auth_rules = {
            "roles": design.roles
        }

        return AppSchema(
            ui_schema=ui_schema,
            api_schema=api_schema,
            db_schema=db_schema,
            auth_rules=auth_rules
        )