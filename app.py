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
        <h3>📊 লাইভ পপুলারিটি মিটার</h3>
        <p><strong>{c1_name} ({c1_mark}):</strong> {st.session_state.c1_pop}% | <strong>{c2_name} ({c2_mark}):</strong> {st.session_state.c2_pop}%</p>
    </div>
    """, unsafe_allow_html=True)

# --- Interactive Game Logic ---
tab1, tab2, tab3 = st.tabs(["⚽ ফুটবল (পেনাল্টি)", "🏏 ক্রিকেট (ব্যাটিং)", "🤝 জনসংযোগ"])

# --- TAB 1: FOOTBALL ---
with tab1:
    st.subheader("গোলপোস্টের কোথায় শট মারবেন?")
    
    goal_col1, goal_col2, goal_col3 = st.columns(3)
    shot = None
    with goal_col1:
        if st.button("🥅 উপরের বাম কোণা"): shot = "TL"
    with goal_col2:
        if st.button("🥅 মাঝখানে"): shot = "C"
    with goal_col3:
        if st.button("🥅 উপরের ডান কোণা"): shot = "TR"
        
    if shot:
        keeper_pos = random.choice(["TL", "C", "TR", "BL", "BR"]) 
        if shot == keeper_pos:
            st.error(f"❌ গোলকিপার বল ঠেকিয়ে দিয়েছে! {c2_name} এর সমর্থকরা স্লোগান দিচ্ছে!")
            st.session_state.c1_pop = max(0, st.session_state.c1_pop - 3)
        else:
            st.success(f"⚽ গোললললল! {c1_name} এর {c1_mark} প্রতীকের জয়জয়কার!")
            st.balloons()
            st.session_state.c1_pop = min(100, st.session_state.c1_pop + 8)

# --- TAB 2: CRICKET ---
with tab2:
    st.subheader("বোলার বল করছে... সঠিক টাইমিংয়ে মারুন!")
    
    timing = st.select_slider("আপনার ব্যাটের সুইং টাইমিং ঠিক করুন:", options=["খুব আগে", "পারফেক্ট", "দেরি করে"])
    
    if st.button("🏏 ব্যাট ঘুরান!"):
        ball_type = random.choice(["খুব আগে", "পারফেক্ট", "দেরি করে"])
        
        if timing == ball_type:
            if timing == "পারফেক্ট":
                st.success(f"🚀 বিশাল ছক্কা! {c1_mark} এখন সবার মুখে মুখে!")
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + 12)
            else:
                st.info("🏃 সিঙ্গেল রান! পপুলারিটি ১% বাড়লো।")
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + 1)
        else:
            st.error(f"☝️ ক্লিন বোল্ড! {c1_name} এর প্রচারণা ধাক্কা খেল।")
            st.session_state.c1_pop = max(0, st.session_state.c1_pop - 5)

# --- TAB 3: JONOSHONJOG ---
with tab3:
    st.subheader(f"🤝 {c1_name} ({c1_mark}) জনগনের সাথে...")
    
    # জনসংযোগের ছবি
    st.image("https://i.ibb.co/L66X2jP/jonoshongjog.jpg", caption=f"{c1_name} এলাকার মানুষের সাথে জনসংযোগে", use_column_width=True) 
    # এই ইমেজ লিঙ্কটি একটি placeholder, আপনি আপনার পছন্দের ছবি ব্যবহার করতে পারেন।

    if st.session_state.current_problem is None:
        st.write("এলাকার মানুষের সাথে কথা বলুন এবং তাদের সমস্যা শুনুন।")
        if st.button("মানুষের সাথে দেখা করুন"):
            problems = [
                {"text": "রাস্তাঘাটের অবস্থা খুব খারাপ, বর্ষায় চলাফেরা করা যায় না।", "cost": 15, "pop_gain": 10},
                {"text": "খাবার পানির খুব অভাব, দূর থেকে পানি আনতে হয়।", "cost": 20, "pop_gain": 15},
                {"text": "স্কুলে শিক্ষক নেই, পড়াশোনা ব্যাহত হচ্ছে।", "cost": 10, "pop_gain": 8},
                {"text": "হাসপাতালের পরিষেবা একদম নিম্নমানের।", "cost": 25, "pop_gain": 18},
                {"text": "বিদ্যুতের লোডশেডিংয়ে জীবন দুর্বিষহ।", "cost": 18, "pop_gain": 12}
            ]
            st.session_state.current_problem = random.choice(problems)
            st.rerun() # সমস্যা দেখানোর জন্য রিফ্রেশ

    if st.session_state.current_problem:
        problem = st.session_state.current_problem
        st.markdown(f"<div class='problem-card'><h4>একজন নাগরিকের অভিযোগ:</h4><p>{problem['text']}</p><p>সমাধানের খরচ: {problem['cost']} পপুলারিটি পয়েন্ট</p></div>", unsafe_allow_html=True)
        
        col_sol1, col_sol2 = st.columns(2)
        if col_sol1.button(f"সমাধান করুন (+{problem['pop_gain']} পপুলারিটি)"):
            if st.session_state.c1_pop >= problem['cost']: # পপুলারিটি থেকে খরচ
                st.session_state.c1_pop -= problem['cost']
                st.session_state.c1_pop = min(100, st.session_state.c1_pop + problem['pop_gain'])
                st.session_state.problem_solved_count += 1
                st.success(f"✅ সমস্যা সমাধান হয়েছে! {c1_name} এর জনপ্রিয়তা বৃদ্ধি পেল।")
                st.session_state.current_problem = None # সমস্যা সমাধান হলে নতুন সমস্যার জন্য অপেক্ষা
                st.rerun()
            else:
                st.error("আপনার পর্যাপ্ত পপুলারিটি নেই এই সমস্যাটি সমাধানের জন্য!")
        if col_sol2.button("বাদ দিন (No action)"):
            st.session_state.c1_pop = max(0, st.session_state.c1_pop - 5) # সমস্যা উপেক্ষা করলে পপুলারিটি কমবে
            st.warning("আপনি সমস্যাটি উপেক্ষা করলেন। জনগণের অসন্তোষ বাড়লো!")
            st.session_state.current_problem = None
            st.rerun()

    if st.session_state.problem_solved_count > 0:
        st.info(f"এ পর্যন্ত {st.session_state.problem_solved_count}টি সমস্যা সমাধান করেছেন!")


# --- Final Win Logic ---
st.divider()
if st.session_state.c1_pop >= 95:
    st.balloons()
    st.snow()
    st.header(f"🎊 রাজকীয় জয়! {c1_name} ({c1_mark}) নির্বাচিত হয়েছেন! 🎊")
    if st.button("নতুন ইলেকশন শুরু করুন"):
        st.session_state.c1_pop = 50
        st.session_state.c2_pop = 50
        st.session_state.current_problem = None
        st.session_state.problem_solved_count = 0
        st.rerun()

st.divider()
st.caption("© 2026 Election Simulation Game | এটি একটি বিনোদনমূলক গেম মাত্র।")
