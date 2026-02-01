import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_page_config(page_title="Election Sports Pro", page_icon="🗳️", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .goal-text { color: green; font-size: 25px; font-weight: bold; text-align: center; }
    .miss-text { color: red; font-size: 25px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🗳️ Election Sports Battle: Play to Win!")

# --- Setup ---
if 'c1_pop' not in st.session_state:
    st.session_state.update({'c1_pop': 50, 'c2_pop': 50, 'score1': 0, 'score2': 0, 'balls': 5})

col1, col2 = st.columns(2)
with col1:
    c1_name = st.text_input("প্রার্থী ১:", value="ক্যান্ডিডেট ১")
    c1_mark = st.selectbox("প্রতীক ১:", ["ধানের শীষ 🌾🌾", "দাঁড়িপাল্লা ⚖️", "গরুর গাড়ি 🐂"])
with col2:
    c2_name = st.text_input("প্রার্থী ২:", value="ক্যান্ডিডেট ২")
    c2_mark = st.selectbox("প্রতীক ২:", ["দাঁড়িপাল্লা ⚖️", "ধানের শীষ 🌾🌾", "গরুর গাড়ি 🐂"], index=1)

st.divider()
st.subheader(f"📊 পপুলারিটি: {c1_name}: {st.session_state.c1_pop}% | {c2_name}: {st.session_state.c2_pop}%")

# --- Game Choice ---
game_mode = st.radio("কোন খেলাটি খেলবেন?", ["ফুটবল (পেনাল্টি)", "ক্রিকেট (ব্যাটিং)"])

# --- FOOTBALL INTERACTIVE ---
if game_mode == "ফুটবল (পেনাল্টি)":
    st.info("গোলকিপারের উল্টো দিকে শট নিন! ৩টি শটের মধ্যে বেশি গোল করলে পপুলারিটি বাড়বে।")
    
    col_play1, col_play2, col_play3 = st.columns(3)
    
    side = None
    if col_play1.button("বাম দিকে শট (Left)"): side = "Left"
    if col_play2.button("মাঝখানে শট (Center)"): side = "Center"
    if col_play3.button("ডান দিকে শট (Right)"): side = "Right"

    if side:
        keeper_side = random.choice(["Left", "Center", "Right"])
        if side == keeper_side:
            st.markdown("<p class='miss-text'>❌ গোলকিপার বল ধরে ফেলেছে! মিস!</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='goal-text'>⚽ গোললললল! দুর্দান্ত শট!</p>", unsafe_allow_html=True)
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 5)
            st.session_state.c2_pop = max(0, st.session_state.c2_pop - 3)

# --- CRICKET INTERACTIVE ---
elif game_mode == "ক্রিকেট (ব্যাটিং)":
    st.info("সঠিক টাইমিংয়ে হিট করুন! নিচে একটি নম্বর গেস করুন, মিললে ছক্কা!")
    
    user_guess = st.slider("আপনার হিটিং পাওয়ার সেট করুন (১-৫):", 1, 5)
    
    if st.button("🏏 বল খেলুন!"):
        ball_luck = random.randint(1, 5)
        if user_guess == ball_luck:
            st.balloons()
            st.success("🏏 বিশাল ছক্কা! ১০% পপুলারিটি বাড়লো!")
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 10)
        elif abs(user_guess - ball_luck) <= 1:
            st.info("🏃 এক রান নিলেন।")
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 1)
        else:
            st.error("☝️ আউট! পপুলারিটি কমে গেল।")
            st.session_state.c1_pop = max(0, st.session_state.c1_pop - 5)

# --- Final Win ---
if st.session_state.c1_pop >= 90:
    st.balloons()
    st.header(f"🎊 {c1_name} ({c1_mark}) জয়ী! 🎊")
    if st.button("Reset"):
        st.session_state.c1_pop = 50
        st.rerun()

st.divider()
st.caption("আপনার প্রতিটি মুভ আপনার পপুলারিটি ঠিক করবে। সাবধানে খেলুন!")
