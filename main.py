import os
from dotenv import load_dotenv
from google import genai
from profile import get_profile, update_profile, load_profile
from skill_gap import analyze_skill_gap
from roadmap import generate_roadmap
from interview import start_interview
from resume import generate_resume_help

# Load environment variables
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")


# Create Gemini client
client = genai.Client(api_key=api_key)


# Load saved user profile
load_profile()

# Get user profile
profile = get_profile()


# Create profile context
def create_profile_context():
    return f"""
User Profile:
Name: {profile.name}
Education: {profile.education}
Skills: {", ".join(profile.skills)}
Career Goal: {profile.career_goal}
Experience: {profile.experience}
"""


# Create CareerPilot instructions
def create_instructions():
    profile_context = create_profile_context()

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
3. When multiple options are reasonable, explain the trade-offs instead of forcing one choice.
4. Clearly distinguish facts, common industry practices, and personal recommendations.
5. Avoid unsupported promises, exaggerated claims, guaranteed outcomes, or claims about what recruiters will definitely prefer.
6. Do not assume that a particular technology is required unless it is relevant to the user's target role.
7. If the user's goal is unclear, ask a short clarifying question or provide options based on common career paths.
8. Prefer actionable steps, realistic timelines, and concrete examples.

Here is the user's current profile:

{profile_context}

Use this profile to personalize your answers.
Do not invent information that is not present in the profile.
"""


# Create chat session
def create_chat():
    return client.chats.create(
        model="gemini-3.5-flash",
        config={
            "system_instruction": create_instructions()
        }
    )


# Create initial chat
chat = create_chat()


# Function to send questions to CareerPilot
def ask_careerpilot(question):
    response = chat.send_message(question)
    return response.text


# Display profile
def show_profile():
    print("\nCareerPilot User Profile")
    print("------------------------")
    print("Name:", profile.name)
    print("Education:", profile.education)
    print("Skills:", ", ".join(profile.skills))
    print("Career Goal:", profile.career_goal)
    print("Experience:", profile.experience)
    print()


# Start conversation
print("\nCareerPilot is ready!")
print("Type 'help' to see commands.")
print("Type 'exit' to end the conversation.\n")


while True:
    question = input("You: ").strip()

    # Exit command
    if question.lower() == "exit":
        print("\nCareerPilot: Goodbye! Keep building your career.")
        break


    # Help command
    if question.lower() == "help":
        print("\nCareerPilot commands:")
        print("- help → Show available commands")
        print("- profile → Show your career profile")
        print("- update profile → Update your career profile")
        print("- skill gap → Analyze your career skill gap")
        print("- roadmap → Generate your learning roadmap")
        print("- interview → Start an AI mock interview")
        print("- resume → Get AI resume improvement suggestions")
        print("- exit → End the conversation")
        print("- You can also ask CareerPilot any career-related question.\n")
        continue


    # Profile command
    if question.lower() == "profile":
        show_profile()
        continue


    # Update profile command
    if question.lower() == "update profile":
        update_profile()

        # Recreate chat so Gemini gets the updated profile
        chat = create_chat()

        print("CareerPilot: Your profile has been updated.")
        print("CareerPilot: I will now use your updated profile for future answers.\n")

        continue
        # Skill gap command
    if question.lower() == "skill gap":
        print("\nCareerPilot: Analyzing your skill gap...\n")

        result = analyze_skill_gap()

        print("CareerPilot:")
        print(result)
        print()
        continue
        # Roadmap command
    if question.lower() == "roadmap":
        print("\nCareerPilot: Creating your learning roadmap...\n")

        result = generate_roadmap()

        print("CareerPilot:")
        print(result)
        print()
        continue
    # Interview command
    if question.lower() == "interview":
        start_interview()
        continue

    # Resume command
    if question.lower() == "resume":
      print("\nCareerPilot: Analyzing your resume profile...\n")

      result = generate_resume_help()

      print("CareerPilot:")
      print(result)
      print()
      continue   
       
    # Empty input
    if not question:
        print("CareerPilot: Please enter a question.")
        continue


    # Send question to Gemini
    answer = ask_careerpilot(question)

    print("\nCareerPilot:")
    print(answer)
    print()