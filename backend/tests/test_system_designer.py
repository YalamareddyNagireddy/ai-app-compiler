from backend.pipeline.intent_extractor import IntentExtractor
from backend.pipeline.system_designer import SystemDesigner

extractor = IntentExtractor()
designer = SystemDesigner()

intent = extractor.extract(
    "Build a CRM with login, contacts, dashboard and premium payments. Admins can view analytics."
)

design = designer.design(intent)

print(design.model_dump())