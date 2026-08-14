from providers.openai_provider import call_openai
from prompts.judge import judge_prompt
from judge_parse import parse_judge_response


def judge_debate(topic, for_side, against_side):
    raw = call_openai(judge_prompt(topic, for_side, against_side), temperature=0)
    return parse_judge_response(raw)
