import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_page_config(page_title="Election Sports Battle", page_icon="🗳️", layout="wide")

# --- Custom CSS for Styling (Fixed the Error) ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { 
        width: 100%; 
        border-radius: 20px; 
        height: 3.5em; 
        background-color: #006a4e; 
        color: white; 
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #004d39;
        color: #ffd700;
    }
    .stProgress > div > div > div > div { background-color: #f42a41; }
    </style>
    """, unsafe_allow_html=True)

st.title("🗳️ Election Sports Battle 2026")
st.write("আপনার পছন্দের প্রতীক নিয়ে নির্বাচনে লড়াই করুন এবং জনপ্রিয়তা অর্জন করুন!")

# --- Step 1: Candidate Setup ---
with st.expander("⚙️ প্রার্থী এবং প্রতীক সেটআপ করুন", expanded=True):
    col1, col2 = st.columns(2)
    
    # আপনার পছন্দের প্রতীকগুলোর লিস্ট
    symbols = ["ধানের শীষ 🌾🌾", "দাঁড়িপাল্লা ⚖️", "গরুর গাড়ি 🐂", "নৌকা ⛵", "লাঙ্গল 🚜"]
    
    with col1:
        st.subheader("প্রথম পক্ষ")
        c1_name = st.text_input("প্রার্থীর নাম (১):", value="ক্যান্ডিডেট ১")
        c1_mark = st.selectbox("প্রতীক (১) পছন্দ করুন:", symbols, index=0) # ডিফল্ট ধানের শীষ
        
    with col2:
        st.subheader("দ্বিতীয় পক্ষ")
        c2_name = st.text_input("প্রার্থীর নাম (২):", value="ক্যান্ডিডেট ২")
        c2_mark = st.selectbox("প্রতীক (২) পছন্দ করুন:", symbols, index=1) # ডিফল্ট দাঁড়িপাল্লা

# --- Session State Management ---
if 'c1_pop' not in st.session_state:
    st.session_state.update({'c1_pop': 50, 'c2_pop': 50, 'toss': None})

# --- Live Dashboard ---
st.divider()
stat_col1, stat_col2 = st.columns(2)
with stat_col1:
    st.metric(label=f"📊 {c1_name} ({c1_mark})", value=f"{st.session_state.c1_pop}%")
    st.progress(st.session_state.c1_pop / 100)
with stat_col2:
    st.metric(label=f"📊 {c2_name} ({c2_mark})", value=f"{st.session_state.c2_pop}%")
    st.progress(st.session_state.c2_pop / 100)

# --- Action Zone ---
st.divider()
st.subheader("🎮 নির্বাচনী প্রচারণার লড়াই (খেলাধুলা)")
action_col1, action_col2, action_col3 = st.columns(3)

# 1. TOSS
if action_col1.button("🎲 টস করুন"):
    winner = random.choice([c1_name, c2_name])
    st.session_state.toss = winner
    st.info(f"🪙 টস জিতেছেন: **{winner}**")

# 2. FOOTBALL
if action_col2.button("⚽ ফুটবল ম্যাচ খেলুন"):
    with st.spinner('মাঠে টানটান উত্তেজনা...'):
        time.sleep(1.5)
        s1, s2 = random.randint(0, 5), random.randint(0, 5)
        st.subheader(f"ফলাফল: {c1_name} {s1} - {s2} {c2_name}")
        
        if s1 != s2:
            win_name = c1_name if s1 > s2 else c2_name
            bonus = random.randint(10, 15)
            if s1 > s2:
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + bonus)
                st.session_state.c2_pop = max(0, st.session_state.c2_pop - 5)
            else:
                st.session_state.c2_pop = min(100, st.session_state.c2_pop + bonus)
                st.session_state.c1_pop = max(0, st.session_state.c1_pop - 5)
            st.success(f"🏆 {win_name} গোল বন্যায় প্রতিপক্ষকে ভাসিয়ে দিলেন!")
        else:
            st.warning("ম্যাচ ড্র! কেউ পপুলারিটি পেল না।")

# 3. CRICKET
if action_col3.button("🏏 ক্রিকেট ম্যাচ খেলুন"):
    with st.spinner('ব্যাট-বলের ধুমধাড়াক্কা লড়াই...'):
        time.sleep(1.5)
        r1, r2 = random.randint(120, 250), random.randint(120, 250)
        st.subheader(f"স্কোর: {c1_name} ({r1} রান) - {c2_name} ({r2} রান)")
        
        win_name = c1_name if r1 > r2 else c2_name
        bonus = random.randint(15, 20)
        if r1 > r2:
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + bonus)
            st.session_state.c2_pop = max(0, st.session_state.c2_pop - 7)
        else:
            st.session_state.c2_pop = min(100, st.session_state.c2_pop + bonus)
            st.session_state.c1_pop = max(0, st.session_state.c1_pop - 7)
        st.success(f"🏆 {win_name} এর বাউন্ডারিতে পপুলারিটি তুঙ্গে!")

# --- Final Election Result ---
if st.session_state.c1_pop >= 95 or st.session_state.c2_pop >= 95:
    final_winner = c1_name if st.session_state.c1_pop >= 95 else c2_name
    final_mark = c1_mark if st.session_state.c1_pop >= 95 else c2_mark
    st.balloons()
    st.header(f"🎊 বিজয় উল্লাস! {final_winner} ({final_mark}) নির্বাচনে বিপুল ভোটে জয়ী! 🎊")
    if st.button("🔄 নতুন করে ভোট শুরু করুন (Reset)"):
        st.session_state.c1_pop = 50
        st.session_state.c2_pop = 50
        st.rerun()

st.divider()
st.caption("© 2026 Election Simulation Game | এটি একটি বিনোদনমূলক গেম মাত্র।")
