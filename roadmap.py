import os
from google import genai
from dotenv import load_dotenv
from profile import get_profile

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


def generate_roadmap():
    # Get the user's profile
    profile = get_profile()

    # Create prompt
    prompt = f"""
You are CareerPilot, an AI career learning roadmap generator.

Create a simple, realistic and personalized 3-month learning roadmap
based on the user's current skills and career goal.

USER PROFILE
Name: {profile.name}
Education: {profile.education}
Current Skills: {", ".join(profile.skills)}
Career Goal: {profile.career_goal}
Experience: {profile.experience}

Create the roadmap in this format:

🗺️ LEARNING ROADMAP

CAREER GOAL
{profile.career_goal}

MONTH 1 — FOUNDATION
Topics:
- Topic 1
- Topic 2

Practice:
- Simple coding/practice activities

Project/Task:
- One small practical task

MONTH 2 — SKILL DEVELOPMENT
Topics:
- Topic 1
- Topic 2

Practice:
- Simple coding/practice activities

Project/Task:
- One small practical task

MONTH 3 — PRACTICAL APPLICATION
Topics:
- Topic 1
- Topic 2

Practice:
- Simple coding/practice activities

Project/Task:
- One small practical project

DAILY PRACTICE
- Give a realistic daily practice routine.

TOOLS & PLATFORMS
- Recommend a short list of useful learning platforms or tools.

IMPORTANT RULES:
1. Keep the roadmap beginner-friendly.
2. Build on the user's existing skills.
3. Focus only on skills relevant to the career goal.
4. Recommend only 2 to 3 major skills per month.
5. Do not introduce many technologies at once.
6. Teach fundamentals before advanced frameworks.
7. Include practical coding practice.
8. Include one project or task each month.
9. Keep the roadmap realistic.
10. Do not guarantee a job or career outcome.
11. Do not recommend skills the user already knows unless they need practice.
12. Keep the explanation concise and easy to follow.
"""

    # Send prompt to Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text