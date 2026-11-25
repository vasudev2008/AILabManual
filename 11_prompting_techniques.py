# Experiment 11: Role-Based, Zero-Shot, One-Shot and Few-Shot Prompting
# Supplementary implementation based on the Experiment 11 title in the manual index.
task = input("Enter a task (example: explain photosynthesis): ")
role = input("Enter a role (example: science tutor): ")

zero_shot = f"Complete this task: {task}. Give a clear and accurate answer."

role_based = (
    f"Act as a {role}. Complete this task: {task}. "
    "Use beginner-friendly language and a short example."
)

one_shot = f"""Task: {task}

Example input: Explain evaporation.
Example output: Evaporation is the process in which a liquid changes into a gas.

Now complete the original task using a similar style."""

few_shot = f"""Task: {task}

Example 1
Question: Define a variable.
Answer: A variable is a named place used to store a value.

Example 2
Question: Define a loop.
Answer: A loop repeats a block of instructions.

Now answer the original task in the same concise question-and-answer style."""

print("\\n--- Zero-Shot Prompt ---\\n", zero_shot)
print("\\n--- Role-Based Prompt ---\\n", role_based)
print("\\n--- One-Shot Prompt ---\\n", one_shot)
print("\\n--- Few-Shot Prompt ---\\n", few_shot)
