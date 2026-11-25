# Experiment 10: Prompt Design and Evaluation Using Generative AI
# Supplementary implementation based on the Experiment 10 title in the manual index.
# This program prepares prompts and evaluates a response pasted by the student.
def build_prompt(task, context, constraints):
    return f"""Task: {task}

Context: {context}

Constraints:
{constraints}

Please provide a clear, accurate, well-structured answer.
If information is missing, state your assumptions instead of inventing facts."""

task = input("Enter the task for Generative AI: ")
context = input("Enter relevant context: ")
constraints = input("Enter constraints (format, length, audience, etc.): ")

prompt = build_prompt(task, context, constraints)
print("\\n--- Prompt to paste into a Generative AI tool ---")
print(prompt)

response = input("\\nPaste the AI response here (or press Enter to skip): ").strip()
if response:
    checks = {
        "Non-empty response": bool(response),
        "Contains multiple lines": "\\n" in response,
        "Within 2000 characters": len(response) <= 2000,
    }
    print("\\n--- Basic Response Evaluation ---")
    for label, passed in checks.items():
        print(f"{label}: {'Pass' if passed else 'Review'}")
    print("Character count:", len(response))
else:
    print("No response supplied. Review the AI output manually for accuracy, relevance and clarity.")
