import os
from dotenv import load_dotenv
from agno.models.google import Gemini

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

model = Gemini(
    id="gemini-2.5-flash",
    api_key=api_key
)