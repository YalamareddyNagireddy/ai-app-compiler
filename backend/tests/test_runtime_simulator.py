from backend.pipeline.intent_extractor import IntentExtractor
from backend.pipeline.system_designer import SystemDesigner
from backend.pipeline.schema_generator import SchemaGenerator
from backend.pipeline.runtime_simulator import RuntimeSimulator

extractor = IntentExtractor()
designer = SystemDesigner()
generator = SchemaGenerator()
simulator = RuntimeSimulator()

intent = extractor.extract(
    "Build a CRM with login, contacts, dashboard and premium payments."
)

design = designer.design(intent)

schema = generator.generate(design)

result = simulator.simulate(schema)

print(result)