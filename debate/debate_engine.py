import os
from providers.openai_provider import call_openai
from providers.anthropic_provider import call_anthropic
from prompts.opening import opening_prompt
from prompts.rebuttal import rebuttal_prompt
from stream import stream_print
from config import OPENAI_NAME, ANTHROPIC_NAME
from dotenv import load_dotenv

load_dotenv()

ROUNDS = int(os.getenv("ROUNDS", "2"))

def run_debate(topic):
    log = {"topic": topic, "rounds": []}

    print("\n===== ROUND 1: OPENING ARGUMENTS =====")

    for_opening = call_openai(opening_prompt(topic, "for"))
    stream_print(f"{OPENAI_NAME} (FOR)", for_opening)

    against_opening = call_anthropic(opening_prompt(topic, "against"))
    stream_print(f"{ANTHROPIC_NAME} (AGAINST)", against_opening)

    log["rounds"].append({"for_opening": for_opening, "against_opening": against_opening})

    last_for = for_opening
    last_against = against_opening

    for i in range(ROUNDS):
        print(f"\n===== ROUND {i+2}: REBUTTALS =====")

        for_rebuttal = call_openai(rebuttal_prompt(topic, last_against))
        stream_print(f"{OPENAI_NAME}", for_rebuttal)

        against_rebuttal = call_anthropic(rebuttal_prompt(topic, last_for))
        stream_print(f"{ANTHROPIC_NAME}", against_rebuttal)

        log["rounds"].append({"for_rebuttal": for_rebuttal, "against_rebuttal": against_rebuttal})

        last_for = for_rebuttal
        last_against = against_rebuttal

    log["final_for"] = last_for
    log["final_against"] = last_against

    return log