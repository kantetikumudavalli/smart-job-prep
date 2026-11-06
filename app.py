import streamlit as st
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
APTITUDE_TOPICS = ["Time & Work", "Blood Relations", "Percentages", "Profit & Loss", "Number Series", "Coding-Decoding", "Direction Sense", "Ratio & Proportion", "Time Speed Distance", "Probability"]
CODING_TOPICS = ["Variables & Loops", "Arrays & Strings", "Functions", "OOPS Concepts", "Recursion", "Stack & Queue", "Sorting & Searching", "Basic DSA", "Pattern Problems", "Time Complexity"]

mode = st.radio("Select Your Mode:", ["🎓 For Beginners (1st & 2nd Year)", "💼 For Seniors (3rd & 4th Year) - Resume Scanner"])

if mode == "🎓 For Beginners (1st & 2nd Year)":
    st.header("🎓 Beginner Roadmap - Start Here!")
    st.success("Don't get confused! Just follow this 2-track plan for company exams.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧠 Aptitude - Must Practice")
        for topic in APTITUDE_TOPICS:
            st.checkbox(topic, key=f"apt_{topic}")
    with col2:
        st.subheader("💻 Coding Fundamentals")
        for topic in CODING_TOPICS:
            st.checkbox(topic, key=f"code_{topic}")
    st.info("💡 Tip: Daily 1 Aptitude topic + 1 Coding topic = 3 months lo placement ready!")
else:
    st.header("💼 Hiring Readiness Scanner")
    role = st.selectbox("Select Target Role:", list(SKILLS_DB.keys()))
    user_input = st.text_area("Paste Your Skills (comma separated):", placeholder="Ex: Python, SQL, Pandas, Excel...")
    name = st.text_input("Your Name:")
    if st.button("🔍 Check My Readiness"):
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
                st.error("📚 Need to work hard! Start with Beginner Roadmap first.")