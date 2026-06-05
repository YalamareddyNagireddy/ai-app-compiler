from backend.pipeline.intent_extractor import IntentExtractor

extractor = IntentExtractor()

result = extractor.extract(
    "Build a CRM with login, contacts, dashboard and premium payments. Admins can view analytics."
)

print(result.model_dump())