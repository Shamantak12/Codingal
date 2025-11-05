# Mood2Emoji — Kid-safe Text Mood Detector

A simple Streamlit app that takes a short sentence and returns a kid-friendly emoji with a one-line explanation. Made for students aged 12-16. Uses Python, Streamlit, and TextBlob.

---

## What this project does
- Takes a short sentence from the student
- Returns an emoji (😀 😐 😞) plus a simple message like "Sounds happy!"
- Has basic bad-word and link filtering - if something's inappropriate or unclear, it defaults to 😐 neutral
- Teacher Mode toggle in the sidebar shows a simple diagram explaining how it works

---

## How it works

The app is super simple - just type a sentence and get an emoji mood!

### Main Interface

![Main Interface](screenshots/main-interface.png)

The app has a clean interface with:
- A text input box where students type their sentence (max 200 characters)
- A "Check Mood" button to analyze the text
- A sidebar with "Teacher Mode" toggle for educators

### Example: Happy Mood

![Happy Example](screenshots/happy-example.png)

When you type something positive like "i enjoy making food", the app returns:
- 😀 **Sounds happy!**

The app recognizes positive sentiment and responds with a happy emoji.

### Example: Neutral Mood

![Neutral Example](screenshots/neutral-example.png)

For neutral or mixed sentences like "i like dancing", you get:
- 😐 **Feels neutral or mixed.**

The app also shows what you typed back to you for feedback.

### Teacher Mode

When you toggle "Teacher Mode" in the sidebar, you'll see:
- A simple diagram showing the flow: Input → Safety Check → Sentiment Score → Emoji
- An explanation of how TextBlob analyzes sentiment
- Why we chose these tools and thresholds

---

## Demo
- Once deployed on Streamlit Cloud, add your URL here

---

## Setup and run (local)

### 1) Requirements
- Python 3.9+
- pip

### 2) Create & activate a virtual environment (recommended)
```bash
python -m venv .venv
# Windows PowerShell
. .venv\\Scripts\\Activate
# macOS/Linux
# source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run the app
```bash
streamlit run app.py
```
Then open the local URL shown in the terminal (usually `http://localhost:8501`).

---

## How kids learn from it
- **Text → Numbers**: Shows how text can be scored simply (positive/negative/neutral)
- **Rules before AI**: Safety filters and thresholds make the logic explainable - kids can understand it
- **Responsible tech**: Unknown or unkind text becomes neutral by design - teaches safety first
- **Systems thinking**: Teacher Mode diagram helps students see the full flow from input to output

---

## Teach it in 60 minutes (facilitator summary)
- **0–10 min**: Warm‑up. Show examples; ask “What mood is this sentence?”
- **10–25 min**: Explain the flow: input → safety check → sentiment → emoji. Demo Teacher Mode.
- **25–45 min**: Hands‑on. Students try sentences (happy/sad/neutral). Discuss edge cases.
- **45–55 min**: Mini‑challenge. In pairs, tune the thresholds (e.g., ±0.15/±0.25) and predict outcomes.
- **55–60 min**: Wrap‑up. Share takeaways and known limits.

A detailed, student‑friendly plan is in `lesson_plan.md` (export to PDF as `lesson_plan.pdf`).

---

## Known limitations
- TextBlob is pretty simple - it might miss sarcasm or complex tone
- Works best with short, simple English sentences
- No memory - each sentence is judged on its own (no context from previous inputs)
- The bad-word list is intentionally minimal for this demo

---

## References
- TextBlob documentation (`https://textblob.readthedocs.io/en/dev/`)
- Streamlit documentation (`https://docs.streamlit.io/`)

---

## Repo structure
```
repo/
  ├─ app.py             # Streamlit script
  ├─ requirements.txt   # dependencies
  ├─ README.md          # how to run + learning notes
  └─ lesson_plan.md     # export to PDF as lesson_plan.pdf
```

---

## License and originality
Original work for a take‑home assignment. No paid APIs used. Keep repository under 50 MB.



