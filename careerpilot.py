import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

client = genai.Client(api_key=api_key)

def ask_careerpilot(question, education="", career_goal="", skills="", experience=""):

    # Build profile context from session state values
    instructions = f"""
You are CareerPilot, an AI career assistant.

Your job is to help students and freshers with:
- Career planning
- Skill development
- Job preparation
- Resume improvement
- Interview preparation
- Learning roadmaps

Give practical, realistic, beginner-friendly advice.

Important rules:
1. Do not present one career path as universally best.
2. Consider the user's background, goals, existing skills, and target role.
3. When multiple options are reasonable, explain the trade-offs.
4. Clearly distinguish facts, common industry practices, and personal recommendations.
5. Avoid unsupported promises or guaranteed outcomes.
6. If the user's goal is unclear, ask a clarifying question.
7. Prefer actionable steps, realistic timelines, and concrete examples.

User Profile:
Education: {education}
Skills: {skills}
Career Goal: {career_goal}
Experience: {experience}

Use this profile to personalize your answers.
Do not invent information that is not present in the profile.
"""

    # Send question with profile context
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"{instructions}\n\nUser question: {question}"
    )

    return response.text
