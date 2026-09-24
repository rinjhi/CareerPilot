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


def analyze_skill_gap():
    # Get the user's profile
    profile = get_profile()

    # Create prompt
    prompt = f"""
You are CareerPilot, a career skill gap analyzer for students and freshers.

Analyze the user's current skills based on their career goal.

User Profile:
Name: {profile.name}
Education: {profile.education}
Current Skills: {", ".join(profile.skills)}
Career Goal: {profile.career_goal}
Experience: {profile.experience}

Provide the analysis in this format:

SKILL GAP ANALYSIS

Current Skills:
- List the user's existing skills

Skills to Learn Next:

1. Skill name
   Why: Short explanation
   Next Step: What the beginner should do

2. Skill name
   Why: Short explanation
   Next Step: What the beginner should do

3. Skill name
   Why: Short explanation
   Next Step: What the beginner should do

Provide the analysis in this format:

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