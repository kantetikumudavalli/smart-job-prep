import streamlit as st
import random
st.set_page_config(page_title="Smart Job Prep AI", page_icon="🎯", layout="wide")
st.title("🎯 Smart Job Prep AI")
st.write("Your College Career Guidance Partner - From 1st Year to Placement")

SKILLS_DB = {
    "ML Engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch", "numpy", "pandas", "sql", "statistics", "nlp"],
    "Data Scientist": ["python", "pandas", "numpy", "sql", "statistics", "machine learning", "data visualization", "excel", "power bi", "matplotlib"],
    "Web Developer": ["html", "css", "javascript", "react", "python", "sql", "git", "node", "api", "mongodb"],
    "Java Developer": ["java", "spring boot", "sql", "oops", "dsa", "git", "hibernate", "rest api", "maven", "html"],
    "Data Analyst": ["excel", "sql", "python", "power bi", "tableau", "statistics", "pandas", "data visualization"]
}

APTITUDE_POOL = ["Time & Work", "Percentages", "Profit & Loss", "Ratio & Proportion", "Number Series", "Blood Relations", "Direction Sense", "Coding-Decoding", "Averages", "Simple & Compound Interest", "Trains & Speed", "Probability", "Permutation & Combination", "Puzzles", "Age Problems", "Mixtures", "Clocks & Calendar", "Seating Arrangement", "Syllogism", "Data Interpretation"]
CODING_POOL = ["Variables & Data Types", "Loops", "Arrays", "Strings", "Functions", "Recursion", "OOPS Concepts", "Stack & Queue", "Sorting", "Searching", "Linked List", "Trees", "Graphs", "Dynamic Programming", "Hashing", "Two Pointers", "Sliding Window", "Greedy", "Backtracking", "Bit Manipulation"]

NOTES_DB = {
    "Time & Work": "Formula: Work = Time x Efficiency. If A does work in 10 days, 1 day work = 1/10. Together work = 1/A + 1/B.",
    "Percentages": "Formula: Percentage = (Value / Total) x 100. Increase % = (New-Old)/Old x 100.",
    "Profit & Loss": "Profit = SP - CP. Profit % = Profit/CP x 100. Loss = CP - SP.",
    "Arrays": "Array stores same type data in continuous memory. Index starts from 0. Access time O(1).",
    "Loops": "For loop = fixed times. While loop = till condition false. Break stops loop, Continue skips one step.",
    "Strings": "String is sequence of characters. Immutable in Python/Java. Use len(), slicing, split().",
    "OOPS Concepts": "4 Pillars: Encapsulation, Inheritance, Polymorphism, Abstraction. Class = Blueprint, Object = Real thing.",
    "Sorting": "Bubble Sort O(n^2), Merge Sort O(n log n), Quick Sort O(n log n) avg. For interviews learn Merge & Quick.",
    "Recursion": "Function calling itself. Must have Base Condition else infinite loop. Ex: Factorial, Fibonacci.",
    "SQL": "SELECT, WHERE, GROUP BY, ORDER BY, JOIN. JOIN types: INNER, LEFT, RIGHT, FULL."
}

QUIZ_DB = [
    {"q": "What is 15% of 200?", "options": ["20", "30", "25", "35"], "ans": "30"},
    {"q": "If A does work in 10 days, B in 15 days, together in how many days?", "options": ["5 days", "6 days", "7 days", "8 days"], "ans": "6 days"},
    {"q": "What is the output of len('Python')?", "options": ["5", "6", "7", "4"], "ans": "6"},
    {"q": "Which is OOPS concept?", "options": ["Encapsulation", "Loop", "Array", "SQL"], "ans": "Encapsulation"},
    {"q": "What is SQL full form?", "options": ["Structured Query Language", "Simple Query Language", "System Query Language", "None"], "ans": "Structured Query Language"},
    {"q": "Time Complexity of Binary Search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "ans": "O(log n)"},
    {"q": "What is 20 + 30 * 2 ?", "options": ["100", "80", "70", "90"], "ans": "80"},
    {"q": "Which data structure is LIFO?", "options": ["Queue", "Stack", "Array", "Tree"], "ans": "Stack"},
    {"q": "Profit if CP=100, SP=120?", "options": ["10%", "20%", "15%", "25%"], "ans": "20%"},
    {"q": "Which keyword is used for inheritance in Python?", "options": ["extends", "inherits", "class Child(Parent)", "super"], "ans": "class Child(Parent)"},
]

MOCK_TEST_DB = [
    {"q": "A train 200m long crosses a pole in 10 sec. Speed?", "options": ["20 m/s", "72 km/hr", "Both A & B", "None"], "ans": "Both A & B"},
    {"q": "If 5 workers do work in 10 days, 10 workers in?", "options": ["5 days", "20 days", "10 days", "2 days"], "ans": "5 days"},
    {"q": "What is 25% of 640?", "options": ["120", "160", "140", "180"], "ans": "160"},
    {"q": "Which is not a Python data type?", "options": ["List", "Tuple", "ArrayList", "Dict"], "ans": "ArrayList"},
    {"q": "What is the output of 2**3 in Python?", "options": ["6", "8", "9", "5"], "ans": "8"},
    {"q": "Which SQL command is used to fetch data?", "options": ["GET", "SELECT", "FETCH", "SHOW"], "ans": "SELECT"},
    {"q": "Next number: 2, 4, 8, 16, ?", "options": ["20", "24", "32", "30"], "ans": "32"},
    {"q": "If CP=500, Profit=20%, SP=?", "options": ["550", "600", "650", "500"], "ans": "600"},
    {"q": "Which data structure uses FIFO?", "options": ["Stack", "Queue", "Tree", "Graph"], "ans": "Queue"},
    {"q": "What is the full form of API?", "options": ["Application Programming Interface", "Advanced Programming Interface", "Application Process Interface", "None"], "ans": "Application Programming Interface"},
]

def get_plan():
    plan = {}
    for d in range(1, 91):
        a1 = APTITUDE_POOL[((d - 1) * 2) % len(APTITUDE_POOL)]
        a2 = APTITUDE_POOL[((d - 1) * 2 + 1) % len(APTITUDE_POOL)]
        c1 = CODING_POOL[((d - 1) * 2) % len(CODING_POOL)]
        c2 = CODING_POOL[((d - 1) * 2 + 1) % len(CODING_POOL)]
        if d > 60:
            level = " - Advanced"
        elif d > 30:
            level = " - Intermediate"
        else:
            level = " - Basics"
        plan[d] = {"Aptitude": [a1 + level, a2 + level], "Coding": [c1 + level, c2 + level]}
    return plan

def show_scanner(prefix):
    st.subheader("🔍 Resume Scanner - Hiring Readiness Check")
    role = st.selectbox("Select Target Role:", list(SKILLS_DB.keys()), key=f"role_{prefix}")
    user_input = st.text_area("Paste Your Skills (comma separated):", placeholder="Ex: Python, SQL, Pandas, Excel...", key=f"skills_{prefix}")
    name = st.text_input("Your Name:", key=f"name_{prefix}")
    if st.button("🔍 Check My Readiness", key=f"check_{prefix}"):
        if not user_input.strip():
            st.warning("Please enter your skills first!")
        else:
            user_skills = [s.strip().lower() for s in user_input.split(",")]
            required = SKILLS_DB[role]
            matched = [s for s in required if s in user_skills or any(s in u for u in user_skills)]
            missing = [s for s in required if s not in matched]
            score = int((len(matched) / len(required)) * 100)
            st.metric(label=f"{name} - Readiness for {role}", value=f"{score}%")
            st.progress(score / 100)
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"✅ You Have ({len(matched)}):")
                for m in matched:
                    st.write(f"- {m.title()}")
            with col2:
                st.error(f"❌ Missing Skills ({len(missing)}):")
                for m in missing:
                    st.write(f"- {m.title()}")
            if score >= 80:
                st.balloons()
                st.success("🎉 Excellent! You are almost placement ready!")
            elif score >= 50:
                st.warning("👍 Good progress! Focus on missing skills.")
            else:
                st.error("📚 Need to work hard!")

def show_roadmap(day_key, title):
    plan = get_plan()
    st.header(title)
    st.success("Complete 4 topics daily. Finish all 4 to unlock the next day!")
    if day_key not in st.session_state:
        st.session_state[day_key] = 1
    day = st.session_state[day_key]
    month = (day - 1) // 30 + 1
    if day > 90:
        st.balloons()
        st.success("🎉 Congratulations! 3 Months Complete!")
        if st.button("🔄 Start Again from Day 1", key=f"restart_{day_key}"):
            st.session_state[day_key] = 1
            st.rerun()
    else:
        st.header(f"📅 Month {month} - Day {day} - Today Target")
        st.write(f"Month {month} / 3 | Day {day} / 90")
        today = plan[day]
        st.subheader("🧠 Aptitude - 2 Topics")
        a1 = st.checkbox(f"Aptitude: {today['Aptitude'][0]}", key=f"a1_{day_key}_{day}")
        a2 = st.checkbox(f"Aptitude: {today['Aptitude'][1]}", key=f"a2_{day_key}_{day}")
        st.subheader("💻 Coding - 2 Topics")
        c1 = st.checkbox(f"Coding: {today['Coding'][0]}", key=f"c1_{day_key}_{day}")
        c2 = st.checkbox(f"Coding: {today['Coding'][1]}", key=f"c2_{day_key}_{day}")
        if a1 and a2 and c1 and c2:
            st.success(f"🎉 Day {day} Complete! Great job!")
            if st.button(f"➡️ Go to Day {day+1}", key=f"next_{day_key}_{day}"):
                st.session_state[day_key] += 1
                st.rerun()
        else:
            st.warning("👆 Please complete all 4 topics and tick all boxes to unlock the next day.")
        st.progress(day / 90)
        st.write(f"Progress: Day {day} / 90 - {int(day/90*100)}% Done")

def show_quiz(prefix):
    st.subheader("📝 Daily Quiz - Test Yourself!")
    st.write("5 Questions - Answer all and check score!")
    if f"quiz_q_{prefix}" not in st.session_state:
        st.session_state[f"quiz_q_{prefix}"] = random.sample(QUIZ_DB, 5)
    questions = st.session_state[f"quiz_q_{prefix}"]
    answers = []
    for i, q in enumerate(questions):
        ans = st.radio(f"Q{i+1}. {q['q']}", q["options"], key=f"quiz_{prefix}_{i}")
        answers.append(ans)
    if st.button("✅ Submit Quiz", key=f"submit_{prefix}"):
        score = sum(1 for i, q in enumerate(questions) if answers[i] == q["ans"])
        st.success(f"Your Score: {score} / 5")
        st.progress(score / 5)
        for i, q in enumerate(questions):
            if answers[i] == q["ans"]:
                st.write(f"Q{i+1}: ✅ Correct - {q['ans']}")
            else:
                st.write(f"Q{i+1}: ❌ Wrong. Correct Answer: {q['ans']}")
        if score == 5:
            st.balloons()
            st.success("🏆 Perfect Score! Amazing!")
    if st.button("🔄 New Quiz", key=f"new_{prefix}"):
        st.session_state[f"quiz_q_{prefix}"] = random.sample(QUIZ_DB, 5)
        st.rerun()

def show_notes(prefix):
    st.subheader("📚 Notes - Quick Revision")
    topic = st.selectbox("Select Topic to Read Notes:", list(NOTES_DB.keys()), key=f"notes_{prefix}")
    st.info(NOTES_DB.get(topic, "Notes coming soon!"))
    st.write("**Tip:** After reading Notes, attempt the Quiz to remember better!")

def show_mock_test(prefix):
    st.subheader("🎯 Mock Test - Real Placement Exam Feel!")
    st.write("10 Questions - Aptitude + Coding + SQL. This is like a real company test!")
    if f"mock_q_{prefix}" not in st.session_state:
        st.session_state[f"mock_q_{prefix}"] = MOCK_TEST_DB
    questions = st.session_state[f"mock_q_{prefix}"]
    answers = []
    for i, q in enumerate(questions):
        ans = st.radio(f"Q{i+1}. {q['q']}", q["options"], key=f"mock_{prefix}_{i}")
        answers.append(ans)
    if st.button("🏁 Finish Mock Test", key=f"finish_mock_{prefix}"):
        score = sum(1 for i, q in enumerate(questions) if answers[i] == q["ans"])
        st.success(f"Mock Test Result: {score} / 10")
        st.progress(score / 10)
        if score >= 8:
            st.balloons()
            st.success("🏆 Placement Ready! You can clear any company test!")
        elif score >= 5:
            st.warning("👍 Good! Practice 30 more days to become placement ready.")
        else:
            st.error("📚 Need more practice. Follow the 90-Day Roadmap daily!")
        for i, q in enumerate(questions):
            if answers[i] != q["ans"]:
                st.write(f"Q{i+1}: ❌ Correct Answer: {q['ans']}")

mode = st.radio("Select Your Mode:", ["🎓 Junior (1st & 2nd Year)", "💼 Senior (3rd & 4th Year)"])

prefix = "junior" if "Junior" in mode else "senior"
day_key = "junior_day" if prefix == "junior" else "senior_day"

# --- JUNIOR vs SENIOR TABS ---
if prefix == "junior":
    st.info("👆 Junior Mode: Roadmap, Quiz, Notes, Mock Test - No Resume Scanner for Juniors!")
    tab1, tab2, tab3, tab4 = st.tabs(["📅 Roadmap", "🔍 Resume Scanner", "📝 Quiz", "📚 Notes"])
    with tab1:
        show_roadmap(day_key, "📅 Junior Roadmap - 3 Months / 90 Days!")
    with tab2:
        show_scanner(prefix)
    with tab3:
        show_quiz(prefix)
    with tab4:
        show_notes(prefix)
else:
    st.info("👍 Senior Mode: Roadmap, Resume Scanner, Quiz, Notes - Full Placement Kit!")
    tab1, tab2, tab3, tab4 = st.tabs(["📅 Roadmap", "🔍 Resume Scanner", "📝 Quiz", "📚 Notes"])
    with tab1:
        show_roadmap(day_key, "📅 Senior Roadmap - 3 Months / 90 Days!")
    with tab2:
        show_scanner(prefix)
    with tab3:
        show_quiz(prefix)
    with tab4:
        show_notes(prefix)
