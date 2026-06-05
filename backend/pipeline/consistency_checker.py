from backend.pipeline.schema_generator import AppSchema


class ConsistencyResult:

    def __init__(self):
        self.valid = True
        self.errors = []


class ConsistencyChecker:

    def check(self, schema: AppSchema):

        result = ConsistencyResult()

        tables = schema.db_schema.get("tables", [])

        if "Contact" in tables:

            endpoints = schema.api_schema.get(
                "endpoints", []
            )

            found = False

            for endpoint in endpoints:

                if endpoint["path"] == "/contacts":
                    found = True

            if not found:
                result.valid = False
                result.errors.append(
                    "Contact table exists but API endpoint missing"
                )

        return result