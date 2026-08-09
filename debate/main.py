import sys
from config import OPENAI_NAME, ANTHROPIC_NAME
from debate_engine import run_debate
from judge import judge_debate
from logger import save_run

def main():
    topic = " ".join(sys.argv[1:])

    if not topic:
        print("Usage: python main.py 'debate topic'")
        return

    try:
        debate = run_debate(topic)
        judgment = judge_debate(topic, debate["final_for"], debate["final_against"])

        debate["judgment"] = judgment

        print("\n===== FINAL JUDGMENT =====")
        print(f"Winner Model: {judgment.get('winner_model')}")
        print(f"Reason: {judgment.get('reason')}")
        openai_score = judgment.get("score_openai", judgment.get("score_for"))
        anthropic_score = judgment.get("score_anthropic", judgment.get("score_against"))
        print(f"Scores: {OPENAI_NAME}={openai_score} {ANTHROPIC_NAME}={anthropic_score}")

        file = save_run(debate)
        print("\nSaved to:", file)

    except Exception as e:
        print("\nERROR OCCURRED:")
        print(e)

if __name__ == "__main__":
    main()
