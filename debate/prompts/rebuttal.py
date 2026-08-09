def rebuttal_prompt(topic, opponent_text):
    return [
        {"role": "system", "content": "You are in a structured debate."},
        {"role": "user", "content": f"""
            Topic: {topic}

            Opponent said: {opponent_text}

            Write a rebuttal only.
            Do NOT repeat your original points.
            Max 120 words.
        """}
    ]
