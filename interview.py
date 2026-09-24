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


def create_interview_chat():
    # Get the user's profile
    profile = get_profile()

    # Create profile information
    profile_context = f"""
Name: {profile.name}
Education: {profile.education}
Skills: {", ".join(profile.skills)}
Career Goal: {profile.career_goal}
Experience: {profile.experience}
"""

    # Interview instructions
    prompt = f"""
You are CareerPilot, conducting a beginner-friendly mock interview.

User Profile:
{profile_context}

The user is a fresher preparing for a software developer role.

Start the interview by asking:

"Tell me about yourself."

After the user answers:
1. Give short and useful feedback.
2. Mention one strength.
3. Mention one improvement.
4. Ask the next relevant interview question.

Ask questions based on the user's profile and career goal.

Possible topics:
- Introduction
- Python
- C
- SQL
- Basic DSA
- Projects
- Software development
- HR/behavioral questions

Keep questions suitable for a fresher.

Do not ask very difficult questions initially.
Do not provide the answer before the user responds.
"""

    # Create interview chat
    interview_chat = client.chats.create(
        model="gemini-3.5-flash",
        config={
            "system_instruction": prompt
        }
    )

    return interview_chat


def start_interview():
    """
    Terminal-based mock interview.
    """

    interview_chat = create_interview_chat()

    print("\nCareerPilot: Welcome to your Mock Interview!")
    print("CareerPilot: Type 'exit' anytime to end the interview.\n")

    # Start interview
    first_question = interview_chat.send_message(
        "Start the mock interview."
    )

    print("CareerPilot:")
    print(first_question.text)
    print()

    # Interview loop
    while True:

        answer = input("You: ").strip()

        if answer.lower() == "exit":

            print("\nCareerPilot: Mock interview ended.")
            print("Keep practicing and improving your interview skills!\n")

            break

        if not answer:

            print("CareerPilot: Please provide an answer.\n")

            continue

        response = interview_chat.send_message(answer)

        print("\nCareerPilot:")
        print(response.text)
        print()


def get_interview_response(interview_chat, answer):
    """
    Send the user's interview answer to Gemini
    and return CareerPilot's response.
    """

    response = interview_chat.send_message(answer)

    return response.text