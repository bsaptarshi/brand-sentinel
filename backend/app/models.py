from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import datetime

class AnalysisInput(BaseModel):
    """Input model for the analysis request."""
    text: str = Field(..., description="The text content to be analyzed.")
    source: Optional[str] = Field(None, description="The source of the text (e.g., 'twitter', 'news_article').")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Optional metadata.")

class RiskFactor(BaseModel):
    """Model representing a single risk factor with its score and weight."""
    name: str = Field(..., description="The name of the risk factor.")
    score: float = Field(..., ge=0.0, le=1.0, description="The score of the risk factor (0.0 to 1.0).")
    weight: float = Field(..., gt=0.0, description="The weight of the factor in the overall calculation.")

class RiskScoreResponse(BaseModel):
    """Response model containing the overall risk score and its contributing factors."""
    overall_risk_score: float = Field(..., ge=0.0, le=1.0, description="The final calculated risk score.")
    risk_factors: List[RiskFactor] = Field(..., description="A list of risk factors that contributed to the score.")
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, description="The UTC timestamp of the analysis.")
