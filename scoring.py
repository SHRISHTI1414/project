from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def sim(a, b):
    v = TfidfVectorizer()
    m = v.fit_transform([a, b])
    return cosine_similarity(m[0], m[1])[0][0]

def depth(t):
    t = t.lower()
    s = 0

    actions = ["built", "developed", "implemented", "designed", "deployed"]
    tech = ["machine learning", "ml", "nlp", "model", "api", "pipeline", "dataset"]

    for w in actions:
        if w in t:
            s += 1.5

    for w in tech:
        if w in t:
            s += 1

    return min(s, 6)

def clarity(t):
    n = len(t.split())
    if n > 80:
        return 1
    if n > 40:
        return 0.5
    return 0.2

def uniq(cur, all_t):
    arr = []
    for x in all_t:
        if x == cur:
            continue
        arr.append(sim(cur, x))

    if not arr:
        return 1

    avg = sum(arr) / len(arr)
    return round((1 - avg) * 2, 2)

def run(cands, jd):
    texts = [c["projects"] + " " + c["why_hire"] for c in cands]
    out = []

    for i, c in enumerate(cands):
        txt = texts[i]

        raw = sim(jd, txt)
        relevance = round(min(raw * 20, 10), 2)

        project_depth = depth(txt)
        uniqueness = uniq(txt, texts)
        clarity_score = clarity(txt)

        score = round(
            0.5 * relevance +
            0.3 * project_depth +
            0.15 * uniqueness +
            0.05 * clarity_score,
            2
        )

        out.append({
            "name": c["name"],
            "score": score,
            "parts": {
                "relevance": relevance,
                "project_depth": project_depth,
                "uniqueness": uniqueness,
                "clarity": clarity_score
            }
        })

    return sorted(out, key=lambda x: x["score"], reverse=True)