from .models import AnalysisInput, RiskFactor, RiskScoreResponse
from typing import List, Dict

# --- Risk Factor Weights ---
# These would be tuned based on business requirements.
RISK_FACTOR_WEIGHTS: Dict[str, float] = {
    "toxicity": 1.5,
    "negative_sentiment": 1.0,
    "misinformation": 1.2,
    "spam": 0.5,
}

# --- Placeholder Scoring Functions ---
# In a real-world scenario, these would be replaced by sophisticated models (e.g., NLP/ML models).

def calculate_toxicity_score(text: str) -> float:
    """Placeholder for toxicity detection."""
    toxic_keywords = ["hate", "awful", "terrible", "racist", "bigot"]
    score = sum(1 for word in toxic_keywords if word in text.lower()) / len(toxic_keywords)
    return min(score, 1.0)

def calculate_negative_sentiment_score(text: str) -> float:
    """Placeholder for negative sentiment analysis."""
    negative_keywords = ["disappointed", "bad", "unhappy", "fail", "poor"]
    score = sum(1 for word in negative_keywords if word in text.lower()) / len(negative_keywords)
    return min(score, 1.0)

def calculate_misinformation_score(text: str) -> float:
    """Placeholder for misinformation detection."""
    misinfo_keywords = ["fake news", "hoax", "conspiracy", "unproven"]
    score = sum(1 for word in misinfo_keywords if word in text.lower()) / len(misinfo_keywords)
    return min(score, 1.0)

def calculate_spam_score(text: str) -> float:
    """Placeholder for spam detection."""
    spam_keywords = ["buy now", "free money", "limited time offer", "click here"]
    score = sum(1 for word in spam_keywords if word in text.lower()) / len(spam_keywords)
    return min(score, 1.0)

# --- Main Risk Calculation Logic ---

def calculate_risk_score(analysis_input: AnalysisInput) -> RiskScoreResponse:
    """
    Calculates the overall risk score based on a weighted formula of various risk factors.
    """
    risk_factors: List[RiskFactor] = []

    # Calculate scores for each factor
    toxicity_score = calculate_toxicity_score(analysis_input.text)
    negative_sentiment_score = calculate_negative_sentiment_score(analysis_input.text)
    misinformation_score = calculate_misinformation_score(analysis_input.text)
    spam_score = calculate_spam_score(analysis_input.text)

    # Create RiskFactor objects
    risk_factors.append(RiskFactor(name="toxicity", score=toxicity_score, weight=RISK_FACTOR_WEIGHTS["toxicity"]))
    risk_factors.append(RiskFactor(name="negative_sentiment", score=negative_sentiment_score, weight=RISK_FACTOR_WEIGHTS["negative_sentiment"]))
    risk_factors.append(RiskFactor(name="misinformation", score=misinformation_score, weight=RISK_FACTOR_WEIGHTS["misinformation"]))
    risk_factors.append(RiskFactor(name="spam", score=spam_score, weight=RISK_FACTOR_WEIGHTS["spam"]))

    # Calculate weighted average for the overall score
    total_weighted_score = sum(factor.score * factor.weight for factor in risk_factors)
    total_weight = sum(factor.weight for factor in risk_factors)

    if total_weight == 0:
        overall_risk_score = 0.0
    else:
        overall_risk_score = total_weighted_score / total_weight
        
    overall_risk_score = min(overall_risk_score, 1.0) # Ensure score is capped at 1.0

    return RiskScoreResponse(
        overall_risk_score=overall_risk_score,
        risk_factors=risk_factors
    )
