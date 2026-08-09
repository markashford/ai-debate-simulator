def judge_prompt(topic, for_side, against_side):
    return [
        {
            "role": "system",
            "content": (
                "You are a neutral debate judge. "
                "You must explicitly reference the model names in your reasoning, "
                "not abstract positions like 'for' or 'against'."
            )
        },
        {
            "role": "user",
            "content": f"""
                Topic: {topic}

                Model A: OpenAI
                Argument: {for_side}

                Model B: Anthropic
                Argument: {against_side}

                Evaluate:
                - Logical strength
                - Factual accuracy
                - Clarity
                - Persuasiveness

                Return STRICT JSON ONLY:
                    {{
                        "winner_model": "OpenAI or Anthropic",
                        "reason": "Explain clearly WHY that model won. Mention the model name explicitly.",
                        "score_openai": number,
                        "score_anthropic": number
                    }}

                Do NOT mention 'for' or 'against'.
                Do NOT add extra text.
            """
        }
    ]
