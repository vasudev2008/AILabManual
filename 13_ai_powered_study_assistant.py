# Experiment 13: AI-Powered Study Assistant Using Python and Generative AI
# Supplementary implementation based on the Experiment 13 title in the manual index.
# Optional live API mode uses the OpenAI Python SDK and OPENAI_API_KEY environment variable.
import os

def offline_study_prompt(topic, question):
    return f"""You are a study assistant for a beginner student.
Topic: {topic}
Student question: {question}

Explain step by step in simple language.
Include a short example and finish with three key points.
If you are unsure, say so rather than guessing."""

topic = input("Enter the topic you are studying: ")
question = input("Ask your question: ")
prompt = offline_study_prompt(topic, question)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("\\nOPENAI_API_KEY was not found.")
    print("Copy the following prompt into your preferred Generative AI tool:")
    print("\\n" + prompt)
else:
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        result = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=prompt
        )
        print("\\n--- Study Assistant Answer ---")
        print(result.output_text)
    except ImportError:
        print("Install the SDK with: pip install openai")
        print("\\nPrompt:\\n", prompt)
    except Exception as error:
        print("The AI request could not be completed:", error)
        print("You can still use this prompt manually:\\n", prompt)
