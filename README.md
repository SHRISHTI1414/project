 # AI Resume Scoring System

## What this is

I built this project to answer a simple question:

> How do you actually identify a *good candidate* from a bunch of resumes?

Most systems just match keywords.
But that doesn’t really work — someone can list 10 skills and still have done nothing real.

So instead of keyword matching, I tried building a **simple but practical scoring system** that looks at:

* how relevant a candidate is to the role
* whether they’ve actually built things
* how different they are from others
* how clearly they present their work

---

## What the system does

The pipeline is pretty straightforward:

```id="s7f1x3"
raw resumes → preprocessing → structured data → scoring → ranking → explanation
```

Each candidate gets:

* a score
* a breakdown of that score
* a short reason explaining why they ranked where they did

Example:

```id="n4j8q2"
Candidate_5 - 2.11

{
  'relevance': 0.45,
  'project_depth': 2,
  'uniqueness': 2.53,
  'clarity': 0.5
}

Reason: unique profile
```

---

## How I approached it

### 1. Data

I used a resume dataset from Kaggle just to get started.
Converted it into a clean JSON format so the scoring system can work on structured input.

Script:

```id="v2l9dp"
preprocess.py
```

---

### 2. Scoring logic

Instead of one metric, I split it into 4 parts:

#### Relevance

* How close is the resume to the job description?
* Used TF-IDF + cosine similarity

#### Project Depth

* Looking for signals like:

  * built
  * developed
  * deployed
  * worked on models / APIs / data

Basically: did they actually *do* something?

#### Uniqueness

* If everyone looks the same, nobody stands out
* So I compare candidates with each other

#### Clarity

* Very simple check — is the resume meaningful or just noise?

---

### Final Score

```id="r6h3k1"
score = weighted combination of all 4 factors
```

Then candidates are ranked.

---

## Explainability (important part)

I didn’t want a black-box score.

So every result includes a reason like:

```id="p9c2l7"
strong JD match
real project work
unique profile
```

This makes it usable from a recruiter’s perspective.

---

## Internshala attempt (real-world test)

I also tried to connect this system to real data (Internshala).

### What I tried:

* sending requests to internship pages
* accessing login routes

### What I observed:

* got HTML responses, not structured data
* login required for deeper access
* dynamic content + session handling

### Conclusion:

You can’t reliably extract data from Internshala without:

* proper API access
* or browser automation

Test scripts:

```id="f3l8kx"
test_internshala.py
test_login.py
```

---

## Problems I ran into

This wasn’t smooth. Some real issues I hit:

* CSV parsing errors (empty file / encoding issues)
* messy resume text
* scoring giving same results for everyone
* difficulty in making the system actually *differentiate* candidates
* real-world data access limitations

Instead of hiding these, I worked through them step by step.

---

## What I learned

A few things became clear while building this:

* good candidates ≠ keyword match
* real signals come from *what people have built*
* data quality matters more than model complexity
* real-world systems fail at integration, not logic

---

## How to run

```id="t4j1w6"
pip install -r requirements.txt
python preprocess.py
python main.py
```

---

## What can be improved

* better NLP (BERT / embeddings instead of TF-IDF)
* smarter project extraction
* real API integration
* feedback loop from recruiters

---

## Final thought

This isn’t a perfect system.

But it’s a practical attempt at:

* building something real
* dealing with messy data
* and thinking like an actual hiring system

That was the goal.

---
