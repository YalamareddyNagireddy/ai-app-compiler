from backend.pipeline.intent_extractor import IntentExtractor
from backend.pipeline.system_designer import SystemDesigner
from backend.pipeline.schema_generator import SchemaGenerator

extractor = IntentExtractor()
designer = SystemDesigner()
generator = SchemaGenerator()

intent = extractor.extract(
    "Build a CRM with login, contacts, dashboard and premium payments. Admins can view analytics."
)

design = designer.design(intent)

schema = generator.generate(design)

print(schema.model_dump())