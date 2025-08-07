import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

client = genai.Client()

def generate_summary(text):
    prompt = f"Summarize the following text in simple language:\n\n{text}"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()

def generate_quiz(text):
    prompt = (
        f"From the following notes, create 5 multiple-choice questions. "
        f"Each should have 4 options (a–d), and clearly indicate the correct answer.\n\n"
        f"{text}\n\n"
        "Format:\n"
        "Q1. ...\n(a) ...\n(b) ...\n(c) ...\n(d) ...\nAnswer: (x)"
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()

def answer_doubt(text, question):
    prompt = (
        f"You are a helpful tutor. Use the provided notes to answer the question:\n\n"
        f"Notes:\n{text}\n\n"
        f"Question: {question}\n\n"
        f"If the answer is not in the notes, provide a general explanation based on your knowledge."
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text.strip()