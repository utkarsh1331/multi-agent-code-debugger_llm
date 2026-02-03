import tkinter as tk
from tkinter import scrolledtext, messagebox
from agents import agent1_code_analyzer, agent2_error_detector, agent3_code_fixer, agent4_code_explainer

def run_agents():
    code = code_text.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Input Error", "Please enter some code.")
        return

    # Agent 1
    analysis = agent1_code_analyzer(code)

    # Agent 2
    errors = agent2_error_detector(code, analysis)

    # Agent 3
    if "No errors found" in errors:
        final_code = code
        fixed_code = "No changes required"
    else:
        fixed_code = agent3_code_fixer(code, errors)
        final_code = fixed_code

    # Agent 4
    explanation = agent4_code_explainer(final_code)

    # Display results in tabular-like format
    output_text.config(state='normal')
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"{'Agent':<15} | {'Output'}\n")
    output_text.insert(tk.END, "-"*70 + "\n")
    output_text.insert(tk.END, f"{'Agent 1 Analysis':<15} | {analysis}\n")
    output_text.insert(tk.END, f"{'Agent 2 Errors':<15} | {errors}\n")
    output_text.insert(tk.END, f"{'Agent 3 Fix':<15} | {fixed_code}\n")
    output_text.insert(tk.END, f"{'Agent 4 Explanation':<15} | {explanation}\n")
    output_text.config(state='disabled')

# Tkinter UI
root = tk.Tk()
root.title("Multi-Agent Code Explainer & Debugger")

tk.Label(root, text="Enter your code:").pack()
code_text = scrolledtext.ScrolledText(root, width=80, height=10)
code_text.pack()

tk.Button(root, text="Submit", command=run_agents).pack(pady=10)

tk.Label(root, text="Output:").pack()
output_text = scrolledtext.ScrolledText(root, width=100, height=20, state='disabled')
output_text.pack()

root.mainloop()
