from backend.pipeline.intent_extractor import IntentExtractor
from backend.pipeline.system_designer import SystemDesigner
from backend.pipeline.schema_generator import SchemaGenerator
from backend.pipeline.validator import Validator
from backend.pipeline.repair_engine import RepairEngine
from backend.pipeline.consistency_checker import ConsistencyChecker
from backend.pipeline.runtime_simulator import RuntimeSimulator


class AppCompiler:

    def __init__(self):
        self.extractor = IntentExtractor()
        self.designer = SystemDesigner()
        self.generator = SchemaGenerator()
        self.validator = Validator()
        self.repair_engine = RepairEngine()
        self.consistency_checker = ConsistencyChecker()
        self.runtime_simulator = RuntimeSimulator()

    def compile(self, prompt):

        intent = self.extractor.extract(prompt)

        design = self.designer.design(intent)

        schema = self.generator.generate(design)

        validation = self.validator.validate(schema)

        if not validation.valid:
            schema = self.repair_engine.repair(schema)

        consistency = self.consistency_checker.check(schema)

        runtime = self.runtime_simulator.simulate(schema)

        return {
            "intent": intent.model_dump(),
            "design": design.model_dump(),
            "schema": schema.model_dump(),
            "validation": {
                "valid": validation.valid,
                "errors": validation.errors
            },
            "consistency": {
                "valid": consistency.valid,
                "errors": consistency.errors
            },
            "runtime": runtime
        }