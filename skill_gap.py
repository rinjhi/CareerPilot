import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

def analyze_skill_gap(profile_data=None):

    # If called from Streamlit, use profile_data from session state
    # If called from main.py CLI, use profile.json
    if profile_data is None:
        from profile import get_profile
        p = get_profile()
        profile_data = {
            "education": p.education,
            "career_goal": p.career_goal,
            "skills": p.skills,
            "experience": p.experience
        }

    # Handle skills as either a list or comma-separated string
    skills = profile_data["skills"]
    if isinstance(skills, list):
        skills_str = ", ".join(skills)
    else:
        skills_str = skills

    # Create prompt
    prompt = f"""
You are CareerPilot, a career skill gap analyzer for students and freshers.

Analyze the user's current skills based on their career goal.

User Profile:
Education: {profile_data['education']}
Current Skills: {skills_str}
Career Goal: {profile_data['career_goal']}
Experience: {profile_data['experience']}

📊 SKILL GAP ANALYSIS

CURRENT SKILLS
- List the skills the user already has.

SKILLS TO LEARN NEXT

1. Skill Name
   Why: Explain why this skill is useful for the user's career goal.
   Next Step: Give one simple beginner action.

2. Skill Name
   Why: Explain why this skill is useful for the user's career goal.
   Next Step: Give one simple beginner action.

3. Skill Name
   Why: Explain why this skill is useful for the user's career goal.
   Next Step: Give one simple beginner action.

PRIORITY

High Priority:
- List the most important skills to learn first.

Medium Priority:
- List useful supporting skills.

LEARNING TIP
Give one short practical tip for the user.

Rules:
- Recommend only 3 to 5 skills.
- Do not recommend skills the user already has.
- Focus only on the user's career goal.
- Keep explanations beginner-friendly.
- Do not invent information about the user.
"""

    # Send prompt to Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text
