import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "debate"))

from judge import parse_judge_response


def test_parse_plain_json():
    raw = '{"winner": "for", "score_for": 8, "score_against": 6, "reason": "Clearer structure"}'
    data = parse_judge_response(raw)
    assert data["winner"] == "for"
    assert data["winner_model"] == "OpenAI"
    assert data["score_openai"] == 8
    assert data["score_anthropic"] == 6


def test_parse_fenced_json():
    raw = """```json
{"winner": "against", "score_for": 4, "score_against": 9, "reason": "Better evidence"}
```"""
    data = parse_judge_response(raw)
    assert data["winner_model"] == "Anthropic"
    assert data["score_anthropic"] == 9


def test_parse_invalid_json():
    data = parse_judge_response("not json at all")
    assert data["error"] == "Failed to parse judge response"
    assert "raw_response" in data
