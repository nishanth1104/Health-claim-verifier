import requests
import os
from dotenv import load_dotenv

# Load Hugging Face API key from .env
load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HF_API_KEY")
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Content-Type": "application/json"
}

def query_hf(prompt):
    payload = {
        "inputs": prompt,
        "options": {
            "wait_for_model": True  # ensures model is loaded if sleeping
        }
    }

    print(f"🧠 Sending prompt:\n{prompt}")
    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)

    print("🔍 HTTP Status:", response.status_code)
    print("🔍 API Raw Response:", response.text)

    try:
        result = response.json()

        # Case 1: result is a list of dicts (most common format)
        if isinstance(result, list):
            for item in result:
                if "generated_text" in item:
                    return item["generated_text"]

        # Case 2: result is a dict
        if isinstance(result, dict):
            if "generated_text" in result:
                return result["generated_text"]
            if "error" in result:
                print("❌ Hugging Face API Error:", result["error"])
                return "Sorry, the AI could not generate a response."

        print("⚠️ Unexpected response format:", result)
        return "Sorry, the AI response format was not recognized."

    except Exception as e:
        print("❌ Exception while parsing response:", e)
        return "Sorry, something went wrong while processing your request."

def get_agent_response(claim):
    prompt = f"""
You are a trusted medical assistant. Evaluate the following health claim and explain whether it is medically accurate.

Claim: "{claim}"

Respond with a brief explanation, then state the final verdict clearly as one of: TRUE, FALSE, or UNCERTAIN.
    """.strip()

    return query_hf(prompt)
