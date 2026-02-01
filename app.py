import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_page_config(page_title="BD Election Battle 2026", layout="wide", page_icon="🇧🇩")

# --- Custom Styling (BD Flag Theme & Mobile Game UI) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #006a4e; /* Deep Green */
        color: white;
    }
    /* Mobile Style Scoreboard */
    .scoreboard {
        background: linear-gradient(145deg, #f42a41, #8b1a26); /* Red Gradient */
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        border: 4px solid #ffffff;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.4);
        margin-bottom: 25px;
    }
    /* Game Controller Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 4.5em;
        font-weight: bold;
        font-size: 18px;
        background-color: #ffffff;
        color: #006a4e;
        border: 3px solid #ffd700;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ffd700;
        color: #006a4e;
        transform: scale(1.05);
    }
    /* Slogan Animation Styling */
    .slogan-text {
        font-size: 30px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 2px 2px #f42a41;
        text-align: center;
        padding: 10px;
        border-radius: 10px;
        background: rgba(0,0,0,0.2);
        margin: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session State ---
if 'c1_pop' not in st.session_state:
    st.session_state.update({'c1_pop': 50, 'c2_pop': 50, 'game_log': "Ready for the Election Battle!"})

# --- Sidebar Setup ---
with st.sidebar:
    st.image("https://img.freepik.com/free-vector/modern-check-mark-election-logo_23-2147514157.jpg", width=100)
    st.header("🎮 Game Settings")
    c1_name = st.text_input("Candidate Name:", value="Candidate A")
    c1_mark = st.selectbox("Your Symbol:", ["Dhaner Shish 🌾🌾", "Scales ⚖️", "Bullock Cart 🐂", "Boat ⛵"])
    st.divider()
    if st.button("🔄 Reset Tournament"):
        st.session_state.c1_pop = 50
        st.rerun()

# --- Main UI ---
st.title("🇧🇩 Election Sports Battle 2026")

# --- Scoreboard ---
st.markdown(f"""
    <div class="scoreboard">
        <h2 style='color: white; margin:0;'>LIVE POPULARITY METER</h2>
        <div style='display: flex; justify-content: space-around; margin-top:15px;'>
            <div><p style='margin:0;'>{c1_name}</p><h1 style='color: #ffd700; font-size: 50px;'>{st.session_state.c1_pop}%</h1></div>
            <div style='border-left: 3px solid white;'></div>
            <div><p style='margin:0;'>Opponent</p><h1 style='color: #ffffff; font-size: 50px;'>{st.session_state.c2_pop}%</h1></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Navigation Tabs ---
tab1, tab2, tab3 = st.tabs(["⚽ Football Game", "🏏 Cricket Game", "📢 Mega Campaign"])

# --- TAB 1: FOOTBALL ---
with tab1:
    st.subheader("🥅 Penalty Shootout (Controller)")
    st.info(f"Log: {st.session_state.game_log}")
    
    colA, colB, colC = st.columns(3)
    shot = None
    with colA:
        if st.button("↖️ SHOOT LEFT"): shot = "L"
    with colB:
        if st.button("⬆️ SHOOT CENTER"): shot = "C"
    with colC:
        if st.button("↗️ SHOOT RIGHT"): shot = "R"
    
    if shot:
        keeper = random.choice(["L", "C", "R"])
        if shot != keeper:
            st.session_state.game_log = "⚽ GOAL! The crowd is cheering for you!"
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 7)
            st.balloons()
        else:
            st.session_state.game_log = "❌ SAVED! Better luck next time."
            st.session_state.c1_pop = max(0, st.session_state.c1_pop - 4)
        st.rerun()

# --- TAB 2: CRICKET ---
with tab2:
    st.subheader("🏏 Cricket Batting (Controller)")
    st.info(f"Commentary: {st.session_state.game_log}")
    
    col_l, col_r = st.columns(2)
    hit = None
    with col_l:
        if st.button("🏏 DEFENSIVE PUSH"): hit = "D"
    with col_r:
        if st.button("🚀 POWER HIT (SIX)"): hit = "A"
        
    if hit:
        if hit == "A":
            if random.random() > 0.4:
                st.session_state.game_log = "🚀 OUT OF THE PARK! MASSIVE SIX!"
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + 12)
                st.snow()
            else:
                st.session_state.game_log = "☝️ CAUGHT! The fielder made no mistake."
                st.session_state.c1_pop = max(0, st.session_state.c1_pop - 8)
        else:
            st.session_state.game_log = "🏃 Smart rotation of strike. 2 Runs!"
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 2)
        st.rerun()

# --- TAB 3: MEGA CAMPAIGN & SLOGANS ---
with tab3:
    st.subheader("📢 Mass Campaigning with Supporters")
    st.image("https://img.freepik.com/free-vector/politician-concept-illustration_114360-14578.jpg", use_container_width=True)
    
    if st.button("🔊 START RALLY & CHANT (মিছিল ও স্লোগান শুরু করুন)"):
        slogans = [
            "🇧🇩 BANGLADESH ZINDABAD!", 
            f"📢 {c1_mark} ER JOY HOBEI!",
            "📢 DESHER NETRE, {c1_name}!" ,
            "🇧🇩 BANGLADESH ZINDABAD!"
        ]
        
        with st.status("Procession Moving Through the Area...", expanded=True) as status:
            for s in slogans:
                time.sleep(1.2)
                st.markdown(f"<div class='slogan-text'>{s}</div>", unsafe_allow_html=True)
            
            gain = random.randint(10, 20)
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + gain)
            status.update(label=f"Mega Rally Success! Gained {gain}% Popularity!", state="complete")
        st.rerun()

# --- Victory Condition ---
if st.session_state.c1_pop >= 95:
    st.balloons()
    st.markdown(f"<h1 style='text-align: center; color: #ffd700; background-color: #f42a41; padding: 20px; border-radius: 20px;'>🎉 {c1_name} ({c1_mark}) HAS WON THE ELECTION! 🎉</h1>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Developed with Pride in Bangladesh | 2026")
