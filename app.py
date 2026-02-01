import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_page_config(page_title="Election Sports Arena", layout="wide", page_icon="🗳️")

# --- Custom Styling ---
st.markdown("""
    <style>
    .game-container {
        border: 5px solid #006a4e;
        background-color: #2e7d32;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; background-color: #006a4e; color: white; border: none; }
    .stButton>button:hover { background-color: #004d39; color: #ffd700; }
    .problem-card {
        background-color: #f7f7f7;
        border-left: 5px solid #ff4b4b;
        padding: 15px;
        margin-top: 15px;
        border-radius: 8px;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🗳️ Election Sports Battle 2026")

# --- Session State ---
if 'c1_pop' not in st.session_state:
    st.session_state.update({
        'c1_pop': 50, 
        'c2_pop': 50, 
        'current_problem': None,
        'problem_solved_count': 0
    })

# --- Candidate Setup ---
col1, col2 = st.columns(2)
with col1:
    c1_name = st.text_input("Candidate 1 Name:", value="Candidate A")
    c1_mark = st.selectbox("Symbol 1:", ["ধানের শীষ 🌾🌾", "দাঁড়িপাল্লা ⚖️", "গরুর গাড়ি 🐂", "নৌকা ⛵", "লাঙ্গল 🚜"])
with col2:
    c2_name = st.text_input("Candidate 2 Name:", value="Candidate B")
    c2_mark = st.selectbox("Symbol 2:", ["দাঁড়িপাল্লা ⚖️", "ধানের শীষ 🌾🌾", "গরুর গাড়ি 🐂", "নৌকা ⛵", "লাঙ্গল 🚜"], index=1)

st.divider()

# --- Popularity Meter ---
st.markdown(f"""
    <div class="game-container">
        <h3>📊 Live Popularity Meter</h3>
        <p><strong>{c1_name} ({c1_mark}):</strong> {st.session_state.c1_pop}% | <strong>{c2_name} ({c2_mark}):</strong> {st.session_state.c2_pop}%</p>
    </div>
    """, unsafe_allow_html=True)

# --- Game Tabs ---
tab1, tab2, tab3 = st.tabs(["⚽ Football", "🏏 Cricket", "🤝 Public Outreach"])

# --- TAB 1: FOOTBALL ---
with tab1:
    st.subheader("Penalty Shootout!")
    shot_col1, shot_col2, shot_col3 = st.columns(3)
    shot = None
    if shot_col1.button("Shoot Left"): shot = "L"
    if shot_col2.button("Shoot Center"): shot = "C"
    if shot_col3.button("Shoot Right"): shot = "R"
    
    if shot:
        if shot != random.choice(["L", "C", "R"]):
            st.success("⚽ GOAL!")
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 5)
        else:
            st.error("❌ SAVED!")

# --- TAB 2: CRICKET ---
with tab2:
    st.subheader("Cricket Batting")
    timing = st.select_slider("Timing:", options=["Early", "Perfect", "Late"])
    if st.button("Hit the Ball"):
        if timing == "Perfect":
            st.success("🚀 SIX!")
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 10)
        else:
            st.info("🏃 Single Run")
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 1)

# --- TAB 3: PUBLIC OUTREACH (Fixed Image Error) ---
with tab3:
    st.subheader("Engagement with Citizens")
    
    # Static Cartoon Image Link (Error fixed)
    st.image("https://img.freepik.com/free-vector/politician-speaking-crowd_23-2147514164.jpg", 
             caption="Leader meeting the public", use_container_width=True)

    if st.session_state.current_problem is None:
        if st.button("Meet People"):
            problems = [
                {"text": "Bad Road conditions in the village.", "cost": 10, "gain": 15},
                {"text": "Water shortage in rural areas.", "cost": 15, "gain": 20},
                {"text": "Electricity Load-shedding issue.", "cost": 5, "gain": 12}
            ]
            st.session_state.current_problem = random.choice(problems)
            st.rerun()

    if st.session_state.current_problem:
        prob = st.session_state.current_problem
        st.markdown(f"<div class='problem-card'><b>Problem:</b> {prob['text']}</div>", unsafe_allow_html=True)
        if st.button(f"Solve (+{prob['gain']} Pop)"):
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + prob['gain'])
            st.session_state.current_problem = None
            st.success("Problem Solved!")
            st.rerun()

# --- Win Condition ---
if st.session_state.c1_pop >= 95:
    st.balloons()
    st.header(f"🎊 {c1_name} ({c1_mark}) Won the Election! 🎊")
    if st.button("Restart Election"):
        st.session_state.c1_pop = 50
        st.rerun()
