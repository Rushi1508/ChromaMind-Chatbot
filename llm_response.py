"""
Handles Groq API integration for LLM responses.
"""
import logging
import requests
from config.settings import GROQ_API_KEY, GROQ_MODEL, SYSTEM_PROMPT

# Groq API Endpoint
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_llm_response(prompt: str):
    """
    Calls Groq API to generate a response dynamically.
    """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }

    logging.debug(f"📤 Sending request to Groq API: {payload}")

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            logging.debug(f"✅ Groq API Response: {response.json()}")
            return response.json()["choices"][0]["message"]["content"]
        else:
            logging.error(f"❌ Groq API Error: {response.status_code} - {response.text}")
            return "I'm unable to process your request at the moment."
    except Exception as e:
        logging.error(f"❌ Groq API Call Failed: {str(e)}")
        return "I'm unable to process your request at the moment."
