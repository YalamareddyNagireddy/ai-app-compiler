from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import time

from backend.pipeline.compiler import AppCompiler
from backend.utils.metrics import Metrics

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
compiler = AppCompiler()
metrics = Metrics()


@app.get("/")
def home():
    return {"message": "AI App Compiler is running"}


@app.post("/generate")
def generate(payload: dict):
    start_time = time.time()

    prompt = payload.get("prompt", "")

    result = compiler.compile(prompt)

    end_time = time.time()
    latency = (end_time - start_time) * 1000

    # success logic
    if isinstance(result, dict) and result.get("status") == "needs_clarification":
        success = False
    elif isinstance(result, dict) and result.get("status") == "success":
        success = True
    else:
        success = True

    metrics.log_request(
        success=success,
        latency=latency,
        repair_used=False
    )

    return {
        "result": result,
        "metrics": {
            "success": success,
            "latency_ms": round(latency, 2)
        }
    }


@app.get("/metrics")
def get_metrics():
    return metrics.get_report()