from backend.pipeline.intent_extractor import IntentExtractor
from backend.pipeline.system_designer import SystemDesigner
from backend.pipeline.schema_generator import SchemaGenerator
from backend.pipeline.validator import Validator

extractor = IntentExtractor()
designer = SystemDesigner()
generator = SchemaGenerator()
validator = Validator()

intent = extractor.extract(
    "Build a CRM with login, contacts, dashboard and premium payments."
)

design = designer.design(intent)

schema = generator.generate(design)

result = validator.validate(schema)

print("Valid:", result.valid)
print("Errors:", result.errors)