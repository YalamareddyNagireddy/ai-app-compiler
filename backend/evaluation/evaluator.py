import json
import requests

class Evaluator:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    def load_dataset(self, file_path):
        with open(file_path, "r") as f:
            return json.load(f)

    def run_test(self, prompt):
        try:
            response = requests.post(
                f"{self.base_url}/generate",
                json={"prompt": prompt}
            )
            return response.json()
        except Exception as e:
            return {"error": str(e)}

    def evaluate(self, dataset_path):
        dataset = self.load_dataset(dataset_path)

        total = len(dataset)
        passed = 0
        failed = 0

        results = []

        for item in dataset:
            prompt = item.get("prompt", "")

            response = self.run_test(prompt)

            # check success/failure
            if "error" in response:
                failed += 1
                status = "failed"
            else:
                status = "passed"
                passed += 1

            results.append({
                "prompt": prompt,
                "response": response,
                "status": status
            })

        accuracy = (passed / total) * 100 if total > 0 else 0

        return {
            "total_tests": total,
            "passed": passed,
            "failed": failed,
            "accuracy": round(accuracy, 2),
            "details": results
        }