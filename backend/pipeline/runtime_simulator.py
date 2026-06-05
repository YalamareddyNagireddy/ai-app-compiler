from backend.pipeline.schema_generator import AppSchema


class RuntimeSimulator:

    def simulate(self, schema: AppSchema):

        report = {
            "ui_pages_loaded": len(
                schema.ui_schema.get("pages", [])
            ),
            "api_endpoints_loaded": len(
                schema.api_schema.get("endpoints", [])
            ),
            "db_tables_loaded": len(
                schema.db_schema.get("tables", [])
            ),
            "roles_loaded": len(
                schema.auth_rules.get("roles", [])
            ),
            "execution_status": "SUCCESS"
        }

        return report