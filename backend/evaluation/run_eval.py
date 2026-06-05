from backend.evaluation.evaluator import Evaluator

evaluator = Evaluator()

# choose dataset
dataset_path = "datasets/edge_case_prompts.json"

result = evaluator.evaluate(dataset_path)

print("\n===== EVALUATION REPORT =====")
print(f"Total Tests: {result['total_tests']}")
print(f"Passed: {result['passed']}")
print(f"Failed: {result['failed']}")
print(f"Accuracy: {result['accuracy']}%")