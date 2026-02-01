import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_page_config(page_title="Election Sports Battle", page_icon="🗳️", layout="wide")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #006a4e; color: white; font-weight: bold; }
    .stProgress > div > div > div > div { background-color: #f42a41; }
    </style>
    """, unsafe_allow_stdio=True)

st.title("🗳️ Election Sports Battle 2026")
st.write("আপনার পছন্দের প্রতীক নিয়ে নির্বাচনে লড়াই করুন!")

# --- Step 1: Candidate Setup with Your Symbols ---
with st.expander("⚙️ প্রার্থী এবং প্রতীক সেটআপ করুন", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        c1_name = st.text_input("প্রার্থীর নাম (১):", value="ক্যান্ডিডেট ১")
        # আপনার দেওয়া প্রতীক: ধানের শীষ
        c1_mark = st.selectbox("প্রতীক (১) পছন্দ করুন:", ["ধানের শীষ 🌾🌾", "দাঁড়িপাল্লা ⚖️", "গরুর গাড়ি 🐂"])
    with col2:
        c2_name = st.text_input("প্রার্থীর নাম (২):", value="ক্যান্ডিডেট ২")
        # ডিফল্ট হিসেবে অন্য একটি প্রতীক
        c2_mark = st.selectbox("প্রতীক (২) পছন্দ করুন:", ["দাঁড়িপাল্লা ⚖️", "ধানের শীষ 🌾🌾", "গরুর গাড়ি 🐂"], index=1)

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
action_col1, action_col2, action_col3 = st.columns(3)

# 1. TOSS
if action_col1.button("🎲 টস করুন"):
    winner = random.choice([c1_name, c2_name])
    st.session_state.toss = winner
    st.info(f"🪙 টস জিতেছেন: **{winner}**")

# 2. FOOTBALL
if action_col2.button("⚽ ফুটবল ম্যাচ"):
    with st.spinner('মাঠে বল গড়াচ্ছে...'):
        time.sleep(1)
        s1, s2 = random.randint(0, 5), random.randint(0, 5)
        st.subheader(f"ফলাফল: {c1_name} {s1} - {s2} {c2_name}")
        if s1 != s2:
            win_name = c1_name if s1 > s2 else c2_name
            bonus = random.randint(10, 15)
            if s1 > s2:
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + bonus)
            else:
                st.session_state.c2_pop = min(100, st.session_state.c2_pop + bonus)
            st.success(f"🏆 {win_name} গোল বন্যায় ভাসিয়ে দিলেন!")
        else:
            st.warning("কেউ গোল করতে পারলো না—ড্র!")

# 3. CRICKET
if action_col3.button("🏏 ক্রিকেট ম্যাচ"):
    with st.spinner('ব্যাট-বলের লড়াই চলছে...'):
        time.sleep(1)
        r1, r2 = random.randint(100, 250), random.randint(100, 250)
        st.subheader(f"স্কোর: {c1_name} ({r1}) - {c2_name} ({r2})")
        win_name = c1_name if r1 > r2 else c2_name
        bonus = random.randint(12, 20)
        if r1 > r2:
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + bonus)
        else:
            st.session_state.c2_pop = min(100, st.session_state.c2_pop + bonus)
        st.success(f"🏆 {win_name} এর ছক্কায় পপুলারিটি আকাশচুম্বী!")

# --- Final Election Result ---
if st.session_state.c1_pop >= 95 or st.session_state.c2_pop >= 95:
    final_winner = c1_name if st.session_state.c1_pop >= 95 else c2_name
    final_mark = c1_mark if st.session_state.c1_pop >= 95 else c2_mark
    st.balloons()
    st.header(f"🎉 বিজয় উল্লাস! {final_winner} ({final_mark}) বিপুল ভোটে জয়ী! 🎉")
    if st.button("🔄 নতুন করে ভোট শুরু করুন"):
        st.session_state.c1_pop = 50
        st.session_state.c2_pop = 50
        st.rerun()

st.divider()
st.caption("এটি একটি বিনোদনমূলক গেম। প্রতীকের সাথে বাস্তব রাজনীতির কোনো সম্পর্ক নেই।")
