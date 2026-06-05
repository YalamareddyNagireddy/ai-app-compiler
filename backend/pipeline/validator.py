from typing import List

from backend.pipeline.schema_generator import AppSchema


class ValidationResult:

    def __init__(self):
        self.valid = True
        self.errors = []


class Validator:

    def validate(self, schema: AppSchema):

        result = ValidationResult()

        # Check UI Schema
        if "pages" not in schema.ui_schema:
            result.valid = False
            result.errors.append(
                "ui_schema missing pages"
            )

        # Check API Schema
        if "endpoints" not in schema.api_schema:
            result.valid = False
            result.errors.append(
                "api_schema missing endpoints"
            )

        # Check DB Schema
        if "tables" not in schema.db_schema:
            result.valid = False
            result.errors.append(
                "db_schema missing tables"
            )

        # Check Auth Rules
        if "roles" not in schema.auth_rules:
            result.valid = False
            result.errors.append(
                "auth_rules missing roles"
            )

        return result