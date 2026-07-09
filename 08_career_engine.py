import csv

# ------------------------------
# Load Job Data
# ------------------------------

jobs = []

with open("11_Jobs.csv", "r") as file:
    
    reader = csv.DictReader(file)

    for row in reader:
        row["Skills"] = [skill.strip().lower() for skill in row["Skills"].split(",")]
        jobs.append(row)

print("=" * 50)
print("      CAREER RECOMMENDATION ENGINE")
print("=" * 50)

# ------------------------------
# User Input
# ------------------------------

name = input("Enter Your Name : ")

location = input("Enter Preferred Location : ").strip().lower()

skills = input("Enter Your Skills (comma separated): ")

user_skills = [skill.strip().lower() for skill in skills.split(",")]

print("\nFinding Best Career...\n")

results = []

# ------------------------------
# Recommendation Logic
# ------------------------------

for job in jobs:

    required = job["Skills"]

    matched = set(user_skills) & set(required)

    missing = list(set(required) - set(user_skills))

    score = int((len(matched) / len(required)) * 100)

    location_bonus = 10 if location == job["Location"].lower() else 0

    final_score = min(score + location_bonus, 100)

    results.append({

        "Job": job["Job Role"],

        "Score": final_score,

        "Missing": missing,

        "Salary": job["Salary"],

        "Location": job["Location"]

    })

# ------------------------------
# Sort Results
# ------------------------------

results.sort(key=lambda x: x["Score"], reverse=True)

print("=" * 60)
print("TOP 3 CAREER RECOMMENDATIONS")
print("=" * 60)

for job in results[:3]:

    print("\nJob Role :", job["Job"])

    print("Location :", job["Location"])

    print("Match Score :", str(job["Score"]) + "%")

    print("Expected Salary :", job["Salary"])

    if len(job["Missing"]) == 0:
        print("Missing Skills : None")
    else:
        print("Missing Skills :", ", ".join(job["Missing"]))

    print("-" * 60)

# ------------------------------
# Career Readiness
# ------------------------------

best = results[0]["Score"]

print("\nCareer Readiness Report")

print("-" * 30)

if best >= 90:
    print("Status : Job Ready")
elif best >= 70:
    print("Status : Almost Ready")
elif best >= 50:
    print("Status : Need Upskilling")
else:
    print("Status : Beginner")

print("Overall Career Score :", str(best) + "/100")

# ------------------------------
# Learning Suggestions
# ------------------------------

roadmap = {

    "python": "Python Crash Course",

    "sql": "SQL Basics",

    "excel": "Advanced Excel",

    "power bi": "Power BI Dashboard",

    "django": "Django Web Development",

    "git": "Git & GitHub",

    "rest api": "REST API Fundamentals",

    "communication": "Business Communication",

    "pandas": "Pandas for Data Analysis",

    "numpy": "NumPy Essentials",

    "scikit-learn": "Machine Learning Basics"

}

print("\nRecommended Learning")

print("-" * 30)

for skill in results[0]["Missing"]:

    print(skill.title(), " --> ", roadmap.get(skill, "Learn Online"))

print("\nThank You,", name)