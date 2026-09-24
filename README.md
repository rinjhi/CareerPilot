# 🚀 CareerPilot

**AI-Powered Career Assistant for Students & Freshers**

CareerPilot is a Streamlit-based AI career assistant that helps students and freshers improve their resumes, identify skill gaps, create learning roadmaps, prepare for interviews, and ask career-related questions.

Built with Python, Streamlit, and the Gemini API.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 Resume Improvement | AI-generated resume suggestions based on your profile |
| 📊 Skill Gap Analysis | Identifies missing skills for your target career goal |
| 🗺️ Learning Roadmap | Personalized 3-month learning plan |
| 🎤 Mock Interview | AI-powered mock interview with feedback |
| 💬 Ask CareerPilot | Ask any career-related question and get AI answers |

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **Programming:** Python
- **AI:** Google Gemini API
- **Environment:** python-dotenv
- **Version Control:** Git & GitHub
- **Deployment:** Streamlit Community Cloud

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/rinjhi/CareerPilot.git
cd CareerPilot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the project folder:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your free API key from [Google AI Studio](https://aistudio.google.com/).

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
CareerPilot/
├── app.py              # Main Streamlit UI
├── careerpilot.py      # Gemini chat session for Ask CareerPilot
├── main.py             # Terminal-based CLI version
├── profile.py          # User profile management
├── resume.py           # Resume improvement feature
├── skill_gap.py        # Skill gap analysis feature
├── roadmap.py          # Learning roadmap feature
├── interview.py        # Mock interview feature
├── requirements.txt    # Python dependencies
└── .env                # API key (not uploaded to GitHub)
```

---

## 👤 Author

**Rinjhi** — BCA Student | Aspiring Software Developer

---

## 📄 License

This project is open source and available under the MIT License.
