import pandas as pd
import json

# Load dataset
df = pd.read_csv("data/UpdatedResumeDataSet.csv", encoding="latin1")

candidates = []

for i, row in df.iterrows():
    text = str(row["Resume"])

    # Basic skill extraction
    skills = []
    for skill in ["Python", "Java", "C++", "Machine Learning", "NLP", "React"]:
        if skill.lower() in text.lower():
            skills.append(skill)

    candidate = {
        "name": f"Candidate_{i}",
        "skills": skills,
        "projects": text[:120],
        "why_hire": text[120:300]
    }

    candidates.append(candidate)

# Save only 20 (stable run)
with open("data/candidates.json", "w") as f:
    json.dump(candidates[:20], f, indent=2)

print("✅ Candidates JSON generated")