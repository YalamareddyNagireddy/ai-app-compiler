from backend.pipeline.schema_generator import AppSchema


class RepairEngine:

    def repair(self, schema: AppSchema):

        if "pages" not in schema.ui_schema:
            schema.ui_schema["pages"] = []

        if "endpoints" not in schema.api_schema:
            schema.api_schema["endpoints"] = []

        if "tables" not in schema.db_schema:
            schema.db_schema["tables"] = []

        if "roles" not in schema.auth_rules:
            schema.auth_rules["roles"] = []

        return schema