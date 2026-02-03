# Multi-Agent Code Explainer & Debugger

A desktop-based Python application that uses multiple AI agents via **Google Gemini API** to analyze, detect errors, fix, and explain code. The UI is built with **Tkinter**, making it interactive and easy to use.

---

## Features

- Analyze code and detect programming language, purpose, and key components.  
- Detect syntax, logical, and runtime errors with explanations.  
- Automatically fix detected errors.  
- Provide step-by-step explanation of code.  
- Interactive Tkinter UI with input box and scrollable output.  
- Clear, tabular-like display of each agent’s output.

---

## Output

After entering your code and clicking **Submit**, you will see:

| Agent | Output |
|-------|--------|
| Agent 1 Analysis | Analysis of your code (language, purpose, key components) |
| Agent 2 Errors   | Detected errors or "No errors found" |
| Agent 3 Fix      | Corrected code or "No changes required" |
| Agent 4 Explanation | Step-by-step explanation in simple language |



---

## Tech Stack

- **Python 3.8+**  
- **Tkinter** → GUI  
- **Requests** → Gemini API calls  
- **python-dotenv** → Securely load API keys from `.env`  

---

## Made by Utkarsh Gupta
