import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_config(page_title="BD Election Battle 2026", layout="wide", page_icon="🇧🇩")

# --- Custom Styling (BD Flag & Game Theme) ---
st.markdown("""
    <style>
    .stApp { background-color: #006a4e; color: white; }
    .scoreboard {
        background: linear-gradient(145deg, #f42a41, #8b1a26);
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        border: 4px solid #ffd700;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.4);
    }
    .stButton>button {
        width: 100%; border-radius: 50px; height: 4em; font-weight: bold;
        background-color: #ffffff; color: #006a4e; border: 3px solid #ffd700;
    }
    .stButton>button:hover { background-color: #ffd700; color: #006a4e; }
    .slogan-text { font-size: 25px; font-weight: bold; color: #ffffff; text-shadow: 2px 2px #f42a41; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- Session State Management ---
if 'c1_pop' not in st.session_state:
    st.session_state.update({
        'c1_pop': 50, 
        'wickets': 0, 
        'total_runs': 0, 
        'game_over': False,
        'log': "Election Field is Ready!"
    })

# --- Sidebar ---
with st.sidebar:
    st.header("🎮 Candidate Setup")
    c1_name = st.text_input("Candidate Name:", value="Leader A")
    c1_mark = st.selectbox("Symbol:", ["Dhaner Shish 🌾🌾", "Scales ⚖️", "Bullock Cart 🐂", "Boat ⛵"])
    if st.button("🔄 Restart Tournament"):
        st.session_state.update({'c1_pop': 50, 'wickets': 0, 'total_runs': 0, 'game_over': False})
        st.rerun()

# --- Live Scoreboard ---
st.markdown(f"""
    <div class="scoreboard">
        <h2 style='color: white; margin:0;'>🏏 CRICKET SCOREBOARD & POPULARITY</h2>
        <div style='display: flex; justify-content: space-around; margin-top:15px;'>
            <div><p>Popularity</p><h1 style='color: #ffd700;'>{st.session_state.c1_pop}%</h1></div>
            <div style='border-left: 2px solid white;'></div>
            <div><p>Runs Scored</p><h1 style='color: #ffffff;'>{st.session_state.total_runs}</h1></div>
            <div style='border-left: 2px solid white;'></div>
            <div><p>Wickets Lost</p><h1 style='color: #ffd700;'>{st.session_state.wickets}/3</h1></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

if st.session_state.game_over:
    st.error(f"❌ GAME OVER! {c1_name} lost 3 wickets. Popularity took a hit!")
    if st.button("Try Again"):
        st.session_state.update({'c1_pop': max(10, st.session_state.c1_pop - 20), 'wickets': 0, 'total_runs': 0, 'game_over': False})
        st.rerun()
else:
    # --- Game Tabs ---
    tab1, tab2, tab3 = st.tabs(["🏏 Cricket Battle", "⚽ Football Battle", "📢 Mega Campaign"])

    with tab1:
        st.subheader("🏏 Cricket: Batting (3 Wickets Limit)")
        st.info(f"Commentary: {st.session_state.log}")
        col_l, col_r = st.columns(2)
        
        if col_l.button("🏏 DEFENSIVE PUSH"):
            runs = random.choice([1, 2, 0])
            st.session_state.total_runs += runs
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + runs)
            st.session_state.log = f"Good shot! Took {runs} run(s)."
            st.rerun()

        if col_r.button("🚀 POWER HIT (SIX)"):
            if random.random() > 0.5:
                st.session_state.total_runs += 6
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + 10)
                st.session_state.log = "🚀 OUT OF THE PARK! MASSIVE SIX!"
                st.snow()
            else:
                st.session_state.wickets += 1
                st.session_state.log = "☝️ OUT! Fielder caught it!"
                if st.session_state.wickets >= 3:
                    st.session_state.game_over = True
            st.rerun()

    with tab2:
        st.subheader("⚽ Football: Penalty")
        st.write("Score goals to increase popularity!")
        if st.button("↖️ SHOOT LEFT") or st.button("⬆️ CENTER") or st.button("↗️ RIGHT"):
            if random.choice([True, False]):
                st.success("⚽ GOAL!")
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + 5)
            else:
                st.error("❌ SAVED!")
                st.session_state.c1_pop = max(0, st.session_state.c1_pop - 2)

    with tab3:
        st.subheader("📢 Campaign Rally")
        if st.button("🔊 START PROCESSION"):
            slogans = ["🇧🇩 BANGLADESH ZINDABAD!", f"📢 {c1_mark} ER JOY HOBEI!"]
            with st.status("Chanting Slogans...", expanded=True) as status:
                for s in slogans:
                    time.sleep(1)
                    st.markdown(f"<div class='slogan-text'>{s}</div>", unsafe_allow_html=True)
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + 15)
                status.update(label="Campaign Success!", state="complete")

# --- Victory Condition ---
if st.session_state.c1_pop >= 95:
    st.balloons()
    st.markdown(f"<h1 style='text-align: center; color: #ffd700; background-color: #f42a41; padding: 20px; border-radius: 20px;'>🎉 {c1_name} ({c1_mark}) IS THE WINNER! 🎉</h1>", unsafe_allow_html=True)

st.caption("Developed with Pride in Bangladesh | 2026")
