import json
import re
from providers.openai_provider import call_openai
from prompts.judge import judge_prompt
from config import OPENAI_NAME, ANTHROPIC_NAME

def judge_debate(topic, for_side, against_side):
    raw = call_openai(judge_prompt(topic, for_side, against_side), temperature=0)
    cleaned = raw.strip()
    fenced = re.match(r"^```(?:json)?\s*(.+?)\s*```$", cleaned, re.DOTALL | re.IGNORECASE)
    if fenced:
        cleaned = fenced.group(1).strip()

    try:
        data = json.loads(cleaned)
    except Exception:
        return {
            "error": "Failed to parse judge response",
            "raw_response": raw
        }

    if not data.get("winner_model"):
        if data.get("winner") == "for":
            data["winner_model"] = OPENAI_NAME
        elif data.get("winner") == "against":
            data["winner_model"] = ANTHROPIC_NAME

    if "score_openai" not in data and "score_for" in data:
        data["score_openai"] = data["score_for"]
    if "score_anthropic" not in data and "score_against" in data:
        data["score_anthropic"] = data["score_against"]

    return data
