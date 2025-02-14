# app/utils/llm_utils.py
import os, requests

AIPROXY_TOKEN = os.environ.get("eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjMwMDI1MzlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.zG6mIw8Zch5LdZRtnjpyXJBH0u91kSEpToxfO0kArYk")
LLM_API_URL = "https://api.llm-proxy.example.com/gpt-4o-mini"  # Replace with the actual API URL

def call_llm(prompt: str) -> str:
    headers = {"Authorization": f"Bearer {AIPROXY_TOKEN}"}
    payload = {"prompt": prompt, "max_tokens": 150}
    try:
        response = requests.post(LLM_API_URL, json=payload, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()
    except Exception:
        return ""
