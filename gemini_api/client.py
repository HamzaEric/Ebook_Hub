import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found in .env file")

client = genai.Client(api_key=api_key)


def ai_prompt(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text
    )
    return response.text


def get_author_ai_bio(name):
    prompt = f"""
    Show me a short biography of the author {name} in no more than 250 characters.
    """
    return ai_prompt(prompt)


def get_book_ai_synopsis(title):
    prompt = f"""
    Show me a short synopsis of the book {title} in no more than 250 characters.
    """
    return ai_prompt(prompt)


def get_ai_genre(name):
    prompt = f"""
    Show me a short description of the literary genre {name} in no more than 250 characters.
    """
    return ai_prompt(prompt)
