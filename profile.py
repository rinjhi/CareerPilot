import json
import os


PROFILE_FILE = "profile.json"


class UserProfile:
    def __init__(self):
        self.name = ""
        self.education = ""
        self.skills = []
        self.career_goal = ""
        self.experience = ""


# Create a user profile
profile = UserProfile()


def save_profile():
    data = {
        "name": profile.name,
        "education": profile.education,
        "skills": profile.skills,
        "career_goal": profile.career_goal,
        "experience": profile.experience
    }

    with open(PROFILE_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_profile():
    if not os.path.exists(PROFILE_FILE):
        return

    # If the file is empty, do nothing
    if os.path.getsize(PROFILE_FILE) == 0:
        return

    with open(PROFILE_FILE, "r") as file:
        data = json.load(file)

    profile.name = data.get("name", "")
    profile.education = data.get("education", "")
    profile.skills = data.get("skills", [])
    profile.career_goal = data.get("career_goal", "")
    profile.experience = data.get("experience", "")


def get_profile():
    return profile


def update_profile():
    print("\nUpdate Your Career Profile")
    print("--------------------------")

    name = input("Name: ").strip()
    education = input("Education: ").strip()
    skills = input("Skills (comma separated): ").strip()
    career_goal = input("Career Goal: ").strip()
    experience = input("Experience: ").strip()

    profile.name = name
    profile.education = education
    profile.skills = [skill.strip() for skill in skills.split(",")]
    profile.career_goal = career_goal
    profile.experience = experience

    save_profile()

    print("\nProfile updated and saved successfully!")