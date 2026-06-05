from fastapi import FastAPI
from pydantic import BaseModel

from backend.pipeline.compiler import AppCompiler

app = FastAPI()

compiler = AppCompiler()


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {
        "message": "AI App Compiler Running"
    }


@app.post("/generate")
def generate(request: PromptRequest):

    result = compiler.compile(
        request.prompt
    )

    return result