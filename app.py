import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_page_config(page_title="Election Sports Battle", layout="wide", page_icon="🗳️")

# --- Custom Styling ---
st.markdown("""
    <style>
    .stButton>button { 
        width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; 
        background-color: #006a4e; color: white;
    }
    .rally-box {
        background-color: #e8f5e9;
        border: 2px dashed #2e7d32;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 10px;
    }
    .game-container {
        border: 4px solid #006a4e;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- App Logo & Title ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image("https://img.freepik.com/free-vector/modern-check-mark-election-logo_23-2147514157.jpg", width=150)
with col_title:
    st.title("Election Sports Battle 2026")
    st.write("Campaign with your supporters and win the field!")

# --- Session State ---
if 'c1_pop' not in st.session_state:
    st.session_state.update({'c1_pop': 50, 'c2_pop': 50, 'supporters': 100})

# --- Candidate Settings ---
with st.expander("⚙️ Candidate Settings", expanded=True):
    col1, col2 = st.columns(2)
    symbols = ["Dhaner Shish 🌾🌾", "Scales ⚖️", "Bullock Cart 🐂", "Boat ⛵", "Tractor 🚜"]
    with col1:
        c1_name = st.text_input("Candidate 1 Name:", value="Candidate A")
        c1_mark = st.selectbox("Symbol 1:", symbols, index=0)
    with col2:
        c2_name = st.text_input("Candidate 2 Name:", value="Candidate B")
        c2_mark = st.selectbox("Symbol 2:", symbols, index=1)

st.divider()

# --- Popularity Meter ---
st.markdown(f"""
    <div class="game-container">
        <h3>📊 Popularity Dashboard</h3>
        <p style="font-size: 1.5em;"><strong>{c1_name} ({c1_mark}):</strong> {st.session_state.c1_pop}% | Supporters: {st.session_state.stopporters if 'stopporters' in st.session_state else 100}</p>
    </div>
    """, unsafe_allow_html=True)

# --- Game Tabs ---
tab1, tab2, tab3, tab4 = st.tabs(["⚽ Football", "🏏 Cricket", "🤝 Outreach", "📢 Campaign Rally"])

# --- TAB 1 & 2 (Football & Cricket) ---
with tab1:
    if st.button("Shoot Penalty"):
        if random.choice([True, False]):
            st.success("Goal!")
            st.session_state.c1_pop += 5
        else: st.error("Missed!")

with tab2:
    if st.button("Hit Six"):
        st.balloons()
        st.session_state.c1_pop += 10

# --- TAB 3: PUBLIC OUTREACH ---
with tab3:
    st.subheader("Leader Meeting Citizens")
    st.image("https://img.freepik.com/free-vector/politician-speaking-crowd_23-2147514164.jpg", width=600)
    if st.button("Solve Local Issue"):
        st.info("You solved a water problem! Popularity increased.")
        st.session_state.c1_pop += 8

# --- NEW TAB 4: CAMPAIGN RALLY (The "Prochar" Feature) ---
with tab4:
    st.subheader(f"📢 Mega Rally: {c1_name} with Supporters")
    
    # প্রচারণা বা মিছিলের ছবি (কার্টুন টাইপ)
    st.image("https://img.freepik.com/free-vector/politician-concept-illustration_114360-14578.jpg", 
             caption="Candidate walking with a massive crowd and banners", use_container_width=True)
    
    st.markdown("""
        <div class='rally-box'>
            <h4>The leader is walking through the streets...</h4>
            <p>Supporters are chanting slogans and carrying banners! 📢</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Campaign Procession (মিছিল শুরু করুন)"):
        with st.status("Walking through the area...", expanded=True) as status:
            st.write("Joining with local people...")
            time.sleep(1)
            st.write("Distributing leaflets...")
            time.sleep(1)
            gain = random.randint(5, 12)
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + gain)
            status.update(label=f"Campaign Successful! Gained {gain}% Popularity!", state="complete")
        st.snow()

# --- Final Win Condition ---
if st.session_state.c1_pop >= 95:
    st.balloons()
    st.header(f"🎊 {c1_name} ({c1_mark}) WON! 🎊")
    if st.button("Reset Game"):
        st.session_state.c1_pop = 50
        st.rerun()
