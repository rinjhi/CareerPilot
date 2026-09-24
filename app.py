import streamlit as st
from profile import get_profile, load_profile
from resume import generate_resume_help
from skill_gap import analyze_skill_gap
from roadmap import generate_roadmap

# -----------------------------
# PAGE SETUP
# -----------------------------

st.set_page_config(
    page_title="CareerPilot — AI Career Assistant",
    page_icon="🚀",
    layout="centered"
)

load_profile()
profile = get_profile()

if "interview_started" not in st.session_state:
    st.session_state.interview_started = False
if "interview_messages" not in st.session_state:
    st.session_state.interview_messages = []
if "interview_chat" not in st.session_state:
    st.session_state.interview_chat = None

# -----------------------------
# STYLING
# -----------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

* { font-family: 'Inter', sans-serif !important; }

#MainMenu, footer, header { visibility: hidden; }

/* Deep navy background */
.stApp {
    background: radial-gradient(ellipse at top, #0a1628 0%, #050d1a 50%, #020810 100%);
    min-height: 100vh;
}

/* ── HERO ── */
.hero {
    text-align: center;
    padding: 60px 20px 20px;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, rgba(6,182,212,0.15), rgba(59,130,246,0.15));
    border: 1px solid rgba(6,182,212,0.4);
    color: #67e8f9;
    font-size: 11px;
    font-weight: 700;
    padding: 7px 18px;
    border-radius: 50px;
    margin-bottom: 24px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero-title {
    font-size: 64px;
    font-weight: 900;
    background: linear-gradient(135deg, #38bdf8 0%, #06b6d4 40%, #3b82f6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    margin-bottom: 16px;
    filter: drop-shadow(0 0 40px rgba(6,182,212,0.4));
}

.hero-subtitle {
    font-size: 17px;
    color: #94a3b8;
    font-weight: 400;
    margin-bottom: 6px;
}

.hero-tagline {
    font-size: 13px;
    color: #334155;
    margin-bottom: 40px;
    letter-spacing: 0.5px;
}

/* ── STATS BAR ── */
.stats-bar {
    display: flex;
    justify-content: center;
    gap: 40px;
    background: rgba(6,182,212,0.04);
    border: 1px solid rgba(6,182,212,0.12);
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 40px;
}

.stat-item { text-align: center; }

.stat-number {
    font-size: 22px;
    font-weight: 800;
    background: linear-gradient(135deg, #38bdf8, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-label {
    font-size: 10px;
    color: #475569;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 3px;
}

/* ── SECTION TITLE ── */
.section-title {
    font-size: 21px;
    font-weight: 700;
    color: #e2e8f0;
    margin: 36px 0 16px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(6,182,212,0.5), transparent);
    margin-left: 10px;
}

/* ── PROFILE CARD ── */
.profile-card {
    background: linear-gradient(135deg,
        rgba(6,182,212,0.06) 0%,
        rgba(59,130,246,0.05) 50%,
        rgba(14,165,233,0.04) 100%
    );
    border: 1px solid rgba(6,182,212,0.18);
    border-radius: 24px;
    padding: 28px;
    margin-bottom: 8px;
    position: relative;
    overflow: hidden;
}

.profile-card::before {
    content: '';
    position: absolute;
    top: -60%;
    right: -15%;
    width: 280px;
    height: 280px;
    background: radial-gradient(circle, rgba(6,182,212,0.07), transparent 70%);
    pointer-events: none;
}

.profile-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
}

.profile-item {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(6,182,212,0.1);
    border-radius: 14px;
    padding: 16px 18px;
    transition: border-color 0.3s, background 0.3s;
}

.profile-item:hover {
    border-color: rgba(6,182,212,0.35);
    background: rgba(6,182,212,0.05);
}

.profile-label {
    font-size: 10px;
    font-weight: 700;
    color: #0891b2;
    text-transform: uppercase;
    letter-spacing: 1.3px;
    margin-bottom: 7px;
}

.profile-value {
    font-size: 15px;
    font-weight: 600;
    color: #e2e8f0;
    line-height: 1.4;
}

/* ── BUTTONS ── */
.stButton > button {
    background: linear-gradient(135deg,
        rgba(6,182,212,0.12),
        rgba(59,130,246,0.08)
    ) !important;
    color: #bae6fd !important;
    border: 1px solid rgba(6,182,212,0.3) !important;
    border-radius: 14px !important;
    padding: 16px 20px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    backdrop-filter: blur(10px) !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg,
        rgba(6,182,212,0.28),
        rgba(59,130,246,0.2)
    ) !important;
    border-color: rgba(56,189,248,0.7) !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 30px rgba(6,182,212,0.2) !important;
    color: #ffffff !important;
}

/* Ask button — solid cyan */
.ask-btn .stButton > button {
    background: linear-gradient(135deg, #0891b2, #2563eb) !important;
    border: none !important;
    color: #ffffff !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    padding: 18px 20px !important;
    box-shadow: 0 4px 20px rgba(8,145,178,0.35) !important;
}

.ask-btn .stButton > button:hover {
    background: linear-gradient(135deg, #0e7490, #1d4ed8) !important;
    box-shadow: 0 8px 32px rgba(8,145,178,0.5) !important;
    transform: translateY(-3px) !important;
}

/* ── RESULT BOX ── */
.result-box {
    background: linear-gradient(135deg,
        rgba(5,15,35,0.9),
        rgba(5,25,50,0.7)
    );
    border: 1px solid rgba(6,182,212,0.2);
    border-left: 4px solid #06b6d4;
    border-radius: 18px;
    padding: 28px;
    margin-top: 16px;
}

/* ── TEXT AREA ── */
.stTextArea > div > div > textarea {
    background: rgba(6,182,212,0.04) !important;
    border: 1px solid rgba(6,182,212,0.2) !important;
    border-radius: 14px !important;
    color: #e2e8f0 !important;
    font-size: 15px !important;
    padding: 16px !important;
    resize: none !important;
}

.stTextArea > div > div > textarea:focus {
    border-color: #06b6d4 !important;
    box-shadow: 0 0 0 3px rgba(6,182,212,0.12) !important;
}

/* ── DIVIDER ── */
.glow-divider {
    height: 1px;
    background: linear-gradient(90deg,
        transparent,
        rgba(6,182,212,0.5),
        rgba(59,130,246,0.3),
        transparent
    );
    margin: 36px 0;
    border: none;
}

/* ── CHAT ── */
.stChatMessage {
    background: rgba(6,182,212,0.03) !important;
    border: 1px solid rgba(6,182,212,0.1) !important;
    border-radius: 16px !important;
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    padding: 50px 0 30px;
    color: #1e3a5f;
    font-size: 13px;
    line-height: 2.2;
}

.footer .highlight {
    color: #0891b2;
    font-weight: 600;
}

.footer .made-with {
    color: #334155;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO
# -----------------------------

st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ Powered by Gemini AI</div>
    <div class="hero-title">🚀 CareerPilot</div>
    <div class="hero-subtitle">Your personal AI career co-pilot</div>
    <div class="hero-tagline">Resume &nbsp;·&nbsp; Skills &nbsp;·&nbsp; Roadmap &nbsp;·&nbsp; Interview &nbsp;·&nbsp; Career Q&amp;A</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="stats-bar">
    <div class="stat-item">
        <div class="stat-number">5</div>
        <div class="stat-label">AI Tools</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">100%</div>
        <div class="stat-label">Personalized</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">Free</div>
        <div class="stat-label">Always</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">AI</div>
        <div class="stat-label">Powered</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# PROFILE
# -----------------------------

st.markdown('<div class="section-title">👤 My Profile</div>', unsafe_allow_html=True)

profile_html = (
    '<div class="profile-card">'
    '<div class="profile-grid">'
    '<div class="profile-item">'
    '<div class="profile-label">🎓 Education</div>'
    '<div class="profile-value">{education}</div>'
    '</div>'
    '<div class="profile-item">'
    '<div class="profile-label">🎯 Career Goal</div>'
    '<div class="profile-value">{career_goal}</div>'
    '</div>'
    '<div class="profile-item">'
    '<div class="profile-label">⚡ Skills</div>'
    '<div class="profile-value">{skills}</div>'
    '</div>'
    '<div class="profile-item">'
    '<div class="profile-label">💼 Experience</div>'
    '<div class="profile-value">{experience}</div>'
    '</div>'
    '</div>'
    '</div>'
).format(
    education=profile.education,
    career_goal=profile.career_goal,
    skills=", ".join(profile.skills),
    experience=profile.experience
)

st.markdown(profile_html, unsafe_allow_html=True)

# -----------------------------
# CAREER TOOLS
# -----------------------------

st.markdown('<hr class="glow-divider">', unsafe_allow_html=True)
st.markdown('<div class="section-title">🛠️ Career Tools</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    if st.button("📄  Improve Resume", use_container_width=True):
        with st.spinner("Analyzing your resume profile..."):
            result = generate_resume_help()
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("📄 Resume Improvement")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if st.button("📊  Skill Gap Analysis", use_container_width=True):
        with st.spinner("Analyzing your skill gap..."):
            result = analyze_skill_gap()
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("📊 Skill Gap Analysis")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)

col3, col4 = st.columns(2, gap="medium")

with col3:
    if st.button("🗺️  Learning Roadmap", use_container_width=True):
        with st.spinner("Creating your learning roadmap..."):
            result = generate_roadmap()
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("🗺️ Learning Roadmap")
        st.write(result)
        st.markdown('</div>', unsafe_allow_html=True)

with col4:
    if st.button("🎤  Mock Interview", use_container_width=True):
        from interview import create_interview_chat
        with st.spinner("Starting your mock interview..."):
            st.session_state.interview_chat = create_interview_chat()
            first_question = (
                st.session_state.interview_chat
                .send_message("Start the mock interview.")
            )
        st.session_state.interview_started = True
        st.session_state.interview_messages = [
            {"role": "assistant", "content": first_question.text}
        ]
        st.rerun()

# -----------------------------
# MOCK INTERVIEW
# -----------------------------

if st.session_state.interview_started:
    st.markdown('<hr class="glow-divider">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎤 Mock Interview</div>', unsafe_allow_html=True)

    for message in st.session_state.interview_messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    answer = st.chat_input("Type your interview answer...")

    if answer:
        st.session_state.interview_messages.append(
            {"role": "user", "content": answer}
        )
        from interview import get_interview_response
        with st.spinner("CareerPilot is evaluating your answer..."):
            response = get_interview_response(
                st.session_state.interview_chat, answer
            )
        st.session_state.interview_messages.append(
            {"role": "assistant", "content": response}
        )
        st.rerun()

# -----------------------------
# ASK CAREERPILOT
# -----------------------------

st.markdown('<hr class="glow-divider">', unsafe_allow_html=True)
st.markdown('<div class="section-title">💬 Ask CareerPilot</div>', unsafe_allow_html=True)

question = st.text_area(
    "question",
    placeholder="e.g. How should I prepare for a Python developer role?",
    height=130,
    label_visibility="collapsed"
)

st.markdown('<div class="ask-btn">', unsafe_allow_html=True)
if st.button("🚀  Ask CareerPilot", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        from careerpilot import ask_careerpilot
        with st.spinner("CareerPilot is thinking..."):
            answer = ask_careerpilot(question)
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("💬 CareerPilot")
        st.write(answer)
        st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("""
<div class="footer">
    <div class="made-with">Built  using Python &nbsp;·&nbsp; Streamlit &nbsp;·&nbsp; Gemini API</div>
    <div><span class="highlight">🚀 CareerPilot</span> &nbsp;·&nbsp; AI Career Assistant for Students &amp; Freshers</div>
</div>
""", unsafe_allow_html=True)
