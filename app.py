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
    .goal-text { color: green; font-size: 25px; font-weight: bold; text-align: center; }
    .miss-text { color: red; font-size: 25px; font-weight: bold; text-align: center; }
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

st.title("🗳️ Election Sports Battle: সরাসরি ময়দানে লড়াই!")

# --- Session State ---
if 'c1_pop' not in st.session_state:
    st.session_state.update({
        'c1_pop': 50, 
        'c2_pop': 50, 
        'msg': "খেলা শুরু করুন!",
        'current_problem': None, # জনসংযোগের জন্য
        'problem_solved_count': 0 # সমস্যা সমাধানের সংখ্যা
    })

# --- Candidate Setup ---
col1, col2 = st.columns(2)
with col1:
    c1_name = st.text_input("প্রার্থী ১:", value="ক্যান্ডিডেট ১")
    c1_mark = st.selectbox("প্রতীক ১:", ["ধানের শীষ 🌾🌾", "দাঁড়িপাল্লা ⚖️", "গরুর গাড়ি 🐂", "নৌকা ⛵", "লাঙ্গল 🚜"])
with col2:
    c2_name = st.text_input("প্রার্থী ২:", value="ক্যান্ডিডেট ২")
    c2_mark = st.selectbox("প্রতীক ২:", ["দাঁড়িপাল্লা ⚖️", "ধানের শীষ 🌾🌾", "গরুর গাড়ি 🐂", "নৌকা ⛵", "লাঙ্গল 🚜"], index=1)

st.divider()

# --- Visual Arena & Popularity ---
st.markdown(f"""
    <div class="game-container">
        <h3>📊 Live Popularity Meter</h3>
        <p><strong>{c1_name} ({c1_mark}):</strong> {st.session_state.c1_pop}% | <strong>{c2_name} ({c2_mark}):</strong> {st.session_state.c2_pop}%</p>
    </div>
    """, unsafe_allow_html=True)

# --- Interactive Game Logic ---
tab1, tab2, tab3 = st.tabs(["⚽ Football (Penalty)", "🏏 Cricket (Batting)", "🤝 Public Outreach"])

# --- TAB 1: FOOTBALL ---
with tab1:
    st.subheader("Where will you shoot?")
    
    goal_col1, goal_col2, goal_col3 = st.columns(3)
    shot = None
    with goal_col1:
        if st.button("🥅 Top Left Corner"): shot = "TL"
    with goal_col2:
        if st.button("🥅 Center"): shot = "C"
    with goal_col3:
        if st.button("🥅 Top Right Corner"): shot = "TR"
        
    if shot:
        keeper_pos = random.choice(["TL", "C", "TR", "BL", "BR"]) 
        if shot == keeper_pos:
            st.error(f"❌ Goalkeeper saved the ball! Supporters of {c2_name} are cheering!")
            st.session_state.c1_pop = max(0, st.session_state.c1_pop - 3)
        else:
            st.success(f"⚽ GOOOOOAL! {c1_name} ({c1_mark}) is on fire!")
            st.balloons()
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 8)

# --- TAB 2: CRICKET ---
with tab2:
    st.subheader("Bowler is bowling... hit with perfect timing!")
    
    timing = st.select_slider("Set your bat swing timing:", options=["Too Early", "Perfect", "Too Late"])
    
    if st.button("🏏 Swing the Bat!"):
        ball_type = random.choice(["Too Early", "Perfect", "Too Late"])
        
        if timing == ball_type:
            if timing == "Perfect":
                st.success(f"🚀 Huge Six! {c1_mark} is now the talk of the town!")
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + 12)
            else:
                st.info("🏃 Single run! Popularity increased by 1%.")
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + 1)
        else:
            st.error(f"☝️ Clean Bowled! {c1_name}'s campaign took a hit.")
            st.session_state.c1_pop = max(0, st.session_state.c1_pop - 5)

# --- TAB 3: PUBLIC OUTREACH ---
with tab3:
    st.subheader(f"🤝 {c1_name} ({c1_mark}) engaging with the public...")
    
    # জনসংযোগের ছবি - কার্টুন স্টাইল ইমেজ জেনারেশন
    # Image Generation: enabled.
    st.image(
"""
A cartoon-style image of a politician walking through a village or rural area, surrounded by many people. The people are looking at the politician, and some are reaching out or talking to him, sharing their problems. The background shows village houses, trees, and possibly some campaign banners in the distance. The politician has a friendly and attentive expression.
""",
        caption=f"{c1_name} on a public outreach program, listening to people's problems (Cartoon Style)",
        use_column_width=True
    )

    if st.session_state.current_problem is None:
        st.write("Talk to the people and listen to their problems.")
        if st.button("Meet the people"):
            problems = [
                {"text": "The roads are in very bad condition, making travel difficult in the rainy season.", "cost": 15, "pop_gain": 10},
                {"text": "There is a severe shortage of drinking water; we have to fetch water from afar.", "cost": 20, "pop_gain": 15},
                {"text": "There are no teachers in the school, disrupting education.", "cost": 10, "pop_gain": 8},
                {"text": "Hospital services are very poor.", "cost": 25, "pop_gain": 18},
                {"text": "Life is unbearable due to electricity load shedding.", "cost": 18, "pop_gain": 12}
            ]
            st.session_state.current_problem = random.choice(problems)
            st.rerun() # Refresh to show the problem

    if st.session_state.current_problem:
        problem = st.session_state.current_problem
        st.markdown(f"<div class='problem-card'><h4>A Citizen's Complaint:</h4><p>{problem['text']}</p><p>Solution Cost: {problem['cost']} Popularity Points</p></div>", unsafe_allow_html=True)
        
        col_sol1, col_sol2 = st.columns(2)
        if col_sol1.button(f"Solve Problem (+{problem['pop_gain']} Popularity)"):
            if st.session_state.c1_pop >= problem['cost']: # Cost from popularity
                st.session_state.c1_pop -= problem['cost']
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + problem['pop_gain'])
                st.session_state.problem_solved_count += 1
                st.success(f"✅ Problem solved! {c1_name}'s popularity increased.")
                st.session_state.current_problem = None # Reset for next problem
                st.rerun()
            else:
                st.error("You don't have enough popularity to solve this problem!")
        if col_sol2.button("Ignore (No action)"):
            st.session_state.c1_pop = max(0, st.session_state.c1_pop - 5) # Popularity decreases if problem ignored
            st.warning("You ignored the problem. Public dissatisfaction increased!")
            st.session_state.current_problem = None
            st.rerun()

    if st.session_state.problem_solved_count > 0:
        st.info(f"Problems solved so far: {st.session_state.problem_solved_count}")


# --- Final Win Logic ---
st.divider()
if st.session_state.c1_pop >= 95:
    st.balloons()
    st.snow()
    st.header(f"🎊 Grand Victory! {c1_name} ({c1_mark}) has been elected! 🎊")
    if st.button("Start a New Election"):
        st.session_state.c1_pop = 50
        st.session_state.c2_pop = 50
        st.session_state.current_problem = None
        st.session_state.problem_solved_count = 0
        st.rerun()

st.divider()
st.caption("© 2026 Election Simulation Game | This is for entertainment purposes only.")
