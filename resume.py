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


def generate_resume_help():
    # Get the user's profile
    profile = get_profile()

       # Create prompt
    prompt = f"""
You are CareerPilot, an AI resume assistant for students and freshers.

Use ONLY the information provided in the user's profile.

User Profile:
Name: {profile.name}
Education: {profile.education}
Current Skills: {", ".join(profile.skills)}
Career Goal: {profile.career_goal}
Experience: {profile.experience}

Create concise, professional resume guidance for this user.

Use this exact format:

RESUME IMPROVEMENT

1. PROFESSIONAL SUMMARY
Write a 2 to 3 sentence professional summary suitable for a fresher.

2. TECHNICAL SKILLS
Organize the user's existing skills into clear categories.
Do not add skills that are not in the profile.

3. EXPERIENCE
Explain how the user's actual experience can be presented.
If the user is a fresher, clearly state that professional experience is limited
and suggest focusing on education, projects, internships, or training that
the user has actually completed.

4. PROJECT BULLET POINTS
Explain how the user's real projects can be written as resume bullet points.
If no project information is provided, do not invent a project.
Instead, give a simple template such as:
- Developed [project] using [technology] to [purpose].
- Implemented [feature] to [purpose].
- Tested/debugged [feature or functionality].

5. RESUME IMPROVEMENT SUGGESTIONS
Give 3 to 5 practical suggestions based on the user's profile.

IMPORTANT RULES:
- Never invent skills.
- Never invent projects.
- Never invent certifications.
- Never invent achievements.
- Never invent job experience.
- Never invent numbers, percentages, users, performance improvements, or results.
- Do not claim the user completed something unless it appears in the profile.
- Keep the content suitable for a fresher.
- Keep the language professional and concise.
- Do not guarantee interviews or jobs.
"""

    # Send prompt to Gemini
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text