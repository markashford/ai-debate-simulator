def opening_prompt(topic, side):
    return [
        {"role": "system", "content": "You are participating in a formal academic debate."},
        {"role": "user", "content": f"""
            Topic: {topic}
            Position: {side}

            Rules:
            - Be persuasive but factual
            - No emotional language
            - Max 180 words
        """}
    ]
