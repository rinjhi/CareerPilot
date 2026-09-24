import os
from dotenv import load_dotenv
from google import genai
from profile import get_profile, load_profile

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

client = genai.Client(api_key=api_key)

load_profile()

def create_instructions():
    profile = get_profile()
    profile_context = f"""
User Profile:
Name: {profile.name}
Education: {profile.education}
Skills: {", ".join(profile.skills)}
Career Goal: {profile.career_goal}
Experience: {profile.experience}
"""
    return f"""
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

Here is the user's current profile:
{profile_context}

Use this profile to personalize your answers.
Do not invent information that is not present in the profile.
"""

def create_chat():
    return client.chats.create(
        model="gemini-3.5-flash",
        config={"system_instruction": create_instructions()}
    )

# Single shared chat session
_chat = create_chat()

def ask_careerpilot(question):
    response = _chat.send_message(question)
    return response.text
