from fastapi import FastAPI
from .models import AnalysisInput, RiskScoreResponse
from .scoring import calculate_risk_score

app = FastAPI(
    title="Brand Sentinel API",
    description="An API for analyzing text to determine brand safety risks.",
    version="1.0.0"
)

@app.get("/", tags=["Health"])
def read_root():
    """Root endpoint for health checks."""
    return {"status": "ok", "message": "Brand Sentinel API is running."}


@app.post("/score", response_model=RiskScoreResponse, tags=["Analysis"])
def score_text(analysis_input: AnalysisInput) -> RiskScoreResponse:
    """
    Analyzes a given text and returns a risk score based on multiple factors.
    """
    return calculate_risk_score(analysis_input)
