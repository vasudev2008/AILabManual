# Experiment 12: AI-Assisted Generation of Technical Content and Python Programs
# Supplementary implementation based on the Experiment 12 title in the manual index.
# Generate a structured request, then paste it into a Generative AI tool.
topic = input("Enter a technical topic: ")
audience = input("Target audience (example: first-year CSE student): ")
content_type = input("Content type (notes / explanation / Python program): ")

if content_type.lower() == "python program":
    requirements = (
        "Write a complete beginner-friendly Python program. Include comments, "
        "input validation, sample input/output, and a short explanation."
    )
elif content_type.lower() == "notes":
    requirements = (
        "Create concise notes with headings, definitions, key points, "
        "and one simple example."
    )
else:
    requirements = (
        "Explain the topic step by step using simple language and a practical example."
    )

prompt = f"""You are a patient technical instructor.
Topic: {topic}
Audience: {audience}
Requested output: {content_type}
Requirements: {requirements}

Do not invent facts. Explain assumptions and keep the result suitable for learning."""

print("\\n--- Copy this prompt into a Generative AI tool ---")
print(prompt)

print("\\nReminder: Run AI-generated code only after reading it, checking its logic, "
      "and testing it with safe sample inputs.")
