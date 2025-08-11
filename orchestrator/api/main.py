from fastapi import FastAPI
from orchestrator.langchain.gemini_mock import parse_natural_language
from orchestrator.spec.validator import validate_spec
from orchestrator.jobs.pipeline_runner import run_pipeline

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Orchestrator API running"}

@app.post("/run")
def run_query(query: str):
    spec = parse_natural_language(query)
    if not validate_spec(spec):
        return {"error": "Invalid spec"}
    result = run_pipeline()
    return {"status": "success", "result": result}
