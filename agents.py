# agents.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Choose your Gemini model here:
# Options: gemini-2.5-flash, gemini-2.5-pro, gemini-3-pro-preview, etc.
MODEL_NAME = "gemini-2.5-flash"  

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"

def call_gemini(prompt, temperature=0.2, max_tokens=500):
    """
    Corrected Gemini API call using the proper endpoint and payload structure.
    """
    # The API key must be passed as a query parameter
    url = f"{BASE_URL}/{MODEL_NAME}:generateContent?key={API_KEY}"
    
    headers = {
        "Content-Type": "application/json"
    }

    # Gemini API expects 'contents' -> 'parts' -> 'text'
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        # Correct path to extract text from Gemini response
        if "candidates" in data and len(data["candidates"]) > 0:
            content = data["candidates"][0].get("content", {})
            parts = content.get("parts", [])
            if parts:
                return parts[0].get("text", "")
        
        return "Error: No output returned by Gemini API."
        
    except requests.exceptions.RequestException as e:
        # Check if it's a 401/403 (Auth issue) or 404 (Model name issue)
        if hasattr(e.response, 'text'):
            return f"API Error: {e.response.text}"
        return f"Connection Error: {str(e)}"

# ------------------------ Agents ------------------------
# (Rest of your agent functions remain the same as they just pass strings to call_gemini)

# def call_gemini(prompt, temperature=0.2, max_tokens=500):
#     """
#     Call Gemini API and return output.
#     """
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "prompt": prompt,
#         "temperature": temperature,
#         "maxOutputTokens": max_tokens
#     }
#     try:
#         response = requests.post(GEMINI_URL, headers=headers, json=payload, timeout=15)
#         response.raise_for_status()
#         data = response.json()
#         # Check if 'candidates' exist
#         if "candidates" in data and len(data["candidates"]) > 0:
#             return data["candidates"][0].get("output", "")
#         else:
#             return "Error: No output returned by Gemini API."
#     except requests.exceptions.RequestException as e:
#         return f"Error: {str(e)}"

# ------------------------ Agents ------------------------

def agent1_code_analyzer(code):
    prompt = f"""
You are a senior software engineer.
Analyze the following code:

{code}

Tasks:
1. Identify programming language
2. Purpose of the code
3. Key components (loops, functions, classes)
4. Any suspicious logic (do not fix yet)

Return output in structured JSON.
"""
    return call_gemini(prompt)

def agent2_error_detector(code, analysis):
    prompt = f"""
You are a debugging expert.
Given this code and analysis:
Code:
{code}
Analysis:
{analysis}

Tasks:
1. Detect any errors (syntax/logical/runtime)
2. Explain WHY the error occurs
3. If no errors, say 'No errors found'
"""
    return call_gemini(prompt)

def agent3_code_fixer(code, error_info):
    prompt = f"""
You are a code correction agent.
Code:
{code}
Error info:
{error_info}

Tasks:
- If errors exist, provide corrected code and explain changes briefly
- If no errors, respond: "No changes required"
"""
    return call_gemini(prompt)

def agent4_code_explainer(final_code):
    prompt = f"""
Explain the following code clearly:
{final_code}

Tasks:
1. What does the code do?
2. How does it work step-by-step?
3. Key concepts used
Explain in simple language.
"""
    return call_gemini(prompt)
