import json
from scoring import run

jd = """
Python developer with strong experience in Machine Learning, NLP, and data science.
Must have built and deployed ML models, worked with datasets,
developed APIs, and implemented end-to-end AI systems.
"""

with open("data/candidates.json") as f:
    cands = json.load(f)

res = run(cands, jd)

def explain(p):
    r = []

    if p["relevance"] > 6:
        r.append("strong JD match")

    if p["project_depth"] > 2:
        r.append("real project work")

    if p["uniqueness"] > 1.2:
        r.append("unique profile")

    if not r:
        r.append("basic match")

    return ", ".join(r)

print("Ranked Candidates:\n")

for x in res:
    print(x["name"], "-", x["score"])
    print(x["parts"])
    print("Reason:", explain(x["parts"]))
    print("-" * 40)