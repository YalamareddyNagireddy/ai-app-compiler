from backend.pipeline.intent_extractor import IntentExtractor
from backend.pipeline.system_designer import SystemDesigner
from backend.pipeline.schema_generator import SchemaGenerator
from backend.pipeline.consistency_checker import ConsistencyChecker

extractor = IntentExtractor()
designer = SystemDesigner()
generator = SchemaGenerator()
checker = ConsistencyChecker()

intent = extractor.extract(
    "Build a CRM with login, contacts and dashboard"
)

design = designer.design(intent)

schema = generator.generate(design)

result = checker.check(schema)

print("Valid:", result.valid)
print("Errors:", result.errors)