# utils.py

import re
import openai
from dotenv import load_dotenv
load_dotenv()

import os
openai.api_key = os.getenv("OPENAI_API_KEY")
def validate_email(email: str) -> bool:
    """
    Validate the format of an email address using regex.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def validate_phone(phone: str) -> bool:
    """
    Validate phone numbers (simple version: digits, length 10-15).
    """
    pattern = r"^\+?\d{10,15}$"
    return re.match(pattern, phone) is not None


def generate_questions(tech_stack: list) -> dict:
    """
    Generate 3-5 technical questions for each technology in the given tech stack
    using OpenAI's language model.

    Args:
        tech_stack (list): List of technology strings.

    Returns:
        dict: Mapping of tech -> list of questions.
    """
    questions = {}
    for tech in tech_stack:
        prompt = (
            f"Generate 3-5 technical interview questions to assess proficiency in {tech}."
            f" The questions should be challenging, relevant, and concise."
        )
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a technical interviewer."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.7
            )
            content = response.choices[0].message.content.strip()
            # Split questions into list
            questions[tech] = [q.strip("- ") for q in content.split("\n") if q.strip()]
        except Exception as e:
            questions[tech] = [f"Error generating questions for {tech}: {e}"]

    return questions
