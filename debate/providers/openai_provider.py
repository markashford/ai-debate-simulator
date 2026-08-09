import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY in .env")

client = OpenAI(api_key=API_KEY)

def call_openai(messages, temperature=0.7, retries=3):
    for attempt in range(retries):
        try:
            response = client.responses.create(
                model="gpt-4.1-mini",
                temperature=temperature,
                input=[
                    {
                        "role": m["role"],
                        "content": [{"type": "input_text", "text": m["content"]}]
                    }
                    for m in messages
                ]
            )
            return response.output_text

        except Exception as e:
            if attempt == retries - 1:
                raise RuntimeError(f"OpenAI failed after retries: {e}")
            time.sleep(2 * (attempt + 1))