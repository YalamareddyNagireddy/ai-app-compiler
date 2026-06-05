from backend.pipeline.schema_generator import AppSchema
from backend.pipeline.repair_engine import RepairEngine
from backend.pipeline.validator import Validator

schema = AppSchema(
    ui_schema={},
    api_schema={},
    db_schema={},
    auth_rules={}
)

validator = Validator()

result = validator.validate(schema)

print("Before Repair")
print(result.valid)
print(result.errors)

repair_engine = RepairEngine()

repaired_schema = repair_engine.repair(schema)

result_after = validator.validate(repaired_schema)

print("After Repair")
print(result_after.valid)
print(result_after.errors)
