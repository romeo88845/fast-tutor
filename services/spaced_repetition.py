"""SM-2 spaced repetition algorithm with safety caps."""
from datetime import datetime, timedelta
from typing import Optional

MAX_INTERVAL_DAYS = 365  # Never schedule more than 1 year out

def calculate_next_review(
    is_correct: bool,
    interval_days: int,
    repetition_count: int,
    easiness_factor: float,
    quality_score: int = 4
) -> dict:
    """SM-2 algorithm with capped intervals."""
    if is_correct:
        if repetition_count == 0:
            interval = 1
        elif repetition_count == 1:
            interval = 6
        else:
            interval = round(interval_days * easiness_factor)
        
        # SM-2: EF' = EF + (0.1 - (5-q) * (0.08 + (5-q) * 0.02))
        ef = easiness_factor + (0.1 - (5 - quality_score) * (0.08 + (5 - quality_score) * 0.02))
        ef = max(1.3, ef)
        rep_count = repetition_count + 1
    else:
        interval = 1
        ef = max(1.3, easiness_factor - 0.2)
        rep_count = 0

    # Safety cap
    interval = min(interval, MAX_INTERVAL_DAYS)
    ef = min(ef, 5.0)
    
    next_review = datetime.utcnow() + timedelta(days=interval)
    return {
        "interval_days": interval,
        "repetition_count": rep_count,
        "easiness_factor": round(ef, 2),
        "next_review_at": next_review
    }

def get_quality_score(is_correct: bool, response_time_seconds: Optional[float] = None) -> int:
    """Convert correctness + response time to SM-2 quality score (0-5)."""
    if not is_correct:
        return 0
    if response_time_seconds is None:
        return 4
    if response_time_seconds < 10:
        return 5
    elif response_time_seconds < 30:
        return 4
    else:
        return 3
