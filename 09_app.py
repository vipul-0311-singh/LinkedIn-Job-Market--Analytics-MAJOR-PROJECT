import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import pandas as pd


# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("11_Jobs.csv")
    df["Skills"] = df["Skills"].apply(lambda x: [i.strip().lower() for i in x.split(",")])
    return df

jobs = load_data()

# -----------------------------
# UI CONFIG
# -----------------------------
st.set_page_config(page_title="Career Recommendation Engine", layout="centered")

st.title(" Career Recommendation Engine")
st.write("Find the best job role based on your skills and location")

# -----------------------------
# USER INPUT
# -----------------------------
name = st.text_input("Enter Your Name")

location = st.selectbox(
    "Select Preferred Location",
    ["Delhi", "Bangalore", "Mumbai", "Pune", "Hyderabad"]
)

skills_input = st.text_area("Enter Your Skills (comma separated)")

# -----------------------------
# BUTTON
# -----------------------------
if st.button("Get Recommendations"):

    if not skills_input:
        st.warning("Please enter your skills")
    else:

        user_skills = [s.strip().lower() for s in skills_input.split(",")]

        results = []

        # -------------------------
        # Recommendation Logic
        # -------------------------
        for _, job in jobs.iterrows():

            required = job["Skills"]

            matched = set(user_skills) & set(required)
            missing = list(set(required) - set(user_skills))

            score = int((len(matched) / len(required)) * 100)

            location_bonus = 10 if location.lower() == job["Location"].lower() else 0

            final_score = min(score + location_bonus, 100)

            results.append({
                "Job Role": job["Job Role"],
                "Score": final_score,
                "Missing Skills": ", ".join(missing) if missing else "None",
                "Salary": job["Salary"],
                "Location": job["Location"],
                "Demand": job["Demand"]
            })

        # Sort
        results = sorted(results, key=lambda x: x["Score"], reverse=True)

        st.subheader("🏆 Top Recommendations")

        # Top 5
        for r in results[:5]:

            st.markdown("---")

            st.write(f"### {r['Job Role']}")
            st.write(f"📍 Location: {r['Location']}")
            st.write(f"📊 Match Score: {r['Score']}%")
            st.write(f"💰 Salary: {r['Salary']}")
            st.write(f"🔥 Demand: {r['Demand']}")
            st.write(f"🧠 Missing Skills: {r['Missing Skills']}")

        # Career readiness
        best_score = results[0]["Score"]

        st.subheader("📌 Career Readiness")

        if best_score >= 90:
            st.success(f"Job Ready ✅ (Score: {best_score}/100)")
        elif best_score >= 70:
            st.info(f"Almost Ready ⚡ (Score: {best_score}/100)")
        else:
            st.warning(f"Need Upskilling 📚 (Score: {best_score}/100)")

        # Learning suggestions
        st.subheader("📚 Learning Suggestions")

        roadmap = {
            "python": "Python Basics + Projects",
            "sql": "SQL Practice (Joins, Queries)",
            "excel": "Advanced Excel",
            "power bi": "Power BI Dashboards",
            "django": "Django Backend Development",
            "git": "Git & GitHub",
            "rest api": "REST API Development",
            "pandas": "Pandas for Data Analysis",
            "numpy": "NumPy Basics",
            "scikit-learn": "Machine Learning Basics",
        }

        missing_skills = results[0]["Missing Skills"].lower().split(",")

        for skill in missing_skills:
            skill = skill.strip()
            if skill in roadmap:
                st.write(f"👉 {skill.title()} → {roadmap[skill]}")