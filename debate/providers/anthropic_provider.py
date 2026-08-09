import os
import time
import anthropic
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing ANTHROPIC_API_KEY in .env")

client = anthropic.Anthropic(api_key=API_KEY)

def call_anthropic(messages, temperature=0.7, retries=3):
    system = ""
    convo = []

    for m in messages:
        if m["role"] == "system":
            system = m["content"]
        else:
            convo.append({"role": m["role"], "content": m["content"]})

    for attempt in range(retries):
        try:
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=500,
                temperature=temperature,
                system=system,
                messages=convo
            )
            return response.content[0].text

        except Exception as e:
            if attempt == retries - 1:
                raise RuntimeError(f"Anthropic failed after retries: {e}")
            time.sleep(2 * (attempt + 1))
